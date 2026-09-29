# V10 IMAGE-SPEC 001 — Administration / HQ / R&D / QC — A_CONTEXT

## Locked source image
`output/rev005-interior-remediation-v09/qa/administration_hq_r_d_qc_A_CONTEXT.png`

Independent V09 verdict: **NOT OK**

Required V10 output:
`output/rev005-interior-remediation-v10/qa/administration_hq_r_d_qc_A_CONTEXT.png`

Read first:
`coordination/Remediation/V10_GLOBAL_BLENDER_MODELING_CONTRACT.md`

## Exact V09 visual failure

V09 shows office desks and a small lab bench on a dark open slab. Reception, meeting room, finished enclosure and true QC/R&D zoning are not visible.

## Required Blender correction

Work in the current REV005 facility location, but replace V09 generic final-visible geometry as required below. Do not stack another generic proxy layer.

1. Build a finished office/lab cutaway shell around the current facility bounds: finished floor, rear + two side walls, ceiling/soffit, at least two door openings and neutral ceiling lighting.
2. Reception zone: one 3.0–3.6 m reception desk, two operator monitors, two task chairs and 4–6 visitor seats.
3. Office zone: minimum 8 real workstations, each with 1.4–1.8 m desk, pedestal/legs, monitor, keyboard plane and task chair; arrange into two logical rows with circulation.
4. Meeting zone: one 4.0×1.4 m table, 8–10 chairs and one presentation screen/board.
5. QC/R&D lab: minimum three 2.5–3.0 m benches with under-bench cabinets, one sink/service point, upper storage/shelves and at least six distinct instrument silhouettes; separate lab with a glazed/solid partition and door.
6. Use off-white walls, medium gray epoxy floor, wood/white office furniture, stainless/white lab furniture and restrained POVU teal accents.

## This image must visibly prove

1. Reception, office workstations, meeting area and lab are all visible in one coherent finished interior.
2. At least rear wall + both side walls + ceiling/soffit and a real doorway are visible.
3. The lab reads differently from the office without labels.

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
