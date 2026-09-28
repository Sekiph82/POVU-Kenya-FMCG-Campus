# REV005 INTERIOR REMEDIATION V07 — VISIBILITY-INTEGRATION ROOT-CAUSE CLOSURE

## Entering status

Independent GPT V06 audit result: REMEDIATION_REQUIRED.

V06 fixed provenance correctly but still achieved only 6/26 visual PASS. The decisive finding is that the project no longer has a simple "not enough objects" problem. V06 reports approximately 1,950 added objects, yet the audited renders still resemble V05 in many areas.

## Mission

Diagnose and fix why V06-added detail is not materially visible/useful in the final REV005 QA and facility views.

This is a visibility/integration/root-cause remediation first, geometry remediation second.

Do NOT begin by mass-adding more objects.

## Canonical tracker

Read root TASKS.md first.

Do not create any .hiveai file or folder.
Do not edit TASKS.md.
Do not edit the locked V07 audit criteria.
Do not self-promote V07 to complete.

## Preserve/freeze

Preserve these six independent PASS groups unless a regression is found:
- Caps and Trigger Assembly
- Daycare / Crèche
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Fire Pump House
- Micro-ingredient Weigh / Dispense

Also preserve:
- REV004 untouched
- current Hands of Growth state
- owner-specified tree removals
- corrected Living Wall extent
- VIP entrance relationships
- no East/West Glass Deck Access presentation references

Do not create REV006.
Do not render owner-review or final-tour video.

## Phase 1 — mandatory V06 visibility/integration diagnostic

For each of the 20 V06 remediation groups, inspect the V06-added objects and determine:

1. Are they in the correct facility coordinates?
2. Are transforms/scales plausible?
3. Are they enabled in viewport and render?
4. Is hide_render false where required?
5. Are collections/view layers enabled for QA and export?
6. Are objects inside, behind or occluded by old proxy geometry?
7. Are old proxy cubes/housings hiding the newly added subassemblies?
8. Are QA cameras still pointing at old V05 proxy geometry?
9. Are V06 objects spatially disconnected from the canonical facility?
10. Are they present in Blender but missing from exported GLB?
11. Are materials/shading making small functional elements visually disappear?
12. Is the useful detail simply too small relative to the camera distance?

Create:
output/rev005-interior-remediation-v07/V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md

For every failing group record:
- root cause category
- affected V06 objects/collections
- corrective action
- whether geometry rebuild was actually required

Do not proceed to broad remodeling until this diagnostic exists.

## Phase 2 — integration correction

Correct the root cause per group.

Allowed corrections include:
- unhide/render-enable
- collection/view-layer correction
- transform/location/scale correction
- moving detail outside/around old proxy shells
- deleting or opening obsolete proxy cover geometry that blocks real detail
- replacing one large proxy box with visible compound subassemblies
- repositioning cameras to show the process
- improving lighting/material contrast
- exporting missing visible objects correctly
- selective additional modeling only when diagnostic proves geometry is genuinely insufficient

## Remaining 20 failing groups

1. Administration / HQ / R&D / QC
2. Bottle Blow Molding
3. Chemical Compound / Controlled Receiving
4. ETP / Water Treatment
5. Finished Goods Warehouse / Dispatch
6. Glass Deck Central Command / Training / Café Gallery
7. Liquid Filling / Packaging
8. Occupational Health / First Aid
9. Packaging Warehouse
10. Powder Handling / Packing
11. Production Hall / Wet Processing / Process Core
12. Raw Material Warehouse / Receiving
13. Restaurant / POVU Café / Kitchen
14. Security / Reception / Visitor Arrival
15. Security Gatehouse
16. Toothpaste Production
17. Training / Academy
18. Utilities / Engineering
19. Wellness / Recreation
20. Wet Wipes Production

## Facility-specific visual closure rules

### Admin / HQ / R&D / QC
Office/admin, meeting and actual lab/QC zones must all be visible. Remove/replace oversized brown masses that hide real detail.

