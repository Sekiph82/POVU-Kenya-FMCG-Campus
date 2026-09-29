# F01-X01 — QUARANTINE V09 GLASS DECK OVERLAP REGRESSION + RE-RUN F01 INTEGRATED PROOF

## Scope

This is a **cross-facility regression quarantine**, not Glass Deck modeling.

Do not remodel:
- F01 Caps & Trigger
- Glass Deck
- Bottle Blow
- Wet Processing
- any other facility

The only model mutation permitted is to quarantine the proven-invalid V09 Glass Deck replacement collection from viewport/render/export.

Then regenerate F01 integrated-context evidence.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F01_CROSS_FACILITY_OVERLAP_ROOT_CAUSE.md`
3. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT.md`
4. `coordination/Prompts/REV005_FACILITY_F01_D_INTEGRATED_CONTEXT_REMEDIATION_GPT_PROMPT.md`
5. `output/rev005-facility-gated/F01_caps_trigger/F01_DESTINATION_MANIFEST.json`
6. `output/rev005-interior-remediation-v09/V09_BUILD_REPORT.json`
7. `3d/revisions/REV005/audit/REV005_INTERIOR_AUDIT.json`

## Canonical current baseline

Blend SHA-256 before this repair:
`1F2031610251CDCBD064867DB4E925CFD573C621010BDD5A72E17F45BE08D703`

GLB SHA-256 before this repair:
`B2972FB7F6F4B25CD4CC30615B550EAEC5A11037E56EDA3F18D9DC96F27B632D`

Create:
`output/rev005-facility-gated/F01_caps_trigger/F01_X01_BASELINE_HASHES.json`

## Phase 1 — verify the regression numerically before mutation

Open canonical REV005.

### A. F01 footprint

Using exact 76-object F01 manifest and real object bound boxes, compute union world bounds.

Record:
- min/max XYZ
- center
- extent

Expected plan region should reconcile approximately with the historical floor:
- center near `(52,31)`
- floor width/depth near `27×15 m`

### B. true historical Glass Deck

Locate and record world bounds of:
- `GLASS_DECK_LINK`
- `GLASS_DECK_LINK_FLOOR`

Expected source audit values:

`GLASS_DECK_LINK`
- X 66–74
- Y -6–46
- Z 8.2–12.2

`GLASS_DECK_LINK_FLOOR`
- X 66.25–73.75
- Y -5.5–45.5
- Z 8.36–8.54

Use actual current-scene bounds and record them.

If the historical source objects are missing:
STOP `BLOCKED_F01_X01_SOURCE_GLASS_DECK_MISSING`

### C. V09 replacement collection

Locate exact collection:

`REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`

Expected V09 build-report object count:
**117**

Record:
- exact current object count
- each object name
- each object bounds
- collection aggregate world bounds
- aggregate overlap volume/plan overlap with F01

The collection must be identifiable as the V09 replacement boundary.

If collection is missing or materially different from report:
STOP `BLOCKED_F01_X01_V09_COLLECTION_MISMATCH`

Write:
`F01_X01_OVERLAP_DIAGNOSTIC.json`

## Phase 2 — protect F01 and historical Glass Deck before mutation

Create manifests/hashes for:

### F01
All 76 restored objects:
- name
- matrix_world
- dimensions
- materials
- parent
- hide_viewport
- hide_render

### Historical Glass Deck source
At minimum:
- GLASS_DECK_LINK
- GLASS_DECK_LINK_FLOOR
- GLASS_DECK_CENTRAL_LIFT
- GLASS_DECK_CENTRAL_LIFT_FRAME
- all source `GLASS_DECK_*_STAIR_STEP_*` objects found in source audit/current scene

Record their transforms and bounds.

Write:
`F01_X01_PROTECTED_OBJECTS_BEFORE.json`

## Phase 3 — quarantine only the invalid V09 Glass Deck replacement collection

Target collection ONLY:

`REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`

Expected objects:
**117**

Do not delete objects.

For the collection:
- set `hide_viewport = True`
- set `hide_render = True`

For every object directly owned by this V09 replacement collection:
- set `hide_viewport = True`
- set `hide_render = True`
- set custom property:
  - `REV005_CROSS_FACILITY_QUARANTINED = True`
  - `REV005_CROSS_FACILITY_QUARANTINE_REASON = "V09 Glass Deck ground-level envelope overlaps accepted F01 Caps/Trigger footprint; true source Glass Deck is elevated at Z>=8.2m"`
  - `REV005_CROSS_FACILITY_QUARANTINE_OWNER = "F01_X01"`

