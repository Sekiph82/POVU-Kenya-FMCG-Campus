# M08.34 — F05 FIRE PUMP HOUSE PRIMARY HISTORICAL RESTORATION

## Scope

Execute F05 only.

Read:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F05_FIRE_PUMP_HISTORICAL_SOURCE_PROVENANCE.md`
4. `coordination/Audits/REV005_FACILITY_F05_FIRE_PUMP_GPT_AUDIT_CRITERIA.md`
5. historical V01–V05 build scripts
6. historical V05 renderer

Do not begin F06.

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

Re-read local root TASKS.md after sync.

It must authorize:
`M08.34 — Facility-Gated F05 Fire Pump House primary historical restoration`

## Locked canonical baseline

Blend:
`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Expected SHA-256:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

Expected SHA-256:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

If mismatch:
STOP `BLOCKED_F05_CANONICAL_BASELINE_MISMATCH`.

## Phase 1 — protect accepted facilities and quarantine state

Before any mutation create exact protection manifests for:
- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- `V09_RESTAURANT_RIGHT_WALL`
- historical Glass Deck source
- historical Wellness/pavilion protected objects

Record:
- name
- matrix_world
- dimensions
- materials
- parent
- collection
- hide_render
- hide_viewport

## Phase 2 — detached historical replay

Create detached OS-temp worktree at:

`420038365847de763d64c8583a9e31ac5a6bd677`

Initial historical Blend SHA:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay exactly:
1. V01
2. V02
3. V03
4. V04
5. V05

Do not patch historical modeling code.

## Phase 3 — resolve exact V05 Fire Pump House selection

Use original V05:

`objects_for("Fire pump house", record)`

Required total:
**123**

Classify each selected object using actual world-center Y:

PRIMARY:
`center_y < 30`

SECONDARY:
`center_y >= 30`

Required:
- PRIMARY = **54**
- SECONDARY = **69**

Also classify source contribution:

Required total:
- BASE 10
- V01 15
- V04 44
- V05 54

Required PRIMARY:
- BASE 5
- V01 0
- V04 22
- V05 27
- total 54

Required SECONDARY:
- BASE 5
- V01 15
- V04 22
- V05 27
- total 69

Write:
`F05_REPLAY_SOURCE_MANIFEST_123.json`
`F05_PRIMARY_54_MANIFEST.json`
`F05_SECONDARY_69_MANIFEST.json`

For every object record:
- contribution source
- primary/secondary classification
- name/type
- collections
- matrix_world
- center XYZ
- dimensions
- material slots
- parent
- data block
- modifiers
- hide flags
- custom properties

If any count differs:
STOP `BLOCKED_F05_HISTORICAL_SPATIAL_SPLIT`.

## Phase 4 — dimensional verification of primary cluster

Verify the exact V04 and V05 PRIMARY geometry against:

`coordination/Audits/REV005_F05_FIRE_PUMP_HISTORICAL_SOURCE_PROVENANCE.md`

Required primary anchors:

V04:
- room center (94,-5)
- pumps at X=91/97, Y=-6
- suction Y=-2.5
- four valves X=88/92/96/100
- panel (100,-10,2.6)

V05:
- envelope center (94,-5), 20×18×7
- pump machines X=91/97, Y=-5
- suction Y=-2
- header Z=4
- valves X=88/92/96/100, Y=-2
- panel (100,-10,2.6)

Tolerance:
<=0.001 m / <=0.0001 rad.

If mismatch:
STOP `BLOCKED_F05_PRIMARY_DIMENSIONAL_SOURCE_MISMATCH`.

## Phase 5 — reproduce historical archived A/B/C

Run the original V05 renderer against the full replayed 123-object source.

Do not alter original historical `show_only()`.

A:
- camera (76,-22,15)
- target (94,-5,3)
- 52 mm / 36 mm
- expected SHA `5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`

B:
- camera (88,-12,9)
- target (94,-5,3)
- expected SHA `D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`

C:
- camera (98,-2,9)
- target (94,-5,3)
- expected SHA `AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

Require exact decoded parity or metadata-only difference.

If source visual content differs:
STOP `BLOCKED_F05_SOURCE_RENDER_MISMATCH`.

## Phase 6 — create PRIMARY-only transfer library

Create temporary transfer collection:

`F05_FIRE_PUMP_PRIMARY_54_TRANSFER`

Link exactly the 54 PRIMARY historical objects and required datablock dependencies.

Do NOT include the 69 SECONDARY objects.

## Phase 7 — inventory current canonical Fire Pump House

Open canonical current REV005.

Write:
`F05_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify existing Fire Pump House objects/collections.

Classify all candidates spatially using actual world center.

