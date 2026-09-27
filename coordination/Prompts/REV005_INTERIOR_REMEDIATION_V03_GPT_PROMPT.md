# REV005 INTERIOR REMEDIATION V03 — VISUAL COMPLETION GATE

## Entering status
V02 independent GPT visual audit result: `REMEDIATION_REQUIRED`.

V02 improved functional specificity and passed structural/pre-validation checks, but REV005 is still not visually complete enough to be accepted as the final fully modeled campus interior revision. This is NOT an object-count remediation. Do not treat existing object counts, named objects, or validation presence as proof of visual completion.

## Primary acceptance rule
For every remediated interior, a reviewer looking ONLY at the QA render, with filenames, labels, callouts and metadata hidden, must be able to understand what kind of room/process/facility is being shown.

If the facility identity depends on a label, object name, report text, or explanation, it is NOT complete.

## Mission
Raise the remaining weak REV005 interiors from schematic/blockout quality to credible finished low-poly architectural/industrial interiors while preserving the approved POVU visual language and all already-good work.

Work only in REV005. REV004 is frozen. Do not create REV006. Do not create the final tour yet.

## Preserve / do not unnecessarily rebuild
V02 independent GPT audit accepted:
- Caps & Trigger Assembly
- Micro-ingredient Weigh / Dispense

Also preserve all previously accepted V01 areas and all regression-passing groups unless a shared-scene correction is strictly required.

Preserve approved exterior corrections:
- Hands of Growth state/location
- owner-specified tree removals
- corrected Living Wall extent
- VIP entrance relationships
- no East Glass Deck Access presentation/callout
- no West Glass Deck Access presentation/callout

## Required V03 focused remediation

### 1. Bottle Blow Molding
Current V02 still reads as simplified boxes/conveyor rather than a convincing blow-molding line.

Create a visually unmistakable low-poly blow-molding process including coherent process sequence and recognisable machine architecture: preform feed/hopper, heating/oven section, mould/clamp/blow station, bottle discharge/outfeed, guards/enclosures and believable machine-to-machine relationships. The render must communicate blow molding without a label.

### 2. Liquid Filling / Packaging
The rotary filler is beginning to read correctly, but the complete line remains too generic.

Create a coherent recognisable production flow: bottle infeed, filling section with visually readable filling heads/nozzles, capping, labeling, inspection/transfer and secondary packing/case handling. Improve machine housings, guards, conveyor relationships and operator/service zones. It must look like one integrated FMCG filling/packaging line, not disconnected props.

### 3. Toothpaste Production
V02 remains visually generic and does not convincingly communicate toothpaste manufacture/filling.

Create a recognisable toothpaste-specific workflow: mixing/vacuum processing vessel, transfer/holding, tube handling/magazine, tube filling, sealing/crimping, coding/inspection and cartoning/packing. Arrange the equipment as a believable process sequence. A reviewer must recognise a tube-product/toothpaste operation without reading the label.

### 4. Wet Wipes Production
V02 remains insufficiently identifiable and must not resemble generic production blocks or the toothpaste line.

Create a visually recognisable wet-wipes converting line: parent roll/unwind, web path, wetting/impregnation section, folding/converting section, cutting/stacking, pouch/feed-film packaging, sealing and discharge. Use machine proportions and visible web/roll/conveyor relationships that distinguish this process immediately from other lines.

### 5. Central Glass Deck Command / Training / Café Gallery
V02 is not a finished interior. Convert it from sparse props into a coherent occupied architectural interior.

It must visibly contain and spatially distinguish:
- command/operations zone with credible monitoring/display wall and operator consoles/workstations;
- training/collaboration zone with tables/seating/presentation function;
- café/gallery zone with proper counter, backbar/service components, seating and circulation;
- coherent floor, wall, ceiling/soffit, lighting/architectural boundaries where appropriate;
- believable circulation and visual relationships between the three functions.

Do not reintroduce East/West Glass Deck Access callouts or presentation references.

### 6. Restaurant / POVU Café / Kitchen
Regression presence is NOT enough. Current QA reads as sparse tables rather than a completed restaurant/café/kitchen interior.

