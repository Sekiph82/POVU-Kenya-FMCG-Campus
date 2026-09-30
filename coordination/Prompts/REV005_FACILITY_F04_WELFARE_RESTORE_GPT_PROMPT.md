# F04 — WELFARE HISTORICAL RESTORATION V02 — INTERIOR-CONTAINED CAMERA

## Scope

One facility only:

**F04 — Employee Changing / Shower / Locker Support**

The previous F04 run correctly stopped before canonical save at:

`BLOCKED_F04_INTEGRATED_COLLISION`

The historical 59-object source, dimensional contract and archived A/B parity had passed.

The blocker was caused by an incorrect **exterior-camera** assumption.

Read first:
1. root `TASKS.md`
2. `coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md`
3. `coordination/Audits/REV005_F04_INTEGRATED_CAMERA_ROOT_CAUSE_CORRECTION.md`
4. `coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md`
5. `coordination/Audits/REV005_FACILITY_F04_WELFARE_GPT_AUDIT_CRITERIA.md`

## Canonical baseline

Root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Required current:
- Blend `754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`
- GLB `A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

The first F04 attempt must not have changed these.

If mismatch:
STOP `BLOCKED_F04_CANONICAL_BASELINE_MISMATCH`.

## Important geometry fact

Historical source audit proves:

`WELLNESS_PAVILION`
- X 19→41
- Y -79→-61
- Z 1.2→7.2
- size 22×18×6
- center (30,-70,4.2)

F04 is an interior support facility inside this pavilion.

Therefore:
- do not quarantine Wellness;
- do not quarantine Training;
- do not quarantine Restaurant;
- do not interpret pavilion containment as a cross-facility regression;
- do not repeat the exterior 8-azimuth ring as the acceptance gate.

## Phase 1 — safe source reconstruction

Repeat or reuse only if independently revalidated from the prior blocked run.

Historical detached worktree:
`420038365847de763d64c8583a9e31ac5a6bd677`

Required:
- 10 BASE
- 49 V01
- total 59
- dimensional contract PASS <=0.001 m
- archived A/B decoded visual parity PASS

If prior local F04 source evidence exists, it may be reused only if:
- source manifest hash is unchanged;
- source object count is 59;
- dimensional result is PASS;
- source A/B decoded-pixel gate is PASS;
- canonical baseline hashes still equal the locked baseline above.

Otherwise rerun historical replay.

## Phase 2 — protect prior PASS/current context

Before canonical in-memory mutation create protection manifests for:
- F01 76
- F02 79
- F03 30
- historical `WELLNESS_PAVILION`
- `WELLNESS_GLASS`
- historical Glass Deck source
- V09 Glass Deck quarantine 117

Also record current V09 Wellness collection:
`REV005_V08_CLEAN_WELLNESS_RECREATION`

Expected historical V09 report count:
**73**

This collection is NOT authorized for quarantine or mutation by F04.

## Phase 3 — reconstruct destination F04 in memory

Open canonical Blend.

Inventory current/broken F04 representation.

Remove/unlink only F04-conflicting current objects.

Append exact accepted 59 objects into:

`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Preserve:
- matrix_world
- dimensions
- materials
- parents
- visibility

Parity tolerances:
- location <=0.001 m/axis
- rotation <=0.0001 rad
- scale <=0.0001
- dimensions <=0.001 m

Do not save yet.

## Phase 4 — destination A/B parity

Render facility-only historical 900×600:

A:
- loc (14,-88,13)
- target (30,-70,3)
- lens 52 mm

B:
- loc (20,-78,8)
- target (30,-70,3)
- lens 52 mm

