# REV005 OWNER INTERIOR REVIEW V01 — LOCKED GPT AUDIT CRITERIA

**Owner:** GPT audit stage  
**Executor:** Codex  
**Rule:** Codex MUST NOT edit this file.

## Audit purpose
Independently determine whether the REV005 Owner Interior Review package genuinely shows every in-scope completed interior and preserves the canonical REV004/REV005 sources.

A technical PASS from Codex is not sufficient. Visual evidence and coverage reconciliation are mandatory.

## Gate A — Source preservation
PASS only if evidence demonstrates:
- REV004 canonical tracked/source artifacts were not modified by this review mission.
- canonical REV005 `.blend` and `.glb` were not modified by this review mission.
- no unrequested REV006 or model mutation was created as a substitute.

## Gate B — Canonical inventory reconciliation
PASS only if:
- the review inventory is derived from actual REV005 model + `REV005_INTERIOR_AUDIT.md` + final validation + completion log;
- every in-scope completed interior/facility is accounted for;
- no facility is silently omitted;
- totals reconcile exactly between inventory, index and coverage audit.

## Gate C — Real visual coverage
For every in-scope interior, audit evidence must show the actual physical interior, not merely a label.

PASS requires, where appropriate:
- orientation/wide view;
- functional/detail view;
- visible functional identity;
- meaningful screen coverage;
- no substantial occlusion;
- no wall/roof/empty-space substitution;
- no duplicate generic view reused to claim different facilities.

## Gate D — Key interiors
The audit must explicitly inspect all applicable key facilities, including:
- Wet Processing
- Raw Material
- Finished Goods
- production/filling/packaging interiors
- Administration / HQ
- R&D / QC
- Training / Academy
- Restaurant
- POVU Café
- Daycare / crèche
- Occupational Health / clinic if in scope
- Wellness/recreation if in scope
- utilities/engineering/support
- maintenance/workshop if in scope
- all additional interiors discovered by canonical inventory

Any missing in-scope key interior is FAIL or BLOCKED, not PASS.

## Gate E — Camera review quality
The inspection video must not repeat the rejected R01/R02 behavior.

Audit for:
- visible teleportation;
- unexplained jumps;
- static waiting;
- repeated viewpoints masquerading as coverage;
- camera facing wrong target;
- labels changing while view remains unrelated;
- prolonged walls/roofs/empty frames.

Isolated intentional editorial transitions between physically separate buildings are acceptable if visually clean and not represented as continuous camera travel.

## Gate F — Label truthfulness
PASS only if facility labels correspond to what is actually visible.

Explicitly reject development/debug labels such as:
- Production massing
- Landscape framework
- UNCERTAIN
- EVIDENCE BOUNDARY
- proxy/blockout/placeholder/debug terminology

## Gate G — Glass Deck exclusions
The review presentation must not show, label or discuss:
- East Glass Deck Access
- West Glass Deck Access

Their appearance in internal historical source material is not itself a failure; reintroduction into the REV005 review deliverable is.

## Gate H — Findings are not silently repaired
Any defect discovered during review must be documented rather than fixed in canonical REV005 during this mission.

Specifically inspect reported status of:
- Hands of Growth placement
- obstructing trees
- Living Wall extent
- incomplete/implausible interiors
- equipment/furniture/circulation issues

## Gate I — Deliverables
Required:
- `POVU_REV005_OWNER_INTERIOR_REVIEW.mp4`
- `REV005_OWNER_INTERIOR_REVIEW_INDEX.md`
- `REV005_OWNER_INTERIOR_COVERAGE_AUDIT.md`
- `REV005_OWNER_INTERIOR_REVIEW_VALIDATION.json`
- `REV005_OWNER_INTERIOR_REVIEW_V01_CODEX_LOG.md`

MP4 may remain local; lightweight evidence/log must be pushed.

## Gate J — Technical video validation
Verify evidence for:
- 1920×1080
- 30 fps
- H.264
- decodable output
- duration reported
- representative visual evidence for every facility

## Gate K — Stop discipline
PASS only if Codex stopped after review-package creation.

It must NOT:
- remediate interiors;
- alter canonical REV005;
- create REV006;
- start the final long-form REV005 tour.

Expected terminal state:
`AWAITING_OWNER_INTERIOR_REVIEW_AND_GPT_AUDIT`

## GPT audit outcome
GPT will later create a separate audit artifact after Codex completion. Possible outcomes:
- `PASS`
- `PASS_WITH_FINDINGS`
- `REMEDIATION_REQUIRED`
- `BLOCKED`

Codex may not self-award the GPT audit result.