# F01 — CAPS & TRIGGER ASSEMBLY — EXACT V05 RESTORATION

## Execution scope

This prompt owns **one facility only**:

**Caps and Trigger Assembly**

Do not touch any other facility except where a temporary QA visibility toggle is required for rendering.

Read first:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT_CRITERIA.md`
4. `coordination/Audits/REV005_INTERIOR_REMEDIATION_V05_GPT_AUDIT.md`

Do not read the superseded V10 batch image specs as executable instructions.

## Canonical workspace

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Canonical current Blend:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Canonical current GLB:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

## Why this is restoration, not remodeling

This facility was independently accepted in V05.

V05 accepted finding:
**recognisable assembly cell with bowl/feed logic, fixtures and multiple work positions.**

V09 is not acceptable because it reduced the facility to a few sparse blocks.

Therefore:
- do not design a new Caps/Trigger line;
- do not approximate V05 with boxes;
- do not reuse V09's sparse nine-object restoration as the model;
- restore the complete V05 geometry exactly.

## Locked historical source

Source commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Source repository path:
`3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Expected V05 source SHA-256:
`B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

Historical facility metadata:
- facility property: `facility == "Caps and Trigger Assembly"`
- V05 QA object count: **76**
- visible cues: bowl feeders; cap/trigger feed tracks; guarded assembly conveyor; reject station.

Historical QA references:
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_A_WIDE.png`
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_C_PROCESS_OR_DETAIL.png`

## Phase 0 — current baseline before any mutation

Create directory:
`output/rev005-facility-gated/F01_caps_trigger/`

Before modifying the Blend, write:
`F01_BASELINE_HASHES.json`

Record SHA-256 and byte size for current Blend and GLB.

Also record:
- current branch;
- current HEAD;
- origin/main;
- current staged/unstaged status.

Do not reset or discard local work.

## Phase 1 — materialize V05 source without changing working tree

Do NOT checkout the V05 commit.

Use an equivalent of:

`git show 420038365847de763d64c8583a9e31ac5a6bd677:3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend > <SYSTEM_TEMP>\POVU_REV005_V05_SOURCE.blend`

The temporary file must be outside the Desktop project tree.

Compute SHA-256.

Expected:
`B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

If it does not match, STOP. Do not mutate the current Blend.

## Phase 2 — extract an exact source manifest

Open the temp V05 Blend in a separate background Blender process.

Identify facility objects using the exact custom property:
`obj.get("facility") == "Caps and Trigger Assembly"`

Also include:
- every parent/ancestor required by those objects;
- object data blocks;
- materials;
- material node groups/images if referenced;
- constraints/modifiers that depend on facility objects.

Write:
`output/rev005-facility-gated/F01_caps_trigger/F01_V05_SOURCE_MANIFEST.json`

For every facility object record:
- object name;
- object type;
- source collection membership;
- parent name;
- matrix_world as 16 numeric values;
- location XYZ;
- rotation_euler XYZ in radians;
- scale XYZ;
- dimensions XYZ in metres;
- mesh/data block name;
- material slot names in order;
- modifier names/types;
- hide_viewport;
- hide_render;
- custom properties.

Sanity check:
V05 historical QA reported **76 visible facility objects**.

A difference is permitted only if the manifest explains parent/helper/non-renderable objects. If you cannot reconcile the count with the historical evidence, STOP at `BLOCKED_F01_SOURCE_MANIFEST_MISMATCH`.

## Phase 3 — create a facility-only transfer Blend

In the V05 background process:

1. Create temporary collection:
   `F01_CAPS_TRIGGER_V05_TRANSFER`
2. Link all exact facility objects into that collection without changing their world matrices.
3. Include required parent chains and dependencies.
4. Write only that collection and dependencies to:
   `<SYSTEM_TEMP>\F01_CAPS_TRIGGER_V05_TRANSFER.blend`

Do not save changes back to the V05 source file.

## Phase 4 — remove the broken current facility only

Open the canonical current REV005 Blend.

Before deletion, create:
`F01_CURRENT_PRE_RESTORE_MANIFEST.json`

Find current objects matching Caps/Trigger using:
- exact `facility` custom property;
- and any V08/V09 clean/restoration collection dedicated to Caps/Trigger.

Record their names and transforms.

Then remove/unlink only the current broken Caps/Trigger objects.

Do not:
- delete neighboring facility objects;
- globally unhide legacy objects;
- change facility world location;
- move campus architecture;
- change REV004.

## Phase 5 — append the exact V05 facility

Append `F01_CAPS_TRIGGER_V05_TRANSFER` into the current REV005 Blend as local data, not linked external data.

Destination collection:
`REV005_FG_F01_CAPS_TRIGGER_ACCEPTED_V05`

