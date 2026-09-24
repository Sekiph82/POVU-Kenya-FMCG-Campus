# POVU Complete Factory Tour — Remotion Architecture V02

## Scope

This is a planning and implementation handoff for M07. It does not alter the locked R02 source or start a render.

## Source contract

- Load only 3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb.
- Recheck SHA-256 BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A.
- Use the V02 matrix and storyboard as the single shot registry.
- Keep external evidence text separate from geometry-derived labels.

## Data flow

V02 coverage matrix → V02 storyboard registry → camera route records → frame-level QA evidence

Each shot record must retain: V02 shot ID, originating V01 IDs, target semantic names, start/end route, height, lens/FOV, look-at, visible features, labels, overlays, animation, transition, purpose, coverage IDs and evidence sources.

## Camera and label implementation

- Resolve semantic targets from the REV004.1 architectural manifest; never replace a missing target with a generic mesh.
- Use world-tracked labels only for confirmed semantic anchors.
- Keep documentary text overlays for HSE, 91-SKU and documented-not-modeled statements.
- Merged shots use sub-segments/holds inside one continuous shot ID; coverage remains row-traceable through Final_Shot_IDs.
- Use the V02 pacing standard for camera height, lens and hold length.

## QA gates before M07 completion

1. GLB hash gate.
2. Route-target existence gate.
3. Rendered-frame legibility gate for each required matrix row.
4. Caveat-card gate for gatehouse, workshop, CIP/hypochlorite, unpaired solar supports and 91-SKU wording.
5. No claim of detailed engineering approval, exact 4,200 modeled panels or one mesh per SKU.

