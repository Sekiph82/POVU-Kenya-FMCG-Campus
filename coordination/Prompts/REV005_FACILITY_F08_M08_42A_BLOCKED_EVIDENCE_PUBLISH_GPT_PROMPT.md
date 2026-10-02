# M08.42A — F08 BLOCKED EVIDENCE PUBLICATION ONLY

## Scope

Publish the already-produced M08.42 / F08 blocked-state evidence to GitHub so independent GPT visual audit can inspect it.

This is **not** a remediation run.

Do not rebuild F08.
Do not change cameras.
Do not change geometry.
Do not save the staged F08 model into the canonical Blend.
Do not replace the canonical GLB.
Do not begin F09.

## Important local-state rule

The local workspace is expected to contain M08.42 F08-only uncommitted files/evidence.

Do **not** discard them.
Do **not** reset them.
Do **not** stash-and-forget them.
Do **not** fast-forward over them before inventorying them.

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

First run:
- `git status --short`
- inventory every modified/untracked file.

Classify each local change as:
- `EXPECTED_M08_42_F08_EVIDENCE_OR_HELPER`
- `UNRELATED_OR_AMBIGUOUS`

If any unrelated/ambiguous local change exists:

STOP `BLOCKED_F08_EVIDENCE_PUBLISH_LOCAL_SCOPE_AMBIGUITY`

without deleting or modifying it.

## Canonical files must remain locked

Before publication verify canonical hashes are still exactly:

Blend:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

GLB:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

If either differs:

STOP `BLOCKED_F08_EVIDENCE_PUBLISH_CANONICAL_HASH_MISMATCH`.

Do not commit either canonical binary in this task.

## Required publication set

Publish the existing M08.42 F08 evidence needed for independent audit.

At minimum commit:

### Core execution evidence
- `output/rev005-facility-gated/F08_bottle_blow/F08_VALIDATION.json`
- `coordination/Logs/REV005_F08_BOTTLE_BLOW_MOLDING_CLASS_N_CODEX_LOG.md`

### Visual evidence
Commit all existing M08.42 F08 review renders/previews, including at minimum:
- `F08_A_CONTEXT_PREVIEW_900x600.png`
- `F08_B_FUNCTIONAL_PREVIEW_900x600.png`
- `F08_C_SEQUENCE_DETAIL_PREVIEW_900x600.png`
- `F08_D_INTEGRATED_PREVIEW_900x600.png`

If corresponding 1440×960 full renders already exist, publish them too.

Do not regenerate them in this task.

### Existing validation evidence
Publish every already-produced F08 JSON that was used to support the blocked report, including when present:
- baseline hashes
- legacy inventory
- new accepted/staged manifest
- dimensional validation
- protection before/after/diff
- legacy retirement before/after/diff
- camera validation
- candidate GLB parity
- candidate/staged export validation
- any camera-candidate manifest

Do not invent missing evidence files.

### Reproduction helpers

If M08.42 created or modified F08-only source/helper scripts that are necessary to deterministically reproduce the staged 789-style Class N build workflow, publish those F08-only source files too.

Do not publish unrelated scripts.

For every such helper/source file, record it in the evidence publication log with:
- path
- purpose
- whether newly created or modified
- SHA-256 or Git blob identity where practical.

## Forbidden publication

Do not commit:
- canonical Blend
- canonical GLB
- temporary exported GLB
- Blender autosaves/backups
- caches
- unrelated files
- TASKS.md
- locked design contract
- locked GPT audit criteria

## No model mutation

Do not open/save the canonical Blend merely to publish evidence.

If Blender is currently open with the staged F08 unsaved model, do not save it over the canonical Blend.

The staged unsaved model may remain open locally if useful, but this task's Git commit must not depend on saving it.

## Publication log

Create:

`coordination/Logs/REV005_F08_M08_42A_BLOCKED_EVIDENCE_PUBLISH_CODEX_LOG.md`

Record:
- starting Git HEAD
- local status inventory
- canonical Blend/GLB hash verification
- exact published file list
- confirmation that canonical Blend/GLB were not committed or changed
- confirmation that no F09 work occurred

## Git

Commit/push the evidence-only publication to `main`.

Required commit message:

`M08.42A publish blocked F08 visual evidence`

After push verify:
- local HEAD = origin/main = live GitHub main
- worktree contains no newly-created task files left uncommitted
- any intentionally retained local-only staged Blender session is not represented as a dirty canonical binary.

## STOP

Success:

`AWAITING_GPT_F08_M08_42_VISUAL_AUDIT`
