# REV005 INTERIOR REMEDIATION V06 — INDEPENDENT GPT AUDIT

## Audit outcome

REMEDIATION_REQUIRED

V06 does not satisfy the locked 26/26 complete-interior gate.

The audit inspected the actual unlabeled V06 QA renders, not only Codex readiness prose, object counts, validation JSON, or matrix claims. Artifact provenance was also checked against the immutable V06 baseline record.

## Executive finding

V06 fixed the hash-provenance defect correctly, but the visual-completion problem remains.

- Provenance integrity: PASS
- Source/workflow protection: PASS based on published evidence
- Preserved V05 PASS groups: 6/6 remain acceptable
- V06 remediated groups: 20/20 still fail the locked final visual-completeness gate to varying degrees
- Overall final visual PASS: 6/26
- Final decision: REMEDIATION_REQUIRED

The dominant V06 root cause is no longer simply “not enough objects.” The V06 build reports about 1,950 new objects, yet the QA renders remain visually close to the V05 evidence in many areas. New geometry is either not materially visible/useful in the audited views, is hidden/occluded/poorly integrated, or still consists of low-information primitives that do not prove the required function.

## Preserved PASS groups

These remain visually acceptable and should remain frozen unless a regression is discovered:

1. Caps and Trigger Assembly
2. Daycare / Crèche
3. Electrical / LV-MV Room
4. Employee Changing / Shower / Locker Support
5. Fire Pump House
6. Micro-ingredient Weigh / Dispense

## V06 remediation groups still failing

### Administration / HQ / R&D / QC — FAIL
The wide and detail renders remain dominated by large brown cuboid masses, sparse tables and generic screens. The required office/admin + R&D/QC-lab distinction is not visible label-blind.

### Bottle Blow Molding — FAIL
The wide shot still reads as large colored housings. B/C are extreme panel closeups and do not prove preform feed, oven/heating, mould/blow cell and bottle outfeed as one process.

### Chemical Compound / Controlled Receiving — FAIL
Renders remain dominated by generic cylindrical tanks/bunds. Receiving containers, staging, transfer pumps/hoses/valves and controlled-access workflow are not visually demonstrated.

### ETP / Water Treatment — FAIL
The wide view shows tanks/pipes, but the treatment train is still not understandable as a sequence. Basins/filters/pumps/service flow are not visually legible enough to identify the system without metadata.

### Finished Goods Warehouse / Dispatch — FAIL
Racking is strong, but dispatch consolidation/loading/AMR/dispatch-control identity is not convincingly visible. The locked warehouse gate requires more than stored pallets.

### Glass Deck Central Command / Training / Café Gallery — FAIL
A_WIDE remains heavily occluded by large foreground geometry. B/C show fragments of command/training/café zones rather than one coherent finished architectural interior.

### Liquid Filling / Packaging — FAIL
B/C still show generic colored housings and panels. Filling nozzles, capper, labeling, inspection and secondary packing are not visually self-identifying as a coherent line.

### Occupational Health / First Aid — FAIL
The wide view contains partitions and sparse furniture, while B/C show partitions/stools/empty floor rather than a recognisable clinic with exam/treatment and clinical support.

### Packaging Warehouse — FAIL
Racks/boxes are present, but packaging-material specificity and issue-to-production/receiving logic remain weak. B/C do not prove the required operational differentiation.

### Powder Handling / Packing — FAIL
The line remains a hopper/tank plus large box-like housings. B/C are dominated by the vessel and do not prove dosing/FFS/fill/seal/finished-pack outfeed.

### Production Hall / Wet Processing / Process Core — FAIL
The evidence still reads mainly as a row of tanks. B/C do not visually prove platforms, manifolds, pumps, CIP and transfer relationships at the required level.

### Raw Material Warehouse / Receiving — FAIL
Racks and drums are present, but receiving/inspection/dock/staging logic is still weak and not strongly differentiated from the other warehouses.

### Restaurant / POVU Café / Kitchen — FAIL
Dining tables are visible, but the evidence does not convincingly show café service/backbar and kitchen/back-of-house as independently legible functional zones.

### Security / Reception / Visitor Arrival — FAIL
Reception/security cues exist, but the finished visitor-flow/access-control relationship remains too generic/open and not fully demonstrated.

