# V10 IMAGE-SPEC 038 — Packaging Warehouse — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/packaging_warehouse_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/packaging_warehouse_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 B shows racks and film rolls but still lacks inspection, issue desk, marked staging and production-side opening.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Build a warehouse shell with wall/roof/lighting cues and two operational edges: receiving/staging and issue-to-production.
2. Packaging-specific inventory: palletized cartons, at least 8 large film rolls, closure/label/bin storage and empty-container packaging where appropriate.
3. Receiving/staging: floor-marked inbound bay, inspection/check desk and temporary staging pallets.
4. Issue-to-production: dedicated marked lane or conveyor, issue desk and clear opening/door toward production.
5. Maintain rack aisles and add one forklift/AMR parked/turning in context; do not place it as the main subject.

## This image must visibly prove
1. Film/carton/label inventory visibly packaging-specific.
2. Issue desk/marked lane or conveyor visible.
3. At least one receiving/staging cue visible beyond the functional foreground.

## Camera
- Medium 3/4 functional view with primary role plus connected subcomponents.
- Camera outside all visible geometry; no clipping/occlusion.
- Do not use camera angle to conceal missing zones.

## Acceptance
PASS only if the V09 failure is gone, label-blind role is clear, required content is visible, V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
