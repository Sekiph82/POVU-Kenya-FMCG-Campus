# V10 IMAGE-SPEC 016 — Employee Changing / Shower / Locker Support — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/employee_changing_shower_locker_support_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/employee_changing_shower_locker_support_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A shows a long gray partition, several tall gray cuboids and white blocks. Lockers, benches, showers and changing-room logic are gone.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Employee Changing / Shower / Locker facility from commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove the V09 generic cuboid/partition substitute.
3. Preserve accepted locker banks, benches, shower cubicles/partitions, changing circulation and room context.
4. Do not rebuild lockers/showers as plain vertical boxes.

## This image must visibly prove

1. Locker banks, changing benches and shower/cubicle partitions visible together.
2. Finished room context/circulation visible.
3. The facility is unmistakably changing/shower support.

## Camera requirement

- Use a 3/4 cutaway context camera showing the complete room/line and its envelope/flow.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
