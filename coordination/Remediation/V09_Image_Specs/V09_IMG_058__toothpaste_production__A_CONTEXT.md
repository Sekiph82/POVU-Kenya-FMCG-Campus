# V09 IMAGE-SPEC 058 — Toothpaste Production — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/toothpaste_production_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/toothpaste_production_A_CONTEXT.png`

## What is wrong
Some nozzle/roller details appear, but repeated colored towers dominate and coherent mix-to-carton path is missing.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_TOOTHPASTE_PRODUCTION` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Build vacuum mix vessel -> holding/transfer -> tube magazine/feed -> tube fill -> crimp/seal/code -> carton/outfeed.
2. Mix vessel needs lid, agitator/vacuum topwork and transfer pipe/pump.
3. Tube line must show repeated tube meshes in magazine/holders and fill nozzles aligned to positions.
4. Crimp/seal/code station needs jaws/head plus inspection/code unit; downstream shows cartons/grouped finished tubes.
5. Replace repeated colored box towers with frames, conveyors, guards and connected product path.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
