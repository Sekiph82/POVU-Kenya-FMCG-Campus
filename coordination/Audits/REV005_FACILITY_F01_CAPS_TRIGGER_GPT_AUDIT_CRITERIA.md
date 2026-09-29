# REV005 FACILITY F01 — CAPS & TRIGGER ASSEMBLY — LOCKED GPT AUDIT CRITERIA V03

**Executor:** Codex  
**Independent auditor:** GPT  
**Method:** deterministic historical pipeline replay + exact facility transfer

Codex MUST NOT edit this file.

## Gate A — no canonical mutation before reconstruction proof

Current canonical V09 baseline must remain unchanged until all source-reconstruction gates pass:
- Blend: `46D427377C315FF8838CBF6917DD469E3F88D14F49E52BE0C18F8C0CFE3D68E8`
- GLB: `F09D1E5F4A3581509C33453C88B576A67BB6D2CAFDC08532B05F342BC18F6DCF`

## Gate B — temp worktree source

Create detached worktree under OS/system temp, never Desktop:

Commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Initial canonical temp Blend SHA-256:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

## Gate C — exact historical replay

Inside temp worktree run, in order, the historical scripts from that worktree:

1. `build_rev005_interior_remediation_v01.py`
2. `build_rev005_interior_remediation_v02.py`
3. `build_rev005_interior_remediation_v03.py`
4. `build_rev005_interior_remediation_v04.py`
5. `build_rev005_interior_remediation_v05.py`

No modeling-code edits.

Expected whole-Blend checkpoint hashes are diagnostic and must be logged:
- V01 `484E495E9F2689A73BE4DDF7297FEAF96D3227B0E2696A5174A6942E3625D26F`
- V02 `9BEE6F87D7762BC415F15047DC287D7B591C44C83FF8E39C226E6A07FD480B0C`
- V03 `9E9A63A2D7AAFA5667CD0A41DFDE746CB2F2A7751F29DAB259CA30E8A99A238F`
- V04 `EC1B7ABDB86A8FCF1443E780497B49FDDD4268B57EC48106D6D2FDB2D00008BB`
- V05 `B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

A whole-Blend checkpoint difference is a diagnostic finding, not an automatic fail, provided the hard facility-equivalence gates below pass.

## Gate D — exact 76-object provenance

After V05 replay, use the original V05 renderer selection logic.

Required selected Caps/Trigger count:
**76**

Composition must reconcile exactly:
- 7 base visible objects
- 21 V01 Caps objects
- 47 V02 Caps objects
- 1 V05 evidence anchor
- 0 V03
- 0 V04

Any count/composition mismatch => STOP before canonical mutation.

## Gate E — exact source render equivalence

Run original historical:
`render_rev005_interior_remediation_v05.py`

Required source images must match archived V05 PNG SHA-256 byte-for-byte:

- A:
  `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
- B:
  `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
- C:
  `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

All three required.

## Gate F — exact 76-object transfer

Transfer exactly the 76 selected source objects and dependencies into the current canonical REV005.

Before append:
- inventory and remove/unlink only current Caps/Trigger representations;
- no other facility may change.

Destination:
`REV005_FG_F01_CAPS_TRIGGER_ACCEPTED_V05_REPLAY`

Geometry parity tolerances:
- location <= 0.001 m per axis
- rotation <= 0.0001 rad per axis
- scale <= 0.0001 per axis
- dimensions <= 0.001 m per axis

All 76 destination objects must be visible in the accepted evidence/operational state:
- `hide_render=False`
- `hide_viewport=False`

Labels/signs are not part of the 76 and remain excluded.

## Gate G — destination 900×600 parity proof

With only the restored 76 facility objects visible and exact historical V05 Workbench/camera settings, render destination parity A/B/C at 900×600.

Required destination parity PNG hashes must again equal the same archived values:

- A `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
- B `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
- C `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

If any destination parity hash differs, F01 is not accepted as an exact restoration.

## Gate H — human review QA

Then render 1440×960:
- A_CONTEXT: loc (60,18,13), target (52,31,3), lens 52
- B_FUNCTIONAL: loc (54,24,8), target (52,31,3), lens 52
- C_DETAIL: loc (46,26,8), target (52,31,3), lens 52
- D_INTEGRATED_CONTEXT: A camera with normal current scene visibility

F01 must visibly show:
- bowl/feed equipment;
- cap/trigger feed tracks;
- guarded assembly conveyor/cell;
- multiple work positions/fixtures;
- reject station.

## Gate I — integration/source protection

- REV004 unchanged
- no REV006
- no second Desktop root
- no `.hiveai`
- no tour/video
- no other facility mutation
- no global unhide
- canonical root unchanged
- TASKS and criteria unchanged by Codex

## Gate J — exact artifacts

Required:
- `F01_BASELINE_HASHES.json`
- `F01_REPLAY_CHECKPOINTS.json`
- `F01_REPLAY_SOURCE_MANIFEST.json`
- `F01_CURRENT_PRE_RESTORE_MANIFEST.json`
- `F01_DESTINATION_MANIFEST.json`
- `F01_SOURCE_RENDER_HASHES.json`
- `F01_DESTINATION_PARITY_HASHES.json`
- `F01_FINAL_HASHES.json`
- `F01_VALIDATION.json`
- source A/B/C replay PNGs
- destination parity A/B/C PNGs
- final A/B/C/D 1440×960 PNGs
- exact Codex log

## Gate K — stop

Stop exactly at:
`AWAITING_GPT_FACILITY_AUDIT_F01`

No Facility 02 work.
