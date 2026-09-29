# V09 IMAGE-SPEC 016 — Employee Changing / Shower / Locker Support — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/employee_changing_shower_locker_support_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/employee_changing_shower_locker_support_A_CONTEXT.png`

## What is wrong
The PNG is 100% black; room context and lockers are absent.

## Blender ownership / safety
This is a preserved V07 PASS group. Diagnose visibility/camera/lighting regression first; do not redesign by default.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Keep the V07 accepted locker/changing/shower design; do not rebuild it.
2. Restore only preserved facility objects/collection if V08 retirement hid them.
3. Verify locker banks, benches, shower/changing partitions, envelope and lights are enabled.
4. Verify camera is not outside the room looking into void or inside a wall.

## Camera correction for this image
1. Use a 3/4 context camera outside every object bounding box, at human-eye to slightly elevated height.
2. Fit the complete functional zone in frame; target should occupy roughly 65–85% of frame and no foreground occluder should cover more than ~15% of it.
3. Show floor plus at least two enclosure/edge cues. Do not aim into black void.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the A_CONTEXT role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
