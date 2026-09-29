# V09 IMAGE-SPEC 022 — Finished Goods Warehouse / Dispatch — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/finished_goods_warehouse_dispatch_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/finished_goods_warehouse_dispatch_B_FUNCTIONAL.png`

## What is wrong
Frame is mostly empty floor with a small bench/platform; no dispatch function is proven.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_FINISHED_GOODS_WAREHOUSE_DISPATCH` in place. Do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Create finished-goods flow: pallet/rack storage -> consolidation/staging -> dispatch control -> loading edge/dock.
2. Use loaded pallet racks, marked staging lanes, dispatch/control desk and loading doors/dock geometry.
3. Add AMR/forklift circulation in context with unobstructed aisle.
4. Add wall/roof/door cues so racks do not float in black space.
5. Differentiate from raw/packaging via finished-case palletization and outbound loading.

## Camera correction for this image
1. Use a medium 3/4 functional camera focused on the primary room/equipment function with visible depth.
2. Target should occupy roughly 70–90% of frame without near-plane clipping or wall/tank obstruction.
3. Show at least three meaningful subcomponents or one complete human-scale room function.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the B_FUNCTIONAL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
