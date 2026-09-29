# V09 IMAGE-SPEC 056 — Security / Reception / Visitor Arrival — B_FUNCTIONAL

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/security_reception_visitor_arrival_B_FUNCTIONAL.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/security_reception_visitor_arrival_B_FUNCTIONAL.png`

## What is wrong
Mostly empty floor and low white blocks; desk/CCTV/screening/access control are unreadable.

## Blender ownership / safety
Edit/replace bad subassemblies in `REV005_V08_CLEAN_SECURITY_RECEPTION_VISITOR_ARRIVAL` in place; do not stack another generic proxy layer.
Canonical Blend: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d\revisions\REV005\POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`
No REV004 edits, REV006, global retired-object unhide or second Desktop copy.

## Required model corrections
1. Create entrance -> reception/security desk -> screening/access control -> visitor seating -> onward controlled circulation.
2. Build real desk with operator workstation/CCTV monitors, not only partition wall.
3. Add turnstile/gate geometry and compact screening point with visible pass-through direction.
4. Place visitor seating in waiting zone and retain glazing/wall/door cues with bright neutral lighting.
5. Use camera angles showing path across facility rather than edge-on partition slabs.

## Camera correction
1. Use medium 3/4 framing on the primary function with visible depth.
2. Keep target 70–90% of frame without clipping.
3. Show multiple meaningful subcomponents, not one flat surface.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for B_FUNCTIONAL, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
