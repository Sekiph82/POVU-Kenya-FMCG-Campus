# M08.40 — F06-X03 DUAL-VIEW EVIDENCE CLOSURE

## Scope

Execute F06-X03 only.

This is an evidence-only closure task.

The independent X02 audit concluded that the remaining F06 issue is no longer a geometry defect or GLB defect. The prior single-frame integrated requirement is superseded for F06 only by a complementary two-view proof.

Do not begin F07.

Do not change the Blend.
Do not export a new GLB.
Do not change geometry.
Do not widen quarantine.
Do not alter saved visibility.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F06_X02_GPT_AUDIT.md`
4. `coordination/Audits/REV005_F06_X01_GPT_AUDIT.md`
5. `coordination/Logs/REV005_F06_X02_WIDE_FOV_GLB_PARITY_CODEX_LOG.md`
6. all F06 / R01 / X01 / X02 evidence

## Safe synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If unexpected local changes exist, STOP without discarding them.

Fetch and fast-forward-only to current `origin/main`.

No reset.
No rebase.
No force.
No second Desktop copy.

Re-read root `TASKS.md`.

It must authorize:

`M08.40 — Facility-Gated F06-X03 dual-view evidence closure`

If not, STOP before work.

## Locked canonical state

Blend SHA-256 must remain exactly:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

GLB SHA-256 must remain exactly:

`948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`

If either differs before work:

STOP `BLOCKED_F06_X03_CANONICAL_BASELINE_MISMATCH`.

No canonical file mutation is authorized.

## Locked F06 state

Accepted destination collection:

`REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`

Required:
- count = 43
- contribution split = BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1
- all accepted object signatures unchanged

Exactly seven X01 quarantine objects remain saved and unchanged:

1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

No eighth quarantine object is permitted.

## Superseded single-frame gate

Do not attempt to force all F06 functional cues into one image.

Do not restart broad camera searches.

F06 closure now requires two complementary current-context integrated views from the exact same locked canonical state.

## View D — Process / Transfer Integrated Overview

Use X02 Candidate 01 as the preferred seed:

- camera = (8,43,6)
- target = (-4,50,2.8)
- lens = 20 mm
- sensor width = 36 mm
- prior LOS = 9/9

You may use this exact camera or a very small evidence-only refinement if direct rendered comparison clearly improves framing.

D must clearly show:
- weigh booth/enclosure;
- substantially complete four-hopper row;
- hopper outlets/valves;
- dosing paths;
- precision-balance stations;
- balance table;
- transfer tote/cart;
- coherent hopper → dosing → balance → transfer relationship;
- legitimate current context.

D does not need to prove the operator/service zone.

Required outputs:

- `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_CONTEXT.png` at 1440×960
- `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_CONTEXT_PREVIEW_900x600.png`

## View E — Operator / Service / Access Proof

This view has a different job.

Search only for a clean operator/service/access angle.

Do not require the entire hopper row.

E must clearly show:
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`;
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_PANEL`;
- `V02_WEIGH_OPERATOR_TABLE`;
- operator/service zone;
- floor/access organization around the working area;
- at least one safety/service cue where practically visible:
  - eyewash,
  - PPE station,
  - staging,
  - service workspace;
- at least one shared process anchor that links E spatially to D:
  - transfer tote,
  - balance table,
  - booth wall,
  - one or more hopper/dosing elements.

The shared anchor must make it visually clear that D and E are complementary views of the same accepted F06 facility.

## E camera search

Do a focused search only.

Render at least 12 and at most 30 900×600 candidates.

Bias the camera toward the front/service side around the operator station at approximately:
- X = -5
- Y = 47.6
- Z = 2.0

and operator table at the historical V02 service side.

Test both:
- front-left/service-oblique positions;
- front-right/service-oblique positions;
- moderate eye heights 3.5–7 m;
- lenses 20/24/28/35/40 mm.

Do not use:
- QA-only hiding;
- temporary quarantine;
- clipping tricks;
- geometry mutation.

Record every E candidate in:

`F06_X03_OPERATOR_ACCESS_CANDIDATES.json`

For every candidate record:
- camera XYZ;
- target XYZ;
- lens;
- camera-outside-geometry;
- operator station body visible;
- operator panel visible;
- V02 operator table visible;
- access/service zone readable;
- safety/service cue visible;
- shared process anchor visible;
- structure dominance/clipping;
- preview path.

## E required final evidence

Select the strongest valid E candidate.

Produce:

- `E_OPERATOR_ACCESS_CONTEXT.png` at 1440×960
- `E_OPERATOR_ACCESS_CONTEXT_PREVIEW_900x600.png`

## Pair validation

Create:

`F06_X03_DUAL_VIEW_VALIDATION.json`

The JSON must explicitly prove:

### D
- process_overview = true
- booth = true
- hopper_row = true
- valves = true
- dosing = true
- precision_balances = true
- balance_table = true
- transfer_tote = true
- coherent_process_relationship = true

### E
- operator_station_body = true
- operator_station_panel = true
- operator_table_or_service_zone = true
- access_organization = true
- service_or_safety_cue = true
- shared_process_anchor = true

### Pair
- same_canonical_blend_state = true
- same_saved_visibility_state = true
- same_locked_seven_quarantines = true
- qa_only_hiding_used = false
- neighbor_mutation = false
- geometry_mutation = false
- complete_original_F06_visual_contract_covered_by_pair = true

## Regression

Create:

`F06_X03_REGRESSION.json`

Require:
- Blend hash unchanged;
- GLB hash unchanged;
- F06 destination count = 43;
- contribution split = 7/12/23/0/0/1;
- all 43 F06 signatures unchanged;
- seven X01 quarantines unchanged;
- prior F01-F05 protection unchanged;
- F07 not started.

## If no E view exists

If a focused operator/access view cannot show the required service-side evidence without geometry or new quarantine:

STOP:

`BLOCKED_F06_X03_OPERATOR_ACCESS_EVIDENCE`

Do not mutate the model.

Publish the candidate evidence and stop for GPT direction.

## Required log

Write:

`coordination/Logs/REV005_F06_X03_DUAL_VIEW_EVIDENCE_CLOSURE_CODEX_LOG.md`

Include:
- locked hashes;
- D camera;
- E search summary;
- selected E camera;
- pair coverage;
- regression;
- stop marker.

## Git scope

Commit/push only:
- X03 D/E renders and previews;
- X03 candidate/validation/regression JSON;
- X03 log.

Do not commit changed Blend.
Do not commit changed GLB.
Do not edit root `TASKS.md`.
Do not edit prior audits.

Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06_X03`
