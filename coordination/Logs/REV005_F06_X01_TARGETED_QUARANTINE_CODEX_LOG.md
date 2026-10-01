# REV005 F06-X01 Targeted Quarantine Codex Log

- Task: M08.38 / F06-X01 only.
- Live authorization verified in `TASKS.md`; `HEAD` and `origin/main` matched at `640502eb1db67ea0e8e3d0692fd107e51cbced7c` before changes.
- Prompt: `coordination/Prompts/REV005_FACILITY_F06_X01_TARGETED_CROSS_FACILITY_QUARANTINE_GPT_PROMPT.md`.
- Baseline canonical hashes: Blend `BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`; GLB `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.
- Ownership: the seven unaccepted V09 Toothpaste/Wet Wipes envelope objects structurally overlapped accepted F06; each object was checked against facility/provenance metadata and the V09 builder envelope definition before mutation.
- Exact mutation: `V09_TOOTHPASTE_FLOOR`, `V09_TOOTHPASTE_BACK_WALL`, `V09_TOOTHPASTE_SOFFIT`, `V09_WET_WIPES_FLOOR`, `V09_WET_WIPES_BACK_WALL`, `V09_WET_WIPES_LEFT_WALL`, `V09_WET_WIPES_SOFFIT`; only `hide_viewport=true`, `hide_render=true`, and the three F06-X01 quarantine custom properties were added. No geometry, transform, material, parent, collection, or other scene edits.
- Quarantine diff: PASS; seven changed objects exactly; no adds/removals; no unauthorized object diffs; collection links and scene properties unchanged. All protected F01-F06 and historical signature categories passed. F06 accepted count remains 43.
- Camera search: 32 previews, all required lenses 35/40/45/52 mm, nine LOS targets recorded per candidate. Candidate 32 clears 9/9 LOS and is outside geometry but the transfer item is cropped; the operator/service zone and access organization are not established. No frame passed the complete visual gate. No additional temporary hiding or neighbor mutation was used. No D integrated render was created.
- Result: `BLOCKED_F06_X01_NO_COMPLETE_INTEGRATED_VIEW`. No quarantine widening, Wet Processing change, or F06 geometry change. Stop for GPT direction; do not begin F07.
- Canonical export used REV005 V09 current policy (`use_visible=True`), with `export_cameras=True`, `export_lights=True`, `export_apply=True`, `export_extras=True`, `use_selection=False`. The attempted `use_visible=True` export yielded SHA-256 `B9C82300BCAA2230F9A245318F0BDF37A0B2AD73D19F1CF6A3A0FDF8B5FEEFDD`, 2,019 nodes versus 10,605 baseline, and omitted 12 of 43 F06 destination names. This failed export was discarded; canonical GLB was restored to locked baseline SHA-256 `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825` to preserve accepted F06 objects. No second export was attempted; GPT direction required.
- Final hashes: Blend `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`; GLB remains locked at `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.

## Evidence

- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_QUARANTINE_BEFORE.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_QUARANTINE_AFTER.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_QUARANTINE_DIFF.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_CAMERA_CANDIDATES.json` and 32 candidate previews
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_INTEGRATED_CAMERA_VALIDATION.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_REGRESSION.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_FINAL_HASHES.json`
- `output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_VALIDATION.json`

BLOCKED_F06_X01_NO_COMPLETE_INTEGRATED_VIEW — publish this blocked evidence for GPT direction; do not widen the quarantine or begin F07.
