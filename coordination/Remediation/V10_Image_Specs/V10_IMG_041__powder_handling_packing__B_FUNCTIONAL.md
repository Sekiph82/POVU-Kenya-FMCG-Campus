# V10 IMAGE-SPEC 041 — Powder Handling / Packing — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/powder_handling_packing_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/powder_handling_packing_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B focuses on generic orange/blue machine bodies and guards; dosing and FFS mechanisms remain hidden.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a conical-bottom powder hopper with visible feed outlet, flexible connector and a real screw/auger tube with motor/gearbox.
2. Connect auger to a vertical FFS machine with film roll spindle, visible film web, forming collar/tube, fill tube, vertical/horizontal sealing jaws and cutter.
3. Provide dust extraction hood/duct at hopper and dosing points.
4. Place at least 8 finished sachet/bag meshes on a discharge chute/conveyor.
5. Add side HMI/control pedestal, guarding around moving parts and clear operator service aisle.

## This image must visibly prove
1. Auger outlet visibly enters the FFS forming/fill area.
2. Film roll/web and forming collar/tube visible.
3. Sealing jaws/cutter and discharge path visible.

## Camera
- Medium 3/4 functional view with primary role plus connected subcomponents.
- Camera outside all visible geometry; no clipping/occlusion.
- Do not use camera angle to conceal missing zones.

## Acceptance
PASS only if the V09 failure is gone, label-blind role is clear, required content is visible, V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
