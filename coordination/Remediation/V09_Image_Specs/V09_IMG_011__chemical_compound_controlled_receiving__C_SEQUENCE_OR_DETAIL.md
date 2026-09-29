# V09 IMAGE-SPEC 011 — Chemical Compound / Controlled Receiving — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/chemical_compound_controlled_receiving_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/chemical_compound_controlled_receiving_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Only red drums against a wall are visible; no IBC, bund or transfer sequence.

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
1. Use an oblique medium-close camera that proves connection/sequence.
2. Show at least two adjacent functional steps plus their connecting material/product/service path.
3. Never use a wall/panel/tank-shell close-up as evidence.
4. Correct the exact failure described above. Use collection/object bounds to ensure camera origin is outside geometry and line-of-sight is not immediately blocked.
5. Use sensible near/far clipping; do not slice the target.

## Lighting/material proof
- Restore/add neutral QA fill so silhouettes do not disappear into black.
- Keep material separation between floor/envelope/equipment and use bevels/normal smoothing on major hard-surface edges.
- Do not use color alone as machine identity.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the C_SEQUENCE_OR_DETAIL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
