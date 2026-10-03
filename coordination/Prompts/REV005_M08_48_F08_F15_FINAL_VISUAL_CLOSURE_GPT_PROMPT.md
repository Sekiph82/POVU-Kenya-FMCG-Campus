# M08.48 — REV005 F08/F09/F11/F15 Combined Visual Closure + F08–F15 Audit Evidence Publication

## Purpose

This is the next single Codex execution task after the independent GPT audit of M08.47.

Do not split this work into four separate prompts.
Do not wait for GPT/owner review between facilities.
Do not redo already-promoted F10/F12/F13/F14 geometry unless a direct rerender proves a genuine visual defect.

The task has two goals:

1. Close the four remaining visual blockers:
   - F08 Bottle Blow Molding
   - F09 Chemical Compound / Controlled Receiving
   - F11 Finished Goods Warehouse / Dispatch
   - F15 Packaging Warehouse

2. Publish Git-tracked final visual evidence for **all F08–F15 facilities**, so GPT can perform a real independent visual audit instead of relying on builder prose.

Canonical repository/workspace:
- GitHub: `Sekiph82/POVU-Kenya-FMCG-Campus`
- Branch: `main`
- Local root: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`
- Live tracker: root `TASKS.md`
- Active model line: REV005
- Do not mutate frozen REV004.

## Mandatory starting inputs

Read before work:
- root `TASKS.md`
- `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_CODEX_LOG.md`
- `coordination/Audits/REV005_M08_47_F08_F15_COMBINED_GPT_AUDIT.md`
- `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_EVIDENCE_INDEX.json`
- `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_SOLID_CAMERA_VALIDATION.json`
- `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_GLB_PARITY.json`
- `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_PROMOTION_VALIDATION.json`
- prior F08 R01/R02/R03/R04 criteria and audit history where relevant

## Authoritative M08.47 technical state

Current canonical selective promotion is technically accepted by GPT:

- F10 promoted
- F12 promoted
- F13 promoted
- F14 promoted

Canonical hashes after M08.47:
- Blend: `83D00D7C18B4DED5B8E674AEF3DF77659E21C9E6035F2CAD318E7F6B414AC3E6`
- GLB: `18C146559F5675D6FE36759328F14CDD44F3626C5571B5671D3DCE6F33BAB5D0`

Exact GLB parity:
- baseline named nodes: 10,941
- old target nodes replaced: 350
- new target nodes: 595
- final expected: 11,186
- final exported: 11,186
- missing: 0
- extra: 0

Non-promoted Blender scene signature:
- baseline objects: 11,052
- final objects: 11,052
- removed: 0
- new: 0
- changed: 0

Preserve this truth.

## Hard preservation rules

F01–F07 remain independently PASS and locked.

F10/F12/F13/F14 are technically promoted and must be treated as protected for this task.

Do not remodel F10/F12/F13/F14 just because their local renders are being republished.

Only modify those facilities if:
- the exact current canonical rerender exposes a real visual defect, AND
- the defect is documented before mutation.

Otherwise rerender and publish them unchanged.

No broad campus cleanup.
No generic replacement of facility collections.
No global quarantine expansion.
No destructive reset/rebase/force-push.
No `.hiveai`.

## Why M08.48 is required

M08.47 left the exact 24 final PNGs and contact sheets only in an ignored local output directory.

That prevented independent GPT visual inspection.

M08.48 must therefore publish the final audit-sized visual evidence into Git.

The builder is not allowed to claim “GPT cannot access local files” after this prompt.

## Required Git-tracked evidence destination

Create and commit:

`coordination/Evidence/M08_48_F08_F15_FINAL_VISUAL_AUDIT/`

Inside it, publish the final individual audit images for all eight facilities.

Required minimum:

- F08_A.png
- F08_B.png
- F08_C.png
- F09_A.png
- F09_B.png
- F09_C.png
- F10_A.png
- F10_B.png
- F10_C.png
- F11_A.png
- F11_B.png
- F11_C.png
- F12_A.png
- F12_B.png
- F12_C.png
- F13_A.png
- F13_B.png
- F13_C.png
- F14_A.png
- F14_B.png
- F14_C.png
- F15_A.png
- F15_B.png
- F15_C.png

Use the exact final 1280×800 audit frames.

Also publish:
- `CONTACT_F08_F15_A.jpg`
- `CONTACT_F08_F15_B.jpg`
- `CONTACT_F08_F15_C.jpg`

Do not publish thumbnails instead of the real final frames.
Do not publish only JSON references to local files.

The committed images must be the exact images used for the final builder visual decision.

## Global visual rule

Every facility must read label-blind.

A reviewer should understand:
- what enters
- what happens
- what main equipment does it
- what leaves
- how stages connect

Do not use labels as a substitute for geometry/process storytelling.

## F08 — required final closure

Current defect:
individual objects exist, but the complete process is still not readable as one sequence.

Required final visible process:

preform/feed
→ heating
→ loaded preform
→ stretch/blow mould state
→ formed bottle
→ eject/release
→ outfeed

Do not create another broad camera campaign.

Fix geometry/process-state staging first.

Mandatory visual distinctions:
- preform must visibly differ from finished bottle
- at least one station must clearly show preform/load/stretch state
- another must clearly show formed-bottle/blow/eject state
- mould/cavity/tie-bar/blow-cell structure must visually explain the operation
- released bottles must visibly connect to outfeed
- process direction must be understandable without text

If needed, enlarge/space the process-state exemplars enough to be visible from realistic audit distance while retaining plausible industrial scale.

Preserve room and major process anchors unless the prior contract explicitly allows movement.

## F09 — required final closure

Current defect:
drum/IBC receiving, tanks and pump-transfer equipment exist, but they do not read as one connected receiving-to-process system.

Required visual chain:

controlled receiving/check
→ drum/IBC containment
→ storage/bulk interface
→ pump/meter skid
→ visible transfer route toward process

Required fixes may include:
- clearer receiving staging
- legible IBC cages/drums
- visually connected hoses/pipes
- pump/meter orientation that clearly belongs to the tanks/receiving flow
- better spatial separation between receipt and downstream transfer
- one overview capable of showing the relationship, supported by one detail view

Do not solve by labels only.

## F11 — required final closure

Current defect:
storage, staging and dock exist, but the handling vehicle and loading relationship are weak.

Required visible chain:

finished pallet storage
→ consolidation/staging
→ dispatch/check
→ handling vehicle
→ dock/leveller/loading interface

The vehicle must unmistakably read as a forklift/AMR or the canonical chosen handling vehicle.

If forklift:
- visible mast
- forks
- wheels/chassis
- operator zone or recognizable body form
- realistic pallet/fork relationship

If AMR:
- unmistakable autonomous pallet mover geometry and pallet interface

Do not leave a generic block-like vehicle.

At least one final frame must make staging-to-dock/loading movement obvious.

## F15 — required final closure

Current defect:
packaging storage and issue lane are present, but receiving and issue roles are not clearly separated; the handling vehicle is also weak.

Required visible chain:

packaging receiving
→ inspection/check
→ segregated storage
→ issue staging
→ issue lane / production handoff

Visually separate:
- inbound receiving zone
- stored packaging
- outbound issue-to-production zone

Use floor organization, equipment orientation, material state and handling paths, not just text.

The vehicle must be recognizable and shown performing a plausible packaging-material movement role.

Correct the low-exposure problem from the prior F15 A view.

## Camera policy

Do not repeat 100+ candidate searches.

For each blocked facility:
- use existing valid M08.47 cameras as starting points
- fix geometry first
- generate only a small bounded set of targeted alternatives if required
- validate actual solid geometry
- directly inspect the rendered image

Maximum intended new candidate count:
- normally <= 8 targeted alternatives per facility
- exceed only if a concrete technical reason is recorded

If multiple reasonable views still cannot tell the story, fix geometry instead of continuing camera search.

## F10/F12/F13/F14 evidence-only rerender

Do not mutate these facilities by default.

Rerender the current canonical promoted state using the M08.47 accepted final camera roles.

Directly inspect each A/B/C.

If all remain visually coherent:
- publish exact frames
- record `BUILDER_VISUAL_PASS_PRESERVED`

If a genuine defect appears:
- document it
- make the smallest facility-local correction
- rerun technical gates
- never silently change a previously promoted facility

## Technical gates after remediation

After any F08/F09/F11/F15 promotion:

1. Verify F01–F07 preservation.
2. Verify F10/F12/F13/F14 preservation unless explicitly corrected.
3. Verify non-target object signatures.
4. Verify exact Blend collection membership.
5. Export GLB using explicit deterministic membership, never a lossy visible-only export.
6. Recompute exact expected named-node set.
7. Require:
   - missing nodes = 0
   - unexpected nodes = 0
8. Run actual solid-camera-origin validation on all 24 final published views.
9. Confirm every published image corresponds to the final canonical state.

Do not promote a blocked facility merely to make counts look complete.

## Final builder decision matrix

The final execution log must contain:

| Facility | Result | Independent-audit evidence path |
|---|---|---|
| F08 | BUILDER_VISUAL_PASS or BLOCKED | tracked image paths |
| F09 | BUILDER_VISUAL_PASS or BLOCKED | tracked image paths |
| F10 | BUILDER_VISUAL_PASS_PRESERVED or corrected result | tracked image paths |
| F11 | BUILDER_VISUAL_PASS or BLOCKED | tracked image paths |
| F12 | BUILDER_VISUAL_PASS_PRESERVED or corrected result | tracked image paths |
| F13 | BUILDER_VISUAL_PASS_PRESERVED or corrected result | tracked image paths |
| F14 | BUILDER_VISUAL_PASS_PRESERVED or corrected result | tracked image paths |
| F15 | BUILDER_VISUAL_PASS or BLOCKED | tracked image paths |

## Required execution log

Create:

`coordination/Logs/REV005_M08_48_F08_F15_FINAL_VISUAL_CLOSURE_CODEX_LOG.md`

Record:
- starting SHA
- starting Blend/GLB hashes
- exact facilities mutated
- exact facilities preserved
- per-facility defect and fix
- camera positions
- final Git-tracked image paths
- direct builder visual decision
- protection results
- exact GLB parity math
- final hashes
- final commit SHA
- local/origin equality
- clean/dirty worktree status

## TASKS.md

Root `TASKS.md` is the only live tracker.

Update M08.48 truthfully.

Do not mark GPT visual PASS.

M08.47 should remain historical/partial with its audit result.

## Success state

If all eight final evidence sets are published and the four blockers are builder-closed:

`AWAITING_GPT_F08_F15_FINAL_VISUAL_AUDIT`

If one or more of the four blocked facilities still genuinely fail after bounded remediation:

`AWAITING_GPT_F08_F15_FINAL_VISUAL_AUDIT_WITH_RECORDED_BLOCKERS`

Either way, all 24 final frames must still be committed and available to GPT.

Do not stop at a local-only evidence state.

## Git publication

Commit:
- prompt-driven geometry/script changes
- audit reports/JSON
- the tracked final 24 images
- the three contact sheets
- execution log
- TASKS.md

Push safely to `origin/main`.

No force push.

Verify local HEAD == origin/main.

## Final response

Return only:
- F08–F15 result matrix
- final state
- tracked evidence directory
- execution log path
- canonical Blend/GLB hashes
- commit SHA
- local/origin sync state
- remaining blockers, if any
