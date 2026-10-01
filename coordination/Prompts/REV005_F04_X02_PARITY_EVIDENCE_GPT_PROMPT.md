# M08.30 — F04-X02 DESTINATION PARITY EVIDENCE CORRECTION

## Scope

Evidence-only correction.

Do not modify canonical model geometry.

Read:
- root `TASKS.md`
- `coordination/Audits/REV005_F04_X01_GPT_AUDIT.md`
- `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`

## Current canonical baseline

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

These hashes must remain unchanged.

## Accepted current F04 state

Destination collection:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Required accepted object count:
**59**

Composition:
- 10 BASE
- 49 V01

X01 quarantine state must remain unchanged:
- V09 Training collection: 81 objects quarantined
- `V09_RESTAURANT_RIGHT_WALL`: quarantined

## Problem

X01 destination parity renders were invalid because unrelated current-scene geometry remained visible.

Do not touch the model to fix this.

Fix only the parity-render isolation.

## Phase 1 — verify canonical state

Open canonical Blend.

Verify:
- Blend hash matches locked X02 baseline before opening/saving workflow
- 59-object F04 accepted destination exists
- X01 quarantine state intact
- F01/F02/F03 protected counts unchanged

Do not save.

## Phase 2 — build exact facility-only render isolation

For parity rendering only:

1. Record the current visibility state of every object and collection that will be touched by the QA isolation.
2. Hide from parity rendering every scene object that is NOT part of the accepted 59-object F04 selection.
3. Show all 59 accepted F04 destination objects.
4. Preserve normal World/background and Workbench settings used by historical V05.
5. No geometry, material, transform, parent, modifier, or collection membership change.
6. This visibility isolation is temporary QA state only and must NOT be saved into canonical Blend.

Use the original V05 accepted selection semantics, not broad facility-name matching.

## Phase 3 — exact A parity

Render 900×600.

Camera:
- location: (14,-88,13)
- target: (30,-70,3)
- lens: 52 mm
- sensor width: 36 mm

Output:
`output/rev005-facility-gated/F04_x02/F04_X02_DEST_PARITY_A_900x600.png`

Archived reference:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_A_WIDE.png`

Archived SHA-256:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

## Phase 4 — exact B parity

Render 900×600.

Camera:
- location: (20,-78,8)
- target: (30,-70,3)
- lens: 52 mm
- sensor width: 36 mm

Output:
`output/rev005-facility-gated/F04_x02/F04_X02_DEST_PARITY_B_900x600.png`

Archived reference:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_B_FUNCTIONAL.png`

Archived SHA-256:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

## Phase 5 — parity comparison

For A and B record:
- raw PNG SHA-256
- decoded pixel equality
- differing pixel count
- differing normalized channel count
- max absolute channel delta

Acceptance:
- exact decoded-pixel match preferred
- microscopic antialias-only differences may be reported truthfully for GPT review
- any structural/image-content difference = BLOCKED

Create:
`output/rev005-facility-gated/F04_x02/F04_X02_DESTINATION_PARITY.json`

## Phase 6 — restore QA visibility state

Restore every object/collection visibility flag exactly to its pre-parity value.

Verify:
- Training quarantine still intact
- Restaurant right wall quarantine intact
- F01/F02/F03 unchanged
- F04 59 objects unchanged

Do not save canonical Blend.

Do not export GLB.

## Phase 7 — canonical hash proof

Recompute current files on disk.

Required unchanged:

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

Create:
`output/rev005-facility-gated/F04_x02/F04_X02_CANONICAL_HASH_PROOF.json`

## Git scope

Commit/push only:
- corrected A parity PNG
- corrected B parity PNG
- parity JSON
- canonical hash proof JSON
- `coordination/Logs/REV005_F04_X02_PARITY_EVIDENCE_CODEX_LOG.md`

Do not commit Blend/GLB.
Do not edit TASKS.md.
Do not modify criteria.
Do not begin F05.

## STOP

If structural A/B parity passes:

`AWAITING_GPT_F04_X02_FINAL_AUDIT`

If not:

`BLOCKED_F04_X02_DESTINATION_PARITY`
