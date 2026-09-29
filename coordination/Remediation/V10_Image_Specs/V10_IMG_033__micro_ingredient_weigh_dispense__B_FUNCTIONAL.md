# V10 IMAGE-SPEC 033 — Micro-ingredient Weigh / Dispense — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B is a closer view of the same white block and yellow post, with no readable weigh/dispense equipment.

## Required Blender correction
Restore the complete accepted V05 facility from commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract. Do not reconstruct it from V09 primitives.

1. Restore the complete accepted V05 Micro-ingredient Weigh / Dispense facility from commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove the V09 sparse block substitute.
3. Preserve V05 hoppers/bins, weigh stations, dosing/dispense layout, operator access and room context.
4. Do not recreate accepted equipment from generic white/yellow cuboids.

## This image must visibly prove
1. At least one complete weigh station with feed/hopper/dispense relationship visible.
2. Multiple ingredient containers/bins visible.
3. The view matches V05 accepted functional identity.

## Camera
- Medium 3/4 functional view with primary function plus connected subcomponents.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
