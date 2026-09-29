# V09 IMAGE-SPEC 067 — Wellness / Recreation — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/wellness_recreation_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/wellness_recreation_A_CONTEXT.png`

## What is wrong
Teal cuboids and yoga mats do not read as recognizable cardio/resistance equipment; room is sparse/open.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_WELLNESS_RECREATION` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create finished enclosed wellness room with cardio, resistance/weights and yoga/stretch zones.
2. Make cardio machines recognizable treadmills/bikes with bases, decks/flywheel, uprights and consoles, not teal cubes.
3. Add resistance rack/bench/dumbbell or cable-machine silhouettes; retain open yoga mat zone.
4. Add lockers/storage, mirror/wall cue, bright lighting and circulation.
5. Frame all zones in context and functional equipment clearly.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
