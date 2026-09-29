# V09 IMAGE-SPEC 054 — Security Gatehouse — C_SEQUENCE_OR_DETAIL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/security_gatehouse_C_SEQUENCE_OR_DETAIL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/security_gatehouse_C_SEQUENCE_OR_DETAIL.png`

## What is wrong
Blank wall/window rectangles without operator desk, controls or lane relationship.

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
1. Use oblique medium-close framing proving connection/sequence.
2. Show at least two adjacent functional steps plus connecting path.
3. No wall/panel close-up.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for C_SEQUENCE_OR_DETAIL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
