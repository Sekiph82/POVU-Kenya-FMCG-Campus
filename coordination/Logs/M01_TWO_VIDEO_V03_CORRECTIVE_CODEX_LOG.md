# POVU M01 — Two-Video V03 Corrective Render Log

## Status

**PASS — exactly two corrective videos rendered and validated.**

This run was deliberately limited to:

1. VIDEO 01 — Wet Processing / Mixing Hall
2. VIDEO 03 — POVU Glass Deck

Hands of Growth and Color & Materials Proof were not rerendered. Existing V02 outputs were not overwritten.

## Source integrity

- Source: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Required source SHA-256: `839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07`
- Verified local source SHA-256: `839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07`
- Source GLB was not modified.
- Rendering used local Windows Blender 5.2 in background mode with `BLENDER_EEVEE`; no cloud renderer, Higgsfield, or GitHub Actions was used.

## Shared render contract

- Native resolution: 1280x720 at 100%
- Frame rate: 24 fps
- Frames: 1–720, 720 rendered frames
- Output codec: H.264, yuv420p
- Duration: 30.000 seconds
- Workbench: not used
- Checkpoints: frames 1, 121, 241, 361, 481, 601, 718 corresponding to 0, 5, 10, 15, 20, 25, and 29.9 seconds
- Every checkpoint passed automated semantic QA and visual inspection before final encoding.

## VIDEO 01 — Wet Processing / Mixing Hall

- Active camera: `PRES_15_MIXING_HALL`
- Semantic targets: `ProcessTank_01`–`ProcessTank_11`, `MIXING_PLATFORM`, `PROCESS_EPOXY_FLOOR`
- Exact output: `3d/video/V03_CORRECTIVE/VIDEO_01_WET_PROCESSING/POVU_VID_019_V03_Wet_Processing_CLEAN_30s.mp4`
- Absolute output: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V03_CORRECTIVE\VIDEO_01_WET_PROCESSING\POVU_VID_019_V03_Wet_Processing_CLEAN_30s.mp4`
- Final QA: 7/7 PASS; clean frames with tanks, platform, floor, and no visible speckle/grain/dither.
- ffprobe: H.264, 1280x720, 24/1 fps, 720 frames, 30.000000 seconds
- SHA-256: `BC44895AB0AD7F750A671999527A1645BEA30924D14AD765884B78798867E7B5`
- Evidence: `3d/video/V03_CORRECTIVE/VIDEO_01_WET_PROCESSING/qa_report.json`, `camera_route.json`, `render_settings.json`, `contact_sheet.png`, `final_qa/`, `final_ffprobe.json`, `final_sha256.txt`

### Wet disposable-scene corrective settings

- Eevee TAA render samples: 32
- TAA reprojection: disabled
- Ray tracing: disabled
- Viewport shadow jitter: disabled
- Volumetric shadows: disabled
- Shadow resolution scale: 2.0
- Shadow ray count: 4
- Shadow step count: 4
- Exposure: -0.75
- World strength: 0.22
- Scene/light shadows and contact shadows: disabled in the disposable V03 render scene to remove stochastic grain
- Imported material blend/dither stabilization: 95 materials were normalized in the disposable scene; the source GLB was untouched. The glass override was applied only after stabilization and only to the confirmed Glass Deck glazing slots.
- No source mesh merge, geometry edit, or GLB rewrite was performed.

## VIDEO 03 — POVU Glass Deck

- Active camera: `VID_GLASS_DECK_V03_CAMERA`
- Semantic targets: `GlassDeck_East`, `GlassDeck_West`, `DECK_TIMBER_FLOOR`, `DECK_EAST_TIMBER_FLOOR`, `GLASS_DECK_LINK`, `GLASS_DECK_LINK_FLOOR`, `DECK_EAST_GLASS`, `Production_Hall`
- Exact output: `3d/video/V03_CORRECTIVE/VIDEO_03_GLASS_DECK/POVU_VID_GLASS_DECK_V03_30s.mp4`
- Absolute output: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V03_CORRECTIVE\VIDEO_03_GLASS_DECK\POVU_VID_GLASS_DECK_V03_30s.mp4`
- Final QA: 7/7 PASS; the deck walkway/glazing is visible at the deck segment and the production tanks are visible through the corrected glazing in the final route segment.
- ffprobe: H.264, 1280x720, 24/1 fps, 720 frames, 30.000000 seconds
- SHA-256: `EC8EC8123AAA9AB375C25D6D8D4770CC6946675402B731113CF4C56649D96F3D`
- Evidence: `3d/video/V03_CORRECTIVE/VIDEO_03_GLASS_DECK/qa_report.json`, `camera_route.json`, `render_settings.json`, `contact_sheet.png`, `final_qa/`, `final_ffprobe.json`, `final_sha256.txt`

### Confirmed disposable glass override

Temporary material: `V03_TEMP_GLASS_DECK_TRANSPARENT`. Only these actual glazing objects and material slots were overridden in the disposable render scene:

| Object | Original slot material | Temporary material |
|---|---|---|
| `DECK_EAST_GLASS` slot 0 | `REF_Glass` | `V03_TEMP_GLASS_DECK_TRANSPARENT` |
| `GLASS_DECK_LINK` slot 0 | `REF_Glass` | `V03_TEMP_GLASS_DECK_TRANSPARENT` |
| `GlassDeck_East` slot 0 | `Glass` | `V03_TEMP_GLASS_DECK_TRANSPARENT` |
| `GlassDeck_West` slot 0 | `Glass` | `V03_TEMP_GLASS_DECK_TRANSPARENT` |

No deck geometry, deck walls, or master GLB material data was changed.

## Reproducibility and publication

- Pipeline: `3d/video/pipeline/render_v03_corrective.py`
- Local heavy frame/checkpoint/final-QA outputs remain ignored workstation evidence; committed evidence includes the render metadata, QA reports, camera routes, settings, contact sheet, final ffprobe records, SHA files, pipeline, and this log.
- The final publication is scoped to this two-video corrective task only.
