# REV005 F04 — INTEGRATED CAMERA ROOT-CAUSE CORRECTION

## State

First F04 execution stopped correctly at:

`BLOCKED_F04_INTEGRATED_COLLISION`

No canonical Blend/GLB mutation was saved.

Historical replay/source gates had already passed:
- 59 objects
- 10 BASE + 49 V01
- dimensional contract PASS
- archived A/B pixel parity PASS

## Root cause

The original F04 integrated-camera criterion assumed an exterior ring around the facility.

That assumption is invalid for F04.

Source audit proves F04 is physically contained inside the historical Wellness Pavilion.

### Historical Wellness Pavilion

Object:
`WELLNESS_PAVILION`

Bounds:
- X: **19.0 → 41.0 m**
- Y: **-79.0 → -61.0 m**
- Z: **1.2 → 7.2 m**

Size:
**22 × 18 × 6 m**

Center:
**(30,-70,4.2)**

Historical front glass:
`WELLNESS_GLASS`

Bounds:
- X: 20 → 40
- Y: -79.2 → -79.0
- Z: 1.45 → 6.95

### F04 accepted welfare geometry

Historical/V01 welfare geometry occupies approximately:
- X: about **21.5 → 40.5 m**
- Y: about **-77.6 → -63.9 m**
- Z: about **1.3 → 4.5 m**

Therefore the changing/shower/locker support facility is intentionally **inside** the source Wellness Pavilion.

An exterior 8-azimuth camera ring necessarily intersects the pavilion shell before reaching F04. A 0/9 result for every exterior candidate does not prove a bad facility or bad pavilion. It proves the camera model was wrong for an enclosed interior facility.

## Important non-finding

Do NOT classify these as invalid overlaps solely because they coexist spatially:
- historical Wellness Pavilion
- V09 Wellness / Recreation layer
- F04 welfare support geometry

Do NOT quarantine Wellness, Training, Restaurant or any neighboring facility based only on the failed exterior camera preflight.

The F04 retry must change only the **integrated evidence camera strategy**, not neighboring canonical geometry.

## Correct integrated evidence method

Use an **interior pavilion camera search**.

The camera:
- must be inside the historical pavilion volume;
- must not be inside any actual mesh object;
- must have direct visual access to the accepted F04 objects;
- must show enough room context to demonstrate that F04 is an interior support zone.

The exterior A/B historical parity images remain the primary model identity proof.

Integrated D is contextual evidence, not a requirement to see through solid building walls.
