# F01 HISTORICAL PIPELINE REPLAY PROVENANCE — V03

## Why the second attempt stopped

Second state:
`BLOCKED_F01_SOURCE_OBJECT_COUNT`

This stop was correct.

The Git-restorable base Blend contains only the original Caps/Trigger subset selected by the owner-review inventory:
- inventory record: 9 names
- V05 label exclusion removes `SAFETY_SIGN` and `REV005_LABEL_CAPS_TRIGGERS`
- base visible selection: **7 objects**

The accepted V05 evidence had **76 selected objects** because Caps/Trigger geometry accumulated through the historical local pipeline before V05 rendering.

## Exact 76-object provenance

### Base committed REV005: 7 objects

Historical inventory record:
1. `REV005_Caps_Triggers_OPERATOR_STATION_BODY`
2. `REV005_Caps_Triggers_OPERATOR_STATION_PANEL`
3. `REV005_Caps_Triggers_SAFETY_EYEWASH`
4. `REV005_Caps_Triggers_SAFETY_PPE`
5. `REV005_Caps_Triggers_SAFETY_SIGN` — excluded by V05 label filter
6. `REV005_Caps_Triggers_STAGING_0`
7. `REV005_Caps_Triggers_STAGING_1`
8. `REV005_Caps_and_trigger_assembly_FLOOR`
9. `REV005_LABEL_CAPS_TRIGGERS` — excluded by V05 label filter

Selected visible base count = **7**.

### V01 Caps function: +21 objects

From `build_rev005_interior_remediation_v01.py::caps()`:

- `RM_CAPS_ROTARY_BOWL` = 1
- `RM_CAPS_BOWL_CENTER` = 1
- `RM_CAPS_FEED_TRACK` = 1
- `RM_TRIGGER_FEEDER` = 1
- `RM_CAP_TRIGGER_ASSEMBLY_LINE_BED` = 1
- `RM_CAP_TRIGGER_ASSEMBLY_LINE_ROLLER_0..4` = 5
- `RM_CAP_TRIGGER_ASSEMBLY_LINE_GUARD_A/B` = 2
- `RM_TRIGGER_PICK_PLACE_0..3` = 4
- `RM_CAP_FEEDER_0..3` = 4
- `RM_CAPS_REJECT_STATION` = 1

V01 contribution = **21**.

### V02 Caps function: +47 objects

From `build_rev005_interior_remediation_v02.py::caps()`:

- `V02_CAPS_BOWL_FEEDER` = 1
- `V02_CAPS_BOWL_RIM` = 1
- `V02_CAPS_BOWL_TRACK` = 1
- `V02_TRIGGER_MAGAZINE` = 1
- `V02_TRIGGER_SLOT_0..4` = 5
- `V02_CAP_TRIGGER_CAROUSEL` = 1
- `V02_ASSEMBLY_NEST_0..5` = 6
- `V02_CAP_COMPONENT_0..5` = 6
- `V02_TRIGGER_COMPONENT_0..5` = 6
- `V02_PICK_HEAD_COLUMN_0..2` = 3
- `V02_PICK_HEAD_0..2` = 3
- `V02_PICK_HEAD_DROP_0..2` = 3
- `V02_CAP_TRIGGER_OUTFEED_FRAME` = 1
- `V02_CAP_TRIGGER_OUTFEED_ROLLER_0..6` = 7
- `V02_CAP_TRIGGER_OUTFEED_SIDE_A/B` = 2

V02 contribution = **47**.

### V03 and V04: +0 Caps objects

V03 focuses Bottle, Liquid, Toothpaste, Wet Wipes, Glass Deck plus Restaurant/Daycare and does not add Caps/Trigger geometry.

V04 does not add Caps/Trigger geometry.

### V05 evidence anchor: +1

`V05_EVIDENCE_ANCHOR_CAPS`
- location: `(52,31,1.08)`
- dimensions: `(0.2,0.2,0.12)`
- facility: `Caps and Trigger Assembly`

V05 contribution = **1**.

## Total

`7 + 21 + 47 + 0 + 0 + 1 = 76`

This exactly explains the V05 historical QA object count.

## Historical pipeline replay

The authoritative reconstruction method is:

1. Create a detached **system-temp Git worktree** at V05 evidence commit `420038365847de763d64c8583a9e31ac5a6bd677`.
2. Verify initial temp Blend SHA-256:
   `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
3. In that temp worktree, run the original historical build scripts, in order:
   - V01
   - V02
   - V03
   - V04
   - V05
4. Do not patch their modeling code.
5. Run the original V05 renderer in that temp worktree.
6. Confirm Caps/Trigger selection = 76.
7. Confirm V05 archived A/B/C image hashes byte-for-byte.

Historical intermediate Blend hashes are diagnostic checkpoints:
- Initial: `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
- after V01: `484E495E9F2689A73BE4DDF7297FEAF96D3227B0E2696A5174A6942E3625D26F`
- after V02: `9BEE6F87D7762BC415F15047DC287D7B591C44C83FF8E39C226E6A07FD480B0C`
- after V03: `9E9A63A2D7AAFA5667CD0A41DFDE746CB2F2A7751F29DAB259CA30E8A99A238F`
- after V04: `EC1B7ABDB86A8FCF1443E780497B49FDDD4268B57EC48106D6D2FDB2D00008BB`
- after V05: `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

These whole-Blend hashes are diagnostic because Blender serialization can be environment-sensitive. The **hard equivalence gate** is:
- 76 selected objects;
- exact archived A/B/C PNG hashes.

## Visibility semantics

Important:

V02 hides V01 focused objects. V05 renderer's `show_only(objs)` overrides `hide_render` and renders all 76 selected objects together.

Therefore destination restoration must reproduce the **V05 evidence-visible state**:
- all 76 selected Caps/Trigger objects visible for final facility operation/evidence;
- labels/signs remain excluded;
- do not preserve a hidden state that would remove the V01 layer from the accepted visual result.

## Archived V05 image SHA-256

Verified directly from GitHub binary files:

- A_WIDE:
  `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
- B_FUNCTIONAL:
  `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
- C_PROCESS_OR_DETAIL:
  `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`
