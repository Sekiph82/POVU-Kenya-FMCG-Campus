# M08.30 — F04 V02 LOCAL SYNC + EXECUTE

The previous F04 run used the superseded exterior 8-azimuth collision gate.

Canonical GitHub main already authorizes the corrected F04 V02 interior-contained camera workflow.

## 1. Sync safely

Work only in:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If there are unexpected local changes, stop without discarding them.

Then:

`git fetch origin main`

If local main is strictly behind origin/main and not diverged:

`git merge --ff-only origin/main`

Do not reset, rebase, force, or create another Desktop copy.

## 2. Re-read live TASKS.md

Required authorization after sync:

- Current Sprint: `M08.30`
- Current Task: `Facility-Gated F04 welfare historical restoration V02 interior-camera retry`
- Current Task Status: `READY_RETRY`
- Required Actor: `CODEX`
- Workflow State: `READY_FOR_CODEX_EXECUTION`

## 3. Execute the corrected F04 V02 prompt only

`coordination/Prompts/REV005_FACILITY_F04_WELFARE_RESTORE_GPT_PROMPT.md`

Important:

Do NOT use the old exterior 8-azimuth ring as the final integrated-camera gate.

Use the interior pavilion camera grid defined in the current prompt and locked V02 audit criteria.

Do not quarantine or modify Wellness, Training, Restaurant, WELLNESS_PAVILION, WELLNESS_GLASS, or any neighboring facility.

Protect F01/F02/F03.

Do not edit TASKS.md.

Do not begin F05.

Normal final state:

`AWAITING_GPT_FACILITY_AUDIT_F04`
