# V10 IMAGE-SPEC 023 — Finished Goods Warehouse / Dispatch — C_SEQUENCE_OR_DETAIL

## Locked source image
`output/rev005-interior-remediation-v09/qa/finished_goods_warehouse_dispatch_C_SEQUENCE_OR_DETAIL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/finished_goods_warehouse_dispatch_C_SEQUENCE_OR_DETAIL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 C remains a rack/conveyor close-up. It does not prove storage → consolidation → dispatch/loading sequence.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create role-specific finished-goods storage plus outbound dispatch flow: finished pallet racks → consolidation/staging lanes → dispatch control → loading dock/door.
2. Populate racks with finished-case pallets; create at least two marked floor staging lanes with grouped outbound pallets.
3. Add a real dispatch desk/control station with monitor and one consolidation/check point.
4. Build a loading edge with at least two dock/door openings or one clear dock leveller/door relationship.
5. Include one forklift/AMR in a secondary position and clear handling aisles.
6. Provide warehouse envelope cues: walls/roof/lighting and loading-side openings.

## This image must visibly prove

1. Rack pick face → staging pallet group → loading/dock direction visible in one oblique frame.
2. Floor lanes/markers show outbound flow.
3. The close view includes dispatch/loading context, not racks alone.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
- Use a close oblique sequence camera showing at least two adjacent process steps and their physical connection.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
