# REV005 F06 — MICRO-INGREDIENT WEIGH / DISPENSE — LOCKED GPT AUDIT CRITERIA

## Baseline

Canonical pre-F06 hashes:

Blend:
`E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`

GLB:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

## Historical source gate

Detached replay through V05 must resolve the exact historical V05 Micro-ingredient Weigh / Dispense selection.

Required total:
- 43 objects

Expected contribution decomposition:
- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1
- total 43

If detached replay contradicts the decomposition, STOP before canonical mutation and report the exact mismatch.

## Historical source / dimensional gate

The exact selected source objects must match the committed V01/V02/V05 geometry contract documented in:

`coordination/Audits/REV005_F06_MICRO_WEIGH_HISTORICAL_SOURCE_PROVENANCE.md`

Tolerance:
- centers/dimensions <= 0.001 m
- pipe/chute endpoints <= 0.001 m
- rotation <= 0.0001 rad

No redesign or approximation is permitted.

## Historical visual parity

Reproduce exact V05 `show_only()` semantics.

Archived references:

- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_A_WIDE.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_C_PROCESS_OR_DETAIL.png`

Required:
- exact decoded parity preferred;
- sparse antialias-only edge deltas may be reported for independent GPT review;
- any structural difference is FAIL.

## Restoration

Restore exactly the 43 historical selected objects into a dedicated accepted F06 collection.

Do not append unrelated facility objects.

Do not rebuild the facility with new substitute geometry.

## Protection

Require exact protection of:
- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted 54 primary objects
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- V09 Restaurant right-wall accepted quarantine state
- historical Glass Deck source
- historical Wellness/pavilion protected state

No prior accepted facility may regress.

## Integrated evidence

The restored F06 facility must be clearly readable in the current canonical context.

Required visible cues:
- weigh booth/enclosure;
- hopper row;
- hopper valves / dosing path;
- precision balance stations;
- balance table/workflow;
- transfer tote/cart;
- operator/service access organization.

A clear-ray score is not sufficient by itself.

Final integrated evidence must:
- keep current saved visibility;
- use no QA-only hiding;
- mutate no neighbor facility;
- keep the camera outside geometry;
- avoid a view dominated by unrelated structures;
- avoid material clipping of the functional cluster;
- show legitimate current context.

## Final QA

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- C_PROCESS_OR_DETAIL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600

Historical A/B/C parity evidence remains separate from current-context final QA.

## Scope

No F07.
No REV004 change.
No REV006.
No .hiveai.
No tour/video.
Codex must not edit root TASKS.md or this locked criteria file.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F06`
