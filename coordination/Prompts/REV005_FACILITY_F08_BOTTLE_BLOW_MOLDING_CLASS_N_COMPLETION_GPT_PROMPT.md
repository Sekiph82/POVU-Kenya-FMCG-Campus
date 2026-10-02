# M08.42 — F08 BOTTLE BLOW MOLDING CLASS N COMPLETION

## Scope

Execute F08 only.

Facility:

`Bottle blow molding`

This is a Class N detailed-completion task.

Do not begin F09.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md`
4. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_GPT_AUDIT_CRITERIA.md`
5. V09 Bottle Blow image specs 004–006
6. V09 builder Bottle Blow section
7. current owner inventory for Bottle blow molding
8. F07 final audit and current protection evidence

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

`M08.42 — Facility-Gated F08 Bottle Blow Molding Class N completion`

If not, STOP before mutation.

## Locked canonical baseline

Blend SHA-256:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

GLB SHA-256:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

If either differs:

STOP `BLOCKED_F08_CANONICAL_BASELINE_MISMATCH`.

## Phase 1 — protect accepted prior state

Before any mutation create:

`output/rev005-facility-gated/F08_bottle_blow/F08_PROTECTION_BEFORE.json`

Protect exact signatures for:
- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted 54
- F06 accepted 43
- F07 accepted 789
- F07 exact 446 retired legacy objects and saved state
- F04 accepted Training/Restaurant quarantine state
- F06 exact seven X01 quarantine objects
- V09 Glass Deck quarantine 117
- Restaurant right-wall accepted quarantine
- historical Glass Deck source
- historical Wellness/pavilion protected state

Record:
- name/type
- matrix_world
- dimensions
- parent
- collections
- materials
- data
- hide flags
- custom properties
- protected collection/layer visibility where applicable.

## Phase 2 — inventory current Bottle Blow ownership

Create:

`F08_LEGACY_BOTTLE_BLOW_INVENTORY.json`

Inventory every current object satisfying at least one:
- facility metadata exactly `Bottle blow molding`;
- collection `REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING`;
- known Bottle Blow owner-inventory object;
- current V09 Bottle Blow naming/provenance.

For each candidate record:
- exact name
- facility
- collections
- transform/dimensions
- materials/data/parent
- visibility
- current GLB membership
- ownership classification:
  - `CONFIRMED_F08_LEGACY`
  - `AMBIGUOUS_SHARED`
  - `NOT_F08`

Do not assume the historical V09 92-object count is still current.

If any object necessary to retire is ambiguous:

STOP `BLOCKED_F08_LEGACY_OWNERSHIP_AMBIGUITY`.

## Phase 3 — build new accepted F08

Create:

`REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N`

Follow the design contract exactly.

### Locked room

- center (52,10)
- X 33…71
- Y -2…22
- 38×24 m
- floor center Z=1.00
- floor thickness 0.18
- wall top Z=7.50
- ceiling/soffit underside≈7.25
- south primary aisle >=2.0 m
- north service aisle >=1.5 m
- local maintenance clearances >=1.2 m

## Phase 4 — construct complete west→east process

### P1 Preform hopper

Build:
- primary support frame near (36.5,10,3.1)
- footprint ≈3×3 m
- overall ≈4.6 m high
- 2.4×2.4×1.8 m upper bulk bin
- visible taper/funnel
- feed throat around Z 2.6–2.9
- service/access side

### P2 Feeder/elevator

Connect physically:
- start near (38,10,2.4)
- discharge near (41,10,4.0)
- width 0.7–0.9 m
- path length ≈4 m

No floating connection.

### P3 Preform rail

Build:
- X≈40.5…44
- Y≈10
- Z≈3.7
- >=3.5 m effective length
- paired neck-support rails/guides
- repeated preforms
- explicit oven entry.

Across hopper/feed/oven sequence show at least 16 preforms.

### P4 Heater oven

Center:
`(47.5,10,3.1)`

