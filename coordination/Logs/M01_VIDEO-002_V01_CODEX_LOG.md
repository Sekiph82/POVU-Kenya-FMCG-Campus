# M01 VIDEO-002 Codex Log

Status: PASS

## Scope and source

- Individual prompt: `coordination/Prompts/M01_VIDEO-002_V01_GPT_PROMPT.md`
- Master prompt read first: `coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md`
- Subject: Main Entrance & POVU Plaza
- Temporary camera: `VID_002_Main_Entrance_POVU_Plaza`
- Source master: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Source SHA-256: `033337f2fcd54e1166a2ca5560c5779fcdd96a55589ef84c6f72b3155ab5dd1d`
- Source is preserved; rendering uses a disposable imported scene and never overwrites the GLB.

## Local production setup

- Blender: `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (local Windows 5.2.2 LTS)
- Blender MCP status: local addon available during background execution; no cloud worker used.
- Pipeline: `3d/video/pipeline/render_m01.py --engine workbench --merge-meshes --frame-format JPEG`, then local `encode_m01.ps1` and `validate_m01.ps1`.
- Route: deterministic bounds-grounded campus reveal with broad context, controlled approach, closer plaza/entrance framing, and final hero hold.

## Render target

1280x720, 24 fps, frames 0-719, approximately 30 seconds, H.264 MP4.

- Render engine: `BLENDER_WORKBENCH` with merged temporary imported meshes.
- Render elapsed: 312.171 seconds.
- Local MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\VID_002_Main_Entrance_POVU_Plaza\POVU_VID_002_Main_Entrance_POVU_Plaza_30s.mp4`
- MP4 size: 8,573,488 bytes.
- MP4 SHA-256: `b5480f9b25830ae9657b9b6383e5ac15febdd1dad145d5d2b5efdf8bff1f0d75`
- ffprobe: duration `30.0 s`; resolution `1280x720`; fps `24.0`; codec `h264`; probeable and non-zero.
- All automated checks passed. Evidence: `3d/video/VID_002_Main_Entrance_POVU_Plaza/qa/validation.json`, `ffprobe.json`, and the render metadata JSON.

## Visual QA

- Beginning: broad approach keeps the full campus readable and establishes the entrance/plaza-side relationship.
- Middle: controlled move toward the central frontage remains geometrically readable with no black frame.
- End: close hero view shows the plaza-side building frontage and landscape elements without camera-through-geometry artifacts or catastrophic missing geometry.
- Evidence: `qa/begin_probe.png`, `qa/middle_probe.png`, `qa/end_probe.png`, and `qa/contact_sheet.png`.

## Fixes / retries

The production pipeline now uses high-quality JPEG intermediates because Blender 5.2 headless rejects its exposed FFMPEG image enum and PNG compression was the dominant local bottleneck. Final output remains H.264 MP4.

## Final state

Final: PASS. The MP4 remains local by design; render metadata, validation evidence, and representative QA stills are committed. Continue automatically to VIDEO-003.
