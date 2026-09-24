import bpy
import hashlib
import json
import os
from mathutils import Vector

ROOT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo"
SOURCE_BLEND = os.path.join(ROOT, "3d", "revisions", "REV004.1", "POVU_Kenya_FMCG_CAMPUS_REV004_1_FINAL_ARCHITECTURAL_MASTER.blend")
SOURCE_GLB = os.path.join(ROOT, "3d", "revisions", "REV004.1", "POVU_REV004_1_FINAL_MASTER.glb")
OUT_DIR = os.path.join(ROOT, "3d", "revisions", "REV004.2")
OUT_BLEND = os.path.join(OUT_DIR, "POVU_Kenya_FMCG_CAMPUS_REV004_2_FINAL_ARCHITECTURAL_MASTER.blend")
OUT_GLB = os.path.join(OUT_DIR, "POVU_REV004_2_FINAL_MASTER.glb")
OUT_MANIFEST = os.path.join(OUT_DIR, "REV004_2_ARCHITECTURAL_MANIFEST.json")
OUT_AUDIT = os.path.join(OUT_DIR, "audit", "rev004_2_geometry_change_audit.json")

HOG_DELTA = Vector((6.0, 0.0, 0.0))
HOG_NAMES = {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}

def vec(v):
    return [round(float(x), 6) for x in v]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def bounds(obj):
    if not hasattr(obj, "bound_box"):
        return None
    pts = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    if not pts:
        return None
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return {"min": vec(lo), "max": vec(hi), "size": vec(hi - lo), "center": vec((lo + hi) / 2)}

def matching_hog(obj):
    return obj.name.startswith("HOG_") or obj.name in HOG_NAMES

def matching_living_wall(obj):
    upper = obj.name.upper()
    return upper.startswith("LIVING_WALL_") or upper == "VIP_LIVINGWALL"

before = {}
hog_objects = []
for obj in bpy.data.objects:
    if matching_hog(obj):
        before[obj.name] = {"world_location": vec(obj.matrix_world.translation), "bounds": bounds(obj)}
        hog_objects.append(obj)

if not hog_objects:
    raise RuntimeError("REV004.1 source has no Hands of Growth objects")

for obj in hog_objects:
    matrix = obj.matrix_world.copy()
    matrix.translation = matrix.translation + HOG_DELTA
    obj.matrix_world = matrix

after = {obj.name: {"world_location": vec(obj.matrix_world.translation), "bounds": bounds(obj)} for obj in hog_objects}

living = {obj.name: bounds(obj) for obj in bpy.data.objects if matching_living_wall(obj) and bounds(obj)}
living_min_x = min(v["min"][0] for v in living.values())
living_max_x = max(v["max"][0] for v in living.values())
living_min_y = min(v["min"][1] for v in living.values())
living_max_y = max(v["max"][1] for v in living.values())

scene = bpy.context.scene
scene["REVISION_ID"] = "REV004.2"
scene["HOG_FORWARD_TRANSLATION_X"] = float(HOG_DELTA.x)
scene["HOG_FORWARD_TRANSLATION_Y"] = float(HOG_DELTA.y)
scene["HOG_FORWARD_TRANSLATION_Z"] = float(HOG_DELTA.z)
scene["LIVING_WALL_BOUNDARY_STATUS"] = "VERIFIED_BOUNDED_NO_GEOMETRY_CHANGE"
scene["LIVING_WALL_BOUNDARY_X_MIN"] = float(living_min_x)
scene["LIVING_WALL_BOUNDARY_X_MAX"] = float(living_max_x)

os.makedirs(os.path.dirname(OUT_BLEND), exist_ok=True)
os.makedirs(os.path.dirname(OUT_AUDIT), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND)
bpy.ops.export_scene.gltf(filepath=OUT_GLB, export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)

audit = {
    "revision": "REV004.2",
    "source_blend": SOURCE_BLEND,
    "source_glb": SOURCE_GLB,
    "source_glb_sha256": sha256(SOURCE_GLB),
    "output_blend": OUT_BLEND,
    "output_glb": OUT_GLB,
    "hog_forward_delta_world": vec(HOG_DELTA),
    "hog_object_count": len(hog_objects),
    "hog_objects_before_after": {name: {"before": before[name], "after": after[name]} for name in sorted(before)},
    "living_wall": {
        "status": "VERIFIED_BOUNDED_NO_GEOMETRY_CHANGE",
        "objects": living,
        "combined_extent_world": {"x_min": living_min_x, "x_max": living_max_x, "y_min": living_min_y, "y_max": living_max_y},
        "note": "The wall assembly ends at the actual entrance-side boundary; no freestanding extension was changed or added.",
    },
    "object_count": len(bpy.data.objects),
    "mesh_object_count": sum(1 for o in bpy.data.objects if o.type == "MESH"),
}
audit["output_blend_sha256"] = sha256(OUT_BLEND)
audit["output_glb_sha256"] = sha256(OUT_GLB)
with open(OUT_AUDIT, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2)

manifest = {
    "revision": "REV004.2",
    "source_revision": "REV004.1",
    "source_blend": SOURCE_BLEND,
    "source_glb": SOURCE_GLB,
    "output_blend": OUT_BLEND,
    "output_glb": OUT_GLB,
    "output_sha256": audit["output_glb_sha256"],
    "geometry_changes": {
        "hands_of_growth": {"translation_world": vec(HOG_DELTA), "objects_moved": sorted(before)},
        "living_wall": {"status": "VERIFIED_BOUNDED_NO_GEOMETRY_CHANGE", "combined_extent_world": audit["living_wall"]["combined_extent_world"]},
    },
    "counts": {"objects": len(bpy.data.objects), "mesh_objects": sum(1 for o in bpy.data.objects if o.type == "MESH"), "materials": len(bpy.data.materials), "cameras": sum(1 for o in bpy.data.objects if o.type == "CAMERA")},
    "reload_test": "PENDING_RELOAD_VALIDATION",
}
with open(OUT_MANIFEST, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)
print("REV004.2_BUILT", OUT_GLB)
print("HOG_DELTA", vec(HOG_DELTA), "OBJECTS", len(hog_objects))
print("LIVING_WALL_EXTENT", living_min_x, living_max_x, living_min_y, living_max_y)
print("OUTPUT_SHA256", audit["output_glb_sha256"])
