# REV005 FACILITY F03 — ELECTRICAL / LV-MV ROOM — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex  
**Independent auditor:** GPT  
**Method:** deterministic historical replay + exact 30-object transfer

Codex MUST NOT edit this file.

## Gate A — current accepted baseline

Canonical baseline after F02:

Blend SHA-256:
`E935539393BBF83173004E7BBA97A5432818C355752ABAA55A88F685C707A0E8`

GLB SHA-256:
`2F593CC82ED68499B5F23C64495229CFEB482C0C44C64F341938802B4A68C277`

Protected accepted facilities:
- F01 Caps & Trigger: 76 objects
- F02 Daycare / Crèche: 79 objects

The 117-object V09 Glass Deck replacement quarantine must remain intact.

## Gate B — detached historical replay

Create detached system-temp worktree at:

`420038365847de763d64c8583a9e31ac5a6bd677`

Initial temp Blend SHA-256:

`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay, in order:
1. V01
2. V02
3. V03
4. V04
5. V05

Do not patch historical modeling code.

## Gate C — exact source composition

Original V05 `objects_for("Electrical / LV-MV room", record)` must return exactly:

**30 objects**

Composition:
- BASE = 7
- V01 = 23
- V02 = 0
- V03 = 0
- V04 = 0
- V05 = 0

Any mismatch => STOP before canonical mutation.

## Gate D — V01 dimensional contract

All 23 V01 objects must match the explicit centers/dimensions/endpoints in:

`coordination/Audits/REV005_F03_ELECTRICAL_HISTORICAL_SOURCE_PROVENANCE.md`

Tolerance:
- center component <= 0.001 m
- dimension component <= 0.001 m
- cable endpoint component <= 0.001 m

## Gate E — historical source visual parity

Run original V05 renderer.

Required archived evidence:

A:
`2F3BDEEAEDDC850B3CF23E4125171EA5CF9858C4883FC146C3B69E6F4EE892A4`

B:
`850EAB71C210E923B9042382E373DD42421B3E2A4A6CED281C294E43A05FFA7A`

Raw PNG metadata differences are permissible only if decoded/IDAT pixel parity is exact.

## Gate F — destination restoration

Remove/unlink only the broken/current Electrical/LV-MV representation.

Append exactly 30 accepted objects + dependencies into:

`REV005_FG_F03_ELECTRICAL_LV_MV_ACCEPTED_V05_REPLAY`

Preserve:
- source world transform
- dimensions
- data
- materials
- parent relationships
- accepted visibility

Tolerances:
- location <= 0.001 m/axis
- rotation <= 0.0001 rad/axis
- scale <= 0.0001/axis
- dimensions <= 0.001 m/axis

## Gate G — destination A/B parity

Facility-only destination renders at historical V05 Workbench settings:

A 900×600:
- location (117,50,11)
- target (111,61,3)
- lens 52 mm

B 900×600:
- location (113,56,7)
- target (111,61,3)
- lens 52 mm

Must visually/pixel-match archived A/B.

## Gate H — prior PASS regression protection

Before and after F03 mutation verify exact protection parity for:

### F01
- 76 names
- matrix_world
- dimensions
- materials
- parent
- visibility

### F02
- 79 names
- matrix_world
- dimensions
- materials
- parent
- visibility

Any prior-PASS mutation => FAIL.

## Gate I — integrated collision preflight

Compute exact F03 union world bounds.

Run 8 azimuth candidates:
0,45,90,135,180,225,270,315°.

For each candidate:
- 9-ray LOS test
- camera not inside geometry
- no immediate architectural intersection within 1.0 m
- full F03 in frame
- F03 projected screen coverage 30–65%

Accept only >=7/9 clear rays.

No automatic hide/quarantine/exclusion of another facility.

If no candidate passes:
STOP and report exact blockers.

## Gate J — human review evidence

Required:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600 same camera/state

Visible cues:
- dense switchgear row
- cabinet front faces
- breaker windows
- cable risers
- busbar trunk
- service clearance
- remote service panel
- safety/service relationship

## Gate K — source/scope protection

- REV004 unchanged
- no REV006
- no .hiveai
- no tour/video
- no F04
- no TASKS edit
- no locked criteria edit
- Glass Deck quarantine unchanged
- historical Glass Deck source unchanged

## Gate L — stop

Stop exactly:
`AWAITING_GPT_FACILITY_AUDIT_F03`

Do not begin F04.
