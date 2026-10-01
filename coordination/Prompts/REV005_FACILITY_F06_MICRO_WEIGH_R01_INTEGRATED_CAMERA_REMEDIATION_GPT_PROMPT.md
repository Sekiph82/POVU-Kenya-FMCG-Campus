# M08.37 — F06-R01 MICRO-INGREDIENT WEIGH / DISPENSE INTEGRATED-CAMERA REMEDIATION

## Scope

Execute F06-R01 only.

This is a camera/evidence remediation driven by:

`coordination/Audits/REV005_F06_MICRO_WEIGH_GPT_AUDIT_V01.md`

Do not begin F07.

Do not rebuild, replace, duplicate, move, resize, relink, rematerial, or otherwise alter the accepted 43-object F06 historical geometry.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_FACILITY_F06_MICRO_WEIGH_GPT_AUDIT_CRITERIA.md`
4. `coordination/Audits/REV005_F06_MICRO_WEIGH_GPT_AUDIT_V01.md`
5. `coordination/Logs/REV005_F06_MICRO_WEIGH_RESTORE_CODEX_LOG.md`
6. all committed F06 evidence under `output/rev005-facility-gated/F06_micro_weigh/`

## Safe synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If unexpected local changes exist, STOP without discarding them.

Fetch and fast-forward-only to current `origin/main`.

No reset.
No rebase.
No force.
No second Desktop copy.

Re-read root `TASKS.md`.

It must authorize:

`M08.37 — Facility-Gated F06-R01 integrated-camera remediation`

If not, STOP before any evidence generation.

## Locked starting canonical state

Blend SHA-256:

`BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`

GLB SHA-256:

`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If either differs:

STOP `BLOCKED_F06_R01_CANONICAL_HASH_MISMATCH`.

## Locked PASS gates — preserve

Do not redo or invalidate these unless a contradiction is discovered:

- historical selected count = 43
- contribution split BASE 7 / V01 12 / V02 23 / V05 1
- historical source A/B/C exact decoded parity
- dimensional validation
- destination A/B/C structural parity
- protected-state diff = zero unauthorized differences
- F01-F05 accepted protection
- destination collection count = 43

No canonical model mutation is expected or authorized.

## Why M08.36 failed

The selected `FRONT_LEFT` camera at:

- camera (-15, 41, 6)
- target (-5, 50, 3)
- 52 mm
- LOS 9/9

shows the hopper/dosing/balance core, but the complete downstream workflow is not readable in one integrated frame.

Specifically:

- transfer tote/cart is materially cropped at the right edge;
- operator/service-access organization is only fragmentary;
- the full hopper → dosing → balance → transfer relationship is not shown coherently.

A 9/9 LOS score is necessary but not sufficient.

## Camera search — wider and farther

Use the current saved canonical visibility state.

Do not hide or quarantine any wall, soffit, neighboring facility, or F06 object for the final integrated view.

Render **at least 20** new 900×600 current-context candidates.

Search beyond the M08.36 grid.

At minimum include candidate families around:

### Far front-left / front-oblique
- (-18,38,6)
- (-20,39,7)
- (-22,40,6)
- (-18,42,5)
- (-20,43,6)

### Moderately farther left
- (-17,44,5)
- (-18,45,6)
- (-20,46,6)

### Higher/wider front-left
- (-18,39,8)
- (-20,41,8)
- (-16,38,7)

### Target variants

Do not point every camera at the same center.

Test targets that bias toward the complete workflow, for example around:
- (-4,50,2.8)
- (-3,49.5,2.8)
- (-2.5,49.5,2.6)
- (-4,49,2.5)

### Lens variants

Test at least:
- 35 mm
- 40 mm
- 45 mm
- 52 mm

Use sensor width 36 mm.

The goal is not maximum zoom. The goal is a coherent complete workflow with legitimate current context.

## Required visual gate

A candidate may be selected only if one single 900×600 integrated frame clearly communicates all of:

- weigh booth/enclosure;
- all or substantially all of the hopper row;
- hopper valves;
- dosing chutes/path;
- precision balance stations;
- balance table;
- transfer tote/cart clearly identifiable, not just a clipped edge;
- operator table or operator/service zone;
- usable service/access organization;
- relationship between dosing and downstream transfer;
- legitimate current context.

The camera must also:

- be outside geometry;
- achieve >=7/9 LOS rays;
- use no QA-only hiding;
- use no neighbor mutation;
- avoid unrelated structural domination;
- avoid material clipping of the process workflow.

Do not count a wall label as proof of process identity.

## LOS sample set

Include at least these functional targets:

- V02_WEIGH_HOPPER_0
- V02_WEIGH_HOPPER_2 or 3
- V02_WEIGH_HOPPER_VALVE_1
- V02_WEIGH_DOSING_CHUTE_0
- V02_WEIGH_DOSING_CHUTE_2
- V02_PRECISION_BALANCE_0
- V02_PRECISION_BALANCE_2
- V02_WEIGH_TRANSFER_TOTE
- V02_WEIGH_OPERATOR_TABLE

If a target is legitimately occluded by another F06 process component, record the exact blocker and judge the frame visually rather than falsifying LOS.

## Candidate evidence

Create:

`output/rev005-facility-gated/F06_micro_weigh/R01/F06_R01_CAMERA_CANDIDATES.json`

and at least 20 previews:

`F06_R01_CANDIDATE_01_900x600.png`
through
`F06_R01_CANDIDATE_20_900x600.png`

More are allowed.

Each JSON row must record:

- candidate ID
- camera XYZ
- target XYZ
- lens
- LOS visible/total
- blocker names
- camera-outside-geometry result
- no-QA-hide result
- no-neighbor-mutation result
- individual visual-cue booleans
- preview path

Do not auto-select based only on LOS.

## Final selection

Select the candidate with the strongest complete functional readability.

Produce:

- `D_INTEGRATED_CONTEXT_R01.png` at 1440×960
- `D_INTEGRATED_CONTEXT_R01_PREVIEW_900x600.png`

Both must use the exact same camera, target, lens and saved visibility state.

Write:

`F06_R01_INTEGRATED_CAMERA_VALIDATION.json`

Required final booleans:

- weigh_booth = true
- hopper_row = true
- hopper_valves = true
- dosing_chutes = true
- precision_balances = true
- balance_table = true
- transfer_tote_or_cart = true
- operator_or_service_zone = true
- access_organization = true
- complete_workflow_relationship = true
- structure_dominance_or_clipping = false
- qa_hiding_used = false
- neighbor_mutation = false

## Regression / hash gate

Because this task is evidence-only, canonical Blend and GLB must remain exactly:

Blend:
`BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`

GLB:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

Also re-confirm:
- destination count 43;
- no F01-F05 protected change;
- no F07 work.

Write:

`F06_R01_REGRESSION.json`

## If no valid view exists

If no camera can satisfy the complete visual gate without changing geometry:

STOP:

`BLOCKED_F06_R01_NO_COMPLETE_INTEGRATED_VIEW`

Do not alter the model.

Report the exact recurring blockers and candidate evidence.

## Required log

Write:

`coordination/Logs/REV005_F06_R01_INTEGRATED_CAMERA_REMEDIATION_CODEX_LOG.md`

## Git scope

Commit/push only:

- F06 R01 candidate previews;
- selected final integrated render/preview;
- R01 JSON evidence;
- R01 log.

Do not commit a changed Blend/GLB.

Do not edit:
- root TASKS.md
- locked criteria
- historical provenance

Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06_R01`
