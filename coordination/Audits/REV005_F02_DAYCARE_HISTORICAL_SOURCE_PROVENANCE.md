# REV005 F02 — DAYCARE / CRÈCHE — HISTORICAL SOURCE PROVENANCE

## Accepted source class

F02 is a Class R historical accepted-facility restoration.

V05 independently preserved Daycare / Crèche as PASS evidence. Do not redesign it.

## Historical selected-object composition

V05 renderer group:
`Daycare / crèche`

Expected selected visible object count:
**79**

Composition:

### Base REV005 inventory: 41 visible objects

Owner inventory contains 42 Daycare objects. V05 label filtering excludes only:
`REV005_LABEL_DAYCARE`

The remaining 41 base objects are selected.

Base visible objects include:
- 4 activity tables:
  - `REV005_DAYCARE_ACTIVITY_0_TABLE`
  - `REV005_DAYCARE_ACTIVITY_1_TABLE`
  - `REV005_DAYCARE_ACTIVITY_2_TABLE`
  - `REV005_DAYCARE_ACTIVITY_3_TABLE`
- 12 chair seat/back pairs = 24 chair objects
- 5 cots:
  - `REV005_DAYCARE_COT_0..4`
- 5 cubbies:
  - `REV005_DAYCARE_CUBBY_0..4`
- `REV005_DAYCARE_NAP_PARTITION`
- `REV005_DAYCARE_SINK`
- `REV005_Daycare_/_crèche_FLOOR`

Total visible base selection:
**41**

### V03 Daycare contribution: 38 objects

Historical function:
`build_rev005_interior_remediation_v03.py::daycare()`

Anchor:
- x = **-105 m**
- y = **-64 m**

Exact V03 geometry:

1. Floor
- name: `V03_DAYCARE_FLOOR`
- center: (-105, -64, 1.02)
- dimensions: (27.0, 20.0, 0.18) m

2. Enclosure left wall
- name: `V03_DAYCARE_ENCLOSURE_LEFT`
- center: (-118.0, -64.0, 2.75)
- dimensions: (0.16, 19.0, 5.5) m

3. Enclosure right wall
- name: `V03_DAYCARE_ENCLOSURE_RIGHT`
- center: (-92.0, -64.0, 2.75)
- dimensions: (0.16, 19.0, 5.5) m

4. Enclosure back wall
- name: `V03_DAYCARE_ENCLOSURE_BACK`
- center: (-105.0, -54.5, 2.75)
- dimensions: (26.0, 0.16, 5.5) m

5. Low internal partition
- `V03_DAYCARE_LOW_PARTITION`
- center: (-105, -64, 2.1)
- dimensions: (22.0, 0.18, 1.7) m

6. Play rug
- `V03_DAYCARE_PLAY_RUG`
- center: (-110, -58, 1.18)
- dimensions: (8.5, 5.5, 0.08) m

7–12. Six play blocks
- names: `V03_DAYCARE_PLAY_BLOCK_00..05`
- dimensions each: (1.0, 1.0, 0.7) m
- Z center: 1.5 m
- row 1 Y: -58.0 m
  - X: -112.0, -110.5, -109.0
- row 2 Y: -56.6 m
  - X: -112.0, -110.5, -109.0
- alternating yellow/teal materials

13. Reading shelf
- `V03_DAYCARE_READING_SHELF`
- center: (-97.0, -58.0, 2.3)
- dimensions: (1.2, 4.5, 2.2) m

14–17. Four reading bins
- `V03_DAYCARE_READING_BIN_00..03`
- center X: -97.7
- center Y: -59.3, -58.4, -57.5, -56.6
- center Z: 2.2
- dimensions each: (0.18, 0.55, 0.42) m

18. Soft nook
- `V03_DAYCARE_SOFT_NOOK`
- center: (-97.6, -65.0, 1.65)
- dimensions: (3.5, 3.2, 0.35) m

19–22. Four soft backs
- `V03_DAYCARE_SOFT_BACK_00..03`
- X: -99.1, -98.1, -97.1, -96.1
- Y: -66.4
- Z: 2.35
- dimensions each: (0.85, 0.25, 1.0) m

23. Caregiver desk
- `V03_DAYCARE_CAREGIVER_DESK`
- center: (-106.0, -66.5, 2.1)
- dimensions: (3.4, 1.1, 1.5) m

24. Caregiver screen
- `V03_DAYCARE_CAREGIVER_SCREEN`
- center: (-106.0, -65.8, 3.5)
- dimensions: (2.4, 0.12, 1.2) m

25–32. Four light fixtures, two meshes each
For i = 0..3:
- X = -114, -108, -102, -96
- Y = -64
- BODY Z = 6.30, dimensions (2.2,0.32,0.10)
- GLOW Z = 6.23, dimensions (1.7,0.16,0.04)
- names:
  - `V03_DAYCARE_LIGHT_00_BODY/GLOW`
  - ...
  - `V03_DAYCARE_LIGHT_03_BODY/GLOW`

33. Child-height handwash
- `V03_DAYCARE_HANDWASH`
- center: (-97.0, -70.5, 1.9)
- dimensions: (3.5, 0.75, 1.5) m

34–38. Five cubby faces
- names: `V03_DAYCARE_CUBBY_FACE_00..04`
- X: -113.0, -109.4, -105.8, -102.2, -98.6
- Y: -72.0
- Z: 2.2
- dimensions each: (2.0, 0.18, 1.7) m

### Other remediation contributions

- V01: 0 Daycare objects
- V02: 0 Daycare objects
- V04: 0 Daycare objects
- V05: 0 Daycare objects

Total:
`41 + 38 = 79`

## Accepted V05 cameras

A_WIDE:
- location: (-122,-80,13)
- target: (-105,-64,3)
- lens: 52 mm
- sensor width: 36 mm

B_FUNCTIONAL:
- location: (-113,-72,8)
- target: (-105,-64,3)
- lens: 52 mm
- sensor width: 36 mm

## Archived V05 PNG hashes

A_WIDE:
`72370EF41D5C1EA3AE81500EE77F5764725D8C0C3E0622D1CD21B55344F757EE`

B_FUNCTIONAL:
`7E06E34994D36AE6D84D3F4A58B1C7E05BC3FEEECD79EC06514ECDB2DC5A3F7B`

## Visual identity

Accepted Daycare must visibly show:
- child-scale activity tables and chairs
- play rug and play blocks
- nap/rest separation and cots/soft nook
- cubbies/storage
- reading shelf/bins
- child-height handwash
- caregiver station
- low internal partition
- clear child-scale room zoning

No labels are required for recognition.
