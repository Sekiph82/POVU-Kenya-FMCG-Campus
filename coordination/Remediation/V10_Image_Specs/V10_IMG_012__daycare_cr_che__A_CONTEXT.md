# V10 IMAGE-SPEC 012 — Daycare / Crèche — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/daycare_cr_che_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/daycare_cr_che_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A lost the accepted daycare and shows repeated simple chairs/blocks separated by a large divider.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Daycare/Crèche facility from the V05 Blend at commit 420038365847de763d64c8583a9e31ac5a6bd677.
2. Remove only the broken V09 daycare replacement/restore result.
3. Preserve V05 child-scale activity/nap/storage zoning, room partitions, furniture and materials.
4. After append, render and compare directly to V05 accepted evidence; do not simplify the restored geometry.

## This image must visibly prove

1. The complete V05 child-scale room zoning is restored and visible.
2. Activity/play, nap/rest and storage/furniture cues are visible together.
3. The image reads unmistakably as daycare without labels.

## Camera requirement

- Use a 3/4 cutaway context camera showing the complete room/line and its envelope/flow.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Keep verticals readable and use perspective, not a flat orthographic proof.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if:
- the exact V09 failure above is gone;
- the function is label-blind readable;
- required content is actually visible, not merely present by object name;
- the image satisfies the global V10 contract;
- no unrelated V05/V09 legacy geometry is reintroduced;
- render is at least 1280×800, non-black and correctly exposed.

Codex may mark only **READY_FOR_GPT_REVIEW**, never independent PASS.
