# V09 IMAGE-SPEC 015 — Electrical / LV-MV Room — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/electrical_lv_mv_room_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/electrical_lv_mv_room_B_FUNCTIONAL.png`

## What is wrong
The PNG is 100% black; switchgear functional proof is completely missing.

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
1. Use a medium 3/4 functional camera focused on the primary room/equipment function with visible depth.
2. Target should occupy roughly 70–90% of frame without near-plane clipping or wall/tank obstruction.
3. Show at least three meaningful subcomponents or one complete human-scale room function.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the B_FUNCTIONAL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
