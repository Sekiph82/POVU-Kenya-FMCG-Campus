# F02 — DAYCARE / CRÈCHE — EXACT HISTORICAL RESTORATION

## ONE FACILITY ONLY

Active facility:
**F02 — Daycare / Crèche**

Do not touch F03 or any other facility.

Read:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F02_DAYCARE_HISTORICAL_SOURCE_PROVENANCE.md`
4. `coordination/Audits/REV005_FACILITY_F02_DAYCARE_GPT_AUDIT_CRITERIA.md`
5. historical V01–V05 build scripts and V05 renderer from the detached temp worktree

## Canonical current baseline

Root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Blend:
`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

GLB:
`3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

Expected current hashes before F02:
- Blend: `80C4FC83DBD260CB9D0A6B02F0582C5829273450437B90D7CD2B9281C17B744E`
- GLB: `9EA90C327C2502AA019AD9ADA656BE0BC0B652A19724BEF3162910058B63FD40`

Output:
`output\rev005-facility-gated\F02_daycare\`

If baseline differs, STOP:
`BLOCKED_F02_CANONICAL_BASELINE_MISMATCH`

## Protected prior PASS

F01 Caps & Trigger is locked.

Before any F02 mutation, create a full protection manifest for F01's accepted 76 objects:
- name
- matrix_world
- dimensions
- materials
- parent
- hide flags

Do not alter them.

Also verify the V09 Glass Deck replacement collection remains quarantined.

## Phase 1 — detached historical replay

Create a detached worktree under OS/system temp, never Desktop.

Commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Initial temp Blend SHA-256:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Run in exact order, in the temp worktree only:

1. `build_rev005_interior_remediation_v01.py`
2. `build_rev005_interior_remediation_v02.py`
3. `build_rev005_interior_remediation_v03.py`
4. `build_rev005_interior_remediation_v04.py`
5. `build_rev005_interior_remediation_v05.py`

Do not patch historical modeling code.

Write:
`F02_REPLAY_CHECKPOINTS.json`

## Phase 2 — exact Daycare source selection

Use the replayed temp Blend and original V05:
`objects_for("Daycare / crèche", record)`

Required total:
**79**

Required composition:
- BASE: 41
- V01: 0
- V02: 0
- V03: 38
- V04: 0
- V05: 0

The owner inventory has 42 Daycare names, but `REV005_LABEL_DAYCARE` must be excluded by historical label filtering.

Write:
`F02_REPLAY_SOURCE_MANIFEST.json`

For every selected object record:
- source category BASE/V03
- name/type
- collection(s)
- parent chain
- 16-value matrix_world
- location XYZ
- rotation XYZ radians
- scale XYZ
- dimensions XYZ metres
- data block
- material slots
- modifiers
- constraints
- hide flags
- custom properties

If total !=79 or category counts differ:
STOP `BLOCKED_F02_REPLAY_COMPOSITION`

## Phase 3 — explicit V03 geometry cross-check

The 38 V03 objects must reconcile with the exact dimensional contract in:
`REV005_F02_DAYCARE_HISTORICAL_SOURCE_PROVENANCE.md`

At minimum verify exact centers/dimensions for:
- V03_DAYCARE_FLOOR: (-105,-64,1.02), 27×20×0.18 m
- enclosure LEFT: (-118,-64,2.75), 0.16×19×5.5 m
- enclosure RIGHT: (-92,-64,2.75), 0.16×19×5.5 m
- enclosure BACK: (-105,-54.5,2.75), 26×0.16×5.5 m
- LOW_PARTITION: (-105,-64,2.1), 22×0.18×1.7 m
- PLAY_RUG: (-110,-58,1.18), 8.5×5.5×0.08 m
- READING_SHELF: (-97,-58,2.3), 1.2×4.5×2.2 m
- SOFT_NOOK: (-97.6,-65,1.65), 3.5×3.2×0.35 m
- CAREGIVER_DESK: (-106,-66.5,2.1), 3.4×1.1×1.5 m
- CAREGIVER_SCREEN: (-106,-65.8,3.5), 2.4×0.12×1.2 m
- HANDWASH: (-97,-70.5,1.9), 3.5×0.75×1.5 m
- six play-block coordinates
- four reading-bin coordinates
- four soft-back coordinates
- four 2-mesh light-fixture coordinates
- five cubby-face coordinates

Tolerance:
<=0.001 m per center/dimension component.

If mismatch:
STOP `BLOCKED_F02_V03_DIMENSIONAL_SOURCE_MISMATCH`

## Phase 4 — reproduce accepted V05 images

Run original V05 renderer in temp replay scene.

Daycare A:
- camera location (-122,-80,13)
- target (-105,-64,3)
- lens 52 mm
- sensor 36 mm
- historical output 900×600

Expected archived SHA-256:
`72370EF41D5C1EA3AE81500EE77F5764725D8C0C3E0622D1CD21B55344F757EE`

Daycare B:
- camera location (-113,-72,8)
- target (-105,-64,3)
- lens 52 mm
- sensor 36 mm

Expected archived SHA-256:
`7E06E34994D36AE6D84D3F4A58B1C7E05BC3FEEECD79EC06514ECDB2DC5A3F7B`

Write:
`F02_SOURCE_RENDER_HASHES.json`

If raw PNG metadata differs, compare decoded/IDAT visual pixel stream and create normalized evidence. The actual image content must match exactly.

If visual pixel content differs:
STOP `BLOCKED_F02_SOURCE_RENDER_MISMATCH`

Only after this gate may canonical mutation begin.

## Phase 5 — create exact transfer library

Create temp collection:
`F02_DAYCARE_ACCEPTED_V05_REPLAY_TRANSFER`

Link exactly the 79 selected Daycare objects.

Include required:
- mesh/data blocks
- materials
- parent dependencies
- modifiers/constraints
- node/image dependencies if used

Do not include:
- `REV005_LABEL_DAYCARE`
- unrelated facility objects

The accepted source geometry is authoritative.

## Phase 6 — inventory/remove only current broken Daycare

Open canonical current REV005.

Create:
`F02_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify Daycare candidates using:
- exact owner inventory names
- facility metadata matching Daycare / Crèche
- V03_DAYCARE_* historical names
- V08/V09 Daycare-specific restoration objects/collections
- any prior failed F02 collections

