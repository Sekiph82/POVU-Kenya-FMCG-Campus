# V09 IMAGE-SPEC 029 — Liquid Filling / Packaging — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/liquid_filling_packaging_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/liquid_filling_packaging_A_CONTEXT.png`

## What is wrong
A corridor of purple/white/orange housings hides bottle path and station sequence.

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
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone in frame at roughly 65–85% occupancy; no foreground occluder >~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly better than V08 and free of unrelated restored proxies.
