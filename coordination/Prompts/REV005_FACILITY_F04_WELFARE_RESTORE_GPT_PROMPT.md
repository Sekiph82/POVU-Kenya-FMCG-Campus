# F04 — EMPLOYEE CHANGING / SHOWER / LOCKER SUPPORT — EXACT HISTORICAL RESTORATION

## Scope

One facility only: F04.

Read:
- root TASKS.md
- coordination/Workflow/REV005_FACILITY_GATED_WORKFLOW.md
- coordination/Audits/REV005_F04_WELFARE_HISTORICAL_SOURCE_PROVENANCE.md
- coordination/Audits/REV005_FACILITY_F04_WELFARE_GPT_AUDIT_CRITERIA.md

## Baseline

Canonical root:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Required current hashes:
- Blend `754A76F35DCCBE9BD054227BA90A8505C332338ABDA9847BFEF101C2EFB0104D`
- GLB `A426A25C19FA85D90CD741358554B484F6414D730A4898872A50D7CA17DA07A1`

If mismatch: STOP `BLOCKED_F04_CANONICAL_BASELINE_MISMATCH`.

## Protect prior PASS

Create before/after protection manifests for:
- F01 76 accepted objects
- F02 79 accepted objects
- F03 30 accepted objects
- historical Glass Deck source
- 117-object V09 Glass Deck quarantine

## Historical replay

Detached OS-temp worktree at:
`420038365847de763d64c8583a9e31ac5a6bd677`

Verify initial source Blend hash:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

Replay V01→V02→V03→V04→V05 unchanged.

Use original V05 objects_for() for:
`Employee changing / shower / locker support`

Required source composition:
- 10 BASE
- 49 V01
- total 59

Write exact replay source manifest.

## V01 dimensional verification

Verify all details numerically.

Locker-bank centers:
X = 23,27,31,35,39; Y=-77.0; Z=2.5.
Each bank = 3.0×0.55×2.5 m.

Each bank has three doors:
X offsets -0.9, 0.0, +0.9;
Y=-77.33; Z=2.5;
each = 0.70×0.06×1.95 m.

Shower centers:
X = 24,29,34,39.

Each shower:
- back center (X,-66.25,2.6), size 3.2×0.12×2.8
- side A (X-1.54,-65.1,2.6), size 0.12×2.3×2.8
- side B (X+1.54,-65.1,2.6), size 0.12×2.3×2.8
- open/front (X,-63.92,2.7), size 1.5×0.05×2.4
- shower head center (X,-64.2,4.3), radius 0.13, depth 0.35
- drain center (X,-64.0,1.31), size 0.65×0.18×0.03

Clean entry:
(30,-70,1.5), size 16×0.16×2.6.

Dirty entry:
(30,-73,1.5), size 16×0.16×2.6.

Bench seat:
(30,-74.4,1.8), size 10×0.75×0.18.

Bench legs:
(25.4,-74.4,1.45) and (34.6,-74.4,1.45), each 0.12×0.5×0.65.

Tolerance <=0.001 m.

## Source parity

Run original V05 renderer.

A:
- loc (14,-88,13)
- target (30,-70,3)
- 52 mm
- archived SHA `485E04DA347BBB257C778204DB7613E7D355199BAD18B79541CE8BF5FA86EB21`

B:
- loc (20,-78,8)
- target (30,-70,3)
- 52 mm
- archived SHA `59F769B86BE5602FC43BA3F2D05786B8C94D169014C39FCBD2BC832D56BBC9D9`

Decoded visual parity must be exact.

## Canonical mutation

Inventory current F04 first.

Remove/unlink only current broken F04 representation.

Append exact 59-object accepted source into:
`REV005_FG_F04_WELFARE_ACCEPTED_V05_REPLAY`

Preserve all source transforms/dimensions/materials/parents.

## Destination parity

Render facility-only historical A/B at 900×600.

Write:
- F04_DEST_PARITY_A_900x600.png
- F04_DEST_PARITY_B_900x600.png
- parity JSON

Require visual/pixel match to archived A/B.

## Prior-PASS regression gate

F01 76 unchanged.
F02 79 unchanged.
F03 30 unchanged.

If any mismatch: STOP `BLOCKED_F04_PRIOR_PASS_REGRESSION`.

## Integrated preflight

Compute exact 59-object union bounds.

Test azimuths:
0,45,90,135,180,225,270,315°.

Use 9-ray LOS.
Require >=7/9 clear.
Require facility 30–65% of frame.
52 mm preferred, 45 mm minimum.
No automatic cross-facility exclusion.

If none passes:
STOP `BLOCKED_F04_INTEGRATED_COLLISION` and report blockers only.

## Final renders

A_CONTEXT:
1440×960, historical A camera.

B_FUNCTIONAL:
1440×960, historical B camera.

D_INTEGRATED_CONTEXT:
1440×960 from selected valid integrated camera.

D preview:
900×600 same camera/state.

## Evidence

Create F04 baseline/replay/source/destination/parity/protection/camera/final/validation JSON files.

Create exact log:
`coordination/Logs/REV005_F04_WELFARE_RESTORE_CODEX_LOG.md`

Save/export canonical Blend/GLB.

Commit only F04 evidence + canonical Blend/GLB.

Do not edit TASKS.md or criteria.
Do not begin F05.

## STOP

`AWAITING_GPT_FACILITY_AUDIT_F04`
