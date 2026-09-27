# POVU Kenya FMCG Campus — Canonical GitHub Task State

This root `TASKS.md` is the only authoritative current project-status tracker consumed by H!veAI for this repository. GitHub repository metadata and the latest commit are the remaining project-truth inputs.

Owner directive: do NOT create or maintain a `.hiveai` file or directory for this project. Root `TASKS.md` is the single live tracker.

Historical prompts, logs, audits, planning files, renders, Blender/GLB artifacts, and videos are evidence/history only. They do not override this file.

## Project Status

- Current Milestone: M08
- Current Sprint: M08.07
- Current Task: M08.07 — REV005 Interior Remediation V04 campus-wide visual completion
- Current Task Status: ACTIVE
- Next Task/Action: Execute the V04 Codex prompt, complete the 26-group visual-completion remediation and QA package, then stop at AWAITING_GPT_REMEDIATION_AUDIT_V04 for independent GPT image audit.
- Required Actor: CODEX
- Workflow State: READY_FOR_CODEX_EXECUTION
- Tracking Repository: Sekiph82/POVU-Kenya-FMCG-Campus
- Tracking Branch: main

## Blockers/Waits

- M08.07 is required because the independent V03 visual audit found that 26/26 facility presence still did not prove 26/26 fully modeled interiors.
- M08.08 cannot start until Codex completes V04 and publishes the new QA package/log.
- M08.09 REV005 freeze cannot occur until GPT gives full visual PASS and the owner accepts the model. PASS_WITH_FINDINGS is not sufficient for the "complete interiors" claim.
- M09 final REV005 tour work is intentionally blocked until REV005 is visually accepted and frozen.
- REV004 and the approved R04 470-second video remain frozen historical deliverables and must not be modified while REV005 is being completed.
- The approved R03/R04 persistent-camera/global-clock system is the mandatory camera baseline for any future REV005 tour.

## H!veAI Parser Contract

- Project Status metadata labels above are plain text. Do not wrap `Current Milestone:`, `Current Sprint:`, `Current Task:`, `Current Task Status:`, `Next Task/Action:`, `Required Actor:`, or `Workflow State:` in Markdown bold markers.
- Every canonical task row must use exactly one of these forms: `- [x] TASK-ID — Title`, `- [~] TASK-ID — Title`, `- [!] TASK-ID — Title`, or `- [ ] TASK-ID — Title`.
- Status semantics are: `[x]` validated complete, `[~]` active/implemented/partial, `[!]` blocked, `[ ]` planned/backlog.
- Only real task/package rows use checkbox markers. Evidence, acceptance notes, historical context, limitations, hashes, and paths use ordinary indented bullets so H!veAI does not count them as tasks.
- Task IDs are stable. Do not reuse an ID for a different task after it has appeared in this file.
- Builder/Codex self-reports are implementation claims, not independent acceptance evidence.
- A model/video task moves to `[x]` only when the evidence appropriate to that task has been independently audited and, where explicitly required, owner-accepted.
- Root `TASKS.md` is the only current-state ledger. Logs, prompts, audit criteria, planning files, render folders, Git history, and any historical tracker artifacts are supporting context only.
- Do not create a `.hiveai` tracker for this repository.

## Canonical Tracking Rules

