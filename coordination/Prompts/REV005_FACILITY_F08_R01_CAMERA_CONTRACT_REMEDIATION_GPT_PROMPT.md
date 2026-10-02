# M08.43 — F08-R01 CAMERA-CONTRACT REMEDIATION + CONDITIONAL CANONICAL PROMOTION

## Scope

Execute F08-R01 only.

This task exists because M08.42 built a technically valid staged F08 model but failed the visual gate due camera composition.

This task is **camera/evidence-first**.

Do not begin F09.

Do not alter F08 geometry unless a new hard geometric contradiction is proven. If a contradiction appears, stop and publish evidence.

## Read first

1. root `TASKS.md`
2. `coordination/Audits/REV005_F08_M08_42_GPT_VISUAL_AUDIT.md`
3. `coordination/Audits/REV005_F08_R01_CAMERA_REMEDIATION_GPT_CRITERIA.md`
4. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md`
5. `coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_GPT_AUDIT_CRITERIA.md`
6. `coordination/Logs/REV005_F08_BOTTLE_BLOW_MOLDING_CLASS_N_CODEX_LOG.md`
7. `coordination/Logs/REV005_F08_M08_42A_BLOCKED_EVIDENCE_PUBLISH_CODEX_LOG.md`
8. all published M08.42 F08 JSON/previews/helpers under:
   `output/rev005-facility-gated/F08_bottle_blow/`

## Mandatory sync first

At the very beginning:

1. inspect `git status --short`;
2. inventory any ignored/local F08 staged files that may still exist;
3. fetch `origin/main`;
4. fast-forward-only the canonical checkout to current `origin/main`;
5. re-read local root `TASKS.md`.

Do not reset, rebase, force, delete, or overwrite owner-local files.

If unexpected unrelated local changes exist:

STOP `BLOCKED_F08_R01_LOCAL_SCOPE_AMBIGUITY`.

After sync, `TASKS.md` must authorize:

`M08.43 — F08-R01 camera-contract remediation`

If not:

STOP `BLOCKED_F08_R01_TRACKER_MISMATCH`.

## Locked canonical baseline before promotion

Canonical Blend:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

Canonical GLB:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

Verify both before work.

If either differs:

STOP `BLOCKED_F08_R01_CANONICAL_BASELINE_MISMATCH`.

## Recover the exact staged F08 state

Preferred local staged file:

`output/rev005-facility-gated/F08_bottle_blow/F08_STAGED.blend`

If it still exists, do **not** trust it blindly.

Validate it against the published M08.42 evidence:

- destination collection exists;
- expected staged F08 object count/signatures match `F08_NEW_ACCEPTED_MANIFEST.json`;
- 391 confirmed F08 legacy objects have the expected staged retirement state;
- 5 NOT_F08 candidates remain unchanged;
- 20 preforms;
- 16 heater elements, 8 per bank;
- 2 service doors;
- 4 HP-air branches;
- 16 formed bottles;
- protection diff remains zero unauthorized differences;
- dimensional anchors remain PASS;
- cross-facility collisions remain zero.

If the local staged file does not pass all checks, reconstruct the staged model **deterministically from the locked canonical baseline** using the published F08-only helpers.

Do not reconstruct by freehand editing.

Published helpers include:
- `F08_preflight_snapshot.py`
- `F08_build_scene.py`
- `F08_visual_refine.py`
- `F08_camera_context_adjust.py`
- `F08_camera_diagnostic.py`
- `F08_render_previews.py`

Reconstruction must be into an ignored/local staged file, not the canonical Blend.

Write:

`output/rev005-facility-gated/F08_bottle_blow/R01/F08_R01_STAGED_STATE_VALIDATION.json`

## Locked staged technical facts

R01 must preserve these accepted staged facts:

- legacy confirmed = 391
- legacy ambiguous = 0
- NOT_F08 preserved = 5
- protected-object unauthorized differences = 0
- cross-facility collisions = 0
- preforms = 20
- heater elements = 16
- heater elements per bank = 8/8
- blow-cell service doors = 2
- HP-air branches = 4
- formed bottles = 16
- north service aisle clear
- south operator aisle clear
- all accepted new F08 geometry inside locked F08 envelope
- deterministic GLB candidate parity = 10,888 expected / 10,888 actual
- missing expected names = 0
- unexpected names = 0

No geometry mutation is authorized to improve screenshots.

## Why the old camera contract is superseded

M08.42 was restricted to small refinements around four original camera seeds.

That restriction caused:
- A_CONTEXT to land behind/inside an opaque architectural obstruction;
- B/C to crop or compress the heater→transfer→blow-cell→outfeed relationship;
- D to show the line but not establish the complete process sequence cleanly.

For R01, the old ±3 m seed limit is removed.

## Camera rules

Camera may be anywhere:
- inside the F08 room envelope; or
- immediately outside a glazed/open frontage,

provided:
- camera origin is outside every object bounding box;
- no camera is inside a wall/soffit/floor/equipment;
- no near-plane slicing;
- no temporary object hiding;
- no new quarantine;
- no saved visibility mutation;
- no clipping tricks.

Sensor width:

36 mm

Allowed lens range:

16–35 mm

## Search strategy

Do not do one random broad sweep.

Use four role-specific search families and render actual 900×600 previews.

### Family A — complete side-on / south-aisle context

Highest priority.

Search around these camera ranges:

- X = 48…56
- Y = -0.5…4.5
- Z = 5.0…7.5

Target ranges:

- X = 50…55
- Y = 9…11
- Z = 2.6…3.4

Lens:

- 16 / 18 / 20 / 22 / 24 mm

Also test south-west oblique:

- camera X = 36…44
- Y = 0…5
- Z = 5…7
- target X = 54…60
- Y = 9…11
- Z = 2.6…3.4
- lens 16…24 mm

A must place hopper/feed, oven, blow cell and outfeed in one readable sequence.

### Family B — heater/transfer/blow functional view

Search:

- camera X = 43…51
- Y = 1.5…5.5
- Z = 4.5…7.0

Targets:

- X = 54…59
- Y = 9…11
- Z = 2.6…3.5

Lens:

- 18 / 20 / 22 / 24 / 28 / 32 mm

B must show:
- heater outlet;
- transfer/starwheel/guide;
- blow-cell structure;
- at least one mould station;
- outfeed with formed bottles.

### Family C — sequence-detail view

Search:

- camera X = 48…55
- Y = 2.5…6.0
- Z = 3.8…6.0

Targets:

- X = 56…61
- Y = 9…11
- Z = 2.5…3.5

Lens:

- 20 / 22 / 24 / 26 / 28 / 30 / 32 mm

C must include in one frame:
- oven or oven exit;
- physical transfer;
- readable clamp/mould/stretch-blow cues;
- formed-bottle discharge or immediate outfeed.

### Family D — integrated line + operator/service

Search both south-side and north/service-side perspectives.

South family:
- camera X = 40…54
- Y = 0…4.5
- Z = 6…8

North family:
- camera X = 40…54
- Y = 16…20
- Z = 6…8

Targets:
- X = 52…57
- Y = 9…11
- Z = 2.8…3.5

Lens:
- 16 / 18 / 20 / 22 / 24 mm

D must show:
- hopper/feed;
- oven;
- blow cell;
- outfeed;
- HMI/operator side or clear operator/service relationship;
- main aisle organization;
- legitimate room context.

## Candidate volume

Render at least:

- 36 A candidates
- 30 B candidates
- 30 C candidates
- 36 D candidates

Total minimum:

132 candidate previews

You may stop a family early only after at least 18 candidates if you have three obviously superior passing views and have documented why more search is unnecessary.

Do not select from metadata alone.

Actually inspect the rendered previews.

## Candidate scoring

For each candidate record:

- candidate ID
- role A/B/C/D
- camera XYZ
- target XYZ
- lens
- camera-inside-geometry = false
- wall/ceiling/floor clipping = false
- hopper visible
- feeder/preform path visible
- heater oven visible
- heater outlet visible
- transfer visible
- blow-cell frame visible
- mould station readable
- stretch/blow cue readable
- outfeed visible
- formed bottles readable
- HMI/operator relationship visible
- aisle/context readable
- dominant occluder
- black-field fraction qualitative flag
- label-blind process sequence PASS/FAIL
- preview path

Write:

`R01/F08_R01_CAMERA_CANDIDATES.json`

## Top-candidate publication

For independent audit, do not commit all 132+ previews unless necessary.

For each role, retain and publish the strongest 12 candidate previews:

- A top 12
- B top 12
- C top 12
- D top 12

Also create one 4×3 contact sheet per role:

- `F08_R01_A_TOP12_CONTACT_SHEET.png`
- `F08_R01_B_TOP12_CONTACT_SHEET.png`
- `F08_R01_C_TOP12_CONTACT_SHEET.png`
- `F08_R01_D_TOP12_CONTACT_SHEET.png`

Each cell must include a small candidate ID caption.

Contact sheets are evidence only; final acceptance is based on the actual selected frame.

## Hard visual selection criteria

### A_CONTEXT selected candidate

Must clearly show:
- hopper/feed;
- heater/oven;
- blow cell;
- formed-bottle outfeed;
- floor/enclosure;
- west→east process order.

No wall or black field may dominate.

### B_FUNCTIONAL selected candidate

Must clearly show:
- heater outlet;
- transfer;
- blow cell;
- at least one mould station;
- outfeed;
- enough upstream/downstream context to understand process direction.

### C_SEQUENCE_DETAIL selected candidate

Must clearly show:
- heater/transfer relation;
- clamp/mould/stretch-blow mechanism;
- formed-bottle discharge/outfeed;
- physical adjacency between steps.

No panel-only framing.

### D_INTEGRATED selected candidate

Must clearly show:
- hopper/feed;
- heater;
- blow cell;
- outfeed;
- HMI/operator or service relationship;
- aisle organization;
- legitimate room context.

## No single-frame absolutism

A/B/C/D are complementary roles.

Do not require A or D alone to show microscopic mould detail.

Do not require C to show the entire room.

But the four selected views **together** must prove the complete label-blind process:

`preforms → heating → transfer → mould/blow forming → formed bottles`

## Visual success gate before canonical save

Before any canonical save, produce provisional selected previews:

- `R01/F08_R01_A_SELECTED_PREVIEW_900x600.png`
- `R01/F08_R01_B_SELECTED_PREVIEW_900x600.png`
- `R01/F08_R01_C_SELECTED_PREVIEW_900x600.png`
- `R01/F08_R01_D_SELECTED_PREVIEW_900x600.png`

Write:

`R01/F08_R01_VISUAL_SELECTION.json`

Every required role must be PASS.

If any role fails:

1. do not save canonical Blend;
2. do not replace canonical GLB;
3. commit/push the R01 candidate JSON, top-12 previews/contact sheets, selected-attempt previews, and R01 log;
4. stop:

`BLOCKED_F08_R01_NO_COMPLETE_VISUAL_SET`.

This blocked evidence must be published in the same run. Do not require another evidence-publication task.

## Technical revalidation before promotion

Only after A/B/C/D all visually PASS:

Re-run:
- staged manifest signature validation;
- dimensional validation;
- F01-F07 protection diff;
- legacy retirement exact diff;
- cross-facility collision check;
- F08 counts;
- deterministic GLB membership candidate export.

Require the same staged technical facts as M08.42.

Write:

- `R01/F08_R01_TECHNICAL_REVALIDATION.json`
- `R01/F08_R01_PROTECTION_DIFF.json`
- `R01/F08_R01_GLB_PARITY_PREPROMOTION.json`

Any regression:

STOP `BLOCKED_F08_R01_TECHNICAL_REGRESSION`

without canonical promotion.

## Canonical promotion

Only after visual + technical gates PASS:

Promote the exact validated staged state to:

`3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Do not rebuild again after visual selection.

