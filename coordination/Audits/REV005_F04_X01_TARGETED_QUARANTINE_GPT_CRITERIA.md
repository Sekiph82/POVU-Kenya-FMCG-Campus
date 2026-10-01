# REV005 F04 X01 — TARGETED CROSS-FACILITY QUARANTINE — LOCKED GPT CRITERIA

## Baseline

Canonical pre-X01 hashes:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

## Gate A — verify exact blockers before mutation

Verify:
- `REV005_V08_CLEAN_TRAINING_ACADEMY` exists and contains exactly 81 objects.
- actual aggregate bounds of that collection.
- plan overlap with historical `WELLNESS_PAVILION`.
- `V09_TRAINING_BOARD` actual bounds.
- `V09_RESTAURANT_RIGHT_WALL` actual bounds.
- historical `Restaurant_Wellness` bounds and its max-X = ~26 m.

If evidence does not support the root-cause document, STOP before mutation.

## Gate B — protected manifests

Before mutation capture:
- F01 76
- F02 79
- F03 30
- WELLNESS_PAVILION
- WELLNESS_GLASS
- historical Restaurant_Wellness
- V09 Wellness collection
- historical Glass Deck source
- 117-object V09 Glass Deck quarantine

## Gate C — authorized quarantine only

### Training

Collection:
`REV005_V08_CLEAN_TRAINING_ACADEMY`

Expected:
81 objects.

For collection and its directly owned V09 Training objects:
- hide_viewport = true
- hide_render = true
- tag `REV005_CROSS_FACILITY_QUARANTINED = true`
- reason = `V09 Training envelope overlaps historical Wellness Pavilion / accepted F04 welfare zone`
- owner = `F04_X01`

No delete/move/mesh/material change.

### Restaurant

Object only:
`V09_RESTAURANT_RIGHT_WALL`

Set:
- hide_viewport = true
- hide_render = true
- same quarantine metadata
- owner = `F04_X01`

Do NOT alter any other Restaurant object.

## Gate D — exact F04 restoration

Restore exact historical:
- BASE 10
- V01 49
- total 59

Destination:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Historical A/B destination parity must pass.

## Gate E — prior PASS protection

F01/F02/F03 exact before/after parity required.

Historical pavilion, Restaurant_Wellness and V09 Wellness unchanged.

## Gate F — integrated evidence

After the targeted quarantine, search for F04 integrated camera using interior pavilion strategy.

Require:
- camera not inside F04 equipment
- >=7/9 clear rays
- no QA-only exclusions
- F04 recognizable as changing/shower/locker support
- legitimate pavilion context visible

Do not impose a hard projected-area percentage. GPT will inspect the actual preview.

Render:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600

If no >=7/9 camera exists:
STOP `BLOCKED_F04_X01_REMAINING_INTEGRATION_COLLISION`
and report exact blockers without further quarantine.

## Gate G — save/export only after success

Only if Gate F succeeds:
- save canonical Blend
- export canonical GLB
- commit canonical files + F04 X01 evidence/renders/log

## Stop

Success:
`AWAITING_GPT_F04_X01_INTEGRATED_AUDIT`

Do not begin F05.
