# M01 VIDEO-001 Codex Log

Status: PASS

## Scope and source

- Individual prompt: `coordination/Prompts/M01_VIDEO-001_V01_GPT_PROMPT.md`
- Master prompt read first: `coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md`
- Subject: POVU Campus Aerial
- Temporary camera: `VID_001_POVU_Campus_Aerial`
- Source master: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Source origin: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d-jutsu-POVU-Kenya-Integrated-Manufacturing-Camp-2026-09-20-22-10-57.glb`
- Source SHA-256: `033337f2fcd54e1166a2ca5560c5779fcdd96a55589ef84c6f72b3155ab5dd1d`
- Source was copied and rendered from a disposable imported scene; it was not overwritten.

## Local production setup

- Machine: Windows local workstation
- Blender: `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe` (5.2.2 LTS)
- Blender MCP status: addon registered during local background execution; production did not use a cloud worker.
- Render pipeline: `3d/video/pipeline/render_m01.py` with `--merge-meshes --engine workbench`, followed by local `ffmpeg` H.264 encoding.
- Engine decision: full-resolution Eevee was benchmarked at about 2.5 seconds/frame after merge; Workbench produced clean representative geometry much faster and is documented as the local-machine production fallback.

## Render target and route

- Target: 1280x720, 24 fps, frames 0-719, approximately 30 seconds, H.264 MP4.
- Route: broad aerial campus context, controlled approach, closer campus/plaza relationship reveal, and final hero hold; camera coordinates are recorded in the render metadata JSON.

## Render / validation

- Render completed locally with Blender 5.2.2 LTS using `BLENDER_WORKBENCH`; temporary imported meshes were merged only inside the disposable render scene.
- Render elapsed: 462.007 seconds.
- Frame range: 0-719; expected duration: 30.0 seconds.
- Local MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\VID_001_POVU_Campus_Aerial\POVU_VID_001_POVU_Campus_Aerial_30s.mp4`
- MP4 size: 7,792,463 bytes.
- MP4 SHA-256: `0897ee3ecd3e8c0ced568f8caf414aec295643eec371c8585772a1a1fcc39837`
- ffprobe: duration `30.0 s`; resolution `1280x720`; fps `24.0`; codec `h264`; probeable `true`; non-zero `true`.
- All automated technical checks passed. Full machine-readable evidence is in `3d/video/VID_001_POVU_Campus_Aerial/qa/validation.json`, with source/camera/render metadata in `POVU_VID_001_POVU_Campus_Aerial_30s.render.json`.

## Visual QA

Beginning: broad campus context is fully visible with strong architectural silhouette and no black frame.
Middle: controlled approach retains campus/plaza relationship and readable building/landscape geometry.
End: closer hero composition remains geometrically readable; edge crops are intentional approach framing, with no camera-through-geometry artifact or catastrophic missing geometry.
QA evidence: `qa/begin_probe.png`, `qa/middle_probe.png`, `qa/end_probe.png`, and `qa/contact_sheet.png`.

## Fixes / retries

- Initial Blender 5.2 movie-output attempt failed because the headless build rejected assigning its exposed `FFMPEG` image enum. The reusable pipeline was corrected to render PNG frames and encode them with installed local ffmpeg.
- Preview render confirmed the imported scene and route are visible before the production render.
- Fixed Blender 5.2 movie-output incompatibility by using local PNG frame output and local ffmpeg H.264 encoding.

## Final state

Final: PASS. MP4 remains local and is intentionally not committed because the repository workflow tracks render metadata and QA evidence while avoiding large binary video history. The individual log, render metadata, validation JSON, and representative QA stills are committed and pushed.

Next action: continue automatically to VIDEO-002 after this log checkpoint.
