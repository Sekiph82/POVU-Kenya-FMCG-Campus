# V10 IMAGE-SPEC 045 — Production Hall / Wet Processing / Process Core — C_SEQUENCE_OR_DETAIL

## Locked source image
`output/rev005-interior-remediation-v09/qa/production_hall_wet_processing_process_core_C_SEQUENCE_OR_DETAIL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/production_hall_wet_processing_process_core_C_SEQUENCE_OR_DETAIL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure
V09 C is a closer tank/header view without useful process connection detail.

## Required Blender correction
Replace V09 generic final-visible geometry as required below. Do not stack another proxy layer.

1. Keep the current tank locations only if useful, but rebuild each as a true process vessel with top-mounted agitator motor/gearbox, shaft/lid/nozzle cues and bottom/side outlets.
2. Add elevated access platform segments around at least three vessels, with stairs and handrails sized to people.
3. Build a low-level pump/manifold corridor: at least four pump skids, branch valves and connected inlet/outlet piping to individual tanks.
4. Add a dedicated CIP skid with CIP tank, supply header, return header, valves and connection to at least two process vessels.
5. Show downstream transfer direction toward filling via product header/transfer line; use stainless/steel and POVU accents rather than identical generic tanks.

## This image must visibly prove
1. Tank outlet/nozzle → pump/valve manifold → transfer/CIP branch visible in one frame.
2. Human-scale platform/handrail visible for scale.
3. No unconnected floating pipe.

## Camera
- Medium 3/4 functional view with primary role plus connected subcomponents.
- Close oblique sequence/detail view with at least two connected operational steps.
- Camera outside all visible geometry; no clipping/occlusion.
- Do not use camera angle to conceal missing zones.

## Acceptance
PASS only if the V09 failure is gone, label-blind role is clear, required content is visible, V10 global contract is met, and render is >=1280×800, non-black and correctly exposed. Codex may mark only READY_FOR_GPT_REVIEW.
