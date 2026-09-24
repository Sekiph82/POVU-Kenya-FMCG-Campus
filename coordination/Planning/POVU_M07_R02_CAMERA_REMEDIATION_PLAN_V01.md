# POVU M07 R02 Camera and Callout Remediation Plan

Status: implementation planned from frozen REV004.1 evidence
Source: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`
Source SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`

## R01 evidence reviewed

The R01 master was visually checked at the opening, CH04 Hands of Growth, CH05 facilities, and CH06 stair checkpoints. The failures are systemic:

- `anchorForShot()` uses text heuristics and repeated broad coordinates rather than the physical target named by the shot.
- World labels are projected from that generic coordinate and display `features[0]`, so labels can describe a different physical object than the image.
- CH01 exposes internal planning language (`Production massing`, `Landscape framework`).
- The caveat/debug overlay exposes `UNCERTAIN callout`, `DOCUMENTED NOT MODELED`, and `REV004.1 EVIDENCE BOUNDARY` in the final render.
- CH04 S015 is framed through unrelated foreground trees; the sculpture is not the visual subject.
- CH05 S024 and S025 reuse the general campus frontage instead of the verified wellness/recreation and daycare/clinic objects.
- CH06 S027 and S028 reuse the same central factory interior angle instead of the east and west stair targets.

## R02 implementation plan

1. Add a typed per-shot target plan. Each shot resolves an explicit ordered list of real GLB object names or prefixes, a human-facing label, camera offset, and field of view. No shot will derive its physical target from arbitrary feature text.
2. Load the frozen GLB once and compute target points from object world bounding boxes. Empty presentation/navigation anchors are preferred where supplied; mesh bounds are used for facility details and production equipment.
3. Drive camera position and look-at from the resolved target point. Interpolate from the previous shot pose with eased travel so the route is continuous and never teleports between unrelated hard-coded parking coordinates.
4. Use shot-specific frontage offsets for VIP, people facilities, Glass Deck stairs, utilities, and production equipment. The camera will be placed outside the target volume and look toward the verified target center.
5. Project the callout from the same resolved target point used by the camera. Use the target plan’s public label only; do not expose internal planning terms, IDs, confidence flags, or evidence/debug text.
6. Keep the opening establishment shot as an intentional approximately 15-second aerial overview, with only verified building labels where a real model target is present.
7. Remove the redundant exterior Glass Deck shot from the R02 composition route. The east, west, and central access shots remain target-specific.
8. Preserve the frozen GLB. Any presentation-only living-wall visibility correction will be documented separately and will not rewrite the source asset.

## Geometry and visual checks

- Living wall: verify the rendered foliage stays aligned with the modeled backing/panels; no new freestanding extension will be created.
- Hands of Growth: use the sculpture empties and mesh bounds as the target and choose a clear elevated three-quarter view so both hands, plinth, trunk, and crowns remain visible.
- East/west/central stairs: use the corresponding stair empties and step meshes; verify each view contains the stair and its Glass Deck relationship.
- Wellness, daycare/clinic, R&D/QC, Academy, café, Garden Pods, and employee garden: verify the named physical object is visible in the final frame of each shot.

## Automated and visual acceptance evidence

- Static source scan: every shot has one explicit target plan; no broad text-coordinate resolver remains.
- Camera scan: consecutive shot poses are interpolated and target-specific; duplicate consecutive poses and zero-length route segments are reported.
- Target scan: object resolution reports missing names/prefixes before rendering.
- Render scan: final R02 master is checked with `ffprobe`, chapter/checkpoint frames, and a complete-timeline contact sheet.
- Human visual QA: opening, CH03 VIP, CH04 landmarks, CH05 people facilities, CH06 stairs, and representative factory/utility chapters are inspected after the complete render.

## Planned deliverables

- R02 source changes under `remotion/povu-digital-twin/src/`
- target-resolution and camera validation tooling under `remotion/povu-digital-twin/scripts/`
- complete R02 MP4 and checkpoint/contact-sheet evidence under `output/complete-tour-r02/`
- structured remediation report A–H and updated M07 CODEX log
