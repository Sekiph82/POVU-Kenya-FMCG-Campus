# REV005 INTERIOR REMEDIATION V09 — IMAGE-BY-IMAGE EXECUTION MASTER

## Entering state

V08 independent GPT audit: `REMEDIATION_REQUIRED`

V08 failed **72/72** supplied integrated/preservation image checks. The six previously accepted groups also regressed to twelve 100% black renders.

## Canonical workspace

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Do not create another Desktop project copy.

## Read in order

1. root `TASKS.md`
2. `coordination/Audits/REV005_INTERIOR_REMEDIATION_V08_GPT_AUDIT.md`
3. `coordination/Remediation/V09_Image_Specs/INDEX.md`
4. all 72 image specs in numeric order
5. `coordination/Audits/REV005_INTERIOR_REMEDIATION_V09_GPT_AUDIT_CRITERIA.md`

The V09 criteria are locked.

## Immutable baseline before mutation

Capture V08-final hashes into:

`output/rev005-interior-remediation-v09/V09_BASELINE_HASHES.json`

Expected:
- Blend: `9860D83DD2799B195EF79617B7F37774DA21FF09C61B7AA6C91F8375263D801A`
- GLB: `57CEE672E093D766A67D141754092739A0E6F4EE8E76261C0366BFCD936808A0`

Commit this file before modifying the canonical Blend/GLB. Never overwrite the before values.

## Execution method

Do not perform another broad "improve interiors" pass.

For each remediation facility:
1. read A_CONTEXT spec;
2. fix major layout/envelope and A camera;
3. read B_FUNCTIONAL spec;
4. refine functional assembly and B camera;
5. read C_SEQUENCE_OR_DETAIL spec;
6. refine connected sequence/detail and C camera;
7. re-render A/B/C together;
8. compare each render to its exact spec;
9. keep correcting until all three visually satisfy their specs;
10. only then move on.

For preserved groups:
1. read A/B specs;
2. diagnose V08 black-frame regression;
3. restore only that facility's accepted render/view-layer visibility, lighting and camera proof;
4. do not redesign unless a true geometry regression is proven;
5. never globally unhide the retired legacy set.

## Hard rules

- No label/object-name/filename counts as proof.
- No featureless cuboid represents a whole machine or room function.
- No panel-only, wall-only, tank-shell-only or empty-floor QA.
- No camera inside geometry or blocked by a foreground object.
- Do not stack a new generic proxy layer; edit/replace V08 clean subassemblies in place.
- Do not globally restore the 62,130 V08-retired objects.
- Do not edit `TASKS.md` or locked V09 criteria.
- Do not touch REV004, create REV006, create a tour/video or create `.hiveai`.

## Render standard

Regenerate:
- 60 remediation integrated A/B/C views;
- 12 preserved A/B views;
- 20 isolated label-blind proofs.

Total: **92 PNGs**.

Minimum resolution: **1280×800**.

Folders:
- `output/rev005-interior-remediation-v09/qa/`
- `output/rev005-interior-remediation-v09/qa_isolated/`

Use sufficient neutral QA lighting to read geometry. Black background must not swallow silhouettes. Validate camera bounds/line-of-sight before rendering.

## Required artifacts

Create:
- `output/rev005-interior-remediation-v09/V09_BASELINE_HASHES.json`
- `output/rev005-interior-remediation-v09/REV005_INTERIOR_REMEDIATION_V09_REPORT.md`
- `output/rev005-interior-remediation-v09/REV005_INTERIOR_REMEDIATION_V09_VALIDATION.json`
- `output/rev005-interior-remediation-v09/REV005_INTERIOR_REMEDIATION_V09_ACCEPTANCE_MATRIX.md`
- `output/rev005-interior-remediation-v09/V09_IMAGE_SPEC_EXECUTION_MATRIX.md`
- `coordination/Logs/REV005_INTERIOR_REMEDIATION_V09_CODEX_LOG.md`

The execution matrix must include all 72 spec IDs, source image, V09 output, implementation summary, camera change, dimensions and non-black validation. Codex readiness is not GPT acceptance.

## Final validation

Verify 72/72 specs executed, 72/72 integrated/preservation PNGs non-black, 20/20 isolated proofs non-black, 92/92 renders >=1280×800, six preserved groups visible, no camera-inside failures, REV004 unchanged, canonical workspace unchanged, and local Git synchronized/clean after push.

## Stop gate

Stop at:

`AWAITING_GPT_REMEDIATION_AUDIT_V09`

Return only:
- final state
- 72-spec execution readiness
- 20 isolated-proof readiness
- 26-group readiness
- 92-render readiness
- Blend path
- GLB path
- QA folder
- isolated QA folder
- V09 baseline path
- final Blend/GLB hashes
- commit SHA
- full GitHub Codex log URL