Save the exact validated state.

Then export canonical GLB using deterministic membership parity.

Do not use broad `use_visible=True`.

Expected membership remains:

- pre-F08 accepted GLB membership
- minus exact 391 retired F08 legacy node names
- plus exact new accepted F08 exportable mesh names

Current staged candidate expectation:

10,888 named nodes

Require:
- actual = expected
- zero missing expected names
- zero unexpected names
- all accepted F01-F07 names preserved
- all intended F08 names present
- all exact retired F08 legacy names absent

If GLB parity fails after Blend promotion:

restore the locked pre-F08 GLB;
do not publish a lossy GLB;
STOP `BLOCKED_F08_R01_FINAL_GLB_PARITY`.

## Final canonical renders

After successful canonical save and GLB parity:

Reopen the saved canonical Blend.

Verify:
- exact selected A/B/C/D camera transforms;
- no visibility drift;
- protection still PASS;
- 391 retired F08 legacy state preserved;
- 5 NOT_F08 preserved.

Render final:

- `F08_A_CONTEXT.png` 1440×960
- `F08_B_FUNCTIONAL.png` 1440×960
- `F08_C_SEQUENCE_DETAIL.png` 1440×960
- `F08_D_INTEGRATED.png` 1440×960

and previews:

- `F08_A_CONTEXT_PREVIEW_900x600.png`
- `F08_B_FUNCTIONAL_PREVIEW_900x600.png`
- `F08_C_SEQUENCE_DETAIL_PREVIEW_900x600.png`
- `F08_D_INTEGRATED_PREVIEW_900x600.png`

