# REV005 F03 Electrical / LV-MV Room Restore — Codex Execution Log

Task: M08.28 — Facility-Gated F03 Electrical / LV-MV historical restoration  
Status: AWAITING_GPT_FACILITY_AUDIT_F03  
Actor: CODEX  
Workflow: READY_FOR_CODEX_EXECUTION

## Governed execution

- Root `TASKS.md` was read before synchronization and was not edited.
- Canonical checkout was clean, fetched from `origin/main`, and fast-forwarded only to `d6ad311faa13fba60950437badd72fb227723261`.
- Baseline Gate A passed before mutation: Blend `E935539393BBF83173004E7BBA97A5432818C355752ABAA55A88F685C707A0E8`; GLB `2F593CC82ED68499B5F23C64495229CFEB482C0C44C64F341938802B4A68C277`.
- Historical replay used the detached OS-temp worktree at commit `420038365847de763d64c8583a9e31ac5a6bd677`, with no historical script edits, no `.hiveai`, no REV006, and no tour/video render.

## F03 evidence

- Exact original V05 selection: 30 objects = 7 BASE + 23 V01; V02/V03/V04/V05 = 0; `REV005_LV_SAFETY_SIGN` excluded.
- V01 dimensional contract: PASS, 46 checks, 0.001 m tolerance.
- Source V05 A/B: decoded-pixel exact against archived references; raw hashes are recorded in `F03_SOURCE_RENDER_HASHES.json`.
- Destination collection: `REV005_FG_F03_ELECTRICAL_LV_MV_ACCEPTED_V05_REPLAY`, exactly 30 objects.
- Destination A/B visual match: B is decoded-pixel exact; A differs from the archived image at two antialias edge pixels, recorded explicitly in `F03_DESTINATION_PIXEL_GATE.json` and `F03_DESTINATION_PARITY_HASHES.json`.
- F01 protection: 76/76 exact before/after parity.
- F02 protection: 79/79 exact before/after parity.
- Historical Glass Deck source: 392/392 exact before/after parity.
- V09 Glass Deck quarantine: 117/117 exact before/after parity; quarantine collection unchanged.

## Integrated collision preflight

- Eight azimuth candidates tested: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°.
- Selected azimuth: 225°; camera `(92.6152267, 42.6152229, 16.8199997)`, target `(111, 61, 3.7740002)`, lens 52 mm.
- LOS: 9/9 clear rays; no immediate architectural intersection; F03 fully in frame; projected screen coverage 32.645953%.
- No automatic exclusion, hiding, or quarantine of another facility.

## Canonical outputs

- Final Blend SHA-256: `754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`.
- Final GLB SHA-256: `A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`.
- Evidence root: `output/rev005-facility-gated/F03_electrical_lv_mv/`.
- Review renders: `F03_A_CONTEXT.png`, `F03_B_FUNCTIONAL.png`, `F03_D_INTEGRATED_CONTEXT.png`, and `F03_D_INTEGRATED_CONTEXT_PREVIEW_900x600.png`.

No other facility was executed. Final stop state: `AWAITING_GPT_FACILITY_AUDIT_F03`.
