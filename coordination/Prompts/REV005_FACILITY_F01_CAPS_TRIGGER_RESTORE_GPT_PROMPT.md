# F01 — CAPS & TRIGGER ASSEMBLY — EXACT HISTORICAL RESTORATION V02

## Scope

One facility only:

**Caps and Trigger Assembly**

Do not touch Facility 02 or any other facility except temporary QA visibility toggles.

Read:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F01_SOURCE_PROVENANCE_CORRECTION.md`
4. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT_CRITERIA.md`
5. `coordination/Audits/REV005_INTERIOR_REMEDIATION_V05_GPT_AUDIT.md`
6. historical V05 renderer: `3d/revisions/REV005/pipeline/render_rev005_interior_remediation_v05.py`

Do not execute superseded V10 batch image specs.

## Canonical paths

Root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Blend:
`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

GLB:
`3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

Output:
`output\rev005-facility-gated\F01_caps_trigger\`

## Important provenance correction

The previous F01 attempt stopped correctly because the prompt incorrectly demanded that the Git-materialized Blend equal the local V05-final whole-file hash.

Do NOT require `B4F24C...` from `git show`.

The authoritative Git-materialized source for this equivalence test is:

Commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Expected Git source SHA-256:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Why this is valid to test:
V05 classified Caps & Trigger as `EVIDENCE_ONLY_REMEDIATION`; V05 did not rebuild it. The facility existed in the earlier committed REV005 Blend and V05 only reframed it.

We will prove exact equivalence using object selection + byte-identical V05 renders before mutation.

## Phase 0 — baseline

Do not alter the existing `F01_BASELINE_HASHES.json` if it already truthfully records the unchanged canonical files from the blocked attempt.

If it does not exist, create it before mutation.

Record:
- current Blend SHA-256/size;
- current GLB SHA-256/size;
- branch/HEAD/origin-main;
- git status.

## Phase 1 — materialize Git source

Without checkout/reset:

`git show 420038365847de763d64c8583a9e31ac5a6bd677:3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend > <SYSTEM_TEMP>\F01_GIT_SOURCE.blend`

Compute SHA-256.

Required:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

If mismatch, stop:
`BLOCKED_F01_GIT_SOURCE_HASH`

## Phase 2 — reproduce the exact historical V05 object set

Do NOT select only by `facility` property.

Run the exact historical selection semantics from V05 renderer:
`render_rev005_interior_remediation_v05.py`

Use:
- its inventory file;
- `objects_for(group, record)`;
- group exactly `Caps and trigger assembly`;
- its label-exclusion logic;
- its de-duplication logic.

Write:
`F01_GIT_SOURCE_MANIFEST.json`

For every selected object:
- name
- type
- collection membership
- parent
- 16-value matrix_world
- location XYZ
- rotation XYZ radians
- scale XYZ
- dimensions XYZ metres
- data-block name
- material slots
- modifiers
- constraints
- hide flags
- custom properties

Required selected object count:
**76**

If count != 76, stop:
`BLOCKED_F01_SOURCE_OBJECT_COUNT`

## Phase 3 — prove byte-identical historical visual source

Before touching the current Blend, render the Git source with EXACT V05 renderer settings.

### Workbench settings

- engine = BLENDER_WORKBENCH
- resolution = 900×600
- percentage = 100
- PNG
- film_transparent = false
- shading.light = STUDIO
- shading.color_type = MATERIAL
- show_shadows = true
- show_cavity = true
- cavity_type = WORLD
- curvature_ridge_factor = 1.8
- curvature_valley_factor = 1.2
- background_type = VIEWPORT
- background_color = (0.08,0.10,0.12)

Use V05 `show_only(objs)` behavior, including its shell-occluder handling.

Camera lens 52 mm, sensor width 36 mm.

A:
- loc (60,18,13)
- target (52,31,3)
- file `F01_SOURCE_A_WIDE_900x600.png`
- expected SHA-256:
  `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`

B:
- loc (54,24,8)
- target (52,31,3)
- file `F01_SOURCE_B_FUNCTIONAL_900x600.png`
- expected SHA-256:
  `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`

C:
- loc (46,26,8)
- target (52,31,3)
- file `F01_SOURCE_C_DETAIL_900x600.png`
- expected SHA-256:
  `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

