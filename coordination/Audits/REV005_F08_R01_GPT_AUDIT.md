# REV005 F08-R01 — Independent GPT Audit

## Verdict

`REMEDIATION_REQUIRED_R02_VISUAL_LEGIBILITY_GEOMETRY`

Audited execution commit:

`bdbd8f41`

Canonical F07 baseline remains unchanged.

F09 remains blocked.

## What R01 proved

M08.43 completed the expanded camera search correctly:

- A candidates: 36
- B candidates: 30
- C candidates: 30
- D candidates: 38
- total: 134
- camera-origin mesh-bound hits: 0
- no QA-only hiding
- no visibility mutation
- no canonical promotion

The search was broad enough to answer the camera-only question.

The answer is:

**camera remediation alone is insufficient.**

## Systematic visibility findings

Across all 134 reviewed candidates:

### A_CONTEXT family
- hopper visible: 0 / 36
- feeder/preform path visible: 36 / 36
- heater visible: 36 / 36
- transfer visible: 36 / 36
- mould station readable: 0 / 36
- stretch/blow cue readable: 0 / 36
- outfeed visible: 36 / 36
- formed bottles readable: 22 / 36

### B_FUNCTIONAL family
- hopper visible: 0 / 30
- heater visible: 30 / 30
- transfer visible: 30 / 30
- mould station readable: 0 / 30
- stretch/blow cue readable: 0 / 30
- outfeed visible: 30 / 30
- formed bottles readable: 16 / 30

### C_SEQUENCE_DETAIL family
- heater visible: 30 / 30
- transfer visible: 30 / 30
- mould station readable: 13 / 30
- stretch/blow cue readable: 6 / 30
- outfeed visible: 30 / 30
- formed bottles readable: 9 / 30

### D_INTEGRATED family
- hopper visible: 0 / 38
- heater visible: 38 / 38
- transfer visible: 38 / 38
- mould station readable: 0 / 38
- stretch/blow cue readable: 0 / 38
- outfeed visible: 38 / 38
- formed bottles readable: 23 / 38
- HMI/operator relationship visible: 12 / 38

The repeated zeroes are decisive. The remaining failure is not caused by one unlucky camera.

## Direct selected-view audit

### A selected attempt

`F08_R01_A_SELECTED_PREVIEW_900x600.png`

Direct review confirms:
- feed/heater/cell/outfeed are present;
- room context is readable;
- hopper is not visually established;
- mould/blow mechanism is not readable.

FAIL.

### B selected attempt

`F08_R01_B_SELECTED_PREVIEW_900x600.png`

Direct review confirms:
- heater bank and guarded cell occupy the frame;
- transfer hardware exists;
- downstream conveyor exists;
- mould mechanism and bottle transformation remain weak/ambiguous.

FAIL.

### C selected attempt

`F08_R01_C_SELECTED_PREVIEW_900x600.png`

This is the clearest proof of the current visual-model weakness.

The two station assemblies are visible, but they read primarily as large rectangular platen/block assemblies. The stretch/blow action and bottle-state transformation are not self-explanatory.

The bottle conveyor is visible, but the bottles remain visually small.

FAIL.

### D selected attempt

`F08_R01_D_SELECTED_PREVIEW_900x600.png`

Direct review confirms:
- HMI visible;
- cell and outfeed visible;
- some feed/heater context visible;
- hopper not established;
- mould/blow mechanism not label-blind readable;
- full process identity remains incomplete.

FAIL.

## Visual-model root cause

R01 demonstrates three systematic legibility defects.

### 1. Hopper / feed identity

The hopper exists dimensionally but never reads as a distinct upstream bulk-preform source across 134 candidate images.

The current rectangular bulk-bin + low funnel + rail arrangement does not produce a strong enough hopper/elevator silhouette.

### 2. Heater / oven identity

The current 16 heater elements are visually dominant as large orange vertical bars.

They establish a repeated heating element pattern, but not a convincing enclosed/open-frame infrared oven process.

The heater bank overwhelms the upstream/downstream relationship in wide views.

### 3. Blow-cell / product-state identity

The two mould stations exist technically, but the current platen/mould blocks do not visually communicate:
- clamp action;
- preform entering;
- stretch/blow action;
- formed bottle leaving.

The bottle-state transition is therefore too abstract.

The outfeed bottles are dimensionally present but visually small in context.

## Technical stage findings

R01 deterministic staged-state validation reports:
- accepted staged meshes: 338
- confirmed legacy: 391
- retired legacy: 391
- preforms: 20
- heater elements: 16
- service doors: 2
- HP-air branches: 4
- formed bottles: 16
- protected unauthorized differences: 0
- cross-facility collisions: 0
- outside-envelope objects: 0
- candidate GLB membership: 10,888 / 10,888

These facts remain the starting technical reference for R02.

## Four reconstruction differences

R01 recorded four differences between the old published M08.42 manifest and deterministic helper reconstruction:

- east door jamb positions normalize to Y=9.0 and 11.0;
- east north-wall length normalizes to 11.0 m;
- east south-wall length normalizes to 11.0 m.

These helper-reconstructed values are consistent with the locked design contract:
- service opening Y = 9.0…11.0;
- north wall segment Y = 11.0…22.0;
- south wall segment Y = -2.0…9.0.

R02 therefore treats the helper-reconstructed east enclosure dimensions as the authoritative staged architectural values. Do not reintroduce the stale manifest values.

## R02 authorization

R02 is a narrow **visual-legibility geometry remediation** of new F08 geometry only.

Authorized families:

1. preform hopper / elevator / feed path;
2. heater oven visual construction;
3. oven-to-cell transfer;
4. mould/blow station internal visual detail;
5. formed-bottle outfeed product readability;
6. line-side HMI / aisle visual linkage;
7. local lighting/material contrast needed to reveal those process elements.

Not authorized:
- moving the major process centers;
- changing the room envelope;
- changing accepted F01-F07;
- wider neighbor quarantine;
- redesigning unrelated F08 architecture;
- F09 work.

## Major process anchors remain locked

Preserve:
- hopper nominal center and envelope;
- heater oven center (47.5,10,3.1) and 7×4×4.2 m envelope;
- blow cell center (57,10,3.3) and 8×5.6×5.2 m guarded envelope;
- outfeed center (65,10,1.7) and 9×1.2 m line envelope;
- west→east sequence;
- south operator aisle;
- north service aisle.

R02 may change internal shapes/details and may add F08-only visual-detail meshes inside these locked envelopes.

## R02 visual target

Without labels, an independent viewer must be able to infer:

`bulk preforms → feed/elevator → infrared heating → transfer → clamp/mould + stretch/blow → formed bottles → inspection/outfeed`

The transformation must read from geometry and product states, not from color blocks.

## Canonical promotion

Canonical promotion remains forbidden until R02 passes:
- A/B/C/D visual acceptance;
- dimensional/collision validation;
- prior-state protection;
- exact legacy-retirement state;
- deterministic GLB membership parity.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R02`
