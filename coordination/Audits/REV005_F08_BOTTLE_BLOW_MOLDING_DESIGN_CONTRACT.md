# REV005 F08 — Bottle Blow Molding — Locked Class N Design Contract

## Facility classification

F08 is a Class N detailed-completion facility.

Process identity is the preform-based blow-molding sequence already established in the project evidence:

`preform hopper/feed → heater/oven → mould/blow cell → formed-bottle outfeed`

The rejected V09 representation is evidence of the required process identity and of prior visual failures. It is not the accepted geometry specification.

## Canonical coordinate frame

Facility center:

`(52.0, 10.0)`

Locked plan envelope:

- X = 33.0 to 71.0 m
- Y = -2.0 to 22.0 m
- width = 38.0 m
- depth = 24.0 m

Floor:
- center = (52.0,10.0,1.00)
- dimensions = 38.0 × 24.0 × 0.18 m
- finished top ≈ Z 1.09 m

Wall/room shell:
- wall bottom = Z 1.09 m
- wall top = Z 7.50 m
- nominal clear internal height ≈ 6.40 m
- ceiling/soffit underside ≈ Z 7.25 m

Primary operator/process aisle:
- south side of line, centered approximately Y=4.0
- clear width >=2.0 m

North service aisle:
- centered approximately Y=16.0
- clear width >=1.5 m

Keep a minimum 1.2 m local maintenance clearance around guarded machinery access points.

## Main process axis

The main product path runs west→east near Y=10.0.

Required process order:

1. preform bulk hopper / loader
2. preform elevator / feed
3. preform neck-support rail / unscrambler feed
4. infrared heater oven
5. oven-to-blow transfer
6. guarded two-station mould / blow cell
7. bottle discharge / outfeed
8. formed-bottle inspection / discharge handoff

The sequence must be readable from geometry alone.

## P1 — Preform hopper / loader

Primary frame:
- center ≈ (36.5,10.0,3.10)
- footprint ≈ 3.0 × 3.0 m
- overall height ≈ 4.6 m

Bulk bin:
- upper body ≈ 2.4 × 2.4 × 1.8 m
- center Z ≈ 4.30 m

Funnel/cone:
- transition below bulk bin
- visible taper to feed throat
- throat elevation ≈ Z 2.6–2.9 m

Required:
- support legs/frame
- access panel or service side
- visible preform load zone
- at least 16 repeated preform pieces visible between hopper/feed and oven entry across the complete sequence evidence.

## P2 — Preform elevator / feed

Inclined or stepped feeder:
- start near (38.0,10.0,2.4)
- discharge near (41.0,10.0,4.0)
- approximate path length 4.0 m
- usable belt/rail width 0.7–0.9 m

Must visibly connect hopper throat to the neck-support/feed rail.

Do not represent the connection as a floating pipe.

## P3 — Preform feed rail / unscrambler path

Feed rail:
- centerline approximately X=40.5…44.0
- Y≈10.0
- Z≈3.7 m
- effective length >=3.5 m

Required:
- paired rails or neck-support channel
- guide frame
- repeated preforms
- clear continuation into oven inlet.

## P4 — Heater oven

Oven center:

`(47.5,10.0,3.10)`

Outer frame:
- length X = 7.0 m
- depth Y = 4.0 m
- height = 4.2 m

Nominal bounds:
- X≈44.0…51.0
- Y≈8.0…12.0

Required structural cues:
- four vertical corner posts minimum
- upper/lower longitudinal frame rails
- guarded/service-panel segments that do not visually seal the process path
- visible inlet and outlet openings

Heater banks:
- two opposing banks, one each side of product path
- bank Y centers ≈8.7 and 11.3
- at least 8 distinct heater elements per side
- heater element active length ≈2.2 m
- vertical/angled elements acceptable if the repeated bank identity remains obvious

Product path:
- neck-support chain/rail visible through oven
- repeated preforms visible at inlet, within at least part of heater zone, and outlet

Do not build a monolithic opaque box.

## P5 — Oven-to-blow transfer

Transfer region:
- X≈51.0…53.0
- Y≈10.0
- Z≈2.7–3.3

Required:
- curved guide / starwheel / neck-transfer cue
- physical connection from heater exit to blow-cell infeed
- guarding where appropriate without hiding the transfer.

## P6 — Guarded mould / blow cell

Cell center:

`(57.0,10.0,3.30)`

Overall guarded envelope:
- X length ≈8.0 m
- Y depth ≈5.6 m
- height ≈5.2 m

Nominal bounds:
- X≈53.0…61.0
- Y≈7.2…12.8

Required:
- structural base frame
- vertical guard posts
- transparent/open guard panels
- two service doors minimum
- HMI/control interface outside guarded envelope on south/operator side

### Two mould stations

Station centers:
- approximately X=55.7 and X=58.3
- Y≈10.0

Each station requires:
- opposing clamp/platen pair
- visible mould cavity block between platens
- vertical stretch-rod / blow-nozzle cue
- lower base/guide
- sufficient gap/relief that the mould station reads as machinery, not a colored cube.

Platen nominal:
- ≈0.30 × 1.4 × 2.4 m each

Mould block nominal:
- ≈0.55 × 1.1 × 1.8 m

Stretch/blow rod:
- diameter cue ≈0.10–0.16 m
- vertical working length ≈1.5–2.0 m