Record everything first.

Remove/unlink only current Daycare representation that conflicts with the incoming accepted 79-object source.

Do not touch F01 or any other facility.

## Phase 7 — append exact accepted Daycare

Destination collection:
`REV005_FG_F02_DAYCARE_ACCEPTED_V05_REPLAY`

Append local data, not external links.

For all 79 selected source objects preserve:
- world location
- world rotation
- scale
- dimensions
- mesh/data
- materials
- parent relationships
- functional geometry

Parity tolerances:
- location <=0.001 m/axis
- rotation <=0.0001 rad/axis
- scale <=0.0001/axis
- dimensions <=0.001 m/axis

Write:
`F02_DESTINATION_MANIFEST.json`

## Phase 8 — destination historical parity

Facility-only visibility, historical V05 Workbench settings.

A_PARITY:
- 900×600
- location (-122,-80,13)
- target (-105,-64,3)
- lens 52

B_PARITY:
- 900×600
- location (-113,-72,8)
- target (-105,-64,3)
- lens 52

Write:
- `F02_DEST_PARITY_A_900x600.png`
- `F02_DEST_PARITY_B_900x600.png`
- `F02_DESTINATION_PARITY_HASHES.json`

Visual/pixel content must match archived A/B exactly.

If not:
STOP `BLOCKED_F02_DESTINATION_PARITY`

## Phase 9 — F01 regression check before save

Compare current F01 protection manifest against pre-F02 manifest.

Required exact:
- 76 names
- matrix_world
- dimensions
- materials
- parents
- operational visibility

If any F01 difference:
STOP `BLOCKED_F02_F01_REGRESSION`

## Phase 10 — integrated collision preflight

Before declaring F02 complete, compute union world bounds of the 79 accepted Daycare objects.

Write exact:
- min/max XYZ
- center
- extents
- horizontal radius

Run integrated camera search around F02 center.

Azimuths:
0°,45°,90°,135°,180°,225°,270°,315°.

Initial horizontal distance:
`D=max(1.65*R,18m)`

Camera Z:
`max(max_z+6m, Cz+0.75*D)`

Target:
`(Cx,Cy,Cz+0.10*Hz)`

Lens:
52 mm preferred; 45 mm minimum.

Run 9-ray line-of-sight test to:
- center
- ±30% X
- ±30% Y
- four upper-offset corner samples

Accept candidate only if:
- >=7/9 clear rays
- camera not inside geometry
- no immediate architectural intersection within 1m
- F02 fully in frame
- projected F02 area 30–65%

Do not hide/quarantine any other facility automatically.

If no candidate passes:
STOP `BLOCKED_F02_INTEGRATED_COLLISION`

Report all first-hit blockers and do not mutate them.

## Phase 11 — final human-review renders

A_CONTEXT:
- 1440×960
- location (-122,-80,13)
- target (-105,-64,3)
- lens 52

B_FUNCTIONAL:
- 1440×960
- location (-113,-72,8)
- target (-105,-64,3)
- lens 52

D_INTEGRATED_CONTEXT:
- selected integrated camera
- 1440×960

D_PREVIEW:
- same selected camera and scene state
- 900×600

Required visible Daycare cues:
- child-scale activity tables/chairs
- play rug/blocks
- nap/rest separation
- cots/soft nook
- reading shelf/bins
- cubbies
- child-height handwash
- caregiver station
- low partition
- coherent child-scale zoning

## Phase 12 — save/export

Save canonical Blend in place.

Export canonical GLB using current project export policy and visible-object policy.

Create:
- `F02_BASELINE_HASHES.json`
- `F02_REPLAY_CHECKPOINTS.json`
- `F02_REPLAY_SOURCE_MANIFEST.json`
- `F02_SOURCE_RENDER_HASHES.json`
- `F02_CURRENT_PRE_RESTORE_MANIFEST.json`
- `F02_DESTINATION_MANIFEST.json`
- `F02_DESTINATION_PARITY_HASHES.json`
- `F02_F01_PROTECTION_BEFORE.json`
- `F02_F01_PROTECTION_AFTER.json`
- `F02_INTEGRATED_CAMERA_VALIDATION.json`
- `F02_FINAL_HASHES.json`
- `F02_VALIDATION.json`

## Phase 13 — Git/log

Create exactly:
`coordination/Logs/REV005_F02_DAYCARE_RESTORE_CODEX_LOG.md`

Commit/push:
- canonical Blend/GLB
- F02-only evidence/render files
- F02 log

Do not edit TASKS.md.
Do not edit locked criteria/workflow.
Do not begin F03.

## STOP

Final state:
`AWAITING_GPT_FACILITY_AUDIT_F02`

Return only:
- final state
- historical replay source hash
- source composition 41+38=79
- V03 dimensional cross-check
- source A/B visual hash/parity
- destination count/parity
- F01 protection parity
- integrated camera XYZ/target/lens
- clear rays/9
- screen coverage %
- A/B/D render paths
- 900 preview path
- final Blend/GLB hashes
- commit SHA
- full GitHub log URL
