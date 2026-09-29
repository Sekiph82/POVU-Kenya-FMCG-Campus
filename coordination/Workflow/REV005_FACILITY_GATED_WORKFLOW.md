# REV005 FACILITY-GATED COMPLETION WORKFLOW

## Purpose

REV005 interior completion is executed **one facility at a time**.

No executor may work on Facility N+1 before Facility N has:
1. been implemented/restored;
2. produced locked QA evidence;
3. been independently reviewed by GPT;
4. received explicit PASS.

A FAIL loops only on that facility.

## Hard rules

- Exactly one facility active at a time.
- No multi-facility batch.
- Codex stops after the active facility.
- Codex never edits root `TASKS.md`.
- Codex never awards independent PASS.
- REV004 frozen; no REV006; no tour/video; no `.hiveai`.
- Canonical local root: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`.
- No second Desktop project copy.

## Class R — historical accepted-facility restoration

These six were independently accepted in V05:
1. Caps and Trigger Assembly
2. Daycare / Crèche
3. Electrical / LV-MV Room
4. Employee Changing / Shower / Locker Support
5. Fire Pump House
6. Micro-ingredient Weigh / Dispense

Important provenance rule:

A V05 report may contain a local post-build whole-Blend hash that was never committed as a binary. Therefore a Class R source is not validated solely by whole-Blend hash.

A historical Git source becomes authoritative when the facility subset is proven equivalent by:
- expected Git source hash;
- exact historical object-selection/count logic;
- exact historical QA render reproduction using locked cameras/render settings.

When exact archived render hashes are available, **byte-identical historical render reproduction is the strongest source-equivalence gate**.

Do not invent replacement dimensions for Class R. Once subset equivalence is proven, source transforms/dimensions/materials are the dimensional specification.

## Class N — new detailed completion

The remaining 20 facilities are rebuilt/refined one-by-one.

Every Class N prompt must define:
- local coordinate frame/origin;
- room/process envelope dimensions in metres;
- major assembly XYZ centers;
- width/depth/height or diameter/height;
- quantity;
- center-to-center spacing;
- aisle/clearance dimensions;
- connections;
- visible pipe/conveyor dimensions;
- wall/door/ceiling dimensions;
- materials;
- lighting;
- camera XYZ/target/lens/render size;
- explicit visual acceptance.

Vague instructions are prohibited.

## QA per facility

Minimum evidence:
- A_CONTEXT
- B_FUNCTIONAL
- C_DETAIL_OR_SEQUENCE when relevant
- integrated context regression render
- exact implementation/source manifest
- before/after hashes

Default review render: 1440×960 PNG unless prompt says otherwise.

## Stop state

Each facility ends at:
`AWAITING_GPT_FACILITY_AUDIT_FXX`

No next-facility work begins automatically.
