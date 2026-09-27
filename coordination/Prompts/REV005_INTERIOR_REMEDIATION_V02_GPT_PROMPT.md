# REV005 INTERIOR REMEDIATION V02 — GPT EXECUTION PROMPT

## Status entering this task
Previous independent GPT visual audit result: `REMEDIATION_REQUIRED`.

REV005 V01 structural/pre-validation claims are not sufficient for acceptance. The attached/produced QA renders were visually inspected. This task is a focused visual-quality remediation, not a rebuild of the campus.

## Mission
Improve only the visually weak REV005 interior areas identified by the independent GPT audit, regenerate honest QA evidence, preserve all already-good work, and stop for another independent GPT audit.

## Source material
Read before editing:
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V01_CODEX_LOG.md`
- `output/rev005-interior-remediation-v01/REV005_INTERIOR_REMEDIATION_V01_REPORT.md`
- `output/rev005-interior-remediation-v01/REV005_INTERIOR_REMEDIATION_V01_VALIDATION.json`
- all V01 QA target and regression PNGs
- canonical REV005 `.blend` and `.glb`

## Independent GPT visual findings
The following remain visually insufficient and must be remediated:

1. **Bottle Blow Molding**
   - Existing machine/conveyor presence is not enough.
   - Make the principal blow-molding process visually unmistakable as a blow-molding line.

2. **Caps & Trigger Assembly**
   - Current conveyor/stations read too generically.
   - Make cap/trigger feeding, assembly and handling visually understandable.

3. **Liquid Filling / Packaging**
   - Current line is too simplified/generic.
   - Strengthen recognisable filling/capping/labeling/packing line identity and coherent process flow.

4. **Micro-ingredient Weigh / Dispense**
   - Current equipment is too abstract.
   - Make weighing, controlled dispensing/dosing and operator workflow visually legible.

5. **Toothpaste Production**
   - Must not look like generic process equipment.
   - Strengthen toothpaste-specific process/filling identity consistent with the established campus programme.

6. **Wet Wipes Production**
   - Must not resemble generic production blocks or the toothpaste area.
   - Strengthen recognisable wet-wipes converting/folding/wetting/packing-line identity.

7. **Central Glass Deck Command / Training / Café Gallery**
   - V01 QA evidence is not acceptable.
   - Geometry reads dark, fragmented and/or visually disconnected.
   - Correct actual geometry/material/placement if necessary, then provide clear evidence showing a coherent, usable command/training/café gallery interior.
   - Do NOT reintroduce East Glass Deck Access or West Glass Deck Access callouts/presentation elements.

## QA camera/evidence remediation
Some regression evidence was too weak even where the model may be correct.

At minimum, regenerate useful evidence for:
- Restaurant / POVU Café / kitchen
- Daycare / crèche
- any other regression view that is empty, badly framed, heavily occluded or does not actually prove the facility.

Do not modify good geometry merely because a bad camera failed to show it. Fix the camera/evidence when geometry is already sufficient.

## Areas considered visually acceptable in V01
Do not unnecessarily rebuild these. Preserve them and regression-check them:
- Production Hall / Wet Processing
- Electrical / LV-MV Room
- Fire Pump House
- Employee Changing / Shower / Locker Support
- Security / Reception / Visitor Arrival
- Security Gatehouse

Also preserve all other previously passing facility groups unless a strictly necessary shared-scene correction is required.

## Exterior / revision protection
- REV004 is frozen. Do not touch it.
- Work only in REV005.
- Do not create REV006.
- Preserve approved Hands of Growth state.
- Preserve removal of the two owner-specified trees.
- Preserve corrected Living Wall extent.
- Preserve VIP entrance/exterior relationships.
- Do not reintroduce East/West Glass Deck Access presentation references.
- Do not start the final campus tour.

## Modeling standard
This is not an object-count exercise.

The interior must communicate its real function visually to a non-technical viewer without depending on labels or object names. Use credible machine silhouettes, process sequence, functional relationships, operator/service clearances and facility-specific details. Avoid generic cubes, decorative placeholders, duplicated generic machinery or superficial prop inflation.

Keep the established low-poly POVU architectural language while raising functional specificity.

## QA requirements
Create a new package under:
`output/rev005-interior-remediation-v02/`

For each of the 7 focused remediation targets provide at least:
- `A_WIDE`: readable orientation/context view
- `B_FUNCTIONAL`: close functional/process view
- `C_PROCESS` where needed to prove the process sequence

Evidence must be well lit, correctly framed, non-empty and materially unobstructed.

Regenerate corrected regression evidence for Restaurant/Café and Daycare, plus any other visibly weak regression proof discovered during the run.

Run regression validation across all 26 canonical facility groups.

## Required deliverables
- `output/rev005-interior-remediation-v02/REV005_INTERIOR_REMEDIATION_V02_REPORT.md`
- `output/rev005-interior-remediation-v02/REV005_INTERIOR_REMEDIATION_V02_VALIDATION.json`
- `output/rev005-interior-remediation-v02/qa/`
- updated canonical REV005 `.blend`
- updated canonical REV005 `.glb`
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V02_CODEX_LOG.md`

Record before/after SHA-256 hashes and prove REV004 remains unchanged.

## Completion gate
Codex may hand off only when:
- all 7 focused visual findings have credible functional evidence;
- Restaurant/Café and Daycare evidence clearly shows their actual interiors;
- all 26 canonical facility groups remain present;
- the six V01 areas explicitly accepted by GPT remain intact;
- approved exterior corrections remain intact;
- REV004 remains unchanged;
- no final tour or REV006 is created.

Do not self-award final visual acceptance.

## Git / publication
Commit and push lightweight scripts, reports, QA evidence and log to `main` according to repository policy. Keep local paths explicit for large binary artifacts if they are not committed.

Final response must include:
- status
- focused remediation closure count
- 26-group regression result
- canonical REV005 `.blend` and `.glb` local paths
- commit SHA
- full GitHub URL to the V02 Codex log

## STOP GATE
STOP after V02 remediation and QA.

Do not create an owner-review video yet.
Do not create the final tour.

Final state:
`AWAITING_GPT_REMEDIATION_AUDIT_V02`
