# V10 IMAGE-SPEC 007 — Caps and Trigger Assembly — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/caps_and_trigger_assembly_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/caps_and_trigger_assembly_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A contains only a small white block and a yellow/red post on a nearly empty slab. The independently accepted V05 assembly cell is gone.

## Required Blender correction

This is one of the six facilities independently accepted in V05. **Do not reconstruct it from V09 primitives.** Restore the complete accepted facility from V05 commit `420038365847de763d64c8583a9e31ac5a6bd677` using the exact-history restoration method in the global contract.

1. Restore the complete accepted V05 Caps/Trigger facility from the V05 Blend at commit 420038365847de763d64c8583a9e31ac5a6bd677, preserving its world transforms/material dependencies.
2. Remove the V09 broken sparse replacement for this facility only.
3. Verify the restored cell includes the accepted bowl/feed logic, fixtures/work positions and assembly equipment seen in V05 audit evidence.
4. After append, render immediately and compare visually against V05 evidence before changing camera.

## This image must visibly prove

1. The complete V05 assembly cell occupies most of frame.
2. Multiple work positions, feed/bowl/fixture logic and assembly equipment are visible.
3. The image is recognisably Caps/Trigger Assembly without labels.

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
