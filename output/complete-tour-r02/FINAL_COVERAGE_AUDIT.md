# M07 R02 Coverage Audit

## Scope

This audit covers the eleven-chapter M07 complete campus and factory tour, not the earlier M01 50-video batch. The R02 camera plan contains 61 physical-target-driven shots after removing the redundant exterior Glass Deck shot.

## Required remediation coverage

| Requirement | Evidence | Status |
|---|---|---|
| Intentional ~15 second aerial opening | CH01 / S001 duration 15 seconds | PASS |
| Continuous moving camera | Target-driven `poseFor()` interpolation and full-master checkpoint review | PASS |
| Real source geometry drives shots | Blender target audit, 61/61 resolved | PASS |
| Public labels match physical targets | Shared target registry for camera and label points | PASS |
| Internal/debug labels removed | Forbidden-term lint and rendered checkpoints | PASS |
| Living wall alignment | S015 Hands of Growth target and visual checkpoint | PASS |
| Hands of Growth visibility | S015 target and end-frame evidence | PASS |
| East Stair / Glass Deck relation | S027 target `GLASS_DECK_EAST_STAIR_STEP_06` | PASS |
| Redundant exterior Glass Deck shot removed | S026 removed from plan and manifest | PASS |
| Wellness / Recreation | S024 target `WELLNESS_PAVILION` | PASS |
| Daycare / Occupational Health | S025 target `DAYCARE_ENTRANCE_SIGNAGE` and related objects | PASS |
| R&D / QC | S021 target `R_D_QC_ENTRANCE_SIGNAGE` | PASS |
| Training / Academy | S022 target `MULTIPURPOSE_STUDIO` / `EXPERIENCE_LINK` | PASS |
| Restaurant / Café | S023 target `CAFE_GLASS_FRONT` | PASS |
| Garden Pods / Employee Garden | S017–S019 target-driven garden entries | PASS |
| Source continuity | Frozen GLB SHA verified before render | PASS |

## Caveat

Where the source GLB does not contain a detailed close-up interior or legible sign, the shot remains a truthful establishing view of the modeled target area. No invented machinery, signage, or facility geometry was added to close that evidence gap.

