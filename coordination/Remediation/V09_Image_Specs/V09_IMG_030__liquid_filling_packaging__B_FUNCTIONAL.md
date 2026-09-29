# V09 IMAGE-SPEC 030 — Liquid Filling / Packaging — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/liquid_filling_packaging_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/liquid_filling_packaging_B_FUNCTIONAL.png`

## What is wrong
Housing-dominated composition with no identifiable filler, capper or labeler.

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
1. Use a medium 3/4 camera on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping or wall/tank obstruction.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly better than V08 and free of unrelated restored proxies.
