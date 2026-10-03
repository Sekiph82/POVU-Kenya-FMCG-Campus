# REV005 F08-R03 — External South-Frontage Evidence — Locked GPT Criteria

## Purpose

R03 is the final camera-only attempt for F08.

It uses the exact R02 staged model and exhausts the previously untested true external south-frontage camera family.

## Locked staged source

Use:

`output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend`

Required staged SHA-256:

`0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`

If the file is absent, rebuild it deterministically using the published R02 helper and verify the same staged technical facts.

## No mutation

Forbidden:
- geometry change
- material change
- transform change
- collection/link change
- visibility change
- additional retirement/quarantine
- room-shell change
- helper-geometry additions

This task changes only camera/evidence objects in the staged working file or ephemeral render state.

## Camera authority

Use true external south-frontage positions:

- Y = -5 … -16 m
- X = 38 … 66 m
- Z = 3.5 … 8.0 m

The camera may remain outside the room envelope and look through the existing south glazing.

Allowed lens:
- 14 / 16 / 18 / 20 / 22 / 24 / 28 / 32 mm

Sensor:
- 36 mm

No near-plane clipping through facade geometry.

No temporary hiding of glazing/walls.

## A_CONTEXT

Goal: complete side-on process identity.

Must show:
- distinct hopper at west end;
- elevator/feed path;
- oven;
- transfer;
- blow cell;
- formed-bottle outfeed;
- room/floor context;
- west→east sequence.

Preferred family:
- camera X 48…56
- Y -8…-16
- Z 5…8
- target X 51…55
- Y 9…11
- Z 2.5…3.5
- lens 14…22 mm

## B_FUNCTIONAL

Must show:
- oven outlet;
- transfer;
- blow cell;
- readable mould/clamp station;
- stretch/blow cue;
- formed-bottle outfeed;
- process direction.

Preferred family:
- camera X 52…60
- Y -5…-12
- Z 4…7
- target X 55…60
- Y 9…11
- Z 2.4…3.5
- lens 18…28 mm

## C_SEQUENCE_DETAIL

Must show:
- oven/transfer adjacency;
- mould/clamp/stretch-blow action;
- one in-process/preform state;
- one formed/released bottle state;
- immediate outfeed relationship.

Preferred family:
- camera X 54…60
- Y -4…-9
- Z 3.5…6
- target X 56…60
- Y 9…11
- Z 2.2…3.4
- lens 20…32 mm

## D_INTEGRATED

Must show:
- hopper/feed;
- oven;
- blow cell;
- outfeed;
- HMI/operator side;
- south operator aisle;
- legitimate room context.

Preferred family:
- camera X 46…58
- Y -8…-15
- Z 6…8
- target X 52…57
- Y 9…11
- Z 2.8…3.5
- lens 14…22 mm

## Candidate minimum

Render at least:
- A: 18
- B: 18
- C: 18
- D: 18

Total minimum:
- 72

Do not repeat nearly identical candidates merely to satisfy count.

## Evidence

For every candidate record:
- ID
- role
- camera
- target
- lens
- camera-inside-geometry result
- glazing/wall clipping result
- hopper visible
- elevator/feed visible
- oven visible
- transfer visible
- mould station readable
- stretch/blow readable
- preform-state readable
- formed-bottle state readable
- outfeed visible
- HMI/operator relationship visible
- aisle/context visible
- complete label-blind sequence PASS/FAIL
- preview path

Retain top 8 per role and create contact sheets.

## Promotion

Canonical promotion is allowed only if:
- A PASS
- B PASS
- C PASS
- D PASS
- technical R02 facts remain unchanged
- protection remains PASS
- collision remains zero
- deterministic GLB membership parity passes

If any role fails:
- publish R03 evidence;
- do not promote;
- stop at `BLOCKED_F08_R03_EXTERNAL_FRONTAGE_VISUAL_FAILURE`.

No further camera-only F08 task is allowed after that stop.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08_R03`
