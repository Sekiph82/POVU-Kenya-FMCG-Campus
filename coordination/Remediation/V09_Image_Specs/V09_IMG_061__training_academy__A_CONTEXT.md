# V09 IMAGE-SPEC 061 — Training / Academy — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/training_academy_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/training_academy_A_CONTEXT.png`

## What is wrong
Tables/stools and shelf appear in an open dark room; instructor zone, screen and finished enclosure are unreadable.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_TRAINING_ACADEMY` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create finished enclosed classroom with perimeter/partition walls, door/opening and ceiling/soffit cues.
2. Provide instructor zone with lectern/desk and large screen/board facing learner seating.
3. Use real desk/chair assemblies with backs/legs, not flat tables plus cylinders.
4. Add storage/cabinet/shelf and clear circulation aisles.
5. Frame instructor zone, learner layout and enclosure together.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
