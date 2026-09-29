# V10 IMAGE-SPEC 013 — Daycare / Crèche — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/daycare_cr_che_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/daycare_cr_che_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B is only a closer view of the same sparse divider/chair arrangement and does not resemble the accepted V05 daycare.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Daycare/Crèche facility from commit 420038365847de763d64c8583a9e31ac5a6bd677, preserving world transforms/material dependencies.
2. Remove only the broken V09 daycare result.
3. Preserve V05 child-scale activity/play, nap/rest, storage and partition zoning.
4. Do not simplify or replace restored geometry with V09 helper primitives.

## This image must visibly prove

1. Child-scale tables/seating/play or nap furniture are clearly visible.
2. Storage/partition zoning is visible.
3. The restored V05 room reads as daycare at human/child scale.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
