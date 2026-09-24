import bpy
import sys
from pathlib import Path

root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"))
bpy.context.view_layer.update()
for obj in bpy.data.objects:
    upper = obj.name.upper()
    if "GLASS_DECK" in upper or "STAIR" in upper or "LIFT" in upper:
        p = obj.matrix_world.translation
        print(f"{obj.name}\t{obj.type}\t{tuple(round(v,2) for v in p)}")