### Bottle Blow Molding
One useful frame must visibly connect preform feed -> heater/oven -> blow/mould cell -> bottle outfeed. Do not use panel closeups.

### Chemical Receiving
Show receiving containers/staging + bunded storage + transfer pump/hoses/piping/valves + controlled access in one operational relationship.

### ETP / Water Treatment
Show treatment stages as a spatial sequence, not isolated tanks/pipes.

### Finished Goods
Show storage + staging + dispatch/loading/control context, not racks alone.

### Glass Deck
Show command + training + café/gallery in a coherent interior. Remove foreground occlusion.

### Liquid Filling
Show bottles and the actual fill/cap/label/inspect/pack sequence. Replace hidden detail behind large proxy housings.

### Occupational Health
Show exam/treatment function, clinical storage/support, waiting/reception and privacy zoning.

### Packaging Warehouse
Show packaging-specific materials and issue-to-production logic, not generic racks/boxes.

### Powder
Show feed/dose -> pack/fill -> seal -> finished pack outfeed in one readable line.

### Wet Processing
Show tanks plus platform/access, agitators, manifolds, pumps, CIP/transfer relationships.

### Raw Material
Show receiving/inspection/staging + raw-material storage and handling context.

### Restaurant / Café / Kitchen
Dining, café service/backbar and kitchen/pass must each be clearly visible.

### Security Reception
Show visitor reception + screening/access-control + onward circulation.

### Gatehouse
Show enclosed booth + operator monitors/controls + visible vehicle lane/barrier relationship.

### Toothpaste
Show mix/hold -> tube feed -> fill -> crimp/seal/code -> carton.

### Training
Show a finished enclosed classroom, not furniture on an open slab.

### Utilities
Visually distinguish compressed air, boiler/steam and RO/water systems.

### Wellness
Show recognisable gym/cardio/resistance/yoga/locker functions in a finished room.

### Wet Wipes
Show parent roll -> web path -> wetting -> fold/cut -> pouch/seal -> discharge continuously.

## QA camera rule

The previous failure repeatedly came from useless closeups.

For every remediation group provide:
- A_CONTEXT: complete useful facility/process view
- B_FUNCTIONAL: human/process-scale view proving core function
- C_SEQUENCE: a view proving relationships/sequence

Do NOT use:
- panel-only closeups
- tank-wall closeups
- pipe-only closeups
- empty-floor views
- duplicate angles
- frames where the subject is mostly hidden

For complex lines, prefer a slightly wider process-scale camera that shows multiple connected stations at once.

## Differential proof

For each of the 20 groups create:
- V06_BEFORE reference path
- V07_AFTER A/B/C
- short statement of what became newly visible

Create:
output/rev005-interior-remediation-v07/REV005_V07_BEFORE_AFTER_MATRIX.md

## Preservation proof

Re-render A/B for the six PASS groups to prove no regression.

## Provenance

Use V06 final as immutable V07 baseline:
- Blend: 393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD
- GLB: 8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089

Before any mutation:
1. hash live canonical Blend/GLB
2. verify exact match to the values above
3. write V07_BASELINE_HASHES.json
4. preserve it before mutation

## Required outputs

output/rev005-interior-remediation-v07/
- V07_BASELINE_HASHES.json
- V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md
- REV005_V07_BEFORE_AFTER_MATRIX.md
- REV005_INTERIOR_REMEDIATION_V07_REPORT.md
- REV005_INTERIOR_REMEDIATION_V07_VALIDATION.json
- REV005_V07_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md
- qa/
- contact sheets

coordination/Logs/REV005_INTERIOR_REMEDIATION_V07_CODEX_LOG.md

Update/export canonical REV005 Blend and GLB.

## Stop gate

STOP at:

AWAITING_GPT_REMEDIATION_AUDIT_V07

Do not create REV006.
Do not create any tour.
Do not freeze REV005.
Do not edit TASKS.md.
Do not self-award GPT PASS.
