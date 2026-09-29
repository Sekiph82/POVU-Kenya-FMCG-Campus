# V10 IMAGE-SPEC 011 — Chemical Compound / Controlled Receiving — C_SEQUENCE_OR_DETAIL

## Locked source image
`output/rev005-interior-remediation-v09/qa/chemical_compound_controlled_receiving_C_SEQUENCE_OR_DETAIL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/chemical_compound_controlled_receiving_C_SEQUENCE_OR_DETAIL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 C shows tank tops, a pipe and drums but still does not demonstrate controlled receiving-to-transfer sequence.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create a receiving dock/apron on one side of the facility with a clear truck-side transfer edge or dock door/threshold.
2. Provide a receiving/check station and a marked staging zone containing at least 6 drums plus 3 IBCs with visible cage frames.
3. Keep three bulk tanks in real bunded containment: continuous curb/wall around the tank group plus visible sump/drain low point.
4. Add at least two pump skids with motor + pump body + base + isolation valves.
5. Connect staged drums/IBCs and bulk tanks with visible flexible hose/hard-pipe transfer route, including elbows and valves that terminate at actual vessels.
6. Add a controlled-access partition/gate/door and safety/eyewash station. Maintain a clear operator aisle.

## This image must visibly prove

1. Frame stages: drum/IBC staging → pump/valve point → tank connection.
2. All three steps are physically connected in the image.
3. No tank shell blocks the transfer path.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
- Use a close oblique sequence camera showing at least two adjacent process steps and their physical connection.
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
