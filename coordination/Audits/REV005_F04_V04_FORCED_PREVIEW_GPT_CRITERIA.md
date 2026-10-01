# REV005 F04 V04 — FORCED CAMERA PREVIEW EVIDENCE — LOCKED GPT CRITERIA

## Purpose

F04 model/source gates are already proven:
- 10 BASE + 49 V01 = 59 objects
- dimensional contract PASS
- archived A/B parity PASS

V02 found multiple interior camera seeds with >=7/9 clear rays.
V03 produced zero preview images because every expanded candidate was rejected by geometric/framing eligibility before rendering.

V04 exists to stop the camera-search loop and let GPT inspect the **actual images**.

## Canonical mutation rule

Evidence-only.

Do NOT save canonical Blend.
Do NOT export/update canonical GLB.
Do NOT mutate any neighboring facility.
Do NOT quarantine/hide/exclude objects in the saved scene.

Locked canonical hashes:

Blend:
`754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`

GLB:
`A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

## Required preview policy

Render actual previews even if framing is imperfect.

A preview candidate is eligible if:
1. historical 59-object F04 is reconstructed in memory;
2. camera is not physically inside an F04 equipment mesh;
3. no QA-only object hiding/quarantine/exclusion is used;
4. LOS clear count is >=7/9.

For V04 preview generation ONLY:
- do **not** reject for projected area percentage;
- do **not** reject because the full union is partly clipped;
- do **not** reject because the camera is close to legitimate pavilion shell;
- do **not** reject merely for wide-angle distortion.

These are visual-review findings, not pre-render blockers.

## Required six previews

Produce six 900×600 PNG previews.

Selection:
- ranks 1–3: top three unique V02/V03 seed camera positions with highest clear-ray count, preferring 9/9 then 8/9 then 7/9;
- ranks 4–6: use the same best three camera positions but widen lens to improve framing:
  - if source lens >=45 mm, use 35 mm;
  - otherwise use 28 mm.

If fewer than three unique >=7/9 seeds exist, use all available and create remaining previews by lens variation 40/35/32/28 mm.

## Evidence JSON

For every preview record:
- source seed ID/rank
- camera XYZ
- target XYZ
- lens
- clear rays / 9
- first-hit table
- projected bbox
- projected area %
- clipping flags
- nearest geometry distance if available
- preview path/hash/bytes

## GPT visual gate

No candidate is auto-PASS.

GPT will inspect all six and decide:
- one camera is usable as-is;
- one camera needs a precise crop/distance/lens refinement;
- or the integrated-view concept must change.

## Stop

Stop exactly at:

`AWAITING_GPT_F04_V04_PREVIEW_REVIEW`

Do not save Blend/GLB.
Do not begin F05.
