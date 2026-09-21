param(
  [Parameter(Mandatory=$true)][string]$Video,
  [Parameter(Mandatory=$true)][string]$QaDir,
  [Parameter(Mandatory=$true)][string]$Metadata
)
$ErrorActionPreference = 'Stop'
$videoPath = (Resolve-Path -LiteralPath $Video).Path
$qaPath = (Resolve-Path -LiteralPath $QaDir).Path
$probePath = Join-Path $qaPath 'ffprobe.json'
$validationPath = Join-Path $qaPath 'validation.json'
$contactPath = Join-Path $qaPath 'contact_sheet.png'
& ffprobe.exe -v error -print_format json -show_format -show_streams $videoPath | Set-Content -LiteralPath $probePath -Encoding utf8
$probe = Get-Content -Raw $probePath | ConvertFrom-Json
$stream = @($probe.streams | Where-Object {$_.codec_type -eq 'video'})[0]
$duration = [double]$probe.format.duration
$fpsText = [string]$stream.avg_frame_rate
$fps = if ($fpsText -match '^([0-9]+)/([0-9]+)$') {[double]$Matches[1] / [double]$Matches[2]} else {[double]$fpsText}
$size = (Get-Item -LiteralPath $videoPath).Length
$sha = (Get-FileHash -LiteralPath $videoPath -Algorithm SHA256).Hash.ToLowerInvariant()
$checks = [ordered]@{
  exists = (Test-Path -LiteralPath $videoPath)
  nonzero = ($size -gt 0)
  duration_approximately_30s = ([math]::Abs($duration - 30.0) -le 0.25)
  resolution_1280x720 = ([int]$stream.width -eq 1280 -and [int]$stream.height -eq 720)
  fps_24 = ([math]::Abs($fps - 24.0) -le 0.01)
  codec_h264 = ([string]$stream.codec_name -eq 'h264')
  probeable = $true
}
& ffmpeg.exe -y -hide_banner -loglevel error -ss 0 -i $videoPath -frames:v 1 (Join-Path $qaPath 'begin_probe.png')
& ffmpeg.exe -y -hide_banner -loglevel error -ss 15 -i $videoPath -frames:v 1 (Join-Path $qaPath 'middle_probe.png')
& ffmpeg.exe -y -hide_banner -loglevel error -ss 29 -i $videoPath -frames:v 1 (Join-Path $qaPath 'end_probe.png')
& ffmpeg.exe -y -hide_banner -loglevel error -i (Join-Path $qaPath 'begin_probe.png') -i (Join-Path $qaPath 'middle_probe.png') -i (Join-Path $qaPath 'end_probe.png') -filter_complex 'hstack=inputs=3' -frames:v 1 $contactPath
$result = [ordered]@{
  video = $videoPath
  bytes = $size
  sha256 = $sha
  duration_seconds = $duration
  width = [int]$stream.width
  height = [int]$stream.height
  fps = $fps
  codec = [string]$stream.codec_name
  checks = $checks
  metadata = (Get-Content -Raw -LiteralPath $Metadata | ConvertFrom-Json)
  qa_frames = @((Join-Path $qaPath 'begin_probe.png'),(Join-Path $qaPath 'middle_probe.png'),(Join-Path $qaPath 'end_probe.png'),$contactPath)
}
$result | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $validationPath -Encoding utf8
$result | ConvertTo-Json -Depth 10
if (@($checks.Values | Where-Object {$_ -eq $false}).Count -gt 0) { exit 2 }
