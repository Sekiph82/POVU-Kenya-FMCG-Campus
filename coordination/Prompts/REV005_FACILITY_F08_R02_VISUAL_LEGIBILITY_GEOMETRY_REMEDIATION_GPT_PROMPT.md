# M08.44 — F08-R02 VISUAL-LEGIBILITY GEOMETRY REMEDIATION + CONDITIONAL PROMOTION

## Scope

Execute F08-R02 only.

This task is a narrow staged-model visual-legibility remediation.

R01 proved that camera-only work is insufficient.

Do not begin F09.

Do not modify any accepted F01-F07 geometry or accepted quarantine/retirement state.

Do not save or replace the canonical Blend/GLB until every R02 staged gate passes.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F08_R01_GPT_AUDIT.md`
3. `coordination/Audits/REV005_F08_R02_VISUAL_LEGIBILITY_GEOMETRY_GPT_CRITERIA.md`
4. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md`
5. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_GPT_AUDIT_CRITERIA.md`
6. `coordination/Logs/REV005_F08_R01_CAMERA_CONTRACT_REMEDIATION_CODEX_LOG.md`
7. all M08.42 / R01 published evidence and helpers

## Mandatory synchronization

Start by:

1. `git status --short`
2. inventory ignored/local F08 staged files
3. `git fetch origin main`
4. fast-forward-only to current `origin/main`
5. re-read local root `TASKS.md`

No reset.
No rebase.
No force.
No deletion of owner-local work.

Tracker must authorize:

`M08.44 — F08-R02 visual-legibility geometry remediation`

Otherwise stop:

`BLOCKED_F08_R02_TRACKER_MISMATCH`

## Locked canonical baseline

Before work verify:

Blend:
`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

GLB:
`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

If either differs:

STOP `BLOCKED_F08_R02_CANONICAL_BASELINE_MISMATCH`.

## Recover deterministic R01 staged baseline

Use the R01 deterministic helper-reconstructed staged model.

If a valid local R01 staged Blend exists, verify it against:

`output/rev005-facility-gated/F08_bottle_blow/R01/F08_R01_STAGED_STATE_VALIDATION.json`

Required starting facts:
- destination meshes = 338
- confirmed legacy = 391
- retired legacy = 391
- ambiguous legacy = 0
- NOT_F08 preserved = 5
- preforms = 20
- heater elements = 16
- service doors = 2
- HP-air branches = 4
- formed bottles = 16
- unauthorized prior differences = 0
- collisions = 0
- outside-envelope objects = 0

If local stage is absent or invalid, rebuild from the locked canonical baseline using the published deterministic helpers.

Do not freehand reconstruct.

For the east service opening, use the helper/design-contract truth:
- jamb Y = 9.0 and 11.0
- north east-wall segment = 11.0 m
- south east-wall segment = 11.0 m

Do not restore stale earlier manifest values.

Create:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STARTING_STAGE_VALIDATION.json`

## Geometry-remediation rule

Only new F08 accepted objects may change.

Major process centers and envelopes remain locked.

No neighbor mutation.

No new quarantine.

No room-envelope redesign.

All changes must be deterministic and scripted.

