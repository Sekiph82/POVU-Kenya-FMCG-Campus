import bpy
import json
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"

def col():
    return bpy.data.collections.get("REV005_INTERIOR_COMPLETION")

def mat(name):
    return bpy.data.materials.get(name)

def add_box(name, loc, dims, material_name):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    obj = bpy.context.object
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col().objects.link(obj)
    obj.name = name
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat(material_name):
        obj.data.materials.append(mat(material_name))
    obj["revision"] = "REV005"
    obj["rev005_facility"] = "Employee changing / shower / locker support"
    obj["rev005_function"] = "sanitary and changing facility"
    return obj

def main():
    for i, x in enumerate((22, 26, 30, 34, 38)):
        add_box(f"REV005_WELFARE_LOCKER_{i}", (x, -77.2, 2.2), (1.1, 0.45, 1.9), "REV005_Steel")
    for i, x in enumerate((23.5, 28.5, 33.5, 38.5)):
        add_box(f"REV005_WELFARE_SHOWER_{i}", (x, -63.3, 2.1), (1.8, 1.6, 2.0), "REV005_Interior_Partition")
    add_box("REV005_WELFARE_CLEAN_DIRTY_PARTITION", (30, -64.6, 2.0), (20, 0.14, 1.5), "REV005_Interior_Partition")
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)
    print("WELFARE_SUPPORT_ADDED")

if __name__ == "__main__":
    main()
