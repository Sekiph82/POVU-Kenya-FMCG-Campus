# REV005 INTERIOR REMEDIATION V01 — GPT EXECUTION PROMPT

## Mission
Remediate the 14 findings from `REV005_OWNER_INTERIOR_REVIEW_V01` inside REV005, without touching REV004 and without starting the final tour.

## Evidence / source of truth
Read before editing:
- `coordination/Logs/REV005_OWNER_INTERIOR_REVIEW_V01_CODEX_LOG.md`
- `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_REVIEW_INDEX.md`
- `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_COVERAGE_AUDIT.md`
- `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_REVIEW_VALIDATION.json`
- `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json`
- `3d/revisions/REV005/REV005_INTERIOR_AUDIT.md`
- canonical REV005 `.blend` and `.glb`

The independent GPT audit result is `REMEDIATION_REQUIRED` because 14 of 26 facility groups did not close the functional-detail/visibility gate.

## Immutable boundaries
- REV004 is frozen and must remain untouched.
- Work only on REV005.
- Preserve the 12 already-passing facility groups unless a strictly necessary shared-scene adjustment is required.
- Do not create REV006.
- Do not start the final campus tour.
- Do not reintroduce East Glass Deck Access or West Glass Deck Access in presentation/callout material.
- Do not replace real functional modeling with labels, generic boxes, staging props, or camera tricks.

## Required remediation targets
Close all 14 findings:
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

## Definition of remediation
For each target, inspect the actual geometry and the finding first. Determine whether the problem is:
A. functional geometry/detail genuinely insufficient,
B. existing geometry is sufficient but placement/occlusion makes it unreadable,
C. review camera/evidence failed to show already-sufficient geometry,
or a combination.

Then apply the minimum correct fix.

If geometry is genuinely insufficient, add credible functional equipment/furniture/layout appropriate to the established POVU facility and project evidence. Do not create decorative placeholders merely to satisfy object counts.

If geometry already exists and is correct, do not rebuild it unnecessarily. Fix only the visibility/placement issue and prove it with new evidence.

## Facility-specific closure requirements
### Bottle Blow Molding
Principal blow-molding equipment/process identity must be visually unmistakable, not merely operator/staging content.

### Caps and Trigger Assembly
Show/model the actual cap/trigger assembly functional equipment and work flow clearly enough to distinguish it from generic production staging.

### Electrical / LV-MV Room
Electrical panel/switchgear/service identity must be clearly readable and functionally credible.

### Employee Changing / Shower / Locker Support
Lockers, showers and clean/dirty separation/circulation must be visually understandable together.

### Fire Pump House
Pump-house identity must be clear through credible pump/manifold/service equipment rather than a sparse generic room.

### Central Glass Deck Command / Training / Café Gallery
The command/training/café-gallery functions must be visually intelligible. Preserve the approved Glass Deck architecture. Do not recreate East/West Glass Deck Access presentation elements.

### Liquid Filling / Packaging
Actual filling/packaging-line identity must be clearly visible, including the meaningful line/process arrangement already established by project scope.

### Micro-ingredient Weigh / Dispense
Weighing/dispensing functional identity must be clear, not just staged containers/operator furniture.

### Powder Handling / Packing
Powder handling/packing equipment and process identity must be clearly legible.

### Production Hall / Wet Processing
This is critical. Preserve the previously approved Wet Processing work. Evidence must clearly show the process core, tanks/equipment/platforms and actual wet-processing identity. Do not substitute warehouse racks/storage views.

### Security / Reception / Visitor Arrival
Show/model a credible visitor/security reception interior and circulation rather than frontage alone.

### Security Gatehouse
Remove the visual obstruction problem and make the gatehouse's functional interior/equipment clearly visible. Do not damage surrounding architecture.

### Toothpaste Production
Make toothpaste-production identity unmistakable through credible process/filling/production equipment consistent with the established campus programme.

### Wet Wipes Production
Make the wet-wipes converting/production-line identity unmistakable, not generic production blocks.

## Preserve owner-approved exterior corrections
Do not regress:
- Hands of Growth correction state in REV005
- removal of the two specified obstructing trees
- corrected Living Wall extent
- approved VIP entrance/exterior architecture
- other REV005 owner corrections

If these are discovered to have regressed, report them. Do not expand scope beyond restoring the already-approved REV005 state.

## QA evidence
Create a new remediation QA package with, at minimum, two useful visual proofs for each of the 14 targets:
- A: orientation/wide
- B: functional/detail

The actual function must be visible. Labels do not count as proof.

Also perform regression checks on all 12 previously passing facility groups to ensure remediation did not break them.

## Required artifacts
Create/update under a dedicated remediation output folder:
- `output/rev005-interior-remediation-v01/REV005_INTERIOR_REMEDIATION_V01_REPORT.md`
- `output/rev005-interior-remediation-v01/REV005_INTERIOR_REMEDIATION_V01_VALIDATION.json`
- `output/rev005-interior-remediation-v01/qa/` with representative evidence for all 14 remediated targets plus regression evidence as practical
- updated canonical REV005 master `.blend` and exported `.glb` in the existing REV005 revision folder
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V01_CODEX_LOG.md`

Record before/after SHA-256 hashes for canonical REV005 master artifacts and prove REV004 remained unchanged.

## Completion gate
Do not self-close based on object names or export success.

Codex pre-validation may pass only if:
- 14/14 remediation targets have clear functional visual proof;
- 12/12 previously passing groups have no regression;
- 26/26 total groups remain present;
- Wet Processing process core is visibly correct;
- Security Gatehouse is not substantially occluded;
- no East/West Glass Deck Access presentation references are reintroduced;
- REV004 is unchanged;
- no final tour is created.

## Git / publication
Commit and push lightweight scripts, reports, QA evidence and log to `main`. Follow repository policy for large binary masters; keep required local paths explicit if binaries are not committed.

The final response must provide:
- status
- 14/14 remediation closure count
- regression count
- REV005 final local `.blend` and `.glb` paths
- commit SHA
- full GitHub URL to `coordination/Logs/REV005_INTERIOR_REMEDIATION_V01_CODEX_LOG.md`

## Stop gate
STOP after remediation and QA.

Do not create another owner-review video yet. Do not create the final tour.

Final state:
`AWAITING_GPT_REMEDIATION_AUDIT`

Locked audit criteria:
`coordination/Audits/REV005_INTERIOR_REMEDIATION_V01_GPT_AUDIT_CRITERIA.md`

Codex must not edit the locked audit criteria.