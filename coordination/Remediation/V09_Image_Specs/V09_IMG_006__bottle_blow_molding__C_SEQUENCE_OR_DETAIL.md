# V09 IMAGE-SPEC 006 — Bottle Blow Molding — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/bottle_blow_molding_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/bottle_blow_molding_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Almost the entire frame is a flat blue panel with a tiny yellow fragment; explicit panel-only failure.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING` in place. Do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Build one readable preform hopper/feed -> heater/oven -> guarded mould/blow cell -> bottle outfeed line.
2. Show repeated preforms on the feed path and repeated formed bottles on the outfeed.
3. Give the heater a tunnel/frame with heater banks and visible product path.
4. Give the blow cell structural frame, guards, mould/clamp zone, service doors and air-manifold cues.
5. Remove/reshape monolithic housings that block the process path.

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
