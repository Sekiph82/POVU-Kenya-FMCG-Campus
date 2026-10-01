# REV005 F04-X01 Targeted V09 Blocker Quarantine — Codex Log

## Final state

`AWAITING_GPT_F04_X01_INTEGRATED_AUDIT`

## Authorization and synchronization

- Task: M08.30 — F04-X01 targeted V09 blocker quarantine + historical restore
- Prompt: `coordination/Prompts/REV005_F04_X01_TARGETED_QUARANTINE_GPT_PROMPT.md`
- Locked criteria: `coordination/Audits/REV005_F04_X01_TARGETED_QUARANTINE_GPT_CRITERIA.md`
- Root cause: `coordination/Audits/REV005_F04_X01_CROSS_FACILITY_BLOCKER_ROOT_CAUSE.md`
- Root `TASKS.md` was read first.
- Clean canonical `main` was fast-forwarded from `e815806` to `f4cfa1e`.
- No reset, rebase, force push, or parallel Desktop checkout was used.

## Gate A — blocker verification

- Baseline Blend: `754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`
- Baseline GLB: `A426A25C19FA85D90CD741358554B484F641D730A4898872A50D7CA17DA07A1`
- `REV005_V08_CLEAN_TRAINING_ACADEMY`: exactly 81 objects.
- Training aggregate bounds overlap the historical Wellness Pavilion in plan by approximately 198 m².
- `V09_TRAINING_BOARD` verified at center `(30,-69.8,4)` with dimensions `7 × 0.12 × 3`.
- `V09_RESTAURANT_RIGHT_WALL` verified beyond the historical Restaurant_Wellness max-X of approximately 26 m.
- Diagnostic: `output/rev005-facility-gated/F04_x01/F04_X01_BLOCKER_DIAGNOSTIC.json`.

## Gate B/C — protected state and authorized quarantine

Only these authorized targets were changed:

1. `REV005_V08_CLEAN_TRAINING_ACADEMY` — 81 objects, hidden in viewport/render and tagged with the F04-X01 quarantine metadata.
2. `V09_RESTAURANT_RIGHT_WALL` — hidden in viewport/render and tagged with the same F04-X01 quarantine metadata.

No Restaurant object other than the named right wall was altered. No object was deleted, moved, or remodeled.

Protection parity is exact:

- F01: 76 objects
- F02: 79 objects
- F03: 30 objects
- Historical Glass Deck source: 392 objects
- Historical pavilion, `WELLNESS_GLASS`, `Restaurant_Wellness`, and V09 Wellness collection: unchanged
- Existing V09 Glass Deck quarantine: 117 objects unchanged

## Gate D — historical F04 restore

- Reused replay source commit `420038365847de763d64c8583a9e31ac5a6bd677`.
- Source hash: `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`.
- Restored exact composition: 10 BASE + 49 V01 = 59 objects.
- Destination collection: `REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`.
- Dimensional contract: PASS.

## Gate E/F — parity and integrated camera

- A/B destination renders were produced at 900×600 for independent visual parity review.
- Selected integrated camera: `(19.8999996,-61.9000015,5.1750002)`.
- Target: `(30.3000011,-69.9624939,2.1237502)`.
- Lens: 28 mm.
- Clear rays: 9/9.
- No hard projected-area gate was applied.
- Required renders were produced:
  - `F04_X01_A_CONTEXT.png` — 1440×960
  - `F04_X01_B_FUNCTIONAL.png` — 1440×960
  - `F04_X01_D_INTEGRATED_CONTEXT.png` — 1440×960
  - `F04_X01_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png` — 900×600

## Gate G — canonical save/export

- Final Blend SHA-256: `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`
- Final GLB SHA-256: `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`
- Canonical save/export completed only after the integrated camera and protection gates passed.
- No REV004, F05, REV006, `.hiveai`, or tour/video work occurred.

## Evidence

- Output folder: `output/rev005-facility-gated/F04_x01/`
- Validation: `F04_X01_VALIDATION.json`
- Camera: `F04_X01_CAMERA_VALIDATION.json`
- Quarantine: `F04_X01_QUARANTINE_MANIFEST.json`
- Final hashes: `F04_X01_FINAL_HASHES.json`

Independent GPT integrated audit is now required. Do not begin Facility 05.
