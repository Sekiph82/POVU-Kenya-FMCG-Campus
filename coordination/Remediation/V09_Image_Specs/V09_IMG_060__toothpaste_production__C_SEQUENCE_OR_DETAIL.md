# V09 IMAGE-SPEC 060 — Toothpaste Production — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/toothpaste_production_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/toothpaste_production_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Nearly entire frame is a blue wall/panel; no process sequence.

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
1. Use oblique medium-close framing proving connection/sequence.
2. Show at least two adjacent functional steps plus connecting path.
3. No wall/panel close-up.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for C_SEQUENCE_OR_DETAIL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
