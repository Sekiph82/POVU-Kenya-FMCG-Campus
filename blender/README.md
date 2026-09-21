# Blender Render Pipeline

POVU presentation videos are rendered with Blender rather than the 3D Jutsu Python worker.

Video 01 uses `.github/workflows/render-video01.yml` and `blender/render_video01.py`.
Target: 30 seconds, 24 fps, 1280x720, H.264 MP4.

The workflow selects the newest GLB under `3d/`. A current clean-master GLB must be committed before the workflow can render. It imports the GLB, builds the aerial camera route, renders the MP4, validates it with ffprobe, and uploads the MP4 and render BLEND as an Actions artifact.
