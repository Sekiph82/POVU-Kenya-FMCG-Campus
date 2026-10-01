# REV005 F06 Micro-ingredient Weigh / Dispense — Independent GPT Audit V01

## Verdict

`REMEDIATION_REQUIRED`

Audited execution commit:

`4dbcc1ce2faeb0b6e0f61a5229f50e934ef82944`

F07 remains blocked.

## PASS gates

The following F06 gates are accepted and locked:

- Exact historical V05 selection = 43 objects.
- Contribution split = BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1.
- Historical source A/B/C replay parity = exact decoded-pixel equality for all three archived references.
- Dimensional validation = PASS.
- Destination collection = exactly 43 objects.
- Destination A/B/C structural parity = PASS:
  - A: 21 differing pixels, max channel delta 8
  - B: 10 differing pixels, max channel delta 22
  - C: exact
- Prior accepted-state protection = PASS.
- Unauthorized protected object differences = 0.
- Unauthorized protected field differences = 0.
- F01-F05 accepted state remains protected.
- Canonical GLB unchanged.
- F07 was not started.

Accepted canonical F06 state after M08.36:

Blend:
`BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`

GLB:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

R01 must preserve these already-passed gates and must not rebuild or replace the 43-object historical facility.

## Integrated visual failure

The locked F06 criteria require the integrated current-context evidence to make the complete workflow visibly readable, including:

- weigh booth/enclosure;
- hopper row;
- hopper valves/dosing path;
- precision balance stations;
- balance table/workflow;
- transfer tote/cart;
- operator/service access organization.

Direct inspection of:

`output/rev005-facility-gated/F06_micro_weigh/F06_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png`

and the identical selected candidate:

`F06_CANDIDATE_FRONT_LEFT_900x600.png`

shows that the selected `FRONT_LEFT` camera does not satisfy the complete visual-readability gate.

Observed:

- the left-side hopper/dosing/balance workflow is readable;
- the camera obtains 9/9 LOS to the chosen ray samples;
- however, the transfer tote/cart workflow is materially cropped at the right edge;
- the operator/service access organization is only fragmentarily represented at the bottom/right edges;
- the full four-hopper / downstream-transfer relationship is not communicated as one coherent integrated process view;
- the visible wall label must not substitute for label-blind process readability.

The alternative `MID_LEFT` candidate is tighter and crops even more of the workflow.

Therefore:

`9/9 LOS != COMPLETE INTEGRATED VISUAL ACCEPTANCE`.

## Required remediation

F06-R01 is camera/evidence-only unless a new contradiction is discovered.

Required:

1. keep canonical F06 geometry and all accepted visibility/protection state unchanged;
2. preserve all 43-object historical source, dimensional and A/B/C parity PASS gates;
3. search a wider integrated camera space, including wider lenses and farther front-left/front-oblique positions;
4. render enough candidate previews to prove the full workflow in one current-context view;
5. select a D view only when the hopper → dosing → precision balance → transfer tote/cart → operator/access relationship is all visibly understandable;
6. use no QA-only hiding or neighbor mutation.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F06_R01`
