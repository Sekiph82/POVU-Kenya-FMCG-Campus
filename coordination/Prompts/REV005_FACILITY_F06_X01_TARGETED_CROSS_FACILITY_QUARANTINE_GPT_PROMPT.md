# M08.38 — F06-X01 TARGETED CROSS-FACILITY QUARANTINE + INTEGRATED RE-AUDIT

## Scope

Execute F06-X01 only.

This is a targeted cross-facility correction after the camera-only R01 proved that no complete current-context view is possible under the present saved geometry/visibility.

Do not begin F07.

Do not redesign F06.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_FACILITY_F06_MICRO_WEIGH_GPT_AUDIT_CRITERIA.md`
4. `coordination/Audits/REV005_F06_MICRO_WEIGH_GPT_AUDIT_V01.md`
5. `coordination/Audits/REV005_F06_X01_CROSS_FACILITY_BLOCKER_ROOT_CAUSE.md`
6. `coordination/Audits/REV005_F06_X01_TARGETED_QUARANTINE_GPT_CRITERIA.md`
7. `coordination/Logs/REV005_F06_R01_INTEGRATED_CAMERA_REMEDIATION_CODEX_LOG.md`
8. all committed F06 and F06/R01 evidence

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

Re-read root `TASKS.md`.

It must authorize:

`M08.38 — Facility-Gated F06-X01 targeted cross-facility quarantine + integrated re-audit`

If not, STOP before mutation.

## Locked canonical baseline

Blend SHA-256:

`BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`

GLB SHA-256:

`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If either differs:

STOP `BLOCKED_F06_X01_CANONICAL_HASH_MISMATCH`.

## Why X01 is authorized

Accepted F06 bounding box:

- X = -15.5 … 5.5
- Y = 45.0 … 55.0

V09 Toothpaste envelope:

- X = -33.0 … 9.0
- Y = 33.5 … 52.5
- overlap with F06 = 157.5 m² = 75% of F06 plan footprint

V09 Wet Wipes envelope:

- X = -4.0 … 48.0
- Y = 33.5 … 52.5
- overlap with F06 = 71.25 m² = 33.93% of F06 plan footprint

These V09 envelopes belong to facilities that remain independently unaccepted and physically occupy the restored accepted F06 area.

This task does not authorize a general cleanup of neighbors.

## Phase 1 — exact pre-mutation proof

Create:

`output/rev005-facility-gated/F06_micro_weigh/X01/F06_X01_QUARANTINE_BEFORE.json`

For the seven authorized objects, record:

- exact name
- type
- facility metadata
- all collections
- matrix_world
- location
- rotation
- scale
- dimensions
- materials
- parent
- data block
- hide_viewport
- hide_render
- custom properties
- V09 remediation provenance properties

Also record equivalent protected signatures for:
- F01 76
- F02 79
- F03 30
- F04 59
- F05 54
- F06 43
- Glass Deck quarantine 117
- Training quarantine 81
- Restaurant right-wall accepted quarantine
- historical Glass Deck / Wellness protected state

## Phase 2 — ownership and builder validation

Validate the seven exact authorized objects against the committed V09 builder.

Authorized list:

### Toothpaste
1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`

### Wet Wipes
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

Require for every object:
- expected facility ownership;
- expected V09 structural-envelope provenance;
- transform/dimensions consistent with the committed V09 `env()` construction;
- not a member of any accepted F01-F06 destination collection.

If any of the seven fails this gate:

STOP `BLOCKED_F06_X01_AUTHORIZED_OBJECT_IDENTITY_MISMATCH`.

Do not substitute another object.

## Phase 3 — targeted saved quarantine

For exactly the seven authorized objects:

- set `hide_viewport = true`
- set `hide_render = true`

Add:

- `REV005_CROSS_FACILITY_QUARANTINED = true`
- `REV005_CROSS_FACILITY_QUARANTINE_OWNER = "F06_X01"`
- `REV005_CROSS_FACILITY_QUARANTINE_REASON = "Unaccepted V09 Toothpaste/Wet Wipes envelope structurally overlaps accepted F06 Micro-ingredient Weigh / Dispense footprint"`

Do not:
- delete
- unlink
- move
- rotate
- scale
- change dimensions
- change mesh data
- change materials
- quarantine entire collections

## Explicit do-not-touch set

Do not alter:

- `V09_WET_PROCESS_BACK_WALL`
- `V09_WET_PROCESS_SOFFIT`
- any other Wet Processing object
- any other Toothpaste object
- any other Wet Wipes object
- `V02_WEIGH_BOOTH_SIDE`
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`
- any of the accepted F06 43 objects
- any F01-F05 accepted object

The Wet Processing wall/soffit may block some camera positions but does not overlap the accepted F06 footprint and is therefore not authorized for quarantine.

## Phase 4 — exact post-mutation protection proof

Create:

