# REV005 INTERIOR REMEDIATION V01 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT audit stage  
**Executor:** Codex  
**Rule:** Codex MUST NOT edit this file.

## Audit objective
Verify that all 14 findings from the REV005 Owner Interior Review were genuinely remediated in the model, not merely hidden by labels, object-name assertions, or camera selection, while preserving the 12 previously passing groups and REV004.

## Gate A — Scope integrity
PASS only if:
- REV004 remains unchanged;
- changes are confined to REV005 remediation needs;
- no REV006 is created;
- no final tour is rendered;
- East/West Glass Deck Access presentation references remain excluded.

## Gate B — 14/14 closure
Independently inspect visual evidence for:
1. Bottle Blow Molding
2. Caps and Trigger Assembly
3. Electrical / LV-MV Room
4. Employee Changing / Shower / Locker Support
5. Fire Pump House
6. Central Glass Deck Command / Training / Café Gallery
7. Liquid Filling / Packaging
8. Micro-ingredient Weigh / Dispense
9. Powder Handling / Packing
10. Production Hall / Wet Processing
11. Security / Reception / Visitor Arrival
12. Security Gatehouse
13. Toothpaste Production
14. Wet Wipes Production

Any unresolved target prevents full PASS.

## Gate C — Functional identity
For each remediated target, the facility's function must be visually understandable from actual geometry/layout. Generic boxes, labels, operator desks, staging blocks or object names alone are insufficient.

Particular scrutiny:
- blow molding equipment must read as blow molding;
- caps/triggers must read as assembly;
- LV/MV must read as electrical switchgear/service;
- welfare must show lockers + showers + clean/dirty logic;
- fire pump house must visibly contain credible pump/manifold equipment;
- liquid filling must visibly read as filling/packaging;
- micro-ingredient area must visibly read as weigh/dispense;
- powder area must visibly read as powder handling/packing;
- toothpaste must visibly read as toothpaste production;
- wet wipes must visibly read as converting/production;
- reception/security and gatehouse must visibly communicate their functions.

## Gate D — Wet Processing critical gate
Wet Processing must show its real process core: meaningful tanks/process equipment/platforms and process identity. Warehouse/rack imagery cannot substitute for this gate. Previously approved Wet Processing work must not be degraded.

## Gate E — Gatehouse occlusion
Security Gatehouse functional detail must no longer be substantially blocked by slab/wall/other geometry in the QA evidence. The correction must not damage surrounding architecture.

## Gate F — 12-group regression
All 12 facility groups that passed the previous owner-review pre-audit must remain intact and visually/functionally valid. Any regression is remediation failure unless separately justified and corrected before handoff.

## Gate G — Total inventory
26/26 canonical facility groups must remain accounted for after remediation. No target may be removed to eliminate a finding.

## Gate H — Approved exterior corrections
Verify no regression of the established REV005 owner corrections, especially:
- Hands of Growth state;
- two-tree removal;
- Living Wall extent;
- VIP entrance/exterior relationships.

## Gate I — Evidence quality
For every remediation target require useful visual evidence:
- orientation/wide view;
- functional/detail view;
- target visible and not materially occluded.

Automated object-name validation is supplementary only.

## Gate J — Deliverables
Require:
- remediation report;
- validation JSON;
- QA evidence;
- updated REV005 master artifacts or explicit repository-policy handling of large binaries;
- Codex log;
- before/after hashes;
- REV004 preservation evidence.

## Gate K — Stop discipline
Codex must stop after remediation/QA at:
`AWAITING_GPT_REMEDIATION_AUDIT`

It must not create the next owner-review video or final campus tour.

## GPT audit outcomes
The independent GPT audit may return:
- `PASS`
- `PASS_WITH_FINDINGS`
- `REMEDIATION_REQUIRED`
- `BLOCKED`

Codex may not self-award the GPT result.