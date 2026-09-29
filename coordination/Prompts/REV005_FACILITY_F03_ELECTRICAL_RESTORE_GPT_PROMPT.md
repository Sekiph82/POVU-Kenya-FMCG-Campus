# F03 — ELECTRICAL / LV-MV ROOM — EXACT HISTORICAL RESTORATION

## ONE FACILITY ONLY

Active facility:
**F03 — Electrical / LV-MV Room**

Do not touch F04 or any other facility.

Read:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F03_ELECTRICAL_HISTORICAL_SOURCE_PROVENANCE.md`
4. `coordination/Audits/REV005_FACILITY_F03_ELECTRICAL_GPT_AUDIT_CRITERIA.md`
5. historical V01–V05 build scripts and V05 renderer from detached temp worktree

## Canonical baseline

Root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Blend:
`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

GLB:
`3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

Required pre-F03 hashes:

Blend:
`E935539393BBF83173004E7BBA97A5432818C355752ABAA55A88F685C707A0E8`

GLB:
`2F593CC82ED68499B5F23C64495229CFEB482C0C44C64F341938802B4A68C277`

If either differs:
STOP `BLOCKED_F03_CANONICAL_BASELINE_MISMATCH`

Output root:
`output\rev005-facility-gated\F03_electrical_lv_mv\`

## Protected prior PASS facilities

Before any mutation create full protection manifests for:

### F01 Caps & Trigger
Expected accepted object count: **76**

### F02 Daycare / Crèche
Expected accepted object count: **79**

For each protected object record:
- name
- matrix_world
- dimensions
- materials
- parent
- hide_viewport
- hide_render

Also verify:
- V09 Glass Deck replacement collection remains quarantined
- historical Glass Deck source objects remain unchanged

## Phase 1 — detached historical replay

Create system-temp detached worktree at:

`420038365847de763d64c8583a9e31ac5a6bd677`

Never create another Desktop project copy.

Verify initial temp Blend SHA-256:

`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Run in exact order:
1. `build_rev005_interior_remediation_v01.py`
2. `build_rev005_interior_remediation_v02.py`
3. `build_rev005_interior_remediation_v03.py`
4. `build_rev005_interior_remediation_v04.py`
5. `build_rev005_interior_remediation_v05.py`

Do not patch historical modeling code.

Write:
`F03_REPLAY_CHECKPOINTS.json`

## Phase 2 — exact historical source selection

Use original V05:

`objects_for("Electrical / LV-MV room", record)`

Required total:
**30**

Required composition:
- BASE 7
- V01 23
- V02 0
- V03 0
- V04 0
- V05 0

BASE inventory contains 8 objects; `REV005_LV_SAFETY_SIGN` must be excluded by historical label filtering.

Write:
`F03_REPLAY_SOURCE_MANIFEST.json`

For all 30 objects record:
- source category BASE/V01
- name/type
- collection(s)
- parent
- matrix_world 16 values
- location XYZ
- rotation XYZ radians
- scale XYZ
- dimensions XYZ metres
- data block
- materials
- modifiers
- constraints
- hide flags
- custom properties

If count/composition differs:
STOP `BLOCKED_F03_REPLAY_COMPOSITION`

## Phase 3 — exact V01 dimensional cross-check

The 23 V01 objects must reconcile numerically with the provenance file.

### Five switchgear X positions

X centers:
**107, 109, 111, 113, 115 m**

For each X:

#### Switchgear
- center: (X,62.2,2.75)
- dimensions: 1.45×1.20×3.40 m

#### Panel door
- center: (X,61.55,2.75)
- dimensions: 1.00×0.08×2.40 m

#### Breaker window
- center: (X,61.49,3.00)
- dimensions: 0.38×0.05×0.75 m

#### Cable riser
- start: (X,62.9,4.5)
- end: (X,62.9,5.4)
- radius: 0.09 m

### Busbar
- center: (111,62.9,5.5)
- dimensions: 9.00×0.18×0.18 m

### Service clearance
- center: (111,59.5,1.36)
- dimensions: 8.50×1.00×0.05 m

### Remote panel
- center: (114,60,2.4)
- dimensions: 1.40×0.50×2.20 m

Tolerance:
<=0.001 m for coordinates/dimensions/endpoints.

If mismatch:
STOP `BLOCKED_F03_V01_DIMENSIONAL_SOURCE_MISMATCH`

## Phase 4 — reproduce archived V05 source A/B

Run original V05 renderer.

A_WIDE:
- loc (117,50,11)
- target (111,61,3)
- lens 52 mm
- sensor 36 mm
- 900×600
- archived SHA-256:
`2F3BDEEAEDDC850B3CF23E4125171EA5CF9858C4883FC146C3B69E6F4EE892A4`

B_FUNCTIONAL:
- loc (113,56,7)
- target (111,61,3)
- lens 52 mm
- sensor 36 mm
- 900×600
- archived SHA-256:
`850EAB71C210E923B9042382E373DD42421B3E2A4A6CED281C294E43A05FFA7A`

Write:
`F03_SOURCE_RENDER_HASHES.json`

If raw PNG metadata differs, decoded visual pixel parity must still be exact.

If visual content differs:
STOP `BLOCKED_F03_SOURCE_RENDER_MISMATCH`

Only now may canonical mutation begin.

## Phase 5 — create exact transfer library

Create temp collection:

`F03_ELECTRICAL_LV_MV_ACCEPTED_V05_REPLAY_TRANSFER`

