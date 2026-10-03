# REV005 M08.47 F08–F15 Independent GPT Combined Audit

## Verdict

`REMEDIATION_REQUIRED_EVIDENCE_PUBLICATION_AND_4_FACILITY_VISUAL_CLOSURE`

M08.47 is technically coherent but cannot receive independent combined visual acceptance yet.

## What is independently verified

The published GitHub evidence supports the following technical findings:

- The campaign resolved F08–F15 identities from repository truth.
- The canonical selective promotion changed only F10, F12, F13 and F14.
- Non-promoted Blender scene signature: 11,052 baseline objects, 11,052 final objects, zero removed, zero new, zero changed.
- Exact GLB named-node parity passes:
  - baseline nodes: 10,941
  - prior promoted-target nodes replaced: 350
  - new promoted-target nodes: 595
  - expected final nodes: 11,186
  - exported nodes: 11,186
  - missing: 0
  - extra: 0
- Actual solid-camera-origin validation reports PASS for all 24 final view origins.
- Canonical hashes after selective promotion:
  - Blend: `83D00D7C18B4DED5B8E674AEF3DF77659E21C9E6035F2CAD318E7F6B414AC3E6`
  - GLB: `18C146559F5675D6FE36759328F14CDD44F3626C5571B5671D3DCE6F33BAB5D0`

These technical gates are accepted.

## Visual audit blocker

The 24 final 1280×800 facility renders and final contact sheets are recorded only under the ignored local path:

`output/rev005-facility-gated/F08_F15_combined/`

They are not present in GitHub. The repository API returns 404 for that evidence directory.

Therefore the independent auditor cannot directly inspect the actual final PNGs that the builder used to claim:

- F10 BUILDER_VISUAL_PASS
- F12 BUILDER_VISUAL_PASS
- F13 BUILDER_VISUAL_PASS
- F14 BUILDER_VISUAL_PASS

Those four promoted facilities remain technically promoted but visually **UNVERIFIED BY GPT**. They must not be marked independent PASS until the exact final audit images are published and directly reviewed.

This is an evidence-publication failure, not evidence that F10/F12/F13/F14 visually fail.

## Builder-recorded blockers accepted as remediation inputs

The combined builder log records four unresolved visual defects. These are consistent with the preceding audit history and are accepted as the scope for the next bounded remediation:

### F08 — Bottle Blow Molding
Still fails complete label-blind process sequence readability. Required closure is a visually obvious:
heated preform → load/stretch/blow → formed bottle → eject/release → outfeed sequence.

Do not restart broad camera search.

### F09 — Chemical Compound / Controlled Receiving
Receiving, IBC/drum handling, bulk tanks and metered pump/transfer equipment do not read as one continuous receiving-to-process relationship.

Required closure is a visually connected:
receiving/check → IBC/drum containment → bulk/storage interface → pump/meter/transfer route.

### F11 — Finished Goods Warehouse / Dispatch
Storage/staging/dock elements exist, but the handling vehicle is not legible enough and the staging → dispatch check → dock/loading relationship remains weak.

Required closure is a visually obvious handling and loading chain with a recognizable forklift/AMR or other canonical handling vehicle.

### F15 — Packaging Warehouse
Storage and issue elements exist, but inbound receiving versus outbound issue-to-production roles are not clearly separated, and the vehicle is not legible enough.

Required closure is a visually obvious:
receiving/inspection → segregated packaging storage → issue staging/lane → production handoff,
plus a recognizable handling vehicle in context.

## Required next action

Run one combined M08.48 remediation/publication task.

Do not redo F10/F12/F13/F14 geometry unless direct rerender inspection exposes a genuine visual defect.

M08.48 must:

1. Preserve the current accepted technical promotion state for F10/F12/F13/F14.
2. Remediate only F08/F09/F11/F15, using facility-specific geometry/process fixes before camera changes.
3. Use bounded camera work only.
4. Re-run protection and exact GLB parity after any new promotion.
5. Publish the final audit images for **all eight facilities** into a Git-tracked evidence directory.
6. Publish the exact individual final views, not only a textual report.
7. Stop only at `AWAITING_GPT_F08_F15_FINAL_VISUAL_AUDIT` or a truthful blocker variant.

## Independent acceptance state after this audit

- F08: REMEDIATION REQUIRED
- F09: REMEDIATION REQUIRED
- F10: TECHNICAL PASS / VISUAL UNVERIFIED
- F11: REMEDIATION REQUIRED
- F12: TECHNICAL PASS / VISUAL UNVERIFIED
- F13: TECHNICAL PASS / VISUAL UNVERIFIED
- F14: TECHNICAL PASS / VISUAL UNVERIFIED
- F15: REMEDIATION REQUIRED

M08.47 therefore remains open and is superseded operationally by M08.48.
