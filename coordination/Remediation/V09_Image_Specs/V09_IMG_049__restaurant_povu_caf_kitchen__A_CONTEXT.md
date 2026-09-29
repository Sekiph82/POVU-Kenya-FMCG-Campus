# V09 IMAGE-SPEC 049 — Restaurant / POVU Café / Kitchen — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/restaurant_povu_caf_kitchen_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/restaurant_povu_caf_kitchen_A_CONTEXT.png`

## What is wrong
Sparse tables/stools and blank partitions read as unfinished dining; café and kitchen are absent.

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
1. Use a 3/4 context camera outside all object bounds.
2. Fit complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
