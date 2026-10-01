# REV005 F05 — FIRE PUMP HOUSE — HISTORICAL SOURCE PROVENANCE

## Important source split

Historical V05 `objects_for("Fire pump house")` returns **123 objects**.

However that selection contains two spatially separate pump-house clusters.

The accepted V05 A/B/C cameras and visual evidence are centered on the **primary cluster around (94,-5)**.

The second cluster around Y≈70 is not visible in the accepted A/B/C evidence and overlaps the Utilities/engineering side of the campus model. It must not be silently restored as part of F05 without separate proof.

Therefore F05 must first reproduce the 123-object historical selection and split it spatially before canonical mutation.

## Historical total selection

Expected:
**123 objects**

Expected contribution accounting:

- BASE visible: **10**
- V01: **15**
- V02: **0**
- V03: **0**
- V04: **44**
- V05: **54**

Total:
`10 + 15 + 44 + 54 = 123`

## Expected spatial split

### Primary accepted review cluster

Anchor:
`(94,-5,3)`

Expected primary cluster count:
**54**

Expected composition:
- BASE: **5**
- V01: **0**
- V04: **22**
- V05: **27**

Primary Y window for deterministic classification:
**-20 m <= object world-bounds center Y <= +10 m**

### Secondary historical duplicate/remediation cluster

Expected secondary count:
**69**

Expected composition:
- BASE: **5**
- V01: **15**
- V04: **22**
- V05: **27**

Secondary Y window:
**55 m <= object world-bounds center Y <= 85 m**

If any of the 123 selected objects fall outside both windows, or the expected 54/69 split fails, STOP before canonical mutation.

The secondary 69-object cluster is historical provenance only for F05 and is NOT authorized for canonical restoration by this task.

## BASE inventory

Owner inventory contains 12 names:
- 8 pump body/panel objects
- 2 floor objects
- 2 label objects

The two label objects are excluded by historical V05 label filtering.

Visible BASE selection = **10**.

Replay geometry determines which 5 belong to the primary cluster and which 5 belong to the secondary cluster.

## V01 Fire Pump contribution

Historical function:
`build_rev005_interior_remediation_v01.py::fire_pump()`

Anchor:
- x = 76
- y = 72

All 15 V01 objects belong to the secondary Y≈70 cluster.

V01 objects:
- three pump motors
- three pump bases
- three suction pipes
- three discharge pipes
- one manifold
- one controller
- one service-access strip

V01 contribution:
**15**

## V04 primary cluster

Historical function:
`build_rev005_interior_remediation_v04.py::fire_pump()`

Primary k=0:
- x = **94**
- y = **-5**

Expected V04 primary object count:
**22**

### Room shell
Prefix:
`V04_FIRE_00`

- FLOOR center (94,-5,1.05), size 18×16×0.18
- BACK center (94,3,3.25), size 18×0.16×6.5
- LEFT center (85,-5,3.25), size 0.16×16×6.5
- RIGHT center (103,-5,3.25), size 0.16×16×6.5

### Two pump sets

Pump X:
- 91
- 97

For each:
- pump cylinder center (X,-6,2.0), radius 0.85, depth 2.2, rotation Y=π/2
- base center (X,-6,1.35), size 3.0×1.7×0.25

### Pipework
- suction: (87,-2.5,2.4) → (101,-2.5,2.4), radius 0.18
- discharge 1: (91,-6,3.0) → (91,-1.2,4.8), radius 0.16
- discharge 2: (97,-6,3.0) → (97,-1.2,4.8), radius 0.16

### Four valves
X:
- 88
- 92
- 96
- 100

Y=-2.5, Z=2.4
radius 0.32, depth 0.18, rotation Y=π/2

### Panel
center:
(100,-10,2.6)
size:
1.1×0.25×2.0

### Three lights

Centers:
- (88,-5,7.5)
- (94,-5,7.5)
- (100,-5,7.5)

Each historical light creates BODY + GLOW = 2 objects.

Total V04 primary:
**22**

## V05 primary cluster

Historical function:
`build_rev005_interior_remediation_v05.py::fire()`

Primary k=0:
- x = **94**
- y = **-5**

Expected V05 primary count:
**27**

### Envelope
Prefix:
`V05_FIRE0`

Envelope dimensions:
20×18×7 m

Objects:
- FLOOR
- BACK
- LEFT
- RIGHT
- 3 SOFFIT objects
- 2 light fixtures × BODY/GLOW = 4 objects
- DOOR_L
- DOOR_R
- DOOR_HEADER

Envelope total:
**14**

Exact major centers:
- floor (94,-5,1.05)
- back (94,4,3.5)
- left (84,-5,3.5)
- right (104,-5,3.5)
- soffit X: 88.4, 94.0, 99.6
- soffit Z: 6.82
- door plane Y: -13.9
- door L X=92
- door R X=96
- door header X=94, Z=5.55

### Two pump machines

Pump centers:
- X=91
- X=97
- Y=-5

Each `machine()` creates:
- HOUSING
- PANEL
- BASE

Each machine = 3 objects.
Two machines = **6**.

Housing:
- dimensions 2.6×2.0×2.0
- center Z=2.0

Panel:
- Y=-6.08
- center Z=2.3
- dimensions 1.43×0.12×0.56

Base:
- center Z=1.28
- dimensions 3.0×2.4×0.22

### Pipework
- suction: (87,-2,3) → (101,-2,3), radius 0.18
- header: (91,-5,4) → (97,-5,4), radius 0.18

### Four valves
X:
88, 92, 96, 100
Y=-2
Z=3
radius 0.30
depth 0.20
rotation Y=π/2

### Panel
center:
(100,-10,2.6)
size:
1.1×0.25×2.2

Total V05 primary:
14 + 6 + 2 + 4 + 1 = **27**

## Historical V05 QA visibility semantics

The V05 renderer selects all 123 group objects, then hides shell-occluders whose names contain:
- _LEFT
- _RIGHT
- _BACK
- _SOFFIT
- _CEILING_BEAM

For primary F05 parity this rule must be reproduced exactly.

Expected hidden primary shell objects include:

V04:
- V04_FIRE_00_BACK
- V04_FIRE_00_LEFT
- V04_FIRE_00_RIGHT

V05:
- V05_FIRE0_BACK
- V05_FIRE0_LEFT
- V05_FIRE0_RIGHT
- all three V05_FIRE0_SOFFIT_* objects

Primary historical QA selection after shell hiding therefore visually emphasizes pumps, manifolds, valves, panel and room floor/open context.

## Accepted V05 cameras

A_WIDE:
- location (76,-22,15)
- target (94,-5,3)
- lens 52 mm
- sensor 36 mm

B_FUNCTIONAL:
- location (88,-12,9)
- target (94,-5,3)
- lens 52 mm
- sensor 36 mm

C_PROCESS_OR_DETAIL:
- location (98,-2,9)
- target (94,-5,3)
- lens 52 mm
- sensor 36 mm

## Archived V05 PNG hashes

A:
`5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`

B:
`D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`

C:
`AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

## Accepted visual identity

Primary Fire Pump House must visibly show:
- two large red pump/motor sets
- paired bases
- suction/header pipework
- multiple red valves
- yellow discharge/header relation
- control panel
- open service access around equipment
- dedicated pump-room context

The secondary Y≈70 historical cluster is not authorized for F05 canonical restore.
