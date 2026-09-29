# V09 IMAGE-SPEC 014 — Electrical / LV-MV Room — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/electrical_lv_mv_room_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/electrical_lv_mv_room_A_CONTEXT.png`

## What is wrong
The PNG is 100% black; the accepted room/panel context is absent.

## Blender ownership / safety
This is a preserved V07 PASS group. Diagnose visibility/camera/lighting regression first; do not redesign by default.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Preserve accepted LV/MV geometry; reverse only render visibility regression.
2. Re-enable switchgear/panel rows, room envelope, safety clearance/aisle objects and relevant lights if hidden.
3. Check view-layer exclusion, `hide_render`, camera clipping and world/area-light availability.
4. Context view must show room/panel arrangement; functional view must show recognizable switchgear faces and aisle.

## Camera correction for this image
1. Use a 3/4 context camera outside every object bounding box, at human-eye to slightly elevated height.
2. Fit the complete functional zone in frame; target should occupy roughly 65–85% of frame and no foreground occluder should cover more than ~15% of it.
3. Show floor plus at least two enclosure/edge cues. Do not aim into black void.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the A_CONTEXT role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
