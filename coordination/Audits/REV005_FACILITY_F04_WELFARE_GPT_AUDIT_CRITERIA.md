# REV005 FACILITY F04 — EMPLOYEE CHANGING / SHOWER / LOCKER SUPPORT — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex  
**Independent auditor:** GPT  
**Method:** deterministic historical replay + exact 59-object transfer

## Gate A — canonical baseline

Required pre-F04 hashes:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

Protected PASS facilities:
- F01 76 objects
- F02 79 objects
- F03 30 objects

Glass Deck V09 quarantine 117/117 must remain unchanged.

## Gate B — historical replay

Detached OS-temp worktree:
`420038365847de763d64c8583a9e31ac5a6bd677`

Initial Blend:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay V01→V02→V03→V04→V05 unchanged.

## Gate C — source composition

Original V05 objects_for() for the F04 group must return exactly:
- BASE 10
- V01 49
- V02/V03/V04/V05 0
- total 59

## Gate D — dimensional contract

All 49 V01 objects must match the exact locker/shower/zoning/bench coordinates and dimensions in:
`coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`

Tolerance <=0.001 m.

## Gate E — source A/B visual parity

Archived A:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

Archived B:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

Decoded visual pixel parity required. Raw metadata differences are acceptable.

## Gate F — exact destination transfer

Destination:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Exactly 59 accepted objects + dependencies.

Preserve source transforms, dimensions, materials, parents, accepted visibility.

Tolerances:
- location <=0.001 m
- rotation <=0.0001 rad
- scale <=0.0001
- dimensions <=0.001 m

## Gate G — destination A/B parity

900×600 historical Workbench parity renders with exact historical cameras.

Visual/pixel parity required.

## Gate H — prior PASS protection

F01 76/76 exact.
F02 79/79 exact.
F03 30/30 exact.

Any prior-PASS mutation => FAIL.

## Gate I — integrated collision preflight

Run 8 azimuths × 9-ray LOS.

Require:
- >=7/9 clear rays
- no camera-inside geometry
- no immediate architectural intersection within 1 m
- facility fully framed
- projected screen coverage 30–65%

No automatic hide/quarantine of another facility.

If no valid camera, STOP and report blockers.

## Gate J — QA images

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600

Visible cues:
- 5 locker banks / locker-door rhythm
- 4 shower cubicles
- shower heads and drains
- clean/dirty separation
- change bench
- coherent circulation

## Gate K — protection/scope

REV004 unchanged.
No REV006/.hiveai/tour/F05.
No TASKS/criteria edits.
Historical Glass Deck source and V09 quarantine unchanged.

## Gate L — stop

Stop:
`AWAITING_GPT_FACILITY_AUDIT_F04`

Do not begin F05.
