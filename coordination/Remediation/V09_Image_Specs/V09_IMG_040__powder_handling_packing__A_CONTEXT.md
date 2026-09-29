# V09 IMAGE-SPEC 040 — Powder Handling / Packing — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/powder_handling_packing_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/powder_handling_packing_A_CONTEXT.png`

## What is wrong
Generic blue/orange housings and rails are visible; hopper/auger/FFS sequence cannot be identified.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_POWDER_HANDLING_PACKING` in place. Do not layer another generic proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Build feed hopper -> auger/screw dosing -> vertical FFS/sachet/bag forming -> fill -> seal/cut -> finished-pack outfeed.
2. Use a conical-bottom hopper with visible auger/dosing tube rather than featureless cuboid.
3. Give FFS station a roll holder/film path, forming collar/tube, sealing jaws and discharge chute/conveyor.
4. Add dust hood/extraction around feed/dose points and a side control panel.
5. Show repeated finished sachet/bag shapes on outfeed.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
