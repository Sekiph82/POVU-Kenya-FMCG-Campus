# REV005 F08-R01 Camera-Contract Remediation — Codex Log

## Scope and preflight

- Executed M08.43 / F08-R01 only. No F09 work and no `TASKS.md` or locked-criteria edits.
- Inspected the initial checkout, inventoried the ignored staged F08 files, fetched `origin/main`, and fast-forwarded the clean `main` checkout to `1f028894e1f7dcab15ec3e25660889d3077cb324`. Local HEAD matched `origin/main` before publication.
- Re-read the tracker and confirmed M08.43 authorization.
- Verified the locked canonical baseline before camera work and again before publication:
  - Blend `3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`: `B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`.
  - GLB `3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`: `B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`.

## Staged-state recovery and technical validation

- The ignored local `F08_STAGED.blend` did not match the published accepted-manifest signatures. Per the prompt, rebuilt from the locked canonical Blend using the published `F08_build_scene.py` and `F08_visual_refine.py` sources, with their output redirected to `output/rev005-facility-gated/F08_bottle_blow/R01/F08_bottle_blow/`.
- The rebuilt stage is separate from the canonical Blend. The independent saved-state validator recorded PASS: 338 accepted meshes; 391/391 confirmed legacy retirement; 20 preforms; 16 heater elements (8 per bank); 2 service doors; 4 air branches; 16 formed bottles; zero unauthorized protection differences; zero cross-facility collisions; zero outside-envelope objects; and exact candidate GLB membership parity (10,888 expected / 10,888 actual).
- Rebuilt helper output differs from the earlier published manifest in four east-opening/wall signatures. These are recorded in the validation JSON and generated deterministically by the published helpers from the locked baseline. No corrective geometry edits were made.
- Re-ran camera-origin checks for each candidate. All 134 origins had no mesh bounding-box hits. No wall, ceiling, or floor clipping and no visibility changes were used.

## Candidate search and visual result

- Rendered 134 actual 900×600 previews: A 36, B 30, C 30, D 38 (minimum required: 36/30/30/36). Reviewed the rendered frames and role contact sheets; selection was based on visible composition, not metadata alone.
- Retained the 12 strongest frames for each role with four labeled 4×3 top-12 contact sheets. Candidate metadata records camera/target/lens, origin check, qualitative cue matrix, dominant occluder, process-sequence verdict, and preview paths.
- Selected attempts and direct rationale:
  - A `A_005`: feed-like preform carriers, heater, guarded cell, outfeed, and room floor/context appear together, but the hopper is not visually distinct and bottle discharge is too small to read; FAIL.
  - B `B_015`: heater outlet/guide, guarded cell, mould area, and outfeed are together, but transfer and formed-bottle cues are not sufficiently legible in one frame; FAIL.
  - C `C_028`: mould/cell and bottle outfeed are clearest, but the oven/transfer relationship is not adequately present in the same view; FAIL.
  - D `D_006`: heater, blow cell, HMI, partial feed, outfeed, and room context appear, but hopper/feed, operator/service relationship, and main aisle organization are not all readable; FAIL.
- Result: `BLOCKED_F08_R01_NO_COMPLETE_VISUAL_SET`. The selected attempts do not pass every hard role gate and the four images do not jointly establish the complete label-blind process sequence.

## Promotion and handoff

- Canonical promotion was not permitted. No canonical Blend or GLB was saved or replaced; their baseline hashes above remain unchanged.
- Evidence in this handoff: candidate JSON; top-12 previews/contact sheets; selected-attempt previews; staged-state validation and helper comparison; deterministic reconstruction, validation, rendering, and packaging scripts/logs; and this log.
- Stop state: `BLOCKED_F08_R01_NO_COMPLETE_VISUAL_SET`, awaiting GPT facility audit of the evidence. No acceptance is claimed.
