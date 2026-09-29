# V10 IMAGE-SPEC 030 — Liquid Filling / Packaging — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/liquid_filling_packaging_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/liquid_filling_packaging_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B shows cap bowl and framed machines, but filler nozzles, cap chute/head, label roll/sensor and case-pack details are not all readable.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a continuous conveyor path with repeated bottle meshes throughout the line: at least 8 bottles at infeed, 8 under/after filler and 8 finished near outfeed.
2. Filler: circular/linear frame with at least 8 visible fill nozzles/heads aligned over bottle positions and product supply manifold.
3. Capper: cap bowl/feeder, chute and capping head visibly meeting bottle path.
4. Label/inspection: label roll/applicator plus sensor/camera/inspection station.
5. Secondary pack: grouped bottles entering a case/tray packer, visible cases/trays and finished outfeed conveyor.
6. Use guarding around moving stations, one operator HMI and a clear service aisle.

## This image must visibly prove
1. Filler nozzles over bottles clearly visible.
2. Cap bowl/chute/capping head visible on the same product path.
3. Label/inspection hardware visible beyond capper.

## Camera
- Medium 3/4 functional view with primary function plus connected subcomponents.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
