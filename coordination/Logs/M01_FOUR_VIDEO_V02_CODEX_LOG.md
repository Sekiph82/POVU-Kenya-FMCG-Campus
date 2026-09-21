# M01 Four-Video V02 Camera-True Validation Batch Codex Log

Status: `PARTIAL`

Run date: 2026-09-21
Blender: `5.2.2 LTS` local Windows Blender
Final engine: `BLENDER_EEVEE`
Final settings: native `1280x720`, `24 fps`, frames `1-720`, `30.000 s`, H.264 MP4

## Global source gate

`SOURCE_INTEGRITY: PASS`

Authoritative source:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d-jutsu-Untitled-3D-Jutsu-2026-09-21-07-44-56.glb`

- SHA-256: `839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07`
- Size: `7,503,776` bytes
- GLB 2.0; nodes `2,031`; meshes `1,937`; materials `95`; cameras `50`
- Required Hands of Growth, Water Wall, QA landmark, Wet Processing camera, process-tank, mixing-platform, and epoxy-floor objects verified.
- Repository master `3d/revisions/REV003/POVU_REV003_MASTER.glb` matches this SHA-256.
- Old pre-landmark SHA `033337f2fcd54e1166a2ca5560c5779fcdd96a55589ef84c6f72b3155ab5dd1d` is superseded and was not used for rendering.

Evidence: `3d/video/V02_CAMERA_TRUE_TEST/SOURCE_INTEGRITY_REPORT.json`, `SOURCE_INTEGRITY_REPORT.md`, `source_inspection.json`, and `3d/revisions/REV003/REVISION.md`.

## Material gate

`MATERIAL_PIPELINE: FAIL FOR VIDEO-03 / PASS FOR VIDEOS 01, 02, 04`

The corrected GLB supplies visible green vegetation/Living Wall, aqua water, bronze/champagne signage, graphite architecture, POVU signage, natural stainless/concrete, process flooring, and Hands of Growth materials. The Glass Deck geometry is present, but its referenced `Glass`, `REF_Glass`, and `PEO_Glass` materials have `Transmission Weight: 0` and render as opaque neutral surfaces in Eevee. This is recorded as `MATERIAL_SOURCE_LIMITATION`; no material or geometry was fabricated or silently recolored.

Evidence: `3d/video/V02_CAMERA_TRUE_TEST/MATERIAL_AUDIT.json`, `MATERIAL_AUDIT.md`, and `VIDEO_03_GLASS_DECK/MATERIAL_SOURCE_LIMITATION.md`.

## Video results

| Video | Subject | Active camera | Semantic targets | Checkpoint QA | Final result |
|---|---|---|---|---|---|
| VIDEO 01 | Wet Processing / Mixing Hall | `PRES_15_MIXING_HALL` | `PRES_15_MIXING_HALL`, `ProcessTank_01..11`, `MIXING_PLATFORM`, `PROCESS_EPOXY_FLOOR` | 7/7 PASS; final MP4 frames correspond to checkpoint views | PASS |
| VIDEO 02 | Hands of Growth | `VID_HOG_V02_CAMERA` | HOG palms, forearms, fingers, trunk, crowns, plinth and plaza context | 7/7 PASS; final MP4 frames correspond to checkpoint views | PASS |
| VIDEO 03 | POVU Glass Deck | `VID_GLASS_DECK_V02_CAMERA` | East/West Glass Deck, timber floors, glass-deck link, Production Hall | Automated route projection 7/7; manual visual QA FAIL at checkpoints 3, 4, 7 | FAIL — `MATERIAL_SOURCE_LIMITATION`; final MP4 withheld |
| VIDEO 04 | POVU Color & Materials Proof | `VID_COLOR_PROOF_V02_CAMERA` | VIP sign, Water Wall/basin, Living Wall, POVU Plaza, Hands of Growth | 7/7 PASS after correcting checkpoint 4 route; final MP4 frames correspond to corrected checkpoint views | PASS |

### VIDEO 01 — PASS

- MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V02_CAMERA_TRUE_TEST\VIDEO_01_WET_PROCESSING\POVU_VID_019_V02_Wet_Processing_30s.mp4`
- File size: `60,435,541` bytes
- SHA-256: `2f93a3c58b81a618c4285a85ada86aad03db0ff2c4bb9328d6fb053c12833d85`
- Validation: H.264, `1280x720`, `24/1 fps`, `30.000000 s`
- Render time: approximately `32:30`
- QA: `qa_report.json`, `camera_route.json`, `contact_sheet.png`, `final_qa/final_01..07.png`

### VIDEO 02 — PASS

- MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V02_CAMERA_TRUE_TEST\VIDEO_02_HANDS_OF_GROWTH\POVU_VID_HOG_V02_Hands_of_Growth_30s.mp4`
- File size: `15,045,921` bytes
- SHA-256: `76acfa10f8a517513983491721fdb8e03270a1a892f3065413a1f400ba32e10e`
- Validation: H.264, `1280x720`, `24/1 fps`, `30.000000 s`
- Render time: approximately `27:00`
- QA: `qa_report.json`, `camera_route.json`, `contact_sheet.png`, `final_qa/final_01..07.png`

### VIDEO 03 — FAIL / BLOCKED

- Expected MP4 path: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V02_CAMERA_TRUE_TEST\VIDEO_03_GLASS_DECK\POVU_VID_GLASS_DECK_V02_30s.mp4`
- Status: not created because the approved seven-checkpoint visual gate failed.
- Failure: `MATERIAL_SOURCE_LIMITATION`; the source deck glazing is opaque in Eevee, so checkpoints 3, 4, and 7 do not provide a readable through-glass production view.
- QA: `qa_report.json` records automated projection results plus manual failure; `MATERIAL_SOURCE_LIMITATION.md` is the controlling explanation.

### VIDEO 04 — PASS

- MP4: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\video\V02_CAMERA_TRUE_TEST\VIDEO_04_COLOR_MATERIAL_PROOF\POVU_VID_COLOR_MATERIAL_PROOF_V02_30s.mp4`
- File size: `6,789,115` bytes
- SHA-256: `d178529c433b48bbcfcbf6e8a442429b0ce87728857f840a07c38f7faa8f3ee8`
- Validation: H.264, `1280x720`, `24/1 fps`, `30.000000 s`
- Render time: approximately `20:06` for the corrected full rerender
- QA: 7/7 manual checkpoint views pass after replacing the invalid plaza keyframe; `qa_report.json`, corrected `camera_route.json`, `contact_sheet.png`, `final_qa/final_01..07.png`

## Repository artifacts

The commit includes the corrected REV003 master and revision record, source/material integrity reports, route-inspection scripts, Blender pipeline script, route metadata, checkpoint QA/contact sheets, final QA stills, MP4 ffprobe/hash evidence, the Video 3 limitation record, and this log. Large render-frame sequences, `.blend` files, and MP4 binaries remain local according to the repository workflow; V01 outputs were not overwritten.

## M01 count

The existing individual V01 logs `M01_VIDEO-001_V01_CODEX_LOG.md` through `M01_VIDEO-050_V01_CODEX_LOG.md` are `PASS` (`50/50` canonical M01 videos completed). This corrective V02 validation batch is `3/4` passed, with `VIDEO-03` failed/blocked by the source material limitation above.