## P7 — High-pressure air / utility cues

High-pressure air manifold:
- run along north side of blow cell
- approximately X=54…60
- Y≈13.3
- Z≈4.6
- visible main diameter cue ≈0.14 m

Provide:
- at least four distinct drops/branches into the mould/blow zone
- visible valve/manifold block cues

Cooling-water supply/return:
- two parallel service lines
- north/service side
- visible diameter cue ≈0.10–0.12 m
- connect into blow-cell/mould region
- visibly distinct routing from air manifold by geometry and location, not color alone.

No full compressor room is required inside F08; only local line-side utility connections.

## P8 — Bottle outfeed

Outfeed conveyor:
- center ≈(65.0,10.0,1.70)
- effective length ≈9.0 m
- width ≈1.2 m
- working surface ≈Z 1.8–2.0 m

Nominal X coverage:
- ≈60.5…69.5

Required:
- conveyor frame/legs
- two side guides
- at least 16 repeated formed bottles
- bottles spaced sufficiently to read as product flow
- formed bottles must be visibly different from preforms.

Bottle shape:
- bottle body + neck + finish
- height ≈0.28–0.38 m
- body width ≈0.08–0.12 m

## P9 — Outfeed inspection / discharge

Inspection bridge:
- approximately X=68.0
- Y=10.0
- vertical sensor/frame over conveyor

Required:
- two side sensor heads or one clear optical inspection pair
- reject/quality sample tote adjacent to outfeed
- handoff direction remains visually obvious.

Do not add a filling/capping machine. F08 ends at bottle production/outfeed.

## Operator / HMI / safety

HMI station:
- south side of blow cell
- center approximately (57.0,5.6,2.0)
- body ≈1.0 × 0.6 × 1.4 m
- angled/vertical screen plane
- E-stop / control cluster geometry

Operator standing/service zone:
- clear area between Y≈3.0…6.5 around HMI and service doors
- preserve >=2.0 m primary aisle.

Safety:
- eyewash near (68.5,4.0)
- PPE station near (66.8,4.0)
- fire/extinguisher or first-response cabinet near (65.2,4.0)

Required:
- distinct geometry
- not text-only evidence.

## Preform staging

Two preform staging bins/pallet boxes:
- west/north side
- around X=35.0…38.0
- Y≈16.5
- each footprint ≈1.5 × 1.2 m

These must not block the north service aisle.

## Architectural completion

Required:
- finished floor
- back/north wall
- east and west enclosure cues
- south/front glazing or open framed wall sections that preserve viewability
- two service/egress openings
- ceiling/soffit cues
- minimum 10 ceiling light fixtures
- no black void
- no fake wall hiding used only for cameras.

Main service door:
- east side near X≈70.9
- clear opening ≈2.0 × 2.6 m

Material language:
- floor: neutral industrial gray
- machine frames: stainless/neutral dark frame
- guards: transparent/light-tint + dark posts
- oven heater elements: distinct metallic/emissive cue
- air/cooling service lines: restrained functional differentiation
- avoid large saturated monolithic housings.

## Label-blind acceptance

Without text labels, F08 must unmistakably read as:

`preforms → heating → mould/blow forming → finished bottle discharge`

The complete sequence must be inferable from geometry, repeated product states, and physical connections.

## Locked camera seeds

All cameras must be outside geometry.

### A_CONTEXT
- camera (35.0,-0.5,6.0)
- target (52.0,10.0,3.0)
- lens 24 mm
- sensor 36 mm

Must show:
- hopper/feed
- oven
- blow cell
- outfeed
- room enclosure/floor

### B_FUNCTIONAL
- camera (42.0,3.5,4.8)
- target (56.0,10.0,3.0)
- lens 32 mm
- sensor 36 mm

Must show:
- heater outlet
- transfer
- mould/blow cell
- outfeed
- enough hopper/feed context to establish sequence.

### C_SEQUENCE_DETAIL
- camera (48.0,5.0,4.0)
- target (56.5,10.0,3.0)
- lens 38 mm
- sensor 36 mm

Must show at least two adjacent functional steps plus physical connection:
- heater/transfer
- mould/clamp/blow zone
- bottle discharge.

### D_INTEGRATED
- camera (34.5,19.5,6.5)
- target (54.0,10.0,3.0)
- lens 24 mm
- sensor 36 mm

Must show:
- whole west→east process sequence
- operator/service relationship
- legitimate enclosure/context
- no dominant wall/panel obstruction.

Final full renders:
- 1440×960

Audit previews:
- 900×600

Small camera refinement is permitted if necessary:
- camera <=3.0 m per axis
- target <=2.0 m per axis
- lens 20–40 mm
- exact final values must be recorded.

## Visual acceptance

A_CONTEXT:
- complete preform-to-bottle sequence readable
- room/floor/enclosure visible
- no machine shell occupies >30% of frame

B_FUNCTIONAL:
- heater + transfer + blow cell + outfeed connected
- at least one mould station readable
- guard does not obscure process identity

C_SEQUENCE_DETAIL:
- heater/transfer/mould relationship readable
- clamp/mould/stretch-blow cues visible
- formed-bottle discharge visible
- never a panel-only close-up

D_INTEGRATED:
- hopper/feed + oven + cell + outfeed visible
- operator/HMI/service side readable
- main aisles understandable
- no black void
- no label dependence.
