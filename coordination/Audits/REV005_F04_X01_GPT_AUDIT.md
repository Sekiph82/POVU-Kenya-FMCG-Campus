# REV005 F04-X01 — INDEPENDENT GPT AUDIT

## Outcome

`REMEDIATION_REQUIRED_PARITY_EVIDENCE_ONLY`

The F04-X01 geometry/restoration and targeted quarantine pass, but F04 cannot yet be closed because the destination A/B parity evidence is invalid.

## What passed

- authorized quarantine scope exactly respected:
  - 81-object `REV005_V08_CLEAN_TRAINING_ACADEMY`
  - single object `V09_RESTAURANT_RIGHT_WALL`
- F04 historical composition: 10 BASE + 49 V01 = 59
- dimensional contract: PASS
- integrated LOS: 9/9
- F01 76/76 protection parity: PASS
- F02 79/79 protection parity: PASS
- F03 30/30 protection parity: PASS
- historical Glass Deck / pavilion / Wellness protection: PASS
- integrated preview materially improved and no longer contains the dominant V09 Training board blocker
- commit scope is limited to canonical Blend/GLB plus F04-X01 evidence

## Direct visual finding

### Integrated preview

`F04_X01_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png`

Visually usable as integrated context evidence:
- shower/cubicle field is visible
- pavilion context is visible
- the former dominant black Training board is gone
- no camera-inside-wall failure
- no destructive blocker comparable to V04 remains

### Destination parity A

`F04_X01_DEST_PARITY_A_900x600.png`

FAIL.

The frame is largely occluded by an unrelated large surface and does not resemble the archived V05 A image.

### Destination parity B

`F04_X01_DEST_PARITY_B_900x600.png`

FAIL.

The frame is nearly flat gray and does not resemble the archived V05 B image.

### Archived V05 reference

A:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_A_WIDE.png`

B:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_B_FUNCTIONAL.png`

Both archived images clearly show the accepted shower/changing/locker geometry.

## Root cause class

Evidence-generation isolation failure.

The accepted 59-object destination appears to be present, but the X01 parity renders were not produced under correct facility-only visibility/isolation.

## Required remediation

Do NOT alter:
- F04 geometry
- F04 transforms/materials/parents
- X01 quarantine state
- F01/F02/F03
- any neighbor facility
- canonical Blend/GLB

Regenerate only facility-only destination parity A/B from the already-saved canonical X01 state.

Required archived SHA references:

A:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

B:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

After X02 parity proof, GPT will combine:
- X01 integrated proof
- X02 corrected A/B parity proof

for final F04 closure.
