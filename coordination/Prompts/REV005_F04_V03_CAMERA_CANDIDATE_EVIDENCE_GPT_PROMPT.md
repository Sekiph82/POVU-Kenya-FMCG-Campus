# M08.30 — F04 V03 CAMERA CANDIDATE EVIDENCE

## Scope

F04 only.

This is an evidence-only camera-selection retry after:

`BLOCKED_F04_INTERIOR_CAMERA_NO_VALID_VIEW`

The historical F04 model itself is not being redesigned.

## Sync

Work only in:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

Fetch origin/main and fast-forward-only if local main is behind.

Do not reset, rebase, force, or create another Desktop copy.

After sync, read:
- root `TASKS.md`
- `coordination/Audits/REV005_F04_V03_CAMERA_SELECTION_GPT_CRITERIA.md`
- `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`
- previous local `F04_V02_INTEGRATED_CAMERA_VALIDATION.json` if present

## Locked canonical baseline

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

These hashes must remain unchanged throughout V03.

## Historical F04 source

Use the already proven historical source contract:

- 10 BASE
- 49 V01
- total 59
- dimensional contract PASS
- archived A/B parity PASS

If prior local replay/source evidence is present and hashes/contracts match, reuse it.

Otherwise rerun the detached V01→V05 historical replay in OS temp.

## Build F04 in memory only

Open canonical Blend.

In memory:
- inventory current F04;
- remove/unlink only current conflicting F04 representation;
- append exact accepted 59 historical objects into the temporary in-memory scene;
- preserve source transforms/dimensions/materials/parents.

Do NOT save the Blend.

Do NOT export GLB.

Do NOT alter F01/F02/F03 or any neighboring facility.

## Use V02 results as seed

If local:
`output/rev005-facility-gated/F04_welfare_v02/F04_V02_INTEGRATED_CAMERA_VALIDATION.json`

exists, read it.

Extract every candidate that achieved >=7/9 clear rays.

Use the best such candidates as seed cameras.

If the file is missing, recompute the V02 interior grid only to recover >=7/9 seed candidates.

## Expanded camera search

For each >=7/9 seed candidate:

### Camera direction

Let:
- C = seed camera
- T = seed target
- V = normalized(C-T)
- d = |C-T|

Test camera distances:
- 0.70d
- 0.80d
- 0.90d
- 1.00d
- 1.10d
- 1.20d
- 1.35d

Candidate camera:
`T + V * new_distance`

Clamp/reject any point outside the legitimate pavilion interior safe volume.

### Vertical variation

Also test Z offsets:
- -0.50 m
- 0.00 m
- +0.50 m
- +0.90 m

while remaining:
- above pavilion floor safe margin
- below pavilion ceiling safe margin
- outside equipment meshes

### Target Z

Test:
- original Tz - 0.35 m
- original Tz
- original Tz + 0.35 m

Keep target inside F04 union vertical bounds.

### Lenses

Test:
- 52 mm
- 45 mm
- 40 mm
- 35 mm
- 32 mm
- 28 mm

Do not go below 28 mm.

## Hard candidate checks

A candidate is eligible only if:

1. camera point is not inside/too close to F04 equipment;
2. camera point is not inside/too close to unrelated visible equipment;
3. >=7/9 LOS rays are clear;
4. no QA-only visibility changes are used;
5. projected F04 union is fully inside:
   - X 1%–99%
   - Y 1%–99%;
6. render contains legitimate pavilion/interior context.

Do NOT reject merely because projected F04 area is outside 35–78%.

Projected area % is informational only.

## Candidate ranking

Rank eligible candidates by:

1. clear rays descending;
2. no clipping;
3. ability to show both locker/changing and shower zones together;
4. visible legitimate pavilion/interior context;
5. minimal unrelated-object obstruction;
6. lens preference for natural perspective:
   - 40 mm
   - 35 mm
   - 45 mm
   - 32 mm
   - 52 mm
   - 28 mm;
7. projected area closest to 60% as a soft preference only.

## Render top candidates

Render the top six eligible candidates at 900×600 PNG with normal current scene visibility.

Files:

`output/rev005-facility-gated/F04_welfare_v03/F04_V03_CANDIDATE_01_PREVIEW_900x600.png`

through:

`F04_V03_CANDIDATE_06_PREVIEW_900x600.png`

Do not render 1440×960 yet.

Do not save the canonical Blend.

## Evidence JSON

Create:

`output/rev005-facility-gated/F04_welfare_v03/F04_V03_CAMERA_CANDIDATES.json`

For every rendered candidate record:
- rank
- camera XYZ
- target XYZ
- lens
- clear rays / 9
- ray first-hit table
- projected F04 bbox
- projected area %
- minimum distance to unrelated visible geometry
- visible pavilion/context object names
- preview path
- SHA-256
- byte size

Also record:
- source 59-object validation
- A/B parity reuse/recheck state
- canonical Blend hash before/after
- canonical GLB hash before/after
- confirmation no model save/export occurred

## Git scope

Commit/push ONLY:
- candidate preview PNGs
- F04_V03_CAMERA_CANDIDATES.json
- `coordination/Logs/REV005_F04_V03_CAMERA_CANDIDATES_CODEX_LOG.md`

Do not commit canonical Blend/GLB because they must be unchanged.

Do not edit TASKS.md.
Do not edit locked criteria.
Do not begin F05.

## STOP

Final state:

`AWAITING_GPT_F04_V03_CAMERA_SELECTION`
