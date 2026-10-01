# M08.30 — F04 V03 SYNC + EXECUTE

The local workspace is stale at `355c258...`.

Canonical GitHub `main` authorizes F04 V03 camera-candidate evidence.

## 1. Sync safely

Work only in:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If there are unexpected staged/unstaged/untracked project changes, STOP without discarding anything.

Then:

`git fetch origin main`

If local `main` is strictly behind `origin/main` and not diverged:

`git merge --ff-only origin/main`

Do not reset, rebase, force, or create another Desktop copy.

## 2. Re-read live TASKS.md

Required active authorization after sync:

- Current Sprint: `M08.30`
- Current Task: `F04 V03 integrated-camera candidate evidence`
- Current Task Status: `READY_RETRY`
- Required Actor: `CODEX`
- Workflow State: `READY_FOR_CODEX_EXECUTION`

## 3. Execute only the current V03 prompt

`coordination/Prompts/REV005_F04_V03_CAMERA_CANDIDATE_EVIDENCE_GPT_PROMPT.md`

This is evidence-only.

Do not save canonical Blend.
Do not export/update canonical GLB.
Do not modify neighboring facilities.
Do not edit TASKS.md.
Do not begin F05.

Normal final state:

`AWAITING_GPT_F04_V03_CAMERA_SELECTION`
