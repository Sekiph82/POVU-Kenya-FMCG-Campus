| Facility | Canonical name | Result | Evidence |
|---|---|---|---|
| F08 | Bottle Blow Molding | BLOCKED — builder visual | output/rev005-facility-gated/F08_F15_combined/F08/ |
| F09 | Chemical Compound / Controlled Receiving | BLOCKED — builder visual | output/rev005-facility-gated/F08_F15_combined/F09/ |
| F10 | ETP / Water Treatment | PASS (builder visual) | output/rev005-facility-gated/F08_F15_combined/F10/ |
| F11 | Finished Goods Warehouse / Dispatch | BLOCKED — builder visual | output/rev005-facility-gated/F08_F15_combined/F11/ |
| F12 | Glass Deck Central Command / Training / Café Gallery | PASS (builder visual) | output/rev005-facility-gated/F08_F15_combined/F12/ |
| F13 | Liquid Filling / Packaging | PASS (builder visual) | output/rev005-facility-gated/F08_F15_combined/F13/ |
| F14 | Occupational Health / First Aid | PASS (builder visual) | output/rev005-facility-gated/F08_F15_combined/F14/ |
| F15 | Packaging Warehouse | BLOCKED — builder visual | output/rev005-facility-gated/F08_F15_combined/F15/ |

# M08.47 — F08–F15 Combined Facility Closure

## Resolved mapping and source-of-truth basis

The mapping follows the ordered `GROUPS` list in `3d/revisions/REV005/pipeline/build_rev005_interior_remediation_v08.py`, corroborated by each matching canonical `REV005_V08_CLEAN_*` collection and facility-specific V10 image specifications. In that sequence, F07 is Administration / HQ / R&D / QC and F08 is Bottle Blow Molding; the seven following groups map consecutively to F09–F15 below. IDs are not encoded as metadata in the Blender collections. Canonical Blend: `3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`; canonical GLB: `3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb`.

| ID | Canonical name | Process / purpose | Authorized collection |
|---|---|---|---|
| F08 | Bottle Blow Molding | Resin/preform input → feed/elevation → heat → stretch/blow moulding → bottle release/outfeed | `REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING` |
| F09 | Chemical Compound / Controlled Receiving | Controlled drum/IBC receipt, containment, storage and metered transfer to process | `REV005_V08_CLEAN_CHEMICAL_COMPOUND_CONTROLLED_RECEIVING` |
| F10 | ETP / Water Treatment | Influent/equalization → treatment/aeration → clarification → filtration/discharge and sludge handling | `REV005_V08_CLEAN_ETP_WATER_TREATMENT` |
| F11 | Finished Goods Warehouse / Dispatch | Finished-case pallet storage → consolidation/staging → dispatch check → dock/loading | `REV005_V08_CLEAN_FINISHED_GOODS_WAREHOUSE_DISPATCH` |
| F12 | Glass Deck Central Command / Training / Café Gallery | Enclosed elevated shared space with distinct operations command, training/collaboration, café and gallery functions | `REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY` |
| F13 | Liquid Filling / Packaging | Bottle infeed → fill → cap → label/inspect → case-pack → outfeed | `REV005_V08_CLEAN_LIQUID_FILLING_PACKAGING` |
| F14 | Occupational Health / First Aid | Reception/waiting → triage/exam/treatment → clinical supplies, handwash and privacy | `REV005_V08_CLEAN_OCCUPATIONAL_HEALTH_FIRST_AID` |
| F15 | Packaging Warehouse | Packaging receipt/inspection → segregated storage/staging → issue lane to production | `REV005_V08_CLEAN_PACKAGING_WAREHOUSE` |

## Campaign source state

- Starting/working revision: `05568bf994d9cd5840712cda04d7a8e855b56764` on `main`, initially clean and equal to `origin/main`.
- Canonical Blend initial SHA-256: `B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642`.
- Canonical GLB initial SHA-256: `B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372`.
- F08 R02 staged Blend SHA-256 inherited and to be reverified before use: `0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25`.
- F08 inherited R02 protection facts: accepted meshes 391; retired legacy 391; NOT_F08 5; preforms 30; elevator riders 6; downstream feed 7; oven path 13; transfer riders 3; heater elements 16; formed outfeed bottles 16; protected differences 0; collisions 0; outside-envelope objects 0.
- F08 R03 audit is `REMEDIATION_REQUIRED_R04_PROCESS_STATE_GEOMETRY`; camera-only work exhausted because stretch/blow, loaded preform, formed bottle and complete sequence readability were each 0.
- V09 audit verdict for all interior groups was `REMEDIATION_REQUIRED`; the target-specific image findings and V10 specs are captured in facility sections below.

