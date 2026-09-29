# V09 IMAGE-SPEC 020 — ETP / Water Treatment — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/etp_water_treatment_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/etp_water_treatment_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
A large yellow wall/curb and vessel edges occupy most of frame; no useful stage-to-stage connection is shown.

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
1. Use an oblique medium-close camera that proves connection/sequence.
2. Show at least two adjacent functional steps plus their connecting material/product/service path.
3. Never use a wall/panel/tank-shell close-up as evidence.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the C_SEQUENCE_OR_DETAIL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
