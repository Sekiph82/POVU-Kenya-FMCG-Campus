# V09 IMAGE-SPEC 031 — Liquid Filling / Packaging — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/liquid_filling_packaging_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/liquid_filling_packaging_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Frame is almost entirely teal/purple panel; explicit panel-only failure.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_LIQUID_FILLING_PACKAGING` in place; do not layer another proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global legacy unhide or second Desktop copy.

## Required model corrections
1. Build continuous bottle infeed -> filler -> capper -> label/inspection -> secondary/case pack -> outfeed.
2. Place repeated bottle meshes on conveyors before and after filling.
3. Filler needs visible nozzles/heads over bottle positions; capper needs cap bowl/chute and capping head.
4. Label/inspection needs roll/application elements and sensor/camera station; case pack needs grouped bottles/cases and outfeed.
5. Replace monolithic colored housings with readable frames/guards and preserve service aisle.

## Camera correction
1. Use an oblique medium-close camera that proves connection/sequence.
2. Show at least two adjacent functional steps plus connecting path.
3. Never use wall/panel/tank-shell close-up as evidence.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for C_SEQUENCE_OR_DETAIL, not occluded, visibly better than V08 and free of unrelated restored proxies.
