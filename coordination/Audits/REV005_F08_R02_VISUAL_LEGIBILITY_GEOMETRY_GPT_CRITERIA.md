# REV005 F08-R02 — Visual-Legibility Geometry Remediation — Locked GPT Criteria

## Purpose

R02 is the first F08 task authorized to change new staged F08 geometry.

The goal is not a redesign. The goal is to make the already-correct process sequence visibly self-explanatory.

## Canonical baseline remains locked until promotion

Blend:
`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

GLB:
`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

Do not change either canonical file until all staged R02 gates pass.

## Starting staged reference

Start from the deterministic R01 helper-reconstructed stage.

Required initial technical reference:
- F08 accepted meshes = 338 before R02 edits
- confirmed F08 legacy = 391
- ambiguous legacy = 0
- NOT_F08 preserved = 5
- protection unauthorized differences = 0
- cross-facility collisions = 0
- outside-envelope objects = 0
- preforms = 20
- heater elements = 16
- service doors = 2
- HP-air branches = 4
- formed bottles = 16
- candidate GLB membership = 10,888 expected / actual

The helper-reconstructed east service opening is authoritative:
- jamb Y = 9.0 / 11.0
- north east-wall segment = 11.0 m
- south east-wall segment = 11.0 m

## Major anchors may not move

Locked:
- room envelope X 33…71, Y -2…22
- hopper center ≈(36.5,10)
- oven center (47.5,10,3.1), envelope 7×4×4.2
- blow cell center (57,10,3.3), envelope 8×5.6×5.2
- outfeed center ≈(65,10,1.7), envelope ≈9×1.2
- south operator aisle >=2.0 m
- north service aisle >=1.5 m

Major equipment-center movement >0.05 m is forbidden.

## Authorized geometry families

Only these new F08 accepted geometry families may change or receive added detail:

1. hopper / bulk-bin / funnel;
2. feeder/elevator;
3. neck-support preform rail;
4. heater oven;
5. oven-to-cell transfer;
6. guarded blow cell internals;
7. product-state cues inside/around blow cell;
8. formed-bottle outfeed;
9. inspection/discharge cue;
10. HMI/operator visual linkage;
11. local F08-only process lighting/material contrast.

Room shell may not be redesigned.

## Hopper visual gate

The upstream source must unmistakably read as a hopper/feed system.

Required:
- strong tapered or open-top bulk-hopper silhouette inside the locked 2.4×2.4×1.8 m upper-bin envelope;
- visibly supported frame;
- visible funnel/throat;
- obvious physical transition into the elevator;
- no generic rectangular bin-only reading.

The hopper must be visible in at least one valid A or D camera.

## Feeder / preform-flow gate

The elevator must visibly carry preforms.

Required:
- inclined mechanical path remains physically connected;
- add repeated cross flights / paddles / carrier features;
- show at least 6 clearly visible preforms on the elevator path;
- show at least 6 preforms on the downstream neck-support/feed rail;
- show at least 8 preforms in or immediately at the oven path.

Total visible preform count may increase beyond 20.

## Heater-oven visual gate

The heater must read as an open-frame infrared oven, not a forest of large orange bars.

Required:
- preserve two banks;
- preserve >=8 heater elements per bank;
- reduce heater-element cross-section enough to read as repeated lamps/elements rather than structural columns;
- preserve active vertical length ≈2.2 m;
- add reflector/backplate or bank-frame cues if needed;
- preserve inlet/outlet openings;
- preserve visible product rail through the oven;
- no opaque monolithic shell.

Heater elements may not dominate >35% of a valid A/B frame.

## Transfer gate

The oven-to-cell transfer must be unmistakable.

Required:
- visible starwheel/curved guide/neck transfer;
- at least 3 visible preform/product-state cues around the transfer;
- physical continuity from oven rail to blow-cell infeed;
- no floating disconnected rods.

The transfer must be readable in B and C.

## Blow-cell visual gate

The guarded cell must visually explain clamp/mould/stretch-blow action.

Required for both stations:
- opposing platens remain;
- mould halves remain;
- tie-bar/guide structure remains;
- stretch/blow rod is visually strong enough to read;
- nozzle cue remains.

Add product-state evidence:
- station 1: visible preform/in-process elongated preform cue;
- station 2: visible formed-bottle/in-mould cue or immediate discharge cue.

Allowed:
- add clamp-cylinder/actuator cues;
- add mould-cavity relief or bottle-shaped insert;
- adjust mould material/contrast;
- reduce visual dominance of generic block faces.

Not allowed:
- move station centers outside tolerance;
- exceed guarded-cell envelope.

## Formed-bottle outfeed gate

Keep >=16 formed bottles.

Each bottle must remain inside:
- height 0.28–0.38 m
- body width 0.08–0.12 m

R02 should use the upper half of the allowed size range where practical for readability.

Required:
- bottle body + shoulder/neck/finish silhouette;
- first formed bottle close enough to cell exit to visually link discharge;
- repeated bottle flow remains obvious;
- inspection bridge remains downstream.

## HMI / operator relationship

HMI must remain outside guards on south operator side.

Add only if needed:
- standing-pad / operator-zone floor cue;
- direct sightline cue to guard doors;
- local task light.

Do not add decorative people or unrelated props.

## Material / contrast gate

Process identity may not depend on labels.

Required:
- heater lamps distinct from structural frames;
- mould/clamp parts distinct from guards;
- preforms visually distinct from formed bottles;
- formed bottles remain readable at 900×600;
- transparent guarding must not erase internal mechanisms.

Avoid using saturated color alone as the process explanation.

## Mesh-count discipline

R02 may add detail meshes, but this is not permission for uncontrolled object growth.

Starting accepted count:
- 338 meshes

Final accepted F08 mesh count should normally remain:
- >=338
- <=460

If >460 is genuinely required, stop and explain why before promotion.

## Camera gate

After geometry remediation, use a new evidence search.

Do not reuse a failing R01 camera automatically.

Minimum:
- 24 A candidates
- 24 B candidates
- 24 C candidates
- 24 D candidates

Lens:
- 16–35 mm

Camera may use the R01 expanded authority.

Required selected-view contracts:

A:
- hopper/feed + oven + cell + outfeed + room context

B:
- heater outlet + transfer + cell + readable mould station + outfeed

C:
- transfer + readable mould/stretch-blow action + product-state transformation + discharge

D:
- complete line + HMI/operator relationship + aisle/context

The four views together must make the sequence self-explanatory.

## Protection / collision gate

Require:
- zero F01-F07 unauthorized differences;
- exact 391 F08 legacy retirement state preserved;
- 5 NOT_F08 candidates preserved;
- zero cross-facility collision;
- no new object outside F08 envelope except legitimate doorway/frontage hardware already allowed.

## GLB parity

R02 deterministic expected membership becomes:

pre-F08 canonical membership
- exact 391 retired F08 legacy baseline names
+ exact final R02 accepted F08 exportable object names.

Do not hard-code 10,888 after mesh additions.

Compute expected membership from names.

Require:
- zero missing expected names;
- zero unexpected names;
- all accepted F01-F07 names preserved;
- all final R02 F08 accepted names present;
- all 391 retired F08 names absent.

## Canonical promotion gate

Promote only after:
1. R02 visual set PASS;
2. dimensional gate PASS;
3. collision/protection PASS;
4. exact legacy-retirement preservation PASS;
5. deterministic GLB parity PASS.

Then:
- save exact staged state as canonical Blend;
- export canonical GLB deterministically;
- reopen canonical Blend;
- rerender final 1440×960 + 900×600 A/B/C/D;
- revalidate saved state.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R02`
