# V10 IMAGE-SPEC 040 — Powder Handling / Packing — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/powder_handling_packing_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/powder_handling_packing_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 A has a giant rectangular hopper and generic framed machines, but no readable auger/film/FFS/sealing/finished-pack sequence.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a conical-bottom powder hopper with visible feed outlet, flexible connector and a real screw/auger tube with motor/gearbox.
2. Connect auger to a vertical FFS machine with film roll spindle, visible film web, forming collar/tube, fill tube, vertical/horizontal sealing jaws and cutter.
3. Provide dust extraction hood/duct at hopper and dosing points.
4. Place at least 8 finished sachet/bag meshes on a discharge chute/conveyor.
5. Add side HMI/control pedestal, guarding around moving parts and clear operator service aisle.

## This image must visibly prove
1. Conical hopper, auger, FFS body, film roll/path, seal/cut zone and finished-pack outfeed visible in order.
2. Dust extraction visible at feed/dose area.
3. Finished packs visibly exit the line.

## Camera
- 3/4 context showing complete facility role, envelope and flow.
- Camera outside all visible geometry; no clipping/occlusion.
- Do not use camera angle to conceal missing zones.

## Acceptance
PASS only if the V09 failure is gone, label-blind role is clear, required content is visible, V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
