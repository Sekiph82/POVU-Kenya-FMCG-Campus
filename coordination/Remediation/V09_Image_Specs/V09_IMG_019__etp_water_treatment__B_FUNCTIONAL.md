# V09 IMAGE-SPEC 019 — ETP / Water Treatment — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/etp_water_treatment_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/etp_water_treatment_B_FUNCTIONAL.png`

## What is wrong
Another obstructed tank/partition view; pumps, headers and stages are not demonstrated.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_ETP_WATER_TREATMENT` in place. Do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Lay out visible influent/equalisation -> aeration/treatment -> clarification -> filtration -> discharge/sludge progression.
2. Differentiate stages by basin/vessel shape and accessories.
3. Connect stages with headers, elbows, valves and pump skids that terminate at real process points.
4. Add service walkways, stairs/steps, handrails and pump-maintenance access.
5. Place cameras outside vessel bounding boxes and look across the train rather than between tanks.

## Camera correction for this image
1. Use a medium 3/4 functional camera focused on the primary room/equipment function with visible depth.
2. Target should occupy roughly 70–90% of frame without near-plane clipping or wall/tank obstruction.
3. Show at least three meaningful subcomponents or one complete human-scale room function.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the B_FUNCTIONAL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
