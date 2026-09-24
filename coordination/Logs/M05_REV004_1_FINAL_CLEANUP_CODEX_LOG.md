# M05 REV004.1 FINAL CLEANUP — CODEX LOG

## Status

**PASS — REV004.1 final architectural cleanup completed.**

This run stopped at REV004.1 as required. The Complete Factory Tour was not started.

## Source and revision boundary

- Approved source: `3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb`
- Expected source SHA-256: `1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA`
- Actual source SHA-256: `1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA`
- New revision directory: `3d/revisions/REV004.1/`
- REV004 was not overwritten.

## Minimal architectural correction

### VIP Living Wall

Added one thin semantic backing mesh, `LIVING_WALL_EXTENDED_BACKING`, to close the existing VIP Living Wall continuously across the usable left wall.

- Usable wall bounds: approximately X `-97.5` to `-65.0`
- Output mesh bounds: X `-97.4` to `-65.1`, Y `-92.02` to `-91.86`, Z `1.8` to `9.8`
- Doors, glazing, portal, canopy, pedestrian circulation, and Water Wall were not moved or covered.
- Existing Living Wall panels, foliage, and VIP Living Wall semantics were retained.

### Hands of Growth

The duplicate audit compared the approved REV004 Blender hierarchy, object names, transforms, custom `hf_id` values, materials, and the REV003 source inventory. All HOG mesh names in REV004 match the original REV003 HOG set. The approved REV004 GLB has one original HOG component set and zero duplicate GLB roots; therefore `objects_removed` is an empty list and the original was preserved.

The apparent second sculpture is the locked `HandsOfGrowthRuntime` presentation overlay in the R02 Remotion source. R02 source and MP4 were not edited or rerendered.

Semantic mapping added in REV004.1:

- Root: `HANDS_OF_GROWTH`
- Components: `HOG_HAND_LEFT`, `HOG_HAND_RIGHT`, `HOG_TREE_TRUNK`, `HOG_TREE_CROWN`, `HOG_PLINTH`
- Original HOG meshes retained: 21
- Verified HOG root count after GLB reload: **1**
- `LABEL_ANCHOR_HANDS_OF_GROWTH` placed at `[-108.0, -79.0, 11.4]`, above the crown and outside the crown geometry.

### Smart Totems

- VIP flagship Smart Totem: **1** (`SMART_TOTEM_VIP_BODY`)
- Campus Smart Totems: **4**

## Validation and visual QA

- Blender: 5.2.2 LTS, local Windows Blender.
- GLB reload validation: **PASS**
- Reloaded object count: 2,227
- Reloaded mesh object count: 2,083
- Reloaded camera count: 55
- Required names missing after reload: `[]`
- Visual QA: **PASS**, six required views rendered and reviewed.
- QA report: `3d/revisions/REV004.1/audit/REV004_1_VISUAL_QA.json`
- Reload report: `3d/revisions/REV004.1/audit/REV004_1_GLTF_RELOAD_INVENTORY.json`
- Regression report: `3d/revisions/REV004.1/audit/REV004_1_REGRESSION_REPORT.json`

QA images:

1. `3d/revisions/REV004.1/qa/QA_01_VIP_ENTRANCE_FRONT.png`
2. `3d/revisions/REV004.1/qa/QA_02_VIP_ENTRANCE_OBLIQUE.png`
3. `3d/revisions/REV004.1/qa/QA_03_FULL_EXTENDED_LIVING_WALL.png`
4. `3d/revisions/REV004.1/qa/QA_04_HANDS_OF_GROWTH_FRONT.png`
5. `3d/revisions/REV004.1/qa/QA_05_HANDS_OF_GROWTH_OBLIQUE.png`
6. `3d/revisions/REV004.1/qa/QA_06_WIDER_PLAZA_SINGLE_HOG.png`

Locked regression checks passed for VIP doors/glazing/portal/canopy, Water Wall, Glass Deck stairs/lift, Production Hall and machinery, solar/façades, roads/logistics/utilities, and landscaping outside the Living Wall backing extension.

## Outputs

- Blend: `3d/revisions/REV004.1/POVU_KENYA_FMCG_CAMPUS_REV004_1_FINAL_ARCHITECTURAL_MASTER.blend`
- GLB: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`
- Final GLB SHA-256: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`
- Manifest: `3d/revisions/REV004.1/REV004_1_ARCHITECTURAL_MANIFEST.json`
- Build audit: `3d/revisions/REV004.1/audit/REV004_1_BUILD_AUDIT.json`
- Source audit: `3d/revisions/REV004.1/audit/REV004_source_semantic_audit.json`

## Pipeline scripts

- `3d/revisions/REV004.1/pipeline/inspect_rev004_source.py`
- `3d/revisions/REV004.1/pipeline/create_rev004_1.py`
- `3d/revisions/REV004.1/pipeline/validate_rev004_1_reload.py`
- `3d/revisions/REV004.1/pipeline/render_rev004_1_qa.py`

## Publication evidence

This log, the REV004.1 blend/GLB, manifest, pipeline scripts, audit JSON, and six QA images are the scoped publication set. Pre-existing untracked REV004 backup/trial files and R02 preview JPGs were not staged.