## F08–F15 execution record

### Common evidence and limits

- The ordered campaign used the canonical V08 groups and facility-specific V10 views. Published evidence index: `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_EVIDENCE_INDEX.json`; it records 24 facility views (A/B/C for F08–F15), camera coordinates and targets, per-object bounds checks, QA-only shell objects hidden, and PNG paths. The companion `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_SOLID_CAMERA_VALIDATION.json` records world-space BVH containment against watertight facility meshes, boundary rejection, and conservative bounds for nonwatertight meshes. All 24 views passed this actual solid-camera-origin check. All PNGs are 1280×800; final A/B/C contact sheets are `CONTACT_FINAL_A.jpg`, `CONTACT_FINAL_B.jpg`, and `CONTACT_FINAL_C.jpg` in the local evidence directory. F15_C was moved outside the front-header solids and rerendered before the final check.
- QA compositions temporarily hide only listed target-facility shell/header/roof or glazing objects to expose internal process relationships. Those objects remain in the canonical model. No broad campus removal or F01–F07 redesign was performed.
- Result labels below are Codex builder findings based on direct inspection of the rendered PNGs. They are not independent GPT audit decisions or owner acceptance.

### F08 — Bottle Blow Molding — BLOCKED

- Contract: resin/preform receipt and feed, preform heating/handling, stretch/blow moulding, formed-bottle release, and continuous outfeed/transfer.
- Starting state: exact accepted R02 staged room and 391-mesh accepted set, with its protected anchors retained. One bounded process-state geometry pass added distinguishable preform/bottle states, mould/cavity and tie-bar cues, and discharge elements; the staged evidence set contains 413 meshes. No source R02 object was deleted from the staged collection; the original canonical F08 remained unpromoted.
- Views: A/B/C at `F08/F08_A.png`, `F08/F08_B.png`, `F08/F08_C.png`. The evidence index records camera origins outside individual target-mesh bounds and the QA-only hidden shell list.
- Finding: individual equipment and product geometry is present, but no reviewed view communicates the complete heated-preform → stretch/blow → formed bottle → release/outfeed sequence label-blind at overview distance. The R03 diagnosis remains applicable: process-state storytelling is unresolved. The bounded geometry pass failed its visual gate; no further camera fishing was done.
- Canonical status: F08 was not promoted by the selective promotion step; the initial canonical F08 collection is preserved in the final Blend/GLB.

### F09 — Chemical Compound / Controlled Receiving — BLOCKED

- Contract: controlled drum/IBC receipt and containment, bulk chemical storage, metered transfer, and a legible route from receiving to process.
- Geometry pass: dock/check point, drums, IBC cages, bundled bulk tanks, two pump/motor skids, transfer pipe/hose routes, gate and eyewash were built within the authorized F09 collection (98 meshes). The prior F09 collection was rebuilt in the staged file; it was not promoted to canonical.
- Views: A/B/C at `F09/F09_A.png`, `F09/F09_B.png`, `F09/F09_C.png`; C was replaced during the final blocker sweep to test a wider receiving-to-tank view.
- Finding: no view shows the IBC/drum receipt, tanks and pump transfer relation together clearly. C shows drums and bulk tanks but does not make the IBC cages and connected transfer sequence readable. Facility remains blocked on spatial process relation.
- Canonical status: not promoted; original F09 collection preserved.

### F10 — ETP / Water Treatment — BUILDER_VISUAL_PASS

- Contract: influent/equalization, aeration, clarification, filtration/discharge and sludge handling with plausible fluid connections and operator access.
- Geometry pass: open equalization and aeration basins with diffuser header, circular clarifier with bridge/scraper, filter vessels, sludge holding tank/pumps, process piping, walkways and rails.
- Views: A/B/C at `F10/F10_A.png`, `F10/F10_B.png`, `F10/F10_C.png`.
- Finding: direct review shows distinct basins/aeration, clarifier and filter/sludge equipment in context; the treatment stages read as a connected utility process at builder level.
- Promotion: included in the selective canonical candidate; collection has 107 mesh objects. Independent combined audit remains required.

