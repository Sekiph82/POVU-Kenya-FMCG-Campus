# REV005 F05 — FIRE PUMP HOUSE — LOCKED GPT AUDIT CRITERIA

## Baseline

Canonical pre-F05 hashes:

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

## Historical source gate

Detached replay V01→V05 must resolve:
- total Fire Pump House selection = 123
- PRIMARY Y<30 = 54
- SECONDARY Y>=30 = 69

Contribution truth:
- BASE 10
- V01 15
- V04 44
- V05 54

Primary contribution:
- BASE 5
- V04 22
- V05 27
- total 54

Secondary contribution:
- BASE 5
- V01 15
- V04 22
- V05 27
- total 69

Any mismatch => STOP before canonical mutation.

## Primary-only restoration

Append exactly 54 PRIMARY objects into:

`REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`

Do not append or mutate the 69 SECONDARY source objects.

## Dimensional gate

V04/V05 primary objects must match the explicit numeric contract in:
`coordination/Audits/REV005_F05_FIRE_PUMP_HISTORICAL_SOURCE_PROVENANCE.md`

Tolerance:
- centers/dimensions <=0.001 m
- pipe endpoints <=0.001 m
- rotation <=0.0001 rad

## Historical parity

Reproduce exact historical V05 `show_only()` semantics.

Required A/B/C references:
- A `5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`
- B `D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`
- C `AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

Structural visual parity is mandatory.
Sparse antialias-only edge differences may be reported for independent GPT review.

## Protection

Exact before/after protection required for:
- F01 76
- F02 79
- F03 30
- F04 59
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- V09 Restaurant right-wall quarantine
- historical Glass Deck source
- historical Wellness/pavilion protected state

## Integrated evidence

Do not use a rigid projected-area percentage gate.

Search historical A/B/C camera positions first, then nearby alternatives if needed.

Requirements:
- PRIMARY 54-object facility clearly visible
- camera not inside equipment
- >=7/9 LOS rays to primary facility samples
- no QA-only hiding/quarantine
- no neighbor mutation
- legitimate current context visible
- paired pumps, piping/valves and panel readable

If no valid integrated camera exists:
STOP `BLOCKED_F05_INTEGRATED_COLLISION`
and report exact blockers without changing them.

## Final QA

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- C_PROCESS_OR_DETAIL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600

## Scope

No F06.
No REV004 change.
No REV006.
No .hiveai.
No tour/video.
No TASKS or criteria edit by Codex.

## Stop

Success:
`AWAITING_GPT_FACILITY_AUDIT_F05`
