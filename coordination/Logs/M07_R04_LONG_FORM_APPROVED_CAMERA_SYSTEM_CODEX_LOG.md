# POVU M07 R04 Long-Form Approved Camera System — CODEX LOG

Status: PASS

## Scope

Produced the complete M07 R04 campus and factory tour from the approved M07 R03 camera system. The route uses one persistent camera, a global Remotion frame clock, smooth waypoint interpolation, constant FOV, continuous TRAVEL → APPROACH → SLOW → REVEAL → PASS → ACCELERATE → NEXT movement, and restrained world-tracked labels.

No Higgsfield, GitHub Actions, cloud Blender worker, or other cloud rendering path was used. Geometry work and GLB reload validation used local Windows Blender 5.2.2. Video rendering used local Remotion/Chromium.

## Geometry revision

- Source REV004.1 GLB SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`
- Output REV004.2 GLB: `3d/revisions/REV004.2/POVU_REV004_2_FINAL_MASTER.glb`
- Output REV004.2 blend: `3d/revisions/REV004.2/POVU_Kenya_FMCG_CAMPUS_REV004_2_FINAL_ARCHITECTURAL_MASTER.blend`
- REV004.2 GLB SHA-256: `400086AC979CCD6C4BBFB6365A92B6101CA9D1C08F79B956F735505B5F001822`
- Hands of Growth correction: exact translation `(+6.0, 0.0, 0.0)` applied to the 27-object assembly; reloaded center approximately `(-102, -79, 4.95)`.
- No resize, rotation, duplicate, or orientation change was introduced.
- Living Wall audit: unchanged; continuous wall-bound assembly with reloaded bounds approximately `x -97.5..-65.1`, `y -92.69..-91.35`; no freestanding extension introduced.
- Reload evidence: `3d/revisions/REV004.2/audit/rev004_2_reload_validation.json` — PASS.

## Camera and coverage

- Composition: `M07-R04-COMPLETE-TOUR`
- Duration: 470 seconds / 14,100 frames / 30 fps
- Resolution: 1920x1080 final
- FOV: 52 degrees
- Control points: 49
- Opening aerial establishment: frames 0–450 / first 15 seconds
- Covered campus destinations: Admin/HQ, R&D/QC Innovation Centre, Training/Academy, Restaurant/POVU Café, Wellness/Recreation, Daycare, Occupational Health, gardens/social spaces, solar systems, Living Wall, Water Wall, Smart Totem, Hands of Growth, and Glass Deck access/production oversight.
- Factory route coverage: RAW MATERIALS → RECEIVING/STORAGE → FEEDING → WET PROCESSING/MIXING → MANUFACTURING → FILLING → PACKAGING → EOL → PALLETIZING → FINISHED GOODS → DISPATCH.

## Validation

- Continuity: PASS; no discontinuities.
- Maximum per-frame position delta: `1.6525341399082862` at frame 13650.
- Maximum per-frame angular delta: `1.37657498498164` degrees at frame 6156.
- Maximum position acceleration: `0.021887220863702792` at frame 13800.
- Maximum angular acceleration: `0.02447415836764654` at frame 5700.
- Static holds outside opening: `0`.
- Duplicate views: `0`.
- Callout target visibility: PASS.
- Visual QA evidence: `output/complete-tour-r04/qa/checkpoint-contact-sheet-01.png`, `checkpoint-contact-sheet-02.png`, `checkpoint-contact-sheet-03.png`, `critical-contact-sheet.png`, and `final-visual-qa-report.md`.

## Final outputs

- Preview: `output/complete-tour-r04/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R04_CAMERA_PREVIEW.mp4`
- Preview SHA-256: `28B9708697501B119FF2012C068F1F7A37DC4EF9CAB900F4BECBCC30A805B899`
- Final: `output/complete-tour-r04/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R04.mp4`
- Final SHA-256: `9E6CF50620F9573FE0308C2DCFC6F394720968CC0294FF3D3F479F686F96205E`
- Final ffprobe: H.264, 1920x1080, `yuv420p`, 30/1 fps, 14,100 frames, 470.000 seconds, TV color range.
- Route evidence directory: `output/complete-tour-r04/`
- Artifact commit SHA: `8d91b6e`

## Publication

Required GitHub log URL:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/coordination/Logs/M07_R04_LONG_FORM_APPROVED_CAMERA_SYSTEM_CODEX_LOG.md