- `F06_X01_QUARANTINE_AFTER.json`
- `F06_X01_QUARANTINE_DIFF.json`

The exact authorized delta must contain only:
- seven hide_viewport false→true changes where applicable;
- seven hide_render false→true changes where applicable;
- the F06-X01 quarantine metadata additions.

No transform/dimension/material/data/parent/collection differences are allowed.

No protected F01-F06 or earlier quarantine-state differences are allowed.

Any extra delta:

STOP `BLOCKED_F06_X01_UNAUTHORIZED_CANONICAL_DELTA`.

## Phase 5 — F06 historical regression

Re-confirm:

- F06 destination collection = exactly 43
- historical contribution split = BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1
- dimensional digest unchanged
- F06 accepted object transforms/dimensions/materials/parents/data unchanged

Do not rebuild or replace any F06 object.

Historical A/B/C parity is already independently accepted. Do not rerender it unless a new contradiction appears.

## Phase 6 — current-context camera search after canonical quarantine

Now search for an integrated F06 camera from the actual saved canonical state with the seven overlap objects quarantined.

Render at least **24** candidate previews at 900×600.

Cover:
- front-left
- wider front-left
- side-left
- front-oblique
- higher/lower variants
- multiple target biases toward the downstream transfer tote
- lenses 35 / 40 / 45 / 52 mm

Do not use any additional temporary hide.

Do not change any neighbor.

## Required LOS targets

Use these 9 targets:

1. `V02_WEIGH_HOPPER_0`
2. `V02_WEIGH_HOPPER_2` or 3
3. `V02_WEIGH_HOPPER_VALVE_1`
4. `V02_WEIGH_DOSING_CHUTE_0`
5. `V02_WEIGH_DOSING_CHUTE_2`
6. `V02_PRECISION_BALANCE_0`
7. `V02_PRECISION_BALANCE_2`
8. `V02_WEIGH_TRANSFER_TOTE`
9. `V02_WEIGH_OPERATOR_TABLE`

Require >=7/9 clear rays.

Record every blocker name.

## Required visual gate

A final integrated candidate must visibly communicate in one frame:

- weigh booth/enclosure;
- substantially complete hopper row;
- hopper valves;
- dosing chutes/path;
- precision balance stations;
- balance table;
- transfer tote/cart fully identifiable, not a cropped fragment;
- operator/service zone;
- access organization;
- coherent hopper → dosing → balance → transfer workflow;
- legitimate current context.

Also require:
- camera outside geometry;
- no unrelated structure dominates;
- no material clipping of the core workflow;
- no QA-only hiding;
- no neighbor mutation beyond the seven canonical quarantines.

Do not use the wall label as evidence of functional completeness.

## Candidate evidence

Directory:

`output/rev005-facility-gated/F06_micro_weigh/X01/`

Create:

`F06_X01_CAMERA_CANDIDATES.json`

and at least 24 named 900×600 previews.

For every candidate record:
- camera
- target
- lens
- LOS count
- blockers
- all visual-cue booleans
- camera-outside result
- preview path

Do not auto-select by LOS alone.

## Phase 7 — final integrated evidence

If a valid candidate exists, produce:

- `D_INTEGRATED_CONTEXT_X01.png` at 1440×960
- `D_INTEGRATED_CONTEXT_X01_PREVIEW_900x600.png`

Create:

`F06_X01_INTEGRATED_CAMERA_VALIDATION.json`

The validation must state the exact selected camera/target/lens, 9 LOS rays, blockers, and the full visual-cue matrix.

## If no valid view exists

If no valid integrated view exists after exactly the seven authorized quarantines:

STOP:

`BLOCKED_F06_X01_NO_COMPLETE_INTEGRATED_VIEW`

Do not widen the quarantine.

Do not alter Wet Processing.
Do not alter F06 geometry.

Publish the evidence and stop for GPT direction.

## Phase 8 — save/export/final hashes

Only after the exact quarantine and all protection gates pass:

Save canonical Blend.

Export canonical GLB using the same current canonical export policy.

Create:

- `F06_X01_FINAL_HASHES.json`
- `F06_X01_VALIDATION.json`
- `F06_X01_REGRESSION.json`

The final hashes may change because the saved canonical visibility/quarantine state changed.

Record exact before/after hashes.

## Required log

Write:

`coordination/Logs/REV005_F06_X01_TARGETED_QUARANTINE_CODEX_LOG.md`

Include:
- baseline hashes;
- ownership proof;
- exact 7-object delta;
- protection result;
- camera-search result;
- final hashes;
- all evidence paths.

## Git scope

Commit/push only:

- canonical Blend/GLB if the authorized seven-object saved quarantine is applied;
- F06 X01 evidence/renders;
- F06 X01 log.

Do not edit:
- root TASKS.md
- locked audit criteria
- root-cause audit

Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06_X01`