- Keep Project Status synchronized with the canonical task row that actually owns the current work.
- GPT/ChatGPT is the independent audit and tracker-acceptance authority for the current workflow. Codex executes tasks and publishes evidence; Codex must not self-promote audit-gated work to `[x]`.
- Owner acceptance controls subjective final-model and final-video closure where specified.
- Read the latest relevant prompt, Codex log, QA evidence, and locked audit criteria before changing task truth.
- Do not resurrect a rejected historical pipeline as current work unless the owner explicitly reopens it.
- REV004 is frozen. REV005 is the active model line.
- No future tour may return to the rejected chapter-reset/sample-and-hold camera architecture.
- Final tour camera behavior must preserve the approved R03/R04 principles: one persistent camera, one global frame clock, smooth travel/approach/reveal/pass/accelerate motion, no fake teleportation, no static label swapping, true 30 fps.
- East Glass Deck Access and West Glass Deck Access are removed from the desired presentation narrative and must not be reintroduced as callout destinations.
- Approved owner exterior corrections for REV005 include the current Hands of Growth state, removal of the two specified obstructing trees, corrected Living Wall extent, and preserved VIP entrance relationships.
- Large local binary artifacts may remain local according to repository policy, but exact paths/hashes and lightweight evidence/logs must be recorded in GitHub.
- The canonical local workspace is `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`; do not create unnecessary parallel desktop project folders.

## Current Truth Snapshot

- The POVU Kenya FMCG Campus concept is a 70,000 m² / 7 ha world-class FMCG campus with production, warehouses, utilities, HSE, people facilities, HQ/R&D/QC, sustainability and social spaces.
- The architectural language is locked around Water + Green + Light, with premium treatment concentrated at the VIP arrival/HQ/R&D/POVU Plaza/Glass Deck and economical industrial shells elsewhere.
- REV004/R04 remains the owner-usable exterior/campus-tour baseline.
- R04 final video is owner-accepted for current use: 1920×1080, 30 fps, H.264, 14,100 frames, 470 seconds, SHA-256 `9E6CF50620F9573FE0308C2DCFC6F394720968CC0294FF3D3F479F686F96205E`.
- R03 established the frozen approved camera architecture: one persistent camera + one global frame clock; no chapter camera resets.
- REV005 is the active complete-interior model line.
- V03 final REV005 hashes reported by Codex:
  - Blend: `9E9A63A2D7AAFA5667CD0A41DFDE746CB2F2A7751F29DAB259CA30E8A99A238F`
  - GLB: `9AC05E7E9D286EB16FB88C2CD6DC30715B8892CF91FCE8AEF9AB52ED94FCF12C`
- V03 technically reported 7/7 focused and 26/26 sweep, but independent image audit returned REMEDIATION_REQUIRED because multiple spaces still read as schematic/blockout/generic rather than complete interiors.
- The decisive acceptance standard for REV005 is now label-blind visual completeness, not object count, group presence, filename, report text, or validation JSON.

## Tasks

Legend: `[x]` validated complete, `[~]` active/implemented-but-partial, `[!]` blocked, `[ ]` planned/backlog.

### M00 — Project source foundation and digital-twin scope

- [x] M00.01 — Establish POVU Kenya FMCG Campus repository and canonical source structure
  - Evidence: repository root contains `3d/`, `blender/`, `coordination/`, `docs/`, `output/`, `presentation/`, `remotion/`, and `source/`.
  - Result: GitHub became the durable project evidence/control surface.

- [x] M00.02 — Consolidate campus masterplan, brand, market, HSE, machinery and 91-SKU evidence basis
  - Evidence: planning/evidence work later reconciled the HSE deck, brand deck, presidential deck, market research and 91-SKU workbook.
  - Result: later factory-tour and interior tasks have a documented source basis rather than free-form invention.

- [x] M00.03 — Lock core campus design language and owner requirements
  - Scope includes 70,000 m² site, approximately 23,000 m² enclosed GFA, Glass Deck target, people/logistics separation, forklift-free production-core intent, solar/utilities/ETP/social facilities, Water + Green + Light language, signature VIP arrival elements and Kenya identity.
  - Result: these are durable design constraints for subsequent revisions.

### M01 — Early Blender 50-video prototype program

- [x] M01.01 — Build the first 50-shot/50-video prompt and logging framework
  - Evidence: `coordination/Prompts/M01_VIDEO-001...050_V01_GPT_PROMPT.md` and matching Codex logs.
  - Result: complete historical experiment package created.

