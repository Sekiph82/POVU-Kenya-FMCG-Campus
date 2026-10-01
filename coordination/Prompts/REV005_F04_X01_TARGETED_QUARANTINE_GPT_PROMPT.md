# M08.30 — F04-X01 TARGETED V09 BLOCKER QUARANTINE + F04 RESTORE

Read root TASKS.md first.

Read:
- `coordination/Audits/REV005_F04_X01_CROSS_FACILITY_BLOCKER_ROOT_CAUSE.md`
- `coordination/Audits/REV005_F04_X01_TARGETED_QUARANTINE_GPT_CRITERIA.md`
- `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`

## Scope

F04 only.

The historical 59-object F04 model is accepted-source material and must not be redesigned.

V04 visual review proved the integrated blockers are V09 cross-facility geometry.

## Baseline

Required canonical hashes:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

If mismatch, STOP.

## Phase 1 — verify blocker geometry

Before mutation verify and write exact diagnostics:

### Historical Wellness Pavilion
Expected:
- X 19→41
- Y -79→-61
- Z 1.2→7.2

### Historical Restaurant_Wellness
Expected:
- X -16→26
- Y -80.5→-55.5
- Z 1.2→9.2

### V09 Training collection
`REV005_V08_CLEAN_TRAINING_ACADEMY`

Expected object count:
**81**

Compute:
- actual collection aggregate bounds
- XY overlap with WELLNESS_PAVILION
- overlap area

Verify:
`V09_TRAINING_BOARD`
actual center/bounds.

### V09 Restaurant blocker
Verify:
`V09_RESTAURANT_RIGHT_WALL`
actual bounds.

Compare its X bounds against historical Restaurant_Wellness max X ≈26 m.

Write:
`F04_X01_BLOCKER_DIAGNOSTIC.json`

If Training collection !=81 or blocker evidence contradicts the root cause:
STOP `BLOCKED_F04_X01_BLOCKER_VERIFICATION`

## Phase 2 — protection manifests

Before mutation capture exact:
- F01 76
- F02 79
- F03 30
- WELLNESS_PAVILION
- WELLNESS_GLASS
- Restaurant_Wellness
- V09 Wellness collection
- historical Glass Deck source
- V09 Glass Deck quarantine 117

## Phase 3 — targeted quarantine

### A. Training collection

Target only:
`REV005_V08_CLEAN_TRAINING_ACADEMY`

Expected 81 objects.

Do NOT delete or move.

Set collection and directly owned objects:
- hide_viewport=true
- hide_render=true
- `REV005_CROSS_FACILITY_QUARANTINED=true`
- `REV005_CROSS_FACILITY_QUARANTINE_REASON="V09 Training envelope overlaps historical Wellness Pavilion / accepted F04 welfare zone"`
- `REV005_CROSS_FACILITY_QUARANTINE_OWNER="F04_X01"`

### B. Restaurant right wall only

Target only:
`V09_RESTAURANT_RIGHT_WALL`

Do NOT alter any other Restaurant object.

Set:
- hide_viewport=true
- hide_render=true
- same quarantine flag/reason
- owner=`F04_X01`

No mesh/material/transform changes.

## Phase 4 — exact F04 historical restore

Revalidate/reuse the proven historical source:
- 10 BASE
- 49 V01
- total 59
- dimensional contract PASS
- archived A/B parity PASS

Restore exact accepted objects into:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Preserve transforms/dimensions/materials/parents.

## Phase 5 — destination A/B parity

Historical 900×600:

A:
- camera (14,-88,13)
- target (30,-70,3)
- lens 52

B:
- camera (20,-78,8)
- target (30,-70,3)
- lens 52

Require visual parity with archived V05.

## Phase 6 — protection recheck

Require exact:
- F01 76
- F02 79
- F03 30
- historical pavilion/glass
- historical Restaurant_Wellness
- V09 Wellness
- historical Glass Deck
- V09 Glass Deck quarantine

Only authorized visibility/quarantine changes:
- 81-object V09 Training collection
- V09_RESTAURANT_RIGHT_WALL

## Phase 7 — integrated camera

Use interior pavilion camera search.

Start from the best V04 wide candidate and also search nearby positions/lenses 52/45/40/35/32/28 mm.

Require:
- camera not inside F04 equipment
- >=7/9 clear rays
- normal canonical visibility after authorized quarantine
- no extra exclusions
- F04 changing/shower/locker identity visually readable
- legitimate pavilion context visible

No hard projected-area percentage gate.

Render the best valid camera:
- `F04_X01_D_INTEGRATED_CONTEXT.png` 1440×960
- `F04_X01_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png` 900×600

Also render final:
- `F04_X01_A_CONTEXT.png`
- `F04_X01_B_FUNCTIONAL.png`

If no >=7/9 view after ONLY these authorized quarantines:
STOP:
`BLOCKED_F04_X01_REMAINING_INTEGRATION_COLLISION`

Report remaining blocker names.
Do not broaden quarantine.

## Phase 8 — save/export/evidence

Only after integrated gate passes:

Save canonical Blend.

Export canonical GLB under current project visibility policy.

Create:
- F04_X01_BLOCKER_DIAGNOSTIC.json
- F04_X01_QUARANTINE_MANIFEST.json
- F04_X01_DESTINATION_MANIFEST.json
- F04_X01_DESTINATION_PARITY.json
- prior-PASS before/after manifests
- pavilion/Restaurant/Wellness protection before/after
- F04_X01_CAMERA_VALIDATION.json
- F04_X01_FINAL_HASHES.json
- F04_X01_VALIDATION.json

Log:
`coordination/Logs/REV005_F04_X01_TARGETED_QUARANTINE_CODEX_LOG.md`

Commit/push only:
- canonical Blend/GLB if success
- F04-X01 evidence/renders/log

Do not edit TASKS.md.
Do not begin F05.

## STOP

Success:
`AWAITING_GPT_F04_X01_INTEGRATED_AUDIT`
