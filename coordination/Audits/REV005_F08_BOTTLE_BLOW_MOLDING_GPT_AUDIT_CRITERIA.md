# REV005 F08 — Bottle Blow Molding — Locked GPT Audit Criteria

## Baseline

Canonical pre-F08 Blend:

`B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`

Canonical pre-F08 GLB:

`B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`

## Design authority

F08 must conform to:

`coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md`

The old V09 bottle-blow representation is failed reference evidence only. It is not the accepted dimensional specification.

## Ownership / replacement gate

Before mutation, inventory:
- all objects whose facility metadata is exactly `Bottle blow molding`;
- all objects in `REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING`;
- current bottle-blow owner-inventory objects;
- every pre-F08 GLB node matching those exact confirmed objects.

Classify every candidate:
- `CONFIRMED_F08_LEGACY`
- `AMBIGUOUS_SHARED`
- `NOT_F08`

Only confirmed legacy F08 objects may be retired.

Any necessary retirement object with ambiguous ownership is a hard stop.

## Geometry / dimensional gate

Locked room:
- center (52,10)
- envelope 38×24 m
- X 33…71
- Y -2…22

Required process sequence:
1. preform hopper
2. feeder/elevator
3. neck-support/feed rail
4. heater oven
5. transfer
6. guarded two-station blow cell
7. bottle outfeed
8. inspection/discharge

All required anchor dimensions, locations, aisle widths, process utilities and product counts are defined in the design contract.

Tolerance:
- room/envelope and major machine centers/dimensions <=0.05 m
- secondary equipment and furniture <=0.10 m
- pipe/conveyor endpoints <=0.10 m
- aisle shortfall <=0.10 m

## Functional-detail gate

Required:
- hopper with support frame and funnel transition;
- connected feeder/elevator;
- repeated preforms;
- visible feed rail into oven;
- oven frame with two heater banks and visible process opening;
- at least 8 heater elements per bank;
- transfer/starwheel/guide between oven and cell;
- guarded blow cell;
- two distinct mould/clamp stations;
- stretch/blow rod cues;
- service doors;
- HMI;
- local high-pressure air manifold with >=4 branches;
- cooling-water supply/return pair;
- supported outfeed conveyor;
- >=16 formed bottles;
- outfeed inspection bridge;
- service/safety cues;
- finished architectural shell and lighting.

Not acceptable:
- monolithic opaque oven/blow boxes;
- color-only identity;
- floating process links;
- generic pipes with no product path;
- panel-only detail image;
- outfeed with no repeated bottles.

## Protection gate

Require exact protection of all accepted prior facilities and accepted quarantines:

- F01 accepted 76
- F02 accepted 79
- F03 accepted 30
- F04 accepted 59
- F05 accepted 54
- F06 accepted 43
- F07 accepted 789
- F07 exact 446 retired legacy state
- F04 accepted Training/Restaurant quarantine state
- F06 seven X01 quarantine objects
- Glass Deck quarantine 117
- Restaurant right-wall accepted quarantine
- historical Glass Deck source
- historical Wellness/pavilion protected state

No unauthorized prior-state differences.

## Legacy retirement gate

Old Bottle Blow Molding geometry must not remain visibly stacked with new F08 geometry.

Retirement may use saved:
- hide_viewport=true
- hide_render=true
- exact F08 retirement metadata

No delete.
No transform/material/data mutation.
No collection-wide hiding unless every member is independently proven F08-owned.

## Visual gate

Required final full renders:
- A_CONTEXT 1440×960
- B_FUNCTIONAL 1440×960
- C_SEQUENCE_DETAIL 1440×960
- D_INTEGRATED 1440×960

Required previews:
- 900×600 for all four.

All evidence must:
- use actual saved canonical state;
- use no QA-only hiding;
- keep camera outside geometry;
- be label-blind readable;
- be non-black;
- avoid dominant unrelated occluders.

Specific visual requirements are locked in the design contract.

The decisive visual question:

Can an independent viewer infer `preforms → heating → blow forming → formed-bottle discharge` without reading labels?

If not, FAIL.

## GLB gate

Do not use broad `use_visible=True`.

Use deterministic membership export:

Expected membership =
- every accepted pre-F08 GLB node except exact confirmed retired F08 legacy nodes that were present in the pre-F08 GLB;
- plus every new accepted F08 exportable object;
- no unrelated omissions;
- no unrelated additions.

Require:
- zero missing expected names;
- zero unexpected names;
- all accepted F01-F07 baseline names preserved;
- all new intended F08 names present;
- exact retired F08 legacy names absent.

Use temporary selection/export staging only; restore it after export and do not save temporary state into the Blend.

## Scope

No F09.
No REV004 changes.
No REV006.
No tour/video.
No .hiveai.
Codex must not edit root TASKS.md or locked audit/design files.

## Success stop

`AWAITING_GPT_FACILITY_AUDIT_F08`
