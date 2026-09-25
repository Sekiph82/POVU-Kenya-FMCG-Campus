# REV005 OWNER INTERIOR REVIEW V01 — GPT EXECUTION PROMPT

## Mission
Create a **review-only Owner Interior Review package** from the completed REV005 digital twin. Do not modify REV004 or the canonical REV005 model. Do not remediate anything and do not create the final campus tour.

## Authoritative inputs
- `3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
- `3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`
- `3d/revisions/REV005/REV005_INTERIOR_AUDIT.md`
- `3d/revisions/REV005/audit/REV005_FINAL_VALIDATION.json`
- `coordination/Logs/REV005_INTERIOR_COMPLETION_CODEX_LOG.md`
- REV005 completion baseline commit: `4f53eb93289f5c6e293dbb275c4bd0af2bd7448a`

## Immutable rules
1. REV004 is frozen. Do not modify it.
2. Canonical REV005 `.blend` and `.glb` are read-only for this task.
3. Do not fix geometry, interiors, Hands of Growth, trees, Living Wall, materials, landscaping or architecture during review.
4. Do not create REV006.
5. Do not create or regenerate the final long-form campus tour.
6. Do not show, label or discuss `East Glass Deck Access` or `West Glass Deck Access`.
7. Any defect discovered must be recorded as an owner-review finding, not silently repaired.

## Interior inventory
Before rendering, reconcile the actual REV005 scene against the audit, validation and completion log. Build a canonical list of **every completed interior/facility**. Do not hand-pick a subset.

The inventory must include all applicable spaces, including but not limited to:
- Wet Processing / liquid production
- Raw Material storage/warehouse
- Finished Goods storage/warehouse
- filling / packaging / production support
- R&D / QC Innovation Centre / laboratory
- Training / Academy
- Administration / HQ / offices
- Restaurant
- POVU Café
- kitchen / food-service support where modeled
- Daycare / crèche
- Occupational Health / clinic where modeled
- Wellness / recreation where modeled
- employee/staff facilities
- utilities / engineering interiors
- maintenance / workshop where modeled
- every additional completed interior discovered in REV005

Do not assume this list is exhaustive. The actual REV005 model and evidence define scope.

## Review video
Produce one inspection video:

`output/rev005-owner-interior-review/POVU_REV005_OWNER_INTERIOR_REVIEW.mp4`

Technical target:
- 1920×1080
- true 30 fps
- H.264
- duration determined by the amount of material genuinely required for inspection

This is an **inspection video, not a promotional film**.

Use the successful R03/R04 camera principles:
- smooth continuous movement
- no teleportation
- no unexplained spatial jumps
- no static waiting
- no repeated fake coverage
- no camera staring at walls, roofs or empty space
- no label-only coverage
- target must actually be visible

Where practical, use a coherent continuous route. Editorial transitions between physically separate buildings are allowed only when clearly intentional and visually clean; never disguise a camera reset as continuous travel.

## Minimum visual proof per significant interior
Prefer at least two useful views:

### View A — Orientation / wide
Show the overall layout, major equipment/furniture and spatial organization.

### View B — Functional / inspection
Move through/across the space and reveal the elements that prove its claimed function.

Examples:
- Restaurant: seating, tables, circulation, service/dining identity.
- Café: counter/service/seating where modeled.
- Daycare: actual child-oriented functional interior.
- R&D/QC: lab/QC benches, work areas, equipment where modeled.
- Raw Material: storage/racking/pallet/material-handling organization.
- Finished Goods: finished-goods storage/staging/dispatch organization.
- Training/Academy: training/classroom identity.
- Administration: office/workplace identity.
- Production: actual tanks, lines, filling/processing/packaging equipment.

Do not count a generic room plus a label as proof.

## Label rule
For every label:

`PHYSICAL TARGET VISIBLE -> LABEL APPEARS`

Never use the label as evidence that coverage occurred. Use clean audience-facing facility names only. Exclude development/debug terminology such as `Production massing`, `Landscape framework`, `UNCERTAIN`, `EVIDENCE BOUNDARY`, proxy/blockout/placeholder/debug labels.

## Owner-review findings
If review reveals any defect, including but not limited to:
- incorrect Hands of Growth placement
- unwanted trees
- Living Wall dimensions
- incomplete or implausible interior
- wrong furniture/equipment
- blocked circulation
- mislabeled facility

record it. Do not fix it in this mission.

## Required deliverables
Create:
1. `output/rev005-owner-interior-review/POVU_REV005_OWNER_INTERIOR_REVIEW.mp4`
2. `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_REVIEW_INDEX.md`
3. `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_COVERAGE_AUDIT.md`
4. `output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_REVIEW_VALIDATION.json`
5. `coordination/Logs/REV005_OWNER_INTERIOR_REVIEW_V01_CODEX_LOG.md`

The index must contain:

| # | Facility / Interior | Start Time | End Time | View A | View B | Visibility | Notes |
|---|---|---:|---:|---|---|---|---|

Every discovered in-scope interior must appear exactly once in the coverage accounting, even if a facility contains multiple review segments.

## Coverage audit
For every interior verify:
- actual interior exists
- camera enters or clearly sees it
- facility identity is visually understandable
- useful orientation view exists
- useful functional/detail view exists where appropriate
- target is not substantially occluded
- label matches visible target
- no accidental wall/roof-only shot
- no static hold masquerading as coverage
- no duplicate/recycled viewpoint masquerading as another facility

Report totals:
- TOTAL INTERIORS DISCOVERED
- TOTAL INTERIORS SHOWN
- PASS
- FAIL
- MISSING
- BLOCKED

Coverage cannot PASS unless all discovered in-scope interiors are accounted for and visually reviewed.

## Validation
Before completion verify:
- MP4 decodes
- 1920×1080
- 30 fps
- H.264
- all discovered interiors accounted for
- representative rendered evidence inspected for every facility
- no East Glass Deck Access presentation reference
- no West Glass Deck Access presentation reference
- REV004 unchanged
- canonical REV005 master unchanged

Do not rely only on object-name or automated mapping tests. Visual evidence is mandatory.

## Git / publication
Commit and push lightweight scripts, reports, QA evidence and the Codex log to `main`. Large MP4 may remain local if repository policy requires it.

The final Codex response must provide the full GitHub URL to:
`coordination/Logs/REV005_OWNER_INTERIOR_REVIEW_V01_CODEX_LOG.md`

## Stop gate
After the review package is produced, STOP.

Do not remediate, modify REV005, create REV006, or start final-tour production.

Final status must be:

`AWAITING_OWNER_INTERIOR_REVIEW_AND_GPT_AUDIT`

The locked GPT audit criteria are in:
`coordination/Audits/REV005_OWNER_INTERIOR_REVIEW_V01_GPT_AUDIT_CRITERIA.md`

Codex must not edit that audit-criteria file.