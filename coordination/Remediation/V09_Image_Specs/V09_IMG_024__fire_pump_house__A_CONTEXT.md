# V09 IMAGE-SPEC 024 — Fire Pump House — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/fire_pump_house_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/fire_pump_house_A_CONTEXT.png`

## What is wrong
The PNG is 100% black; the accepted fire-pump room is not rendered.

## Blender ownership / safety
Preserved V07 PASS group: restore visibility/camera/lighting first; do not redesign by default.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global legacy unhide or second Desktop copy.

## Required model corrections
1. Do not remodel the accepted pump house; restore its render/export visibility after the V08 retirement sweep.
2. Compare V07/current collection and object render flags; re-enable only pump-house equipment/envelope.
3. Verify pumps, manifold/header, valves, room envelope, lighting and camera clipping.
4. Context must show pump-house arrangement; functional view must show pumps/manifold.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone in frame at roughly 65–85% occupancy; no foreground occluder >~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly better than V08 and free of unrelated restored proxies.
