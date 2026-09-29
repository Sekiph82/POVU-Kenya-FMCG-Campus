# V09 IMAGE-SPEC 071 — Wet Wipes Production — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/wet_wipes_production_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/wet_wipes_production_B_FUNCTIONAL.png`

## What is wrong
Boxes and circular roll dominate; no continuous web path or seal/discharge relationship.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_WET_WIPES_PRODUCTION` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Build parent roll unwind -> continuous web rollers/path -> wetting -> folding/converting -> cut/stack -> pouch film/feed -> seal -> discharge.
2. Use large parent rolls with visible web strip physically passing over rollers.
3. Wetting stage needs spray/manifold/impregnation box connected to web; folding/cutting uses guides/rollers/cutter/stack.
4. Packaging stage needs film roll, pouch-form/seal jaws and finished packs on discharge conveyor.
5. Remove tall generic boxes that interrupt material continuity and camera sightline.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
