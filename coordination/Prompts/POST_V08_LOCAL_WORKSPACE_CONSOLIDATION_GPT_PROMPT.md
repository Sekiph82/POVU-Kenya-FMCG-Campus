# POST-V08 LOCAL WORKSPACE CONSOLIDATION — CANONICAL PATH NORMALIZATION

## Execution timing — mandatory

This is a **queued follow-up task**.

Do **NOT** interrupt, pause, cancel, restart, or otherwise alter the currently active M08.16 / REV005 Interior Remediation V08 execution.

First finish M08.16 exactly as instructed by its current prompt, produce/push all required V08 artifacts, and reach:

`AWAITING_GPT_REMEDIATION_AUDIT_V08`

Only **after** that state has been reached and the V08 work has been safely committed/pushed may you execute this workspace-consolidation task.

The final project state after this maintenance task must still remain:

`AWAITING_GPT_REMEDIATION_AUDIT_V08`

Do not begin M08.17 audit work yourself.

## Owner objective

There are currently two desktop folders:

1. `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`
2. `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

The owner wants **one and only one canonical local project folder**:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

After careful reconciliation, the redundant folder:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`

must be removed.

Do not create any additional permanent project folder on the Desktop.

## Core safety rule

This is a **merge/reconciliation operation, not a blind rename or delete**.

Before deleting anything, inspect both folders thoroughly and prove that no unique or newer project data will be lost.

Forbidden shortcuts:

- no `git reset --hard` to erase local work;
- no force-push;
- no blind recursive overwrite;
- no deleting either folder before reconciliation is complete;
- no replacing one `.git` directory with another without first establishing which repository metadata is authoritative;
- no assuming files are duplicates based only on filename;
- no deleting ignored/untracked assets merely because they are not in Git;
- no creating a third permanent Desktop copy as a backup;
- no rewriting historical logs merely to change old path references.

Temporary working data may use a system temp location if genuinely necessary, and must be cleaned up after successful verification.

## Phase 1 — establish the truth of both folders

Inspect both folders and record:

- whether each is a Git repository;
- repository root;
- `origin` URL;
- current branch;
- HEAD SHA;
- relationship to `origin/main`;
- staged changes;
- unstaged changes;
- untracked files;
- ignored files that are materially part of the project;
- submodules/worktrees if any;
- top-level directory/file inventory;
- file counts and sizes;
- unique files in each folder;
- same-path files whose contents differ;
- important large local artifacts not tracked by Git;
- whether either folder contains files newer than the other version of the same logical artifact.

Use hashes for ambiguous same-name/same-size files when needed.

Determine why two folders exist if the evidence makes that clear, but do not guess.

## Phase 2 — protect the just-completed V08 state

The workspace containing the completed M08.16/V08 work is authoritative for the just-finished V08 mutations unless comparison proves that another copy contains additional non-conflicting owner data.

Before any consolidation:

1. verify V08 is fully committed;
2. verify the V08 commit is pushed to `origin/main`;
3. fetch remote state;
4. verify the active local branch is not ahead/behind unexpectedly;
5. preserve every required V08 local binary/QA artifact that repository policy intentionally leaves untracked/ignored.

Do not lose any Blend, GLB, QA, validation, report, hash, or local source artifact created by V08.

## Phase 3 — reconcile into the owner-selected canonical folder

Canonical destination:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Merge the useful contents of both existing folders into that destination.

Rules:

- preserve the valid Git history and the correct `origin` connection for `Sekiph82/POVU-Kenya-FMCG-Campus`;
- preserve all unique project files from both folders;
- for conflicting same-path files, compare Git ancestry, timestamps, hashes, content and V08 provenance before deciding;
- never silently discard a divergent file;
- if one version is superseded but contains unique information, preserve that information in the canonical workspace or its proper project history before removal;
- maintain the repository's existing policy for large local binaries;
- do not upload huge/generated local artifacts to GitHub merely because folders are being merged;
- do not create duplicate copies of the same large artifact unless required to prevent data loss.

If the canonical destination already contains its own valid `.git`, reconcile repository state safely rather than nesting one repo inside another.

If only the `-repo` folder is the valid Git repository, migrate that repository identity safely into the owner-selected canonical destination.

At the end there must be no nested duplicate project root such as:

`POVU-Kenya-FMCG-Campus\POVU-Kenya-FMCG-Campus-repo`

## Phase 4 — normalize active canonical path references

The canonical local workspace from now on is exactly:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Search the active repository/configuration/scripts/current tracker for operational references to:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`

Update **current operational references** to the new canonical path where appropriate.

This includes, where relevant:

- root `TASKS.md` canonical local workspace statement;
- active scripts/configuration;
- current handoff/readme instructions that define the live workspace;
- automation/helper scripts that rely on an absolute project root.

Do **not** rewrite historical Codex logs, historical audit evidence, old prompts, or provenance records merely because they truthfully recorded the old path at the time.

Do not create a `.hiveai` file or folder.

## Phase 5 — GitHub synchronization

After reconciliation:

1. work only from `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`;
2. confirm `origin` points to the correct GitHub repository;
3. fetch `origin`;
4. reconcile any legitimate local changes created by this maintenance task;
5. commit current-path/tracker/maintenance changes with a clear commit message if needed;
6. push to `main`;
7. verify local `HEAD` == `origin/main`;
8. verify `git status` is clean, except for intentionally local/ignored large artifacts allowed by repository policy.

Do not force-push.

## Phase 6 — deletion gate for the redundant folder

Only delete:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`

after ALL of the following are proven:

- the canonical destination opens as the correct repository;
- `origin` is correct;
- local HEAD matches `origin/main`;
- no staged/unstaged/untracked project file remains uniquely stranded in the old folder;
- no ignored but important local artifact remains uniquely stranded there;
- V08 Blend/GLB/QA/report/validation/provenance artifacts remain available at their intended canonical paths;
- a final source-vs-destination comparison finds no owner/project data that exists only in the old folder;
- the canonical workspace contains the complete merged project;
- current operational path references use the new canonical folder.

Then remove the redundant `-repo` folder completely.

Do not remove the owner-selected canonical folder.

## Required lightweight evidence

Create and commit:

`coordination/Logs/POST_V08_LOCAL_WORKSPACE_CONSOLIDATION_CODEX_LOG.md`

The log must include:

- confirmation that M08.16 was finished first and was not interrupted;
- pre-merge identity/status of both folders;
- which folder contained the authoritative Git metadata before merge;
- summary of unique/conflicting files found;
- reconciliation actions taken;
- important untracked/ignored local artifacts preserved;
- confirmation of new canonical path;
- current operational files updated for the path change;
- deletion-gate checks;
- confirmation that the old `-repo` folder was removed;
- final branch;
- final local HEAD SHA;
- `origin/main` SHA;
- final Git status;
- final canonical local path;
- GitHub log URL.

Do not commit a giant full filesystem listing. Summarize only the evidence needed to prove no loss and correct synchronization.

## Final required state

Exactly one desktop project root remains:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

The repository and GitHub `main` are synchronized.

The old folder:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`

no longer exists.

The project workflow state remains:

`AWAITING_GPT_REMEDIATION_AUDIT_V08`

## Return only

- confirmation that M08.16/V08 finished before this task began
- canonical local path
- old folder deletion status
- reconciliation summary: unique/conflicting files preserved
- final local HEAD SHA
- `origin/main` SHA
- Git status
- commit SHA for this maintenance task
- full GitHub Codex log URL
