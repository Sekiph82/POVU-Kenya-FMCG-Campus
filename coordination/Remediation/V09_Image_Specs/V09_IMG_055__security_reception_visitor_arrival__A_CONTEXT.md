# V09 IMAGE-SPEC 055 — Security / Reception / Visitor Arrival — A_CONTEXT

## Source evidence
- V08 image: `output/rev005-interior-remediation-v08/qa/security_reception_visitor_arrival_A_CONTEXT.png`
- Independent verdict: **NOT OK**
- Required V09 image: `output/rev005-interior-remediation-v09/qa/security_reception_visitor_arrival_A_CONTEXT.png`

## What is wrong
Tall blue partitions dominate; low blocks/chairs appear but no coherent visitor/security flow.

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
1. Use a 3/4 context camera outside all object bounds.
2. Fit complete zone at roughly 65–85% frame occupancy; foreground occluder <~15%.
3. Show floor and enclosure/edge cues; never aim into black void.
4. Correct this image's exact failure and verify camera/target line of sight from bounds.
5. Use neutral QA fill and sane clipping distances.

## Acceptance
PASS only if non-black, label-blind readable, correct for A_CONTEXT, not occluded, visibly fixes the stated failure and reintroduces no unrelated proxy.
