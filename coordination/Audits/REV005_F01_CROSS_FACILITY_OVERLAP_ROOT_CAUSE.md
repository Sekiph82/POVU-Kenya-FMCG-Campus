# REV005 F01 — CROSS-FACILITY OVERLAP ROOT-CAUSE FINDING

## Status

`CONFIRMED_V09_GLASS_DECK_GROUND_LEVEL_OVERLAP_REGRESSION`

## Why F01-D could not find a valid integrated camera

The focused camera search tested eight azimuths and could achieve only 3/9 clear rays even after one temporary exclusion.

Reported blockers included:
- `V09_BLOW_SOFFIT`
- `V09_GLASS_DECK_SOFFIT`
- `V09_WET_PROCESS_RIGHT_WALL`
- QA-only exclusion attempt: `V09_WET_PROCESS_SOFFIT`

The camera search itself was not the root cause.

## F01 accepted footprint

Historical/restored F01 floor:
- object: `REV005_Caps_and_trigger_assembly_FLOOR`
- center: approximately `(52,31)`
- size: approximately `27×15 m`

Horizontal footprint:
- X: approximately `38.5–65.5`
- Y: approximately `23.5–38.5`

## True historical Glass Deck source geometry

Source audit:
`3d/revisions/REV005/audit/REV005_INTERIOR_AUDIT.json`

True central link:
- object: `GLASS_DECK_LINK`
- bounds X: `66–74`
- bounds Y: `-6–46`
- bounds Z: `8.2–12.2`
- size: `8×52×4 m`

True floor:
- object: `GLASS_DECK_LINK_FLOOR`
- bounds X: `66.25–73.75`
- bounds Y: `-5.5–45.5`
- bounds Z: `8.36–8.54`

The historical Glass Deck is therefore an **elevated narrow link/deck**, not a ground-level 40×24 m room.

## Erroneous V09 Glass Deck replacement

V09 code:
`build_rev005_interior_remediation_v09.py::build_glass()`

It calls:

`env("GLASS_DECK",70,24,40,24,8,...)`

The V08/V09 envelope helper constructs:
- floor at Z ≈ 1 m
- side/back/front envelope at ground level
- soffit at Z ≈ 7.85 m

V09 ground-level footprint:
- X: `50–90`
- Y: `12–36`

This overlaps the accepted F01 footprint by approximately:
- X overlap: `50–65.5` = **15.5 m**
- Y overlap: `23.5–36` = **12.5 m**
- overlap plan area: approximately **193.75 m²**

This is a real cross-facility regression, not a camera-choice problem.

## V09 collection boundary

V09 build report identifies:

Collection:
`REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`

V09 object count:
**117**

This collection is the V09 replacement layer. It is not the historical source Glass Deck shell/link.

## Safe repair decision

Do not move/rebuild Glass Deck now.

Facility-gated workflow remains in force.

For F01 integration closure:
- quarantine the entire 117-object V09 Glass Deck replacement collection from viewport/render/export;
- preserve the collection and objects in the Blend for provenance;
- add explicit quarantine metadata;
- preserve historical/source Glass Deck objects untouched;
- do not modify F01's 76 objects;
- do not modify Bottle Blow or Wet Processing geometry.

Later, when Glass Deck becomes the active facility, it will be rebuilt/restored against the true elevated source geometry.

## Required post-quarantine proof

After quarantine:
1. source Glass Deck link/floor bounds remain unchanged;
2. F01 76-object geometry/transform parity remains unchanged;
3. rerun integrated-camera 8-azimuth/9-ray search;
4. require >=7/9 clear rays;
5. require F01 30–65% screen coverage;
6. render 1440×960 plus 900×600 preview;
7. inspect independently before F02 unlock.
