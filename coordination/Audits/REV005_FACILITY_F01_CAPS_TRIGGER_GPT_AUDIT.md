# REV005 FACILITY F01 — CAPS & TRIGGER — INDEPENDENT GPT AUDIT

## Final outcome

`PASS`

F01 Caps & Trigger Assembly is independently accepted.

## Accepted execution lineage

- historical replay/restoration commit: `6384c03c943f06eef43550e4eb57b6ffede0435d`
- cross-facility overlap quarantine/integrated-proof commit: `8cdd5e6032a5f235b3186fa0cff23554f35d2e90`

## Historical restoration

PASS.

- exact historical composition reconstructed: 7 base + 21 V01 + 47 V02 + 0 V03 + 0 V04 + 1 V05 anchor = 76
- selected/restored object count: 76
- transform/dimension/parent parity: exact
- facility-only A/B/C destination parity reproduces the accepted V05 visual source
- bowl/feed equipment, feed track, assembly fixtures/cell, multiple work positions and reject/outfeed relationship are readable

## Cross-facility regression finding and repair

The failed original D integrated view was not an F01 model defect.

Root cause was confirmed as a V09 Glass Deck placement regression:
- true historical Glass Deck is an elevated link at Z 8.2–12.2 m
- V09 incorrectly created a 40×24 m ground-level Glass Deck envelope centered at (70,24)
- measured overlap with F01: 202.5731 m² plan / 979.6435 m³ AABB volume

The invalid V09 replacement collection:
`REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`

was quarantined without moving/deleting its 117 objects. Historical source Glass Deck geometry remained protected.

## Integrated context proof

Direct visual inspection of:
`F01_D_INTEGRATED_CONTEXT_V03_PREVIEW_900x600.png`

PASS.

Observed:
- F01 is clearly visible in the current scene
- bowl/feed, carousel/assembly fixtures, pick/place equipment and outfeed/conveyor are visible
- surrounding current architecture/context is visible
- no destructive overlap hides the facility
- no camera-inside-wall failure
- no global legacy-unhide regression is visible

Camera evidence:
- location: `(13.470107,-7.779893,44.214287)`
- target: `(52.25,31.0,3.565600)`
- lens: 52 mm
- clear rays: 9/9
- F01 projected screen coverage: 46.0022%
- temporary exclusions: none

## Protection

PASS.

- F01 76-object protection parity: PASS
- historical source Glass Deck protection parity: PASS
- no Bottle Blow mutation
- no Wet Processing mutation
- no unrelated facility mutation reported
- REV004 unchanged
- no REV006
- no .hiveai
- no tour/video

## Canonical hashes after accepted repair

Blend:
`80C4FC83DBD260CB9D0A6B02F0582C5829273450437B90D7CD2B9281C17B744E`

GLB:
`9EA90C327C2502AA019AD9ADA656BE0BC0B652A19724BEF3162910058B63FD40`

## Residual finding

The V09 Glass Deck replacement collection remains quarantined and must be handled when Glass Deck becomes its own active facility. This does not invalidate F01.

## Final decision

`PASS`

F01 is closed and locked.

Facility 02 is now allowed to begin.

No future facility may modify F01 without an explicit independent regression finding.