Complete the actual space so it visibly reads as hospitality:
- dining tables and chairs with intentional layout;
- café/service counter and point-of-service identity;
- kitchen/preparation/back-of-house equipment appropriate to the low-poly style;
- service/pass relationship where appropriate;
- walls/partitions, circulation, functional zoning and architectural enclosure;
- enough detail that dining, café service and kitchen functions are independently legible.

### 7. Daycare / Crèche
Regression presence is NOT enough. Current QA does not convincingly read as a finished daycare.

Complete it as a recognisable child-oriented interior with appropriately scaled furniture and clear activity functions, for example activity/play tables, child seating, storage/cubbies, soft/play zone, learning/play elements, caregiver visibility/circulation and coherent room enclosure. Keep the POVU low-poly language. Do not rely on text labels to make the room identifiable.

## Campus-wide interior completion sweep
The project requirement remains: **REV005 is the complete version with the interiors of all campus buildings modeled.**

After the seven focused corrections, perform a visual completion sweep across all 26 canonical facility groups. Do not merely check whether objects exist. Identify any other facility whose interior is still visibly empty, placeholder-like, generic, incoherent, badly enclosed or only identifiable through labels.

If such an area exists, finish it within REV005 before handoff. Preserve already-good areas and avoid gratuitous redesign.

## Architectural completion standard
For occupied interiors, avoid the appearance of furniture floating on an empty slab. Where the building model permits it, establish readable spatial enclosure and zoning through floors, walls/partitions, ceilings/soffits, counters, storage, lighting/fixtures or other low-poly architectural cues appropriate to the facility.

For industrial interiors, avoid isolated primitive boxes. Equipment should form a visually coherent process with believable sequence, proportions, interfaces, conveyors/piping/web paths/guards where appropriate, operator access and service relationships.

Do not inflate object counts for validation. Quality and legibility are the gate.

## QA evidence rules
Create a new package:
`output/rev005-interior-remediation-v03/`

For each of the 7 focused targets provide at least:
- `A_WIDE` — clearly shows the overall room/line and its spatial identity
- `B_FUNCTIONAL` — clearly shows the defining equipment/furniture/function
- `C_PROCESS_OR_DETAIL` — proves process sequence or architectural completion

QA renders must:
- contain NO facility-identifying callout/label that could bias the audit;
- be well lit;
- use useful human-scale/presentation-scale camera positions;
- avoid trees, walls or unrelated geometry blocking the subject;
- show the actual target rather than merely proving objects exist;
- be materially different views when multiple views are supplied.

Also provide a campus-wide visual-completion contact sheet or index of QA views covering all 26 canonical facility groups so GPT can audit the claim that every building interior is complete.

## Validation
Structural validation remains required but cannot award visual PASS.

Validate:
- 26/26 canonical facility groups remain present;
- accepted Caps & Trigger and Micro-Weigh work remains intact;
- all previously accepted V01 areas remain intact;
- approved exterior corrections remain intact;
- restricted East/West Glass Deck Access live/presentation references remain absent;
- REV004 hash remains unchanged;
- no REV006 exists;
- no final tour is produced.

## Required deliverables
- updated canonical REV005 `.blend`
- updated canonical REV005 `.glb`
- `output/rev005-interior-remediation-v03/REV005_INTERIOR_REMEDIATION_V03_REPORT.md`
- `output/rev005-interior-remediation-v03/REV005_INTERIOR_REMEDIATION_V03_VALIDATION.json`
- `output/rev005-interior-remediation-v03/qa/`
- 26-group visual completion contact sheet/index
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V03_CODEX_LOG.md`

Record before/after SHA-256 hashes and REV004 protection evidence.

## Handoff gate
Do NOT self-award final visual acceptance.

Before handoff, internally verify the decisive question for every focused target:
**If all labels and filenames disappeared, would a reviewer understand what this place/process is from the image itself?**

If the answer is no, continue modeling before handoff.

Final response must include:
- status
- focused remediation closure count
- campus-wide 26-group completion sweep result
- canonical REV005 `.blend` and `.glb` paths
- QA package path
- commit SHA
- full GitHub URL to the V03 Codex log

## STOP GATE
STOP after V03 modeling, campus-wide visual completion sweep, QA and validation.

Do not create an owner-review video.
Do not create the final campus tour.
Do not create REV006.

Final state:
`AWAITING_GPT_REMEDIATION_AUDIT_V03`
