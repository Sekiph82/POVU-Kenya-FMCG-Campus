# REV005 F05 — FIRE PUMP HOUSE — HISTORICAL SOURCE PROVENANCE

## Historical V05 selection

Group:
`Fire pump house`

Original V05 `objects_for()` selection after V01→V05 replay must contain exactly:

**123 objects**

Historical contribution count:

- BASE visible: **10**
- V01: **15**
- V02: **0**
- V03: **0**
- V04: **44**
- V05: **54**

Total:
`10 + 15 + 44 + 54 = 123`

## Spatial split

The 123 historical objects contain two physically separate Fire Pump House clusters.

Use actual replayed object world centers and classify:

- **PRIMARY**: world-center Y < 30 m
- **SECONDARY**: world-center Y >= 30 m

Required split:

- PRIMARY = **54 objects**
- SECONDARY = **69 objects**

No object may fall ambiguously on the threshold.

Historical accepted A/B/C cameras all target the PRIMARY cluster around:

`(94,-5,3)`

The SECONDARY cluster around Y≈70 is not part of the primary accepted facility restoration.

## Contribution split

### BASE

10 visible base objects total.

Historical replay must prove:
- PRIMARY BASE = **5**
- SECONDARY BASE = **5**

Do not infer by capitalization. Classify by actual world center.

### V01

Historical function:
`build_rev005_interior_remediation_v01.py::fire_pump()`

Anchor:
- x = 76
- y = 72

All 15 V01 objects are SECONDARY.

V01 objects:
- 3 pump motors
- 3 bases
- 3 suction pipes
- 3 discharge pipes
- 1 manifold
- 1 controller
- 1 service-access strip

### V04

Historical function:
`build_rev005_interior_remediation_v04.py::fire_pump()`

Two clusters:
- PRIMARY = (94,-5)
- SECONDARY = (94,70)

Each cluster contributes exactly **22 objects**.

Per cluster:
- room floor/back/left/right = 4
- two pump bodies + two bases = 4
- suction/discharge/discharge2 pipes = 3
- four valves = 4
- panel = 1
- three lights × BODY/GLOW = 6

Total:
22.

#### PRIMARY V04 exact geometry

Room:
- floor center (94,-5,1.05), size 18×16×0.18 m
- back center (94,3,3.25), size 18×0.16×6.5 m
- left center (85,-5,3.25), size 0.16×16×6.5 m
- right center (103,-5,3.25), size 0.16×16×6.5 m

Pumps:
- centers (91,-6,2.0), (97,-6,2.0)
- radius 0.85 m
- depth 2.2 m
- rotation X = π/2

Bases:
- centers (91,-6,1.35), (97,-6,1.35)
- size 3.0×1.7×0.25 m

Suction:
- (87,-2.5,2.4) → (101,-2.5,2.4)
- radius 0.18 m

Discharge 1:
- (91,-6,3.0) → (91,-1.2,4.8)
- radius 0.16 m

Discharge 2:
- (97,-6,3.0) → (97,-1.2,4.8)
- radius 0.16 m

Valves:
- X = 88,92,96,100
- Y = -2.5
- Z = 2.4
- radius 0.32 m
- depth 0.18 m

Panel:
- center (100,-10,2.6)
- size 1.1×0.25×2.0 m

Lights:
- X = 88,94,100
- Y = -5
- Z = 7.5
- each light has BODY + GLOW

### V05

Historical function:
`build_rev005_interior_remediation_v05.py::fire()`

Two clusters:
- PRIMARY = (94,-5)
- SECONDARY = (94,70)

Each cluster contributes exactly **27 objects**.

Per cluster:
- envelope = 14
- two pump machines × 3 objects = 6
- suction + header = 2
- four valves = 4
- panel = 1

Total:
27.

#### PRIMARY V05 envelope

Center:
(94,-5)

w = 20 m
d = 18 m
h = 7 m

Floor:
- center (94,-5,1.05)
- size 20×18×0.18 m

Back:
- center (94,4,3.5)
- size 20×0.18×7 m

Left:
- center (84,-5,3.5)
- size 0.18×18×7 m

Right:
- center (104,-5,3.5)
- size 0.18×18×7 m

Soffits:
- X = 88.4, 94.0, 99.6
- Y = -5
- Z = 6.82
- each size 3.2×17.2×0.18 m

Lights:
- X = 89,99
- Y = -5
- Z = 6.5
- BODY + GLOW per light

Doors:
- L center (92,-13.9,3.0), size 0.12×0.16×5.2
- R center (96,-13.9,3.0), size 0.12×0.16×5.2
- header center (94,-13.9,5.55), size 4.2×0.16×0.16

#### PRIMARY V05 pump machines

Machine centers:
- X = 91,97
- Y = -5
- w = 2.6
- d = 2.0
- h = 2.0

Each machine:
- HOUSING center Z=2.0, size 2.6×2.0×2.0
- PANEL center Y=-6.08, Z=2.3, size 1.43×0.12×0.56
- BASE center Z=1.28, size 3.0×2.4×0.22

Suction:
- (87,-2,3) → (101,-2,3)
- radius 0.18

Header:
- (91,-5,4) → (97,-5,4)
- radius 0.18

Valves:
- X = 88,92,96,100
- Y = -2
- Z = 3
- radius 0.30
- depth 0.20

Panel:
- center (100,-10,2.6)
- size 1.1×0.25×2.2 m

## Required primary destination

Restore only the **54 PRIMARY objects**.

Do not append the 69 SECONDARY objects.

Destination collection:

`REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`

## Historical V05 cameras

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

## Archived hashes

A:
`5CC3309AA25319E7C4DAA55DDBE2F8B8D50EDAD26EC40F74E82206B584D1F724`

B:
`D97723E350428731580A1DB79CA84FEBC3922B05B6978D580879D2FA558B7D1F`

C:
`AC46E1F4DD829E66B3B3898857E85D53FAFB64DECBB635F7528728033F5A7304`

## Historical V05 QA visibility rule

For A/B/C parity, reproduce original `show_only()` exactly.

Even selected objects are hidden if their name contains:
- `_LEFT`
- `_RIGHT`
- `_BACK`
- `_SOFFIT`
- `_CEILING_BEAM`

This is temporary QA visibility only and must not alter the saved canonical model.

## Accepted visual identity

Primary Fire Pump House must visibly read as:
- paired pump sets
- pump bases
- suction/header piping
- discharge piping
- multiple valves
- dedicated control panel
- service-access relationship
- compact dedicated pump-room arrangement
