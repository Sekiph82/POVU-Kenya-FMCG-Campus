# M08.35 — F05-R01 FIRE PUMP HOUSE INTEGRATED VIEW + PROTECTION EVIDENCE REMEDIATION

## Scope

Execute F05-R01 only.

This is a narrow remediation of the independent GPT audit failure recorded in:

`coordination/Audits/REV005_F05_FIRE_PUMP_GPT_AUDIT_V01.md`

Do not begin F06.

Do not rebuild the already-proven 123-object historical source.
Do not alter the accepted 54-object F05 primary geometry unless an independently verifiable protection correction explicitly authorized below requires a saved visibility-only change.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_FACILITY_F05_FIRE_PUMP_GPT_AUDIT_CRITERIA.md`
4. `coordination/Audits/REV005_F05_FIRE_PUMP_GPT_AUDIT_V01.md`
5. `coordination/Logs/REV005_F05_FIRE_PUMP_RESTORE_CODEX_LOG.md`
6. all committed F05 evidence under `output/rev005-facility-gated/F05_fire_pump/`

## Safe synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If unexpected local changes exist, STOP without discarding them.

Fetch and fast-forward-only to current `origin/main`.

No reset.
No rebase.
No force.
No second Desktop copy.

Re-read root `TASKS.md` after sync.

It must authorize M08.35 / F05-R01 only.

## Locked current F05 model

The current accepted-for-remediation F05 canonical model must begin with:

Blend SHA-256:
`E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`

GLB SHA-256:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If either mismatches before any model mutation:

STOP `BLOCKED_F05_R01_CANONICAL_HASH_MISMATCH`.

## Already-passed gates — preserve, do not redo casually

Treat these as locked PASS unless new evidence proves a contradiction:

- historical V05 selection total = 123
- PRIMARY = 54
- SECONDARY = 69
- contribution counts
- dimensional contract
- historical source A/B/C decoded parity
- destination A/B/C structural parity
- destination collection count = 54

Do not replace the F05 primary geometry merely to improve the camera.

## Failure 1 — integrated D visual evidence

The previous selected D preview used historical A and achieved 9/9 LOS, but failed visual readability because large overhead/slab elements materially obscured the functional cluster.

The remediation must prove:

- both primary pump housings are clearly visible;
- both pump bases are visible enough to read the equipment arrangement;
- suction/header network is readable;
- multiple valves are readable;
- control panel is visibly identifiable;
- service/access organization can be understood;
- no large unrelated structural element dominates or slices through the core functional view;
- the primary cluster is not materially clipped;
- legitimate current context remains visible;
- camera is not inside equipment or geometry;
- no QA-only hiding/quarantine is used for the final integrated view;
- no neighbor facility is mutated.

A LOS score is necessary but not sufficient.

## Camera search

Evaluate, at minimum:

1. historical A
2. historical B
3. historical C
4. at least six nearby/interior alternatives

Nearby/interior alternatives may move around the Fire Pump House room and may use a lower interior eye level if that improves system readability.

For every candidate:

- render a true integrated preview at 900×600;
- use the current saved model state;
- do not hide roof/walls/slabs/equipment merely for the candidate;
- camera must not intersect geometry;
- cast the same 9 primary-facility LOS rays;
- require >=7/9 clear rays;
- record camera XYZ, target XYZ, lens, clear-ray count and blocker names;
- record whether both pumps, bases, header/suction, valves, panel and access organization are visible.

Do not auto-select the first 9/9 camera.

Rank candidates by:

1. actual functional visual readability;
2. absence of material occlusion;
3. both-pump + panel + piping completeness;
4. natural perspective;
5. clear-ray count;
6. historical-camera proximity.

## Candidate evidence

Create:

`output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_CAMERA_CANDIDATES.json`

and at least nine 900×600 previews:

`F05_R01_CANDIDATE_01_900x600.png`
through
`F05_R01_CANDIDATE_09_900x600.png`

More are allowed if useful.

Keep each review preview practical for independent connector review. Do not replace these with only 1440×960 files.

If no candidate meets the full visual requirement:

STOP `BLOCKED_F05_R01_INTEGRATED_VIEW`

and do not change canonical geometry.

## Failure 2 — Restaurant right-wall protection evidence

The previous committed manifests contain an inconsistency:

`F05_PROTECTION_BEFORE.json`
reports:
`quarantine_state.restaurant_right_wall = false`

`F05_PROTECTION_AFTER.json`
reports:
`quarantine_state.restaurant_right_wall = true`

while the recorded `V09_RESTAURANT_RIGHT_WALL` object payload is otherwise unchanged.

Resolve this by evidence, not assumption.

### Authoritative references

Use:

- pre-F05 repository/model baseline commit:
  `4fd49a647224727139f45016fa21d5c1ca724418`
- accepted F04-X01 quarantine execution:
  `674a6bf`
- accepted F04-X03 evidence-only closure:
  `0fb3ff0`
- current F05 canonical state

Inspect the exact Restaurant right-wall state at all relevant levels:

- object `hide_render`
- object `hide_viewport`
- object custom properties
- owning collection(s) `hide_render`
- owning collection(s) `hide_viewport`
- view-layer / LayerCollection exclude or hide state where applicable
- collection/object linkage

Also verify the existing Glass Deck and Training quarantine states.

Write:

`output/rev005-facility-gated/F05_fire_pump/R01/F05_R01_PROTECTION_STATE_AUDIT.json`

The JSON must explicitly state whether the old false→true delta was:

- `MANIFEST_DERIVATION_BUG_ONLY`, or
- `REAL_CANONICAL_PROTECTION_MUTATION`.

### If it is a manifest derivation bug only

Do not mutate the model.

Fix only the evidence-generation logic used for this R01 proof and produce a correct exact-state comparison.

### If it is a real canonical protection mutation

Restore only the precise accepted F04 quarantine visibility/linkage state proven by the accepted F04 references.

Do not change:
- transforms
- dimensions
- mesh data
- materials
- unrelated visibility
- any other facility

Then re-run all protected-state comparisons.

If the accepted F04 reference itself is contradictory or cannot be proven:

STOP `BLOCKED_F05_R01_PROTECTION_STATE_AMBIGUOUS`.

## Protection gate after remediation

Require exact protected-state parity for:

- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- V09 Restaurant right-wall accepted quarantine state
- historical Glass Deck source
- historical Wellness/pavilion protected state

Create:

- `F05_R01_PROTECTION_REFERENCE.json`
- `F05_R01_PROTECTION_CURRENT.json`
- `F05_R01_PROTECTION_DIFF.json`

The diff must end with zero unauthorized protected-state differences.

## Final integrated selection

Once a visually valid candidate exists, select the best one as R01 D.

Produce:

- `D_INTEGRATED_CONTEXT_R01.png` at 1440×960
- `D_INTEGRATED_CONTEXT_R01_PREVIEW_900x600.png`

The preview must be generated from the exact same camera and saved model state.

Also produce:

`F05_R01_INTEGRATED_CAMERA_VALIDATION.json`

Record:
- selected candidate;
- camera/target/lens;
- 9 LOS rays;
- blocker list;
- visual cue booleans;
- no-QA-hide assertion;
- no-neighbor-mutation assertion.

## Regression checks

Before save/push, re-confirm:

- F05 destination collection remains exactly 54;
- no SECONDARY 69 object was appended into the primary accepted collection;
- F05 primary object transforms/dimensions/materials/parents remain unchanged;
- F01-F04 accepted facilities remain unchanged;
- no F06 object/file/work begins.

If no real protection correction was required, canonical Blend/GLB hashes must remain exactly:

Blend:
`E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`

GLB:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If a proven visibility-only protection correction was required, record exact before/after hashes and the one authorized state delta.

## Required log

Write exactly:

`coordination/Logs/REV005_F05_R01_INTEGRATED_PROTECTION_REMEDIATION_CODEX_LOG.md`

Include:
- starting commit/hash state;
- camera candidates and selection;
- direct explanation of why the old D failed;
- protection-state root cause;
- any authorized visibility-only correction;
- final hashes;
- all evidence paths.

## Git scope

Commit/push only:

- R01 evidence/renders/log;
- canonical Blend/GLB only if a proven accepted-state visibility correction was actually necessary.

Do not edit root `TASKS.md`.
Do not edit locked audit criteria.
Do not begin F06.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F05_R01`