Do not change:
- object locations
- rotations
- scales
- dimensions
- mesh data
- materials

Do not touch any object outside this one collection.

## Phase 4 — post-quarantine protection check

Recompute and compare:

### F01 76 objects
Required exact parity with Phase 2:
- same 76 names
- matrix_world exact within floating serialization tolerance <=1e-6
- dimensions <=1e-6 m difference
- material slots unchanged
- parent relationships unchanged
- F01 hide flags unchanged from accepted operational state

### historical Glass Deck source
Required:
- source object transforms/bounds unchanged
- no source Glass Deck object received quarantine tag
- source objects remain available according to their prior visibility state

If any protected object changes:
STOP `BLOCKED_F01_X01_PROTECTED_OBJECT_MUTATION`

Write:
`F01_X01_PROTECTED_OBJECTS_AFTER.json`

## Phase 5 — save and export the corrected canonical scene

This quarantine is an intentional canonical REV005 correction.

Save canonical Blend in place.

Export canonical GLB using the existing current project export policy, respecting visibility.

Create:
`F01_X01_FINAL_HASHES.json`

The Blend/GLB hashes are expected to change because the erroneous V09 replacement collection is now quarantined.

Do not treat hash change as failure.

## Phase 6 — rerun integrated camera diagnostics

Now rerun the F01-D camera selection algorithm against the corrected canonical scene.

Use exact 76 F01 objects for target bounds.

Evaluate 8 azimuths:
- 0
- 45
- 90
- 135
- 180
- 225
- 270
- 315 degrees

Initial distance:
`D=max(1.65*R,18m)`

Camera Z:
`max(max_z+6m, Cz+0.75*D)`

Target:
`(Cx,Cy,Cz+0.10*Hz)`

Lens:
- 52 mm preferred
- 45 mm allowed
- never below 45 mm

Near/far:
- 0.10 m
- 1000 m

### 9-ray gate

Same nine target samples as F01-D prompt.

Accept only:
- >=7/9 unobstructed rays
- camera not inside geometry
- F01 fully in frame
- F01 projected image area 30–65%

This time:
**do not temporarily exclude any additional architectural object.**

If no candidate reaches >=7/9 after the proven-invalid Glass Deck replacement is quarantined:
STOP `BLOCKED_F01_X01_REMAINING_INTEGRATION_COLLISION`

In that stop case, report exact remaining first-hit occluders. Do not change them.

## Phase 7 — render integrated evidence

Render from selected camera with normal corrected canonical visibility.

Main:
`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V03.png`
- 1440×960 PNG

Audit preview:
`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V03_PREVIEW_900x600.png`
- 900×600 PNG

Same camera, same scene state.

Write:
`F01_X01_CAMERA_VALIDATION.json`

Record:
- selected camera XYZ
- target XYZ
- lens
- 9-ray table
- clear count
- F01 projected bbox
- screen coverage %
- remaining visible surrounding architecture
- output hashes/bytes/resolutions

## Phase 8 — final scope validation

Verify:
- F01 76 objects unchanged geometrically
- historical source Glass Deck unchanged
- exactly one V09 replacement collection quarantined
- no Bottle Blow mutation
- no Wet Processing mutation
- no other facility mutation
- REV004 unchanged
- no REV006
- no .hiveai
- no tour/video
- no TASKS edit
- no audit-criteria edit

Create:
`F01_X01_VALIDATION.json`

## Phase 9 — Git

Create exact log:
`coordination/Logs/REV005_F01_X01_GLASS_DECK_OVERLAP_QUARANTINE_CODEX_LOG.md`

Commit:
- canonical REV005 Blend/GLB
- F01_X01 JSON evidence
- corrected D V03 1440 render
- 900 preview
- log

Do not begin F02.

## STOP

Final state:
`AWAITING_GPT_F01_X01_INTEGRATED_AUDIT`

Return only:
- final state
- V09 Glass Deck collection object count
- measured F01/V09 Glass Deck overlap
- historical source Glass Deck bounds confirmation
- F01 76-object protection parity
- source Glass Deck protection parity
- new Blend/GLB hashes
- selected camera XYZ/target/lens
- clear rays / 9
- F01 screen coverage %
- 1440 output path/hash
- 900 preview path/hash
- commit SHA
- full GitHub log URL
