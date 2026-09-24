import bpy
import sys
from pathlib import Path
from mathutils import Vector

root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"))
for obj in bpy.data.objects:
    if obj.type == "CAMERA" or obj.name.upper().startswith("PRES_"):
        p = obj.matrix_world.translation
        f = obj.matrix_world.to_quaternion() @ Vector((0, 0, -1)) if obj.type == "CAMERA" else Vector((0, 0, 0))
        print(f"{obj.name}\t{obj.type}\t{tuple(round(v,2) for v in p)}\tforward={tuple(round(v,2) for v in f)}")