Only PRIMARY-zone conflicting Fire Pump House representation may be removed/unlinked.

Do NOT remove or mutate anything with center Y>=30 merely because it has Fire Pump metadata.

Do NOT alter Utilities/Engineering or any other facility.

## Phase 8 — restore exact 54 PRIMARY objects

Destination:

`REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`

Append exactly 54 PRIMARY objects.

Preserve:
- matrix_world
- dimensions
- materials
- parent relationships
- object data
- modifiers
- accepted saved visibility

Do not append SECONDARY 69.

Write:
`F05_DESTINATION_PRIMARY_54_MANIFEST.json`

## Phase 9 — exact V05 parity from PRIMARY destination

Parity QA must reproduce historical V05 `show_only()` semantics exactly.

This includes temporary render hiding for selected object names containing:
- `_LEFT`
- `_RIGHT`
- `_BACK`
- `_SOFFIT`
- `_CEILING_BEAM`

This is QA-only.
Do not save those temporary visibility changes.

Render destination A/B/C at 900×600 using exact historical Workbench settings.

Outputs:
- `F05_DEST_PARITY_A_900x600.png`
- `F05_DEST_PARITY_B_900x600.png`
- `F05_DEST_PARITY_C_900x600.png`
- `F05_DESTINATION_PARITY.json`

Compare to archived V05 references.

Because SECONDARY objects are far outside A/B/C framing, restoring only PRIMARY 54 must still reproduce the accepted primary-cluster images.

Structural mismatch:
STOP `BLOCKED_F05_DESTINATION_PARITY`.

## Phase 10 — prior PASS protection

Compare before/after manifests.

Require exact:
- F01 76/76
- F02 79/79
- F03 30/30
- F04 59/59
- Glass Deck quarantine 117
- Training quarantine 81
- Restaurant right-wall quarantine
- historical Glass Deck
- protected Wellness/pavilion state

Any mismatch:
STOP `BLOCKED_F05_PRIOR_PASS_REGRESSION`.

## Phase 11 — integrated primary-cluster evidence

Do not use a rigid projected-area percentage threshold.

Test the three historical viewpoints first:
- A (76,-22,15)
- B (88,-12,9)
- C (98,-2,9)

Then search nearby camera positions if necessary.

Target:
primary 54-object union center, biased toward pump/header region.

For every candidate:
- camera must not lie inside geometry
- cast 9 LOS rays across primary union
- require >=7/9 clear
- no QA-only hiding/quarantine
- no neighbor mutation
- paired pumps, piping/valves and control panel must be visually readable
- legitimate current context should remain visible
- full primary functional cluster should not be materially clipped

Rank valid cameras by:
1. clear rays
2. primary functional readability
3. minimal unrelated obstruction
4. natural perspective
5. historical camera proximity

If no valid view:
STOP `BLOCKED_F05_INTEGRATED_COLLISION`
and report blocker names only.

## Phase 12 — final QA renders

Produce:

A_CONTEXT:
- 1440×960
- historical A camera

B_FUNCTIONAL:
- 1440×960
- historical B camera

C_PROCESS_OR_DETAIL:
- 1440×960
- historical C camera

D_INTEGRATED_CONTEXT:
- 1440×960
- selected valid integrated camera

D preview:
- same camera/state
- 900×600

Required visible cues:
- paired primary pumps
- pump bases
- suction/header network
- discharge relation
- multiple valves
- control panel
- service/access organization

## Phase 13 — save/export/evidence

Only after all gates pass:

Save canonical Blend.

Export canonical GLB under current project export visibility policy.

Create:
- F05_BASELINE_HASHES.json
- F05_REPLAY_SOURCE_MANIFEST_123.json
- F05_PRIMARY_54_MANIFEST.json
- F05_SECONDARY_69_MANIFEST.json
- F05_PRIMARY_DIMENSIONAL_VALIDATION.json
- F05_SOURCE_RENDER_HASHES.json
- F05_CURRENT_PRE_RESTORE_MANIFEST.json
- F05_DESTINATION_PRIMARY_54_MANIFEST.json
- F05_DESTINATION_PARITY.json
- F05_PROTECTION_BEFORE.json
- F05_PROTECTION_AFTER.json
- F05_INTEGRATED_CAMERA_VALIDATION.json
- F05_FINAL_HASHES.json
- F05_VALIDATION.json

Log exactly:

`coordination/Logs/REV005_F05_FIRE_PUMP_RESTORE_CODEX_LOG.md`

## Git scope

Commit/push:
- canonical Blend/GLB
- F05-only evidence/renders
- F05 log

Do not edit TASKS.md.
Do not edit locked criteria.
Do not begin F06.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F05`
