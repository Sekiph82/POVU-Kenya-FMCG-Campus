# V10 IMAGE-SPEC 035 — Occupational Health / First Aid — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/occupational_health_first_aid_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/occupational_health_first_aid_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B focuses on the divider and bed area but still lacks convincing clinical support equipment and room completion.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a finished clinic shell: floor, rear + side walls, ceiling, doorway, neutral clinical lighting and one internal privacy partition/curtain track.
2. Entry/waiting: reception/check desk plus 4 visitor chairs.
3. Treatment: full exam bed with mattress/head support, bedside/treatment trolley with shelves/drawers and one monitor/stand.
4. Clinical support: sink/basin with counter, wall/under-counter cabinets, supply shelf and medical storage.
5. Use light clinical finishes, privacy curtain and clear circulation between waiting and treatment.

## This image must visibly prove
1. Exam bed + treatment trolley + monitor/stand visible.
2. Sink/cabinet/support storage visible nearby.
3. Privacy partition/curtain is functional, not a giant blocking wall.

## Camera
- Medium 3/4 functional view with primary function plus connected subcomponents.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
