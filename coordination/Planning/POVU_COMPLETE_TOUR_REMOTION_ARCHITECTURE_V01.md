# POVU COMPLETE TOUR REMOTION ARCHITECTURE V01

## Scope

This is an implementation plan only. M06 does not modify the frozen GLB, implement the long-form compositions, integrate OpenMontage, or render the final film.

Authoritative source:

- `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`
- SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`

R02 source, MP4, visual system and QA evidence remain locked. The long film expands the proven digital-twin presentation instead of redesigning it.

## Composition tree

```text
POVUCompleteTour
├── CH01_Campus
├── CH02_Arrival_Sustainability
├── CH03_VIP
├── CH04_Landmarks
├── CH05_People
├── CH06_GlassDeck
├── CH07_WetProcessing
├── CH08_Manufacturing
├── CH09_Logistics
├── CH10_Utilities_HSE
└── CH11_Finale
```

Each child composition receives a chapter-local shot list derived from the M06 storyboard. The parent composition owns chapter ordering, title cards, geographic transition cards, final title and derived-cut trims.

## Shared runtime systems

### GLB loader and scene registry

- Load the frozen GLB once in the parent or a shared preloaded asset boundary.
- Build a semantic registry from object names and the REV004.1 manifest.
- Resolve world anchors by semantic ID, not by fragile array index.
- Keep repeated groups grouped for labels and visibility staging: `ProcessTank_01..11`, solar groups, pallet/rack groups, and three wipes lines.
- Fail closed when a storyboard-required semantic target is missing.

### Material and lighting system

Reuse the R02 `MaterialSystem` classification and lighting baseline:

- vegetation treatment, brown trunks and natural green HOG crown;
- solar/PV material;
- façade light-neutral, graphite and bronze/champagne hierarchy;
- architectural glass;
- Water Wall and Living Wall appearance;
- machine and Smart Totem visual language.

No M06 redesign is authorized. Material changes require a separate approved mission.

### Camera system

- Use a chapter-local camera route with explicit keyframes and look-at targets.
- Convert Blender Z-up coordinates through the proven R02 coordinate transform.
- Use ease-in/ease-out splines and shot-local speed limits from `POVU_CAMERA_PACING_STANDARD_V01.md`.
- Support walking-height, interior, medium aerial, restrained crane and near-static hero shots.
- Store every route segment with its matrix IDs so frame QA can trace coverage.

### Labels and world-space anchors

- Use the R02 world-to-screen label system with clamping and occlusion-aware fade.
- Limit normal frames to 1–3 labels.
- Use M05 anchors for HOG and production equipment.
- HOG must use `LABEL_ANCHOR_HANDS_OF_GROWTH`, with `HANDS OF GROWTH` and `People • Skills • Future`.
- Equipment labels should prioritize the wet-processing group, selected production machines, EOL, AMR infrastructure, utilities and HSE markers.

### Water Wall shader and animation

- Preserve the frame-driven Water Wall animation approach from R02.
- Animate `WATER_WALL_WATER_SURFACE`, `WATER_WALL_TOP_FEED` and the visible fall/crest presentation deterministically from frame number.
- Include a contextual shot, medium shot and close detail in CH03.
- Validate the basin relationship and readable POVU branding at the target camera distance.

### Smart Totem system

- Keep one VIP flagship and four campus placements.
- Show a totem in context rather than repeating identical close-ups.
- Use the screen/light treatment from R02 and location-specific destination text only where the manifest supports it.

### Transitions and chapter graphics

- Prefer route-motivated transitions over unrelated dissolves.
- Use a restrained chapter title system with zone name, destination and one-line purpose.
- Use geographic route lines only when they clarify a distant move.
- Evidence caveats for C/D items are documentary cards, not decorative claims.

## Chapter implementation notes

- CH01 owns campus bounds, orientation and production reveal staging.
- CH02 owns all three PV groups, inverter relationship, canopy-underneath inspection and pedestrian arrival.
- CH03 owns VIP, Living Wall, Water Wall animation and real entrance coverage.
- CH04/CH05 own public realm and people facilities with walking-height routes.
- CH06 owns the complete Glass Deck access and interior sequence before production reveal.
- CH07/CH08 own material flow, wet process and all confirmed manufacturing families.
- CH09 owns packaging supply, EOL, AMR infrastructure, FG warehouse and dispatch.
- CH10 owns utilities, ETP, HSE and explicit missing-workshop caveat.
- CH11 owns sustainability synthesis, evidence-limited portfolio language, people return and final campus hero.

## Derived cuts

The parent composition should support:

- Complete Tour: approximately 25:25 from M06 planning estimates;
- Executive Cut: approximately 4:30;
- Promo Cut: approximately 75 seconds.

Cuts must be trims of the authoritative chapter compositions, not separate contradictory scenes.

## OpenMontage later orchestration

OpenMontage may later orchestrate chapter production, storyboard execution, render QA, assembly and final mastering. It must call the proven local Remotion/Three.js renderer and consume the same shot manifest. It must not replace the GLB loader, the semantic camera/label system, or the renderer. OpenMontage integration is explicitly outside M06.

## M07 readiness gates

Before implementation, resolve or explicitly accept the documented/uncertain items in the completeness report, confirm the 91-SKU evidence source, decide how to present the unpaired solar support cluster, and preserve the frozen GLB SHA. After implementation, perform frame-level coverage QA against all matrix rows; background visibility does not pass a row.
