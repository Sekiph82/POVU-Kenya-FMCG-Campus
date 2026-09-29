# V09 IMAGE-SPEC 050 — Restaurant / POVU Café / Kitchen — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/restaurant_povu_caf_kitchen_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/restaurant_povu_caf_kitchen_B_FUNCTIONAL.png`

## What is wrong
Large brown partition blocks scene; no café backbar or kitchen equipment is visible.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_RESTAURANT_POVU_CAF_KITCHEN` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create three functions in one coherent hospitality layout: dining, café service and kitchen/back-of-house.
2. Dining needs real table/chair assemblies around circulation, not only flat tables/cylinders.
3. Café needs POS/service counter, backbar shelving, beverage-machine silhouettes, undercounter storage and queue/service relationship.
4. Kitchen needs prep worktop, cooking line/hood, sink, storage/refrigeration and pass.
5. Use partitions/doors/half-height separation and brighter warm interior lighting.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
