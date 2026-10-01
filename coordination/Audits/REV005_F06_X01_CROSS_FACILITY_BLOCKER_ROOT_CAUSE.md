# REV005 F06-X01 — Cross-Facility Blocker Root Cause

## Decision

M08.37 correctly stopped at:

`BLOCKED_F06_R01_NO_COMPLETE_INTEGRATED_VIEW`

The failure is no longer classified as a camera-search deficiency.

It is a proven cross-facility envelope overlap between the accepted F06 Micro-ingredient Weigh / Dispense footprint and unaccepted V09 Toothpaste / Wet Wipes replacement envelopes.

## Accepted F06 footprint

Derived directly from the committed 43-object destination manifest:

`output/rev005-facility-gated/F06_micro_weigh/F06_DESTINATION_43_MANIFEST.json`

Full selected-object bounding box:

- X: -15.5 to 5.5 m
- Y: 45.0 to 55.0 m
- Z: 1.0200000445 to 5.750000089 m

The dominant plan envelope is the accepted F06 floor:

- width = 21.0 m
- depth = 10.0 m
- plan area = 210.0 m²

## V09 Toothpaste envelope

Committed V09 builder:

`3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v09.py`

calls:

`env("TOOTHPASTE",-12,43,42,19,8,...)`

The inherited envelope helper creates the structural shell.

Toothpaste plan envelope:

- X: -33.0 to 9.0 m
- Y: 33.5 to 52.5 m

Intersection with accepted F06 plan:

- X: -15.5 to 5.5 = 21.0 m
- Y: 45.0 to 52.5 = 7.5 m
- overlap area = 157.5 m²
- overlap = 75.0% of accepted F06 plan footprint

Therefore the V09 Toothpaste envelope materially occupies the accepted F06 facility area.

Relevant overlapping V09 structural objects:

- `V09_TOOTHPASTE_FLOOR`
- `V09_TOOTHPASTE_BACK_WALL`
- `V09_TOOTHPASTE_SOFFIT`

The left wall, right wall, front header and entry structure do not intersect the accepted F06 plan bounds and are not authorized for F06-X01 quarantine.

## V09 Wet Wipes envelope

The V09 builder calls:

`env("WET_WIPES",22,43,52,19,8,...)`

Wet Wipes plan envelope:

- X: -4.0 to 48.0 m
- Y: 33.5 to 52.5 m

Intersection with accepted F06 plan:

- X: -4.0 to 5.5 = 9.5 m
- Y: 45.0 to 52.5 = 7.5 m
- overlap area = 71.25 m²
- overlap = 33.93% of accepted F06 plan footprint

Relevant overlapping V09 structural objects:

- `V09_WET_WIPES_FLOOR`
- `V09_WET_WIPES_BACK_WALL`
- `V09_WET_WIPES_LEFT_WALL`
- `V09_WET_WIPES_SOFFIT`

The right wall, front header and entry structure are outside the accepted F06 plan bounds and are not authorized for F06-X01 quarantine.

## M08.37 blocker evidence

The 32-camera R01 search repeatedly hit:

Foreign V09 geometry:
- `V09_WET_PROCESS_BACK_WALL`
- `V09_WET_WIPES_LEFT_WALL`
- `V09_TOOTHPASTE_SOFFIT`
- `V09_WET_PROCESS_SOFFIT`

Legitimate F06 geometry:
- `V02_WEIGH_BOOTH_SIDE`
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`

Other blockers included holding-tank objects.

The classification matters:

### Keep — legitimate F06
Do not hide, move or alter:
- `V02_WEIGH_BOOTH_SIDE`
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`
- any of the accepted 43 F06 objects

### Keep — non-overlapping neighbor structure
Do not quarantine for F06:
- `V09_WET_PROCESS_BACK_WALL`
- `V09_WET_PROCESS_SOFFIT`

The V09 Wet Processing plan ends at Y=40.0 m, while accepted F06 begins at Y=45.0 m. These objects may restrict some southern camera positions, but they do not occupy the accepted F06 footprint.

### Resolve — proven overlapping V09 envelope structure
Only the seven listed Toothpaste/Wet Wipes envelope objects are authorized for targeted canonical quarantine in F06-X01.

## Historical context

The independent V09 audit already found:

- V09 preserved prior-PASS groups: 0/6;
- Micro-ingredient Weigh / Dispense: FAIL;
- Toothpaste Production: FAIL;
- Wet Wipes Production: FAIL.

F06 has since been restored exactly to its accepted V05 43-object historical state.

Therefore the unaccepted V09 neighbor envelopes must not be allowed to overwrite or visually occupy the restored accepted F06 footprint.

## Authorized X01 mutation

F06-X01 may change only saved visibility/quarantine metadata for these seven objects:

1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

Allowed changes:
- hide_viewport = true
- hide_render = true
- explicit F06-X01 cross-facility quarantine custom properties

Not allowed:
- delete objects
- move/scale/rotate objects
- alter mesh data/materials
- quarantine any Wet Processing object
- alter any accepted F01-F06 object
- alter other Toothpaste/Wet Wipes equipment
- begin F07

If any named object does not have the expected Toothpaste/Wet Wipes facility ownership and V09 remediation provenance, STOP before mutation.

## Next gate

After the targeted quarantine:
- re-run protection parity;
- verify the seven-object delta exactly;
- run a fresh integrated-camera search;
- require complete F06 workflow readability;
- stop for independent GPT audit.

This is a targeted cross-facility correction, not a redesign of F06, Toothpaste, or Wet Wipes.
