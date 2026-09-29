# F02 LOCAL SYNC + EXECUTE HANDOFF

The previous attempt stopped because the local checkout was stale.

Canonical GitHub main already authorizes F02.

## Local synchronization

Work only in:

C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus

First inspect local Git status. If there are unexpected local project changes, stop and report them without discarding anything.

Synchronize the local main branch with the current origin/main using fetch followed by fast-forward-only synchronization.

Do not create another Desktop project copy.

If local main has diverged from origin/main, stop and report:
BLOCKED_F02_LOCAL_SYNC_DIVERGED

After synchronization, re-read local root TASKS.md.

Required authorization:
- Current Sprint: M08.26
- Current Task: Facility-Gated F02 Daycare / Crèche historical restoration
- Current Task Status: READY
- Required Actor: CODEX
- Workflow State: READY_FOR_CODEX_EXECUTION

Verify these files now exist locally:
- coordination/Prompts/REV005_FACILITY_F02_DAYCARE_RESTORE_GPT_PROMPT.md
- coordination/Audits/REV005_FACILITY_F02_DAYCARE_GPT_AUDIT_CRITERIA.md
- coordination/Audits/REV005_F02_DAYCARE_HISTORICAL_SOURCE_PROVENANCE.md

If any is missing after synchronization, stop:
BLOCKED_F02_SYNC_ARTIFACT_MISSING

## Execute

Once the local checkout matches origin/main and F02 authorization is confirmed, execute only:

coordination/Prompts/REV005_FACILITY_F02_DAYCARE_RESTORE_GPT_PROMPT.md

Follow the locked F02 audit criteria exactly.

Protect F01 and the historical Glass Deck source.
Keep the V09 Glass Deck replacement quarantined.
Do not begin F03.
Do not edit TASKS.md.

Normal final state:
AWAITING_GPT_FACILITY_AUDIT_F02
