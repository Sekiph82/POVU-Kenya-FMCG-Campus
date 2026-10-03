# REV005 F08-R04 — Process-State Geometry Remediation — Locked GPT Criteria

## Purpose

R04 is a narrow process-state visual-legibility remediation.

R03 proved that:
- hopper/feed can now be shown;
- oven/transfer/cell/outfeed can be shown;
- but preform → stretch/blow → formed bottle is still not readable at 900×600.

R04 must fix that transformation without moving the major process centers.

## Locked source

Start from the exact R02 staged model:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`

Required SHA-256:

`0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`

## Major anchors locked

Do not move:
- hopper center ≈(36.5,10)
- oven center = (47.5,10,3.1)
- blow-cell center = (57,10,3.3)
- outfeed center ≈(65,10,1.7)
- room envelope X 33…71 / Y -2…22
- south operator aisle
- north service aisle

Major center movement tolerance:
- <=0.05 m

## Allowed geometry scope

Only new F08 accepted process-detail geometry may change:
- hopper throat / product visibility
- elevator/feed product cues
- transfer/starwheel
- mould station internals
- clamp/tie-bar details
- stretch/blow rods/nozzles
- in-process preform
- formed/released bottle
- discharge handoff
- first outfeed bottles
- local line-side lighting/material contrast
- optional realistic first-off sample progression rack

No neighbor mutation.
No room-shell redesign.
No additional quarantine.

## Required two-state blow-cell storytelling

The two stations must read as different process states.

### Station 1 — load/stretch state

Required:
- mould halves visibly separated enough that the internal state can be seen;
- one heated preform visibly suspended/aligned at mould center;
- neck finish visible;
- stretch/blow rod visibly aligned above/through the preform axis;
- nozzle/head visibly connected;
- clamp/tie-bar relationship readable.

The preform must remain physically plausible:
- narrow cylindrical body
- clearly smaller body diameter than final bottle
- height approx 0.18–0.28 m before visible elongation cue
- optional elongated in-process body up to approx 0.30–0.34 m inside the station

### Station 2 — blow/eject state

Required:
- mould halves visibly separated/open enough to reveal the product state;
- one formed bottle visible between/opening out of the mould;
- bottle silhouette consistent with outfeed bottle geometry;
- discharge guide/starwheel/air-conveyor handoff visibly continues to the outfeed.

The station must not read as another identical closed block.

## Mould/platen treatment

The current large grey block reading must be reduced.

Allowed:
- preserve platen bounding dimensions while adding central relief/window/recess;
- make mould halves distinct from platens by material and shape;
- add bottle-shaped cavity relief on inner mould faces;
- add four tie bars / guides per station if useful;
- strengthen clamp-cylinder/actuator geometry;
- preserve the guarded-cell envelope.

Do not delete the safety guard.

## Transfer and discharge continuity

Transfer from oven to Station 1:
- keep starwheel/guide
- at least 3 readable preform states
- no floating rods

Station 2 to outfeed:
- add explicit discharge guide/neck rail/short transfer segment
- first two formed bottles must begin close to cell exit
- preserve total formed bottles >=16
- bottle dimensions remain within locked range:
  - height 0.28–0.38 m
  - width 0.08–0.12 m

## Product materials

Preforms and formed bottles must differ by silhouette first.

Material/tint may support readability but may not be the only distinction.

Use physically plausible translucent PET.

Avoid neon/color-coded teaching props.

## Optional first-off sample rack

A realistic line-side quality/first-off sample rack may be added near the HMI/operator side.

If used:
- no text labels
- exactly 3 physical samples:
  1. cold preform
  2. elongated/heated preform
  3. formed bottle
- rack is supplementary only
- in-machine states must still be readable.

## Camera-validity correction

Do not invalidate a camera solely because it lies within the broad AABB of `Production_Hall` or `PRODUCTION_ROOF`.

AABB may be a prefilter only.

Final camera-inside-solid validation must use actual geometry/shell logic:
- point-in-solid;
- signed distance / nearest-surface;
- ray parity;
- or an equivalent deterministic test.

Record the method.

## Camera evidence

After geometry remediation:
- A minimum 12 candidates
- B minimum 12
- C minimum 12
- D minimum 12

Do not run another 100+ random sweep.

Use the strongest proven R03/R02 families and the corrected camera validator.

C may use camera Z above 6.0 m where needed, provided the actual camera point is not inside solid geometry.

## Visual gates

A:
- hopper/feed + oven + blow cell + outfeed + room context

B:
- heater outlet + transfer + readable Station 1 + Station 2 + outfeed

C:
- clearly visible preform state
- stretch/blow rod/nozzle
- mould/cavity relationship
- clearly visible formed bottle state
- discharge handoff

D:
- complete line + HMI/operator side + aisle/context

Across the four views, an independent viewer must infer without labels:

`bulk preforms → feed → infrared heating → transfer → mould/stretch/blow → formed bottles → outfeed`

## Technical gates

Require:
- zero F01-F07 unauthorized differences
- exact 391 legacy retirement preserved
- 5 NOT_F08 preserved
- zero cross-facility collisions
- all major anchors within tolerance
- final accepted F08 meshes <=460
- deterministic GLB membership parity exact

## Promotion

Canonical Blend/GLB promotion only after:
- A/B/C/D PASS
- technical gates PASS
- deterministic GLB parity PASS

Otherwise publish R04 blocked evidence and stop.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R04`