- [x] M01.02 — Execute the initial V01 per-video batch
  - Evidence: individual M01 VIDEO-001 through VIDEO-050 logs.
  - Outcome: technically produced/validated as an experiment but not accepted as the final tour approach.

- [x] M01.03 — Execute corrective V02/V03 batch experiments
  - Evidence: `M01_FOUR_VIDEO_V02_CODEX_LOG.md`, `M01_TWO_VIDEO_V03_CORRECTIVE_CODEX_LOG.md`, `M01_REMAINING_46_V03_CLEAN_MASTER_CODEX_LOG.md`, and V03 per-video logs.
  - Outcome: exposed a generic overall-bounds/angle camera strategy that did not create meaningful subject-driven cinematography.

- [x] M01.04 — Retire the generic 50-video Blender camera algorithm as a production approach
  - Acceptance: owner rejected the generic/teleporting visual behavior.
  - Durable rule: do not revive the old generic 50-camera algorithm.

### M02 — REV003 clean master and landmark development

- [x] M02.01 — Establish clean REV003 Higgsfield/GLB campus baseline
  - Evidence: REV003 revision assets in `3d/revisions/REV003` and historical 3D Jutsu project/export trail.
  - Result: stable base for later architectural finalization.

- [x] M02.02 — Add signature campus landmarks and identity elements
  - Scope included Hands of Growth, approximately 7 m Water Wall, Organic Canopy refinement, Smart Totems and landscape/arrival identity.
  - Result: signature architecture/landscape language carried forward.

### M03 — REV004 architectural master

- [x] M03.01 — Build REV004 final architectural master
  - Evidence: `coordination/Logs/M03_REV004_FINAL_ARCHITECTURAL_MASTER_CODEX_LOG.md`.
  - Result: campus architecture, exterior systems and major spatial organization finalized to the then-approved concept level.

- [x] M03.02 — Perform REV004.1 final cleanup and freeze
  - Evidence: `coordination/Logs/M05_REV004_1_FINAL_CLEANUP_CODEX_LOG.md`; commit `937ecce`.
  - Final master path: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`.
  - Recorded SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`.
  - Result: stable architectural source for coverage planning and early tour production.

- [x] M03.03 — Lock flagship Smart Totem and campus-totem hierarchy
  - Rule: one large `SMART_TOTEM_VIP`; limited smaller campus decision-point totems.
  - Result: avoided uncontrolled signage duplication.

### M04 — Remotion digital-twin proof of concept

- [x] M04.01 — Prove direct GLB-driven Remotion digital-twin rendering
  - Evidence: local R01 POC and subsequent R02 package.
  - Result: demonstrated that the campus could be rendered/animated in Remotion without cloud/Higgsfield rendering.

- [x] M04.02 — Produce and validate Remotion POC R02
  - Evidence: `coordination/Logs/M04_REMOTION_DIGITAL_TWIN_POC_R02_CODEX_LOG.md`, `output/poc-r02/`.
  - Result: visually successful 60-second concept with vegetation/material/campus callout treatment.

### M05 — REV004.1 architectural cleanup gate

- [x] M05.01 — Remove duplicate/cleanup issues and preserve a frozen architectural master
  - Evidence: `M05_REV004_1_FINAL_CLEANUP_CODEX_LOG.md`.
  - Result: one Hands of Growth root, cleaned hierarchy and final architecture baseline.

- [x] M05.02 — Record later-discovered owner visual corrections for future revision
  - Findings later included Living Wall overextension and Hands of Growth presentation/visibility concerns.
  - Result: these were intentionally handled in REV005 rather than rewriting the owner-usable REV004 deliverable.

### M06 — Complete-tour coverage, evidence reconciliation and storyboard

- [x] M06.01 — Build first complete-tour coverage matrix/storyboard
  - Evidence: `POVU_COMPLETE_FACTORY_TOUR_COVERAGE_MATRIX_V01.csv`, `POVU_COMPLETE_FACTORY_TOUR_MASTER_STORYBOARD_V01.md`, M06 V01 log.
  - Result: initial broad campus/factory coverage plan.

