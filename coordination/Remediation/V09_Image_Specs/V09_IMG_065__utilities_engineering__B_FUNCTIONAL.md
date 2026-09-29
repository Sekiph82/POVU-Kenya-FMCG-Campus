# V09 IMAGE-SPEC 065 — Utilities / Engineering — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/utilities_engineering_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/utilities_engineering_B_FUNCTIONAL.png`

## What is wrong
Severe vessel occlusion; compressor, boiler and RO cannot be distinguished.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_UTILITIES_ENGINEERING` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create three distinguishable systems: compressed air, boiler/steam and RO/water.
2. Compressed air needs compressor housing, receiver, dryer/filter pair and connected air header.
3. Boiler/steam needs boiler body, burner/door, steam header/valves and service clearance.
4. RO/water needs skid frame, membrane vessels/columns, pump/filter components and product/reject piping.
5. Add distribution manifolds/service access; never place camera inside/behind receiver or tank.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
