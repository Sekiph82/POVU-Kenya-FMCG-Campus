# REV005 F01-X01 Glass Deck Overlap Quarantine — Codex Log

## Final state

`AWAITING_GPT_F01_X01_INTEGRATED_AUDIT`

## Scope

This execution quarantined only the proven-invalid V09 replacement collection:

`REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`

No Glass Deck rebuild was performed. F01 Caps & Trigger, the historical Glass Deck source, Bottle Blow, Wet Processing, other facilities, REV004 and REV006 were not remodeled.

## Pre-mutation proof

- Accepted F01 selection: 76 objects.
- V09 replacement collection: 117 direct objects.
- F01 exact world bounds: X `38.5–66.0`, Y `23.5–38.5`, Z `0.664–5.5`.
- V09 collection aggregate bounds: X `49.91–90.5`, Y `11.87–36.09`, Z `0–8`.
- Exact aggregate AABB overlap: X `49.91–66.0`, Y `23.5–36.09`, Z `0.664–5.5`; plan area `202.57310437622073 m²`; volume `979.6435378829058 m³`.
- Historical `GLASS_DECK_LINK`: X `66–74`, Y `-6–46`, Z `8.199999809265137–12.199999809265137`.
- Historical `GLASS_DECK_LINK_FLOOR`: X `66.25–73.75`, Y `-5.5–45.5`, Z `8.359999656677246–8.539999961853027`.

## Quarantine

Only the named V09 collection and its 117 direct objects were set `hide_viewport=true` and `hide_render=true`. Each direct object received the required `REV005_CROSS_FACILITY_QUARANTINED`, reason and owner metadata. No object was deleted or moved.

## Protection and camera QA

- F01 76-object protection parity: PASS.
- Historical Glass Deck protection parity: PASS.
- Outside-collection mutations: none detected.
- Temporary camera exclusions: none.
- Selected camera: `(13.470107078552246, -7.779893398284912, 44.21428680419922)`.
- Target: `(52.25, 31.0, 3.5655999183654785)`.
- Lens: `52 mm`.
- Clear rays: `9/9`.
- F01 projected screen coverage: `46.002223398145745%`.

## Outputs

- Main: `output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V03.png` — SHA-256 `066AA81C418B5CF248991152134FE9FF213984FAE7973F6C4DA83E8CDD3907F6`, 1440×960, 1,697,389 bytes.
- Preview: `output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT_V03_PREVIEW_900x600.png` — SHA-256 `C7F62DC596CB56BA37BEB233C563DFCCD32D0CD259E889F501B2540C152F33A1`, 900×600, 681,959 bytes.

## Canonical artifacts

- Blend after quarantine: SHA-256 `80C4FC83DBD260CB9D0A6B02F0582C5829273450437B90D7CD2B9281C17B7444E`.
- GLB after quarantine: SHA-256 `9EA90C327C2502AA019AD9ADA656BE0BC0B652A19724BEF3162910058B63FD40`.
- GLB export policy: `use_visible=True`.

## Scope controls

`TASKS.md`, locked audit criteria, REV004, REV006, `.hiveai`, Bottle Blow, Wet Processing, other facilities and tour/video outputs were not edited or created.

Independent GPT audit remains pending. Facility 02 was not started.
