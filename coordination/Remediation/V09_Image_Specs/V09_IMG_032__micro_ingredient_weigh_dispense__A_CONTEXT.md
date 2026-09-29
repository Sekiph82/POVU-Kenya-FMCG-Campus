# V09 IMAGE-SPEC 032 — Micro-ingredient Weigh / Dispense — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/micro_ingredient_weigh_dispense_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/micro_ingredient_weigh_dispense_A_CONTEXT.png`

## What is wrong
The PNG is 100% black; accepted micro-weigh room context is gone.

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
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone in frame at roughly 65–85% occupancy; no foreground occluder >~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly better than V08 and free of unrelated restored proxies.