### F11 — Finished Goods Warehouse / Dispatch — BLOCKED

- Contract: finished-case pallet storage, consolidation/staging, dispatch check and dock/loading transfer, with a legible handling vehicle/interface.
- Geometry pass: case racks, pallets and lane markings, consolidation staging, dispatch desk/monitor/scale, dock levellers and door frames, and a forklift-like vehicle form (188 meshes). The staged F11 collection was not promoted.
- Views: A/B/C at `F11/F11_A.png`, `F11/F11_B.png`, `F11/F11_C.png`; the final sweep cleared a false front-wall occlusion for review.
- Finding: racks, staging and dock are visible, but the vehicle does not read clearly as a forklift/AMR and the loading relationship between staging and dispatch remains under-readable. Blocked.
- Canonical status: not promoted; original F11 collection preserved.

### F12 — Glass Deck Central Command / Training / Café Gallery — BUILDER_VISUAL_PASS

- Contract: distinct command/operations, training/collaboration, café and gallery/circulation zones within the elevated enclosed shared space.
- Geometry pass: zone floor inlays, four command consoles/operator screens and multi-display wall, training tables/chairs/screen, café counter/backbar/machine, seating/gallery circulation, glazing and shell (215 meshes). The promoted collection replacement is the only F12 change in canonical Blend/GLB.
- Views: A/B/C at `F12/F12_A.png`, `F12/F12_B.png`, `F12/F12_C.png`; C was replaced during the final sweep for a closer combined zone view.
- Finding: A/B distinguish all three programmed functions and C clarifies command consoles alongside training/café/circulation. Builder visual pass.
- Promotion: included in the selective canonical candidate; collection has 215 mesh objects. Canonical name is `REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY`.

### F13 — Liquid Filling / Packaging — BUILDER_VISUAL_PASS

- Contract: bottle infeed, filling, capping, labelling/inspection, case packing and outfeed, with continuous product path and guards/operator interface.
- Geometry pass: infeed bottle conveyor, bottles, eight-nozzle filler/manifold, cap bowl/chute/capper, label roll/applicator/inspection sensor, case pack/outfeed, guards and HMI (210 meshes). The promoted collection replacement is the only F13 change in canonical Blend/GLB.
- Views: A/B/C at `F13/F13_A.png`, `F13/F13_B.png`, `F13/F13_C.png`.
- Finding: A communicates the operation order; B makes label/case-pack and bottle path visible; C shows the adjacent line-to-packer relation. Builder visual pass.
- Promotion: included in the selective canonical candidate; collection has 210 mesh objects.

### F14 — Occupational Health / First Aid — BUILDER_VISUAL_PASS

- Contract: reception/waiting, triage/exam/treatment, clinical supplies, handwash and privacy.
- Geometry pass: room shell, reception/waiting seating, treatment bed/mattress/head support, trolley/shelf, monitor, privacy curtain/track, sink and storage (63 meshes). The promoted collection replacement is the only F14 change in canonical Blend/GLB.
- Views: A/B/C at `F14/F14_A.png`, `F14/F14_B.png`, `F14/F14_C.png`.
- Finding: A/B make waiting/reception and treatment readable; C gives a closer bed/privacy/monitor view, with some framing crop but adequate builder evidence in the combined set. Builder visual pass.
- Promotion: included in the selective canonical candidate; collection has 63 mesh objects.

### F15 — Packaging Warehouse — BLOCKED

- Contract: packaging receipt/inspection, segregated storage/staging and issue lane to production, with visible material movement and receiving/issue role separation.
- Geometry pass: carton/closure racks, film rolls, marked inbound/check desk, issue lane/conveyor/desk, dock/doors, pallets and forklift form (176 meshes). The staged F15 collection was not promoted.
- Views: A/B/C at `F15/F15_A.png`, `F15/F15_B.png`, `F15/F15_C.png`.
- Finding: storage, rolls, issue lane and pallet groups are visible, but the handling vehicle is not legible in context and the receiving-versus-issue split is not sufficiently clear. A is also low exposure. Blocked.
- Canonical status: not promoted; original F15 collection preserved.

