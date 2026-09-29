# V10 IMAGE-SPEC 018 — ETP / Water Treatment — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/etp_water_treatment_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/etp_water_treatment_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A is a row of nearly identical cylindrical tanks with turquoise pipes and small generic pumps. Distinct treatment stages are not label-blind readable.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create a clearly differentiated treatment train: influent/equalisation → aeration/biological treatment → clarification → filtration → treated discharge/sludge handling.
2. Equalisation: open/covered basin with inlet pipe and level/overflow cue; aeration: basin/tank with visible air grid/diffuser/header; clarification: circular clarifier with central feed/bridge or scraper-arm cue.
3. Filtration: at least two vertical filter vessels or a skid with inlet/outlet manifold; sludge: dedicated sludge tank/pump or dewatering cue.
4. Connect each stage with visible pipes, elbows and at least three pump skids. Pipes must visibly terminate at stage inlets/outlets.
5. Add operator walkway, stairs and handrails around at least two stages; maintain service access and use process-specific materials.

## This image must visibly prove

1. At least four visually different treatment stages appear in sequence.
2. Clarifier/filter/sludge handling are distinguishable from generic tanks.
3. Walkway/handrail/service access is visible.

## Camera requirement

- Use a 3/4 cutaway context camera showing the complete room/line and its envelope/flow.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
