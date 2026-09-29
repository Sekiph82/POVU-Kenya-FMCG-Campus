# V09 IMAGE-SPEC 038 — Packaging Warehouse — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/packaging_warehouse_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/packaging_warehouse_B_FUNCTIONAL.png`

## What is wrong
Film-roll-like cylinders and boxes appear, but staging/issue logic and enclosure are not demonstrated.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_PACKAGING_WAREHOUSE` in place. Do not layer another generic proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Make packaging role unmistakable with carton bundles, film rolls, label/closure bins or container packaging on dedicated racks.
2. Create separate receiving/staging and issue-to-production zones using floor markings, transfer lane or conveyor.
3. Keep rack aisles unobstructed and handling vehicle secondary to the subject.
4. Add warehouse enclosure/loading/issue openings and readable lighting.
5. Differentiate from raw/finished warehouses through packaging-specific inventory and issue-to-line flow.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without near-plane clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
