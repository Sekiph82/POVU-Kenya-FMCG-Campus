# F01 — CAPS & TRIGGER ASSEMBLY — HISTORICAL PIPELINE REPLAY RESTORATION V03

## ONE FACILITY ONLY

Active facility:
**F01 — Caps and Trigger Assembly**

Do not touch any other facility.
Do not begin Facility 02.

Read in order:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F01_HISTORICAL_PIPELINE_REPLAY_PROVENANCE_V03.md`
4. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT_CRITERIA.md`
5. historical scripts V01–V05 and V05 renderer from the detached worktree

## Critical correction

Do NOT expect the initial Git source Blend to contain 76 Caps objects.

The correct historical construction is:

- base selected visible objects: **7**
- V01 Caps adds: **21**
- V02 Caps adds: **47**
- V03 Caps adds: **0**
- V04 Caps adds: **0**
- V05 evidence anchor: **1**

Total accepted V05 selection:
**76**

The previous F01 V02 stop at 7 objects was correct because it tested the base before replay.

## Canonical current files — DO NOT MUTATE YET

Root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Blend:
`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Current expected SHA-256:
`46D427377C315FF8838CBF6917DD469E3F88D14F49E52BE0C18F8C0CFE3D68E8`

GLB expected SHA-256:
`F09D1E5F4A3581509C33453C88B576A67BB6D2CAFDC08532B05F342BC18F6DCF`

Output:
`output\rev005-facility-gated\F01_caps_trigger\`

Preserve the truthful baseline already captured by the blocked attempts.

## PHASE 1 — create isolated system-temp historical worktree

Use OS/system temp, not Desktop and not a permanent project copy.

Suggested pattern:
`%TEMP%\POVU_F01_V05_REPLAY_<unique>`

Use:
`git worktree add --detach <TEMP_WORKTREE> 420038365847de763d64c8583a9e31ac5a6bd677`

This worktree is temporary evidence machinery only.

Verify the temp canonical Blend exists.

Initial temp Blend SHA-256 MUST be:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

If not:
STOP `BLOCKED_F01_REPLAY_BASE_HASH`

## PHASE 2 — replay the exact historical pipeline

Use the same Blender executable/environment currently used by the project.

Run these scripts FROM THE TEMP WORKTREE, against the TEMP worktree Blend, in this exact order:

1. `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v01.py`
2. `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v02.py`
3. `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v03.py`
4. `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v04.py`
5. `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v05.py`

Do not copy these scripts into the canonical working tree.
Do not patch their modeling functions.
Do not run them against canonical current REV005.

After each stage compute temp Blend SHA-256 and write:
`F01_REPLAY_CHECKPOINTS.json`

Historical expected diagnostic hashes:

- initial:
  `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
- after V01:
  `484E495E9F2689A73BE4DDF7297FEAF96D3227B0E2696A5174A6942E3625D26F`
- after V02:
  `9BEE6F87D7762BC415F15047DC287D7B591C44C83FF8E39C226E6A07FD480B0C`
- after V03:
  `9E9A63A2D7AAFA5667CD0A41DFDE746CB2F2A7751F29DAB259CA30E8A99A238F`
- after V04:
  `EC1B7ABDB86A8FCF1443E780497B49FDDD4268B57EC48106D6D2FDB2D00008BB`
