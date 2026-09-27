# REV005 INTERIOR REMEDIATION V04 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT independent audit stage  
**Executor:** Codex  
**Tracker:** root `TASKS.md`  
**Rule:** Codex MUST NOT edit this audit-criteria file and MUST NOT promote the V04 task to `[x]` in `TASKS.md`.

## Audit objective

Determine whether REV005 has finally reached the owner's requirement:

> The campus must be a complete digital-twin version in which the interiors of all campus buildings/facilities are actually modeled and visually understandable, not merely present as named groups, generic blocks, sparse props, empty slabs, or labels.

The audit is image-first. Builder self-report, object counts, group counts, file existence, object names, and validation JSON are supporting evidence only.

## Gate A — Scope and source protection

PASS requires:
- REV004 remains frozen and unchanged.
- Work is confined to REV005.
- No REV006 is created.
- No final tour or owner-review MP4 is created during this remediation task.
- Approved exterior corrections remain intact: Hands of Growth state, owner-specified tree removals, Living Wall extent, VIP entrance relationships.
- East Glass Deck Access and West Glass Deck Access presentation/callout references remain absent.
- Root `TASKS.md` is not self-promoted by Codex; GPT updates tracker truth after independent audit.

## Gate B — 26/26 visual-completeness audit

The audit must inspect every canonical facility group independently. Presence is not completion.

Canonical groups:
1. Administration / HQ / R&D / QC
2. Bottle Blow Molding
3. Caps and Trigger Assembly
4. Chemical Compound / Controlled Receiving
5. Daycare / Crèche
6. ETP / Water Treatment
7. Electrical / LV-MV Room
8. Employee Changing / Shower / Locker Support
9. Finished Goods Warehouse / Dispatch
10. Fire Pump House
11. Central Glass Deck Command / Training / Café Gallery
12. Liquid Filling / Packaging
13. Micro-ingredient Weigh / Dispense
14. Occupational Health / First Aid
15. Packaging Warehouse
16. Powder Handling / Packing
17. Production Hall / Wet Processing / Process Core
18. Raw Material Warehouse / Receiving
19. Restaurant / POVU Café / Kitchen
20. Security / Reception / Visitor Arrival
21. Security Gatehouse
22. Toothpaste Production
23. Training / Academy
24. Utilities / Engineering
25. Wellness / Recreation
26. Wet Wipes Production

Any unresolved group means the complete-REV005 claim is not accepted.

## Gate C — Label-blind identity test

For every group, inspect the unlabeled QA render as if the filename and metadata were hidden.

PASS requires that a reasonable reviewer can infer the facility/process from visible geometry, layout, equipment, furniture, circulation, enclosure, and process relationships.

A label, object name, folder name, report paragraph, or builder explanation must not be required to understand the scene.

## Gate D — Finished-interior standard

Occupied/support interiors must not look like furniture floating on an empty slab. Audit for:
- coherent floor/wall/partition/ceiling or soffit cues where appropriate;
- functional zoning;
- believable circulation;
- furniture/equipment appropriate to the facility;
- service/storage/support relationships;
- sufficient density and specificity to read as a completed interior rather than a concept blockout.

Industrial interiors must not look like isolated primitives. Audit for:
- coherent process sequence;
- facility-specific machine silhouettes;
- conveyors, piping, manifolds, web paths, guards, tanks, hoppers, racks or other interfaces where appropriate;
- operator/service access;
- logical infeed/process/outfeed relationships;
- differentiation from other production areas.

## Gate E — Known V03 weak areas

Apply heightened scrutiny to the areas that failed or remained weak in the V03 independent visual audit:

- Bottle Blow Molding
- Liquid Filling / Packaging
- Toothpaste Production
- Wet Wipes Production
- Central Glass Deck Command / Training / Café Gallery
- Restaurant / POVU Café / Kitchen
- Finished Goods Warehouse / Dispatch
- Raw Material Warehouse / Receiving
- ETP / Water Treatment
- Fire Pump House
- Occupational Health / First Aid
- Utilities / Engineering
- Administration / HQ / R&D / QC visual proof

These areas may PASS only with convincing new visual evidence. Do not accept object-count growth as remediation.

## Gate F — Previously stronger areas / regression protection

