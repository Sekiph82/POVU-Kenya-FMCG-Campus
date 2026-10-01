# REV005 F06-X01 — Independent GPT Audit

## Verdict

`REMEDIATION_REQUIRED_X02`

Audited execution commit:

`13569d4000751e71b38e9b6969bcd182144f9ff0`

## Accepted X01 work

The seven-object targeted cross-facility quarantine is accepted.

Exact authorized changed objects:
- V09_TOOTHPASTE_BACK_WALL
- V09_TOOTHPASTE_FLOOR
- V09_TOOTHPASTE_SOFFIT
- V09_WET_WIPES_BACK_WALL
- V09_WET_WIPES_FLOOR
- V09_WET_WIPES_LEFT_WALL
- V09_WET_WIPES_SOFFIT

The committed diff proves:
- exactly seven changed objects;
- no added/removed objects;
- no collection-link changes;
- no transform/dimension/material/data/parent changes;
- all F01-F06 protected signatures PASS;
- F06 accepted count remains 43.

The canonical Blend after accepted X01 quarantine is therefore locked for X02:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

No wider quarantine is authorized.

## Camera finding

X01 correctly stopped rather than falsely passing.

However the evidence does not prove that the integrated view is impossible.

Candidate 32:
- camera (8,43,6)
- target (-4,50,2.8)
- lens 52 mm
- LOS 9/9
- no blockers

Direct visual review shows:
- hopper row readable;
- hopper valves readable;
- dosing paths readable;
- precision-balance line readable;
- balance table readable;
- yellow transfer tote/cart is present but clipped near the lower/right framing boundary;
- operator/service side is present toward the left but not fully established in the single frame.

This is now primarily a field-of-view/framing problem.

The X01 search was restricted to 35/40/45/52 mm lenses. It did not test 20/24/28/30/32 mm lenses around the successful right/front-oblique camera family.

Therefore no further geometry or quarantine change is justified before a dedicated wide-FOV evidence pass.

## GLB export finding

The X01 attempted `use_visible=True` GLB export is rejected as a canonical export method for this state.

Evidence:
- locked baseline GLB nodes: 10,605
- attempted export nodes: 2,019
- delta: -8,586 nodes
- F06 names retained: 31/43
- 12 accepted F06 names omitted

This failure is caused by visibility-based export filtering, not by missing canonical F06 geometry. The Blend still has all 43 accepted F06 objects and their protected signatures pass.

The failed export was correctly discarded and the locked GLB restored.

X02 must not repeat `use_visible=True`.

## X02 GLB strategy

Use the current locked canonical GLB as the structural export membership reference.

Goal:
- preserve the existing canonical GLB node-name set;
- remove exactly the seven accepted X01 quarantine object names;
- preserve all other baseline GLB node names;
- include all 43 accepted F06 destination names.

A deterministic temporary export staging state may be used in memory only:
- read baseline GLB node names;
- resolve those exact object names in the canonical Blend;
- exclude only the seven X01 quarantine names;
- temporarily make the export set selectable/exportable without saving visibility changes;
- export with explicit selection-based membership rather than `use_visible=True`;
- restore all temporary state after export;
- never save the temporary export visibility/selection state into the Blend.

Expected structural target if baseline node/object mapping is one-to-one:
- 10,598 nodes = 10,605 - 7

If exact one-to-one mapping is not true, derive the correct expected count from the baseline GLB node-name multiset and document it rather than forcing 10,598.

The hard membership gate is:
- 43/43 accepted F06 names present;
- all seven authorized quarantine names absent;
- zero other baseline node-name omissions;
- zero unexpected new node names.

## Evidence bug

`F06_X01_REGRESSION.json` reports the historical contribution split as all zeros while the accepted F06 manifest and earlier audit prove:

- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1

This is an X01 regression-report extraction bug, not a model regression.

X02 must produce a corrected regression record derived from the locked destination manifest/source contribution fields.

## X02 scope

X02 is:
- camera/evidence only;
- GLB export-parity repair;
- regression-evidence repair.

X02 is not:
- new geometry;
- wider quarantine;
- F06 object mutation;
- Wet Processing mutation;
- F07 work.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F06_X02`
