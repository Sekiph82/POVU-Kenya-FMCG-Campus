# REV005 F04-X03 SHOW_ONLY Parity Replay — Codex Log

## Final state

`AWAITING_GPT_F04_X03_FINAL_AUDIT`

The replay is evidence-only. Independent GPT audit remains required; Codex does not promote the task to final acceptance.

## Authorization and source controls

- Task: `M08.33 — F04-X03 EXACT V05 SHOW_ONLY PARITY REPLAY`.
- Prompt: `coordination/Prompts/REV005_F04_X03_SHOW_ONLY_PARITY_GPT_PROMPT.md` supplied at the authorized GitHub main-branch URL.
- Read: root `TASKS.md`, the F04-X02 root-cause finding, historical V05 renderer, and F04 historical source provenance.
- Root `TASKS.md` was not edited. F05 was not started.
- No canonical geometry, object data, collection membership, quarantine state, Blend, or GLB was modified or saved.

## Canonical baseline and destination gates

- Blend before/after SHA-256: `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`.
- GLB before/after SHA-256: `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`.
- Destination collection: `REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`.
- Historical V05 selection: 59 unique objects, exactly equal to the destination collection.
- Composition: 10 BASE + 49 V01.
- F01/F02/F03 protection counts: 76 / 79 / 30.
- Quarantine checks: Training 81 objects, Glass Deck 117 objects, `V09_RESTAURANT_RIGHT_WALL` quarantined.

## Exact historical SHOW_ONLY replay

The historical V05 rule was applied in memory only for each render:

- hide objects outside the selected 59-object set;
- hide non-`MESH`/`CURVE`/`SURFACE` objects;
- hide selected objects containing `_LEFT`, `_RIGHT`, `_BACK`, `_SOFFIT`, or `_CEILING_BEAM`.

The selected F04 shell-hidden list resolved exactly to:

- `RM_WELFARE_SHOWER_BACK_0`
- `RM_WELFARE_SHOWER_BACK_1`
- `RM_WELFARE_SHOWER_BACK_2`
- `RM_WELFARE_SHOWER_BACK_3`

Visibility records covered 10,605 objects and 35 collections. All `hide_render` and `hide_viewport` flags were restored exactly in memory after rendering.

## Render and parity evidence

Blender 5.2.2 Workbench, 900×600 PNG, STUDIO/MATERIAL shading, shadows and WORLD cavity, ridge 1.8, valley 1.2, viewport background `(0.08, 0.10, 0.12)`.

- A: camera `(14,-88,13)` targeting `(30,-70,3)`, 52 mm / 36 mm; raw SHA-256 `F8B1E81797F9E86A1831C9E5ACBE997CB2CFA8C1ED80428CF640098B9114C4F1`; 99 differing pixels, 192 differing normalized channels, max delta 30.
- B: camera `(20,-78,8)` targeting `(30,-70,3)`, 52 mm / 36 mm; raw SHA-256 `465ACEB151ECE8492A87CD121A4D9097D8FC50FFA810F238285623457AE38141`; 35 differing pixels, 78 differing normalized channels, max delta 30.

Decoded pixels are not byte-for-byte identical to the archived references, but direct image inspection found only sparse edge-pixel antialiasing differences and no structural/image-content difference. This is recorded as the accepted microscopic-antialias-only case; raw metrics remain preserved in `F04_X03_DESTINATION_PARITY.json`.

## Evidence files

- `output/rev005-facility-gated/F04_x03/F04_X03_SHOW_ONLY_DIAGNOSTIC.json`
- `output/rev005-facility-gated/F04_x03/F04_X03_DEST_PARITY_A_900x600.png`
- `output/rev005-facility-gated/F04_x03/F04_X03_DEST_PARITY_B_900x600.png`
- `output/rev005-facility-gated/F04_x03/F04_X03_DESTINATION_PARITY.json`
- `output/rev005-facility-gated/F04_x03/F04_X03_CANONICAL_HASH_PROOF.json`

Runtime note: Blender wrote both renders and all evidence successfully; it emitted an exit-time `EXCEPTION_ACCESS_VIOLATION` from `igxelpicd64.dll` after artifact generation. Post-run file, JSON, hash, and visibility-restoration checks passed.

Stop at `AWAITING_GPT_F04_X03_FINAL_AUDIT`.
