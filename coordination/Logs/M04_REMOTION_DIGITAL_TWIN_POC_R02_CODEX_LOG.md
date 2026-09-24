# POVU Kenya FMCG Campus M04 — Remotion Digital Twin POC R02

## Result

- Status: **PASS**
- Mission: R02 Remotion digital-twin proof of concept only; long-form film production was not started.
- Date: 2026-09-24
- Repository: `https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus`
- Branch: `main`
- Renderer: local Windows Remotion 4.0.527 with local Chromium/ffmpeg; no Higgsfield, GitHub Actions, or cloud Blender worker used.

## Authoritative source and preservation

- Authoritative source: `3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb`
- Runtime copy: `remotion/povu-digital-twin/public/POVU_REV004_FINAL_MASTER.glb`
- REV004 source SHA-256: `1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA`
- The REV004 GLB was copied for runtime use and not modified.
- REV004 manifest counts: 2,221 objects, 2,082 mesh objects, 2,082 mesh data blocks, 104 materials, 55 cameras.
- The repository contained a blank Remotion scaffold for this R02 implementation; no committed R01 Remotion output was overwritten.

## Composition and output

- Composition ID: `R02`
- Canvas: 1920×1080
- Frame rate: 30 fps
- Duration: 1,800 frames / 60.000 seconds
- Codec: H.264 High profile
- Pixel format: `yuv420p`
- Output: `output/poc-r02/POVU_REMOTION_DIGITAL_TWIN_POC_R02.mp4`
- Output SHA-256: `5812D874B1F862B387186E11C774FCB2AF88F374216AE89D4BFB65626ADBF6B4`
- Output size: 17,155,684 bytes
- ffprobe evidence: `output/poc-r02/qa/ffprobe.json`

## Implementation

- `src/CameraPath.ts` provides deterministic Blender-Z-up to Three-Y-up conversion and interpolated camera keyframes covering the campus aerial, VIP approach, Water Wall, Hands of Growth, glass deck, and manufacturing route.
- `src/MaterialSystem.ts` classifies semantic source names into water, living wall, Hands of Growth, solar/PV, glass, machines, architecture, paving, landscape, and smart-totem treatments.
- `src/R02Video.tsx` loads the REV004 GLB, applies the runtime material system, renders deterministic lighting/environment/UI overlays, and provides the Water Wall shader, VIP façade treatment, Hands of Growth presentation layer, route indicator, process flow, and world-tracked machine labels.
- Water Wall motion is frame-driven (`uTime = frame / 30`); no wall-clock or `useFrame` animation is used.
- Production labels use world-space anchors and screen-space clamping to remain inside the output frame.

## Visual QA evidence

- Full-resolution checkpoints: **11/11 PASS** at frames 0, 180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, and 1797.
- Water Wall close-ups: **3/3 PASS** at frames 450, 500, and 535.
- Contact sheet: `output/poc-r02/qa/contact-sheet.png`
- Machine-readable QA report: `output/poc-r02/qa/qa-report.json`
- Camera route report: `output/poc-r02/qa/camera-route-report.json`
- Material report: `output/poc-r02/qa/material-override-report.json`
- Water Wall report: `output/poc-r02/qa/waterwall-qa.json`
- Label tracking report: `output/poc-r02/qa/label-tracking-report.json`
- QA checks covered: opening aerial visibility, VIP entry/doors/green wall/Water Wall, Hands of Growth presentation, glass deck route, production machinery, process labels, label bounds, and final-frame readability.

## Validation

- `npm run lint` passed: ESLint and TypeScript checks completed without errors.
- Remotion rendered all 1,800 frames successfully.
- Final ffprobe: H.264, 1920×1080, `yuv420p`, 30/1, 60.000000 seconds, 1,800 frames.
- The final H.264 was locally normalized with ffmpeg to the required `yuv420p` pixel format after the initial Remotion encode reported full-range `yuvj420p` signaling.

## Scope notes

- The source-massing geometry remains the REV004 GLB; runtime presentation overrides are limited to material classification, selected façade/production visibility staging, Water Wall shader presentation, Hands of Growth staging clarity, and labels/UI.
- This is a silent visual POC; no voiceover or long-form film pipeline was initiated.
- Existing unrelated untracked REV004 Blender backup/trial files were preserved and excluded from the R02 commit.

## Publication handoff

- Commit and push are required for this log, R02 source/configuration, runtime assets, output MP4, QA checkpoints/reports, and contact sheet.
