# REV005 FACILITY F05 — FIRE PUMP HOUSE — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex
**Independent auditor:** GPT

## Gate A — baseline

Required canonical pre-F05 hashes:

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

Protected PASS:
- F01 76
- F02 79
- F03 30
- F04 59

Protected quarantine state:
- V09 Glass Deck: 117
- V09 Training Academy: 81
- V09 Restaurant right wall: quarantined

## Gate B — historical replay and 123-object truth

Replay V01→V05 in detached OS-temp worktree from:
`420038365847de763d64c8583a9e31ac5a6bd677`

Initial source Blend:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Original V05 objects_for("Fire pump house") must return exactly:
**123**

Contribution accounting:
- BASE 10
- V01 15
- V02 0
- V03 0
- V04 44
- V05 54

## Gate C — spatial provenance split

Split the 123 selected objects by object world-bounds center Y.

Primary:
-20 <= centerY <= +10

Expected:
**54**

Composition:
- BASE 5
- V01 0
- V04 22
- V05 27

Secondary:
55 <= centerY <= 85

Expected:
**69**

Composition:
- BASE 5
- V01 15
- V04 22
- V05 27

No object may fall outside both windows.

If split differs:
STOP before canonical mutation.

Only the 54-object PRIMARY cluster is authorized for F05 canonical restore.

## Gate D — primary dimensional contract

Verify the V04/V05 exact coordinates and dimensions recorded in:
`coordination/Audits/REV005_F05_FIRE_PUMP_HISTORICAL_SOURCE_PROVENANCE.md`

Tolerance:
<=0.001 m / component.

BASE 5 objects are replay-authoritative and must preserve exact replay transforms/dimensions.

## Gate E — archived source visual parity

Run the original historical V05 renderer on the replayed scene.

A/B/C archived hashes:
- A `5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`
- B `D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`
- C `AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

Decoded-pixel parity required.

## Gate F — exact primary destination restore

Destination:
`REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`

Append exactly:
**54 primary objects**

Do NOT append the 69-object secondary historical cluster.

Preserve:
- mesh/data
- matrix_world
- dimensions
- materials
- parents
- accepted visibility

## Gate G — destination historical parity

For parity rendering, temporarily reproduce exact historical V05 `show_only()` behavior.

Render A/B/C at 900×600 with historical cameras.

The primary destination views must visually reproduce archived A/B/C.

No saved visibility changes.

## Gate H — prior PASS protection

Exact before/after:
- F01 76
- F02 79
- F03 30
- F04 59

X01 quarantine states unchanged.

## Gate I — integrated evidence

Integrated camera target is the primary accepted cluster near:
`(94,-5,3)`

Do NOT calculate framing bounds across the un-restored secondary historical cluster.

Search current scene around primary cluster only.

Require:
- >=7/9 clear rays
- no automatic hide/quarantine
- pumps/manifolds/valves/panel recognizable
- legitimate local building/campus context visible

No hard projected-area percentage is required before GPT visual review.

If no valid view:
STOP and report blockers without altering them.

## Gate J — final evidence

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- C_PROCESS_DETAIL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600

## Gate K — scope

- REV004 unchanged
- no REV006
- no .hiveai
- no tour
- no F06
- no TASKS edit by Codex
- secondary 69-object historical cluster not restored

## Stop

Success:
`AWAITING_GPT_FACILITY_AUDIT_F05`

Do not begin F06.
