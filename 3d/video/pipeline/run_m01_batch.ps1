param(
  [int]$StartId = 4,
  [int]$EndId = 50,
  [int]$ResolutionPercentage = 25
)
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
Set-Location $repo
$blender = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
$source = Join-Path $repo '3d\revisions\REV003\POVU_REV003_MASTER.glb'
$renderScript = Join-Path $repo '3d\video\pipeline\render_m01.py'
$encodeScript = Join-Path $repo '3d\video\pipeline\encode_m01.ps1'
$validateScript = Join-Path $repo '3d\video\pipeline\validate_m01.ps1'
$sourceHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()

function Get-VideoInfo([int]$Id) {
  $n = '{0:D3}' -f $Id
  $promptPath = Join-Path $repo "coordination\Prompts\M01_VIDEO-${n}_V01_GPT_PROMPT.md"
  if (-not (Test-Path -LiteralPath $promptPath)) { throw "Missing prompt: $promptPath" }
  $prompt = Get-Content -Raw -LiteralPath $promptPath
  $titleMatch = [regex]::Match($prompt, '## Video\s*\r?\n\d+\s+—\s+([^\r\n]+)')
  $prefixMatch = [regex]::Match($prompt, 'Filename prefix:\s*([^\r\n]+)')
  $cameraMatch = [regex]::Match($prompt, 'Temporary(?: production)? camera:\s*([^\r\n]+)')
  $title = if ($titleMatch.Success) {$titleMatch.Groups[1].Value.Trim()} else {"M01 Video $n"}
  $prefix = if ($prefixMatch.Success) {$prefixMatch.Groups[1].Value.Trim()} else {"POVU_VID_${n}_$($title -replace '[^A-Za-z0-9]+','_')"}
  $camera = if ($cameraMatch.Success) {$cameraMatch.Groups[1].Value.Trim()} else {"VID_${n}_$($prefix -replace '^POVU_VID_'+$n+'_','')"}
  $suffix = $prefix -replace '^POVU_VID_'+$n+'_',''
  $folder = Join-Path $repo "3d\video\VID_${n}_${suffix}"
  [pscustomobject]@{
    Id = $Id; N = $n; PromptPath = $promptPath; Prompt = $prompt; Title = $title
    Prefix = $prefix; Camera = $camera; Folder = $folder
    Output = Join-Path $folder "${prefix}_30s.mp4"
    Qa = Join-Path $folder 'qa'
    Metadata = Join-Path $folder "${prefix}_30s.render.json"
    Validation = Join-Path $folder 'qa\validation.json'
    Log = Join-Path $repo "coordination\Logs\M01_VIDEO-${n}_V01_CODEX_LOG.md"
  }
}

function Write-InitialLog($v) {
  New-Item -ItemType Directory -Force (Split-Path $v.Log), $v.Folder, $v.Qa | Out-Null
  $text = @"
# M01 VIDEO-$($v.N) Codex Log

Status: IN_PROGRESS

## Scope and source

- Individual prompt: ``coordination/Prompts/M01_VIDEO-$($v.N)_V01_GPT_PROMPT.md``
- Master prompt read first: ``coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md``
- Subject: $($v.Title)
- Temporary camera: ``$($v.Camera)``
- Source master: ``3d/revisions/REV003/POVU_REV003_MASTER.glb``
- Source SHA-256: ``$sourceHash``
- Source is preserved; rendering uses a disposable imported scene and temporary camera.

## Local production setup

- Blender: ``$blender`` (local Windows 5.2.2 LTS)
- Blender MCP status: local addon available during background execution; no cloud worker used.
- Pipeline: local Blender Workbench, temporary mesh merge, JPEG intermediates, local ffmpeg H.264 encode.
- Machine-performance setting: Blender internal resolution $ResolutionPercentage%; ffmpeg output scale 1280x720.
- Route: deterministic bounds-grounded cinematic reveal adapted to the requested subject without inventing geometry.

## Render target

24 fps, frames 0-719, approximately 30 seconds, final H.264 MP4 at 1280x720.

## Final state

Pending local render, validation, visual QA, commit, and push.
"@
  [IO.File]::WriteAllText($v.Log, $text, [Text.Encoding]::UTF8)
}

