# REV005 INTERIOR REMEDIATION V07 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT independent audit  
**Executor:** Codex  
**Canonical tracker:** root TASKS.md

Codex MUST NOT edit this file.

## Objective

Verify that V07 fixed the actual visibility/integration root cause rather than merely adding more hidden or generic objects.

Full PASS requires:
- 26/26 label-blind visual PASS
- truthful before/after proof
- preserved six prior PASS groups
- correct provenance
- no source/workflow regressions

## Gate A — V07 root-cause diagnostic

Require V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md.

For each of the 20 prior FAIL groups it must truthfully identify whether the V06 detail was:
- hidden or render-disabled
- on a disabled collection/view layer
- misplaced or wrong scale
- inside/behind proxy geometry
- off-camera
- spatially disconnected
- missing from export
- visually lost due materials/lighting
- genuinely insufficient geometry
- another clearly evidenced cause

A generic “added more detail” explanation is not sufficient.

## Gate B — Preserve six PASS groups

These must remain PASS:
- Caps and Trigger Assembly
- Daycare / Crèche
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Fire Pump House
- Micro-ingredient Weigh / Dispense

Any regression blocks full PASS.

## Gate C — Twenty-group remediation closure

All 20 prior V06 FAIL groups must independently PASS.

Any one failure means REMEDIATION_REQUIRED.

## Gate D — Label-blind identity

Hide filenames, folder names, matrix text and labels mentally.

The facility/process must be understandable from visible geometry, spatial organization and functional relationships.

If the matrix prose is required to explain what the image is, FAIL.

## Gate E — Useful QA framing

For each prior FAIL group require:
- A_CONTEXT
- B_FUNCTIONAL
- C_SEQUENCE

Reject:
- panel-only closeups
- tank-wall closeups
- pipe-only closeups
- empty-floor views
- duplicate angles
- views dominated by occluding proxy geometry
- views where the actual process/function is not visible

## Gate F — Before/after material improvement

Require REV005_V07_BEFORE_AFTER_MATRIX.md.

For every prior FAIL group, V07 must visibly improve over the cited V06 evidence.

If the V07 images are materially equivalent to V06 in useful visible content, FAIL that group.

## Gate G — Architectural interiors

The following must visibly read as finished usable interiors:
- Admin / HQ / R&D / QC
- Glass Deck Command / Training / Café Gallery
- Occupational Health / First Aid
- Restaurant / POVU Café / Kitchen
- Security / Reception / Visitor Arrival
- Security Gatehouse
- Training / Academy
- Wellness / Recreation

Require coherent enclosure, zoning and circulation.

## Gate H — Warehouse differentiation

Raw Material, Packaging and Finished Goods must be visually distinct.

Require:
- Raw Material: receiving/inspection/staging + raw storage
- Packaging: packaging-specific materials + issue-to-production logic
- Finished Goods: finished storage + dispatch/loading/control logic

Racks alone are insufficient.

## Gate I — Process specificity

### Bottle Blow Molding
Must show preform feed -> heating -> blow/mould -> bottle outfeed.

### Liquid Filling
Must show bottle infeed -> fill -> cap -> label/inspect -> pack/outfeed.

### Powder
Must show feed/dose -> pack/fill -> seal -> finished outfeed.

### Wet Processing
Must show tanks + access/platform + agitator/process + manifolds/pumps/CIP/transfer.

### Toothpaste
Must show mix/hold -> tube feed -> fill -> crimp/seal/code -> carton.

### Wet Wipes
Must show roll -> web -> wetting -> fold/cut -> pouch/seal -> discharge.

Generic colored boxes do not pass.

## Gate J — Utilities/support specificity

### Chemical Receiving
Receiving/staging + bunding + transfer + controlled access must be visible.

### ETP
Treatment stages must read as a coherent treatment train.

### Utilities
Compressed air, boiler/steam and RO/water functions must be visually distinguishable.

Fire Pump and Electrical must remain PASS.

## Gate K — Matrix truthfulness

The V07 matrix may only claim features clearly visible in linked renders.

Any systematic overclaim is an audit failure.

## Gate L — Provenance

V07 baseline must exactly match V06 final:
- Blend: 393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD
- GLB: 8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089

Before values must be immutable and final values must differ if geometry changed.

## Gate M — Source/workflow protection

PASS requires:
- REV004 unchanged
- no REV006
- no tour
- no .hiveai
- TASKS.md untouched by Codex
- approved exterior corrections preserved
- East/West Glass Deck Access presentation references absent

## Gate N — Final count

Only 26/26 visual PASS permits owner freeze.

No PASS_WITH_FINDINGS.

## Gate O — Stop discipline

Codex must stop at:

AWAITING_GPT_REMEDIATION_AUDIT_V07

Independent outcomes:
- PASS
- REMEDIATION_REQUIRED
- BLOCKED