These final previews must be rendered from the saved canonical Blend, not the pre-promotion staged file.

## Final validation

Create:

- `R01/F08_R01_FINAL_HASHES.json`
- `R01/F08_R01_FINAL_GLB_PARITY.json`
- `R01/F08_R01_FINAL_SAVED_STATE_VALIDATION.json`
- `R01/F08_R01_VALIDATION.json`

Record:
- new Blend SHA-256
- new GLB SHA-256
- expected/actual GLB node membership
- selected cameras
- all visual cue booleans
- protection result
- exact legacy retirement count
- F09 not started

## Required log

Write:

`coordination/Logs/REV005_F08_R01_CAMERA_CONTRACT_REMEDIATION_CODEX_LOG.md`

Include:
- sync/preflight
- staged-state source/reconstruction path
- candidate counts by role
- top selections
- direct visual rationale
- technical revalidation
- canonical promotion result or blocked stop
- final hashes if promoted
- exact evidence paths

## Git scope

If blocked before promotion, commit/push:
- R01 candidate JSON
- strongest candidate previews/contact sheets
- selected-attempt previews
- R01 validation
- R01 log
- any R01-only helper scripts

If successful, additionally commit/push:
- canonical Blend
- canonical GLB
- final A/B/C/D full renders and previews
- all final R01 validation files

Do not edit root `TASKS.md`.
Do not edit locked audit/design criteria.
Do not begin F09.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F08_R01`
