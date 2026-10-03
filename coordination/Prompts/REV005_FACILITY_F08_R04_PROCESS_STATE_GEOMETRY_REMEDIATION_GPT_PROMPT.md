# M08.46 — F08-R04 PROCESS-STATE GEOMETRY REMEDIATION + CONDITIONAL PROMOTION

## Scope

Execute F08-R04 only.

R03 exhausted the remaining camera-only path. R04 is a narrow process-state geometry remediation.

Do not begin F09.

Do not move major process centers.
Do not redesign the room.
Do not mutate F01-F07 or neighbors.
Do not add quarantine.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F08_R03_GPT_AUDIT.md`
3. `coordination/Audits/REV005_F08_R04_PROCESS_STATE_GEOMETRY_GPT_CRITERIA.md`
4. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md`
5. `coordination/Logs/REV005_F08_R03_EXTERNAL_SOUTH_FRONTAGE_VISUAL_CLOSURE_CODEX_LOG.md`
6. all R02/R03 F08 evidence

## Synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Start with:
- `git status --short`
- inventory ignored/local staged files
- `git fetch origin main`
- fast-forward-only
- re-read root `TASKS.md`

No reset.
No rebase.
No force.
No deletion of owner-local files.

Tracker must authorize:

`M08.46 — F08-R04 process-state geometry remediation`

Otherwise STOP:

`BLOCKED_F08_R04_TRACKER_MISMATCH`

## Locked canonical baseline

Canonical Blend:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

Canonical GLB:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

Do not touch either until promotion is explicitly authorized by all staged gates.

## Locked staged source