Camera rotation formula:
`(Vector(target)-Vector(location)).to_track_quat("-Z","Y").to_euler()`

All three image hashes MUST match exactly.

If any differs, STOP:
`BLOCKED_F01_SOURCE_RENDER_MISMATCH`

Do not mutate canonical REV005.

## Phase 4 — create exact transfer package

Only after Phase 1–3 PASS.

In the source Blender process:
- create temporary collection `F01_CAPS_TRIGGER_HISTORICAL_TRANSFER`;
- link exactly the selected 76 objects;
- preserve world matrices;
- include necessary parents, mesh/curve data, materials, node groups/images, modifiers/constraint dependencies;
- do not include unrelated facility geometry.

Write transfer Blend to SYSTEM TEMP, not Desktop/project root.

## Phase 5 — inventory current broken F01

Open current canonical REV005.

Write:
`F01_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify all objects currently representing Caps/Trigger through:
- exact facility metadata;
- dedicated V08/V09 Caps/Trigger collections;
- known current F01/broken-restoration collection if present.

Record them before mutation.

Remove/unlink only the broken current Caps/Trigger representation.

## Phase 6 — append historical accepted source

Append transfer collection as local data into destination collection:

`REV005_FG_F01_CAPS_TRIGGER_ACCEPTED_SOURCE`

Do not link externally.

For the 76 source-selected objects, destination parity must satisfy:
- location <= 0.001 m/axis
- rotation <= 0.0001 rad/axis
- scale <= 0.0001/axis
- dimensions <= 0.001 m/axis

Write:
`F01_DESTINATION_MANIFEST.json`

If parity fails, correct it before rendering.

## Phase 7 — cue check

Visually/structurally confirm source geometry includes:
- bowl/feed equipment;
- cap/trigger feed tracks;
- guarded assembly conveyor/cell;
- multiple assembly/work positions;
- reject station.

Do not add invented geometry merely to satisfy this list. Historical source is authoritative.

## Phase 8 — final F01 QA renders

Render 1440×960 PNG, perspective, 52 mm, sensor 36 mm.

A_CONTEXT:
- loc (60,18,13)
- target (52,31,3)
- `F01_A_CONTEXT.png`

B_FUNCTIONAL:
- loc (54,24,8)
- target (52,31,3)
- `F01_B_FUNCTIONAL.png`

C_DETAIL:
- loc (46,26,8)
- target (52,31,3)
- `F01_C_DETAIL.png`

For A/B/C use facility-focused QA visibility equivalent to historical source proof, but do not delete or mutate unrelated objects.

If an unrelated current object obstructs:
1. first use QA-only view-layer exclusion;
2. do not move F01;
3. only if necessary adjust camera <=1.0 m total and target <=0.5 m;
4. log exact adjustment.

Then restore normal current scene visibility and render:

D_INTEGRATED:
- same A camera
- `F01_D_INTEGRATED_CONTEXT.png`

D must prove correct campus integration and no global legacy-unhide regression.

## Phase 9 — save/export

Save current canonical Blend in place.

Export canonical GLB in place using existing project policy.

Create:
- `F01_FINAL_HASHES.json`
- `F01_VALIDATION.json`

Validation must record:
- Git source hash;
- source selected count = 76;
- three historical source-render hashes;
- destination object count/parity;
- four final render dimensions/bytes;
- REV004 unchanged;
- no REV006;
- no `.hiveai`;
- no tour;
- canonical path unchanged.

## Phase 10 — exact log and Git

Create exactly:
`coordination/Logs/REV005_F01_CAPS_TRIGGER_RESTORE_CODEX_LOG.md`

Commit/push only F01 outputs and canonical Blend/GLB changes.

Do not edit TASKS.md or locked criteria.

Verify local HEAD == origin/main and clean status.

## STOP

Stop at exactly:
`AWAITING_GPT_FACILITY_AUDIT_F01`

Do NOT begin Daycare or any other facility.

Return only:
- final state
- Git source hash verification
- source selected-object count
- A/B/C historical source-render hash verification
- restored destination-object count
- transform parity
- four final QA paths
- Blend/GLB paths
- final hashes
- commit SHA
- full GitHub Codex log URL