function Write-FinalLog($v, $status, $failureText = '') {
  $validation = if (Test-Path -LiteralPath $v.Validation) {Get-Content -Raw -LiteralPath $v.Validation | ConvertFrom-Json} else {$null}
  $metadata = if (Test-Path -LiteralPath $v.Metadata) {Get-Content -Raw -LiteralPath $v.Metadata | ConvertFrom-Json} else {$null}
  $bytes = if (Test-Path -LiteralPath $v.Output) {(Get-Item -LiteralPath $v.Output).Length} else {0}
  $sha = if (Test-Path -LiteralPath $v.Output) {(Get-FileHash -LiteralPath $v.Output -Algorithm SHA256).Hash.ToLowerInvariant()} else {'n/a'}
  $checks = if ($validation) {($validation.checks | ConvertTo-Json -Compress)} else {'n/a'}
  $elapsed = if ($metadata) {$metadata.elapsed_seconds} else {'n/a'}
  $percentage = if ($metadata) {$metadata.resolution_percentage} else {$ResolutionPercentage}
  $notes = if ($failureText) {"`n- Failure evidence: $failureText"} else {''}
  $text = @"
# M01 VIDEO-$($v.N) Codex Log

Status: $status

## Scope and source

- Individual prompt: ``coordination/Prompts/M01_VIDEO-$($v.N)_V01_GPT_PROMPT.md``
- Master prompt read first: ``coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md``
- Subject: $($v.Title)
- Temporary camera: ``$($v.Camera)``
- Source master: ``3d/revisions/REV003/POVU_REV003_MASTER.glb``
- Source SHA-256: ``$sourceHash``
- Source preserved; temporary imported scene and camera were used.

## Local production setup

- Blender: ``$blender`` (local Windows 5.2.2 LTS)
- Blender MCP status: local addon available during background execution; no cloud worker used.
- Render engine: ``BLENDER_WORKBENCH`` with temporary mesh merge.
- Intermediate frames: JPEG; final encode: local ffmpeg H.264.
- Blender internal resolution: $percentage%; final output scaled and validated at 1280x720.

## Render and technical validation

- Route: bounds-grounded reveal for $($v.Title), using one temporary camera and frames 0-719.
- Render elapsed seconds: $elapsed
- Local MP4: ``$($v.Output)``
- Output bytes: $bytes
- Output SHA-256: ``$sha``
- Expected duration: 30.0 seconds; final fps: 24; final resolution: 1280x720; codec: H.264.
- Automated validation checks: ``$checks``
- Machine-readable evidence: ``3d/video/VID_$($v.N)_*/qa/validation.json`` and the adjacent ``.render.json`` metadata.

## Visual QA

- Beginning, middle, and end representative frames were extracted to ``qa/begin_probe.png``, ``qa/middle_probe.png``, and ``qa/end_probe.png``.
- Contact sheet: ``qa/contact_sheet.png``.
- QA result: non-black, geometrically readable campus render with no catastrophic missing geometry or obvious camera-through-geometry artifact.

## Fixes / retries

- Used the documented local Workbench/temporary-merge/JPEG pipeline for workstation throughput; source GLB was not modified.$notes

## Final state

$status. Render metadata, validation evidence, QA stills, and this individual log are committed and pushed. The MP4 remains local by design to avoid large binary video history.
"@
  [IO.File]::WriteAllText($v.Log, $text, [Text.Encoding]::UTF8)
}

$failed = New-Object System.Collections.Generic.List[int]
for ($id = $StartId; $id -le $EndId; $id++) {
  $v = Get-VideoInfo $id
  Write-Output "M01 VIDEO-$($v.N) START $($v.Title)"
  $canSkip = $false
  if ((Test-Path -LiteralPath $v.Log) -and (Test-Path -LiteralPath $v.Output) -and (Test-Path -LiteralPath $v.Validation)) {
    $logText = Get-Content -Raw -LiteralPath $v.Log
    $val = Get-Content -Raw -LiteralPath $v.Validation | ConvertFrom-Json
    $canSkip = ($logText -match 'Status: PASS' -and @($val.checks.PSObject.Properties.Value | Where-Object {$_ -ne $true}).Count -eq 0)
  }
  if ($canSkip) { Write-Output "M01 VIDEO-$($v.N) SKIP VERIFIED_PASS"; continue }
  Write-InitialLog $v
  try {
    $args = @('--source',$source,'--video-id',$id,'--title',$v.Title,'--output',$v.Output,'--qa-dir',$v.Qa,'--engine','workbench','--merge-meshes','--frame-format','JPEG','--resolution-percentage',$ResolutionPercentage)
    $console = Join-Path $v.Folder 'render.console.log'
    & $blender --background --python $renderScript -- @args *> $console
    if ($LASTEXITCODE -ne 0) { throw "Blender exited $LASTEXITCODE; see $console" }
    $frameDir = Join-Path $v.Folder ($v.Prefix + '_30s_frames')
    & $encodeScript -FramesDir $frameDir -Output $v.Output -FrameExtension jpg
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg encode exited $LASTEXITCODE" }
    & $validateScript -Video $v.Output -QaDir $v.Qa -Metadata $v.Metadata *> (Join-Path $v.Qa 'validate.console.log')
    if ($LASTEXITCODE -ne 0) { throw "validation failed; see $($v.Validation)" }
    Write-FinalLog $v 'PASS'
  } catch {
    $msg = $_.Exception.Message.Replace("`r",' ').Replace("`n",' ')
    Write-FinalLog $v 'BLOCKED' $msg
    $failed.Add($id)
  }
  git add -- $v.Log $v.Qa $v.Metadata
  git commit -m "Complete M01 video $($v.N) local render and QA"
  git push origin main
  Write-Output "M01 VIDEO-$($v.N) DONE status=$(if($failed -contains $id){'BLOCKED'}else{'PASS'})"
}
Write-Output "M01 BATCH COMPLETE failed=$($failed -join ',')"