Use:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`

Required SHA-256:

`0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`

If absent, rebuild it deterministically from the published R02 helper and verify the same hash/facts.

Required starting facts:
- accepted F08 meshes = 391
- retired legacy = 391
- ambiguous legacy = 0
- NOT_F08 preserved = 5
- preforms total = 30
- elevator riders = 6
- downstream feed preforms = 7
- oven path preforms = 13
- transfer riders = 3
- heater elements = 16
- formed outfeed bottles = 16
- protection diff = 0
- collisions = 0
- outside envelope = 0

Create:

`output/rev005-facility-gated/F08_bottle_blow/R04/F08_R04_STARTING_STAGE_VALIDATION.json`

## Why R04 exists

R03 finally showed the entire process through true external frontage cameras.

That proved:
- hopper/feed can be seen;
- oven can be seen;
- transfer can be seen;
- twin mould stations can be seen;
- outfeed can be seen.

But across R03:
- stretch/blow readable = 0 in every role;
- in-process preform readable = 0 in every role;
- formed-bottle state readable = 0 in every role;
- complete label-blind sequence = 0.

The remaining defect is the visual explanation of the actual transformation.

## Geometry-change rule

Only objects inside:

`REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N`

may change.

Major locked centers/envelopes remain fixed:
- hopper ≈(36.5,10)
- oven = (47.5,10,3.1)
- blow cell = (57,10,3.3)
- outfeed ≈(65,10,1.7)
- room X 33…71 / Y -2…22

Major-center tolerance:

<=0.05 m

Create deterministic helper:

`R04/F08_R04_process_state_geometry_remediation.py`

It must assert:
- exact task authorization
- exact R02 staged source
- exact destination collection
- no outside-destination object mutation

## R04-1 — preserve what already improved

Do **not** undo:
- tapered/open hopper
- hopper rim/throat
- elevator flights
- visible elevator riders
- slim 16-element heater banks
- reflector/backplate structure
- transfer starwheel
- enlarged formed-bottle outfeed
- clear F08 safety glazing
- HMI operator pad
- R02 lighting improvements

These are accepted starting improvements.

## R04-2 — Station 1 must visibly read as PREPARE / STRETCH

Station 1 center remains:

approximately X=55.7 / Y=10

Create a visibly open/load state inside the existing guarded-cell envelope.

Required:

- keep left/right platen system and station center;
- separate mould halves symmetrically enough to expose the product state;
- keep all moving pieces within the locked station/cell envelope;
- add/strengthen four tie-bar or guide cues around the mould region where practical;
- make mould halves visually distinct from platens;
- add bottle-shaped cavity relief/recess on the inner mould faces;
- place one clearly visible heated preform at the station centerline;
- preform neck finish must be readable;
- align the stretch/blow rod directly above the preform axis;
- nozzle/head must visibly connect to the rod/preform axis;
- allow one elongated in-process preform cue if needed.

Heated/in-process preform:
- body visibly narrower than final bottle;
- nominal height 0.22…0.30 m
- elongated state may reach 0.34 m
- physically plausible PET silhouette
- do not simply scale up a bottle.

The viewer must understand:
“a preform is being loaded/stretched here.”

## R04-3 — Station 2 must visibly read as BLOWN / EJECT

Station 2 center remains:

approximately X=58.3 / Y=10

Create a visibly different cycle state.

Required:
- mould halves visibly open/separated enough to reveal product;
- one formed bottle clearly visible at the mould center or just exiting;
- bottle silhouette must match the outfeed bottle family;
- keep clamp/actuator cues;
- make inner cavity/mould surfaces visible;
- keep stretch/blow/nozzle relationship readable;
- create a direct short discharge guide/neck rail from Station 2 toward outfeed.

The viewer must understand:
“a bottle has been formed and is leaving here.”

Station 1 and Station 2 must **not** look like two identical grey blocks.

## R04-4 — reduce generic platen-block dominance

Preserve locked platen bounds/centers, but improve visual reading.

Allowed:
- recesses
- central cutouts/openings
- framed platen geometry inside the same bounding envelope
- distinct mould-face insert
- relief geometry
- tie bars
- clamp cylinders
- guide rods

The bounding dimensions may remain the same while the visible geometry inside the bound becomes less monolithic.

Do not create impossible floating structure.

## R04-5 — oven→Station 1 handoff

Strengthen physical continuity.

Required:
- preserve transfer starwheel/guide;
- at least three visible product states around transfer;
- first station infeed neck guide visibly meets the Station 1 centerline;
- no disconnected product path.

## R04-6 — Station 2→outfeed handoff

Required:
- explicit short discharge guide/air-conveyor/neck-rail segment;
- first formed bottle positioned close to the cell exit;
- second formed bottle continues toward conveyor;
- remaining >=16 bottle outfeed continues eastward;
- inspection bridge remains downstream.

Do not move the outfeed center/envelope.

## R04-7 — optional first-off sample rack

This is optional and supplementary.

If used, place a realistic small quality/first-off sample rack near HMI/operator side.

Exactly 3 physical samples:
1. cold preform
2. elongated/heated preform
3. formed bottle

No text labels.

The rack cannot substitute for readable Station 1 / Station 2 product states.

## R04-8 — material and local light

Improve silhouette separation.

Required:
- platen/frame neutral steel
- mould inserts visibly distinct from platen
- preforms translucent PET with slender silhouette
- formed bottles translucent PET with shoulder/body/neck silhouette
- guard remains transparent enough to see internals
- no neon teaching colors
- no text explanation.

Add local F08-only task light only if required.

## Mesh discipline

Starting R02 accepted meshes:
391

R04 final target:
391…460

If >460:

STOP `BLOCKED_F08_R04_DETAIL_OBJECT_BLOAT`

without promotion.

## Save staged R04 only

Save to:

`output/rev005-facility-gated/F08_bottle_blow/R04/F08_R04_STAGED.blend`

Do not save canonical yet.

## Technical revalidation

Create:
- `F08_R04_ACCEPTED_MANIFEST.json`
- `F08_R04_DIMENSIONAL_VALIDATION.json`
- `F08_R04_PROTECTION_DIFF.json`
- `F08_R04_COLLISION_VALIDATION.json`

Require:
- zero F01-F07 unauthorized mutation
- 391 legacy retirement preserved
- 5 NOT_F08 preserved
- zero cross-facility collisions
- zero unintended outside-envelope objects
- all major anchors within tolerance.

## Correct camera-validity logic

R03's C-family validator used broad AABB overlap as final invalidation for `Production_Hall` and `PRODUCTION_ROOF`.

Do not repeat that.

Use AABB only as prefilter.

Final camera-inside-solid verdict must use actual geometry logic, such as:
- point-in-closed-mesh
- ray parity
- signed/nearest surface logic
- explicit shell interior logic

Record:

`F08_R04_CAMERA_VALIDATOR.json`

including method and validation fixtures.

## Focused camera validation

No 100+ random search.

Minimum:
- A 12
- B 12
- C 12
- D 12

Use strongest known families from R03 and R02.

### A
Must show:
- hopper/feed
- oven
- cell
- outfeed
- room context

### B
Must show:
- oven outlet
- transfer
- visibly different Station 1 and Station 2
- readable mould/clamp
- formed-bottle outfeed

### C
This is decisive.

Must show in one valid frame:
- in-process preform at Station 1
- stretch/blow rod/nozzle
- mould/cavity relationship
- formed bottle at Station 2
- discharge guide to outfeed

C camera may use Z > 6.0 m if actual solid-geometry validation passes.

### D
Must show:
- full line
- HMI/operator side
- aisle/context
- process order.

## Visual selection

Produce:
- `F08_R04_A_SELECTED_PREVIEW_900x600.png`
- `F08_R04_B_SELECTED_PREVIEW_900x600.png`
- `F08_R04_C_SELECTED_PREVIEW_900x600.png`
- `F08_R04_D_SELECTED_PREVIEW_900x600.png`

Create:

`F08_R04_VISUAL_SELECTION.json`

All four must PASS.

The four-view set must make this label-blind sequence understandable:

`bulk preforms → feed → infrared heating → transfer → preform loaded/stretched → bottle formed/ejected → outfeed`

If any role fails:

do not promote canonical Blend/GLB.

Publish R04 evidence and stop:

`BLOCKED_F08_R04_VISUAL_ACCEPTANCE`

## GLB parity before promotion

Only after visual PASS:

Compute deterministic expected membership:

pre-F08 canonical membership
- exact 391 retired F08 legacy names
+ exact final R04 accepted F08 exportable names

Do not hard-code node count.

Require:
- zero missing names
- zero unexpected names
- all F01-F07 accepted baseline names preserved
- all R04 accepted F08 names present
- retired 391 names absent.

Write:

`F08_R04_GLB_PARITY_PREPROMOTION.json`

## Canonical promotion

Only after all staged gates PASS:

Promote the **exact** R04 staged model to canonical Blend.

Do not rebuild after visual approval.

Export canonical GLB deterministically.

Then reopen canonical Blend and verify:
- final object manifest
- protection
- retirement
- selected cameras
- saved visibility
- GLB membership parity.

## Final renders

Render from reopened canonical Blend:

- F08_A_CONTEXT.png 1440×960
- F08_B_FUNCTIONAL.png 1440×960
- F08_C_SEQUENCE_DETAIL.png 1440×960
- F08_D_INTEGRATED.png 1440×960

plus matching 900×600 previews.

## Final evidence

Create:
- `F08_R04_FINAL_HASHES.json`
- `F08_R04_FINAL_GLB_PARITY.json`
- `F08_R04_FINAL_SAVED_STATE_VALIDATION.json`
- `F08_R04_VALIDATION.json`

## Required log

Write:

`coordination/Logs/REV005_F08_R04_PROCESS_STATE_GEOMETRY_REMEDIATION_CODEX_LOG.md`

Include:
- source/hash
- exact geometry changes
- mesh count
- camera-validity method
- selected A/B/C/D
- direct visual rationale
- dimensional/protection/collision result
- GLB parity
- promotion result
- final hashes or blocked stop
- F09 not started

## Git scope

If blocked:
commit/push R04 script, evidence, selected previews, validation and log.

If successful:
also commit/push canonical Blend, canonical GLB, final full renders/previews and final parity evidence.

Do not edit root `TASKS.md`.
Do not edit locked audits/design files.
Do not begin F09.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F08_R04`
