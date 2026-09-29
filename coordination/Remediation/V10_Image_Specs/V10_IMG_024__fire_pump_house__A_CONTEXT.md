# V10 IMAGE-SPEC 024 — Fire Pump House — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/fire_pump_house_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/fire_pump_house_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A is almost empty; only two tiny red blocks are visible in the distance. The accepted V05 fire-pump installation is gone.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Fire Pump House from commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove the V09 near-empty result.
3. Preserve paired pump sets, motors, suction/discharge headers, manifold, valves and room/house context.
4. Do not rebuild fire pumps as tiny colored blocks.

## This image must visibly prove

1. Complete paired pump sets and manifold/header visible.
2. Room/house context and service aisle visible.
3. The facility reads immediately as a fire-pump installation.

## Camera requirement

- Use a 3/4 cutaway context camera showing the complete room/line and its envelope/flow.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
