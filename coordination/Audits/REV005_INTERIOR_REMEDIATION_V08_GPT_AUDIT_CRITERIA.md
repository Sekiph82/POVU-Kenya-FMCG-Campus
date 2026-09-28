# REV005 INTERIOR REMEDIATION V08 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT independent audit  
**Executor:** Codex  
**Canonical tracker:** root `TASKS.md`

Codex MUST NOT edit this file.

## Objective

Verify that V08 replaced intrinsically weak/generic geometry in the 20 failing groups with clean, facility-specific, label-blind readable interiors/processes.

Only full 26/26 PASS permits owner freeze.

## Gate A — Preserve six prior PASS groups

Must remain PASS:
- Caps and Trigger Assembly
- Daycare / Crèche
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Fire Pump House
- Micro-ingredient Weigh / Dispense

## Gate B — Clean-replacement evidence

Require `V08_CLEAN_REPLACEMENT_MAP.md`.

For each of the 20 failing groups it must identify:
- dedicated V08 clean subcollection;
- obsolete legacy/proxy geometry hidden from render/export;
- replacement scope;
- isolated proof path;
- integrated proof paths.

A vague "improved details" statement is insufficient.

## Gate C — Isolated label-blind proof

Each of the 20 remediation groups must have one isolated unlabeled proof image.

PASS requires:
- facility occupies most of frame;
- no label/callout;
- function is understandable from geometry alone;
- no legacy proxy blocking;
- no open-slab placeholder presentation when an interior envelope is required.

If isolated proof fails, the group fails even if integrated campus views look better.

## Gate D — Integrated QA

Each remediation group requires:
- A_CONTEXT
- B_FUNCTIONAL
- C_SEQUENCE_OR_DETAIL

Each preserved group requires:
- A_CONTEXT
- B_FUNCTIONAL

Expected minimum total: 92 QA images.

Reject blank, duplicate, tiny-subject, panel-only, tank-wall, pipe-only, empty-floor or misleading views.

## Gate E — Architectural interiors

These must visibly show coherent finished interiors:
- Admin/HQ/R&D/QC
- Glass Deck Command/Training/Café Gallery
- Occupational Health
- Restaurant/Café/Kitchen
- Security/Reception
- Security Gatehouse
- Training/Academy
- Wellness/Recreation

Props on an open slab are FAIL.

## Gate F — Warehouse differentiation

Raw Material, Packaging and Finished Goods must each be complete and visually distinct.

- Raw: receiving/inspection/staging + raw storage.
- Packaging: packaging-material storage + issue-to-production.
- Finished: finished storage + consolidation/dispatch/loading.

Racks alone are FAIL.

## Gate G — Industrial process specificity

### Bottle
preform feed -> heat -> blow/mould -> bottle outfeed

### Liquid Filling
bottle infeed -> fill -> cap -> label/inspect -> secondary pack/outfeed

### Powder
feed/dose -> fill/FFS -> seal -> finished pack outfeed

### Wet Processing
mix tanks + agitators + access + piping/manifold/pumps + CIP/transfer

### Toothpaste
mix/hold -> tube feed -> fill -> seal/crimp/code -> carton

### Wet Wipes
roll -> web -> wet -> fold/cut -> pouch/seal -> discharge

Generic colored boxes do not pass.

## Gate H — Utilities/support specificity

- Chemical Receiving: receiving/staging + bunding + controlled transfer/access.
- ETP: visually coherent treatment stages and service flow.
- Utilities: compressed air, boiler/steam, RO/water visibly distinguishable.
- Fire Pump and Electrical preserve PASS.

## Gate I — People-space specificity

- Admin distinguishes office/admin and QC/R&D lab.
- Clinic reads as clinic/treatment/waiting/support.
- Restaurant shows dining + café + kitchen.
- Training reads as enclosed classroom.
- Wellness reads as enclosed fitness/wellness.
- Security/Reception shows visitor/security flow.
- Gatehouse shows booth + lane/barrier relationship.
- Glass Deck shows command + training + café/gallery in one coherent interior.

## Gate J — Matrix truthfulness

The V08 matrix may claim only features clearly visible in linked images.

Any systematic overclaim is FAIL.

## Gate K — Provenance

V08 baseline must exactly match V07 final:
- Blend: `BF61CAFCD0EA20E5FE371D491913A51D866AE058F58242FDC30B94AB454ACBD8`
- GLB: `105C83237E5903B1957E206A17E278B7B60214BE38E78F65AB65937294338BE7`

Before values must be immutable and final values must differ if canonical geometry/export changed.

## Gate L — Source/workflow protection

PASS requires:
- REV004 unchanged;
- no REV006;
- no tour;
- no `.hiveai`;
- TASKS.md untouched by Codex;
- locked criteria untouched;
- owner exterior corrections preserved;
- East/West Glass Deck Access presentation references absent.

## Gate M — Final count

Full PASS requires:
- 26/26 visual PASS
- 20/20 isolated remediation proof PASS
- 6/6 preservation PASS
- 0 enclosure failures
- 0 process failures
- 0 evidence failures
- 0 source/provenance failures

No PASS_WITH_FINDINGS.

## Gate N — Stop discipline

Codex must stop at:

`AWAITING_GPT_REMEDIATION_AUDIT_V08`

Independent outcomes:
- `PASS`
- `REMEDIATION_REQUIRED`
- `BLOCKED`
