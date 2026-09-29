# V10 IMAGE-SPEC 026 — Glass Deck Command / Training / Café Gallery — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/glass_deck_central_command_training_caf_gallery_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/glass_deck_central_command_training_caf_gallery_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 A is mostly conference tables and black screens on an open slab. Command operations, café/gallery and a premium glazed interior are not present.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Create a complete premium cutaway shell with glass framing, floor, side/rear enclosure, ceiling/soffit and lighting; the camera-facing glass/wall may be QA-hidden only.
2. Command zone: minimum 4 operator consoles with monitors/chairs facing a multi-screen command wall of at least 4 displays; include equipment/storage strip.
3. Training zone: one presentation screen, 2 collaboration tables and at least 8 chairs with clear circulation.
4. Café/gallery zone: 4–6 m service counter, backbar/shelving, beverage machine silhouettes, display/gallery wall and 6–8 customer seats.
5. Use floor/ceiling/material changes to zone functions while keeping one coherent interior; glazing frames and premium finishes must be visible.

## This image must visibly prove
1. Command, training and café/gallery zones all visible at once.
2. Finished glazed/ceiling envelope and premium interior treatment visible.
3. Each zone can be identified without text.

## Camera
- 3/4 cutaway context, complete room/line and envelope visible.
- Camera outside all visible geometry, no clipping/occlusion.
- Perspective only; do not use angle choice to hide missing geometry.

## Acceptance
PASS only if the exact V09 failure is gone, required content is visible label-blind, the V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