- [x] M06.02 — Reconcile evidence and close M06 V02 coverage planning
  - Evidence: `M06_COMPLETE_TOUR_COVERAGE_AND_STORYBOARD_CODEX_LOG_V02.md`, V02 matrix/storyboard, evidence register, gap report and capability map.
  - Recorded result: 69 coverage rows, 66 required accounted, 62 optimized shots, 1,393 seconds raw runtime, three solar installations confirmed.
  - Important caveat: planning coverage did not itself prove every physical model detail.

- [x] M06.03 — Document physical-evidence gaps instead of inventing them
  - Recorded gaps included items such as gatehouse/dedicated workshop/dedicated CIP or specific hypochlorite-vessel proof where not physically verified at that stage.
  - Result: later tasks were instructed not to fabricate architecture/equipment simply to satisfy labels.

### M07 — Complete campus/factory tour camera system

- [x] M07.01 — Produce long-form R01 complete-tour prototype
  - Evidence: `M07_COMPLETE_FACTORY_TOUR_PRODUCTION_CODEX_LOG.md`, `output/complete-tour-r01/`.
  - Outcome: technically complete but owner-rejected.
  - Root cause later identified: 2-fps chapter sampling/sample-and-hold converted to 30 fps plus repeated/parked camera views and text-as-evidence behavior.

- [x] M07.02 — Attempt R02 camera remediation
  - Evidence: R02 output/planning artifacts.
  - Outcome: still owner-rejected due visible jumps/reset behavior and weak subject proof.

- [x] M07.03 — Produce and owner-approve R03 60-second camera POC
  - Evidence: `coordination/Logs/M07_R03_60S_POC_CODEX_LOG.md`.
  - Commit: `5e214a122755ac285eba65b1e4594a14d8471d37`.
  - Output: `output/complete-tour-r03-poc-60s/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R03_POC_60S.mp4`.
  - Result: 60 s, 1,800 frames, 1920×1080, true 30 fps, persistent camera, zero hard cuts/discontinuities, FOV 52.
  - Durable rule: one persistent camera + one global frame clock is frozen as the approved system.

- [x] M07.04 — Produce R04 long-form approved-camera-system tour
  - Evidence: `coordination/Logs/M07_R04_LONG_FORM_APPROVED_CAMERA_SYSTEM_CODEX_LOG.md`.
  - Commit: `845f27245d89d35c358a84b0377fa1434e8abb4f`.
  - Output: `output/complete-tour-r04/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R04.mp4`.
  - Result: owner accepted the final 470-second exterior/campus/factory tour for use.
  - Note: owner tolerated the then-imperfect Hands of Growth direction because REV004/R04 was frozen rather than reopened.

- [x] M07.05 — Freeze R04 camera choreography rules for all future tours
  - Required behavior: TRAVEL → APPROACH → SLOW DOWN → REFRAME/REVEAL → PASS SUBJECT → ACCELERATE → NEXT.
  - Prohibited behavior: STOP → LABEL → WAIT → CHANGE LABEL → WAIT → TELEPORT.
  - Result: future REV005 tour work must reuse this camera logic rather than redesign it.

### M08 — REV005 complete-interior digital twin

- [x] M08.01 — Build initial REV005 Interior Completion master
  - Evidence: `coordination/Logs/REV005_INTERIOR_COMPLETION_CODEX_LOG.md`.
  - Deliverables: canonical REV005 Blend/GLB, interior audit and validation.
  - Reported result: 2,826 GLB nodes, 15/15 initial visual QA, all in-scope facilities populated, Wet Processing preserved, owner exterior corrections applied, REV004 preserved.
  - Important limitation: later independent review showed that "populated" did not equal visually complete.

