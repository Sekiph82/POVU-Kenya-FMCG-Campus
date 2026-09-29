# V09 IMAGE-SPEC 041 — Powder Handling / Packing — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/powder_handling_packing_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/powder_handling_packing_B_FUNCTIONAL.png`

## What is wrong
Large orange block and guards dominate; dosing and fill/seal mechanisms remain hidden.

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
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without near-plane clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
