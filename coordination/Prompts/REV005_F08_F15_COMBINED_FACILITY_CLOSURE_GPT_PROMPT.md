# M08.47 — REV005 F08–F15 Combined Facility Closure

## Owner directive

This prompt supersedes the previous one-facility-at-a-time execution restriction for the active REV005 facility program.

Execute F08 through F15 in one continuous Codex campaign.

Do not stop after F08.
Do not wait for GPT/owner review between facilities.
Do not begin an endless camera-search loop.
If one facility remains blocked after bounded remediation, record the blocker and continue to the next facility. After F15, perform one final blocker sweep.

Canonical repository/workspace:
- GitHub: `Sekiph82/POVU-Kenya-FMCG-Campus`
- Branch: `main`
- Local root: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`
- Live tracker: root `TASKS.md`
- REV005 only. Do not mutate frozen REV004.

## Current authoritative state

F01–F07 are independently PASS and locked. Preserve them.

F08 is Bottle Blow Molding and is currently blocked after R03.

Latest accepted execution/audit facts:
- M08.43 / F08-R01 rendered 134 candidates. Camera-only remediation failed.
- M08.44 / F08-R02 added geometry but the selected visual set still failed.
- M08.45 / F08-R03 tested true external south-frontage views.
- A/D proved the tapered hopper/feed can be visible.
- Across the R03 roles: stretch/blow readability = 0, in-process preform readability = 0, formed-bottle state readability = 0, complete label-blind process sequence = 0.
- Canonical Blend/GLB were not promoted by R03.
- Independent GPT decision: camera-only F08 work is exhausted. Remaining defect is process-state storytelling inside the blow cell and immediate discharge path.
- Existing M08.46 / F08-R04 prompt is superseded for execution by this owner-authorized combined campaign. Reuse its valid technical findings and criteria rather than discarding them.

## Step 1 — Resolve real F08–F15 identities from repository truth

Before modifying geometry, inspect canonical repository sources and resolve the exact facility mapping for F08, F09, F10, F11, F12, F13, F14 and F15.

For each facility record:
- facility ID and canonical name
- process/purpose
- current authorized object collection/object set
- room/facility envelope
- existing geometry and prior REV005 work
- locked machine/equipment centers where applicable
- existing camera constraints
- show/hide/quarantine rules already accepted
- canonical Blend/GLB paths
- prior evidence/audits relevant to that facility

Do not invent F09–F15 names from memory. Repository truth wins.

Write the resolved F08–F15 mapping at the top of the combined execution log.

## Global acceptance principle

Every facility must be readable without depending on labels.

A reviewer should understand:
- what enters
- what process occurs
- what major equipment performs it
- what leaves
- how material/product moves between stages

Readability must come from geometry, scale, arrangement, connections, process states and spatial organization. Labels may supplement but never replace missing process geometry.

Generic boxes/tanks/cylinders with labels are not acceptable final facility models.

## Protect accepted facilities

F01–F07 are locked.

Do not redesign, move, delete, replace or casually re-export their accepted geometry.

Before canonical mutation, capture enough object/transform/hash signatures to prove F01–F07 remain unchanged except for unavoidable shared references that produce no visible/structural regression.

Do not reopen historical accepted facilities just because a helper script could make them “cleaner”.

## F08 required remediation

F08 is Bottle Blow Molding.

Do not start with another broad camera search.

Fix the actual process-state storytelling.

Preserve the R02 staged room and major process anchors unless repository evidence explicitly authorizes otherwise.

At minimum the final label-blind sequence must distinguish:
1. resin/preform input
2. hopper/feed
3. preform handling
4. heating / machine entry
5. mould / stretch-blow zone
6. in-process preform/load/stretch state
7. formed-bottle/blow/eject state
8. released bottle
9. bottle outfeed
10. downstream transfer

The previously unreadable cues that must be fixed directly include:
- mould/cavity identity
- tie-bar / blow-cell structure where physically appropriate
- stretch/blow cue
- in-process preform state
- formed-bottle state
- eject/release state
- discharge continuity
- obvious distinction between preform and formed bottle

Do not make microscopic details that vanish at QA distance.

Use the valid M08.46 technical direction:
- Station 1 visibly reads as heated-preform/load/stretch state
- Station 2 visibly reads as formed-bottle/blow/eject state
- add only physically plausible process-state, mould/cavity, tie-bar, discharge and product-continuity detail
- replace broad-AABB camera invalidation with actual solid-geometry validation

## F09–F15 facility-specific work

For each F09–F15, first create an internal facility contract:

- What enters?
- What process occurs?
- What equipment is essential?
- What leaves?
- What material/product connections must be visible?
- What existing geometry is already correct and must be preserved?
- What is generic, incomplete, disconnected, implausible or unreadable?

Then implement only the missing facility-specific geometry and evidence needed for production-quality label-blind readability.

Do not apply the same procedural machine kit to all facilities.

## Campus process logic

Preserve the campus manufacturing logic:

raw-material receiving
→ RM storage/supermarket
→ automated feeding
→ process/mixing
→ filling/packing
→ pallet/material-handling spine
→ finished-goods warehouse
→ dispatch

Maintain people/process/logistics/service separation where relevant.

Production remains a controlled process zone, not a warehouse aisle.

Do not route routine forklifts casually through automation-first process areas when the canonical concept intends controlled transfer.

## Geometry before camera

Cameras are evidence tools, not substitutes for modelling.

For each facility:
1. inspect geometry/process completeness
2. fix the actual process model
3. analytically identify valid observation regions
4. render the minimum useful evidence set
5. inspect the real PNGs

Do not generate 100+ random candidate cameras.

Normally use:
- one facility/process overview
- one process-flow view
- one equipment/detail view
- additional evidence only when genuinely required

Reject cameras that:
- intersect solid geometry
- sit inside walls/roof/columns
- violate permitted height
- have blocked LOS
- clip major process equipment
- show the wrong facility
- require destructive hiding of canonical context

If two reasonable validated camera approaches cannot communicate the process, classify the defect as geometry/process-storytelling and fix the model. Stop camera fishing.

## Actual solid-geometry camera validation

Do not repeat the old F08-R03 false invalidation caused by broad Production_Hall/roof AABBs.

Use actual solid-geometry intersection/containment checks or a repository-supported equivalent.

A broad building bounding box alone must not automatically invalidate a camera that is physically outside solid structure.

## Human and machine scale

Validate real-world plausibility:
- door/platform heights
- machine/tank dimensions
- operator access
- conveyor heights
- guardrails/stairs/ladders where relevant
- pipe/duct diameters
- bottle/preform/pallet/IBC/drum scale where relevant
- maintenance/service clearance

Do not accept geometry that only satisfies bounding-box math but is industrially implausible.

## Process connections

Where a real process needs a connection, show it.

Examples where applicable:
- pipes
- ducts
- vacuum/resin transfer
- conveyors
- bottle/cap/lid transfer
- product transfer
- feed hopper connections
- discharge/outfeed
- AMR/pallet interfaces
- utility connections

Avoid disconnected equipment islands and decorative pipes with no plausible source/destination.

## Architectural visibility

Do not solve evidence visibility by deleting the surrounding campus.

Use only previously sanctioned show/hide semantics.

Do not invent broad new quarantine sets.

Do not permanently remove roofs/walls just to obtain screenshots.

If a QA-only visibility composition is legitimately required and already allowed by workflow, preserve canonical geometry and document exactly what is temporarily hidden.

## Bounded execution loop

Process in this order:

F08 → F09 → F10 → F11 → F12 → F13 → F14 → F15

For each facility:

### Pass A
- inspect
- resolve facility contract
- fix geometry/process identity
- validate dimensions/connections
- choose validated evidence cameras
- render
- visually inspect actual PNGs
- run technical/protection/parity checks

If PASS:
- record builder PASS evidence
- continue immediately to next facility

If FAIL:
- classify exact reason

If geometry/process identity:
- perform one focused geometry remediation

If genuinely camera-only:
- perform one focused camera replacement

Then run Pass B.

If Pass B succeeds:
- record builder PASS evidence
- continue

If Pass B still fails:
- record exact blocker
- continue to next facility

Do not terminate the campaign because one facility remains blocked.

After F15, perform one final targeted sweep of remaining blockers where a clear actionable solution exists.

No infinite loops.

## Visual gate

A frame cannot pass if it is:
- black or near-black
- empty
- wall/roof dominated
- clipped through geometry
- wrong-facility
- too distant to identify equipment
- too close to understand process
- dependent on labels
- numerically valid but visually confusing

Inspect every final PNG directly.

Diagnostic failures must not be presented as accepted evidence.

## Blend / GLB parity

For every promoted facility:
- save canonical Blend correctly
- export canonical GLB correctly
- verify expected facility objects in both
- verify relevant transforms/material visibility
- verify no accidental object loss
- verify no duplicate major equipment
- verify sanctioned hidden/quarantine state only
- verify no black-render/export-state regression

At the end perform one integrated F08–F15 parity sweep.

Verify F01–F07 remain preserved.

## Builder vs independent audit

Codex may report a facility as `BUILDER_VISUAL_PASS` but must not claim independent GPT acceptance.

Do not mark independent-audit-gated work complete in TASKS.md.

The combined campaign ends in one of:

`AWAITING_GPT_F08_F15_FINAL_AUDIT`

or, if bounded blockers remain:

`AWAITING_GPT_F08_F15_FINAL_AUDIT_WITH_RECORDED_BLOCKERS`

Do not stop at intermediate states such as:
- AWAITING_GPT_F08
- AWAITING_OWNER
- CAMERA_SEARCH_EXHAUSTED
- WAITING_FOR_NEXT_PROMPT

## Evidence package

Create one combined authoritative execution package under existing REV005 conventions.

Suggested combined log:

`coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_CODEX_LOG.md`

The log must start with:

| Facility | Canonical name | Result | Evidence |
|---|---|---|---|
| F08 | ... | PASS/BLOCKED | ... |
| F09 | ... | PASS/BLOCKED | ... |
| F10 | ... | PASS/BLOCKED | ... |
| F11 | ... | PASS/BLOCKED | ... |
| F12 | ... | PASS/BLOCKED | ... |
| F13 | ... | PASS/BLOCKED | ... |
| F14 | ... | PASS/BLOCKED | ... |
| F15 | ... | PASS/BLOCKED | ... |

For each facility include:
- resolved facility contract
- pre-existing defect
- geometry changed
- objects added/modified/removed
- locked objects preserved
- camera positions and camera-validity proof
- accepted PNG paths
- direct visual-review result
- Blend validation
- GLB validation
- deterministic parity result
- remaining blocker if any

Also record:
- starting Git HEAD
- ending Git HEAD
- canonical Blend hash before/after
- canonical GLB hash before/after
- scope diff
- F01–F07 preservation proof
- scripts/tests run
- warnings/errors
- final working-tree/branch/remote state

## Tracking

Root `TASKS.md` is the only live tracker.

Do not create a new dashboard/index/roadmap/tracker system.
Do not create `.hiveai`.

At completion update TASKS.md truthfully with:
- F08 through F15 builder results
- any remaining blockers
- combined audit state
- exact next action = independent GPT combined audit

Do not self-mark independent GPT PASS.

## Git safety/publication

Start from real current `main`.

Do not reset/rebase/force-push owner work.

Do not delete unrelated local files.

Do not use destructive cleanup commands.

Preserve unrelated dirty owner changes.

When the campaign and evidence are complete:
- run relevant validation
- run diff checks
- verify scope
- update TASKS.md
- commit
- push safely to `origin/main`
- verify local HEAD == origin/main

## Final required response

Return only a concise execution summary containing:
- F08–F15 result matrix
- final state
- combined log path
- commit SHA
- local/origin synchronization state
- any remaining blockers

The campaign is not complete until F15 and the final blocker sweep have both been processed.
