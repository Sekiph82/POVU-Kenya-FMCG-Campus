# REV005 V10 — GLOBAL BLENDER MODELING CONTRACT

This contract applies to every V10 image-specific remediation spec.

## 1. Canonical workspace and source safety

Canonical workspace:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`

Canonical Blend:
`3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Rules:
- REV004 is immutable.
- Do not create REV006.
- Do not create another Desktop project copy.
- Do not create `.hiveai`.
- Do not render tour/final-owner video.
- V10 modifies REV005 only.
- Capture V09-final Blend/GLB hashes into immutable `V10_BASELINE_HASHES.json` before mutation.

Expected V09-final hashes:
- Blend: `46D427377C315FF8838CBF6917DD469E3F88D14F49E52BE0C18F8C0CFE3D68E8`
- GLB: `F09D1E5F4A3581509C33453C88B576A67BB6D2CAFDC08532B05F342BC18F6DCF`

## 2. Mandatory exact V05 restoration for six accepted facilities

Do not rebuild these six from V09/V08 inventory objects:
- Caps and Trigger Assembly
- Daycare / Crèche
- Electrical / LV-MV Room
- Employee Changing / Shower / Locker Support
- Fire Pump House
- Micro-ingredient Weigh / Dispense

Source commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Source V05 Blend SHA-256 recorded by independent audit:
`B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

Safe restoration method:
1. Do **not** reset/checkout the working tree.
2. Materialize the V05 Blend from Git history into a system temp path using `git show <commit>:<blend-path>`.
3. Verify the temp V05 Blend hash.
4. Inspect the six accepted facilities in the V05 file and identify their complete visible object/collection sets.
5. Remove the broken V09 restored versions for those six only.
6. Append/link-copy the accepted V05 geometry into the current V10 canonical Blend while preserving V05 world transforms/materials.
7. If an object depends on a material/node group/library block, append the dependency too.
8. Do not import unrelated V05 facility geometry.
9. Render A/B proof immediately and visually compare to the V05 accepted evidence before continuing.

The V09 “restored_count” inventory method is prohibited for these six because it produced the wrong visible result.

## 3. Finished interior envelope contract

For Admin, Glass Deck, Occupational Health, Restaurant/Café/Kitchen, Security/Reception, Gatehouse, Training and Wellness:

A final visible room may **not** be props on a dark slab.

Required shell:
- finished floor slab with epoxy/tile/wood material as appropriate;
- rear wall;
- both side walls;
- ceiling/soffit;
- real door/opening;
- internal partitions where specified;
- base/trim or visible wall-floor junction;
- ceiling lighting fixtures;
- camera-facing wall may be hidden **for QA only** to create a cutaway, but the wall must exist in the canonical model.

Use facility bounds to size the shell. Do not hard-code one generic shell for every room.

Typical human-space dimensions:
- door: about 0.9–1.2 m wide × 2.1–2.4 m high;
- workstation desk: about 1.4–1.8 × 0.7–0.9 m;
- chair seat height: about 0.45 m;
- countertop: about 0.9 m high;
- people-space ceiling: generally about 2.8–3.6 m unless campus architecture dictates otherwise.

## 4. Industrial geometry contract

A visible industrial machine cannot be one featureless cuboid.

Each machine must show at least:
- structural frame/body;
- infeed/outfeed interface;
- functional head/tool/process region;
- access/guard/service opening;
- control/sensor or utility connection where appropriate.

Process lines must show **product/material continuity**:
- repeated bottles/preforms/tubes/pouches/web/packs/drums/IBCs/etc.;
- conveyors/tracks/hoses/pipes that physically connect adjacent steps;
- no floating disconnected station sequence.

Use bevels on visible hard edges (typically 0.02–0.08 m depending on scale) and smooth/weighted normals where appropriate.

## 5. Warehouse contract

All three warehouses require:
- room/building envelope cues;
- role-specific inventory;
- receiving/issue/dispatch zone;
- staging lanes;
- handling aisle;
- one handling vehicle/AMR/forklift in context;
- door/dock relationship.

Racks alone do not pass.

## 6. Lighting/material contract

Do not use a flat gray world as the main visual read.

Required:
- neutral ambient/world fill;
- ceiling/area lights appropriate to facility;
- readable shadows without crushing detail;
- material separation among wall, floor, stainless/process steel, painted machine frames, wood, glass, product/load and POVU accent.

## 7. Camera contract

All QA cameras:
- must be outside object bounds;
- must have clear line-of-sight to intended target;
- must not clip through walls/equipment;
- must maintain near/far clipping that preserves the complete subject;
- must use perspective rather than orthographic flattening unless a spec explicitly requires otherwise.

A_CONTEXT:
- 3/4 cutaway context;
- whole functional zone visible;
- facility occupies roughly 65–85% of frame.

B_FUNCTIONAL:
- medium 3/4;
- primary functional assembly and at least two related subcomponents visible.

C_SEQUENCE_OR_DETAIL:
- useful close/oblique proof;
- at least two adjacent functional steps plus their connection;
- never a wall/panel/tank-shell-only frame.

## 8. V10 anti-abstraction rule

The V09 helper approach produced visually generic results. Therefore:
- helper functions may create primitive scaffolds;
- final-visible facility geometry must be facility-specific;
- a generic `machine_frame`, `env`, rack row, or colored box cannot be accepted as the final representation by itself;
- do not claim completion from object count, collection name or render existence.

Visual evidence is the gate.
