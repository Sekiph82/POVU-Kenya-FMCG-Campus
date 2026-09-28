# REV005 INTERIOR REMEDIATION V08 — CLEAN-REPLACEMENT FINAL VISUAL CLOSURE

## Entering status

Independent GPT V07 audit result:

`REMEDIATION_REQUIRED`

V07 correctly identified and removed real legacy-proxy occlusion, but independent review of all 72 V07 QA renders still found only **6/26 visual PASS**.

The remaining blocker is now proven to be intrinsic model quality in the 20 failing groups:
- under-modeling;
- generic primitive geometry;
- incomplete architectural enclosure;
- missing facility-specific subassemblies;
- process sequences that cannot be understood label-blind.

Do NOT spend another cycle primarily on proxy hiding, camera widening, or visibility debugging.

## Canonical tracker

Read root `TASKS.md` first.

Do NOT create `.hiveai`.
Do NOT edit root `TASKS.md`.
Do NOT edit the locked V08 GPT audit criteria.
Do NOT self-promote V08 or downstream tasks.

## Preserve the six independent-PASS groups

These six groups are frozen for visual content unless a genuine regression is discovered:

1. Caps and Trigger Assembly
2. Daycare / Crèche
3. Electrical / LV-MV Room
4. Employee Changing / Shower / Locker Support
5. Fire Pump House
6. Micro-ingredient Weigh / Dispense

Re-render them only for regression proof.

## V08 strategy: clean replacement, not layered patching

For each of the 20 failing groups:

1. Create a dedicated V08 clean subcollection:
   `REV005_V08_CLEAN_<GROUP>`

2. Identify all obsolete generic/proxy geometry from V03-V07 that visually represents the same facility and would conflict with the clean replacement.

3. Hide those obsolete facility-specific proxies from canonical render/export only after recording them in the V08 report.

4. Build a new low-poly but function-specific facility representation from meaningful subassemblies.

5. Produce an **ISOLATED_LABEL_BLIND** proof render of the clean facility before campus integration.

6. If the isolated image still requires the filename to understand the facility/process, continue modeling. Do not proceed to integrated QA yet.

7. After isolated proof is visually self-explanatory, integrate the clean replacement into the canonical campus and produce:
   - A_CONTEXT
   - B_FUNCTIONAL
   - C_SEQUENCE_OR_DETAIL

8. Verify no regression to exterior/master architecture or the six preserved PASS groups.

## Anti-placeholder rule

The following are explicitly forbidden as completion strategies:

- one colored cuboid representing an entire machine;
- rows of featureless cuboids representing offices/labs;
- tanks without connected functional systems;
- warehouse racks without receiving/dispatch/issue logic;
- labels/object names used as proof;
- repeated generic machine boxes recolored for different processes;
- open gray slab interiors presented as complete occupied rooms.

Primitive geometry is allowed only as subcomponents of recognizable assemblies.

## Architectural-interior rule

Occupied/support spaces must show a believable finished concept-level interior.

At minimum, where appropriate:
- floor;
- enclosing walls/partitions;
- doors/openings;
- glazing where relevant;
- ceiling/soffit cue;
- circulation;
- furniture/equipment zoning;
- storage/service functions;
- human-scale layout.

Use cutaway review views if needed, but never delete the whole envelope just to expose props.

## The 20 V08 clean-replacement groups

### 1. Administration / HQ / R&D / QC

Must visibly contain and distinguish:
- reception/admin arrival;
- real office workstations;
- meeting/collaboration;
- R&D/QC laboratory benches;
- lab-specific equipment/storage;
- partitions/doors/circulation;
- ceiling/soffit/enclosure cues.

Plain brown cuboid rows are prohibited.

### 2. Bottle Blow Molding

Must visibly show:
- preform hopper/feed;
- preform movement;
- oven/heater section;
- guarded mould/clamp/blow cell;
- formed bottle outfeed;
- visible preform/bottle product cues;
- operator/service access.

### 3. Chemical Compound / Controlled Receiving

Must visibly show:
- receiving dock/edge or staging;
- drums/IBCs/containers;
- bunded storage;
- transfer pumps;
- hoses/piping/valves;
- controlled-access partition/door;
- safe circulation.

### 4. ETP / Water Treatment

Must visibly read as a treatment train:
- influent/equalisation stage;
- treatment/aeration/clarification cues;
- filtration;
- pumps;
- sludge/service handling;
- interconnected piping;
- walkway/rails/service access.

### 5. Finished Goods Warehouse / Dispatch

Must show:
- finished-goods pallet/rack storage;
- consolidation/staging;
- dispatch control;
- loading edge/dock relationship;
- AMR/forklift circulation context;
- enclosed warehouse cues.

Must differ clearly from Raw Material and Packaging Warehouse.

### 6. Glass Deck Command / Training / Café Gallery

Must be one coherent finished interior with three readable zones:
- command/operations monitoring wall + consoles;
- training/collaboration tables/seating/presentation;
- café/gallery counter/backbar/service/seating;
- circulation and architectural enclosure/glazing.

Do not reintroduce East/West Glass Deck Access callouts.

### 7. Liquid Filling / Packaging

Must visibly show:
- bottle infeed with actual bottle units;
- filling heads/nozzles or rotary fill geometry;
- cap feed/capper;
- label roll/application station;
- inspection/transfer;
- case/secondary pack;
- product outfeed;
- guards/frames/service aisle.

### 8. Occupational Health / First Aid

Must show:
- reception/waiting;
- exam/treatment bed;
- trolley;
- cabinets/clinical storage;
- basin/support;
- privacy partition/curtain;
- coherent room envelope.

### 9. Packaging Warehouse