Preserve and regression-check the areas that were previously visually stronger or accepted in narrower audits, including:
- Caps and Trigger Assembly
- Micro-ingredient Weigh / Dispense
- Daycare / Crèche
- Production Hall / Wet Processing / Process Core
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Security / Reception / Visitor Arrival
- Security Gatehouse
- Training / Academy
- Chemical Compound / Controlled Receiving
- Packaging Warehouse
- Wellness / Recreation

A regression in any of these prevents full PASS.

## Gate G — Warehouse-specific acceptance

Raw Material Warehouse, Packaging Warehouse, and Finished Goods Warehouse / Dispatch must each be visually distinct and operationally credible.

Audit for:
- real rack/pallet/storage organization where relevant;
- receiving/staging/dispatch logic;
- aisle/circulation layout;
- material-handling context;
- clear differentiation among raw-material receiving, packaging storage, and finished-goods dispatch.

Floor striping alone is not a warehouse interior.

## Gate H — Utility/support-specific acceptance

ETP / Water Treatment, Utilities / Engineering, Electrical / LV-MV, and Fire Pump House must each have distinct functional identity.

Examples of acceptable visual cues:
- ETP/water: tanks/basins, pumps, filters, treatment train/piping, service access;
- utilities: compressor/air system, boiler/steam, RO/water, service manifolds/equipment as supported by project scope;
- electrical: switchgear/panels, safe service clearances;
- fire pump: pump sets, headers/manifold, valves and service arrangement.

Generic boxes do not close this gate.

## Gate I — People/support-space acceptance

Administration / HQ / R&D / QC, Occupational Health, Restaurant/Café/Kitchen, Daycare, Training and Wellness must read as real usable spaces.

Particular requirements:
- Admin/HQ/R&D/QC must show offices/meeting/reception plus identifiable lab/QC work where applicable.
- Occupational Health must visibly read as a clinic/first-aid environment with treatment/waiting/support identity.
- Restaurant/Café/Kitchen must independently communicate dining, café service and back-of-house kitchen functions.
- Daycare must remain clearly child-oriented.
- Training must retain classroom/presentation identity.
- Wellness must retain actual recreation/wellness use.

## Gate J — Production-line acceptance

The following production areas must be mutually distinguishable without labels:
- Bottle Blow Molding
- Caps/Trigger Assembly
- Liquid Filling/Packaging
- Powder Handling/Packing
- Toothpaste Production
- Wet Wipes Production
- Wet Processing

A generic conveyor plus colored boxes repeated across lines is an audit failure.

## Gate K — QA evidence quality

For each canonical group require at least two useful unlabeled renders:
- orientation/wide;
- functional/detail.

For known weak/complex groups, require a third process/detail view when needed.

Evidence must:
- be well lit;
- be non-empty;
- avoid blocking walls/slabs/trees/unrelated geometry;
- show materially different views;
- show the actual target;
- avoid facility-identifying labels/callouts embedded in the image.

A 26-group contact sheet/index must reconcile exactly with the canonical inventory.

## Gate L — Evidence and artifact integrity

Require:
- updated REV005 master `.blend`;
- updated exported REV005 `.glb`;
- V04 report;
- V04 validation JSON;
- 26-group visual acceptance matrix/index;
- QA renders;
- Codex log;
- before/after REV005 SHA-256 hashes;
- frozen REV004 hash evidence.

Automated validation may support but never replace image inspection.

## Gate M — Stop discipline

Codex must stop at:
`AWAITING_GPT_REMEDIATION_AUDIT_V04`

It must NOT:
- create an owner-review video;
- create the final REV005 campus tour;
- create REV006;
- mark M08.07 or M08.08 complete in root `TASKS.md`.

## Independent GPT audit outcomes

- `PASS` — all 26 groups meet the visual-completion gates and source/regression gates.
- `REMEDIATION_REQUIRED` — any group remains incomplete, generic, misleading, badly evidenced, or regressed.
- `BLOCKED` — required evidence/artifacts cannot be inspected or a source-integrity problem prevents a reliable audit.

For final REV005 model freeze, `PASS_WITH_FINDINGS` is not sufficient. The complete-interior claim requires full `PASS`.
