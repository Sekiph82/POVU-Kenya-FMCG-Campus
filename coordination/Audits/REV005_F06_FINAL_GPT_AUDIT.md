# REV005 F06 Micro-ingredient Weigh / Dispense — Final Independent GPT Audit

## Final decision

`PASS`

Audited closure commit:

`dcad5ce30b0a3c1640a94c740f81744229602b69`

F06 is accepted and locked.

## Accepted canonical state

Blend SHA-256:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

GLB SHA-256:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

Accepted F06 destination collection:

`REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`

Count:
- 43 objects

Contribution split:
- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1

## Historical / structural gates

Locked PASS:
- exact historical V05 source reconstruction;
- source A/B/C decoded parity;
- dimensional validation;
- destination A/B/C structural parity;
- all 43 accepted F06 signatures unchanged through X03;
- F01-F05 protection unchanged.

## Accepted X01 quarantine

Exactly seven overlapping unaccepted V09 structural-envelope objects remain canonically quarantined:

1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

No wider quarantine was used or accepted.

## GLB parity

X02 deterministic membership export is accepted:
- 10,598 nodes
- 10,442 meshes
- zero missing expected baseline names
- zero unexpected names
- 43/43 accepted F06 names present
- all seven X01 quarantine names absent

## X03 visual closure

The F06-specific single-frame all-cues requirement was superseded by the independent X02 audit after exhaustive camera search proved that legitimate geometry creates an unavoidable process-side versus service-side occlusion tradeoff.

X03 therefore used two complementary current-context views from the exact same locked canonical state.

### D — Process / Transfer Integrated Overview

Direct review of:

`output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_CONTEXT_PREVIEW_900x600.png`

confirms:
- weigh booth/enclosure readable;
- substantially complete four-hopper row readable;
- hopper outlets/valves readable;
- dosing paths readable;
- precision-balance stations readable;
- balance table readable;
- transfer tote/cart identifiable;
- coherent hopper → dosing → balance → transfer relationship;
- legitimate current context.

Camera:
- XYZ (8,43,6)
- target (-4,50,2.8)
- lens 20 mm
- sensor 36 mm

Result: D PASS.

### E — Operator / Service / Access

Direct review of:

`output/rev005-facility-gated/F06_micro_weigh/X03/E_OPERATOR_ACCESS_CONTEXT_PREVIEW_900x600.png`

confirms:
- operator station body readable;
- operator station panel readable;
- V02 operator/service table readable;
- open access/service aisle readable;
- PPE/service cue visible;
- staging/workspace cue visible;
- hopper/balance process geometry provides a shared spatial anchor linking E to D;
- legitimate current context.

Selected E candidate:
- E01
- camera (-14,44,4.5)
- target (-6,48,2.2)
- lens 20 mm
- sensor 36 mm

Result: E PASS.

## Pair gate

The D + E pair:
- uses the same canonical Blend;
- uses the same saved visibility state;
- preserves exactly the same seven X01 quarantines;
- uses no QA-only hiding;
- uses no neighbor mutation;
- uses no geometry mutation;
- collectively covers the complete original F06 functional visual contract.

Result: pair PASS.

## Closure

F06 Micro-ingredient Weigh / Dispense is independently PASS and locked.

The six Class R historical accepted-facility restorations are now complete.

The facility-gated workflow may proceed to the first Class N facility, F07 Administration / HQ / R&D / QC.
