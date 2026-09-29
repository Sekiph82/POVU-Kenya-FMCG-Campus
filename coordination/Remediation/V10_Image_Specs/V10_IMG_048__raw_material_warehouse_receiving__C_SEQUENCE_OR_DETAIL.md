# V10 IMAGE-SPEC 048 — Raw Material Warehouse / Receiving — C_SEQUENCE_OR_DETAIL

## Locked source image
`output/rev005-interior-remediation-v09/qa/raw_material_warehouse_receiving_C_SEQUENCE_OR_DETAIL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/raw_material_warehouse_receiving_C_SEQUENCE_OR_DETAIL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 C remains a rack close-up and does not show inbound dock → inspection/quarantine → storage sequence.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a warehouse shell with receiving dock/door, roof/wall/lighting cues and clear material-handling aisles.
2. Receiving: dock edge/door plus inspection/check desk and marked quarantine/staging bay.
3. Raw inventory must be mixed: pallet sacks/cartons, at least 6 drums and at least 3 IBCs with cage frames, rather than only identical orange boxes.
4. Storage racks must hold mixed raw containers; separate quarantine/staging from released storage.
5. Add one forklift/AMR in context and floor markings showing inbound movement from dock to inspection/quarantine to storage.

## This image must visibly prove
1. Dock/inbound edge → inspection/quarantine → storage aisle visible in one oblique frame.
2. At least one drum and one IBC visible.
3. Floor markings or aisle alignment visibly indicate inbound flow.

## Camera
- Medium 3/4 functional view with primary role plus connected subcomponents.
- Close oblique sequence/detail view with at least two connected operational steps.
- Camera outside all visible geometry; no clipping/occlusion.
- Do not use camera angle to conceal missing zones.

## Acceptance
PASS only if the V09 failure is gone, label-blind role is clear, required content is visible, V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
