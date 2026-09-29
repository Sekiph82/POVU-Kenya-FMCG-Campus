# V09 IMAGE-SPEC 008 — Caps and Trigger Assembly — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/caps_and_trigger_assembly_B_FUNCTIONAL.png`

## What is wrong
The PNG is mathematically 100% black; the previously accepted assembly is absent.

## Blender ownership / safety
This is a preserved V07 PASS group. Diagnose visibility/camera/lighting regression first; do not redesign by default.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
Do not edit REV004, create REV006, globally unhide V08-retired proxies, or create another Desktop project copy.

## Required model corrections
1. Do not remodel the prior accepted assembly unless a true geometry regression is proven.
2. Compare V07/current collection visibility, `hide_render`, `hide_viewport` and view-layer exclusion.
3. Reverse only preserved-facility hide flags accidentally caused by V08 retirement; never globally unhide retired proxies.
4. Verify camera is outside geometry, near clip is not slicing and QA world/fill light is active.
5. After restoration retain the accepted assembly layout and only adjust camera/light as needed.

## Camera correction for this image
1. Use a medium 3/4 functional camera focused on the primary room/equipment function with visible depth.
2. Target should occupy roughly 70–90% of frame without near-plane clipping or wall/tank obstruction.
3. Show at least three meaningful subcomponents or one complete human-scale room function.
4. Correct the exact failure described above. Use collection/object bounds to ensure camera origin is outside geometry and line-of-sight is not immediately blocked.
5. Use sensible near/far clipping; do not slice the target.

## Lighting/material proof
- Restore/add neutral QA fill so silhouettes do not disappear into black.
- Keep material separation between floor/envelope/equipment and use bevels/normal smoothing on major hard-surface edges.
- Do not use color alone as machine identity.

## Acceptance
PASS only if the PNG is non-black, label-blind readable, fulfills the B_FUNCTIONAL role, is not camera-occluded, visibly fixes the stated failure, and reintroduces no unrelated legacy proxy.
