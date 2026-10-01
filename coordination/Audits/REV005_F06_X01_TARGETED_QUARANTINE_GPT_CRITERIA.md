# REV005 F06-X01 — Targeted Cross-Facility Quarantine — Locked GPT Audit Criteria

## Baseline

Starting canonical state must match:

Blend:
`BA2CFFBA98C317EBE8E96E0DAC40263FCACF1C4485D544FA467C38EFD2853655`

GLB:
`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

## Authorized object set

Exactly these seven V09 structural objects may receive saved quarantine visibility changes:

1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

No other object is authorized.

## Ownership gate

Before mutation, each named object must prove:

- facility metadata belongs to Toothpaste Production or Wet Wipes Production as appropriate;
- it is part of the V09 remediation structural envelope;
- transform and dimensions match the committed V09 builder;
- it is not an accepted F01-F06 object.

Any contradiction is a hard stop.

## Allowed mutation

Only:
- hide_viewport = true
- hide_render = true
- F06-X01 quarantine custom properties

No delete.
No unlink.
No transform.
No dimension change.
No mesh/material change.
No collection-wide quarantine.

## Protection gate

Require exact protection of:

- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted primary 54
- F06 accepted historical 43
- V09 Glass Deck quarantine 117
- V09 Training quarantine 81
- V09 Restaurant right-wall accepted quarantine
- historical Glass Deck source
- historical Wellness/pavilion state

The only authorized before→after differences are the seven saved visibility/quarantine-property changes above.

## Explicit non-target protection

Must remain unchanged and visible according to their current saved state:

- `V09_WET_PROCESS_BACK_WALL`
- `V09_WET_PROCESS_SOFFIT`
- all other Wet Processing objects
- all other Toothpaste objects
- all other Wet Wipes objects
- `V02_WEIGH_BOOTH_SIDE`
- `REV005_WEIGH_DISPENSE_ROOM_OPERATOR_STATION_BODY`
- every accepted 43-object F06 historical object

## F06 historical regression gate

Re-confirm:
- destination count = 43
- BASE/V01/V02/V05 split unchanged
- historical A/B/C source parity remains locked
- destination A/B/C parity remains locked
- no F06 transform/material/parent/data changes

Do not rerender historical parity unless needed to prove a suspected contradiction.

## Integrated-camera gate

After the seven-object canonical quarantine, search current-context camera positions again.

Minimum:
- 20 900×600 candidates
- lenses among 35/40/45/52 mm
- multiple front-left/front-oblique/side and target variants
- camera outside geometry
- no QA-only hiding
- no further quarantine

The final selected frame must visibly communicate in one current-context view:

- weigh booth/enclosure
- substantially complete hopper row
- hopper valves
- dosing chutes/path
- precision balance stations
- balance table
- transfer tote/cart
- operator/service zone
- access organization
- coherent hopper→dosing→balance→transfer workflow

LOS requirement:
- >=7/9 clear rays

Visual completeness remains mandatory even at 9/9.

## Final evidence

Required:
- quarantine before manifest
- quarantine after manifest
- exact authorized diff
- candidate manifest
- selected D integrated render 1440×960
- selected D preview 900×600
- camera validation
- final Blend/GLB hashes
- regression JSON
- Codex log

## Scope

No F07.
No additional neighbor quarantine.
No F06 redesign.
No TASKS.md edit by Codex.
No locked-criteria edit by Codex.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F06_X01`
