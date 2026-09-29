# V10 IMAGE-SPEC 010 — Chemical Compound / Controlled Receiving — B_FUNCTIONAL

## Locked source image
`output/rev005-interior-remediation-v09/qa/chemical_compound_controlled_receiving_B_FUNCTIONAL.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/chemical_compound_controlled_receiving_B_FUNCTIONAL.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 B is mainly a closer tank view. Pump skid, IBC cage, valves/hoses and receiving operation are not readable.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Create a receiving dock/apron on one side of the facility with a clear truck-side transfer edge or dock door/threshold.
2. Provide a receiving/check station and a marked staging zone containing at least 6 drums plus 3 IBCs with visible cage frames.
3. Keep three bulk tanks in real bunded containment: continuous curb/wall around the tank group plus visible sump/drain low point.
4. Add at least two pump skids with motor + pump body + base + isolation valves.
5. Connect staged drums/IBCs and bulk tanks with visible flexible hose/hard-pipe transfer route, including elbows and valves that terminate at actual vessels.
6. Add a controlled-access partition/gate/door and safety/eyewash station. Maintain a clear operator aisle.

## This image must visibly prove

1. One IBC cage and multiple drums are visible beside a real pump skid.
2. At least two valves and a hose/pipe connection are visible between staging and tank system.
3. Tank bund curb and access aisle remain visible.

## Camera requirement

- Use a medium 3/4 functional camera showing the primary equipment/function plus connected subcomponents.
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
