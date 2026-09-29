# REV005 F03 — ELECTRICAL / LV-MV ROOM — HISTORICAL SOURCE PROVENANCE

## Accepted source class

F03 is a Class R historical accepted-facility restoration.

V05 independently preserved Electrical / LV-MV Room as PASS evidence. Do not redesign it.

## Historical selected-object composition

V05 renderer group:
`Electrical / LV-MV room`

Expected selected visible object count:
**30**

Composition:

### BASE REV005: 7 visible objects

Owner inventory contains 8 Electrical/LV-MV objects:

1. `REV005_Electrical_/_LV-MV_room_FLOOR`
2. `REV005_LV_PANEL_0`
3. `REV005_LV_PANEL_1`
4. `REV005_LV_PANEL_2`
5. `REV005_LV_PANEL_3`
6. `REV005_LV_SAFETY_EYEWASH`
7. `REV005_LV_SAFETY_PPE`
8. `REV005_LV_SAFETY_SIGN`

Historical V05 label filtering excludes:
- `REV005_LV_SAFETY_SIGN`

Selected BASE count = **7**.

The replayed historical source manifest is authoritative for exact transforms/dimensions/materials of these 7 BASE objects. Do not invent or normalize them.

## V01 contribution: 23 objects

Historical function:
`build_rev005_interior_remediation_v01.py::lv()`

Facility string:
`Electrical / LV-MV Room`

Anchor:
- x = **111.0 m**
- y = **61.0 m**

### Five switchgear positions

For i = 0..4:

`px = 111 - 4 + i*2`

Therefore X centers:
- i0 = **107.0 m**
- i1 = **109.0 m**
- i2 = **111.0 m**
- i3 = **113.0 m**
- i4 = **115.0 m**

For each i:

#### Switchgear cabinet
Name:
`RM_LV_SWITCHGEAR_i`

Center:
- X = px
- Y = **62.2 m**
- Z = **2.75 m**

Dimensions:
- width X = **1.45 m**
- depth Y = **1.20 m**
- height Z = **3.40 m**

Material:
`REV005_RM_DARK`

#### Panel door / front face
Name:
`RM_LV_PANEL_DOOR_i`

Center:
- X = px
- Y = **61.55 m**
- Z = **2.75 m**

Dimensions:
- X = **1.00 m**
- Y = **0.08 m**
- Z = **2.40 m**

Material:
`REV005_RM_STEEL`

#### Breaker / inspection window
Name:
`RM_LV_BREAKER_WINDOW_i`

Center:
- X = px
- Y = **61.49 m**
- Z = **3.00 m**

Dimensions:
- X = **0.38 m**
- Y = **0.05 m**
- Z = **0.75 m**

Material:
`REV005_RM_PROCESS_CYAN`

#### Cable riser
Name:
`RM_LV_CABLE_i`

Historical pipe endpoints:
- start = `(px, 62.9, 4.5)`
- end   = `(px, 62.9, 5.4)`

Radius:
- **0.09 m**

Vertical center:
- `(px,62.9,4.95)`

Vertical length:
- **0.90 m**

Material:
`REV005_RM_FIRE_RED`

Five positions × four objects = **20 objects**.

### Busbar trunk

Name:
`RM_LV_BUSBAR_TRUNK`

Center:
- X = **111.0 m**
- Y = **62.9 m**
- Z = **5.50 m**

Dimensions:
- X = **9.00 m**
- Y = **0.18 m**
- Z = **0.18 m**

Material:
`REV005_RM_FIRE_RED`

### Service-clearance strip

Name:
`RM_LV_SERVICE_CLEARANCE`

Center:
- X = **111.0 m**
- Y = **59.5 m**
- Z = **1.36 m**

Dimensions:
- X = **8.50 m**
- Y = **1.00 m**
- Z = **0.05 m**

Material:
`REV005_RM_SAFETY_YELLOW`

### Remote service/control panel

Name:
`RM_LV_REMOTE_SERVICE_PANEL`

Center:
- X = **114.0 m**
- Y = **60.0 m**
- Z = **2.40 m**

Dimensions:
- X = **1.40 m**
- Y = **0.50 m**
- Z = **2.20 m**

Material:
`REV005_RM_PROCESS_BLUE`

V01 contribution = **23**.

## Other remediation contributions

- V02 = 0 Electrical objects
- V03 = 0 Electrical objects
- V04 = 0 Electrical objects
- V05 = 0 Electrical objects

Total accepted selection:

`7 BASE + 23 V01 = 30`

## Accepted V05 cameras

A_WIDE:
- location = **(117,50,11)**
- target = **(111,61,3)**
- lens = **52 mm**
- sensor width = **36 mm**

B_FUNCTIONAL:
- location = **(113,56,7)**
- target = **(111,61,3)**
- lens = **52 mm**
- sensor width = **36 mm**

## Archived V05 evidence hashes

A_WIDE:
`2F3BDEEAEDDC850B3CF23E4125171EA5CF9858C4883FC146C3B69E6F4EE892A4`

B_FUNCTIONAL:
`850EAB71C210E923B9042382E373DD42421B3E2A4A6CED281C294E43A05FFA7A`

## Accepted visual identity

Without labels, the room must visibly read as electrical/LV-MV through:

- dense switchgear/panel row
- distinct cabinet front faces
- breaker/inspection window regions
- vertical cable risers
- overhead busbar trunk
- explicit front service-clearance strip
- remote service/control panel
- original safety eyewash/PPE cues
- clear aisle/working relationship

The historical source geometry is authoritative.
