# REV005 FACILITY F01 — CAPS & TRIGGER ASSEMBLY — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex  
**Independent auditor:** GPT  
**Source class:** R — exact V05 restoration

Codex MUST NOT edit this file.

## Source truth

Authoritative accepted source:
- commit: `420038365847de763d64c8583a9e31ac5a6bd677`
- Blend path: `3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
- expected V05 Blend SHA-256: `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`
- source custom property matcher: `facility == "Caps and Trigger Assembly"`
- historical V05 visible object count: **76**
- accepted visible cues: **bowl feeders, cap/trigger feed tracks, guarded assembly conveyor, reject station**

Source V05 evidence:
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_A_WIDE.png`
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`
- `output/rev005-interior-remediation-v05/qa/caps_and_trigger_assembly_C_PROCESS_OR_DETAIL.png`

## Gate A — historical source integrity

PASS requires:
- V05 temp Blend extracted from the exact commit without checkout/reset;
- SHA-256 matches the expected V05 hash;
- source object manifest created before current-model mutation;
- all source objects matching the facility property identified;
- parent/material/data dependencies captured.

If source manifest is materially different from the historical ~76-object evidence, Codex must STOP and report the discrepancy rather than guessing.

## Gate B — exact restoration

PASS requires:
- broken/current Caps & Trigger facility geometry removed or render-disabled only for this facility;
- complete V05 facility geometry appended into current REV005;
- each restored object's source world transform retained;
- source object parent relationships retained;
- source mesh/curve data and material dependencies retained;
- no unrelated V05 facility objects imported;
- no global unhide of retired legacy objects.

Object count alone is never acceptance.

## Gate C — visual identity

All required cues must be visually readable without labels:
- bowl/feed equipment;
- cap/trigger feed tracks;
- guarded assembly conveyor/cell;
- multiple assembly/work positions;
- reject station.

The restored result must visually match or exceed the accepted V05 evidence.

## Gate D — locked camera proof

First three QA cameras use the historical V05 coordinates:

- A: location `(60, 18, 13)`, target `(52, 31, 3)`
- B: location `(54, 24, 8)`, target `(52, 31, 3)`
- C: location `(46, 26, 8)`, target `(52, 31, 3)`
- lens: **52 mm**
- sensor width: **36 mm**
- render: **1440×960 PNG**

Only a small camera adjustment is allowed if a current non-facility collision obstructs the historical view. Any adjustment must be documented numerically.

## Gate E — scene integration

The restored facility must occupy its historical world location. No translation/rotation/scale of the complete facility is allowed to "make the camera work".

No collision with unrelated current facilities may be created.

## Gate F — evidence

Required files:
- source manifest JSON;
- destination restoration manifest JSON;
- baseline hash JSON;
- final hash JSON;
- A/B/C QA PNGs;
- integrated-context PNG;
- Codex log.

## Gate G — stop discipline

Codex must stop at exactly:
`AWAITING_GPT_FACILITY_AUDIT_F01`

No Daycare or any other facility work may begin.

Independent outcomes:
- PASS
- REMEDIATION_REQUIRED
- BLOCKED
