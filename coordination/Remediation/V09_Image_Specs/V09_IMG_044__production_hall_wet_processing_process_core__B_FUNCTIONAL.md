# V09 IMAGE-SPEC 044 — Production Hall / Wet Processing / Process Core — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/production_hall_wet_processing_process_core_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/production_hall_wet_processing_process_core_B_FUNCTIONAL.png`

## What is wrong
Again dominated by tank shells; functional piping/pump architecture is not visible.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_PRODUCTION_HALL_WET_PROCESSING_PROCESS_CORE` in place. Do not layer another generic proxy system.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Keep process tanks but add top agitator motors/gearboxes, access platform, stairs, handrails and vessel nozzles.
2. Build a manifold/pump corridor with visible pump bodies, valves, elbows and branch lines connected to tank outlets/inlets.
3. Add dedicated CIP skid/tank with supply/return headers and separate cleaning circuit.
4. Show transfer direction toward downstream filling via connected piping/conveyor relationship.
5. Frame across multiple tanks plus manifold/platform; no single tank shell may dominate.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without near-plane clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct the exact observed failure; validate camera/target line of sight using bounds before rendering.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
