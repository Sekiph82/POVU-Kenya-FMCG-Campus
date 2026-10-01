# REV005 F06-X02 Wide-FOV + GLB Export Parity — Codex Log

## Scope and stop state

- Task: `M08.39` / `F06-X02` only.
- Live `TASKS.md` authorized M08.39 / F06-X02. F07 was not started. `TASKS.md` and locked prior audits were not edited.
- Checkout: canonical POVU workspace, branch `main`, current starting ref `a544139`; the clean checkout was fast-forwarded from `13569d4` to live `origin/main` before reading the active prompt.
- Locked Blend baseline: `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`.
- Locked GLB baseline: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.
- The Blend remained byte-identical. No geometry edits, saved visibility edits, or quarantine widening occurred.

## Regression and quarantine

- Corrected the X01 contribution-split extraction error from `F06_DESTINATION_43_MANIFEST.json`: BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1, total 43.
- All 43 accepted F06 destination signatures match the committed manifest.
- Exactly the locked seven F06-X01 quarantine objects retain `hide_viewport=true`, `hide_render=true`, and owner `F06_X01`.
- F01-F05 protection remains unchanged by byte identity to the accepted locked Blend. The reference protection snapshot is `output/rev005-facility-gated/F06_micro_weigh/F06_PROTECTION_AFTER.json`.

## Wide-FOV camera search

- Rendered and visually reviewed 78 new 900×600 previews with sensor width 36 mm. All required lenses (20/24/28/30/32/35 mm), all five required target families, all eight required camera positions, and four farther-back right/front-oblique positions were tested.
- Nineteen candidates reached at least 7/9 LOS. LOS was not used to auto-select a frame.
- Best partial frame: `F06_X02_CANDIDATE_01`, camera `(8,43,6)`, target `(-4,50,2.8)`, 20 mm, 9/9 LOS. It clearly shows the booth, four-hopper row, outlets/valves, dosing paths, balance stations/table, and transfer tote. The foreground neighboring structure still masks the operator/service zone and access organization and dominates part of the frame. No candidate passed the complete visual gate.
- No final integrated 1440×960 or 900×600 pair was created because no candidate passed.
- Camera result: `BLOCKED_F06_X02_NO_COMPLETE_INTEGRATED_VIEW`.

## Deterministic GLB membership export

- Baseline GLB has 10,605 uniquely named nodes / 10,449 meshes and maps one-to-one to 10,605 Blender objects.
- Required export selection contained exactly all baseline members except the seven X01 quarantine names: 10,598 names / 10,442 expected meshes.
- For export only, 10,598 baseline objects were explicitly selected with `use_selection=true`, `use_visible=false`. Hidden collection visibility flags for member collections were temporarily enabled in memory so historically hidden accepted baseline members remained selectable; object, collection, and layer-collection states were restored before process exit. No temporary state was saved into the Blend.
- Actual output: 10,598 nodes / 10,442 meshes; zero missing baseline names, zero unexpected names, 43/43 accepted F06 names present, and 7/7 X01 quarantine names absent.
- Exact membership parity passed. The canonical GLB was replaced only after this gate passed. Final GLB SHA-256: `948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`.

## Final hashes and handoff

- Final Blend SHA-256: `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B` (unchanged).
- Final GLB SHA-256: `948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133` (exact membership parity PASS).
- Overall result is blocked on the complete integrated-camera visual gate, despite the passing contribution regression and GLB membership export.
- Stop marker: `BLOCKED_F06_X02_NO_COMPLETE_INTEGRATED_VIEW`. Do not begin F07.

## Evidence

- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_REGRESSION.json`
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_CAMERA_CANDIDATES.json` and 78 candidate previews
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_INTEGRATED_CAMERA_VALIDATION.json`
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_GLB_BASELINE_MEMBERSHIP.json`
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_GLB_EXPORT_PARITY.json`
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_FINAL_HASHES.json`
- `output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_VALIDATION.json`

BLOCKED_F06_X02_NO_COMPLETE_INTEGRATED_VIEW
