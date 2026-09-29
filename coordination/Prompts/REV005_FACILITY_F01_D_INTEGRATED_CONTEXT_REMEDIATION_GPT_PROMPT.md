# F01-D — CAPS & TRIGGER INTEGRATED CONTEXT CAMERA REMEDIATION

## Scope

One evidence defect only:

`F01_D_INTEGRATED_CONTEXT.png`

The F01 facility model is already accepted for geometry/parity purposes.

**DO NOT MODIFY THE F01 MODEL.**
**DO NOT MODIFY ANY OTHER FACILITY.**

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT.md`
3. `coordination/Audits/REV005_FACILITY_F01_CAPS_TRIGGER_GPT_AUDIT_CRITERIA.md`
4. `output/rev005-facility-gated/F01_caps_trigger/F01_DESTINATION_MANIFEST.json`
5. `output/rev005-facility-gated/F01_caps_trigger/F01_FINAL_HASHES.json`

## Locked canonical baseline

Current accepted F01 Blend SHA-256:
`1F2031610251CDCBD064867DB4E925CFD573C621010BDD5A72E17F45BE08D703`

Current accepted F01 GLB SHA-256:
`B2972FB7F6F4B25CD4CC30615B550EAEC5A11037E56EDA3F18D9DC96F27B632D`

The remediation is render/camera-only.

After completion, these two hashes MUST remain exactly unchanged.

If either changes:
STOP `BLOCKED_F01_D_MODEL_MUTATION`

## Existing failed image

Failed file:
`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT.png`

Failure:
the current integrated camera is hidden behind/inside an architectural surface; F01 is not visible at all.

Do not reuse the failed camera without validating line of sight.

## Phase 1 — load scene without saving

Open the current canonical REV005 Blend.

Do not save it.

Do not export GLB.

Identify the exact restored F01 set using:
- `F01_DESTINATION_MANIFEST.json`
- restored F01 names/tags

Expected target count: 76.

## Phase 2 — calculate exact F01 world bounds

For every one of the 76 F01 objects:

1. read its 8 local `bound_box` corners;
2. transform each corner by `matrix_world`;
3. collect all world-space points.

Compute exact union:
- `min_x, max_x`
- `min_y, max_y`
- `min_z, max_z`

Compute:
- `Cx=(min_x+max_x)/2`
- `Cy=(min_y+max_y)/2`
- `Cz=(min_z+max_z)/2`
- `Wx=max_x-min_x`
- `Wy=max_y-min_y`
- `Hz=max_z-min_z`
- horizontal radius `R=sqrt((Wx/2)^2+(Wy/2)^2)`

Write these exact numeric values to:
`F01_D_CAMERA_DIAGNOSTIC.json`

Do not invent the bounds.

## Phase 3 — diagnose the failed historical A camera in the current integrated scene

Failed D camera started from:
- location: `(60.000,18.000,13.000)`
- target: `(52.000,31.000,3.000)`
- lens: 52 mm
- sensor width: 36 mm

Ray-cast from this camera to the following 9 target samples inside the F01 union bounds:

1. center `(Cx,Cy,Cz)`
2. `(Cx-Wx*0.30,Cy,Cz)`
3. `(Cx+Wx*0.30,Cy,Cz)`
4. `(Cx,Cy-Wy*0.30,Cz)`
5. `(Cx,Cy+Wy*0.30,Cz)`
6. `(Cx-Wx*0.20,Cy-Wy*0.20,Cz+Hz*0.20)`
7. `(Cx+Wx*0.20,Cy-Wy*0.20,Cz+Hz*0.20)`
8. `(Cx-Wx*0.20,Cy+Wy*0.20,Cz+Hz*0.20)`
9. `(Cx+Wx*0.20,Cy+Wy*0.20,Cz+Hz*0.20)`

For every ray, record:
- first hit object name
- first hit distance
- whether hit object belongs to F01
- distance to target sample

Any non-F01 first hit before the target sample is an occluder.

Record the exact failed occluder object names.

## Phase 4 — candidate integrated cameras

Do NOT change scene geometry.

Generate candidate cameras around the computed F01 center.

Use 8 azimuths in world XY:
- 0°
- 45°
- 90°
- 135°
- 180°
- 225°
- 270°
- 315°

For each azimuth:

Horizontal camera distance:
`D=max(1.65*R, 18.0 m)`

Camera XY:
- `cam_x = Cx + cos(azimuth)*D`
- `cam_y = Cy + sin(azimuth)*D`

Camera Z:
`cam_z = max(max_z + 6.0 m, Cz + 0.75*D)`

Initial target:
`(Cx, Cy, Cz + 0.10*Hz)`

Lens candidates:
- 52 mm first
- 45 mm only if 52 mm cannot fit the F01 bounds plus surrounding context

Do not use lens below 45 mm.

Near clip:
`0.10 m`

Far clip:
`1000 m`

Rotation:
`(Vector(target)-Vector(location)).to_track_quat("-Z","Y").to_euler()`

## Phase 5 — hard line-of-sight gate for candidate cameras

For each candidate, run the same 9-ray test.

Candidate is REJECTED if:
- fewer than 7 of 9 rays reach F01/target without a non-F01 blocker;
- camera world point is inside any mesh bounding volume;
- camera-to-center direction immediately intersects an architectural mesh within 1.0 m;
- projected F01 bounds fall partly outside frame.

Prefer a candidate with:
- 9/9 unobstructed rays;
- if none, 8/9;
- if none, 7/9.

Do not accept <7/9.

## Phase 6 — screen-coverage gate

For each surviving candidate:

Project all F01 world-bound corners into camera normalized coordinates.

Required:
- entire F01 projected bounds inside 5%–95% of image width;
- entire F01 projected bounds inside 7%–93% of image height;
- projected F01 bounding rectangle occupies **30%–65%** of total image area.

Purpose:
the image must show F01 clearly **and** enough current surrounding architecture to prove integration.

Reject:
- F01 <30% area: too distant;
- F01 >65% area: not enough integrated context.

If coverage is too small:
decrease D in 1.0 m steps, never below `1.25*R`.

If too large:
increase D in 1.0 m steps.

After every move rerun the 9-ray line-of-sight gate.

## Phase 7 — architecture handling rule

Preferred solution is camera relocation.

Do NOT globally hide walls, roofs, shells or legacy objects.

Only if no 8-azimuth candidate can achieve >=7/9 clear rays:

1. identify the **single** non-F01 architectural object that blocks the greatest number of rays;
2. create a QA-only temporary view-layer exclusion for that one object;
3. render only D evidence;
4. immediately restore its visibility in memory;
5. do not save the Blend.

Maximum temporary exclusions:
**1 architectural object**

If more than one exclusion is needed:
STOP `BLOCKED_F01_D_NO_VALID_INTEGRATED_CAMERA`

## Phase 8 — render exact evidence

Render with current integrated scene visibility.

Main file:
`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V02.png`

Resolution:
**1440×960 PNG**

Also render an audit-access preview from the exact same camera and scene state:

`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V02_PREVIEW_900x600.png`

Resolution:
**900×600 PNG**

The 900×600 preview is mandatory so GPT can inspect it through GitHub without the >1 MB binary limit.

Do not resize the rendered 1440 image after the fact.
Render both from the same camera.

## Phase 9 — image validation

For both outputs verify:
- non-black;
- image dimensions exact;
- F01 projected bbox meets coverage rule;
- >=7/9 clear rays;
- no camera-inside-mesh condition.

Write:
`F01_D_CAMERA_VALIDATION.json`

Required fields:
- exact F01 world bounds;
- exact center/extents/radius;
- failed old-camera ray table;
- failed occluder names;
- all candidate positions/targets/lenses;
- candidate rejection reasons;
- selected camera position/target/lens;
- selected 9-ray table;
- projected F01 screen bbox;
- F01 screen-area percentage;
- any temporary QA-only exclusion;
- output SHA-256/bytes/resolution;
- Blend hash before/after;
- GLB hash before/after.

## Phase 10 — immutable model check

Before commit, recompute canonical files.

Required unchanged:

Blend:
`1F2031610251CDCBD064867DB4E925CFD573C621010BDD5A72E17F45BE08D703`

GLB:
`B2972FB7F6F4B25CD4CC30615B550EAEC5A11037E56EDA3F18D9DC96F27B632D`

If either differs:
do not commit.
STOP `BLOCKED_F01_D_MODEL_MUTATION`

## Git scope

Commit ONLY:
- `F01_D_INTEGRATED_CONTEXT_V02.png`
- `F01_D_INTEGRATED_CONTEXT_V02_PREVIEW_900x600.png`
- `F01_D_CAMERA_DIAGNOSTIC.json`
- `F01_D_CAMERA_VALIDATION.json`
- exact remediation log

Do not recommit/modify Blend or GLB.
Do not edit TASKS.md.
Do not edit audit criteria.
Do not touch F02.

Create exactly:
`coordination/Logs/REV005_F01_D_INTEGRATED_CONTEXT_REMEDIATION_CODEX_LOG.md`

## STOP

Final state:
`AWAITING_GPT_F01_D_INTEGRATED_AUDIT`

Return only:
- final state
- failed old-camera primary occluder(s)
- selected new camera XYZ
- selected target XYZ
- lens
- clear-ray count / 9
- F01 projected screen coverage %
- any QA-only exclusion
- 1440×960 output path/hash
- 900×600 preview path/hash
- Blend hash unchanged confirmation
- GLB hash unchanged confirmation
- commit SHA
- full GitHub log URL