Create a dedicated R02 helper script:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_visual_legibility_remediation.py`

The helper must assert:
- task = M08.44 / F08-R02
- exact starting staged state
- exact destination collection
- no F01-F07 object mutation

## R02-1 — Hopper visual identity

Current problem:
the hopper exists dimensionally but never reads as the upstream bulk source.

Preserve:
- center ≈(36.5,10)
- upper-bin envelope ≈2.4×2.4×1.8 m
- overall support envelope
- funnel/throat centerline

Remediate by:
- replacing the generic rectangular upper-bin reading with a visibly hopper-like open-top/tapered or folded-panel silhouette inside the same envelope;
- keeping a clearly supported frame;
- keeping a visible lower funnel;
- strengthening the feed throat connection;
- adding a visible top lip/rim;
- optionally showing a small number of preforms at the throat/top without exceeding the envelope.

Do not move the hopper center.

## R02-2 — Elevator / feed path

Current rails are too skeletal.

Keep the same start/end path.

Add:
- visible carrier flights/paddles or bucket/step cues along the incline;
- at least 6 clearly visible preforms riding the elevator;
- mechanical side rails/supports;
- explicit discharge into the neck-support rail.

Feed rail:
- keep centerline/envelope;
- at least 6 visible preforms downstream of elevator;
- preserve physical continuation into oven inlet.

The hopper→elevator→rail sequence must read continuously.

## R02-3 — Infrared oven

Current 16 heater elements visually read as oversized orange columns.

Preserve:
- oven center = (47.5,10,3.1)
- outer envelope = 7×4×4.2 m
- two banks
- >=8 heater elements per bank
- active element length ≈2.2 m
- product rail through oven

Remediate:
- reduce heater-element cross-section to a lamp-like section, nominally around 0.08–0.12 m width/depth;
- preserve the 16-element count;
- add shallow reflector/backplate or heater-bank frame geometry behind each bank;
- keep inlet/outlet visibly open;
- add light guard/frame cues without creating an opaque shell;
- retain or add at least 8 visible preforms in/at the oven path.

The oven must read as a machine, not as two freestanding orange fences.

## R02-4 — Oven-to-cell transfer

Make the transfer visually obvious.

Preserve transfer region:
- X≈51…53
- Y≈10
- Z≈2.7…3.3

Remediate:
- enlarge/strengthen the starwheel or curved-guide silhouette inside the allowed region;
- preserve physical continuity from oven rail to cell;
- add at least 3 visible preform/product cues around the starwheel/guide;
- use guard geometry that does not hide the transfer.

No floating rods.

## R02-5 — Mould / blow visual explanation

Keep:
- blow-cell envelope
- station centers ≈55.7 and 58.3
- two stations
- opposing platens
- mould halves
- stretch/blow rods
- guard envelope

Improve readability.

For each station:
- keep platen centers/major dimensions within tolerance;
- make tie-bars/guide structure clearer;
- add visible actuator/clamp-cylinder cues;
- strengthen stretch/blow rod diameter/contrast within the allowed 0.10–0.16 m cue;
- make nozzle/head visibly connected;
- reduce generic flat-block dominance through material separation and mould-face relief.

Add product-state cues:

Station 1:
- one visible preform/in-process elongated-preform cue aligned with the mould center.

Station 2:
- one visible formed-bottle/in-mould or just-released bottle cue aligned with the mould/discharge path.

These are process-state evidence, not decoration.

The viewer must be able to infer that the station transforms a preform into a bottle.

## R02-6 — Guard transparency / frame dominance

The guard frame must remain.

But internal machinery must remain readable.

Allowed:
- reduce guard glazing opacity further if technically appropriate;
- keep dark structural posts;
- slightly reduce non-load-bearing guard-member visual weight if necessary.

Not allowed:
- remove required guard posts;
- make the cell unguarded;
- use QA-only hiding.

## R02-7 — Formed-bottle outfeed

Keep:
- >=16 formed bottles
- conveyor envelope
- inspection bridge

Use bottle dimensions in the upper half of the locked range where practical:
- height target ≈0.36–0.38 m
- body width target ≈0.10–0.12 m

Preserve body + shoulder + neck + finish.

Make the first bottle appear close to the cell discharge so the transformation reads continuously.

Use a readable PET material/tint that remains distinct from preforms.

Do not make bottles cartoonishly oversized.

## R02-8 — HMI / operator connection

Keep HMI center and south-side relationship.

Allowed:
- stronger standing-pad/floor marking;
- local task light;
- clear access line to service doors.

No people/mannequins.

## R02-9 — local lighting / material contrast

Improve visibility without turning the scene into a color-coded diagram.

Required:
- heater lamps visually distinct from steel structure;
- mould halves distinct from platens and guards;
- preforms distinct from formed bottles;
- formed bottles readable at 900×600;
- no overbright white washout.

Do not use text labels as proof.

## Mesh-count gate

Starting F08 accepted meshes:

338

Target final staged F08 accepted mesh count:
- 338 to 460

If R02 exceeds 460 accepted meshes:

STOP `BLOCKED_F08_R02_DETAIL_OBJECT_BLOAT`

and explain why.

## Stage-only save

Save the remediated model only to:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`

Do not touch canonical Blend yet.

## Dimensional / protection revalidation

Create:

- `R02/F08_R02_DIMENSIONAL_VALIDATION.json`
- `R02/F08_R02_PROTECTION_DIFF.json`
- `R02/F08_R02_COLLISION_VALIDATION.json`
- `R02/F08_R02_ACCEPTED_MANIFEST.json`

Require:
- major room/machine anchors within locked tolerance;
- zero F01-F07 unauthorized differences;
- exact 391 legacy retirement preserved;
- 5 NOT_F08 candidates unchanged;
- zero cross-facility collisions;
- zero unintended F08 objects outside envelope.

## Camera search after geometry remediation

Use actual remediated staged state.

Minimum candidate counts:

