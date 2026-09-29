# V10 IMAGE-SPEC 022 — Finished Goods Warehouse / Dispatch — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/finished_goods_warehouse_dispatch_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/finished_goods_warehouse_dispatch_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B is mainly racks and the long yellow element; no dispatch/control/loading function is readable.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create role-specific finished-goods storage plus outbound dispatch flow: finished pallet racks → consolidation/staging lanes → dispatch control → loading dock/door.
2. Populate racks with finished-case pallets; create at least two marked floor staging lanes with grouped outbound pallets.
3. Add a real dispatch desk/control station with monitor and one consolidation/check point.
4. Build a loading edge with at least two dock/door openings or one clear dock leveller/door relationship.
5. Include one forklift/AMR in a secondary position and clear handling aisles.
6. Provide warehouse envelope cues: walls/roof/lighting and loading-side openings.

## This image must visibly prove

1. Dispatch desk/check point and grouped outbound pallets are visible.
2. A loading opening/dock relationship is visible in the same functional scene.
3. At least one handling vehicle/AMR appears in context.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