- after V05:
  `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

Record MATCH/MISMATCH per checkpoint.

Checkpoint mismatch alone does not authorize canonical mutation and does not by itself block. The hard source proof is Phases 3–4.

## PHASE 3 — prove exact 76-object composition

After V05 replay, use the exact `objects_for()` logic from the TEMP worktree's:
`render_rev005_interior_remediation_v05.py`

Group:
`Caps and trigger assembly`

Required total:
**76**

Reconcile exactly:

### Base = 7
- REV005_Caps_Triggers_OPERATOR_STATION_BODY
- REV005_Caps_Triggers_OPERATOR_STATION_PANEL
- REV005_Caps_Triggers_SAFETY_EYEWASH
- REV005_Caps_Triggers_SAFETY_PPE
- REV005_Caps_Triggers_STAGING_0
- REV005_Caps_Triggers_STAGING_1
- REV005_Caps_and_trigger_assembly_FLOOR

The inventory's `SAFETY_SIGN` and `REV005_LABEL_CAPS_TRIGGERS` are excluded by the historical label filter.

### V01 = 21
Must include:
- RM_CAPS_ROTARY_BOWL
- RM_CAPS_BOWL_CENTER
- RM_CAPS_FEED_TRACK
- RM_TRIGGER_FEEDER
- RM_CAP_TRIGGER_ASSEMBLY_LINE_BED
- RM_CAP_TRIGGER_ASSEMBLY_LINE_ROLLER_0..4
- RM_CAP_TRIGGER_ASSEMBLY_LINE_GUARD_A
- RM_CAP_TRIGGER_ASSEMBLY_LINE_GUARD_B
- RM_TRIGGER_PICK_PLACE_0..3
- RM_CAP_FEEDER_0..3
- RM_CAPS_REJECT_STATION

### V02 = 47
Must include:
- V02_CAPS_BOWL_FEEDER
- V02_CAPS_BOWL_RIM
- V02_CAPS_BOWL_TRACK
- V02_TRIGGER_MAGAZINE
- V02_TRIGGER_SLOT_0..4
- V02_CAP_TRIGGER_CAROUSEL
- V02_ASSEMBLY_NEST_0..5
- V02_CAP_COMPONENT_0..5
- V02_TRIGGER_COMPONENT_0..5
- V02_PICK_HEAD_COLUMN_0..2
- V02_PICK_HEAD_0..2
- V02_PICK_HEAD_DROP_0..2
- V02_CAP_TRIGGER_OUTFEED_FRAME
- V02_CAP_TRIGGER_OUTFEED_ROLLER_0..6
- V02_CAP_TRIGGER_OUTFEED_SIDE_A
- V02_CAP_TRIGGER_OUTFEED_SIDE_B

### V05 = 1
- V05_EVIDENCE_ANCHOR_CAPS
  - location (52,31,1.08)
  - dimensions (0.2,0.2,0.12)

No V03 or V04 Caps objects.

Write:
`F01_REPLAY_SOURCE_MANIFEST.json`

For all 76:
- source category BASE/V01/V02/V05
- name/type
- collection(s)
- parent
- matrix_world 16 values
- location XYZ
- rotation XYZ radians
- scale XYZ
- dimensions XYZ metres
- data block
- material slots
- modifiers
- constraints
- hide_viewport/hide_render
- custom properties

If total != 76 or category counts != 7/21/47/1:
STOP `BLOCKED_F01_REPLAY_COMPOSITION`

## PHASE 4 — reproduce archived V05 images exactly

Still in TEMP worktree, run its original:

`3d/revisions/REV005/pipeline/render_rev005_interior_remediation_v05.py`

Do not modify renderer.

The historical renderer itself establishes:
- BLENDER_WORKBENCH
- 900×600
- STUDIO
- MATERIAL color
- shadows/cavity
- 52 mm camera
- exact show_only behavior

For Caps/Trigger, verify generated files SHA-256:

A_WIDE:
`0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`

B_FUNCTIONAL:
`B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`

C_PROCESS_OR_DETAIL:
`229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

Write:
`F01_SOURCE_RENDER_HASHES.json`

ALL THREE must match exactly.

If not:
STOP `BLOCKED_F01_REPLAY_RENDER_MISMATCH`

Only now is canonical mutation permitted.

## PHASE 5 — build an exact transfer library

From the replayed TEMP V05 Blend, transfer exactly the 76 selected objects plus required data dependencies.

Create temp collection:
`F01_CAPS_TRIGGER_ACCEPTED_V05_REPLAY_TRANSFER`

Link exactly those 76 selected objects into it.

Important V05 visibility semantics:
V02 had hidden V01 focused objects, but V05 `show_only()` rendered all 76. The accepted visual state therefore requires all 76 selected objects to be visible.

For transfer/destination accepted state:
- set `hide_render=False`
- set `hide_viewport=False`

Do not import excluded signs/labels.
Do not import other facilities.

Write a temp transfer Blend/library under system temp.

## PHASE 6 — inventory and remove current broken F01 only

Open canonical current REV005.

Confirm canonical Blend/GLB still match pre-mutation baseline.

