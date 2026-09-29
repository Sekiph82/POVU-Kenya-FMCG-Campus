# V09 IMAGE-SPEC 035 — Occupational Health / First Aid — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/occupational_health_first_aid_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/occupational_health_first_aid_B_FUNCTIONAL.png`

## What is wrong
Camera is too close to partition and hides exam/treatment equipment.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_OCCUPATIONAL_HEALTH_FIRST_AID` in place; do not layer another proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global legacy unhide or second Desktop copy.

## Required model corrections
1. Create a coherent clinic envelope with reception/waiting at entry and separated exam/treatment zone.
2. Add exam bed, treatment trolley, clinical cabinets/storage, basin/sink, privacy curtain/track and waiting chairs.
3. Use partitions/door openings to show privacy and circulation; remove tall slabs that block bed/waiting area.
4. Add small clinic cues such as wall cabinet/supply shelf/monitor stand without text labels.
5. Use brighter neutral clinical lighting and clear material separation.

## Camera correction
1. Use a medium 3/4 camera on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping or wall/tank obstruction.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact observed failure and validate camera/target line of sight from bounds.
5. Use neutral QA fill and non-clipping near/far planes.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly better than V08 and free of unrelated restored proxies.
