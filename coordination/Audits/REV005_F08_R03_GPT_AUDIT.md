# REV005 F08-R03 — Independent GPT Audit

## Verdict

`REMEDIATION_REQUIRED_R04_PROCESS_STATE_GEOMETRY`

Audited execution commit:

`753fe43`

Canonical Blend and GLB remain unchanged. F09 remains blocked.

## What R03 proved

R03 exhausted the previously untested true external south-frontage camera family without changing geometry or saved visibility.

Rendered candidates:
- A = 24
- B = 24
- C = 24 diagnostic
- D = 24

For valid A/B/D families:
- no geometry/visibility mutation;
- no canonical promotion;
- exact R02 staged source retained.

### Aggregate cue results

A:
- hopper visible: 13/24
- mould station readable: 0/24
- stretch/blow readable: 0/24
- in-process preform readable: 0/24
- formed bottle readable: 0/24
- complete label-blind sequence: 0/24

B:
- mould station readable: 24/24
- stretch/blow readable: 0/24
- in-process preform readable: 0/24
- formed bottle readable: 0/24
- complete label-blind sequence: 0/24

C:
- rendered for diagnosis, but all 24 origins were rejected by the current broad AABB validator;
- mould station readable: 24/24;
- stretch/blow readable: 0/24;
- in-process preform readable: 0/24;
- formed bottle readable: 0/24;
- complete label-blind sequence: 0/24.

D:
- hopper visible: 13/24
- mould station readable: 0/24
- stretch/blow readable: 0/24
- in-process preform readable: 0/24
- formed bottle readable: 0/24
- complete label-blind sequence: 0/24

The decisive repeated zero is the process-state transformation evidence.

## Direct visual audit

### A selected
External frontage finally shows:
- tapered bulk hopper;
- elevator/feed;
- oven;
- cell;
- outfeed.

However the cell internals do not communicate the transformation. Product-state cues are too small at context scale.

### B selected
Heater, transfer, guarded twin mould stations and outfeed are visible.

The mould stations read as machinery, but the actual preform→stretch/blow→bottle state transition is still not visible.

### C selected
The frame provides the clearest twin-station view.

Even here:
- stretch/blow rods do not dominate enough to explain action;
- in-process preform is not readable;
- formed/released bottle state is not readable;
- the machine still reads as two large platen/mould assemblies rather than an understandable transformation sequence.

### D selected
The overall line, hopper/feed, oven, HMI and outfeed are present.

The process still cannot be inferred label-blind because the critical state change inside the blow cell is missing at readable scale.

## Camera-validation correction

R03 marks every C candidate invalid because the camera point lies inside the broad AABBs of `Production_Hall` and `PRODUCTION_ROOF`.

For a hollow hall/roof shell, an AABB hit is not sufficient proof that the camera origin is physically inside solid geometry.

R04 must replace the broad-AABB camera validity test with an actual solid-geometry test, for example:
- point-inside closed mesh where applicable;
- nearest-surface / signed-distance test;
- ray parity test;
- or exact shell-specific spatial logic.

AABB may remain a cheap prefilter, but it may not be the final invalidation criterion.

This validator correction does not change the R03 verdict because all C frames still failed the product-state legibility gate.

## Root cause after R03

Camera-only remediation is now exhausted.

The remaining defect is the visual storytelling of the blow transformation.

The model already contains:
- hopper/feed;
- oven;
- transfer;
- two mould stations;
- outfeed;
- formed bottles.

But it does not visibly explain:
1. heated preform entering a station;
2. mould/clamp action around that preform;
3. vertical stretch/blow action;
4. formed bottle state appearing at/ejecting from the second station;
5. continuous handoff to outfeed.

This is a process-state geometry problem, not another camera problem.

## R04 authorization

R04 may modify only the new staged F08 process-state/detail geometry inside the already-locked major machine envelopes.

Major room/process anchors remain fixed.

R04 may:
- make the two blow stations visibly different cycle states;
- open/reveal mould halves within the locked station envelopes;
- strengthen tie-bar / clamp / nozzle / stretch-rod relationships;
- create clearly visible heated-preform and formed-bottle states at physically plausible positions;
- improve the starwheel/discharge handoff;
- improve first-bottle continuity onto the conveyor;
- improve product silhouette/material contrast;
- add a realistic line-side first-off/sample progression rack only as supplementary evidence, never as a substitute for readable in-machine states;
- improve local lighting/contrast.

R04 must not:
- move major machine centers;
- change the room envelope;
- change accepted F01-F07;
- alter neighbor geometry;
- use text labels to explain the process;
- create another broad camera-only loop.

## Promotion rule

Canonical promotion remains forbidden until:
- A/B/C/D visual set PASS;
- exact process-state transformation is readable without labels;
- dimensional/collision/protection gates PASS;
- exact legacy retirement remains preserved;
- deterministic GLB membership parity PASS.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R04`
