# REV005 F06-R01 Integrated-Camera Remediation — Codex Log

## Scope and stop state

- Task: `M08.37` / Facility `F06-R01` only.
- Work type: current-context camera/evidence search; no canonical geometry or saved visibility edits.
- Live tracker authorized `M08.37` / `F06-R01`; repository was fast-forwarded from `4dbcc1ce2faeb0b6e0f61a5229f50e934ef82944` to `49de1b11cf2069ee7a2df90879b50003cfd6cf89` before evidence generation.
- The locked starting Blend and GLB hashes matched exactly.
- Stop marker: `BLOCKED_F06_R01_NO_COMPLETE_INTEGRATED_VIEW`.
- F07 was not started. `TASKS.md`, locked criteria, historical provenance, canonical Blend, and canonical GLB were not edited.

## Camera search

- Rendered 32 new 900×600 candidates with sensor width 36 mm and lenses 35/40/45/52 mm.
- Covered every required far/front-oblique, farther-left and higher/wider front-left position, varied target points, and added 12 south/front-center probes.
- Used the saved canonical visibility state for every render. No QA-only hiding and no neighbor mutation were used.
- Best partial view: `F06_R01_CANDIDATE_05_900x600.png`, camera `(-20, 43, 6)`, target `(-4, 50, 2.8)`, 35 mm. It shows only part of the hopper/dosing/balance/table arrangement. The transfer tote/cart is not clearly identifiable; the full row and service-access relationship are obstructed/cropped.
- No candidate met the visual acceptance gate. The maximum target-origin LOS count was 3/9 (minimum 7/9).
- The first Blender background process reported a graphics-driver access violation during shutdown after writing candidate 20 and the manifest; all 32 PNGs were reopened and dimension-checked, and the second batch exited normally.
- Recurring blockers: `V09_WET_PROCESS_BACK_WALL`, `V09_WET_WIPES_LEFT_WALL`, `V09_TOOTHPASTE_SOFFIT`, `V09_WET_PROCESS_SOFFIT`, `V02_WEIGH_BOOTH_SIDE`, `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`, `HOLDING_TANK_VESSEL`, and `HOLDING_TANK_LID`.
- No final integrated image was selected or created; selecting the best partial view would misstate the locked visual gate.

## Regression evidence

- Canonical Blend SHA-256 before/after: `BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655` (unchanged).
- Canonical GLB SHA-256 before/after: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825` (unchanged).
- Accepted destination collection remains 43 objects; historical split remains BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1.
- Prior F01–F05 protection evidence remains PASS; this task made no canonical model changes.
- Candidate manifest: `output/rev005-facility-gated/F06_micro_weigh/R01/F06_R01_CAMERA_CANDIDATES.json`.
- Validation: `output/rev005-facility-gated/F06_micro_weigh/R01/F06_R01_INTEGRATED_CAMERA_VALIDATION.json`.
- Regression: `output/rev005-facility-gated/F06_micro_weigh/R01/F06_R01_REGRESSION.json`.

The required success view cannot be produced under the current saved geometry/visibility without changing protected structure or facility geometry. Await a revised F06-specific instruction; do not begin F07.
