# V10 IMAGE-SPEC 009 — Chemical Compound / Controlled Receiving — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/chemical_compound_controlled_receiving_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/chemical_compound_controlled_receiving_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 A shows tanks, drums and yellow pipes, but no IBCs, receiving dock/check area, controlled-access zone or convincing pump/transfer operation.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create a receiving dock/apron on one side of the facility with a clear truck-side transfer edge or dock door/threshold.
2. Provide a receiving/check station and a marked staging zone containing at least 6 drums plus 3 IBCs with visible cage frames.
3. Keep three bulk tanks in real bunded containment: continuous curb/wall around the tank group plus visible sump/drain low point.
4. Add at least two pump skids with motor + pump body + base + isolation valves.
5. Connect staged drums/IBCs and bulk tanks with visible flexible hose/hard-pipe transfer route, including elbows and valves that terminate at actual vessels.
6. Add a controlled-access partition/gate/door and safety/eyewash station. Maintain a clear operator aisle.

## This image must visibly prove

1. Receiving dock/check area, drums/IBCs, bunded bulk tanks and transfer equipment are visible together.
2. At least one visible path connects staging to pump/tank.
3. Controlled-access barrier/door is visible.

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
