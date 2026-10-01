# REV005 F06 — Micro-ingredient Weigh / Dispense — Historical Source Provenance

## Facility class

F06 is a Class R historical accepted-facility restoration.

Independent V05 audit accepted Micro-ingredient Weigh / Dispense as PASS and explicitly listed it in the V06 preservation set.

The historical V05 visual cue contract is:

`weigh booth, hoppers, precision balances, dosing chutes and transfer cart`

## Historical V05 selection truth

The original V05 renderer uses:

`objects_for("Micro-ingredient weigh / dispense", record)`

and reports:

`object_count = 43`

for all three V05 QA views.

Historical V03 and V04 renderer outputs both report:

`object_count = 42`

V05 adds exactly one evidence-only anchor for Micro-ingredient Weigh / Dispense.

Therefore the locked V05 historical selection is expected to resolve to 43 objects.

Expected contribution decomposition from the committed build pipeline:

- pre-V01/base selected objects: 7
- V01 additions: 12
- V02 additions: 23
- V03 additions: 0
- V04 additions: 0
- V05 evidence anchor: 1
- total: 43

This decomposition must be verified by detached replay before canonical mutation. If replay contradicts it, STOP and report the exact mismatch instead of forcing the expected count.

## Historical build geometry

### V01

Source:
`3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v01.py`

Facility origin:
- x = -5
- y = 50

Key V01 objects include:

- `RM_WEIGH_BOOTH`
  - center (-5, 52.2, 2.8)
  - dimensions 8.0 × 4.2 × 3.2 m
- `RM_WEIGH_SCALE_TABLE`
  - center (-5, 48.6, 1.8)
  - dimensions 6.0 × 1.0 × 1.2 m
- four `RM_WEIGH_BIN_*`
- four `RM_WEIGH_HOPPER_*`
- `RM_WEIGH_BALANCE`
  - center (-5, 48.1, 2.7)
  - dimensions 1.2 × 0.7 × 0.7 m
- `RM_WEIGH_TRANSFER_CART`
  - center (0, 49.5, 1.7)
  - dimensions 1.8 × 1.2 × 1.0 m

V01 contribution count: 12.

### V02

Source:
`3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v02.py`

V02 adds 23 Micro-Weigh objects:

- booth back wall
- booth side wall
- four tapered hoppers
- four hopper valves
- four dosing chutes
- balance table
- three precision balances
- three balance bowls
- transfer tote
- operator table

Key anchors:

- `V02_WEIGH_BOOTH_BACK`
  - center (-5, 53.1, 3.1)
  - dimensions 10.0 × 0.12 × 4.0 m
- `V02_WEIGH_BOOTH_SIDE`
  - center (-10, 51.1, 3.1)
  - dimensions 0.12 × 4.0 × 4.0 m
- hopper X positions: -8, -6, -4, -2
- hopper Y = 52.0
- hopper Z = 4.2
- hopper-valve Z = 3.1
- dosing chutes terminate approximately at Y=49.8, Z=2.35
- `V02_WEIGH_BALANCE_TABLE`
  - center (-5, 48.9, 1.8)
  - dimensions 7.0 × 1.0 × 1.1 m
- precision balance X positions: -7.2, -5.0, -2.8
- precision balance Y = 48.5
- precision balance Z = 2.45
- `V02_WEIGH_TRANSFER_TOTE`
  - center (0, 49.2, 1.8)
- `V02_WEIGH_OPERATOR_TABLE`
  - center (-10, 48.2, 1.7)

V02 contribution count: 23.

### V03 / V04

No Micro-Weigh geometry additions.

Historical renderer selection remains 42 objects.

### V05

Source:
`3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v05.py`

V05 does not rebuild the facility.

It adds one minimal evidence anchor:

`V05_EVIDENCE_ANCHOR_MICR`

at approximately:
- x = -5
- y = 50
- z = 1.08
- dimensions 0.2 × 0.2 × 0.12 m

V05 final selected count: 43.

## Historical V05 QA contract

Renderer:
`3d/revisions/REV005/pipeline/render_rev005_interior_remediation_v05.py`

Exact `show_only()` semantics:
- keep only selected facility objects;
- hide non-MESH/CURVE/SURFACE objects;
- additionally hide selected names containing:
  - `_LEFT`
  - `_RIGHT`
  - `_BACK`
  - `_SOFFIT`
  - `_CEILING_BEAM`

Workbench:
- 900 × 600
- lens 52 mm
- sensor 36 mm
- Studio lighting
- material color
- shadows on
- cavity on / WORLD

Historical V05 cameras:

A_WIDE:
- camera (-16, 40, 12)
- target (-5, 50, 3)

B_FUNCTIONAL:
- camera (-11, 45, 8)
- target (-5, 50, 3)

C_PROCESS_OR_DETAIL:
- camera (-3, 49, 8)
- target (-5, 50, 3)

Committed archived references:

- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_A_WIDE.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_B_FUNCTIONAL.png`
- `output/rev005-interior-remediation-v05/qa/micro_ingredient_weigh_dispense_C_PROCESS_OR_DETAIL.png`

Source replay must reproduce these references with exact decoded parity or only sparse antialias-edge differences suitable for independent GPT review.

## Historical acceptance

Independent V05 audit states:

`Micro-ingredient Weigh / Dispense | PASS | Reframed evidence shows hoppers/weigh stations/dosing layout with enough functional specificity to close the evidence-only concern.`

It is one of the six V05 facilities explicitly protected from rebuild.

Therefore F06 is a restoration task, not a redesign task.