### Security Gatehouse — FAIL
A_WIDE hints at barrier/control geometry, but B/C largely show partitions/monitor panels and do not demonstrate an enclosed booth with clear vehicle-control relationship.

### Toothpaste Production — FAIL
The process remains tanks plus generic machine housings. B/C do not prove tube feed/fill/crimp/code/carton sequence.

### Training / Academy — FAIL
Classroom furniture and screen are recognisable, but the space still lacks a convincingly finished architectural envelope in the audited views.

### Utilities / Engineering — FAIL
A_WIDE shows tanks/piping, while B/C become tank/pipe closeups. Compressor/air, boiler/steam and RO/water systems are not visually differentiated.

### Wellness / Recreation — FAIL
Some equipment/yoga cues exist, but B/C show sparse machines/open floor. The room still does not read as a finished wellness interior.

### Wet Wipes Production — FAIL
Unwind cues exist at one end, but B/C revert to generic colored boxes. Web path, wetting, folding/cutting and pouch/sealing/outfeed are not visually legible as one process.

## Locked-gate assessment

### Gate A — Source/workflow protection
PASS based on published evidence.

REV004 is reported unchanged; no REV006, tour, .hiveai, or tracker self-promotion was created by Codex.

### Gate B — Preserve six V05 PASS groups
PASS.

The six preserved groups remain acceptable.

### Gate C — Remediate all 20 V05 FAIL groups
FAIL.

The audited V06 QA does not close the 20-group visual-completeness requirement.

### Gate D — Label-blind identity
FAIL.

Multiple remediated groups still require filename/matrix prose to understand their intended function.

### Gate E — Architectural enclosure
FAIL.

Admin, Glass Deck, Occupational Health, Restaurant/Café/Kitchen, Security/Reception, Gatehouse, Training and Wellness remain insufficiently finished in the audited views.

### Gate F — Warehouse differentiation/completion
FAIL.

Storage is visible, but receiving/issue/dispatch operational identity and differentiation remain insufficient.

### Gate G — Industrial process specificity
FAIL.

Bottle, Liquid Filling, Powder, Wet Processing, Toothpaste and Wet Wipes remain under-proven visually.

### Gate H — Utilities/support specificity
FAIL.

Chemical Receiving, ETP and Utilities remain too generic. Fire Pump and Electrical remain preserved PASS.

### Gate I — People-space specificity
FAIL.

Several occupied spaces remain sparse or generic.

### Gate J — QA framing
FAIL.

Many B/C views are excessively close and hide the function they are intended to prove. Examples include Bottle panels, Chemical tank walls, Powder vessel closeups, Utilities tanks/pipes, Gatehouse partitions and Wet Wipes generic housings.

### Gate K — Matrix truthfulness
FAIL.

The matrix continues to claim several process/facility features that are not clearly visible in the linked renders.

### Gate L — Provenance integrity
PASS.

The provenance defect from V05 is fixed correctly.

Immutable V05 baseline:
- Blend: B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6
- GLB: 1BF506A0EF8ADAF73D20CADAAD151258E293929440FFE681AC6A2ABD21CE4D20

V06 final:
- Blend: 393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD
- GLB: 8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089

The before values were captured before mutation in V06_BASELINE_HASHES.json and were not overwritten.

### Gate M — 26/26 final count
FAIL: 6/26 visual PASS.

### Gate N — Stop discipline
PASS.

Codex stopped at AWAITING_GPT_REMEDIATION_AUDIT_V06.

## Root-cause direction for V07

V07 must not begin by adding another large batch of objects.

Before changing geometry, it must audit why the V06-added collection is not materially visible in the QA:

- object locations and scale relative to the canonical facility;
- collection/view-layer visibility and hide_render state;
- whether new objects are inside/behind old proxy geometry;
- whether cameras are pointed at the old proxy instead of the new geometry;
- whether V06 additions are spatially disconnected from the canonical facility;
- whether old large cuboids obscure the new detailed subassemblies;
- whether GLB/export visibility differs from Blender QA visibility.

Only after that diagnostic should geometry be repositioned, unhidden, integrated, or selectively rebuilt.

The next remediation must prove the correction with useful process-scale views, not extreme closeups.

## Final decision

REMEDIATION_REQUIRED

REV005 is not frozen. Final-tour work remains blocked.
