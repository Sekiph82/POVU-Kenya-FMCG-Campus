# M08.45 — F08-R03 EXTERNAL SOUTH-FRONTAGE VISUAL CLOSURE

## Scope

Execute F08-R03 only.

This is the final camera-only F08 evidence attempt.

Use the exact R02 staged model and exhaust the untested true external south-frontage camera family.

Do not begin F09.

Do not change F08 geometry, materials, transforms, collection membership, visibility, retirement state, or room shell.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F08_R02_GPT_AUDIT.md`
3. `coordination/Audits/REV005_F08_R03_EXTERNAL_FRONTAGE_GPT_CRITERIA.md`
4. `coordination/Audits/REV005_F08_R02_VISUAL_LEGIBILITY_GEOMETRY_GPT_CRITERIA.md`
5. `coordination/Logs/REV005_F08_R02_VISUAL_LEGIBILITY_GEOMETRY_REMEDIATION_CODEX_LOG.md`
6. all published R02 evidence under:
   `output/rev005-facility-gated/F08_bottle_blow/R02/`

## Safe synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

First:
- inspect `git status --short`;
- inventory any local/ignored R02 staged files;
- fetch `origin/main`;
- fast-forward-only;
- re-read root `TASKS.md`.

No reset.
No rebase.
No force.
No deletion of owner-local work.

Tracker must authorize:

`M08.45 — F08-R03 external south-frontage visual closure`

Otherwise:

STOP `BLOCKED_F08_R03_TRACKER_MISMATCH`.

## Locked canonical baseline

Canonical Blend must remain:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

Canonical GLB must remain:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

until successful promotion.

## Locked R02 staged source

Preferred staged file:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`

Required SHA-256:

`0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`

If this exact local stage exists, use it after validation.

If absent, rebuild deterministically using the published R02 helper from the locked R01 source.

Do not freehand reconstruct.

Required R02 facts:
- accepted meshes = 391
- retired legacy = 391
- NOT_F08 preserved = 5
- preforms total = 30
- elevator riders = 6
- downstream feed preforms = 7
- oven path preforms = 13
- transfer riders = 3
- heater elements = 16
- formed outfeed bottles = 16
- protected unauthorized differences = 0
- cross-facility collisions = 0
- outside-envelope objects = 0

Write:

`output/rev005-facility-gated/F08_bottle_blow/R03/F08_R03_STAGED_STATE_VALIDATION.json`

## Critical audit finding

The south glazed frontage is approximately:

`Y = -1.84 m`

But published R02 cameras stayed inside/north of it:

- A Y = 7…13
- B Y = 3…9
- C Y = 0.5…3.5
- D Y = 3…9

R01 likewise did not meaningfully exhaust an external south elevation.

R03 must therefore place cameras **outside the south frontage**, generally Y=-5…-16, and look through the existing glazing/open frontage without hiding it.

## No mutation rule

Do not:
- move any F08 object;
- add any mesh;
- edit materials;
- alter guard transparency;
- change visibility;
- hide glazing;
- hide walls;
- change retirement/quarantine;
- change room shell;
- change protected neighbors.

Only camera/evidence objects may change in the staged working state.

## Camera technical rules

Sensor:
- 36 mm

Allowed lenses:
- 14 / 16 / 18 / 20 / 22 / 24 / 28 / 32 mm

Camera may sit outside the room envelope.

Require:
- camera outside every mesh AABB;
- no near-plane slicing;
- no opaque wall between camera and intended process sequence;
- no temporary QA hiding;
- no clipping tricks.

## Family A — complete external process elevation

Render at least 18 candidates.

Camera range:
- X = 48…56
- Y = -8…-16
- Z = 5…8

Target range:
- X = 51…55
- Y = 9…11
- Z = 2.5…3.5

Lens:
- 14 / 16 / 18 / 20 / 22 mm

A must show:
- visibly distinct hopper at west end;
- elevator/feed;
- oven;
- transfer;
- blow cell;
- formed-bottle outfeed;
- room/floor context;
- readable west→east order.

## Family B — functional external oblique

Render at least 18 candidates.

Camera range:
- X = 52…60
- Y = -5…-12
- Z = 4…7

Target:
- X = 55…60
- Y = 9…11
- Z = 2.4…3.5

Lens:
- 18 / 20 / 22 / 24 / 28 mm

B must show:
- heater outlet;
- transfer/starwheel;
- blow cell;
- at least one readable mould/clamp station;
- stretch/blow cue;
- formed-bottle outfeed;
- clear process direction.

## Family C — transformation side elevation

Render at least 18 candidates.

Camera:
- X = 54…60
- Y = -4…-9
- Z = 3.5…6

Target:
- X = 56…60
- Y = 9…11
- Z = 2.2…3.4

Lens:
- 20 / 22 / 24 / 28 / 32 mm

C must show:
- oven/transfer adjacency;
- mould/clamp mechanism;
- stretch/blow rod/nozzle;
- in-process preform state;
- formed/released bottle state;
- immediate outfeed relationship.

