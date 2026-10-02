# REV005 F06-X02 — Independent GPT Audit

## Verdict

`REMEDIATION_REQUIRED_X03_EVIDENCE_PAIR`

Audited execution commit:

`c1963124397d4b343349e075fd9b883eb911f403`

F07 remains blocked.

## PASS gates locked

### F06 accepted geometry
- Destination count = 43.
- Contribution split = BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1.
- All 43 accepted F06 signatures unchanged.
- Canonical Blend unchanged:
  `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

### X01 quarantine
Exactly seven authorized X01 quarantine objects remain locked:
- V09_TOOTHPASTE_FLOOR
- V09_TOOTHPASTE_BACK_WALL
- V09_TOOTHPASTE_SOFFIT
- V09_WET_WIPES_FLOOR
- V09_WET_WIPES_BACK_WALL
- V09_WET_WIPES_LEFT_WALL
- V09_WET_WIPES_SOFFIT

No quarantine widening is authorized.

### GLB export parity
Deterministic baseline-membership export PASS:
- baseline nodes = 10,605
- final nodes = 10,598
- baseline meshes = 10,449
- final meshes = 10,442
- missing expected names = 0
- unexpected names = 0
- accepted F06 names present = 43/43
- seven X01 quarantine names absent = 7/7

Accepted canonical GLB:
`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

This GLB is locked for X03.

## Camera evidence finding

X02 rendered 78 new current-context candidates and 19 reached >=7/9 LOS.

Best process overview:
`F06_X02_CANDIDATE_01`

- camera (8,43,6)
- target (-4,50,2.8)
- lens 20 mm
- LOS 9/9

Direct review confirms this frame shows:
- weigh booth/enclosure;
- substantially complete four-hopper row;
- hopper valves/outlets;
- dosing paths;
- precision balance stations;
- balance table;
- transfer tote;
- coherent hopper → dosing → balance → transfer relationship;
- legitimate current context.

However it does not clearly establish:
- operator/service zone;
- access organization.

The foreground neighboring structure also occupies a large part of the frame.

## Root-cause conclusion

After:
- M08.37: 32 candidates;
- M08.38: 32 candidates;
- M08.39: 78 candidates;

the remaining failure is not evidence of missing accepted F06 geometry.

The single-frame contract itself is over-constrained for this facility.

The accepted historical F06 geometry places:
- process/hopper/dosing/balance elements toward the booth/workflow side;
- operator/service elements toward the front/service side.

Current legitimate context creates occlusion tradeoffs between those two functions.

Continuing to demand one frame that proves both sides simultaneously would encourage either:
- unnecessary geometry mutation;
- unjustified neighbor quarantine;
- misleading extreme-lens framing.

None is authorized.

## X03 evidence contract

F06 may close using two complementary current-context integrated views:

### View D — Process Integrated Overview
Must show in one frame:
- booth/enclosure;
- hopper row;
- valves/outlets;
- dosing paths;
- precision balances;
- balance table;
- transfer tote/cart;
- coherent process relationship;
- legitimate context.

### View E — Operator / Service / Access Proof
Must show in one frame:
- operator station body/panel;
- operator table/service zone;
- clear floor/access organization around the working area;
- relationship from operator/service side toward balance/transfer workflow;
- enough F06 process geometry to prove this is the same facility;
- legitimate current context.

The two views together must prove the full F06 functional contract.

Neither view may use:
- QA-only hiding;
- additional quarantine;
- geometry mutation;
- neighbor mutation;
- saved visibility changes.

## Acceptance logic

F06-X03 passes if:

1. D independently passes the process-overview gate.
2. E independently passes the operator/service/access gate.
3. Both use the same locked canonical Blend visibility state.
4. Both preserve the accepted seven X01 quarantines only.
5. Both are camera-outside-geometry.
6. Together they cover every original F06 required visual cue.
7. Blend remains unchanged.
8. GLB remains exactly the accepted X02 hash.
9. F07 is not started.

A single-frame all-cues gate is superseded for F06 only.

## X03 scope

Evidence-only.

No Blend save.
No GLB export.
No geometry change.
No quarantine change.
No F07.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F06_X03`
