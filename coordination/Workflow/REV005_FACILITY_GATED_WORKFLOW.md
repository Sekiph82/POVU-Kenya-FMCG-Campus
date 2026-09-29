# REV005 FACILITY-GATED COMPLETION WORKFLOW

## Purpose

The previous broad V01–V09 remediation cycles are closed as a failed working method. From this point onward REV005 interior completion is executed **one facility at a time**.

No executor may work on Facility N+1 before Facility N has:
1. been implemented;
2. produced its locked QA evidence;
3. been independently reviewed by GPT;
4. received explicit PASS for that facility.

A facility FAIL loops only on that facility.

## Hard workflow rules

- Exactly one facility is active at a time.
- No batch/master execution across multiple facilities.
- No "continue with the next facility" behavior after rendering.
- Codex stops after the active facility and waits for GPT audit.
- Codex never edits root `TASKS.md`.
- Codex never awards independent PASS.
- REV004 remains frozen.
- REV006 is prohibited.
- No final tour/video until all 26 facilities pass.
- Canonical local root: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`.
- No second Desktop project copy and no `.hiveai`.

## Two facility classes

### Class R — exact historical restoration

These six facilities were independently accepted in V05 and must **not** be approximated or redesigned:
1. Caps and Trigger Assembly
2. Daycare / Crèche
3. Electrical / LV-MV Room
4. Employee Changing / Shower / Locker Support
5. Fire Pump House
6. Micro-ingredient Weigh / Dispense

Authoritative source:
- V05 commit: `420038365847de763d64c8583a9e31ac5a6bd677`
- V05 Blend SHA-256: `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

For Class R, **source geometry/world transforms/materials are the dimensional specification**. Do not invent replacement dimensions. Restore exactly.

### Class N — new/detailed completion

The remaining 20 facilities are rebuilt/refined one-by-one.

Every Class N prompt MUST define:
- facility local coordinate frame and origin;
- facility room/process envelope in metres;
- each major assembly center X/Y/Z;
- width/depth/height or diameter/height;
- quantity;
- center-to-center spacing;
- aisle/clearance dimensions;
- connections between stations;
- pipe/conveyor dimensions where visible;
- wall/door/ceiling dimensions for people spaces;
- materials;
- lighting;
- camera position, target, lens and render size;
- explicit visual acceptance criteria.

Phrases such as "add some equipment", "make it detailed", "place nearby", "improve the line" or "make it realistic" are not sufficient.

## QA contract per facility

Minimum evidence before GPT review:
- A_CONTEXT
- B_FUNCTIONAL
- C_DETAIL_OR_SEQUENCE when functionally relevant
- one integrated-context regression render when requested
- exact implementation manifest / source manifest
- before/after hashes

Default review render size: **1440×960 PNG** unless the facility prompt specifies otherwise.

## Stop state

Every facility prompt defines its own stop state:
`AWAITING_GPT_FACILITY_AUDIT_FXX`

No next-facility work begins from that state.
