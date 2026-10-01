# REV005 F06 Micro-ingredient Weigh / Dispense — Codex Restoration Log

## Scope and stop state

- Task: `M08.36` / Facility `F06` only.
- Class: `R` historical restoration.
- Starting canonical commit: `27808edbf3547244874d8cc923b7a3297959812f`.
- No `TASKS.md` edit was made. `F07` was not started.
- Final handoff marker: `AWAITING_GPT_FACILITY_AUDIT_F06`.

## Historical replay

- Detached source commit: `420038365847de763d64c8583a9e31ac5a6bd677`.
- Historical V05 Blend SHA-256: `266A4706FD994ACF171B5C5E3C8E0371CEAD5223888E8BE1B202D25901E294B5`.
- Historical V05 GLB SHA-256: `B08AB2A38CFA5540F62DF166D292CDB9643806AFEF67195EC5D5EBCCB429062C`.
- Exact unchanged V01→V02→V03→V04→V05 replay selection: `43` objects.
- Contribution split: `BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1`.
- Historical V05 renderer resolved `43` objects and its A/B/C images were pixel-identical to the archived references.

## Canonical restoration

The canonical scene already contained the exact historical 43-object selection with matching names, dimensions, locations, materials, and source collections. The restoration therefore bound those existing objects into `REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`; it did not duplicate geometry, broad-delete spatial neighbors, or mutate F01–F05 protected content.

- Destination collection count: `43`.
- Dimensional anchor validation: `PASS` (`0.001 m` center/dimension tolerance; `0.0001 rad` rotation tolerance).
- Destination A/B/C parity: `PASS`; decoded pixel gate passed for all three views. A/B had only bounded renderer deltas (max channel deltas `8` and `22`, respectively); C was exact.
- Protection comparison: `PASS`; unauthorized object diffs `0`, unauthorized field diffs `0`.
- Integrated camera candidates: `12`; selected `FRONT_LEFT`; line of sight `9/9`; current-context and no-QA-hiding gates passed.

## Final artifact hashes

- Canonical Blend: `BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`.
- Canonical GLB: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.

## Evidence

All F06 evidence is under `output/rev005-facility-gated/F06_micro_weigh/`, including the replay source manifest, dimensional validation, source/destination parity, pre-restore inventory, protection before/after/diff, integrated camera candidates/validation, final hashes, final QA renders, and `F06_VALIDATION.json`.

Codex status is readiness for the named independent GPT facility audit; it does not award the audit PASS.