Include exactly the 30 selected objects + required dependencies.

Do not include:
- REV005_LV_SAFETY_SIGN
- unrelated facilities

Do not redesign or simplify switchgear.

## Phase 6 — inventory/remove only current broken F03

Open canonical current REV005.

Write:
`F03_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify current Electrical/LV-MV representation via:
- owner inventory names
- facility metadata
- RM_LV_* historical names
- V08/V09 dedicated Electrical objects/collections
- prior F03 attempt collection if any

Record first.

Remove/unlink only current Electrical/LV-MV representation that conflicts with incoming accepted 30-object source.

Do not touch F01/F02/other facilities.

## Phase 7 — append exact accepted F03

Destination collection:

`REV005_FG_F03_ELECTRICAL_LV_MV_ACCEPTED_V05_REPLAY`

Append local data.

For all 30 selected objects preserve:
- world transforms
- dimensions
- data
- materials
- parent relationships
- accepted visibility

Parity tolerances:
- location <=0.001 m/axis
- rotation <=0.0001 rad/axis
- scale <=0.0001/axis
- dimensions <=0.001 m/axis

Write:
`F03_DESTINATION_MANIFEST.json`

## Phase 8 — destination A/B parity

Use facility-only visibility and exact historical V05 Workbench settings.

A:
- 900×600
- loc (117,50,11)
- target (111,61,3)
- lens 52

B:
- 900×600
- loc (113,56,7)
- target (111,61,3)
- lens 52

Write:
- `F03_DEST_PARITY_A_900x600.png`
- `F03_DEST_PARITY_B_900x600.png`
- `F03_DESTINATION_PARITY_HASHES.json`

Require visual/pixel parity with archived A/B.

If not:
STOP `BLOCKED_F03_DESTINATION_PARITY`

## Phase 9 — F01/F02 regression gate

Compare before/after manifests.

F01:
- exactly 76 accepted objects unchanged

F02:
- exactly 79 accepted objects unchanged

Required exact:
- names
- matrix_world
- dimensions
- materials
- parent
- accepted visibility

If any mismatch:
STOP `BLOCKED_F03_PRIOR_PASS_REGRESSION`

## Phase 10 — integrated collision preflight

Compute union world bounds of accepted 30 F03 objects.

Run 8 azimuths:
0,45,90,135,180,225,270,315°.

Initial:
- D = max(1.65*horizontal_radius,18 m)
- camera Z = max(max_z+6 m, Cz+0.75D)
- target = (Cx,Cy,Cz+0.10Hz)
- lens 52 mm preferred; 45 mm minimum
- near clip 0.10 m
- far clip 1000 m

Nine target rays:
- center
- ±30% X
- ±30% Y
- four upper-offset corner samples

Candidate PASS:
- >=7/9 clear rays
- no immediate architectural intersection within 1m
- camera not inside geometry
- F03 fully inside frame
- projected F03 screen area 30–65%

Do not automatically hide/quarantine another facility.

If no candidate passes:
STOP `BLOCKED_F03_INTEGRATED_COLLISION`
and report exact blockers.

## Phase 11 — final human-review renders

A_CONTEXT:
- 1440×960
- loc (117,50,11)
- target (111,61,3)
- lens 52

B_FUNCTIONAL:
- 1440×960
- loc (113,56,7)
- target (111,61,3)
- lens 52

D_INTEGRATED_CONTEXT:
- selected integrated camera
- 1440×960

D_PREVIEW:
- same camera/state
- 900×600

Required visible identity:
- five-dense-switchgear row
- visible cabinet doors/front faces
- breaker/inspection windows
- five cable risers
- overhead 9 m busbar
- front service-clearance strip
- remote service panel
- original eyewash/PPE safety cues
- readable service aisle

## Phase 12 — save/export/evidence

Save canonical Blend in place.

Export canonical GLB under current export policy.

Create:
- F03_BASELINE_HASHES.json
- F03_REPLAY_CHECKPOINTS.json
- F03_REPLAY_SOURCE_MANIFEST.json
- F03_SOURCE_RENDER_HASHES.json
- F03_CURRENT_PRE_RESTORE_MANIFEST.json
- F03_DESTINATION_MANIFEST.json
- F03_DESTINATION_PARITY_HASHES.json
- F03_F01_PROTECTION_BEFORE.json
- F03_F01_PROTECTION_AFTER.json
- F03_F02_PROTECTION_BEFORE.json
- F03_F02_PROTECTION_AFTER.json
- F03_INTEGRATED_CAMERA_VALIDATION.json
- F03_FINAL_HASHES.json
- F03_VALIDATION.json

## Phase 13 — log/Git

Create exactly:

`coordination/Logs/REV005_F03_ELECTRICAL_RESTORE_CODEX_LOG.md`

Commit/push only:
- canonical Blend/GLB mutation
- F03 evidence/renders
- F03 log

Do not edit TASKS.md.
Do not edit locked criteria/workflow.
Do not begin F04.

## STOP

Final state:

`AWAITING_GPT_FACILITY_AUDIT_F03`

Return only:
- final state
- source composition 7+23=30
- dimensional cross-check
- source A/B parity
- destination count/parity
- F01 protection parity
- F02 protection parity
- integrated camera XYZ/target/lens
- clear rays/9
- screen coverage %
- A/B/D render paths
- D 900×600 preview path
- final Blend/GLB hashes
- commit SHA
- full GitHub log URL
