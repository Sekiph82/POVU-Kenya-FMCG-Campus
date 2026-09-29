# V09 IMAGE-SPEC 033 — Micro-ingredient Weigh / Dispense — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`

## What is wrong
The PNG is 100% black; accepted weighing/dispense evidence is gone.

## Blender ownership / safety
Preserved V07 PASS group: restore visibility/camera/lighting first; do not redesign by default.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global legacy unhide or second Desktop copy.

## Required model corrections
1. Preserve the V07 accepted micro-weigh/dispense geometry; diagnose only why evidence is black.
2. Restore facility collection/object visibility if bulk retirement hid it.
3. Verify scale/weigh station, ingredient bins/containers, dispense points, enclosure and QA lighting.
4. Use prior accepted camera logic after confirming restored walls do not clip it.

## Camera correction
1. Use a medium 3/4 camera on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping or wall/tank obstruction.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly better than V08 and free of unrelated restored proxies.