Outer:
- 7.0×4.0×4.2 m
- open/guarded inlet and outlet
- structural posts/rails
- no opaque monolithic shell

Two heater banks:
- Y≈8.7 and 11.3
- >=8 distinct heater elements per bank
- visible product rail through the oven.

### P5 Oven-to-blow transfer

Build:
- X≈51…53
- Y≈10
- Z≈2.7…3.3

Required:
- curved guide/starwheel/neck-transfer cue
- visible physical connection
- guard that does not hide the mechanism.

### P6 Blow cell

Center:
`(57,10,3.3)`

Guarded envelope:
- ≈8.0×5.6×5.2 m
- X≈53…61
- Y≈7.2…12.8

Required:
- structural base/frame
- guard posts
- transparent/open guards
- >=2 service doors
- HMI outside guards on operator side.

Two mould stations:
- X≈55.7 and 58.3
- Y≈10
- each with opposing platens
- mould block
- stretch/blow rod
- lower guide/base.

Platen:
- ≈0.30×1.4×2.4 m

Mould:
- ≈0.55×1.1×1.8 m

Rod:
- visible diameter ≈0.10–0.16 m
- working length ≈1.5–2 m.

### P7 Local utilities

High-pressure air manifold:
- X≈54…60
- Y≈13.3
- Z≈4.6
- main visible diameter ≈0.14 m
- >=4 branch drops into blow zone.

Cooling water:
- parallel supply/return
- north/service side
- visible diameter ≈0.10–0.12 m
- connect into mould region.

Do not build a separate compressor room here.

### P8 Bottle outfeed

Conveyor:
- center ≈(65,10,1.7)
- length ≈9 m
- width ≈1.2 m
- X≈60.5…69.5

Required:
- legs/frame
- side guides
- >=16 formed bottles
- bottle geometry distinct from preforms.

Bottle:
- body + neck + finish
- height ≈0.28–0.38 m
- width ≈0.08–0.12 m.

### P9 Inspection/discharge

Near X≈68:
- inspection bridge
- sensor heads/optical pair
- quality/reject/sample tote
- continued eastward handoff.

Do not add filling/capping equipment.

## Phase 5 — operator/service/safety

HMI:
- around (57,5.6,2.0)
- body ≈1.0×0.6×1.4
- screen plane
- control/E-stop cues

Preserve >=2.0 m south operator aisle.

Safety:
- eyewash near (68.5,4.0)
- PPE near (66.8,4.0)
- first-response cabinet near (65.2,4.0)

Preform staging:
- two bins/pallet boxes
- X≈35…38
- Y≈16.5
- each ≈1.5×1.2 m
- must not block north service aisle.

## Phase 6 — architectural completion

Required:
- finished floor
- north/back wall
- east/west enclosure cues
- south/front glazing/open frame treatment
- service/egress openings
- ceiling/soffit
- >=10 ceiling lights
- east service door near X≈70.9, clear ≈2.0×2.6 m
- no black void
- no camera-only fake wall.

Use restrained industrial materials from the design contract.

## Phase 7 — retire exact confirmed legacy F08

Only after the new F08 build is complete.

For exact `CONFIRMED_F08_LEGACY` objects only:

Allowed:
- hide_viewport=true
- hide_render=true
- `REV005_F08_LEGACY_RETIRED=true`
- `REV005_F08_RETIRED_BY="F08_CLASS_N"`

Not allowed:
- delete/unlink
- transform
- material/data change
- collection-wide hide without per-object proof.

Create:
- `F08_LEGACY_RETIREMENT_BEFORE.json`
- `F08_LEGACY_RETIREMENT_AFTER.json`
- `F08_LEGACY_RETIREMENT_DIFF.json`

## Phase 8 — dimensional and collision validation

Create:

`F08_DIMENSIONAL_VALIDATION.json`

Validate all design-contract anchors.

Tolerance:
- room/major machinery <=0.05 m
- secondary equipment <=0.10 m
- pipe/conveyor endpoints <=0.10 m
- aisle shortfall <=0.10 m

