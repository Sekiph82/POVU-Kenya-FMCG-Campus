# REV005 F04-X02 Destination Parity Evidence — Codex Log

## Final state

`BLOCKED_F04_X02_DESTINATION_PARITY`

## Authorization and synchronization

- Task: M08.32 — F04-X02 destination parity evidence correction
- Prompt: `coordination/Prompts/REV005_F04_X02_PARITY_EVIDENCE_GPT_PROMPT.md`
- Root `TASKS.md` was read first.
- Clean canonical `main` was safely fast-forwarded from `674a6bf4469bc1810b7e51145671e0c18a0d8d53` to `4474bb76fb15cfabb7c0083df63d5deee3f833d4`.
- No reset, rebase, stash, or force-push was used.

## Source and protection gates

- Canonical pre-render Blend SHA-256 matched the locked X02 baseline: `DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`.
- Canonical pre-render GLB SHA-256 matched the locked X02 baseline: `812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`.
- Exact destination: `REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`, 59 unique objects, 10 BASE + 49 V01.
- Historical V05 object-selection semantics independently resolved 59 objects and exactly matched the destination set.
- F01/F02/F03 protection counts verified: 76 / 79 / 30.
- Historical Glass Deck source verified: 392 objects; V09 Glass Deck quarantine: 117 objects.
- V09 Training quarantine verified: 81 objects; `V09_RESTAURANT_RIGHT_WALL` quarantine intact.

## Evidence-only render isolation

- Blender 5.2.2 Workbench; historical V05 camera, lens, sensor, lighting, cavity, background and 900×600 output settings used.
- Facility-only visibility isolation touched 10,605 object render-visibility flags; all original object and collection visibility flags were recorded and restored in memory.
- All 59 F04 destination objects were shown; all other scene objects were hidden for the parity renders.
- Canonical Blend was not saved; GLB was not exported.

## Parity result

- A raw destination SHA-256: `CDB1BF8549DC630E81CC8674BD8BA1DE1376FD068A3FAB75FABBF158BFFCAB3E`.
- A comparison: 63,944 differing pixels, 184,018 differing normalized channels, maximum absolute channel delta 134; decoded pixels are not equal.
- B raw destination SHA-256: `B2E8D4F3E08B39D9CE574487A31990DF1012A38B45363C789EEA83A960C1BEDD`.
- B comparison: 109,361 differing pixels, 317,142 differing normalized channels, maximum absolute channel delta 133; decoded pixels are not equal.
- Both differences are structural/image-content differences, not microscopic antialias-only variation. Per the locked prompt, parity is blocked; no attempt was made to alter canonical geometry or conceal the difference.

## Evidence files

- `output/rev005-facility-gated/F04_x02/F04_X02_DEST_PARITY_A_900x600.png`
- `output/rev005-facility-gated/F04_x02/F04_X02_DEST_PARITY_B_900x600.png`
- `output/rev005-facility-gated/F04_x02/F04_X02_DESTINATION_PARITY.json`
- `output/rev005-facility-gated/F04_x02/F04_X02_CANONICAL_HASH_PROOF.json`

Stop at `BLOCKED_F04_X02_DESTINATION_PARITY`. Do not begin F05.
