# M08.34 — F05 FIRE PUMP HOUSE PRIMARY HISTORICAL RESTORATION

## Scope

One facility only:
**F05 — Fire Pump House**

Read first:
1. root TASKS.md
2. coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md
3. coordination/Audits/REV005_F05_FIRE_PUMP_HISTORICAL_SOURCE_PROVENANCE.md
4. coordination/Audits/REV005_FACILITY_F05_FIRE_PUMP_GPT_AUDIT_CRITERIA.md

## Canonical baseline

Required:
- Blend `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`
- GLB `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

If mismatch:
STOP `BLOCKED_F05_CANONICAL_BASELINE_MISMATCH`.

## Protect accepted prior work

Before mutation capture exact manifests for:
- F01 76
- F02 79
- F03 30
- F04 59

Also preserve:
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- V09_RESTAURANT_RIGHT_WALL quarantine
- historical pavilion/Wellness/Glass Deck protections

## Phase 1 — detached historical replay

Create OS-temp detached worktree at:
`420038365847de763d64c8583a9e31ac5a6bd677`

Verify initial historical Blend:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Run in exact order:
1. V01
2. V02
3. V03
4. V04
5. V05

Do not patch historical modeling code.

## Phase 2 — resolve full historical Fire Pump selection

Using original V05:
`objects_for("Fire pump house", record)`

Required:
**123 objects**

Contribution:
- BASE 10
- V01 15
- V02 0
- V03 0
- V04 44
- V05 54

Create:
`F05_FULL_HISTORICAL_SOURCE_MANIFEST.json`

If total/contribution differs:
STOP `BLOCKED_F05_FULL_SOURCE_COMPOSITION`.

## Phase 3 — mandatory spatial split

For each of the 123 selected objects compute world bounding-box center Y.

PRIMARY window:
-20 <= centerY <= +10

Expected:
**54 objects**
- BASE 5
- V01 0
- V04 22
- V05 27

SECONDARY window:
55 <= centerY <= 85

Expected:
**69 objects**
- BASE 5
- V01 15
- V04 22
- V05 27

Any object outside both windows or any count mismatch:
STOP `BLOCKED_F05_HISTORICAL_SPATIAL_SPLIT`.

Create:
- `F05_PRIMARY_SOURCE_MANIFEST.json`
- `F05_SECONDARY_PROVENANCE_ONLY_MANIFEST.json`

IMPORTANT:
Only PRIMARY 54 is authorized for canonical restore.
Do not append the secondary 69.

## Phase 4 — dimensional contract

Verify primary V04 and V05 objects exactly against the provenance document.

### V04 primary
center anchor:
(94,-5)

Expected 22:
- 4 room shell objects
- 2 pump cylinders
- 2 pump bases
- 1 suction pipe
- 2 discharge pipes
- 4 valves
- 1 panel
- 6 light BODY/GLOW objects

### V05 primary
center anchor:
(94,-5)

Expected 27:
- 14 envelope objects
- 6 pump machine objects
- 2 pipes
- 4 valves
- 1 panel

Tolerance:
<=0.001 m.

BASE 5 must match replay exactly.

## Phase 5 — historical A/B/C proof

Run original V05 renderer unchanged.

A:
- camera (76,-22,15)
- target (94,-5,3)
- 52 mm
- expected SHA `5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`

B:
- camera (88,-12,9)
- target (94,-5,3)
- 52 mm
- expected SHA `D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`

C:
- camera (98,-2,9)
- target (94,-5,3)
- 52 mm
- expected SHA `AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

Decoded pixel parity must pass.

## Phase 6 — inventory current Fire Pump representation

Open canonical current REV005.

Record every current Fire Pump candidate before mutation.

Create:
`F05_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify by:
- owner inventory names
- facility metadata
- RM_FIRE_*
- V04_FIRE_*
- V05_FIRE*
- V08/V09 Fire-Pump-specific collection/objects
- prior F05 collection if any

Do not remove anything until manifest complete.

## Phase 7 — restore PRIMARY only

Remove/unlink only current Fire Pump representation that conflicts with the accepted PRIMARY cluster.

Do not touch Utilities or any secondary-region object unless it is explicitly a current Fire Pump duplicate being retired by exact lineage and this action is separately logged.

Append exactly 54 primary historical objects into:

`REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`

Do not append the 69 secondary historical source objects.

Preserve all source geometry and metadata.

## Phase 8 — destination A/B/C parity

Temporary QA visibility only.

Reproduce original V05 `show_only()` semantics exactly:
- hide non-selected objects
- hide non MESH/CURVE/SURFACE
- hide selected names containing _LEFT/_RIGHT/_BACK/_SOFFIT/_CEILING_BEAM

Render destination:
- A 900×600
- B 900×600
- C 900×600

Restore all visibility flags after rendering.

Create:
`F05_DESTINATION_PARITY.json`

## Phase 9 — prior PASS protection

Exact before/after:
- F01 76
- F02 79
- F03 30
- F04 59

Quarantine states unchanged.

If any mismatch:
STOP `BLOCKED_F05_PRIOR_PASS_REGRESSION`.

## Phase 10 — integrated primary-cluster camera

Integrated target:
primary cluster only around (94,-5,3).

Do not include secondary historical cluster in bounds/framing.

Search appropriate exterior/interior positions around primary cluster.

Require:
- camera not inside geometry
- >=7/9 clear rays
- no temporary hiding/quarantine
- paired red pump sets visible
- suction/header/valve relation visible
- panel/service access readable
- legitimate surrounding context visible

If no valid camera:
STOP `BLOCKED_F05_INTEGRATED_COLLISION`
and report exact blockers only.

## Phase 11 — final QA

Render:
- F05_A_CONTEXT.png 1440×960
- F05_B_FUNCTIONAL.png 1440×960
- F05_C_PROCESS_DETAIL.png 1440×960
- F05_D_INTEGRATED_CONTEXT.png 1440×960
- F05_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png

## Phase 12 — save/export

Only after all gates pass.

Save canonical Blend.
Export canonical GLB.

Create all source/split/destination/protection/camera/hash/validation evidence.

Log:
`coordination/Logs/REV005_F05_FIRE_PUMP_RESTORE_CODEX_LOG.md`

Commit/push:
- canonical Blend/GLB
- F05 evidence/renders/log

Do not edit TASKS.md.
Do not begin F06.

## STOP

`AWAITING_GPT_FACILITY_AUDIT_F05`