- [x] M08.02 — Produce REV005 Owner Interior Review V01
  - Evidence: `coordination/Logs/REV005_OWNER_INTERIOR_REVIEW_V01_CODEX_LOG.md`.
  - Output: 58.667-second review MP4, 26 canonical facility groups, 52 stills.
  - Result: 26/26 shown, but Codex itself recorded 14 functional/detail findings.
  - Independent conclusion: REMEDIATION_REQUIRED.

- [x] M08.03 — Execute Interior Remediation V01
  - Evidence: `coordination/Logs/REV005_INTERIOR_REMEDIATION_V01_CODEX_LOG.md`.
  - Commit: `5f25ac11dce4dd1e423ddc626c2e17a350dca0b4`.
  - Codex claim: 14/14 closure and 12/12 regression protection.
  - Independent image audit outcome: REMEDIATION_REQUIRED because multiple production/support interiors remained too generic/schematic.

- [x] M08.04 — Execute Interior Remediation V02 focused functional-specificity pass
  - Evidence: `coordination/Logs/REV005_INTERIOR_REMEDIATION_V02_CODEX_LOG.md`.
  - Commit: `5e770a84fe08eb75b5221ad4df4d519bb78cdef2`.
  - Codex claim: 7/7 focused closure, 26/26 regression.
  - Independent image audit outcome: REMEDIATION_REQUIRED.
  - Accepted/stronger examples included Caps & Trigger Assembly and Micro-ingredient Weigh/Dispense; several other spaces still read as low-detail functional blockouts.

- [x] M08.05 — Execute Interior Remediation V03 label-blind visual-completion pass
  - Evidence: `coordination/Logs/REV005_INTERIOR_REMEDIATION_V03_CODEX_LOG.md`.
  - Commit: `42f434501a9401834d67c9ab0e484506322bb681`.
  - Codex claim: 7/7 focused, 26/26 sweep, 21 unlabeled focused proofs plus 26-group evidence.
  - Result: technically complete package produced for independent visual audit.

- [x] M08.06 — Independently audit V03 QA images
  - Audit basis: user-provided V03 QA ZIP plus 21 focused renders and 26-group sweep/contact sheets.
  - Result: REMEDIATION_REQUIRED.
  - Clear improvement/acceptance: Daycare became visually credible; Caps/Trigger and Micro-Weigh remained stronger from V02.
  - Remaining weak/failing examples included Bottle Blow Molding, Liquid Filling, Toothpaste, Wet Wipes, Glass Deck Command/Training/Café, Restaurant/Café/Kitchen, Finished Goods, Raw Material, ETP, Fire Pump House, Occupational Health, Utilities, and weak Admin/HQ/R&D/QC proof.
  - Core finding: Codex continued to conflate group presence with finished-interior visual completeness.

- [~] M08.07 — REV005 Interior Remediation V04 campus-wide visual completion
  - Current execution prompt: `coordination/Prompts/REV005_INTERIOR_REMEDIATION_V04_GPT_PROMPT.md`.
  - Locked audit criteria: `coordination/Audits/REV005_INTERIOR_REMEDIATION_V04_GPT_AUDIT_CRITERIA.md`.
  - Goal: close all remaining visual-completion gaps across all 26 groups, with heightened focus on the V03 weak areas.
  - Acceptance principle: if labels/filenames/metadata disappear, the facility/process must still be understandable from the image.
  - Codex must stop at `AWAITING_GPT_REMEDIATION_AUDIT_V04` and must not mark this task complete.

- [ ] M08.08 — Independent GPT V04 26-group visual audit
  - Required evidence: V04 QA folder, 26-group acceptance matrix/contact sheet, report, validation, canonical hashes and Codex log.
  - Closure rule: full PASS requires 26/26 visual completeness plus regression/source-protection gates.
  - PASS_WITH_FINDINGS does not freeze REV005.

