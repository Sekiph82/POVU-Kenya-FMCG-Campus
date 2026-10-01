# REV005 F05 Fire Pump House Primary Restoration — Codex Log

## Final state

`AWAITING_GPT_FACILITY_AUDIT_F05`

Independent GPT facility audit remains required. Codex does not promote this task to final acceptance.

## Authorization and source controls

- Task: `M08.34 — Facility-Gated F05 Fire Pump House primary historical restoration`.
- Root `TASKS.md` was re-read after safe fast-forward to `4fd49a647224727139f45016fa21d5c1ca724418`; M08.34 was READY and F06 was not started.
- Canonical workspace remained `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`.
- No reset, rebase, force push, second Desktop copy, TASKS.md edit, locked-criteria edit, or F06 work.

## Baselines and replay

- Canonical Blend baseline SHA-256: `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`.
- Canonical GLB baseline SHA-256: `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`.
- Detached replay commit: `420038365847de763d64c8583a9e31ac5a6bd677`.
- Historical initial Blend SHA-256: `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747`.
- Unmodified V01→V05 replay completed. V05 replay Blend SHA-256: `E0D19E6CE2F8029FED6B20DA8C58340153B203E5B548942A95AF7666ABB59796`; replay GLB SHA-256: `B08AB2A38CFA5540F62DF166D292CDB9643806AFEF67195EC5D5EBCCB429062C`.

## Exact historical selection

- Original V05 `objects_for("Fire pump house", record)` resolved 123 objects.
- Spatial split by actual world-center Y: primary `<30` = 54; secondary `>=30` = 69.
- Contribution totals: BASE 10, V01 15, V04 44, V05 54.
- Primary contribution: BASE 5, V01 0, V04 22, V05 27.
- Secondary contribution: BASE 5, V01 15, V04 22, V05 27.

## Restoration and protection

- Only the primary-zone 54-object F05 representation was transferred into `REV005_FG_F05_FIRE_PUMP_PRIMARY_ACCEPTED_V05_REPLAY`.
- The secondary 69 objects remained present and spatially unchanged.
- Destination collection count: exactly 54.
- F01/F02/F03/F04 accepted counts protected: 76 / 79 / 30 / 59.
- Existing Glass Deck and Training quarantine counts protected: 117 / 81.
- Restaurant right-wall quarantine and historical Glass Deck / Wellness / pavilion protection states were retained.

## Dimensional and visual gates

- Primary V04/V05 dimensional anchors passed at the required 0.001 m tolerance; rotation tolerance recorded as 0.0001 rad.
- Historical V05 A/B/C source renders reproduced the locked references exactly at decoded-pixel level; expected SHA-256 values are recorded in `F05_SOURCE_RENDER_HASHES.json`.
- Destination A/B/C parity passed the exact V05 `show_only()` rule. Raw PNG metadata differed; decoded content was structurally identical apart from sparse antialias-edge pixels (the same microscopic edge-difference class accepted in the prior REV005 parity audit).
- Integrated historical A camera `(76,-22,15)` targeting `(94,-5,3)` achieved 9/9 clear LOS rays with no QA hiding, quarantine, or neighbor mutation.
- Final A/B/C/D QA renders were produced at 1440×960; D preview was produced at 900×600.

## Final artifacts

- Final Blend SHA-256: `E331FB7ADA9BF10DA43B544EDF6189A34D86002C5D3CD82FE74DA7D8CF019D07`.
- Final GLB SHA-256: `98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`.
- Evidence directory: `output/rev005-facility-gated/F05_fire_pump/`.
- F05 evidence includes source/primary/secondary manifests, dimensional validation, source and destination parity renders, current pre-restore manifest, protection before/after, integrated camera validation, final QA renders, baseline/final hashes, and validation status.

Stop at `AWAITING_GPT_FACILITY_AUDIT_F05`.
