# POVU M07 R02 Remediation Report A–H

## A. Authority and source

The attached M07 master remediation brief was treated as authoritative. Production used the frozen REV004.1 GLB with SHA-256 `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`.

## B. Camera choreography

R01 was rejected for static-feeling travel, target mismatch, and continuity defects. R02 replaces generic camera destinations with a target registry that resolves real GLB objects, uses target-relative offsets, and interpolates camera position and orientation over each shot. The first shot is a deliberate 15-second aerial establishment.

## C. Callout accuracy

Camera and label positions are derived from the same resolved target registry. Public-facing labels are limited to the requested facility language; internal/debug strings were removed from the render path.

## D. Campus and landscape fixes

Hands of Growth / living-wall alignment is driven by the real target object. The public realm, garden pods, employee garden, and arrival sequence remain tied to the frozen source geometry. The redundant exterior Glass Deck shot was removed.

## E. Facility coverage

Wellness / Recreation, Daycare / Occupational Health, R&D / QC, Training / Academy, Restaurant / Café, and the garden facilities have dedicated target-driven shots. The final QA records the daycare and west-stair shots as wider establishing views where the source geometry does not support a truthful close-up.

## F. Glass Deck and factory relation

East, west, and central Glass Deck stairs use real stair-step or access targets. The factory sequence then progresses through materials, processing, filling, packaging, dispatch, utilities, and HSE without adding fabricated industrial detail.

## G. Render and validation

All eleven chapters rendered locally from the Windows Remotion/Three.js project using deterministic 2 fps sampling followed by local FFmpeg interpolation. Final output was normalized to 41,160 frames at 30 fps, 1920x1080, H.264, yuvj420p, and 1,372 seconds. Lint and the Blender target audit passed.

## H. Acceptance position

The production and visual QA gates are complete for the M07 R02 tour. The final master is a local-only media deliverable; the repository publication contains the source pipeline, target plan, validation tooling, QA evidence, and production log. The large MP4 remains on the local Windows machine and is not claimed as a GitHub binary artifact.