## Family D — integrated external process + operator side

Render at least 18 candidates.

Camera:
- X = 46…58
- Y = -8…-15
- Z = 6…8

Target:
- X = 52…57
- Y = 9…11
- Z = 2.8…3.5

Lens:
- 14 / 16 / 18 / 20 / 22 mm

D must show:
- hopper/feed;
- oven;
- blow cell;
- outfeed;
- HMI/operator side;
- south operator aisle;
- legitimate room context.

## Candidate evidence

Create:

`R03/F08_R03_CAMERA_CANDIDATES.json`

For every candidate record:
- candidate ID
- role
- camera XYZ
- target XYZ
- lens
- camera-inside-geometry
- facade/glazing clipping
- hopper visible
- elevator/feed visible
- oven visible
- transfer visible
- mould station readable
- stretch/blow readable
- in-process preform readable
- formed bottle readable
- outfeed visible
- HMI/operator relationship
- aisle/context
- complete label-blind sequence
- preview path

Actually inspect each rendered frame.

Do not infer PASS from metadata.

## Top evidence

Retain strongest 8 candidates per role.

Publish:
- top 8 individual previews per role
- 4×2 contact sheet per role

Create:
- `F08_R03_A_TOP8_CONTACT_SHEET.png`
- `F08_R03_B_TOP8_CONTACT_SHEET.png`
- `F08_R03_C_TOP8_CONTACT_SHEET.png`
- `F08_R03_D_TOP8_CONTACT_SHEET.png`

## Selected provisional previews

Produce:

- `F08_R03_A_SELECTED_PREVIEW_900x600.png`
- `F08_R03_B_SELECTED_PREVIEW_900x600.png`
- `F08_R03_C_SELECTED_PREVIEW_900x600.png`
- `F08_R03_D_SELECTED_PREVIEW_900x600.png`

Create:

`F08_R03_VISUAL_SELECTION.json`

All A/B/C/D roles must PASS.

The four views together must make this sequence self-explanatory without labels:

`bulk preforms → elevator/feed → infrared heating → transfer → clamp/mould + stretch/blow → formed bottles → inspection/outfeed`

## Hard failure rule

If any role still fails after the required external search:

1. do not modify geometry;
2. do not promote canonical Blend;
3. do not replace canonical GLB;
4. publish R03 candidate evidence, top-8 previews/contact sheets, selected attempts, validation and log;
5. stop:

`BLOCKED_F08_R03_EXTERNAL_FRONTAGE_VISUAL_FAILURE`

After this stop, no further camera-only F08 task is permitted.

## Technical revalidation if visual PASS

Only if all visual roles PASS, re-run:
- accepted R02 mesh count = 391
- dimensional validation
- F01-F07 protection
- legacy retirement = 391
- NOT_F08 preserved = 5
- collision = 0
- outside-envelope = 0
- deterministic GLB membership parity

No technical fact may regress.

## Deterministic GLB parity

Expected membership:

pre-F08 canonical GLB names
- exact 391 retired F08 legacy names
+ exact 391 R02 accepted F08 exportable names

Do not hard-code node count.

Require:
- zero missing expected names
- zero unexpected names
- all F01-F07 baseline names preserved
- all intended F08 names present
- all 391 retired legacy names absent

## Canonical promotion

Only after visual + technical + GLB gates PASS:

Promote the exact validated R02 staged state to canonical Blend.

Do not rebuild geometry after visual approval.

Export canonical GLB deterministically.

Then reopen the canonical Blend and rerender final:
- A_CONTEXT 1440×960 + 900×600 preview
- B_FUNCTIONAL 1440×960 + 900×600 preview
- C_SEQUENCE_DETAIL 1440×960 + 900×600 preview
- D_INTEGRATED 1440×960 + 900×600 preview

using the exact selected R03 cameras.

## Final evidence

Create:
- `F08_R03_TECHNICAL_REVALIDATION.json`
- `F08_R03_GLB_PARITY_PREPROMOTION.json`
- `F08_R03_FINAL_HASHES.json`
- `F08_R03_FINAL_GLB_PARITY.json`
- `F08_R03_FINAL_SAVED_STATE_VALIDATION.json`
- `F08_R03_VALIDATION.json`

## Required log

Write:

`coordination/Logs/REV005_F08_R03_EXTERNAL_SOUTH_FRONTAGE_VISUAL_CLOSURE_CODEX_LOG.md`

Include:
- sync/preflight
- exact staged source/hash
- candidate counts
- selected A/B/C/D
- direct visual rationale
- technical revalidation
- promotion result or blocked stop
- final hashes if promoted
- confirmation F09 not started

## Git scope

If blocked:
commit/push R03 evidence, top candidate previews/contact sheets, selected attempts, validation, log and R03-only helper scripts.

If successful:
also commit/push canonical Blend/GLB and final full renders/previews.

Do not edit root `TASKS.md`.
Do not edit locked audit/design files.
Do not begin F09.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F08_R03`
