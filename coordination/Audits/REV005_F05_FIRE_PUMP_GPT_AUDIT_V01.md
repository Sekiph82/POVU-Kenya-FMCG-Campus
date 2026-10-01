# REV005 F05 Fire Pump House — Independent GPT Audit V01

## Verdict

`REMEDIATION_REQUIRED`

Audited execution commit:

`aab5d952ac10eb7751b12502d50547c811ada4e5`

F06 remains blocked.

## PASS gates

The following locked F05 gates are accepted from the committed evidence:

- Canonical pre-F05 Blend baseline: `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`.
- Canonical pre-F05 GLB baseline: `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`.
- Historical V01→V05 selection: 123 objects.
- Spatial split: PRIMARY Y<30 = 54; SECONDARY Y>=30 = 69.
- Contribution totals and primary/secondary contribution counts match the locked criteria.
- Exact primary destination count: 54.
- V04/V05 dimensional anchor validation: PASS.
- Historical source A/B/C decoded-pixel parity: exact, 0 differing decoded channels.
- Destination A/B/C structural parity: accepted as sparse antialias-edge-only deltas:
  - A: 149 differing channels
  - B: 13 differing channels
  - C: 23 differing channels
- Integrated LOS computation reports 9/9 clear rays for historical A, B and C.
- Required F05 evidence set and final hashes were committed.
- Final F05 hashes from the execution:
  - Blend: `E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`
  - GLB: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

These passes are preserved. R01 must not rebuild the 54-object historical source or redo already-proven source parity unless a new contradiction is found.

## Hard visual failure — integrated D evidence

The locked criteria require the integrated evidence to show the PRIMARY 54-object facility clearly, with paired pumps, piping/valves and the control panel readable, legitimate current context visible, and no material clipping/occlusion of the functional cluster.

Direct inspection of:

`output/rev005-facility-gated/F05_fire_pump/D_INTEGRATED_CONTEXT_PREVIEW_900x600.png`

does not meet that gate.

Observed:

- large horizontal overhead/roof/slab elements dominate the frame;
- the paired pump area is only partially exposed;
- the header/valve network is materially obscured;
- the control panel is not clearly readable as part of the functional cluster;
- the view therefore does not communicate the complete Fire Pump House primary system despite the 9/9 LOS sample result.

Conclusion:

`9/9 LOS != visual acceptance`.

The LOS test is a necessary geometric check, not a substitute for the locked visual-readability requirement.

## Protection-evidence inconsistency

The committed protection manifests are not internally clean enough for final acceptance.

Comparing:

- `F05_PROTECTION_BEFORE.json`
- `F05_PROTECTION_AFTER.json`

shows the protected object/category payloads and counts are otherwise stable, but the top-level quarantine summary changes:

- before: `quarantine_state.restaurant_right_wall = false`
- after: `quarantine_state.restaurant_right_wall = true`

while the recorded `V09_RESTAURANT_RIGHT_WALL` object payload itself remains the same in the two manifests.

The locked criterion is exact prior-state protection, including the Restaurant right-wall quarantine. R01 must determine whether this is:

1. a real canonical collection/visibility-state mutation, or
2. a manifest/derivation inconsistency.

Do not guess and do not silently normalize the value.

## Required remediation

F05-R01 is narrowly scoped to:

1. produce visually acceptable integrated evidence without changing F05 geometry;
2. resolve the Restaurant right-wall protection-state inconsistency with exact collection/object visibility evidence;
3. preserve all already-passed historical source, split, dimensional and parity gates.

No F06 work is authorized.

## Stop state

Successful remediation stops at:

`AWAITING_GPT_FACILITY_AUDIT_F05_R01`
