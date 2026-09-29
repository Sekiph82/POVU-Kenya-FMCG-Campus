# REV005 FACILITY F02 — DAYCARE / CRÈCHE — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex  
**Independent auditor:** GPT  
**Method:** deterministic historical replay + exact 79-object transfer

Codex MUST NOT edit this file.

## Gate A — current baseline protection

Current canonical accepted baseline after F01:
- Blend SHA-256: `80C4FC83DBD260CB9D0A6B02F0582C5829273450437B90D7CD2B9281C17B744E`
- GLB SHA-256: `9EA90C327C2502AA019AD9ADA656BE0BC0B652A19724BEF3162910058B63FD40`

F01's accepted 76 objects are protected and may not change.

The quarantined V09 Glass Deck replacement collection must remain quarantined.

## Gate B — historical replay source

Create detached system-temp worktree at:
`420038365847de763d64c8583a9e31ac5a6bd677`

Initial temp Blend SHA-256:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay V01→V02→V03→V04→V05 exactly, without modifying historical modeling code.

## Gate C — exact 79-object composition

After replay, original V05 `objects_for()` logic for:
`Daycare / crèche`

must return exactly **79** objects:
- 41 visible base objects
- 38 V03 Daycare objects
- 0 V01
- 0 V02
- 0 V04
- 0 V05

Any mismatch => STOP before canonical mutation.

## Gate D — exact source visual proof

Run original V05 renderer.

Required archived visual SHA-256:

A_WIDE:
`72370EF41D5C1EA3AE81500EE77F5764725D8C0C3E0622D1CD21B55344F757EE`

B_FUNCTIONAL:
`7E06E34994D36AE6D84D3F4A58B1C7E05BC3FEEECD79EC06514ECDB2DC5A3F7B`

Raw PNG metadata differences are permitted only if decoded/IDAT pixel equality is demonstrated and normalized evidence reproduces archived hashes.

## Gate E — exact destination transfer

Remove/unlink only broken/current Daycare representations.

Append exactly 79 accepted objects + dependencies into:
`REV005_FG_F02_DAYCARE_ACCEPTED_V05_REPLAY`

Transform tolerances:
- location <= 0.001 m/axis
- rotation <= 0.0001 rad/axis
- scale <= 0.0001/axis
- dimensions <= 0.001 m/axis

All selected accepted objects must be visible in the operational accepted state.

## Gate F — destination parity

Facility-only destination renders at historical V05 900×600 settings must visually/pixel-match archived A/B.

Required:
- A visual parity
- B visual parity

## Gate G — F01 regression protection

Before and after F02 mutation:
- F01 76 names unchanged
- F01 matrix_world unchanged
- F01 dimensions/materials/parents unchanged
- F01 visible operational state unchanged

Any F01 mutation => FAIL.

## Gate H — integrated collision preflight

Before saving F02 as complete:
- compute exact F02 world bounds
- run 8-azimuth integrated-camera search
- 9-ray target test
- candidate requires >=7/9 clear rays
- F02 projected screen coverage 30–65%
- no temporary cross-facility exclusion is allowed automatically

If no valid camera:
STOP with exact first-hit blockers.
Do not mutate another facility.

## Gate I — human review evidence

Render:
- A_CONTEXT 1440×960 from historical A camera
- B_FUNCTIONAL 1440×960 from historical B camera
- D_INTEGRATED_CONTEXT 1440×960
- D preview 900×600 from the exact same integrated camera

All must clearly show the accepted child-scale Daycare identity.

## Gate J — source/scope protection

- REV004 unchanged
- no REV006
- no .hiveai
- no tour/video
- no second Desktop root
- no other facility geometry mutation
- quarantined Glass Deck replacement remains quarantined
- historical Glass Deck source remains unchanged
- TASKS and criteria files not edited by Codex

## Gate K — stop

Stop exactly:
`AWAITING_GPT_FACILITY_AUDIT_F02`

Do not begin F03.
