# M08.30 — F04 V04 FORCED CAMERA PREVIEW EVIDENCE

## Scope

F04 only.

This is an evidence-only diagnostic task.

Previous state:
`BLOCKED_F04_V03_NO_ELIGIBLE_CANDIDATES`

The F04 model is not the problem. The purpose of V04 is to render the actual >=7/9-clear camera candidates instead of rejecting them before GPT can see them.

## Safe sync

Work only in:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect status first.

Fetch origin/main and fast-forward-only if local main is behind.

Do not reset, rebase, force, or create another Desktop copy.

Read:
1. root `TASKS.md`
2. `coordination/Audits/REV005_F04_V04_FORCED_PREVIEW_GPT_CRITERIA.md`
3. `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`
4. local V02/V03 F04 camera evidence if present

## Locked canonical files

Blend hash:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB hash:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

They must remain unchanged.

## Reconstruct F04 in memory only

Use/revalidate the proven historical source:

- 10 BASE
- 49 V01
- total 59
- dimensional contract PASS
- archived A/B parity PASS

Open canonical Blend.

In memory only:
- inventory current F04;
- replace conflicting current F04 representation with exact accepted 59 historical objects;
- preserve source transforms/dimensions/materials/parents.

Do NOT save.

Do NOT export GLB.

Do NOT touch F01/F02/F03 or neighboring facilities.

## Recover >=7/9 camera seeds

Preferred source:

`output/rev005-facility-gated/F04_welfare_v02/F04_V02_INTEGRATED_CAMERA_VALIDATION.json`

V03 reported:
- 45 V02 rows at >=7/9 clear rays
- 15 unique seeds
- 6 best seeds used

If V02 evidence exists, parse it directly.

If not, recompute the V02 interior camera grid only to recover >=7/9 seeds.

Do not apply the V02 projected-area gate.

Sort unique seeds by:
1. clear rays descending;
2. projected clipping severity ascending;
3. projected area closeness to 55% as soft preference;
4. natural lens preference 52 > 45 > 40.

## Render previews regardless of imperfect framing

### Preview 1
Best unique seed, original camera/target/lens.

### Preview 2
Second-best unique seed, original camera/target/lens.

### Preview 3
Third-best unique seed, original camera/target/lens.

### Preview 4
Same camera and target as Preview 1, lens = **35 mm**.

### Preview 5
Same camera and target as Preview 2, lens = **35 mm**.

### Preview 6
Same camera and target as Preview 3, lens = **28 mm**.

If a seed's original lens is already <35 mm:
- Preview 4/5 use 32 mm;
- Preview 6 use 28 mm.

Do not reject any of these solely for:
- projected area;
- partial clipping;
- closeness to pavilion shell;
- wide-angle distortion.

Only refuse to render a candidate if:
- camera is physically inside F04 equipment; OR
- clear rays fall below 7/9; OR
- rendering would require hiding/quarantining another object.

## Render settings

For all six:
- 900×600 PNG
- normal current integrated scene visibility
- no QA-only exclusions
- same normal material/render mode used for current facility QA

Output folder:

`output/rev005-facility-gated/F04_welfare_v04/`

Files:

- `F04_V04_CANDIDATE_01_PREVIEW_900x600.png`
- `F04_V04_CANDIDATE_02_PREVIEW_900x600.png`
- `F04_V04_CANDIDATE_03_PREVIEW_900x600.png`
- `F04_V04_CANDIDATE_04_PREVIEW_900x600.png`
- `F04_V04_CANDIDATE_05_PREVIEW_900x600.png`
- `F04_V04_CANDIDATE_06_PREVIEW_900x600.png`

## Candidate JSON

Create:

`output/rev005-facility-gated/F04_welfare_v04/F04_V04_CAMERA_PREVIEWS.json`

For each preview record:
- candidate rank
- source seed index/id
- camera XYZ
- target XYZ
- lens
- clear rays / 9
- 9-ray first-hit table
- projected bbox
- projected area %
- clipping flags
- nearest unrelated geometry distance if available
- PNG path
- SHA-256
- byte size

Also record:
- historical source count 59
- dimensional validation state
- canonical Blend hash before/after
- canonical GLB hash before/after
- confirmation no save/export/model mutation occurred

## Git scope

Commit/push ONLY:
- six preview PNGs (or all renderable previews if fewer)
- `F04_V04_CAMERA_PREVIEWS.json`
- `coordination/Logs/REV005_F04_V04_FORCED_PREVIEW_CODEX_LOG.md`

Do NOT commit Blend/GLB.
Do NOT edit TASKS.md.
Do NOT edit criteria.
Do NOT begin F05.

## STOP

Final state:

`AWAITING_GPT_F04_V04_PREVIEW_REVIEW`
