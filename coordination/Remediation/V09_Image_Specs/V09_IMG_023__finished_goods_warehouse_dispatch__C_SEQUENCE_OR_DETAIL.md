# V09 IMAGE-SPEC 023 — Finished Goods Warehouse / Dispatch — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/finished_goods_warehouse_dispatch_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/finished_goods_warehouse_dispatch_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Racks and boxes appear, but dispatch desk, consolidation lanes and loading relationship are missing.

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
1. Use an oblique medium-close camera that proves connection/sequence.
2. Show at least two adjacent functional steps plus their connecting material/product/service path.
3. Never use a wall/panel/tank-shell close-up as evidence.
4. Correct the exact failure described above; use bounds/line-of-sight checks before rendering.
5. Use sensible near/far clipping and neutral QA fill.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the C_SEQUENCE_OR_DETAIL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
