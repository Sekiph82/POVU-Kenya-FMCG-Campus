# REV005 F04 — EMPLOYEE CHANGING / SHOWER / LOCKER SUPPORT — HISTORICAL SOURCE PROVENANCE

## Accepted source class

F04 is a Class R historical accepted-facility restoration.

V05 independently preserved this facility as PASS. Do not redesign it.

## Historical selected-object composition

V05 renderer group:
`Employee changing / shower / locker support`

Expected selected visible object count:
**59**

Composition:

### BASE REV005: 10 objects

Owner inventory contains exactly:
- `REV005_WELFARE_CLEAN_DIRTY_PARTITION`
- `REV005_WELFARE_LOCKER_0..4` = 5
- `REV005_WELFARE_SHOWER_0..3` = 4

No label/sign object is present in this base inventory, so all 10 are selected.

### V01 contribution: 49 objects

Historical function:
`build_rev005_interior_remediation_v01.py::welfare()`

Facility string:
`Employee Changing / Shower / Locker Support`

#### Locker banks: 20 objects

Five locker-bank X centers:
- 23 m
- 27 m
- 31 m
- 35 m
- 39 m

For each i:

Locker bank:
- name: `RM_WELFARE_LOCKER_BANK_i`
- center: `(X,-77.0,2.5)`
- dimensions: **3.0 × 0.55 × 2.5 m**
- material: steel

Three locker doors per bank, j=0..2:
- name: `RM_WELFARE_LOCKER_DOOR_i_j`
- X = `X-0.9 + j*0.9`
- Y = **-77.33**
- Z = **2.5**
- dimensions: **0.70 × 0.06 × 1.95 m**
- material: blue

5 banks + 15 doors = **20 objects**.

#### Shower cubicles: 24 objects

Four shower center X values:
- 24 m
- 29 m
- 34 m
- 39 m

For each i:

Back wall:
- `RM_WELFARE_SHOWER_BACK_i`
- center: `(X,-66.25,2.6)`
- dimensions: **3.2 × 0.12 × 2.8 m**

Side A:
- `RM_WELFARE_SHOWER_SIDE_A_i`
- center: `(X-1.54,-65.1,2.6)`
- dimensions: **0.12 × 2.3 × 2.8 m**

Side B:
- `RM_WELFARE_SHOWER_SIDE_B_i`
- center: `(X+1.54,-65.1,2.6)`
- dimensions: **0.12 × 2.3 × 2.8 m**

Open/front panel:
- `RM_WELFARE_SHOWER_OPEN_i`
- center: `(X,-63.92,2.7)`
- dimensions: **1.5 × 0.05 × 2.4 m**

Shower head:
- `RM_WELFARE_SHOWER_HEAD_i`
- center: `(X,-64.2,4.3)`
- radius: **0.13 m**
- depth/height: **0.35 m**

Drain:
- `RM_WELFARE_DRAIN_i`
- center: `(X,-64.0,1.31)`
- dimensions: **0.65 × 0.18 × 0.03 m**

4 cubicles × 6 objects = **24 objects**.

#### Clean/dirty zoning: 2 objects

Clean entry:
- `RM_WELFARE_CLEAN_ENTRY`
- center: **(30,-70.0,1.5)**
- dimensions: **16.0 × 0.16 × 2.6 m**
- material: green

Dirty entry:
- `RM_WELFARE_DIRTY_ENTRY`
- center: **(30,-73.0,1.5)**
- dimensions: **16.0 × 0.16 × 2.6 m**
- material: yellow

#### Change bench: 3 objects

Seat:
- `RM_WELFARE_CHANGE_BENCH_SEAT`
- center: **(30,-74.4,1.8)**
- dimensions: **10.0 × 0.75 × 0.18 m**
- material: wood

Bench legs:
Historical `bench()` places legs at dx = -w/2+0.4 and +w/2-0.4, with w=10.

Therefore leg X centers:
- **25.4 m**
- **34.6 m**

Each leg:
- Y = **-74.4**
- Z = **1.45**
- dimensions: **0.12 × 0.50 × 0.65 m**
- material: steel

Bench contribution = **3 objects**.

V01 contribution total:
`20 + 24 + 2 + 3 = 49`

Other versions:
- V02 = 0
- V03 = 0
- V04 = 0
- V05 = 0

Historical accepted total:
`10 BASE + 49 V01 = 59 objects`

## Accepted V05 cameras

A_WIDE:
- location: **(14,-88,13)**
- target: **(30,-70,3)**
- lens: **52 mm**
- sensor width: **36 mm**

B_FUNCTIONAL:
- location: **(20,-78,8)**
- target: **(30,-70,3)**
- lens: **52 mm**
- sensor width: **36 mm**

## Archived V05 hashes

A_WIDE:
`485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

B_FUNCTIONAL:
`59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

## Accepted visual identity

Without labels the facility must read as:
- locker/changing zone
- multiple shower cubicles with heads/drains
- clear clean/dirty separation
- central change bench
- coherent circulation between changing and shower areas