Rules:
- preserve each source object's matrix_world exactly;
- preserve parent relationships;
- preserve material assignments;
- preserve mesh/curve data;
- preserve modifiers/constraints where dependencies exist;
- preserve object dimensions;
- do not uniformly scale or translate the restored collection.

After append, programmatically compare destination versus source manifest.

Numerical tolerances:
- location: <= **0.001 m** per axis;
- rotation: <= **0.0001 rad** per axis;
- scale: <= **0.0001** per axis;
- dimensions: <= **0.001 m** per axis.

If outside tolerance, correct the transfer before rendering.

## Phase 6 — visual cue verification before rendering

Before creating QA images, verify the restored scene visibly contains all four accepted cue families:

1. **Bowl/feed equipment**
   - at least one recognisable bowl/feed device from V05;
   - not a single featureless cuboid.

2. **Cap/trigger feed tracks**
   - visible track/chute/feeding relationship;
   - physically associated with the assembly cell.

3. **Guarded assembly conveyor/cell**
   - guarding/frame plus assembly/work zone;
   - conveyor/transfer relationship visible.

4. **Reject station**
   - the V05 reject/outfeed/reject-area geometry present in its historical location.

Do not add replacement geometry merely to satisfy this checklist. The source is the accepted V05 model.

## Phase 7 — locked QA cameras

Use perspective camera with:
- lens: **52 mm**
- sensor width: **36 mm**
- render format: PNG
- resolution: **1440 × 960**
- transparent film: false

Camera A:
- location: **(60.000, 18.000, 13.000) m**
- target: **(52.000, 31.000, 3.000) m**
- output: `F01_A_CONTEXT.png`

Camera B:
- location: **(54.000, 24.000, 8.000) m**
- target: **(52.000, 31.000, 3.000) m**
- output: `F01_B_FUNCTIONAL.png`

Camera C:
- location: **(46.000, 26.000, 8.000) m**
- target: **(52.000, 31.000, 3.000) m**
- output: `F01_C_DETAIL.png`

For all cameras:
`rotation = (target - location).to_track_quat("-Z","Y").to_euler()`

Start with the exact coordinates above.

If a current unrelated facility object that did not exist in V05 obstructs one camera:
- do not move the restored Caps/Trigger facility;
- first create a QA-only view-layer exclusion for the obstructing unrelated object;
- only if exclusion is inappropriate may the camera move;
- maximum camera position adjustment without stopping: **1.0 m total Euclidean distance**;
- maximum target adjustment: **0.5 m**;
- log exact before/after XYZ.

Do not use a wide-angle lens below 45 mm.

## Phase 8 — integrated regression render

Restore normal scene visibility.

Use the same A camera:
- location (60,18,13)
- target (52,31,3)
- lens 52 mm
- 1440×960

Render:
`F01_D_INTEGRATED_CONTEXT.png`

This render must prove:
- Caps/Trigger remains in the correct campus location;
- no obvious overlap with unrelated equipment/architecture;
- restoration did not globally unhide legacy proxies.

## Phase 9 — save/export/validate

Save the canonical Blend in place.

Export canonical GLB in place using the existing project export policy.

Create:
- `F01_DESTINATION_MANIFEST.json`
- `F01_FINAL_HASHES.json`
- `F01_VALIDATION.json`

Validation JSON must include:
- V05 source hash;
- source facility-object count;
- restored destination object count;
- source/destination transform-tolerance result;
- 4 render paths, dimensions and byte sizes;
- unrelated-facility object-count/hash checks where practical;
- REV004 unchanged;
- no REV006;
- no `.hiveai`;
- canonical local path unchanged.

## Phase 10 — Git discipline

Commit:
- canonical Blend/GLB changes;
- F01 manifests/validation;
- four QA PNGs;
- Codex log.

Do not edit:
- root `TASKS.md`;
- locked F01 audit criteria;
- workflow protocol.

Push to `main`.

Verify:
- local HEAD == origin/main;
- git status clean except intentionally ignored project binaries allowed by policy.

## Required Codex log

Create exactly:
`coordination/Logs/REV005_F01_CAPS_TRIGGER_RESTORE_CODEX_LOG.md`

Include:
- source commit/hash verification;
- source manifest count;
- current broken-object count removed;
- destination restored-object count;
- transform comparison result;
- any camera adjustment;
- four QA paths;
- Blend/GLB before and after hashes;
- final commit SHA;
- Git status.

## STOP

After the four renders and artifacts are pushed, STOP.

Do not begin Daycare.
Do not make any other facility change.

Final state:
`AWAITING_GPT_FACILITY_AUDIT_F01`

Return only:
- final state
- V05 source hash verification
- source facility-object count
- restored destination-object count
- transform parity result
- four QA image paths
- Blend path
- GLB path
- final Blend/GLB hashes
- commit SHA
- full GitHub Codex log URL
