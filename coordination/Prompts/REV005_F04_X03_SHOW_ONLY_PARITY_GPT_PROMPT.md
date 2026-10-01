# M08.33 — F04-X03 EXACT V05 SHOW_ONLY PARITY REPLAY

## Scope

Evidence-only.

Do not modify canonical geometry or quarantine state.

Read:
1. root `TASKS.md`
2. `coordination/Audits/REV005_F04_X02_DESTINATION_PARITY_ROOT_CAUSE.md`
3. historical `3d/revisions/REV005/pipeline/render_rev005_interior_remediation_v05.py`
4. `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`

## Canonical baseline

Required unchanged files:

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

If either differs, STOP.

## Accepted F04 destination

Collection:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Required:
- 59 unique objects
- 10 BASE
- 49 V01

Do not change any object mesh, transform, dimensions, material, parent, collection membership or saved visibility.

## X01 quarantine state

Must remain exactly:
- `REV005_V08_CLEAN_TRAINING_ACADEMY`: 81 objects quarantined
- `V09_RESTAURANT_RIGHT_WALL`: quarantined
- existing V09 Glass Deck quarantine: 117 objects

No new quarantine.

## Phase 1 — verify historical renderer semantics

Read the historical V05 renderer directly.

Confirm its facility selection resolves exactly 59 F04 objects.

Confirm historical temporary visibility behavior is equivalent to:

For every scene object:
- hide if object is not in the selected F04 set; OR
- hide if type is not MESH/CURVE/SURFACE; OR
- hide if object name contains any shell-occluder token:
  - `_LEFT`
  - `_RIGHT`
  - `_BACK`
  - `_SOFFIT`
  - `_CEILING_BEAM`

Do not simplify or reinterpret this rule.

Create:
`output/rev005-facility-gated/F04_x03/F04_X03_SHOW_ONLY_DIAGNOSTIC.json`

Record:
- selected 59 names
- which selected names are additionally hidden by shell-occluder logic
- expected F04 shell-hidden list

Expected F04-specific shell-hidden objects must include exactly:
- RM_WELFARE_SHOWER_BACK_0
- RM_WELFARE_SHOWER_BACK_1
- RM_WELFARE_SHOWER_BACK_2
- RM_WELFARE_SHOWER_BACK_3

If additional selected F04 objects match the historical token logic, record them truthfully and apply the historical rule exactly.

## Phase 2 — record current visibility

Before temporary QA isolation, record:
- hide_render
- hide_viewport
for every object/collection that will be touched.

Do not save the Blend.

## Phase 3 — exact historical V05 QA visibility

Apply the historical V05 `show_only()` semantics in memory only.

Important:
- selected F04 shell-occluder objects are hidden for parity rendering;
- this is temporary QA state only;
- do not persist any visibility change.

## Phase 4 — exact historical renderer setup

Use exactly:

- engine: BLENDER_WORKBENCH
- resolution: 900×600
- PNG
- film transparent: false
- display shading light: STUDIO
- color type: MATERIAL
- shadows: true
- cavity: true
- cavity type: WORLD
- ridge factor: 1.8
- valley factor: 1.2
- background type: VIEWPORT
- background color: (0.08,0.10,0.12)

## Phase 5 — A parity

Camera:
- location (14,-88,13)
- target (30,-70,3)
- lens 52 mm
- sensor width 36 mm

Output:
`output/rev005-facility-gated/F04_x03/F04_X03_DEST_PARITY_A_900x600.png`

Archived reference:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_A_WIDE.png`

Archived SHA-256:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

## Phase 6 — B parity

Camera:
- location (20,-78,8)
- target (30,-70,3)
- lens 52 mm
- sensor width 36 mm

Output:
`output/rev005-facility-gated/F04_x03/F04_X03_DEST_PARITY_B_900x600.png`

Archived reference:
`output/rev005-interior-remediation-v05/qa/employee_changing_shower_locker_support_B_FUNCTIONAL.png`

Archived SHA-256:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

## Phase 7 — decoded parity comparison

For A and B compute:
- raw PNG SHA-256
- decoded-pixel equality
- differing pixel count
- differing normalized channel count
- max absolute channel delta

Create:
`output/rev005-facility-gated/F04_x03/F04_X03_DESTINATION_PARITY.json`

Expected result:
- exact decoded-pixel equality, or
- only microscopic antialias-only differences comparable to prior accepted facilities.

If there remains a structural difference:
STOP:
`BLOCKED_F04_X03_DESTINATION_PARITY`

Do not mutate canonical geometry.

## Phase 8 — restore all temporary visibility

Restore every touched object and collection visibility flag exactly.

Verify:
- F04 59 objects unchanged
- F01 76 unchanged
- F02 79 unchanged
- F03 30 unchanged
- X01 Training quarantine unchanged
- X01 Restaurant-right-wall quarantine unchanged
- Glass Deck quarantine unchanged

## Phase 9 — canonical hash proof

Recompute on-disk hashes.

Required unchanged:

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

Create:
`output/rev005-facility-gated/F04_x03/F04_X03_CANONICAL_HASH_PROOF.json`

## Git scope

Commit/push only:
- F04_X03_SHOW_ONLY_DIAGNOSTIC.json
- corrected A/B PNGs
- F04_X03_DESTINATION_PARITY.json
- F04_X03_CANONICAL_HASH_PROOF.json
- `coordination/Logs/REV005_F04_X03_SHOW_ONLY_PARITY_CODEX_LOG.md`

Do not commit Blend/GLB.
Do not edit TASKS.md.
Do not begin F05.

## STOP

If A/B parity passes:

`AWAITING_GPT_F04_X03_FINAL_AUDIT`

If structural parity still fails:

`BLOCKED_F04_X03_DESTINATION_PARITY`
