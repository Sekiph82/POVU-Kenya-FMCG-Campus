# V09 IMAGE-SPEC 046 — Raw Material Warehouse / Receiving — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/raw_material_warehouse_receiving_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/raw_material_warehouse_receiving_A_CONTEXT.png`

## What is wrong
Foreground orange rack/box masses block receiving overview; dock and inspection context are absent.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_RAW_MATERIAL_WAREHOUSE_RECEIVING` in place. Do not layer another generic proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create inbound flow: loading/receiving door or dock -> inspection/check desk -> quarantine/staging -> raw storage racks.
2. Populate mixed raw pallets, drums and IBCs rather than same-sized boxes only.
3. Use marked staging/quarantine lanes and inspection point near receiving.
4. Provide handling aisle and one forklift/AMR in secondary position; include enclosure cues.
5. Differentiate from finished goods through mixed raw containers and receiving/inspection orientation.

## Camera correction
1. Use a 3/4 context camera outside all object bounds.
2. Fit the complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
