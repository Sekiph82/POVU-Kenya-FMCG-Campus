# V09 IMAGE-SPEC 009 — Chemical Compound / Controlled Receiving — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/chemical_compound_controlled_receiving_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/chemical_compound_controlled_receiving_A_CONTEXT.png`

## What is wrong
Foreground vessels/columns block most of the facility; receiving and transfer flow cannot be read.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_CHEMICAL_COMPOUND_CONTROLLED_RECEIVING` in place. Do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Build dock/receiving edge -> drum/IBC staging -> bunded storage -> transfer pump/hoses -> hard-piped controlled transfer.
2. Show IBC cage geometry, drums with lids, bund curb/sump and a pump skid with motor/pump/valves.
3. Connect hoses/pipes visibly to real vessels/transfer points with elbows and valves.
4. Add controlled-access partition/door, circulation aisle and receiving/check station.
5. Move tall vessels out of camera sightlines.

## Camera correction for this image
1. Use a 3/4 context camera outside every object bounding box, at human-eye to slightly elevated height.
2. Fit the complete functional zone in frame; target should occupy roughly 65–85% of frame and no foreground occluder should cover more than ~15% of it.
3. Show floor plus at least two enclosure/edge cues. Do not aim into black void.
4. Correct the exact failure described above. Use collection/object bounds to ensure camera origin is outside geometry and line-of-sight is not immediately blocked.
5. Use sensible near/far clipping; do not slice the target.

## Lighting/material proof
- Restore/add neutral QA fill so silhouettes do not disappear into black.
- Keep material separation between floor/envelope/equipment and use bevels/normal smoothing on major hard-surface edges.
- Do not use color alone as machine identity.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the A_CONTEXT role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
