# REV005 F08 Bottle Blow Molding — Independent GPT Visual Audit of M08.42

## Verdict

`REMEDIATION_REQUIRED_R01_CAMERA_CONTRACT`

Audited evidence publication commit:

`0960465b3ecc22a3f500aac2cc0d628f46f8530b`

Canonical Blend/GLB remain unchanged and F09 remains blocked.

## Accepted staged technical gates

The following M08.42 staged gates are accepted for R01 unless a new contradiction is found:

- F08 legacy ownership inventory: 391 confirmed F08 legacy, 0 ambiguous, 5 non-F08 preserved.
- Protection diff: PASS, 2,331 protected objects, zero unauthorized differences.
- Dimensional validation: PASS.
- Cross-facility collisions: 0.
- New F08 staged geometry remains inside the locked facility envelope.
- South operator aisle: clear.
- North service aisle: clear.
- Hopper/feed preforms: 20.
- Heater elements: 16 total, 8 per bank.
- Blow-cell service doors: 2.
- High-pressure-air branches: 4.
- Formed-bottle outfeed: 16 bottles.
- Deterministic candidate GLB membership parity: PASS.
- Candidate GLB expected nodes = actual nodes = 10,888.
- Missing expected names = 0.
- Unexpected names = 0.
- Accepted F01-F07 baseline names preserved.
- New F08 names present.
- Exact retired F08 legacy names absent.

These technical results do not authorize canonical promotion until visual acceptance passes.

## Direct visual findings

### A_CONTEXT — FAIL

`F08_A_CONTEXT_PREVIEW_900x600.png`

The frame is dominated by an opaque wall/black field. The required complete preform-to-bottle process is not visible.

This is a camera-placement failure, not proof of missing process geometry.

### B_FUNCTIONAL — PARTIAL / NOT ACCEPTED

`F08_B_FUNCTIONAL_PREVIEW_900x600.png`

Direct review confirms visible process geometry:
- repeated orange heater elements;
- oven/transfer framing;
- guarded mould/blow-cell structure;
- downstream conveyor/outfeed context.

However the functional sequence is not yet composed clearly enough as one readable heater → transfer → blow-cell → bottle-outfeed chain.

### C_SEQUENCE_DETAIL — PARTIAL / NOT ACCEPTED

`F08_C_SEQUENCE_DETAIL_PREVIEW_900x600.png`

Direct review confirms:
- two distinct mould/clamp stations;
- visible stretch/blow rod cues;
- guard structure;
- downstream bottle conveyor with formed bottles.

The frame is useful evidence that the blow-cell/outfeed geometry exists.

But the heater-to-cell connection is mostly outside/at the edge of the frame, so it does not satisfy the sequence-detail contract.

### D_INTEGRATED — PARTIAL / NOT ACCEPTED

`F08_D_INTEGRATED_PREVIEW_900x600.png`

The long process line is visible and the staged room/enclosure is readable.

However the oblique north-side composition does not make the full west→east process sequence unambiguous:
- hopper/feed is not clearly established;
- outfeed is pushed to the edge;
- heater/cell ordering is visually compressed.

## Root cause

The M08.42 prompt constrained camera refinement to approximately ±3 m around four seed positions.

That constraint is now superseded for F08 R01.

The room and process geometry are much longer than the original evidence angles comfortably cover. A side-on/south-aisle camera family is required.

The decisive visual task is not to redesign the machinery. It is to find camera positions from which the already-built staged geometry proves the process sequence label-blind.

## R01 authorization

R01 is camera/evidence-first.

No geometry mutation is authorized unless the expanded camera search proves a specific geometric contradiction.

R01 may:
- deterministically reproduce the exact staged F08 build if needed from the published helpers;
- use the existing ignored local `F08_STAGED.blend` only if its staged manifest/signatures match the published M08.42 evidence;
- search camera positions anywhere inside the locked F08 room envelope or immediately outside glazed/open wall areas, provided the camera is outside object geometry;
- use lenses from 16–35 mm;
- use side-on and south/operator-aisle views not limited by the original ±3 m seed rule.

## Preferred search families

Highest-priority family: south-side / side-on process elevation.

Examples to test, not hard-coded final answers:

- camera around (52,0…4,5…7), target around (52,10,2.8…3.2), lens 16–24 mm;
- camera around (44…48,1…5,5…7), target around (54…58,10,2.8…3.2), lens 18–28 mm;
- camera around (58…62,1…5,5…7), target around (54…58,10,2.8…3.2), lens 18–28 mm;
- west-to-east oblique from south aisle around (36…42,2…5,5…7), target around (55…60,10,3), lens 16–24 mm.

The search should also include focused B/C camera families once a valid complete A/D orientation is found.

## Promotion rule

Do not save the staged model into the canonical Blend and do not replace the canonical GLB merely because camera candidates improve.

Canonical promotion is allowed only after:
1. A/B/C/D visual gates all pass from the exact staged state;
2. staged geometry/signatures still match the accepted M08.42 technical evidence;
3. protection remains clean;
4. deterministic GLB membership parity remains exact.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R01`