Must show packaging-specific content:
- cartons;
- film rolls;
- labels/containers where appropriate;
- racks;
- receiving/staging;
- issue-to-production zone;
- handling aisles;
- enclosure.

### 10. Powder Handling / Packing

Scope is powder handling/packing.

Must show:
- hopper/feed;
- auger/dosing;
- FFS/sachet/bag packing identity;
- fill;
- seal;
- finished pack outfeed;
- dust/containment cues where appropriate.

### 11. Production Hall / Wet Processing / Process Core

Must show:
- mix/process tanks;
- agitator motors;
- access platform/stairs/rails;
- manifolds/process piping;
- pumps;
- CIP skid/cleaning relationship;
- coherent transfer toward filling.

A row of tanks alone is prohibited.

### 12. Raw Material Warehouse / Receiving

Must show:
- receiving dock/door/edge;
- inspection/staging;
- raw pallets/drums/IBCs;
- racks;
- handling aisles;
- receiving/check desk;
- enclosure.

### 13. Restaurant / POVU Café / Kitchen

All three functions must be independently readable:
- dining zone;
- café/POS/service counter/backbar;
- kitchen/back-of-house with prep/cooking/sink/storage/pass;
- partitions/enclosure;
- circulation/service relationship.

### 14. Security / Reception / Visitor Arrival

Must show:
- enclosed reception/security desk;
- visitor seating;
- CCTV/security workstation;
- screening/access control/turnstile cues;
- onward circulation;
- walls/glazing/openings.

### 15. Security Gatehouse

Must show:
- enclosed booth;
- windows;
- operator desk/CCTV;
- barrier controls;
- barrier arm;
- vehicle lane relationship;
- door/service access.

### 16. Toothpaste Production

Must show:
- vacuum/mixing vessel;
- holding/transfer;
- visible tube magazine/tubes;
- tube fill/nozzle;
- crimp/seal;
- code/inspect;
- carton handling;
- coherent sequence.

### 17. Training / Academy

Must show:
- enclosed classroom;
- instructor zone;
- screen/board;
- desks/tables/seating;
- storage;
- door/opening/circulation;
- ceiling/soffit cues.

### 18. Utilities / Engineering

Must visually distinguish project-supported systems:
- compressed air compressor + receiver/dryer;
- boiler/steam;
- RO/water skid/columns;
- distribution manifolds;
- maintenance/service access.

Do not invent unsupported major utility systems.

### 19. Wellness / Recreation

Must show a real enclosed wellness interior:
- cardio machines;
- resistance/weights or functional training;
- yoga/stretch zone;
- lockers/storage;
- mirrors/wall cues where useful;
- circulation/enclosure.

### 20. Wet Wipes Production

Must show visible material continuity:
- parent roll unwind;
- web path;
- wetting/impregnation;
- folding/converting;
- cutting/stacking;
- pouch/feed-film roll;
- sealing;
- pack discharge.

The web/material path must make the process understandable without a label.

## Isolated proof gate

For each of the 20 remediation groups produce:

`qa_isolated/<group>_ISOLATED_LABEL_BLIND.png`

The facility must occupy most of the frame.

The image must not contain:
- label;
- title;
- filename text;
- callout;
- explanatory overlay.

Codex must ask internally:

> Could a reviewer identify the function from geometry alone?

If no, continue modeling before integration.

## Integrated QA gate

After isolated proof passes, render:

- `A_CONTEXT`
- `B_FUNCTIONAL`
- `C_SEQUENCE_OR_DETAIL`

for each of the 20 remediation groups.

For the six preserved groups render:
- `A_CONTEXT`
- `B_FUNCTIONAL`

Expected minimum:
- 20 isolated = 20
- 20 × 3 integrated = 60
- 6 × 2 preserved = 12
- **92 total QA renders**

All renders must be unlabeled, non-empty, well lit and materially different.

## Before/after provenance

Before any canonical REV005 mutation:
- hash V07-final Blend/GLB;
- write immutable `V08_BASELINE_HASHES.json`;
- commit/preserve it before mutation;
- never overwrite before values.

Expected V07 baseline:
- Blend: `BF61CAFCD0EA20E5FE371D491913A51D866AE058F58242FDC30B94AB454ACBD8`
- GLB: `105C83237E5903B1957E206A17E278B7B60214BE38E78F65AB65937294338BE7`

## Required artifacts

Create:
- `output/rev005-interior-remediation-v08/V08_BASELINE_HASHES.json`
- `output/rev005-interior-remediation-v08/V08_CLEAN_REPLACEMENT_MAP.md`
- `output/rev005-interior-remediation-v08/REV005_INTERIOR_REMEDIATION_V08_REPORT.md`
- `output/rev005-interior-remediation-v08/REV005_INTERIOR_REMEDIATION_V08_VALIDATION.json`
- `output/rev005-interior-remediation-v08/REV005_V08_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md`
- `output/rev005-interior-remediation-v08/CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md`
- `output/rev005-interior-remediation-v08/qa_isolated/`
- `output/rev005-interior-remediation-v08/qa/`
- contact sheets for isolated and integrated evidence
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V08_CODEX_LOG.md`

Update canonical REV005 Blend and GLB only after baseline capture.

## Protection gates

Verify:
- REV004 unchanged;
- no REV006;
- no tour;
- no `.hiveai`;
- TASKS.md untouched;
- locked criteria untouched;
- exterior owner corrections preserved;
- East/West Glass Deck Access presentation references absent.

## Stop gate

STOP at:

`AWAITING_GPT_REMEDIATION_AUDIT_V08`

Do not create an owner-review video.
Do not create a final tour.
Do not freeze REV005.
Do not edit TASKS.md.
