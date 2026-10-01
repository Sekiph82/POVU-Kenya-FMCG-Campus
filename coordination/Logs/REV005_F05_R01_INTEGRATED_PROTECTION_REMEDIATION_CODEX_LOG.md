# REV005 F05-R01 Integrated Protection Remediation — Codex Log

## Final state

`AWAITING_GPT_FACILITY_AUDIT_F05_R01`

The R01 evidence package is complete. Independent GPT facility audit remains required; Codex does not promote this task to final acceptance. F06 was not started.

## Authorization and starting state

- Task: `M08.35 — Facility-Gated F05-R01 integrated-view + protection-evidence remediation`.
- Canonical workspace: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`.
- Starting commit after safe fast-forward: `62db905`.
- Root `TASKS.md` authorized M08.35 / F05-R01 only and was not edited.
- No reset, rebase, force push, second Desktop copy, locked-criteria edit, or F06 work.
- Locked M08.34 canonical Blend SHA-256: `E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`.
- Locked M08.34 canonical GLB SHA-256: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.

## Integrated-view remediation

The prior D evidence failed visual readability because overhead/slab elements dominated, the paired pump area was only partly exposed, the header/valve network was obscured, and the control panel was not clearly identifiable. The prior 9/9 LOS result was not treated as visual acceptance.

The saved current model was evaluated with 25 rendered candidates: historical A/B/C plus 22 nearby/interior alternatives. Every candidate was rendered at 900×600 with current saved visibility, no QA-only hiding, and no neighbor mutation. The selected candidate was not the first qualifying camera.

Selected R01 D camera:

- Candidate: `front_exterior_right`.
- Camera: `(106.0, -20.0, 4.2)`.
- Target: `(94.0, -4.5, 2.8)`.
- Lens: `40 mm`.
- LOS: `9/9` functional-facility rays; blocker names are retained in the validation JSON.
- Both pump housings and bases, header/suction, multiple valves, control panel, and access organization are readable.
- No unrelated structure dominates; the primary cluster is not materially clipped; legitimate current context remains visible.

## Protection-state remediation

Direct Blender inspection was performed against:

- pre-F05 baseline `4fd49a647224727139f45016fa21d5c1ca724418`;
- accepted F04-X01 quarantine execution `674a6bf`;
- accepted F04-X03 evidence-only closure `0fb3ff0`;
- current F05 canonical state.

All four scenes carry the accepted Restaurant right-wall quarantine state: `V09_RESTAURANT_RIGHT_WALL` has `hide_viewport=true`, `hide_render=true`, the F04-X01 quarantine properties, visible owning collection, and no excluded/hidden layer collection. Glass Deck remains 117 objects quarantined and Training remains 81 objects quarantined.

Root cause: `MANIFEST_DERIVATION_BUG_ONLY`.

The old F05 manifests reported a false→true summary change while their recorded Restaurant object payload remained unchanged. The direct accepted-state comparison shows no canonical protection mutation. No model, visibility, linkage, transform, dimension, mesh, material, or neighbor correction was made.

Protected-state diff result: zero unauthorized protected-state differences.

## Regression and hashes

- F05 destination primary collection: exactly 54.
- F05 secondary spatial set: 69; no secondary object was appended to the primary collection.
- F01/F02/F03/F04 accepted counts and locked source/parity gates were preserved.
- Canonical Blend SHA-256 remains `E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`.
- Canonical GLB SHA-256 remains `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.

## Evidence paths

- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_CAMERA_CANDIDATES.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_CANDIDATE_01_900x600.png` through `F05_R01_CANDIDATE_25_900x600.png`
- `output/rev005-facility-gated/F05_fire_pump/R01/D_INTEGRATED_CONTEXT_R01.png`
- `output/rev005-facility-gated/F05_fire_pump/R01/D_INTEGRATED_CONTEXT_R01_PREVIEW_900x600.png`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_INTEGRATED_CAMERA_VALIDATION.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_PROTECTION_STATE_AUDIT.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_PROTECTION_REFERENCE.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_PROTECTION_CURRENT.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_PROTECTION_DIFF.json`
- `output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_REGRESSION.json`

Stop at `AWAITING_GPT_FACILITY_AUDIT_F05_R01`.
