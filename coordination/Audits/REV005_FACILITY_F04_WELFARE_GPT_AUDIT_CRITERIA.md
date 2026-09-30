# REV005 FACILITY F04 — EMPLOYEE CHANGING / SHOWER / LOCKER SUPPORT — LOCKED GPT AUDIT CRITERIA V02

**Executor:** Codex  
**Independent auditor:** GPT  
**Method:** deterministic historical restoration + interior-contained integration proof

Codex MUST NOT edit this file.

## Gate A — canonical baseline

Required pre-F04 canonical hashes:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

The previous blocked attempt must not have changed them.

Protected PASS facilities:
- F01: 76
- F02: 79
- F03: 30

V09 Glass Deck quarantine:
- 117/117 unchanged

## Gate B — historical replay/source

Detached OS-temp replay at commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Required selected source:
- BASE 10
- V01 49
- total 59

Dimensional contract from:
`coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`

must pass <=0.001 m.

## Gate C — archived source visual identity

Historical A:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

Historical B:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

Decoded visual pixel parity required.

## Gate D — exact destination transfer

Destination:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Required count:
59.

Preserve source:
- world transforms
- dimensions
- materials
- parents
- accepted visibility

Tolerance:
- location <=0.001 m
- rotation <=0.0001 rad
- scale <=0.0001
- dimensions <=0.001 m

## Gate E — destination A/B parity

900×600 historical Workbench views:
- A camera (14,-88,13) -> (30,-70,3), 52 mm
- B camera (20,-78,8) -> (30,-70,3), 52 mm

Must visually reproduce archived F04 evidence.

## Gate F — prior PASS protection

Exact before/after protection:
- F01 76/76
- F02 79/79
- F03 30/30

Any mutation => FAIL.

## Gate G — historical pavilion containment proof

Current scene must contain historical:

`WELLNESS_PAVILION`

Expected bounds approximately:
- X 19 → 41
- Y -79 → -61
- Z 1.2 → 7.2

and:
`WELLNESS_GLASS`

Expected front bounds approximately:
- X 20 → 40
- Y -79.2 → -79.0
- Z 1.45 → 6.95

Record actual bounds.

Do not alter these objects.

The accepted 59-object F04 union must be spatially consistent with an interior support zone inside/within this pavilion.

## Gate H — interior integrated-camera search

Do NOT use the old exterior 8-azimuth ring as the final gate.

Search from inside the historical pavilion.

### Pavilion geometry

Let:
- PminX/PmaxX
- PminY/PmaxY
- PminZ/PmaxZ

come from actual `WELLNESS_PAVILION` world bounds.

Let accepted F04 union bounds be:
- Fmin/Fmax
- center Fc
- extent Fw/Fd/Fh

### Interior candidate XY grid

For inset values:
- **0.9 m**
- **1.8 m**
- **3.0 m**

Generate eight perimeter candidates per inset:

1. (PminX+s, PminY+s)
2. ((PminX+PmaxX)/2, PminY+s)
3. (PmaxX-s, PminY+s)
4. (PminX+s, (PminY+PmaxY)/2)
5. (PmaxX-s, (PminY+PmaxY)/2)
6. (PminX+s, PmaxY-s)
7. ((PminX+PmaxX)/2, PmaxY-s)
8. (PmaxX-s, PmaxY-s)

Total XY candidates:
24.

### Camera Z levels

Use two Z candidates:

Z1 =
`min(PmaxZ-0.80, max(FmaxZ+0.70, 4.80))`

Z2 =
`min(PmaxZ-0.45, max(FmaxZ+1.20, 5.40))`

Total positions before rejection:
48.

### Target

Primary target:
`(Fc.x, Fc.y, FminZ + 0.45*Fh)`

Also allow target Z offsets:
- primary
- primary + 0.35 m
- primary - 0.25 m

Target must remain within F04 vertical union.

### Lens order

Test:
1. 52 mm
2. 45 mm
3. 40 mm

Do not go below 40 mm.

### Camera collision rejection

Reject a candidate if:
- camera point is inside/within 0.30 m of any F04 equipment object;
- camera point is inside/within 0.25 m of any visible non-shell mesh;
- camera point is outside pavilion XY bounds;
- camera Z is <= PminZ+1.2 or >= PmaxZ-0.25.

The historical `WELLNESS_PAVILION` bounding volume itself is a legitimate containing shell and must NOT be rejected merely because the camera lies inside its overall AABB.

### 9-ray visibility gate

Use nine target samples across F04 union:
- center
- ±30% X
- ±30% Y
- four upper offset samples

A ray counts clear if:
- first hit is one of the 59 accepted F04 objects; OR
- no non-F04 object is hit before the target sample.

A ray is blocked if first hit before target is:
- another facility's equipment;
- a pavilion wall/shell surface;
- a V09 replacement object;
- any unrelated mesh.

Require:
**>=7/9 clear rays**

No automatic quarantine/hide/exclusion is allowed.

### Framing

Projected F04 union must:
- fit entirely inside 4%–96% width
- fit entirely inside 5%–95% height
- occupy **35%–78%** of image area

This wider range is intentional for an interior room.

### Context requirement

The final integrated frame must visibly retain interior context. At least one of the following must be visually present around F04:
- pavilion wall/glazing edge
- pavilion floor/room boundary
- ceiling/upper room edge
- doorway/entry relation
- adjacent legitimate wellness interior context

GPT will decide this visually.

## Gate I — no neighbor mutation

Do NOT:
- quarantine Wellness
- quarantine Training
- quarantine Restaurant
- move pavilion shell
- hide neighboring facility collections in the canonical scene
- save QA-only visibility changes

If no interior candidate reaches Gate H:
STOP:
`BLOCKED_F04_INTERIOR_CAMERA_NO_VALID_VIEW`

Return blocker objects. Do not mutate them.

## Gate J — final QA

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- D_INTERIOR_INTEGRATED_CONTEXT 1440×960
- D preview 900×600 same camera/state

F04 visual identity must show:
- locker banks/doors
- shower cubicles
- shower heads/drains
- clean/dirty separation
- change bench
- circulation

## Gate K — scope/source protection

REV004 unchanged.
No REV006.
No .hiveai.
No tour.
No F05.
No TASKS edit.
No criteria edit.
Historical pavilion unchanged.
V09 Glass Deck quarantine unchanged.

## Gate L — stop

Stop exactly:
`AWAITING_GPT_FACILITY_AUDIT_F04`

Do not begin F05.
