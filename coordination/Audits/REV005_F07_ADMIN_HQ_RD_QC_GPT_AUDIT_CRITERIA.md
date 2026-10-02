# REV005 F07 — Administration / HQ / R&D / QC — Locked GPT Audit Criteria

## Baseline

Canonical pre-F07 Blend:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

Canonical pre-F07 GLB:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

## Design authority

F07 must conform to:

`coordination/Audits/REV005_F07_ADMIN_HQ_RD_QC_DESIGN_CONTRACT.md`

The V09 Administration/HQ/R&D/QC representation is reference evidence of what failed, not a geometry specification to preserve.

## Ownership / replacement gate

Before mutation:
- inventory every current object with facility metadata `Administration / HQ / R&D / QC`;
- inventory every object in `REV005_V08_CLEAN_ADMINISTRATION_HQ_R_D_QC`;
- classify all overlaps/duplicates by exact object name and collection;
- protect any object whose ownership is ambiguous.

Only confirmed Administration/HQ/R&D/QC legacy representation may be retired/quarantined.

No accepted F01-F06 object may change.

## Geometry gate

Required room envelope:
- center (-58,-64)
- 46 × 28 m
- X -81…-35
- Y -78…-50

Required functional zones:
1. reception / visitor arrival;
2. HQ open office;
3. meeting / collaboration;
4. R&D / QC laboratory.

Required dimensions, equipment, clearances and exact anchor locations are locked in the design contract.

Tolerance:
- primary zone/envelope centers/dimensions <= 0.05 m
- furniture/equipment anchors <= 0.10 m
- required clear aisle dimensions may not be undersized by >0.10 m

## Detail gate

Not acceptable:
- floating desk slabs;
- generic box-only lab;
- empty open slab;
- text-label-only functional identity;
- one colored partition dominating the evidence.

Required:
- supported desks;
- monitors/keyboards/chairs;
- complete meeting table/chairs/display;
- supported lab benches with cabinets;
- sink/service point;
- sample-prep island;
- six distinct QC instrument classes;
- lab storage;
- safety/service cues;
- finished enclosure and lighting.

## Protection gate

Require exact protection of:
- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted 54
- F06 accepted 43
- F04 accepted Training/Restaurant quarantine state
- F06 seven X01 quarantine objects
- Glass Deck quarantine 117
- historical Glass Deck source
- historical Wellness/pavilion protected state
- Restaurant right-wall accepted quarantine state

No unauthorized prior-state difference.

## Legacy retirement gate

The old Administration/HQ/R&D/QC representation must not remain visibly stacked with the new F07 model.

Retirement may use saved visibility/quarantine only for exact confirmed old Admin-owned objects.

Do not delete ambiguous objects.

The retirement manifest must record:
- exact names;
- previous visibility;
- new visibility;
- facility ownership proof;
- collection membership;
- zero transform/material/data changes.

## Visual gate

Required final evidence:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- C_LAB_DETAIL 1440×960
- D_INTEGRATED 1440×960
- 900×600 previews for independent audit

All images must:
- use current canonical saved state;
- use no QA-only hiding;
- be non-black;
- be label-blind readable;
- keep cameras outside geometry;
- avoid dominant foreground blockers.

Specific cue requirements are locked in the design contract.

## GLB gate

Do not use broad `use_visible=True` export.

Use deterministic membership export based on the accepted pre-F07 GLB node-name set:
- remove only exact retired legacy Admin-owned node names that were present in the pre-F07 GLB;
- preserve every other pre-F07 node name;
- add every new F07 accepted object intended for export;
- zero unexpected omissions;
- zero unrelated new nodes.

All accepted F01-F06 names present in the pre-F07 GLB must remain present.

## Scope

No F08.
No REV004 changes.
No REV006.
No tour/video.
No .hiveai.
Codex must not edit root TASKS.md or locked audit/design files.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F07`
