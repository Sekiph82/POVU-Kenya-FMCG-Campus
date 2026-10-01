# REV005 F04 V03 — INTERIOR CAMERA CANDIDATE SELECTION — LOCKED GPT CRITERIA

## Purpose

F04 source/model restoration already passed:
- 10 BASE + 49 V01 = 59 objects
- dimensional contract PASS
- archived A/B parity PASS

V02 tested 432 interior-camera candidates. Best candidates reached 7/9 clear rays but failed the numeric 35–78% coverage gate.

That coverage threshold is no longer the acceptance authority for F04 integrated evidence.

For V03, Codex must produce a small set of **evidence-only candidate previews** for GPT to inspect visually.

## Canonical mutation rule

V03 camera selection is evidence-only.

Do NOT save the canonical Blend.
Do NOT export/update the canonical GLB.
Do NOT mutate F01/F02/F03/Wellness/Training/Restaurant/Glass Deck.
Do NOT quarantine/hide neighbors in the saved scene.

Canonical hashes must remain:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

## Candidate eligibility

Each preview candidate must satisfy:

1. F04 historical 59-object source restored in memory only.
2. Destination A/B parity already revalidated or truthfully reused from unchanged source evidence.
3. Camera lies inside the legitimate historical Wellness Pavilion interior volume.
4. Camera is not inside F04 equipment or unrelated visible equipment.
5. No QA-only hiding/quarantine/exclusion.
6. At least **7/9** LOS rays clear.
7. Entire projected F04 union fits inside the frame with no clipping:
   - X within 1%–99%
   - Y within 1%–99%
8. Frame visibly contains some legitimate pavilion/interior context.
9. F04 remains visually legible as changing/shower/locker support.

There is **no hard projected-area percentage gate** in V03. GPT will select/reject based on the actual previews.

## Candidate search expansion

Starting from the best 7/9 V02 candidates, Codex may vary:
- camera distance along the camera-target vector;
- camera height within pavilion safe limits;
- target Z within F04 bounds;
- lens: 52, 45, 40, 35, 32, 28 mm.

Do not go below 28 mm.

Do not change scene geometry.

## Required evidence

Commit exactly six 900×600 PNG candidate previews where possible:

- F04_V03_CANDIDATE_01_PREVIEW_900x600.png
- ...
- F04_V03_CANDIDATE_06_PREVIEW_900x600.png

If fewer than six eligible candidates exist, commit all eligible candidates and state the count.

Also commit:
- `F04_V03_CAMERA_CANDIDATES.json`
- `coordination/Logs/REV005_F04_V03_CAMERA_CANDIDATES_CODEX_LOG.md`

For each candidate record:
- camera XYZ
- target XYZ
- lens
- 9-ray table / clear count
- projected F04 bbox
- projected area percentage for information only
- nearest non-F04 geometry distance
- visible pavilion-context objects
- PNG path/hash/bytes

## Stop

Stop at:

`AWAITING_GPT_F04_V03_CAMERA_SELECTION`

Do not save Blend/GLB.
Do not begin F05.
