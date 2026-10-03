# REV005 F08-R02 — Independent GPT Audit

## Verdict

`REMEDIATION_REQUIRED_R03_EXTERNAL_SOUTH_FRONTAGE_EVIDENCE`

Audited execution commit:

`26e55140ca75a99c4ba8088c541d2339c6dbe086`

Canonical Blend/GLB remain unchanged. F09 remains blocked.

## Technical R02 result

Accepted staged technical gates:

- R02 accepted F08 meshes: 391
- prior staged count: 338
- added R02 meshes: 53
- legacy retired: 391 / 391
- ambiguous legacy: 0
- NOT_F08 preserved: 5
- F01-F07 unauthorized differences: 0
- cross-facility collisions: 0
- outside-envelope objects: 0
- dimensional validation: PASS
- protection: PASS
- canonical Blend unchanged
- canonical GLB unchanged

The R02 staged Blend is therefore technically suitable for one final evidence-only camera closure attempt.

## Direct visual audit

### A selected

`F08_R02_A_SELECTED_PREVIEW_900x600.png`

Direct review:
- outfeed bottles are clearly readable;
- guarded cell is present;
- oven/feed structures exist;
- room context is clean;
- bulk hopper is not established as the process origin.

FAIL.

### B selected

`F08_R02_B_SELECTED_PREVIEW_900x600.png`

Direct review:
- heater bank, transfer region, guarded cell and outfeed are all present;
- formed bottles read well;
- mould/blow transformation remains visually compressed and ambiguous.

FAIL.

### C selected

`F08_R02_C_SELECTED_PREVIEW_900x600.png`

Direct review:
- two mould stations are visible;
- clamp/actuator cues are improved;
- outfeed bottle line is visible;
- HMI is visible;
- oven/transfer-to-transformation relationship is not strong enough in-frame.

FAIL.

### D selected

`F08_R02_D_SELECTED_PREVIEW_900x600.png`

Direct review:
- feed, oven, cell, outfeed and HMI context are present;
- process direction is suggested;
- hopper/source identity is still absent;
- complete bulk-preform-to-bottle sequence is not label-blind readable.

FAIL.

## Important camera-search gap

R02 rendered 96 candidates, but the camera search did not test the most important remaining architectural viewpoint: a true external south-frontage elevation through the glazed facade.

Published R02 camera ranges:

### A
- X: 62…70
- Y: 7…13
- lens: 16…24 mm

### B
- X: 60…70
- Y: 3…9
- lens: 16…28 mm

### C
- X: 50…60
- Y: 0.5…3.5
- lens: 20…32 mm

### D
- X: 38…58
- Y: 3…9
- lens: 16…24 mm

The locked south glazed frontage is around:

`Y = -1.84 m`

Therefore R02 used no camera meaningfully outside the south glazed facade.

R01 also never exhausted this family; its minimum A-camera Y was approximately -0.5 m.

The complete process line spans roughly west→east from hopper at X≈36.5 to outfeed near X≈69.5. A camera 8–15 m south of the glazed frontage can view the entire line nearly side-on and may establish:
- bulk hopper silhouette at the west end;
- elevator/feed continuity;
- oven;
- transfer;
- twin mould stations in side elevation;
- formed-bottle outfeed at the east end.

This exact architectural vantage has not yet been tested.

## Audit correction

The prior R01 conclusion that camera search was fully exhausted was too broad.

R02 model legibility has improved materially:
- heater bars no longer dominate;
- formed bottles are now clearly visible;
- clamp/actuator cues are stronger.

Before authorizing additional geometry mutation, the untested true external south-frontage family must be exhausted.

## R03 scope

R03 is the **final camera-only F08 evidence attempt**.

Use the exact published R02 staged model:
- no geometry edits;
- no material edits;
- no visibility changes;
- no new quarantine;
- no canonical promotion unless all visual + technical gates pass.

Priority is side-on/external south elevation through the existing glazed frontage.

If R03 fails, no R04 camera-only task is permitted. The next task must be model/process-identity remediation.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R03`
