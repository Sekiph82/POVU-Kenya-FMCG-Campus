# M08.39 — F06-X02 WIDE-FOV INTEGRATED VIEW + GLB EXPORT PARITY

## Scope

Execute F06-X02 only.

This is an evidence/export remediation after:

- M08.38 correctly quarantined exactly seven proven cross-facility V09 envelope objects;
- M08.38 then correctly stopped because its 35–52 mm camera grid still did not satisfy the complete integrated visual gate;
- the attempted `use_visible=True` GLB export incorrectly dropped thousands of canonical nodes including 12 accepted F06 names.

Do not begin F07.

Do not change geometry.

Do not widen quarantine.

## Read first

1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F06_X01_GPT_AUDIT.md`
4. `coordination/Audits/REV005_F06_X01_CROSS_FACILITY_BLOCKER_ROOT_CAUSE.md`
5. `coordination/Audits/REV005_F06_X01_TARGETED_QUARANTINE_GPT_CRITERIA.md`
6. `coordination/Logs/REV005_F06_X01_TARGETED_QUARANTINE_CODEX_LOG.md`
7. all F06 / R01 / X01 committed evidence

## Safe synchronization

Canonical workspace:

`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Inspect Git status first.

If unexpected local changes exist, STOP without discarding them.

Fetch and fast-forward-only to current `origin/main`.

No reset.
No rebase.
No force.
No second Desktop copy.

Re-read root `TASKS.md`.

It must authorize:

`M08.39 — Facility-Gated F06-X02 wide-FOV integrated view + GLB export parity`

If not, STOP before work.

## Locked starting state

Canonical Blend must be:

`4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`

Canonical GLB must still be:

