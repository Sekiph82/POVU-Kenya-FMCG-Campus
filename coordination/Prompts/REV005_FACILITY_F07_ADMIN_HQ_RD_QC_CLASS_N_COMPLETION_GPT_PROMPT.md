# M08.41 — F07 ADMINISTRATION / HQ / R&D / QC CLASS N COMPLETION

## Scope

Execute F07 only.

Facility:

`Administration / HQ / R&D / QC`

This is the first Class N facility.

Do not begin F08.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F07_ADMIN_HQ_RD_QC_DESIGN_CONTRACT.md`
4. `coordination/Audits/REV005_F07_ADMIN_HQ_RD_QC_GPT_AUDIT_CRITERIA.md`
5. `coordination/Audits/REV005_INTERIOR_REMEDIATION_V09_GPT_AUDIT.md`
6. V09 Administration image specs 001–003
7. current accepted F01-F06 protection evidence
8. F06 final audit

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

`M08.41 — Facility-Gated F07 Administration / HQ / R&D / QC Class N completion`

If not, STOP before mutation.

## Locked canonical baseline

Blend SHA-256:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

GLB SHA-256:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

If either differs:

STOP `BLOCKED_F07_CANONICAL_BASELINE_MISMATCH`.

## Phase 1 — exact current-state inventory and protection

Before any mutation, create:

`output/rev005-facility-gated/F07_admin_hq_rd_qc/F07_PROTECTION_BEFORE.json`

Protect exact signatures for:

- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted 54
- F06 accepted 43
- F04 Training/Restaurant accepted quarantine state
- F06 exact seven X01 quarantine objects
- V09 Glass Deck quarantine 117
- historical Glass Deck source
- historical Wellness/pavilion protected state
- Restaurant right-wall accepted quarantine state

For every protected object record:
- name
- type
- matrix_world
- dimensions
- parent
- collections
- material slots
- data block
- hide_viewport
- hide_render
- custom properties

Also record relevant protected collection and layer-collection visibility.

## Phase 2 — inventory legacy Administration ownership

Create:

`F07_LEGACY_ADMIN_INVENTORY.json`

Inventory every current object satisfying at least one of:

- facility metadata exactly `Administration / HQ / R&D / QC`;
- membership in `REV005_V08_CLEAN_ADMINISTRATION_HQ_R_D_QC`;
- known current Admin/HQ/R&D/QC object prefixes from the owner inventory.

The historical V09 clean collection previously contained 145 objects, but do not assume current count blindly.

For every candidate record:
- exact name
- facility metadata
- collections
- matrix/dimensions
- visibility
- material/data/parent
- whether present in current GLB
- ownership classification:
  - `CONFIRMED_F07_LEGACY`
  - `AMBIGUOUS_SHARED`
  - `NOT_F07`

If any object that must be retired is ownership-ambiguous:

STOP `BLOCKED_F07_LEGACY_OWNERSHIP_AMBIGUITY`

and do not mutate it.

## Phase 3 — build exact Class N facility

Create destination collection:

`REV005_FG_F07_ADMIN_HQ_RD_QC_ACCEPTED_CLASS_N`

Build to the exact design contract.

Do not reuse the failed V09 blockout as the accepted result.

### Locked room envelope

- center = (-58,-64)
- X = -81…-35
- Y = -78…-50
- plan = 46 × 28 m
- floor slab center Z=1.00
- floor thickness=0.18 m
- wall bottom Z=1.09
- wall top Z=6.80
- ceiling underside≈6.60
- primary circulation >=1.80 m
- secondary circulation >=1.20 m

### Required Z1 — Reception / visitor arrival

Zone:
- X -80…-68
- Y -77…-68

Reception desk:
- center (-74.0,-72.5,1.48)
- 5.5 × 1.0 × 0.78 m
- supported construction, not floating slab
- raised transaction ledge

Entrance:
- front/south at Y≈-78
- double-door clear width 2.40 m
- clear height 2.60 m
- center X=-75.0

Required:
- operator chair
- four visitor chairs
- readable waiting/arrival relationship
- clear route from entrance to internal circulation

### Required Z2 — HQ open office

Zone:
- X -72…-54
- Y -69…-58

Eight workstations.

Desk:
- 1.60 × 0.75 × 0.75 m

Rows:
- Y=-65.2
- Y=-61.3

X:
- -69
- -65
- -61
- -57

Each station must have:
- supported desk
- monitor
- keyboard
- task chair
- visible human-scale spacing

No generic repeated slab-only desks.

### Required Z3 — Meeting / collaboration

Zone:
- X -65…-53
- Y -58…-51

Table:
- center (-59,-54.5,1.47)
- 4.8 × 1.8 × 0.76 m

Chairs:
- 10
- five per long side
- ≈0.90 m center spacing

Display:
- center ≈(-59,-50.35,3.40)
- face 3.2 × 1.8 m

Use glazing/partition cues so the meeting function reads as a room.

### Required Z4 — R&D / QC laboratory

Zone:
- X -51…-36
- Y -76…-57

Lab separation:
- partition X≈-52
- thickness 0.12 m
- two 1.20 m clear glazed door openings

Primary benches:
1. (-48,-72,1.55), 4.0×0.8×0.9
2. (-43,-72,1.55), 4.0×0.8×0.9
3. (-48,-66,1.55), 4.0×0.8×0.9
4. (-43,-66,1.55), 4.0×0.8×0.9

Each bench:
- supported/cabinet base
- at least two visible doors/drawers
- stainless/light neutral worktop

Sink/service bench:
- (-38.5,-72,1.55)
- 2.2×0.8×0.9
- visible basin
- faucet/gooseneck
- splashback

Sample-prep island:
- (-44.5,-60.5,1.55)
- 5.0×1.2×0.9
- storage below
- >=1.20 m usable aisle

### Required QC instruments

Build six visibly distinct label-blind instrument classes:

1. analytical balance
   - approx 0.50×0.45×0.55
   - draft shield
2. pH/conductivity station
   - base ≈0.35×0.30
   - probe arm
3. rotational viscometer
   - base ≈0.45×0.40
   - vertical spindle column
4. spectrophotometer/colorimeter
   - ≈0.55×0.45×0.35
   - sample compartment cue
5. stability/incubator cabinet
   - ≈0.80×0.70×1.60
6. compact centrifuge/mixer
   - ≈0.45×0.45×0.35

Distribute them across benches/island.

Do not make six colored cubes.

### Storage / safety

Five storage bays:
- bay width 1.20 m
- depth 0.45 m
- height 2.20 m
- east lab side

Safety:
- eyewash near (-37.5,-74.5)
- PPE near (-37.5,-73.0)
- spill/first response cabinet near (-37.5,-70.8)

These must be geometry-readable without labels.

## Phase 4 — finish the architecture

Required:
- floor
- back/east/west walls
- front glazing
- mullions
- actual entry opening
- ceiling/soffit cues
- internal partitions
- visible doors
- no black/open void
- no camera-only fake shell

Front facade must remain sufficiently glazed to read the interior.

Use the material/lighting contract exactly:
- neutral floor/walls
- wood office furniture
- stainless/white lab
- restrained safety color
- 12 ceiling light modules minimum
- 4000K-neutral appearance
- task lighting over lab as needed

## Phase 5 — legacy retirement

Only after the new F07 build is internally complete:

Quarantine exact objects classified `CONFIRMED_F07_LEGACY`.

Allowed:
- hide_viewport=true
- hide_render=true
- add:
  - `REV005_F07_LEGACY_RETIRED=true`
  - `REV005_F07_RETIRED_BY="F07_CLASS_N"`

Not allowed:
- delete
- transform
- material edit
- mesh edit
- change unrelated collection visibility

Do not quarantine `AMBIGUOUS_SHARED` objects.

Create:

- `F07_LEGACY_RETIREMENT_BEFORE.json`
- `F07_LEGACY_RETIREMENT_AFTER.json`
- `F07_LEGACY_RETIREMENT_DIFF.json`

## Phase 6 — exact geometry/dimension validation

Create:

`F07_DIMENSIONAL_VALIDATION.json`

Validate every locked anchor and zone from the design contract.

Required tolerance:
- primary room/zone anchor <=0.05 m
- furniture/equipment <=0.10 m
- aisle shortfall <=0.10 m maximum

Also validate:
- no required object outside F07 envelope unless intentionally part of front entry/glazing hardware;
- no new F07 geometry intersects protected F01-F06 objects.

If protected cross-facility collision is found:

STOP `BLOCKED_F07_CROSS_FACILITY_COLLISION`

Do not mutate the neighbor.

## Phase 7 — final cameras

Use exact seeds from the design contract first.

### A_CONTEXT
- camera (-78,-75,5.2)
- target (-57,-64,2.6)
- lens 24 mm

### B_FUNCTIONAL
- camera (-69,-67,4.4)
- target (-45,-66,2.4)
- lens 32 mm

### C_LAB_DETAIL
- camera (-50.5,-75,3.8)
- target (-43.5,-67.5,2.2)
- lens 40 mm

### D_INTEGRATED
- camera (-77,-71,5.8)
- target (-52,-63.5,2.7)
- lens 24 mm

Sensor:
- 36 mm

Final render:
- 1440×960

Independent-audit preview:
- 900×600

If a seed intersects geometry or materially clips a required cue, small refinement is allowed:
- <=3 m per camera axis
- <=2 m per target axis
- lens 20–40 mm

Record exact final values.

## Phase 8 — visual gate

A_CONTEXT must prove:
- arrival/reception
- office depth
- meeting or lab separation
- finished enclosure
- circulation

B_FUNCTIONAL must prove:
- multiple real office workstations
- office→lab relationship
- lab partition
- multiple real lab benches/instruments

C_LAB_DETAIL must prove:
- >=3 distinct QC instruments
- supported benches/cabinets
- sink/service or sample-prep workflow
- no generic box-only lab

D_INTEGRATED must prove:
- >=3 functional zones
- circulation
- finished interior
- no dominant occluder
- no black void

All evidence is label-blind.

No QA-only hiding is permitted.

## Phase 9 — protection after

Create:

`F07_PROTECTION_AFTER.json`
`F07_PROTECTION_DIFF.json`

Require zero unauthorized prior-state differences.

The only allowed old-state visibility changes are exact confirmed F07 legacy retirement objects.

## Phase 10 — deterministic GLB export

Do not use broad `use_visible=True`.

Parse the pre-F07 accepted GLB node-name membership.

Build new intended membership:

- every pre-F07 node except exact legacy F07 nodes intentionally retired;
- plus every new accepted F07 exportable object;
- no unrelated omission;
- no unrelated new node.

Use temporary selection/export staging only.

Allowed:
- in-memory selection/hide manipulation needed to select intended nodes
- `use_selection=true`
- `use_visible=false`
- restore all temporary state before exit

Do not save temporary staging state into Blend.

Create:

`F07_GLB_EXPORT_PARITY.json`

Require:
- zero missing expected names
- zero unexpected names
- all accepted F01-F06 baseline names preserved
- all new F07 intended names present
- exact retired F07 legacy names absent

If parity fails:

discard attempted GLB,
restore the pre-F07 accepted GLB,
STOP `BLOCKED_F07_GLB_EXPORT_PARITY`.

## Phase 11 — save/evidence

Only after geometry, visual and protection gates pass:

Save canonical Blend.

Export and retain canonical GLB only after deterministic membership parity passes.

Evidence directory:

`output/rev005-facility-gated/F07_admin_hq_rd_qc/`

Required files:

- `F07_BASELINE_HASHES.json`
- `F07_LEGACY_ADMIN_INVENTORY.json`
- `F07_NEW_ACCEPTED_MANIFEST.json`
- `F07_DIMENSIONAL_VALIDATION.json`
- `F07_LEGACY_RETIREMENT_BEFORE.json`
- `F07_LEGACY_RETIREMENT_AFTER.json`
- `F07_LEGACY_RETIREMENT_DIFF.json`
- `F07_PROTECTION_BEFORE.json`
- `F07_PROTECTION_AFTER.json`
- `F07_PROTECTION_DIFF.json`
- `F07_CAMERA_VALIDATION.json`
- `F07_GLB_EXPORT_PARITY.json`
- `F07_FINAL_HASHES.json`
- `F07_VALIDATION.json`
- A/B/C/D full renders and previews

Required log:

`coordination/Logs/REV005_F07_ADMIN_HQ_RD_QC_CLASS_N_CODEX_LOG.md`

## Git scope

Commit/push:
- canonical Blend
- canonical GLB only after export parity PASS
- F07 evidence/renders
- F07 log

Do not edit root `TASKS.md`.
Do not edit locked design/audit criteria.
Do not begin F08.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F07`
