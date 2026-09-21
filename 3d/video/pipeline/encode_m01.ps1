param(
  [Parameter(Mandatory=$true)][string]$FramesDir,
  [Parameter(Mandatory=$true)][string]$Output,
  [ValidateSet('png','jpg')][string]$FrameExtension = 'jpg'
)
$ErrorActionPreference = 'Stop'
$framesPath = (Resolve-Path -LiteralPath $FramesDir).Path
$outputPath = [System.IO.Path]::GetFullPath($Output)
$first = Join-Path $framesPath ("frame_0000.{0}" -f $FrameExtension)
if (-not (Test-Path -LiteralPath $first)) { throw "Missing first rendered frame: $first" }
& ffmpeg.exe -y -hide_banner -loglevel error -framerate 24 -i (Join-Path $framesPath ("frame_%04d.{0}" -f $FrameExtension)) -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -movflags +faststart $outputPath
if ($LASTEXITCODE -ne 0) { throw "ffmpeg encoding failed with exit code $LASTEXITCODE" }
if (-not (Test-Path -LiteralPath $outputPath)) { throw "ffmpeg did not create $outputPath" }
Get-Item -LiteralPath $outputPath | Select-Object FullName,Length
