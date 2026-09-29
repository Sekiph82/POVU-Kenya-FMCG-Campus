# V09 IMAGE-SPEC 018 — ETP / Water Treatment — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/etp_water_treatment_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/etp_water_treatment_A_CONTEXT.png`

## What is wrong
Large teal/gray vessel faces dominate and hide the treatment train.

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
1. Use a 3/4 context camera outside every object bounding box, at human-eye to slightly elevated height.
2. Fit the complete functional zone in frame; target should occupy roughly 65–85% of frame and no foreground occluder should cover more than ~15% of it.
3. Show floor plus at least two enclosure/edge cues. Do not aim into black void.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the A_CONTEXT role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
