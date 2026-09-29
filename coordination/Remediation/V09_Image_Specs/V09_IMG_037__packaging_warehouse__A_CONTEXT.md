# V09 IMAGE-SPEC 037 — Packaging Warehouse — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/packaging_warehouse_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/packaging_warehouse_A_CONTEXT.png`

## What is wrong
Foreground rack structure blocks overview; packaging content and issue-to-production relationship are unreadable.

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
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
