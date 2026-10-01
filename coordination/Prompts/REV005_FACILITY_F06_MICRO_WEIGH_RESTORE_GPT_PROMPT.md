# M08.36 — F06 MICRO-INGREDIENT WEIGH / DISPENSE HISTORICAL RESTORATION

## Scope

Execute F06 only.

Facility:

`Micro-ingredient Weigh / Dispense`

This is a Class R historical accepted-facility restoration.

Do not begin F07.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F06_MICRO_WEIGH_HISTORICAL_SOURCE_PROVENANCE.md`
4. `coordination/Audits/REV005_FACILITY_F06_MICRO_WEIGH_GPT_AUDIT_CRITERIA.md`
5. historical V01–V05 build scripts
6. historical V05 renderer
7. F05 final accepted audit and current F01–F05 protection evidence

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

Re-read local root `TASKS.md` after sync.

It must authorize:

`M08.36 — Facility-Gated F06 Micro-ingredient Weigh / Dispense historical restoration`

If not, STOP before mutation.

## Locked canonical baseline

Blend:

`3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Required SHA-256:

`E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`

GLB:

`3d\revisions\REV005\POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`

Required SHA-256:

`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If either differs:

STOP `BLOCKED_F06_CANONICAL_BASELINE_MISMATCH`.

## Phase 1 — protect all accepted prior state

Before any canonical mutation, capture exact manifests for:

- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted primary 54
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- `V09_RESTAURANT_RIGHT_WALL` accepted F04-X01 quarantine state
- historical Glass Deck source
- historical Wellness/pavilion state

For protected objects record:
- name
- matrix_world
- dimensions
- materials
- parent
- collections
- hide_render
- hide_viewport
- custom properties

For protected collections/layer collections also record:
- collection hide_render
- collection hide_viewport
- layer exclude
- layer hide_viewport

Write:

`output/rev005-facility-gated/F06_micro_weigh/F06_PROTECTION_BEFORE.json`

## Phase 2 — detached historical replay

Create a detached OS-temp worktree from the historical source commit used by the accepted Class R pipeline:

`420038365847de763d64c8583a9e31ac5a6bd677`

Historical starting Blend expected SHA-256:

`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay the committed V01 → V02 → V03 → V04 → V05 build sequence exactly.

Do not patch the historical modeling scripts.

If the starting source cannot be proven:

STOP `BLOCKED_F06_HISTORICAL_SOURCE_BASELINE`.

## Phase 3 — resolve exact historical V05 selection

Use the original V05 renderer selection logic:

`objects_for("Micro-ingredient weigh / dispense", record)`

Required final selected count:

**43**

Expected contribution decomposition:

- BASE = 7
- V01 = 12
- V02 = 23
- V03 = 0
- V04 = 0
- V05 = 1
- total = 43

Classify contribution using the detached replay and actual object provenance, not only string heuristics.

Write:

`F06_REPLAY_SOURCE_MANIFEST_43.json`

For every selected object record:
- contribution source
- name/type
- collections
- matrix_world
- world center XYZ
- dimensions
- material slots
- parent
- data block
- modifiers
- hide flags
- custom properties

If total count or contribution decomposition differs:

STOP `BLOCKED_F06_HISTORICAL_SELECTION_MISMATCH`

and do not mutate the canonical model.

## Phase 4 — dimensional verification

Validate the exact selected historical geometry against:

`coordination/Audits/REV005_F06_MICRO_WEIGH_HISTORICAL_SOURCE_PROVENANCE.md`

At minimum explicitly validate:

### V01 anchors
- `RM_WEIGH_BOOTH`
- `RM_WEIGH_SCALE_TABLE`
- four `RM_WEIGH_BIN_*`
- four `RM_WEIGH_HOPPER_*`
- `RM_WEIGH_BALANCE`
- `RM_WEIGH_TRANSFER_CART`

### V02 anchors
- `V02_WEIGH_BOOTH_BACK`
- `V02_WEIGH_BOOTH_SIDE`
- four `V02_WEIGH_HOPPER_*`
- four `V02_WEIGH_HOPPER_VALVE_*`
- four `V02_WEIGH_DOSING_CHUTE_*`
- `V02_WEIGH_BALANCE_TABLE`
- three `V02_PRECISION_BALANCE_*`
- three `V02_BALANCE_BOWL_*`
- `V02_WEIGH_TRANSFER_TOTE`
- `V02_WEIGH_OPERATOR_TABLE`

### V05
- one evidence anchor at the Micro-Weigh origin

Tolerance:
- center/dimensions <= 0.001 m
- pipe/chute endpoints <= 0.001 m
- rotation <= 0.0001 rad

Write:

`F06_PRIMARY_DIMENSIONAL_VALIDATION.json`

Any mismatch:

STOP `BLOCKED_F06_DIMENSIONAL_SOURCE_MISMATCH`.

## Phase 5 — reproduce historical V05 A/B/C

Use the exact original V05 `show_only()` semantics and Workbench setup.

Historical cameras:

A:
- camera (-16,40,12)
- target (-5,50,3)
- lens 52 mm / sensor 36 mm

B:
- camera (-11,45,8)
- target (-5,50,3)
- lens 52 mm / sensor 36 mm

C:
- camera (-3,49,8)
- target (-5,50,3)
- lens 52 mm / sensor 36 mm

Archived references:

- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_A_WIDE.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_C_PROCESS_OR_DETAIL.png`

Render detached replay source at 900×600.

Require:
- same dimensions;
- exact decoded-pixel parity preferred;
- only sparse antialias-edge differences may proceed for independent GPT review;
- structural difference is a hard stop.

Write:

`F06_SOURCE_RENDER_PARITY.json`

Structural mismatch:

STOP `BLOCKED_F06_SOURCE_RENDER_MISMATCH`.

## Phase 6 — create exact 43-object transfer

Create a temporary transfer collection containing exactly the historical V05 43-object selection and required datablock dependencies.

Do not include neighboring-facility objects.

## Phase 7 — inventory current canonical F06 state

Open the canonical current REV005.

Write:

`F06_CURRENT_PRE_RESTORE_MANIFEST.json`

Identify every current Micro-ingredient Weigh / Dispense representation by:
- exact facility metadata match;
- exact historical object identity/prefix;
- current F06-specific collection membership;
- spatial location around the Micro-Weigh area.

Do not use a broad spatial delete.

Do not remove an object solely because it is geometrically nearby.

If ownership is ambiguous between Micro-Weigh and Packaging Warehouse / Toothpaste / Wet Wipes / another neighbor:

STOP `BLOCKED_F06_CURRENT_OWNERSHIP_AMBIGUITY`

and report the exact objects.

Only the conflicting current F06 representation may be unlinked/replaced.

## Phase 8 — restore accepted F06

Destination collection:

`REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`

Append/link exactly 43 historical selected objects.

Preserve:
- matrix_world
- dimensions
- materials
- parents
- object data
- modifiers
- saved historical visibility

Write:

`F06_DESTINATION_43_MANIFEST.json`

Destination count must be exactly 43.

## Phase 9 — destination historical parity

Run exact V05 `show_only()` QA semantics on the restored destination 43.

Remember V05 temporarily hides selected names containing:
- `_LEFT`
- `_RIGHT`
- `_BACK`
- `_SOFFIT`
- `_CEILING_BEAM`

This hiding is QA-only.
Do not save it into the canonical model.

Render:

- `F06_DEST_PARITY_A_900x600.png`
- `F06_DEST_PARITY_B_900x600.png`
- `F06_DEST_PARITY_C_900x600.png`

Write:

`F06_DESTINATION_PARITY.json`

Require structural visual parity with the archived V05 references.

Structural mismatch:

STOP `BLOCKED_F06_DESTINATION_PARITY`.

## Phase 10 — prior-PASS protection

Rebuild the protection manifest after the F06 restoration.

Write:

`F06_PROTECTION_AFTER.json`

Compare against Phase 1.

Require zero unauthorized differences for all F01–F05 accepted geometry and all locked quarantine/historical states.

Any prior-PASS regression:

STOP `BLOCKED_F06_PRIOR_PASS_REGRESSION`.

## Phase 11 — integrated current-context camera search

Do not equate LOS success with visual acceptance.

Start with historical A/B/C, then test current-context alternatives.

Render at least **12** true integrated 900×600 candidate previews from the current saved model state.

No QA-only hiding.
No neighbor mutation.
No temporary quarantine for the final candidate.

Candidate requirements:
- camera outside geometry;
- >=7/9 clear LOS rays across functional samples;
- booth/enclosure readable;
- hopper row readable;
- hopper valves/dosing path readable;
- precision balance stations readable;
- balance table/workflow readable;
- transfer tote/cart readable;
- operator/service access understandable;
- no unrelated structure dominates;
- primary functional cluster not materially clipped;
- legitimate current context remains visible.

Suggested sample targets:
- booth center
- hopper row left/right
- two dosing chutes
- two precision balances
- transfer tote/cart
- operator table/access zone

For every candidate record:
- camera XYZ
- target XYZ
- lens
- LOS results
- blocker names
- visual-cue booleans
- preview path

Write:

`F06_INTEGRATED_CAMERA_CANDIDATES.json`

Do not auto-select the first 9/9 camera.

Rank primarily by actual visual readability.

If no visually acceptable camera exists:

STOP `BLOCKED_F06_INTEGRATED_VIEW`

without modifying neighbor geometry.

## Phase 12 — final QA

Using the restored saved canonical state, produce:

A_CONTEXT:
- 1440×960
- useful contextual view

B_FUNCTIONAL:
- 1440×960
- focus on hoppers/dosing/balance workflow

C_PROCESS_OR_DETAIL:
- 1440×960
- process/detail view

D_INTEGRATED_CONTEXT:
- 1440×960
- selected integrated candidate

D preview:
- same camera/state
- 900×600

Required final cues:
- weigh booth
- hoppers
- valves/dosing chutes
- precision balances
- transfer tote/cart
- workflow/access organization

## Phase 13 — save/export/evidence

Only after all gates pass:

Save canonical Blend.

Export canonical GLB under the current project export visibility policy.

Create:

- `F06_BASELINE_HASHES.json`
- `F06_REPLAY_SOURCE_MANIFEST_43.json`
- `F06_PRIMARY_DIMENSIONAL_VALIDATION.json`
- `F06_SOURCE_RENDER_PARITY.json`
- `F06_CURRENT_PRE_RESTORE_MANIFEST.json`
- `F06_DESTINATION_43_MANIFEST.json`
- `F06_DESTINATION_PARITY.json`
- `F06_PROTECTION_BEFORE.json`
- `F06_PROTECTION_AFTER.json`
- `F06_PROTECTION_DIFF.json`
- `F06_INTEGRATED_CAMERA_CANDIDATES.json`
- `F06_INTEGRATED_CAMERA_VALIDATION.json`
- `F06_FINAL_HASHES.json`
- `F06_VALIDATION.json`

Evidence directory:

`output/rev005-facility-gated/F06_micro_weigh/`

Required log:

`coordination/Logs/REV005_F06_MICRO_WEIGH_RESTORE_CODEX_LOG.md`

## Git scope

Commit/push:
- canonical Blend/GLB
- F06-only evidence/renders
- F06 log

Do not edit root `TASKS.md`.
Do not edit locked criteria/provenance.
Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06`
