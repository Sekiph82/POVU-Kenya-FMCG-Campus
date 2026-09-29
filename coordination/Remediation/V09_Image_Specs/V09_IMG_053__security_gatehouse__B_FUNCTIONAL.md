# V09 IMAGE-SPEC 053 — Security Gatehouse — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/security_gatehouse_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/security_gatehouse_B_FUNCTIONAL.png`

## What is wrong
Barrier/wall view with booth interior missing; camera looks into black void.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_SECURITY_GATEHOUSE` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Build enclosed booth with walls/roof cue, transparent windows, door/service access and operator desk.
2. Place CCTV monitors and barrier controls on desk/console.
3. Show vehicle lane with barrier arm/post, road markings/curb and booth beside the lane.
4. Context camera must frame booth + lane + barrier together; functional view must see into booth controls while retaining lane relationship.
5. Remove giant blank wall planes between camera and target.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