Require:
- all intended new F08 geometry inside facility envelope except legitimate doorway/glazing hardware;
- no collision with accepted F01-F07 geometry.

If protected cross-facility collision occurs:

STOP `BLOCKED_F08_CROSS_FACILITY_COLLISION`

without mutating the neighbor.

## Phase 9 — final cameras

Use design-contract seeds first.

### A_CONTEXT
- camera (35,-0.5,6)
- target (52,10,3)
- lens 24

### B_FUNCTIONAL
- camera (42,3.5,4.8)
- target (56,10,3)
- lens 32

### C_SEQUENCE_DETAIL
- camera (48,5,4)
- target (56.5,10,3)
- lens 38

### D_INTEGRATED
- camera (34.5,19.5,6.5)
- target (54,10,3)
- lens 24

Sensor width:
- 36 mm

Full:
- 1440×960

Preview:
- 900×600

Permitted refinement:
- <=3 m camera adjustment per axis
- <=2 m target adjustment per axis
- lens 20–40 mm

Record exact final camera values.

## Phase 10 — visual acceptance

A_CONTEXT must show:
- hopper/feed
- heater
- blow cell
- outfeed
- enclosure/floor
- complete process sequence

B_FUNCTIONAL must show:
- heater outlet
- transfer
- readable mould/blow cell
- outfeed
- connected process path

C_SEQUENCE_DETAIL must show:
- at least two adjacent steps
- heater/transfer/mould relation
- clamp/mould/stretch-blow cues
- formed bottle discharge
- no panel-only framing

D_INTEGRATED must show:
- full west→east sequence
- HMI/operator/service relation
- aisle organization
- legitimate room context.

The label-blind process must read:

`preforms → heating → blow forming → bottles`

No QA-only hiding.

## Phase 11 — protection after

Create:
- `F08_PROTECTION_AFTER.json`
- `F08_PROTECTION_DIFF.json`

Require zero unauthorized differences across all accepted prior facilities and quarantines.

Only exact confirmed F08 legacy retirement visibility/metadata changes are allowed.

## Phase 12 — deterministic GLB export

Do not use broad `use_visible=True`.

Parse current accepted pre-F08 GLB membership.

Expected new membership:
- all pre-F08 names
- minus exact confirmed retired F08 legacy names that were in the pre-F08 GLB
- plus all intended new accepted F08 exportable names.

Use temporary selection staging:
- `use_selection=true`
- `use_visible=false`
- restore temporary state before exit
- do not save staging into Blend.

Create:

`F08_GLB_EXPORT_PARITY.json`

Require:
- zero missing expected names
- zero unexpected names
- all accepted F01-F07 names preserved
- all new F08 intended names present
- exact retired F08 names absent.

If parity fails:

discard attempted GLB,
restore pre-F08 GLB,
STOP `BLOCKED_F08_GLB_EXPORT_PARITY`.

## Phase 13 — save/evidence

Only after all gates pass:

Save canonical Blend.

Retain new canonical GLB only after deterministic parity PASS.

Evidence directory:

`output/rev005-facility-gated/F08_bottle_blow/`

Required:
- `F08_BASELINE_HASHES.json`
- `F08_LEGACY_BOTTLE_BLOW_INVENTORY.json`
- `F08_NEW_ACCEPTED_MANIFEST.json`
- `F08_DIMENSIONAL_VALIDATION.json`
- legacy retirement before/after/diff
- protection before/after/diff
- `F08_CAMERA_VALIDATION.json`
- `F08_GLB_EXPORT_PARITY.json`
- `F08_FINAL_HASHES.json`
- `F08_VALIDATION.json`
- A/B/C/D full renders and previews

Required log:

`coordination/Logs/REV005_F08_BOTTLE_BLOW_MOLDING_CLASS_N_CODEX_LOG.md`

## Git scope

Commit/push:
- canonical Blend
- canonical GLB only after parity PASS
- F08 evidence/renders
- F08 log

Do not edit root `TASKS.md`.
Do not edit locked design/audit criteria.
Do not begin F09.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F08`
