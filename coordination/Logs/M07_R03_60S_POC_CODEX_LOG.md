# M07 R03 60-Second POC — CODEX LOG

This log is append-only for the M07 R03 proof-of-concept.

## 2026-09-24 / 2026-09-25 — final local production

- Read the attached authoritative M07 R03 brief before implementation.
- Preserved the approved `poc-r02` source/output and the rejected M07 R02 output.
- Frozen source: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`.
- Frozen source SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`.
- Root cause confirmed: R02 concatenated eleven independent chapter compositions with local frame clocks and fresh cameras; each chapter's first shot used `travel = 1`, creating visible camera resets.
- Implemented one persistent R03 camera and one global frame clock in `M07-R03-POC-60S`.
- Added R03 route, callout metadata, DOM overlay, continuity validator, and Blender GLB callout audit.
- Initial render exposed a Remotion DOM removal exception from R3F `Html`; replaced it with a regular Remotion DOM overlay and rerendered successfully.
- Visual QA exposed a low diagonal route crossing roof volumes; added elevated transition controls and rerendered locally.
- `npm run lint`: PASS.
- Full-frame camera validator: PASS; 1,800 frames; persistent camera; 0 hard cuts; 0 discontinuities; constant FOV 52.
- Blender callout audit: PASS; 2,227 imported objects; 0 missing targets.
- Final MP4 technical validation: PASS; H.264, 1920×1080, 30 fps, 1,800 frames, 60.000 seconds.
- Final MP4 SHA-256: `476C86979CD332299EA45183252DF30D62F7138B45B4C9FCBF8AD213D4C9DBF2`.
- Final visual evidence: 2-second checkpoints, control-point neighborhoods, contact sheets, and selected actual-MP4 frame inspection all PASS for this POC.
- Final output: `output/complete-tour-r03-poc-60s/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R03_POC_60S.mp4`.
- Per the brief, stopped after the 60-second POC. Long-form production remains unstarted pending explicit user approval.