- [ ] M08.09 — Owner final REV005 model review and freeze
  - Dependency: M08.08 full PASS.
  - Required owner check: key production lines, warehouses, people/support spaces, utilities, Hands of Growth/Living Wall/trees and overall digital-twin coherence.
  - On acceptance: record final Blend/GLB paths and SHA-256 hashes and freeze REV005 against casual edits.

### M09 — Final REV005 owner-review and campus/factory tour

- [!] M09.01 — Build final REV005 owner-review walkthrough
  - Blocker: REV005 must first pass M08.08 and owner freeze M08.09.
  - Scope: concise inspection walkthrough of the final accepted interiors, not another remediation pass.
  - Camera baseline: R03/R04 persistent-camera/global-clock behavior.

- [!] M09.02 — Plan final REV005 complete-tour route/storyboard
  - Blocker: M08.09.
  - Scope: campus exterior + all important interiors + production + warehouses + utilities + people facilities.
  - Rule: runtime emerges from truthful coverage; no artificial 23-minute padding.

- [!] M09.03 — Render REV005 final camera preview
  - Blocker: M09.02.
  - Requirement: true 30 fps, smooth continuous choreography, target-visible labels only, no sample-and-hold, no chapter camera resets.
  - Owner/GPT must review camera choreography before full-quality final render.

- [!] M09.04 — Render final REV005 complete campus/factory tour
  - Blocker: camera preview approval.
  - Requirement: use frozen R04 camera system quality and the final accepted REV005 geometry.
  - Deliverables: local master MP4, hashes, QA evidence, log.

- [!] M09.05 — Independent GPT + owner final-tour acceptance
  - Blocker: M09.04.
  - Audit: continuity, target visibility, interior truthfulness, labels, motion, repeated views, technical encode and owner presentation quality.
  - Final-tour task closes only after owner acceptance.

### M10 — Presentation integration and executive delivery

- [ ] M10.01 — Integrate final accepted REV005 tour into POVU master presentation workflow
  - Dependency: M09.05.
  - Intended presentation architecture includes Campus / People / Production / Logistics / Safety / Utilities / Sustainability navigation and production sub-navigation where useful.
  - Do not replace the existing owner-usable R04 material until REV005 final media is explicitly approved.

- [ ] M10.02 — Add final interior/factory visual evidence to executive slides where it materially improves the presentation
  - Dependency: M09.05.
  - Scope: use only owner-approved visuals; avoid debug/audit labels and internal model terminology.

- [ ] M10.03 — Final presentation QA for Kenya executive/presidential audience
  - Dependency: integrated deck.
  - QA: factual consistency, source support, legibility, video playback, navigation, no placeholder/internal terminology, no unsupported engineering/legal claims.

### M11 — Final archive, provenance and handoff

- [ ] M11.01 — Freeze final accepted master artifacts and hashes
  - Dependency: final REV005 model and final tour acceptance.
  - Record final Blend, GLB, MP4, presentation and key QA artifact hashes/paths.

- [ ] M11.02 — Final GitHub evidence/index cleanup
  - Dependency: project acceptance.
  - Ensure prompts/logs/audits/planning remain historical evidence while root `TASKS.md` accurately reflects final project truth.

- [ ] M11.03 — Produce final owner handoff summary
  - Include canonical local paths, GitHub links, accepted revision IDs, hashes, known concept-level limitations and future optional enhancement areas.

## Milestone Summary

- M00-M06 are complete historical foundation/planning packages.
- M07 is complete and contains the owner-approved R03 camera system plus the owner-usable R04 470-second tour.
- M08 is the active milestone. V01-V03 execution/review cycles are complete history, but REV005 is not yet frozen because the V03 independent visual audit found remaining incomplete/generic interiors.
- M08.07 V04 is the current task and is designed to replace presence/object-count validation with true 26-group visual-completion acceptance.
- M09-M11 are planned future work and remain blocked/planned until REV005 itself is independently and owner-accepted.