`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

If either differs:

STOP `BLOCKED_F06_X02_CANONICAL_BASELINE_MISMATCH`.

## Locked accepted X01 quarantine

Exactly these seven objects must remain canonically quarantined:

1. `V09_TOOTHPASTE_FLOOR`
2. `V09_TOOTHPASTE_BACK_WALL`
3. `V09_TOOTHPASTE_SOFFIT`
4. `V09_WET_WIPES_FLOOR`
5. `V09_WET_WIPES_BACK_WALL`
6. `V09_WET_WIPES_LEFT_WALL`
7. `V09_WET_WIPES_SOFFIT`

Their:
- hide_viewport = true
- hide_render = true
- F06-X01 quarantine custom properties

must remain unchanged.

No additional object may be quarantined.

## Locked F06 geometry

The accepted F06 historical destination remains:

`REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`

Required count:

43

Required contribution split:

- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1

Do not:
- add/delete objects;
- move/rotate/scale;
- change dimensions;
- change material/data/parent;
- change collection membership;
- rebuild the facility.

## Part A — correct X01 regression evidence

The X01 regression file incorrectly reported the contribution split as all zeros.

Do not edit historical X01 evidence in place.

Create:

`output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_REGRESSION.json`

Derive contribution counts directly from the committed 43-object destination manifest `source_contribution` fields.

Require:
- BASE 7
- V01 12
- V02 23
- V03 0
- V04 0
- V05 1
- total 43

Also re-confirm:
- all 43 F06 accepted signatures unchanged;
- X01 seven-object quarantine unchanged;
- all F01-F05 protection remains unchanged.

## Part B — wide-FOV camera search

Candidate 32 from X01 is the seed:

- camera (8,43,6)
- target (-4,50,2.8)
- lens 52 mm
- LOS 9/9

It already shows the hopper/dosing/balance process but clips the transfer/service relationship.

Do not restart with another broad random camera grid.

Search tightly around the successful right/front-oblique family.

### Required lens set

Test at least:

- 20 mm
- 24 mm
- 28 mm
- 30 mm
- 32 mm
- 35 mm

Sensor width:

36 mm

### Required camera families

At minimum test combinations around:

- (8,43,6)
- (10,43,6)
- (12,43,6)
- (10,41,7)
- (12,41,7)
- (14,42,7)
- (10,45,7)
- (12,45,8)

Also test at least four farther-back right/front-oblique positions of your own choosing.

### Target families

Bias framing so both the left operator/service side and right/downstream transfer item stay in frame.

At minimum test targets around:

- (-4,50,2.8)
- (-5,49.5,2.6)
- (-4.5,49,2.5)
- (-5.5,49,2.8)
- (-3.5,49.5,2.4)

### Candidate count

Render at least 30 new current-context candidates at 900×600.

Do not use:
- temporary object hiding;
- new quarantine;
- geometry edits;
- clipping planes that change scene truth.

## Required LOS targets

Use the same nine F06 process targets:

1. `V02_WEIGH_HOPPER_0`
2. `V02_WEIGH_HOPPER_2` or 3
3. `V02_WEIGH_HOPPER_VALVE_1`
4. `V02_WEIGH_DOSING_CHUTE_0`
5. `V02_WEIGH_DOSING_CHUTE_2`
6. `V02_PRECISION_BALANCE_0`
7. `V02_PRECISION_BALANCE_2`
8. `V02_WEIGH_TRANSFER_TOTE`
9. `V02_WEIGH_OPERATOR_TABLE`

Require:

>=7/9 LOS

LOS is necessary, not sufficient.

## Required final visual gate

One single integrated frame must clearly show:

- weigh booth/enclosure;
- substantially complete four-hopper row;
- hopper valves;
- dosing chutes/path;
- precision balance stations;
- balance table;
- transfer tote/cart clearly identifiable and not materially clipped;
- operator/service zone visibly identifiable;
- service/access organization;
- coherent hopper → dosing → balance → transfer relationship;
- legitimate current context.

Also require:
- camera outside geometry;
- no unrelated structure dominating;
- no material clipping of required functional cues;
- no QA-only hiding;
- no neighbor mutation beyond the locked seven X01 quarantines.

Do not use the wall label as functional proof.

## Candidate evidence

Create:

`output/rev005-facility-gated/F06_micro_weigh/X02/F06_X02_CAMERA_CANDIDATES.json`

and at least 30 previews:

`F06_X02_CANDIDATE_01_900x600.png`
through
`F06_X02_CANDIDATE_30_900x600.png`

More are allowed.

Each candidate record must include:
- camera XYZ;
- target XYZ;
- lens;
- LOS result;
- blocker names;
- full visual-cue matrix;
- camera-outside-geometry;
- preview path.

Do not auto-select by LOS.

## Final integrated evidence

If a valid candidate exists, produce:

- `D_INTEGRATED_CONTEXT_X02.png` at 1440×960
- `D_INTEGRATED_CONTEXT_X02_PREVIEW_900x600.png`

Create:

`F06_X02_INTEGRATED_CAMERA_VALIDATION.json`

The 1440×960 and 900×600 outputs must use the exact same:
- camera
- target
- lens
- canonical saved visibility state.

If no candidate passes:

STOP `BLOCKED_F06_X02_NO_COMPLETE_INTEGRATED_VIEW`

Do not change geometry or widen quarantine.

## Part C — deterministic GLB export parity

Do not call the canonical export with `use_visible=True`.

The current locked baseline GLB is the structural membership reference:

`98BFAE794024D7217FCEC51936B832F6D3AF4C33ECD17F7973860BBC9AE98825`

First parse the baseline GLB and record:
- node count;
- node-name multiset;
- mesh count;
- all 43 accepted F06 names;
- the seven X01 quarantine names.

Create:

`F06_X02_GLB_BASELINE_MEMBERSHIP.json`

### Export membership target

The new GLB must preserve the baseline node-name membership except the seven quarantined X01 objects.

Hard requirements:

- 43/43 accepted F06 destination names present;
- all seven X01 quarantine names absent;
- zero other baseline node-name omissions;
- zero unexpected new node names.

If baseline node-name membership maps one-to-one to current Blender object names, expected node count is:

10,598 = 10,605 - 7

If it does not map one-to-one, compute and document the exact expected count from the baseline node-name multiset. Do not force 10,598 blindly.

### Temporary export staging is allowed

You may create an in-memory export state only.

Allowed:
- snapshot all object selection/hide states;
- resolve the baseline GLB member objects in Blender;
- temporarily make only the intended export member objects selectable/exportable;
- temporarily unhide intended export members if required by Blender selection semantics;
- select the intended export member set;
- export with explicit selection membership;
- set `use_selection=True`;
- set `use_visible=False` if supported/required so selected historically hidden accepted objects are not dropped;
- restore all temporary selection/hide state afterward;
- verify the canonical Blend hash remains unchanged after the export process.

Not allowed:
- save the temporary staging visibility into the Blend;
- add helper geometry;
- modify materials/transforms;
- use a broad visible-only export.

### GLB parity evidence

Create:

`F06_X02_GLB_EXPORT_PARITY.json`

Record:
- baseline node-name multiset;
- expected after node-name multiset;
- actual after node-name multiset;
- missing names;
- unexpected names;
- 43 F06 name check;
- seven-quarantine absence check;
- node/mesh counts;
- final GLB SHA.

If exact membership parity cannot be achieved:

discard the attempted GLB,
restore the locked baseline GLB,
STOP `BLOCKED_F06_X02_GLB_EXPORT_PARITY`.

Do not publish a lossy GLB.

## Part D — final protection and hashes

After all successful evidence/export work:

Re-confirm:
- canonical Blend hash remains exactly:
  `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`
- F06 destination count = 43;
- contribution split = 7/12/23/0/0/1;
- seven X01 quarantines unchanged;
- all prior accepted/protected signatures unchanged;
- F07 not started.

Create:

- `F06_X02_FINAL_HASHES.json`
- `F06_X02_VALIDATION.json`

The GLB hash may change only if the deterministic membership export passes.

## Required log

Write:

`coordination/Logs/REV005_F06_X02_WIDE_FOV_GLB_PARITY_CODEX_LOG.md`

Include:
- baseline hashes;
- corrected contribution split;
- camera search summary;
- selected integrated candidate;
- GLB baseline/expected/actual membership counts;
- final hashes;
- stop marker.

## Git scope

Commit/push only:

- X02 evidence/renders/log;
- canonical GLB only if deterministic export membership parity passes.

Do not commit a changed canonical Blend.

Do not edit:
- root TASKS.md
- locked prior audits
- prior evidence files

Do not begin F07.

## STOP

Success:

`AWAITING_GPT_FACILITY_AUDIT_F06_X02`
