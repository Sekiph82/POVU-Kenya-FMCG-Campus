# REV005 INTERIOR REMEDIATION V06 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT independent audit  
**Executor:** Codex  
**Canonical tracker:** root `TASKS.md`

Codex MUST NOT edit this file.

## Objective

Verify whether REV005 finally satisfies the owner's complete-interior digital-twin requirement.

V06 is judged from actual unlabeled QA renders plus truthful artifact provenance.

## Gate A — Source/workflow protection

PASS requires:
- REV004 unchanged;
- only REV005 edited;
- no REV006;
- no owner-review/final tour rendered;
- no `.hiveai`;
- TASKS.md not self-promoted;
- owner exterior corrections preserved;
- East/West Glass Deck Access presentation references absent.

## Gate B — Preserve the 6 V05 PASS groups

These must remain PASS:
- Caps and Trigger Assembly
- Daycare / Crèche
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Fire Pump House
- Micro-ingredient Weigh / Dispense

Any regression prevents full PASS.

## Gate C — Remediate all 20 V05 FAIL groups

Every one of these must independently PASS:
- Administration / HQ / R&D / QC
- Bottle Blow Molding
- Chemical Compound / Controlled Receiving
- ETP / Water Treatment
- Finished Goods Warehouse / Dispatch
- Central Glass Deck Command / Training / Café Gallery
- Liquid Filling / Packaging
- Occupational Health / First Aid
- Packaging Warehouse
- Powder Handling / Packing
- Production Hall / Wet Processing / Process Core
- Raw Material Warehouse / Receiving
- Restaurant / POVU Café / Kitchen
- Security / Reception / Visitor Arrival
- Security Gatehouse
- Toothpaste Production
- Training / Academy
- Utilities / Engineering
- Wellness / Recreation
- Wet Wipes Production

No partial project PASS is allowed.

## Gate D — Label-blind identity

Mentally hide filename, folder and matrix text.

The facility/process must be inferable from visible geometry, spatial organization and functional relationships.

If explanation is required, FAIL.

## Gate E — Architectural enclosure

Occupied/support interiors must visibly show a coherent envelope or credible cutaway:
- walls/partitions;
- doors/openings;
- floor;
- ceiling/soffit/roof-interior cues where appropriate;
- circulation;
- functional zoning.

Props on an open gray slab are FAIL.

Apply strictly to:
- Admin/HQ/R&D/QC
- Glass Deck
- Occupational Health
- Restaurant/Café/Kitchen
- Security/Reception
- Security Gatehouse
- Training/Academy
- Wellness/Recreation

## Gate F — Warehouse differentiation/completion

Raw Material, Packaging and Finished Goods must each:
- be enclosed/architecturally legible;
- show rack/storage organization;
- show staging/handling routes;
- show their own operational edge;
- be visually different from one another.

Specific expectations:
- Raw Material: receiving/inspection/staging + drums/IBCs/raw pallets.
- Packaging: cartons/film/labels/containers + issue-to-production logic.
- Finished Goods: finished pallets + dispatch consolidation/loading context.

Racks alone are FAIL.

## Gate G — Industrial process specificity

### Bottle Blow Molding
Must visibly show:
preform feed -> heating -> blow/mould -> bottle outfeed.

### Liquid Filling / Packaging
Must visibly show:
bottle infeed -> fill/nozzles -> cap -> label/inspect -> secondary pack/outfeed.

### Powder Handling / Packing
Must visibly show:
powder feed/dosing -> fill/FFS/pack -> seal -> finished pack outfeed.

### Wet Processing
Must visibly show:
mix tanks + agitator/process access + piping/manifolds/pumps + CIP/transfer relationship.

### Toothpaste
Must visibly show:
mix/hold -> tube feed -> fill -> seal/crimp/code -> carton.

### Wet Wipes
Must visibly show:
roll unwind -> web path -> wetting -> fold/cut -> film/pouch seal -> pack discharge.

Generic colored boxes are FAIL.

## Gate H — Utilities/support specificity

### Chemical Controlled Receiving
Must show receiving containers/staging, bunding, controlled transfer and access.

### ETP / Water Treatment
Must show a coherent treatment train with basins/tanks/filters/pumps/piping/service access.

### Utilities / Engineering
Must visually distinguish project-supported compressor/air, boiler/steam and RO/water utilities.

### Fire Pump House
Preserved PASS must remain visually distinct.

### Electrical
Preserved PASS must remain visually distinct.

## Gate I — People-space specificity

### Admin/HQ/R&D/QC
Must visibly distinguish office/admin and lab/QC functions.

### Occupational Health
Must look like clinic/first aid, not generic benches/partitions.

### Restaurant/Café/Kitchen
Dining, café service and kitchen/back-of-house must all be independently legible.

### Training
Must be enclosed and clearly classroom/presentation oriented.

### Wellness
Must be enclosed and clearly fitness/wellness oriented.

### Security/Reception
Must show enclosed visitor/security flow.

### Gatehouse
Must show enclosed booth + vehicle-control relationship.

### Glass Deck
Must show command, training and café/gallery functions in one coherent interior.

## Gate J — QA framing

Minimum expected:
- 20 remediation groups × 3 views;
- 6 preservation groups × 2 views;
- 72 total renders.

Reject:
- blank/invalid frames;
- wall-only or slab-only views;
- excessively close views that hide the function;
- duplicate views;
- tiny subjects;
- misleading cutaways that erase the interior envelope.

## Gate K — Matrix truthfulness

The V06 matrix may claim only features visibly proven in linked renders.

Any repeated prose-overclaim is an audit failure.

## Gate L — Provenance integrity

Require immutable baseline file:
`V06_BASELINE_HASHES.json`

It must record the actual V05-final canonical Blend/GLB hashes **before mutation**.

Expected V05 final baseline from the independent record:
- Blend: `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`
- GLB: `1BF506A0EF8ADAF73D20CADAAD151258E293929440FFE681AC6A2ABD21CE4D20`

V06 final hashes must be different if geometry changed.

The baseline file, report, validation and Codex log must agree.

If "before" hashes are overwritten with final hashes, FAIL.

## Gate M — 26/26 final count

Full PASS requires:
- 26/26 groups visually PASS;
- 0 evidence failures;
- 0 enclosure failures;
- 0 process-identity failures;
- 0 source/provenance failures.

No PASS_WITH_FINDINGS for REV005 freeze.

## Gate N — Stop discipline

Codex must stop at:
`AWAITING_GPT_REMEDIATION_AUDIT_V06`

No tour, no REV006, no freeze.

## Independent outcomes

- `PASS`
- `REMEDIATION_REQUIRED`
- `BLOCKED`

Only full `PASS` permits owner final REV005 review/freeze.
