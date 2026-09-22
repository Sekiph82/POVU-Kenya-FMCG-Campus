param(
  [Parameter(Mandatory=$true)][int]$Video,
  [Parameter(Mandatory=$true)][string]$OutputDir,
  [Parameter(Mandatory=$true)][string]$Manifest,
  [Parameter(Mandatory=$true)][string]$RepoRoot,
  [Parameter(Mandatory=$true)][string]$RenderTime
)
$ErrorActionPreference = 'Stop'
$specs = Get-Content $Manifest -Raw | ConvertFrom-Json
$spec = @($specs.videos | Where-Object { $_.id -eq $Video })[0]
if (-not $spec) { throw "Video $Video missing from manifest" }
$out = (Resolve-Path $OutputDir).Path
$mp4 = Join-Path $out ("POVU_VID_{0:000}_{1}_30s.mp4" -f $Video, $spec.slug)
$frames = Join-Path $out 'frames/frame_%04d.jpg'
& ffmpeg -y -loglevel error -framerate 24 -i $frames -c:v libx264 -pix_fmt yuv420p -movflags +faststart $mp4
if ($LASTEXITCODE -ne 0) { throw "ffmpeg encode failed for VIDEO-$Video" }
$qa = Join-Path $out 'final_qa'
New-Item -ItemType Directory -Force $qa | Out-Null
$times = @(@{t='0';n='01'},@{t='5';n='02'},@{t='10';n='03'},@{t='15';n='04'},@{t='20';n='05'},@{t='25';n='06'},@{t='29.9';n='07'})
foreach ($item in $times) {
  & ffmpeg -y -loglevel error -ss $item.t -i $mp4 -frames:v 1 (Join-Path $qa ("final_" + $item.n + '.png'))
  if ($LASTEXITCODE -ne 0) { throw "Final QA extraction failed for VIDEO-$Video at $($item.t)s" }
}
& ffprobe -v error -show_format -show_streams -of json $mp4 | Set-Content -Encoding utf8 (Join-Path $out 'final_ffprobe.json')
if ($LASTEXITCODE -ne 0) { throw "ffprobe failed for VIDEO-$Video" }
(Get-FileHash -Algorithm SHA256 $mp4).Hash | Set-Content -Encoding ascii (Join-Path $out 'final_sha256.txt')
Write-Output "FINALIZED VIDEO-$Video $mp4"
