# M08.40 — F06-X03 COMPLEMENTARY INTEGRATED EVIDENCE CLOSURE

## Scope

Execute F06-X03 only.

This is an evidence-only closure task.

The single-frame all-cues requirement is superseded for F06 only by the independent X02 audit:

`coordination/Audits/REV005_F06_X02_GPT_AUDIT.md`

F06 must now be proven with two complementary current-context views:

- D = process integrated overview
- E = operator / service / access proof

Do not begin F07.

Do not mutate the model.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F06_X02_GPT_AUDIT.md`
3. `coordination/Audits/REV005_F06_X01_GPT_AUDIT.md`
4. `coordination/Logs/REV005_F06_X02_WIDE_FOV_GLB_PARITY_CODEX_LOG.md`
5. all committed F06 X02 camera evidence

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

`M08.40 — Facility-Gated F06-X03 complementary integrated evidence closure`

If not, STOP before work.

## Locked canonical state

Blend SHA-256:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

GLB SHA-256:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

If either differs:

STOP `BLOCKED_F06_X03_CANONICAL_HASH_MISMATCH`.

## Locked geometry / quarantine

F06 accepted destination:

`REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`

Count:

43

Contribution split:

- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1

The seven X01 quarantine objects remain exactly as accepted.

No object visibility, geometry, collection, material, transform, parent, data, or quarantine change is authorized.

## Part A — D process integrated overview

The independent X02 audit accepts this X02 seed as a valid process overview:

`F06_X02_CANDIDATE_01`

- camera = (8,43,6)
- target = (-4,50,2.8)
- lens = 20 mm
- sensor = 36 mm
- LOS = 9/9

First re-render this exact camera from the locked canonical state.

Create:

- `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_X03.png` at 1440×960
- `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_X03_PREVIEW_900x600.png`

Required D cues:

- weigh booth/enclosure = true
- four-hopper row = true
- hopper valves/outlets = true
- dosing paths = true
- precision balances = true
- balance table = true
- transfer tote/cart = true
- coherent hopper→dosing→balance→transfer relationship = true
- legitimate current context = true
- camera outside geometry = true
- QA-only hiding = false
- new neighbor mutation = false

The D view does NOT need to prove the operator/service/access side.

If exact candidate 01 no longer reproduces these accepted D cues from the locked state, STOP:

`BLOCKED_F06_X03_D_REPRODUCTION_MISMATCH`

Do not substitute geometry changes.

## Part B — E operator / service / access proof

Create a dedicated current-context camera search focused on the front/service side of F06.

This E view is not required to show the entire four-hopper process line.

It must prove the complementary functions that D cannot show clearly.

### Required E visual cues

One E frame must clearly communicate:

- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_PANEL`
- `V02_WEIGH_OPERATOR_TABLE` or equivalent clearly readable operator work surface
- front/service working zone
- usable floor/access organization around operator and balance/transfer area
- visible relationship toward either:
  - precision balance stations, or
  - transfer tote/cart, or
  - dosing/balance workflow
- enough F06 geometry to prove this is the same Micro-ingredient Weigh / Dispense facility
- legitimate current context
- camera outside geometry
- no QA-only hiding
- no new neighbor mutation

### Camera search

Render at least 24 new E candidates at 900×600.

Prioritize the front-left / service-side region.

At minimum test families around:

- (-14,44,4.5)
- (-13,45,4.0)
- (-12,46,4.0)
- (-11,45,5.0)
- (-10,44,4.5)
- (-9,45,4.0)
- (-8,44,5.0)
- (-7,45,4.5)

Also test at least four closer interior/service-side positions of your own choosing that remain outside geometry.

Target families must include points around:

- (-6,48,2.2)
- (-5,47.6,2.2)
- (-7,48.5,2.3)
- (-4,48.5,2.2)
- (-2,49,2.2)

Test lenses:

- 24 mm
- 28 mm
- 32 mm
- 35 mm
- 40 mm

Sensor width:

36 mm

Do not reject a candidate merely because it does not show all four hoppers.

The E task is specifically operator/service/access proof.

## E LOS / obstruction evidence

Use a dedicated E target set:

1. `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`
2. `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_PANEL`
3. `V02_WEIGH_OPERATOR_TABLE`
4. `V02_PRECISION_BALANCE_0`
5. `V02_PRECISION_BALANCE_2`
6. `V02_WEIGH_TRANSFER_TOTE`
7. `V02_WEIGH_BALANCE_TABLE`

Require at least 5/7 clear rays.

LOS is supporting evidence only. Visual readability controls acceptance.

Record blockers by exact object name.

## E candidate evidence

Create:

`output/rev005-facility-gated/F06_micro_weigh/X03/F06_X03_E_CAMERA_CANDIDATES.json`

and at least 24 E previews.

Each record must contain:
- candidate ID
- camera XYZ
- target XYZ
- lens
- 7-ray LOS result
- blockers
- operator station body visible
- operator panel visible
- operator table/service surface visible
- access floor organization visible
- relationship to balance/transfer workflow visible
- same-facility context visible
- camera outside geometry
- preview path

Do not auto-select by LOS alone.

## Final E selection

If a valid E candidate exists, produce:

- `E_OPERATOR_SERVICE_ACCESS_X03.png` at 1440×960
- `E_OPERATOR_SERVICE_ACCESS_X03_PREVIEW_900x600.png`

The full and preview renders must use the exact same camera/target/lens and locked canonical state.

If no E candidate satisfies the complementary proof gate:

STOP:

`BLOCKED_F06_X03_NO_OPERATOR_SERVICE_ACCESS_VIEW`

Do not change geometry.
Do not widen quarantine.

## Combined D+E coverage gate

Create:

`F06_X03_COMBINED_VISUAL_COVERAGE.json`

Required combined booleans:

- weigh_booth_enclosure = true
- four_hopper_row = true
- hopper_valves = true
- dosing_paths = true
- precision_balances = true
- balance_table = true
- transfer_tote_or_cart = true
- operator_station = true
- operator_panel = true
- operator_service_zone = true
- access_organization = true
- coherent_process_relationship = true
- legitimate_current_context = true

Also record which view proves each cue: D, E, or both.

No cue may be marked true solely from object metadata; it must be visually supported by D or E.

## Regression gate

Because X03 is evidence-only:

Blend must remain exactly:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

GLB must remain exactly:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

Re-confirm:

- F06 destination count = 43
- contribution split = 7/12/23/0/0/1
- seven X01 quarantines unchanged
- no F01-F05 accepted-state change
- no F07 work

Create:

`F06_X03_REGRESSION.json`

## Final validation

Create:

`F06_X03_VALIDATION.json`

Success requires:

- D process overview = PASS
- E operator/service/access = PASS
- combined D+E coverage = PASS
- regression = PASS
- canonical hashes unchanged
- F07 not started

## Required log

Write:

`coordination/Logs/REV005_F06_X03_COMPLEMENTARY_EVIDENCE_CODEX_LOG.md`

## Git scope

Commit/push only:

- X03 D/E renders and previews
- E candidate previews
- X03 evidence JSON
- X03 log

Do not commit changed Blend or GLB.

Do not edit root TASKS.md.
Do not edit locked audits.
Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06_X03`