Require visual/decoded-pixel parity to archived:
- A `485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`
- B `59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

If not:
STOP `BLOCKED_F04_DESTINATION_PARITY` without saving.

## Phase 5 — exact pavilion/F04 bounds

Compute world bounds from actual geometry.

Write:
`F04_INTERIOR_CAMERA_DIAGNOSTIC.json`

Record:

### Historical pavilion
`WELLNESS_PAVILION`
- min/max XYZ
- center
- extents

Expected approximate:
- min (19,-79,1.2)
- max (41,-61,7.2)

### Front glass
`WELLNESS_GLASS`
- min/max XYZ

Expected approximate:
- X 20→40
- Y -79.2→-79.0
- Z 1.45→6.95

### Accepted F04
59-object union:
- min/max XYZ
- center Fc
- width Fw
- depth Fd
- height Fh

Confirm spatial relationship truthfully.

Do not fail merely because F04 is inside the pavilion. That is expected.

## Phase 6 — interior camera grid

Use ACTUAL pavilion bounds.

Let:
- PminX/PmaxX
- PminY/PmaxY
- PminZ/PmaxZ

For s in:
- 0.9
- 1.8
- 3.0

Generate these 8 XY points:

1. (PminX+s, PminY+s)
2. ((PminX+PmaxX)/2, PminY+s)
3. (PmaxX-s, PminY+s)
4. (PminX+s, (PminY+PmaxY)/2)
5. (PmaxX-s, (PminY+PmaxY)/2)
6. (PminX+s, PmaxY-s)
7. ((PminX+PmaxX)/2, PmaxY-s)
8. (PmaxX-s, PmaxY-s)

24 XY points.

Compute two Z values:

`Z1=min(PmaxZ-0.80, max(FmaxZ+0.70, 4.80))`

`Z2=min(PmaxZ-0.45, max(FmaxZ+1.20, 5.40))`

Total base camera positions:
48.

For each position test target Z values:

Primary:
`Tz=FminZ+0.45*Fh`

Then:
- Tz
- Tz+0.35
- Tz-0.25

Keep target inside F04 vertical bounds.

Target XY:
`(Fc.x,Fc.y)`

Test lens in order:
- 52 mm
- 45 mm
- 40 mm

Never below 40 mm.

## Phase 7 — camera collision rejection

For each candidate:

Reject if:
- outside pavilion XY bounds;
- camera Z <= PminZ+1.2;
- camera Z >= PmaxZ-0.25;
- camera point lies inside or within 0.30 m of an F04 equipment mesh;
- camera point lies inside or within 0.25 m of any other visible equipment/non-shell mesh.

Do NOT reject merely because the camera point lies inside the overall AABB of `WELLNESS_PAVILION`; that is expected.

Do reject a position if an actual pavilion surface occupies/intersects the camera point.

Record every rejection reason.

## Phase 8 — 9-ray interior visibility gate

For every surviving candidate cast to 9 F04 samples:

1. center
2. X -30%
3. X +30%
4. Y -30%
5. Y +30%
6. X -20%, Y -20%, Z +20%
7. X +20%, Y -20%, Z +20%
8. X -20%, Y +20%, Z +20%
9. X +20%, Y +20%, Z +20%

A ray = CLEAR when:
- first hit is one of the accepted 59 F04 objects; OR
- no non-F04 hit occurs before the target sample.

A ray = BLOCKED if another object is hit first.

Require:
**>=7/9 clear rays**

Do not hide or quarantine blockers.

## Phase 9 — framing gate

Project F04 union.

Require:
- X bounds within 4%–96%
- Y bounds within 5%–95%
- projected F04 bounding rectangle = **35%–78%** image area

If multiple pass, rank in this order:
1. clear-ray count descending
2. coverage nearest 55%
3. lens preference 52 > 45 > 40
4. greater minimum distance from other geometry

Record top 5 candidates in JSON.

If no candidate passes:
STOP:
`BLOCKED_F04_INTERIOR_CAMERA_NO_VALID_VIEW`

Return exact top blocker object names.
Do not save canonical Blend.

## Phase 10 — final evidence renders

With normal current scene visibility and no QA-only exclusions:

A_CONTEXT:
- 1440×960
- historical A camera

B_FUNCTIONAL:
- 1440×960
- historical B camera

D_INTERIOR_INTEGRATED_CONTEXT:
- 1440×960
- selected interior camera

D preview:
`F04_D_INTERIOR_INTEGRATED_CONTEXT_PREVIEW_900x600.png`
- 900×600
- exact same camera/state

Final D must visibly show F04 and interior pavilion context.

## Phase 11 — regression check

Before save compare:
- F01 76 exact
- F02 79 exact
- F03 30 exact
- historical WELLNESS_PAVILION unchanged
- WELLNESS_GLASS unchanged
- V09 Wellness collection unchanged
- historical Glass Deck unchanged
- V09 Glass Deck quarantine unchanged

If any protected item changed beyond the intended F04 replacement:
STOP `BLOCKED_F04_PROTECTED_CONTEXT_MUTATION`.

## Phase 12 — save/export/evidence

Only after all gates pass:

Save canonical Blend.

Export canonical GLB under current visibility policy.

Create:
- F04_BASELINE_HASHES.json
- F04_REPLAY_SOURCE_MANIFEST.json
- F04_SOURCE_RENDER_HASHES.json
- F04_CURRENT_PRE_RESTORE_MANIFEST.json
- F04_DESTINATION_MANIFEST.json
- F04_DESTINATION_PARITY_HASHES.json
- F04_F01_PROTECTION_BEFORE/AFTER.json
- F04_F02_PROTECTION_BEFORE/AFTER.json
- F04_F03_PROTECTION_BEFORE/AFTER.json
- F04_PAVILION_PROTECTION_BEFORE/AFTER.json
- F04_INTERIOR_CAMERA_DIAGNOSTIC.json
- F04_INTERIOR_CAMERA_VALIDATION.json
- F04_FINAL_HASHES.json
- F04_VALIDATION.json

Create exact log:
`coordination/Logs/REV005_F04_WELFARE_RESTORE_CODEX_LOG.md`

Commit only:
- canonical Blend/GLB
- F04 evidence/renders/log

Do not edit TASKS.md.
Do not edit criteria/workflow.
Do not begin F05.

## STOP

Normal final state:

`AWAITING_GPT_FACILITY_AUDIT_F04`
