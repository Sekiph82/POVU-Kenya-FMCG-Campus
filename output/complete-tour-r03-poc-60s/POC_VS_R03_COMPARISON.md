# Approved POC vs M07 R03

## Approved `poc-r02`

- One persistent camera over the full 1,800-frame composition.
- Eleven meaningful global controls.
- Smoothstep interpolation for camera position and target.
- No hard cuts or chapter-local camera resets.
- Actual REV004.1 GLB source.

## Rejected M07 R02 root cause

R02 registered eleven separate `M07-CH01` through `M07-CH11` compositions. `CompleteTourChapter` used a local `useCurrentFrame()` clock and initialized a new `CameraRig` for each chapter. At each chapter boundary, the first shot began with `travel = 1`, so concatenation reset the camera to the next chapter's first pose. Per-shot target, offset, FOV, and anchor logic amplified the visible jump.

## R03 correction

R03 registers one `M07-R03-POC-60S` composition and one `R03World` camera over all frames. It retains the approved interpolation philosophy, uses constant FOV 52, and uses elevated transition controls to keep the camera outside roof volumes. The full-frame validator reports:

- persistent camera: true
- hard cuts: 0
- control points: 14
- maximum position delta: 2.5542 at frame 1171
- maximum angular delta: 0.6124 degrees at frame 1527
- maximum FOV delta: 0
- discontinuities: none
