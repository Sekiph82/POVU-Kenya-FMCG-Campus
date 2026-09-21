# M01 VIDEO-010 Codex Log

Status: PASS

## Scope and source

- Individual prompt: `coordination/Prompts/M01_VIDEO-010_V01_GPT_PROMPT.md`
- Master prompt read first: `coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md`
- Subject: Occupational Health Centre
- Temporary camera: `VID_010_Occupational_Health_Centre`
- Source master: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Source SHA-256: `033337f2fcd54e1166a2ca5560c5779fcdd96a55589ef84c6f72b3155ab5dd1d`
- Source preserved; temporary imported scene and camera were used.

## Local production setup

- Blender: `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (local Windows 5.2.2 LTS)
- Blender MCP status: local addon available during background execution; no cloud worker used.
- Render engine: `BLENDER_WORKBENCH` with temporary mesh merge.
- Intermediate frames: JPEG; final encode: local ffmpeg H.264.
- Blender internal resolution: 25%; final output scaled and validated at 1280x720.

## Render and technical validation

- Route: bounds-grounded reveal for Occupational Health Centre, using one temporary camera and frames 0-719.
- Render elapsed seconds: 49.26
- Local MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\VID_010_Occupational_Health_Centre\POVU_VID_010_Occupational_Health_Centre_30s.mp4`
- Output bytes: 9475248
- Output SHA-256: `28ba2fada2444b2f927e281787710ffed88c1fdc3a239d8d31a79966bb90e331`
- Expected duration: 30.0 seconds; final fps: 24; final resolution: 1280x720; codec: H.264.
- Automated validation checks: `{"exists":true,"nonzero":true,"duration_approximately_30s":true,"resolution_1280x720":true,"fps_24":true,"codec_h264":true,"probeable":true}`
- Machine-readable evidence: `3d/video/VID_010_*/qa/validation.json` and the adjacent `.render.json` metadata.

## Visual QA

- Beginning, middle, and end representative frames were extracted to `qa/begin_probe.png`, `qa/middle_probe.png`, and `qa/end_probe.png`.
- Contact sheet: `qa/contact_sheet.png`.
- QA result: non-black, geometrically readable campus render with no catastrophic missing geometry or obvious camera-through-geometry artifact.

## Fixes / retries

- Used the documented local Workbench/temporary-merge/JPEG pipeline for workstation throughput; source GLB was not modified.

## Final state

PASS. Render metadata, validation evidence, QA stills, and this individual log are committed and pushed. The MP4 remains local by design to avoid large binary video history.