Create:
`F01_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify every current Caps/Trigger representation through:
- normalized facility property matching;
- historical BASE/V01/V02 names;
- V05 evidence anchor;
- V08/V09 Caps dedicated collection/object naming;
- prior failed F01 collections if any.

Record all before changes.

Remove/unlink those Caps/Trigger representations only.

Do not change any other facility.

## PHASE 7 — append exact 76-object accepted facility

Append the temp transfer library as local data into:

`REV005_FG_F01_CAPS_TRIGGER_ACCEPTED_V05_REPLAY`

Required:
- exactly 76 selected source objects represented;
- source world transform retained;
- source geometry dimensions retained;
- materials/data/parents/modifiers/constraints retained;
- all 76 visible in viewport/render;
- no labels/signs;
- no unrelated V05 objects.

Parity tolerances:
- location <= 0.001 m/axis
- rotation <= 0.0001 rad/axis
- scale <= 0.0001/axis
- dimensions <= 0.001 m/axis

Write:
`F01_DESTINATION_MANIFEST.json`

## PHASE 8 — destination byte-parity render gate

Before normal integrated rendering, temporarily isolate only the restored 76 F01 objects using the exact historical V05 `show_only()` semantics.

Render in canonical destination at **900×600** with the exact historical Workbench settings and exact historical cameras:

A:
- loc (60,18,13)
- target (52,31,3)
- lens 52 mm

B:
- loc (54,24,8)
- target (52,31,3)
- lens 52 mm

C:
- loc (46,26,8)
- target (52,31,3)
- lens 52 mm

Write:
- `F01_DEST_PARITY_A_900x600.png`
- `F01_DEST_PARITY_B_900x600.png`
- `F01_DEST_PARITY_C_900x600.png`

Required SHA-256 again:

A:
`0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`

B:
`B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`

C:
`229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

Write:
`F01_DESTINATION_PARITY_HASHES.json`

If any destination parity hash differs:
do not claim completion.
STOP `BLOCKED_F01_DESTINATION_PARITY`

## PHASE 9 — final human-review renders

After parity passes, render 1440×960 PNG.

Use exact historical locations/target/lens:

A_CONTEXT:
- loc (60,18,13)
- target (52,31,3)
- lens 52 mm
- `F01_A_CONTEXT.png`

B_FUNCTIONAL:
- loc (54,24,8)
- target (52,31,3)
- lens 52 mm
- `F01_B_FUNCTIONAL.png`

C_DETAIL:
- loc (46,26,8)
- target (52,31,3)
- lens 52 mm
- `F01_C_DETAIL.png`

Then restore normal current scene visibility and render:

D_INTEGRATED_CONTEXT:
- A camera
- 1440×960
- `F01_D_INTEGRATED_CONTEXT.png`

Do not move F01 to fix D.
If unrelated geometry blocks D, record it for GPT; do not mutate another facility.

## PHASE 10 — save/export/validate

Save canonical current Blend in place.

Export canonical GLB using the project's current export policy.

Create exact files:
- F01_REPLAY_CHECKPOINTS.json
- F01_REPLAY_SOURCE_MANIFEST.json
- F01_SOURCE_RENDER_HASHES.json
- F01_CURRENT_PRE_RESTORE_MANIFEST.json
- F01_DESTINATION_MANIFEST.json
- F01_DESTINATION_PARITY_HASHES.json
- F01_FINAL_HASHES.json
- F01_VALIDATION.json

Validation must prove:
- canonical baseline unchanged before Phase 6;
- 7/21/47/1 composition;
- 76 total;
- source A/B/C exact hash match;
- destination A/B/C exact parity hash match;
- transforms within tolerance;
- 1440×960 A/B/C/D present;
- no other facility mutation;
- REV004 unchanged;
- no REV006/.hiveai/tour/second Desktop root.

## PHASE 11 — exact log / Git

Create exactly:
`coordination/Logs/REV005_F01_CAPS_TRIGGER_RESTORE_CODEX_LOG.md`

Commit/push F01 outputs and canonical Blend/GLB changes.

Do not edit TASKS.md.
Do not edit locked criteria/workflow.
Do not start F02.

Verify local HEAD == origin/main and git status clean except permitted ignored local binaries.

## STOP

Final state:
`AWAITING_GPT_FACILITY_AUDIT_F01`

Return only:
- final state
- replay initial source hash
- replay checkpoint hash table
- source composition 7/21/47/1 = 76
- source A/B/C archived hash match
- destination restored object count
- transform parity
- destination A/B/C parity hash match
- final A/B/C/D paths
- Blend/GLB paths and hashes
- commit SHA
- full GitHub Codex log URL
