# V10 IMAGE-SPEC 032 — Micro-ingredient Weigh / Dispense — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/micro_ingredient_weigh_dispense_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/micro_ingredient_weigh_dispense_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 A shows a white block, a yellow post and a few brown blocks on an empty slab. The accepted V05 hoppers/weigh layout is gone.

## Required Blender correction
Restore the complete accepted V05 facility from commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract. Do not reconstruct it from V09 primitives.

1. Restore the complete accepted V05 Micro-ingredient Weigh / Dispense facility from commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove the V09 sparse block substitute.
3. Preserve V05 hoppers/bins, weigh stations, dosing/dispense layout, operator access and room context.
4. Do not recreate accepted equipment from generic white/yellow cuboids.

## This image must visibly prove
1. Multiple ingredient bins/hoppers and weigh stations visible.
2. Dispense/dosing relationship and operator access visible.
3. The restored V05 facility occupies most of frame.

## Camera
- 3/4 cutaway context, complete room/line and envelope visible.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
