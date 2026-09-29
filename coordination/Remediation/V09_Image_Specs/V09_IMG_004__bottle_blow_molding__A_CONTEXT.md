# V09 IMAGE-SPEC 004 — Bottle Blow Molding — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/bottle_blow_molding_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/bottle_blow_molding_A_CONTEXT.png`

## What is wrong
Colored housings and pipes fill the view; complete preform-to-bottle sequence is unreadable.

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