## Final blocker sweep and selective promotion

- After completing F15, the final sweep retested the F08–F15 blockers with front-header visibility adjustments and targeted C-view changes for F09 and F12. It did not convert F08, F09, F11 or F15 to passes. Final matrix remains four builder visual passes (F10/F12/F13/F14) and four blockers (F08/F09/F11/F15).
- A promotion candidate replaces only the four passing collections. Blender comparison reports 11,052 non-promoted scene objects in both baseline and candidate, zero removed, zero added, zero changed, result `PASS`; see `M08_47_PROMOTION_CANDIDATE_VALIDATION.json`.
- The initial candidate GLB export used visible-only export and was found to lose campus nodes (3,033 exported versus 10,941 in the starting GLB). That file was rejected. A corrected explicit-selection export was validated against the exact expected named-node set: 10,941 baseline nodes, 350 old target nodes replaced, 595 new target nodes, 11,186 expected final nodes, 11,186 exported nodes, zero missing and zero extra. Published proof: `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_GLB_PARITY.json`. The companion `coordination/Logs/REV005_F08_F15_COMBINED_FACILITY_CLOSURE_PROMOTION_VALIDATION.json` records the four promoted collection object sets and zero-difference signature for all non-promoted objects. This parity export is the GLB promoted to canonical.
- First solid-camera validation found F15_C within `PKG_V10_FRONT_HEADER` and `PKG_V10_FRONT_R`; this frame was rejected. The camera moved from (0, 56.5, 8) to (0, 47.5, 10), was rerendered and directly reviewed. The final BVH-based check returned `PASS` for all 24 origins; the exact camera coordinates and per-view counts are in the published solid-camera report.
- The first diagnostic render invocation also overwrote two ignored scratch files, `output/rev005-interior-remediation-v08/F08/F08_A.png` and `F08_B.png`, due to a helper resetting its output root. The execution script was corrected immediately to reapply the M08.47 destination after helper import. The official V08 QA images/index and canonical state were not altered by that collision. The two scratch files were not blindly restored; the incident is recorded for transparent provenance.
- Blender 5.2.2 completed all geometry/render/export operations successfully. Shutdown emitted a BlenderKit add-on `unregister_class` cleanup traceback after the operations; this was an add-on teardown warning and did not invalidate the saved artifacts or parity report.

## Canonical result and publication handoff

- Final canonical Blend SHA-256: `83D00D7C18B4DED5B8E674AEF3DF77659E21C9E6035F2CAD318E7F6B414AC3E6`.
- Final canonical GLB SHA-256: `18C146559F5675D6FE36759328F14CDD44F3626C5571B5671D3DCE6F33BAB5D0`.
- Selective promotion scope: only F10, F12, F13 and F14 facility collections changed in the canonical model. F01–F07 and all other non-promoted collections retain the baseline Blender object signature reported above. GLB node parity is exact to the stated replacement rule.
- Final state: `AWAITING_GPT_F08_F15_FINAL_AUDIT_WITH_RECORDED_BLOCKERS`. Independent GPT combined audit is the next required actor. No GPT audit PASS or owner acceptance is claimed by this execution log.
- Starting Git HEAD: `05568bf994d9cd5840712cda04d7a8e855b56764`; branch `main`; starting worktree was clean and HEAD matched `origin/main`.
- Scripts run: `execute_m0847_f08_f15.py` (geometry/render evidence, with final F15_C rerender), `promote_m0847_builder_passes.py` (four-collection candidate and Blender signature comparison), `export_m0847_parity_glb.py` (exact named-node export), `validate_m0847_solid_cameras.py` (24 solid-geometry origin checks), and `make_m0847_contact_sheets.py` (final contact sheets). No general test suite was run; these are task-specific model/evidence validation gates.
- `git diff --check` passed before publication. Large render images, staged candidates and baseline backups remain in the ignored local evidence directory; published lightweight reports and the combined execution log are in `coordination/Logs/`.
- Git ending HEAD, commit, push result and local/origin equality are recorded after commit and safe push.
