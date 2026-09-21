# POVU M01 local Blender pipeline

`render_m01.py` is the reusable one-video-at-a-time renderer for M01. It imports the preserved REV003 GLB into a temporary Blender process, creates only the requested production camera, and renders 720 high-quality JPEG frames at 24 fps in local Blender Eevee or Workbench. `encode_m01.ps1` then encodes those local render frames into the required H.264 MP4 with the installed local ffmpeg.

Example from PowerShell:

```powershell
$blender = 'C:\Program Files\Blender Foundation\Blender 5.2\blender.exe'
& $blender --background --python 3d/video/pipeline/render_m01.py -- `
  --source 3d/revisions/REV003/POVU_REV003_MASTER.glb `
  --video-id 1 `
  --title 'POVU Campus Aerial' `
  --output 3d/video/VID_001_POVU_Campus_Aerial/POVU_VID_001_POVU_Campus_Aerial_30s.mp4 `
  --qa-dir 3d/video/VID_001_POVU_Campus_Aerial/qa `
  --engine workbench `
  --merge-meshes `
  --frame-format JPEG
```

The source GLB is never opened for saving. The temporary `.blend` archive and `.render.json` metadata are written next to the requested output. The runner is restartable: run one video in a fresh Blender process and use the individual Codex log plus output metadata to decide whether an existing result is a genuine PASS.

Technical target: 1280x720, 24 fps, frames 0-719, 30 seconds, H.264 MP4, Eevee or the documented local Workbench fallback. Blender 5.2’s headless build cannot assign its exposed FFMPEG image enum, so the intermediate-frame plus local-ffmpeg path is intentional.

For this 1,898-object GLB, the production run merges only the temporary imported mesh objects inside the disposable render scene. The source GLB is unchanged. Workbench was benchmarked locally because full-resolution Eevee took about 2.5 seconds per frame even after merging, while Workbench produced the same-resolution representative geometry in a fraction of that time. The engine choice and benchmark are recorded in each individual log.
