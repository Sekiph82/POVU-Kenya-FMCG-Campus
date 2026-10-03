# M08.45 — REV005 F08-R03 External South-Frontage Visual Closure Log

## Scope and synchronization

- Authorized task: `M08.45 — F08-R03 external south-frontage visual closure` only.
- Repository: `Sekiph82/POVU-Kenya-FMCG-Campus`; branch `main`.
- Initial checkout was clean at `26e55140ca75a99c4ba8088c541d2339c6dbe086`, matching the then-known `origin/main`.
- Fetched `origin/main` and fast-forwarded only to `f935c0c03cac6351`; local `main` matches the live `origin/main` task authorization for M08.45 / F08-R03.
- Root `TASKS.md` and all locked R03/R02 criteria/audit files were read and not edited. No F09 work was started.
- R03 output under `output/` is ignored by the repository, so exact task evidence is force-added at publication. No owner-local prior R03 output existed at task start.

## Exact source and locked baselines

- Source: `output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`.
- Required SHA-256 verified before and after rendering: `0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`.
- R03 camera transforms were applied only in the in-memory Blender render session. The R02 staged Blend was not saved or modified.
- Canonical Blend SHA-256 rechecked: `B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642` (locked baseline preserved).
- Canonical GLB SHA-256 rechecked: `B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372` (locked baseline preserved).
- No geometry, material, transform, collection membership, visibility, retirement/quarantine, room-shell, or protected-neighbor changes were made.

## Candidate search and technical camera gate

- Rendered 24 distinct 900×600 candidates per family (A/B/C/D), 96 total. All preview files exist.
- Every frame was reviewed on its role's 24-image contact sheet; top eight individual previews and a 4×2 sheet were retained for each family.
- Camera-origin checks used every scene mesh world-space AABB. A=24 clear; B=24 clear; C=0 clear; D=24 clear.
- A/B/D candidates were placed at authorized elevations above the Production_Hall and roof AABB tops. C is constrained to Z=3.5…6.0 m. The `Production_Hall` world AABB spans X=-75…75, Y=-36…36, Z=-6…6 and `PRODUCTION_ROOF` reaches Z=6.0 m. Every C camera with X/Y inside the authorized ranges and Z≤6.0 is therefore inside/on these mesh AABBs. The C images were rendered solely to review composition; all 24 are marked invalid as camera candidates. No allowed C origin satisfies the required “outside every mesh AABB” gate.
- No glazing, wall, camera visibility, or other scene visibility was changed. The south-frontage mullions remain visible and intrude on some process sightlines.

## Selected views and direct visual rationale

- A selected `A_005`: distinct hopper/funnel, feed/elevator path, oven, guarded cell, and outfeed appear in west-to-east order. The glazing posts cross portions of the line and the product states are too small to establish the full label-blind sequence. FAIL.
- B selected `B_005`: heater outlet, transfer hardware, guarded twin stations, and outfeed are present. Clamp/stretch-blow action and individual formed bottles are not sufficiently readable at 900×600. FAIL.
- C selected `C_005` for diagnosis only: the mould/clamp stations and adjacent outfeed are visible, but the preform-to-bottle state change is not readable. The camera is AABB-invalid, as are all allowed C positions. FAIL.
- D selected `D_005`: hopper/feed, oven, blow cell, outfeed, HMI/operator pad, aisle, and room context appear together. Product states remain too small to make the complete label-blind sequence self-explanatory. FAIL.
- No role passes; the required collective sequence remains unestablished at the required label-blind readability.

## R02 technical facts and promotion

- R02 published technical gates and the independent R02 audit report: accepted meshes=391; retired legacy=391; NOT_F08 preserved=5; preforms=30; elevator riders=6; downstream feed preforms=7; oven path preforms=13; transfer riders=3; heater elements=16; formed outfeed bottles=16; unauthorized protected differences=0; cross-facility collisions=0; outside-envelope objects=0; dimensional and protection validation PASS.
- No new technical rerun or GLB membership parity was performed because the R03 visual gate failed; these facts are explicitly carried as inherited R02 results in `F08_R03_STAGED_STATE_VALIDATION.json`.
- Canonical promotion was not authorized or attempted. Canonical Blend/GLB hashes remain at the locked baselines above.

## Stop

- Exact stop: `BLOCKED_F08_R03_EXTERNAL_FRONTAGE_VISUAL_FAILURE`.
- Further camera-only F08 work is not permitted by the task gate.
- F09 was not started.

