# POVU M01 — V03 Clean Master Production Log

## Batch scope

This production run rebuilds the 48 canonical videos with IDs 001–011 and 013–050 using local Windows Blender. Approved canonical 012 and 019 are retained as existing approved V03 outputs and are not rerendered. Hands of Growth and Color/Materials Proof are additional approved validation films and are also untouched.

- Batch state: `coordination/batch_state.json`
- Source: `3d/revisions/REV003/POVU_REV003_MASTER.glb`
- Required source SHA-256: `839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07`
- Verified source SHA-256: `839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07`
- Renderer: local Windows Blender Eevee only
- Output root: `3d/video/V03_CLEAN_MASTER/`
- Current status: **IN PROGRESS — VIDEO-001 rendering**

## Quality contract

Every rebuilt video requires actual REV003 semantic targets, a subject-specific camera route, native 1280x720 Eevee at 24 fps for frames 1–720, seven full-resolution checkpoint renders, visual contact-sheet QA, final H.264 encoding, ffprobe, seven extracted final QA frames, SHA-256, an individual log, and GitHub publication. Source geometry and source GLB materials remain unchanged; all camera, lighting, visibility, and material stabilization changes are disposable-scene changes.

## Video results

Detailed results are maintained in the per-video logs `M01_VIDEO-NNN_V03_CODEX_LOG.md`. The batch state is authoritative for restart status.

| Video | Subject | Status |
|---:|---|---|
| 001 | POVU Campus Aerial | RENDERING |
| 002–011 | Remaining campus/people/facility subjects | PENDING |
| 012 | POVU Glass Deck | APPROVED EXISTING — not rerendered |
| 013–018 | Raw material/control subjects | PENDING |
| 019 | Liquid Mixing / Wet Processing | APPROVED EXISTING — not rerendered |
| 020–050 | Remaining production/logistics/site subjects | PENDING |

## Restart rule

On interruption, inspect `coordination/batch_state.json` and each V03 output directory. Resume at the first video that is not genuinely PASS or documented `BLOCKED_MISSING_GEOMETRY`. Do not rerender an already validated PASS output.

