# M01 VIDEO-003 Codex Log

Status: PASS

## Scope and source

- Individual prompt: `coordination/Prompts/M01_VIDEO-003_V01_GPT_PROMPT.md`
- Master prompt read first: `coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md`
- Subject: People & Employee Campus
- Temporary camera: `VID_003_People_Employee_Campus`
- Source master: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Source SHA-256: `033337f2fcd54e1166a2ca5560c5779fcdd96a55589ef84c6f72b3155ab5dd1d`
- Source is preserved; rendering uses a disposable imported scene.

## Local production setup

- Blender: `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (local Windows 5.2.2 LTS)
- Blender MCP status: local addon available during background execution; no cloud worker used.
- Pipeline: local Blender Workbench, temporary mesh merge, JPEG intermediates, local ffmpeg H.264 encode.
- Machine-performance setting: Blender internal resolution 25%; ffmpeg output scale 1280x720. This is recorded in render metadata and is subject to the native output validation gate.
- Route: bounds-grounded campus reveal adapted to the employee-campus subject without inventing geometry.

## Render target

24 fps, frames 0-719, approximately 30 seconds, final H.264 MP4 at 1280x720.

- Render engine: `BLENDER_WORKBENCH`; temporary imported mesh objects merged only in the disposable scene.
- Blender internal resolution: 25%; local ffmpeg upscaled the encoded output to the required 1280x720.
- Render elapsed: 168.299 seconds.
- Local MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\VID_003_People_Employee_Campus\POVU_VID_003_People_Employee_Campus_30s.mp4`
- MP4 size: 7,331,851 bytes.
- MP4 SHA-256: `e329f071dd731b34e1e20e6d0961ceb27b2e3c0e862d24f6d24552639ae03c37`
- ffprobe: duration `30.0 s`; resolution `1280x720`; fps `24.0`; codec `h264`; probeable and non-zero.
- All automated checks passed. Evidence is in `3d/video/VID_003_People_Employee_Campus/qa/validation.json`, `ffprobe.json`, and the render metadata JSON.

## Visual QA

- Beginning: full campus context is visible without a black frame.
- Middle: employee-campus approach remains readable as architectural massing and campus landscape.
- End: closer hero view remains geometrically coherent with no camera-through-geometry artifact or catastrophic missing geometry.
- Evidence: `qa/begin_probe.png`, `qa/middle_probe.png`, `qa/end_probe.png`, and `qa/contact_sheet.png`.

## Fixes / retries

No video-specific retry was required. The documented 25% intermediate render/upscale was used for local throughput; final technical validation remained native 1280x720.

## Final state

Final: PASS. MP4 remains local by design; render metadata, validation evidence, and representative QA stills are committed. Continue automatically to VIDEO-004.
