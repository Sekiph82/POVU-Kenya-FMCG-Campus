import bpy
import sys
from pathlib import Path

root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"))
for obj in bpy.data.objects:
    upper = obj.name.upper()
    if any(token in upper for token in ("HOG", "TREE", "CANOPY", "HANDS_OF_GROWTH", "PRES_01_CAMPUS_HERO", "NAV_TARGET_CAMPUS_AERIAL", "NAV_TARGET_MAIN_ARRIVAL")):
        print(f"{obj.name}\tparent={obj.parent.name if obj.parent else '-'}\tloc={tuple(round(v,2) for v in obj.location)}")
