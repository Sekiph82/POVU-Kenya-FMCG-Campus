# V10 IMAGE-SPEC 025 — Fire Pump House — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/fire_pump_house_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/fire_pump_house_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B is essentially blank and contains no readable pump, motor, header or valve system.

## Required Blender correction
Restore the complete accepted V05 facility from commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract. Do not reconstruct it from V09 primitives.

1. Restore the complete accepted V05 Fire Pump House from commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove the V09 near-empty result.
3. Preserve paired pump sets, motors, suction/discharge headers, manifold, valves and room/house context.
4. Do not rebuild fire pumps as tiny colored blocks.

## This image must visibly prove
1. At least two pump/motor sets visible at functional scale.
2. Header/manifold and multiple valves visible and physically connected.
3. The restored V05 geometry dominates the frame, not empty floor.

## Camera
- Medium 3/4 functional view with primary function plus connected subcomponents.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
