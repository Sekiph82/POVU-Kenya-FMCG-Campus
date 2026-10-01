# REV005 F04 X01 — CROSS-FACILITY BLOCKER ROOT CAUSE

## Finding

F04 historical model is valid:
- 10 BASE + 49 V01 = 59
- dimensional contract PASS
- archived A/B parity PASS

F04 V04 rendered six real integrated previews. None is acceptable.

Direct GPT visual review found the dominant blockers are V09 Training/Restaurant geometry, not F04.

## Historical bounds

Historical `WELLNESS_PAVILION`:
- X 19 → 41
- Y -79 → -61
- Z 1.2 → 7.2

Historical `Restaurant_Wellness`:
- X -16 → 26
- Y -80.5 → -55.5
- Z 1.2 → 9.2

## V09 Training regression

V09 builder:
`env("TRAINING",30,-61,28,18,7,...)`

Therefore the V09 Training envelope footprint is approximately:
- X 16 → 44
- Y -70 → -52

Overlap with historical Wellness Pavilion:
- X 19 → 41 = 22 m
- Y -70 → -61 = 9 m
- plan overlap ≈ **198 m²**

Specific visible blocker:
`V09_TRAINING_BOARD`
- center (30,-69.8,4.0)
- dimensions 7 × 0.12 × 3.0 m

This object lies inside the historical Wellness Pavilion / accepted F04 zone and appears as the large black panel in V04 candidate previews.

V09 build report collection:
`REV005_V08_CLEAN_TRAINING_ACADEMY`
- 81 objects

The historical source audit contains no Training/Academy source shell/object corresponding to this V09 28×18 m envelope. This V09 layer therefore cannot override the already accepted historical F04 welfare geometry.

## V09 Restaurant regression

V09 builder:
`env("RESTAURANT",5,-69,46,26,7,...)`

The right wall is therefore near:
- X ≈ 28 m

Historical `Restaurant_Wellness` shell max X:
- X = 26 m

So the V09 Restaurant right wall extends roughly 2 m beyond the historical Restaurant shell into the Wellness/F04 side.

Specific blocker observed by LOS:
`V09_RESTAURANT_RIGHT_WALL`

V09 Restaurant collection:
`REV005_V08_CLEAN_RESTAURANT_POVU_CAF_KITCHEN`
- 135 objects

Do NOT quarantine the entire Restaurant collection under F04. Only the proven right-wall blocker is authorized.

## Authorized minimal repair

1. Quarantine the entire invalid V09 Training / Academy replacement collection:
`REV005_V08_CLEAN_TRAINING_ACADEMY`
expected 81 objects.

2. Quarantine only:
`V09_RESTAURANT_RIGHT_WALL`

Do not quarantine any other Restaurant object.

3. Preserve:
- historical WELLNESS_PAVILION
- WELLNESS_GLASS
- historical Restaurant_Wellness shell
- V09 Wellness collection
- F01/F02/F03
- historical Glass Deck
- existing V09 Glass Deck quarantine

4. Then restore exact 59-object F04 historical model and rerun integrated evidence.

If another blocker remains, stop and report it. Do not broaden quarantine automatically.
