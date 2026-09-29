# REV005 F02 Daycare / Crèche Restore — Codex Execution Log

Task: M08.26 — Facility-Gated F02 Daycare / Crèche historical restoration

Status: AWAITING_GPT_FACILITY_AUDIT_F02

Canonical authorization was verified after fetch + `git merge --ff-only origin/main` at `e1a1fbbf412f41fcfe2f8e5ff127abd98cb0bfcd`.

Pre-mutation baseline:

- Blend SHA-256: `80C4FC83DBD260CB9D0A6B02F0582C5829273450437B90D7CD2B9281C17B744E`
- GLB SHA-256: `9EA90C327C2502AA019AD9ADA656BE0BC0B652A19724BEF3162910058B63FD40`
- F01 protection manifest: `output/rev005-facility-gated/F02_daycare/F02_F01_PROTECTION_BEFORE.json`
- Quarantined Glass Deck collection verified hidden with 117 direct objects.

Historical replay:

- Detached temp worktree commit: `420038365847de763d64c8583a9e31ac5a6bd677`
- Initial replay Blend SHA-256: `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
- Replay order: V01 → V02 → V03 → V04 → V05
- Source composition: 41 BASE + 38 V03 = 79; V01/V02/V04/V05 = 0
- V03 dimensional contract: PASS at <=0.001 m tolerance
- Archived V05 A/B decoded-pixel parity: PASS; raw PNG metadata differed only

Canonical F02-only mutation and verification:

- Removed only the 42 current Daycare inventory objects and existing V03 Daycare objects; preserved 16 legacy hidden architecture/QA objects.
- Appended local data into `REV005_FG_F02_DAYCARE_ACCEPTED_V05_REPLAY` with exactly 79 visible accepted objects: 41 BASE + 38 V03.
- Destination transform/material/parent contract: PASS; manifest: `output/rev005-facility-gated/F02_daycare/F02_DESTINATION_MANIFEST.json`.
- Destination A/B evidence: visual-match gate PASS. B is decoded-pixel exact; A differs at six antialias edge pixels (13 normalized channels) while remaining visually identical. This delta is retained transparently in `F02_DESTINATION_PARITY_HASHES.json` for GPT audit.
- F01 protection: PASS; 76 names, transforms, dimensions, materials, parents, and visibility unchanged.
- Glass Deck quarantine: unchanged; collection hidden in viewport/render with 117 direct objects.
- Integrated collision preflight: PASS across 8 azimuth candidates; selected azimuth 45 degrees, 9/9 clear rays, no blockers, fully in frame, 36.4232% Daycare screen coverage, no automatic cross-facility exclusion/quarantine.
- Context renders: `F02_A_CONTEXT.png`, `F02_B_FUNCTIONAL.png`, `F02_D_INTEGRATED_CONTEXT.png`, and `F02_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png`; all non-black.
- Final Blend SHA-256: `E935539393BBF83173004E7BBA97A5432818C355752ABAA55A88F685C707A0E8`
- Final GLB SHA-256: `2F593CC82ED68499B5F23C64495229CFEB482C0C44C64F341938802B4A68C277`
- Validation manifest: `output/rev005-facility-gated/F02_daycare/F02_VALIDATION.json`
- Protected controls verified unchanged: `TASKS.md`, locked F02 audit criteria, REV004, no REV006, no `.hiveai`, no tour/video, and no F03 execution.

Stop state: `AWAITING_GPT_FACILITY_AUDIT_F02`
