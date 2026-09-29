# V10 IMAGE-SPEC 005 — Bottle Blow Molding — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/bottle_blow_molding_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/bottle_blow_molding_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B moves closer but still shows colored housings rather than recognizable heater and mould/blow machinery.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create one physical left-to-right line: preform hopper/unscrambler → preform feed rail → infrared heater/oven → guarded blow/mould cell → bottle outfeed conveyor.
2. Preform hopper: tapered bin/bowl plus feed chute; place at least 12 small repeated preform meshes on the rail.
3. Heater: 4–6 m tunnel/frame with two rows of at least eight vertical heater elements and the preform rail visibly passing through it.
4. Blow cell: rigid frame, transparent/mesh guards, two readable mould halves/clamp region, service doors and compressed-air manifold/hoses.
5. Outfeed: conveyor with at least eight formed bottle meshes so input/output transformation is visually obvious.
6. Add one operator HMI/control pedestal beside the line and a service aisle; do not use one colored cuboid as a complete machine.

## This image must visibly prove

1. Heater elements and preform track are readable.
2. Mould/clamp/blow cell structure and air connection are readable.
3. Preforms visibly enter the cell path and formed bottles visibly leave it.

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
