# V10 IMAGE-SPEC 019 — ETP / Water Treatment — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/etp_water_treatment_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/etp_water_treatment_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B remains a closer view of similar tanks; there is no clear aeration/clarification/filtration identity.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create a clearly differentiated treatment train: influent/equalisation → aeration/biological treatment → clarification → filtration → treated discharge/sludge handling.
2. Equalisation: open/covered basin with inlet pipe and level/overflow cue; aeration: basin/tank with visible air grid/diffuser/header; clarification: circular clarifier with central feed/bridge or scraper-arm cue.
3. Filtration: at least two vertical filter vessels or a skid with inlet/outlet manifold; sludge: dedicated sludge tank/pump or dewatering cue.
4. Connect each stage with visible pipes, elbows and at least three pump skids. Pipes must visibly terminate at stage inlets/outlets.
5. Add operator walkway, stairs and handrails around at least two stages; maintain service access and use process-specific materials.

## This image must visibly prove

1. One biological/aeration stage plus one clarification or filtration stage are visible with their actual process-specific geometry.
2. A pump/manifold physically connects the stages.
3. No two adjacent stages read as the same generic tank copied twice.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
- Camera origin must be outside all visible geometry and must not intersect a wall/equipment shell.
- Do not hide missing geometry with a flattering angle.

## Acceptance

PASS only if the V09 failure is gone, the function is label-blind readable, required content is visibly present, and the global V10 contract is met. Render must be at least 1280×800, non-black and correctly exposed. Codex may mark only **READY_FOR_GPT_REVIEW**.
