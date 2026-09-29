# V10 IMAGE-SPEC 008 — Caps and Trigger Assembly — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B is only a closer view of the same single white block; none of the accepted V05 functional assembly equipment is present.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Caps/Trigger facility from the V05 Blend at commit 420038365847de763d64c8583a9e31ac5a6bd677, preserving its world transforms/material dependencies.
2. Remove the V09 broken sparse replacement for this facility only.
3. Verify the restored cell includes the accepted bowl/feed logic, fixtures/work positions and assembly equipment seen in V05 audit evidence.
4. After append, render immediately and compare visually against V05 evidence before changing camera.

## This image must visibly prove

1. Close/medium view shows feed/bowl, fixtures and multiple assembly work positions from the restored V05 geometry.
2. No empty-slab framing.
3. Camera proves the accepted V05 functional identity.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
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