- A: 24
- B: 24
- C: 24
- D: 24

Allowed lens:
- 16–35 mm

Camera rules from R01 remain valid:
- outside geometry
- no near-plane slicing
- no QA-only hiding
- no visibility mutation

### A_CONTEXT must show
- visibly distinct hopper
- elevator/feed
- oven
- blow cell
- formed-bottle outfeed
- room context
- process order

### B_FUNCTIONAL must show
- heater outlet
- transfer/starwheel
- blow cell
- at least one readable mould station
- outfeed and formed bottles
- connected process direction

### C_SEQUENCE_DETAIL must show
- oven/transfer
- readable clamp/mould
- stretch/blow cue
- product-state transformation
- discharge/outfeed

### D_INTEGRATED must show
- hopper/feed
- oven
- blow cell
- outfeed
- HMI/operator side
- aisle/context

The four selected views together must label-blind read:

`bulk preforms → elevator/feed → IR heating → transfer → clamp/mould + stretch/blow → formed bottles → inspection/outfeed`

## Candidate evidence

Create:

`R02/F08_R02_CAMERA_CANDIDATES.json`

Retain strongest 8 candidates per role.

Publish:
- 8 individual previews per role
- one 4×2 contact sheet per role

Create:
- `F08_R02_A_TOP8_CONTACT_SHEET.png`
- `F08_R02_B_TOP8_CONTACT_SHEET.png`
- `F08_R02_C_TOP8_CONTACT_SHEET.png`
- `F08_R02_D_TOP8_CONTACT_SHEET.png`

## Provisional visual gate

Before canonical promotion, create:

- `F08_R02_A_SELECTED_PREVIEW_900x600.png`
- `F08_R02_B_SELECTED_PREVIEW_900x600.png`
- `F08_R02_C_SELECTED_PREVIEW_900x600.png`
- `F08_R02_D_SELECTED_PREVIEW_900x600.png`

Write:

`R02/F08_R02_VISUAL_SELECTION.json`

Every A/B/C/D role must be PASS.

If any role fails:

Do not promote.

Publish all R02 evidence and stop:

`BLOCKED_F08_R02_VISUAL_ACCEPTANCE`

## Deterministic GLB parity before promotion

If staged visual acceptance passes:

Build a candidate GLB by exact-name deterministic selection.

Expected membership:

pre-F08 canonical GLB named membership
- exact 391 retired F08 legacy names
+ exact final R02 accepted F08 exportable names

Do not hard-code node count.

Write:

`R02/F08_R02_GLB_PARITY_PREPROMOTION.json`

Require:
- zero missing expected names
- zero unexpected names
- all F01-F07 baseline names preserved
- all final F08 names present
- all 391 retired names absent

If parity fails:

STOP `BLOCKED_F08_R02_GLB_PARITY`

without canonical promotion.

## Canonical promotion

Only after all staged visual + technical + GLB gates PASS:

Promote the exact R02 staged state to canonical Blend.

Do not rebuild again after visual approval.

Export canonical GLB using the same deterministic membership set.

Then reopen canonical Blend and verify:
- exact selected cameras
- saved visibility
- protection
- legacy retirement
- final accepted F08 manifest
- final GLB parity

## Final renders

Render from reopened canonical Blend:

- `F08_A_CONTEXT.png` 1440×960
- `F08_B_FUNCTIONAL.png` 1440×960
- `F08_C_SEQUENCE_DETAIL.png` 1440×960
- `F08_D_INTEGRATED.png` 1440×960

plus matching 900×600 previews.

## Final evidence

Create:

- `R02/F08_R02_FINAL_HASHES.json`
- `R02/F08_R02_FINAL_GLB_PARITY.json`
- `R02/F08_R02_FINAL_SAVED_STATE_VALIDATION.json`
- `R02/F08_R02_VALIDATION.json`

## Required log

Write:

`coordination/Logs/REV005_F08_R02_VISUAL_LEGIBILITY_GEOMETRY_REMEDIATION_CODEX_LOG.md`

Include:
- sync/preflight
- staged reconstruction source
- exact geometry changes by family
- before/after object count
- dimensional/protection/collision results
- candidate counts
- selected A/B/C/D
- GLB parity
- canonical promotion result
- final hashes or blocked stop
- F09 not started

## Git scope

If blocked:
commit/push R02 scripts, evidence, selected previews/contact sheets, validation and log.

If successful:
also commit/push canonical Blend, canonical GLB and final full renders/previews.

Do not edit root `TASKS.md`.
Do not edit locked audit/design files.
Do not begin F09.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F08_R02`
