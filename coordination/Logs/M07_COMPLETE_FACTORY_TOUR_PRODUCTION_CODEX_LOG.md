# M07 Complete Factory Tour Production CODEX Log

## Scope

This log records the local Remotion production of the M07 long-form campus and factory tour from the frozen REV004.1 GLB. The workflow is restartable at the first chapter without a genuine PASS gate.

## Source and authority

- Frozen source: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`
- Required SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`
- Planning baseline: M06 V02 commit `1ebb97007e0e3b9a90574d8cb3695a6afe89672d`
- Renderer: local Windows Remotion/Three.js project under `remotion/povu-digital-twin`
- Delivery contract: 1920x1080, 30 fps, H.264, yuv420p

## Execution ledger

| Event | Evidence | Result |
|---|---|---|
| M07 brief read | Attached M07 final long-form production master | PASS |
| Frozen GLB verified | Exact SHA-256 above | PASS |
| V02 planning loaded | 69 matrix rows, 66 REQUIRED, 62 shots, 11 chapters | PASS |
| Source copied to Remotion public input | `public/POVU_REV004_1_FINAL_MASTER.glb`, exact SHA preserved | PASS |
| Renderer lint/typecheck | `npm run lint` | PASS |
| Composition enumeration | `npx remotion compositions` | PASS; M07-CH01 through M07-CH11 present |
| CH01 opening preflight | `qa/preflight/CH01_opening_preflight.png` at scale 0.25 | PASS; campus establishing view visible |
| Full-frame throughput benchmark | 60 frames at 1920x1080, local concurrency 8 | PASS technically; 35.4 sec for 60 frames, not viable for complete 41,790-frame batch |
| CH01_CAMPUS gate | `output/complete-tour-r01/qa/CH01_CAMPUS_QA.md` | PASS; 50 sec, 1500 frames, 1920x1080, H.264/yuv420p, checkpoint contact sheet reviewed |
| CH02–CH11 chapter renders | `output/complete-tour-r01/chapters/CH02.mp4` through `CH11.mp4` | PASS technical probes; all expected durations/frame counts, 1920x1080, 30 fps, yuv420p |
| CH02–CH11 visual gates | Per-chapter QA reports and contact sheets under `output/complete-tour-r01/qa/` | PASS; five checkpoints reviewed for each chapter |
| Solar evidence gate | `output/complete-tour-r01/qa/solar/SOLAR_CONTACT.jpg` | PASS; three modeled locations reviewed |
| Final master assembly | `output/complete-tour-r01/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R01.mp4` | PASS; 1393 sec, 41790 frames, 1920x1080, 30 fps, yuv420p, silent stereo AAC |
| Final master visual QA | `output/complete-tour-r01/FINAL_MASTER_QA.md` | PASS; five final-master checkpoints reviewed |
| Coverage audit | `output/complete-tour-r01/FINAL_COVERAGE_AUDIT.md` | PASS; 66/66 REQUIRED rows mapped to rendered shot IDs |
| Final master SHA-256 | `AE15C7BC61DE5E676607E40A7FA7D2A9ABD4B2CC7DE28F95D3977C91E9D0CB16` | PASS |

## Final result

M07 COMPLETE. Source, manifests, QA evidence, status, and this log were pushed to `origin/main` at commit `39366aa`. The large MP4 and intermediate media remain local-only by design. Final master path: `output/complete-tour-r01/POVU_KENYA_COMPLETE_CAMPUS_FACTORY_TOUR_R01.mp4`.

## Render method

The production renderer retains the same 1920x1080 camera/material/GLB path but uses a deterministic 2 fps sampling composition (`M07-S2-CH01` through `M07-S2-CH11`) and local FFmpeg motion interpolation to produce the required 30 fps chapter deliverables. This keeps the complete local run bounded while preserving shot timing and the authoritative camera interpolation function.

## Chapter gates

Chapter-by-chapter render, checkpoint visual QA, technical validation, and QA report entries are appended here as each gate completes. Final assembly is not permitted before all eleven gates are PASS.

## Current state

CH01 full render is the next active operation. No final master has been assembled.
