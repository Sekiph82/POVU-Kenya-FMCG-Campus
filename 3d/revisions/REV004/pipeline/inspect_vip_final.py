import bpy
from mathutils import Vector

bpy.ops.wm.open_mainfile(filepath=r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\revisions\REV004\POVU_KENYA_FMCG_CAMPUS_REV004_FINAL_ARCHITECTURAL_MASTER.blend")
for obj in sorted(bpy.context.scene.objects, key=lambda item: item.name):
    if obj.type != "MESH" or not obj.bound_box:
        continue
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    lo = [min(p[i] for p in points) for i in range(3)]
    hi = [max(p[i] for p in points) for i in range(3)]
    if hi[1] >= -96 and lo[1] <= -89 and hi[0] >= -90 and lo[0] <= -35 and hi[2] >= 1.1 and lo[2] <= 10:
        mats = ",".join(slot.material.name for slot in obj.material_slots if slot.material)
        print(obj.name, "bounds", [round(v, 1) for v in lo], [round(v, 1) for v in hi], "mats", mats, "hidden", obj.hide_render)
