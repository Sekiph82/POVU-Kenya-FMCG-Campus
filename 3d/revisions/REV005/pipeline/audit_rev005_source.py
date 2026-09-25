import bpy
import json
import os
from mathutils import Vector

ROOT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo"
SOURCE = os.path.join(ROOT, "3d", "revisions", "REV004.2", "POVU_Kenya_FMCG_CAMPUS_REV004_2_FINAL_ARCHITECTURAL_MASTER.blend")
OUT = os.path.join(ROOT, "3d", "revisions", "REV005", "audit", "REV005_INTERIOR_AUDIT.json")

def bounds(obj):
    if not hasattr(obj, "bound_box") or not obj.bound_box:
        return None
    pts = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return {"min": [round(float(v), 3) for v in lo], "max": [round(float(v), 3) for v in hi], "size": [round(float(v), 3) for v in hi - lo], "center": [round(float(v), 3) for v in (lo + hi) / 2]}

def item(obj):
    return {"name": obj.name, "type": obj.type, "parent": obj.parent.name if obj.parent else None, "bounds": bounds(obj), "role": obj.get("role"), "category": obj.get("category"), "semantic_id": obj.get("rev004_semantic_id")}

TERMS = ("ADMIN", "HQ", "R_D", "QC", "ACADEMY", "TRAIN", "RESTAURANT", "CAFE", "DAYCARE", "CLINIC", "WELLNESS", "LOCKER", "SHOWER", "PRODUCTION", "PROCESS", "MIX", "FILL", "PACK", "WAREHOUSE", "RAW", "RM_", "FG_", "DISPATCH", "WIPES", "POWDER", "TOOTHPASTE", "PLASTIC", "BLOW", "INJECTION", "UTILITY", "ETP", "RO_", "BOILER", "COMPRESS", "GENERATOR", "MAINT", "WORKSHOP", "MUSTER", "SECURITY", "RECEPTION", "GLASS_DECK", "HANDS", "LIVING_WALL", "TREE")

all_items = [item(o) for o in sorted(bpy.data.objects, key=lambda x: x.name.lower()) if o.type in {"MESH", "EMPTY", "CAMERA"}]
term_items = [x for x in all_items if any(t in x["name"].upper() for t in TERMS)]

large = []
facility_candidates = []
for x in all_items:
    b = x.get("bounds")
    if not b:
        continue
    sx, sy, sz = b["size"]
    if x["type"] == "MESH" and sx >= 12 and sy >= 10 and sz >= 3:
        large.append(x)
    if x["type"] == "MESH" and sx >= 6 and sy >= 6 and sz >= 2.5:
        facility_candidates.append(x)

data = {
    "revision": "REV005",
    "source_revision": "REV004.2",
    "source_blend": SOURCE,
    "source_scene": bpy.data.filepath,
    "object_count": len(bpy.data.objects),
    "mesh_object_count": sum(1 for o in bpy.data.objects if o.type == "MESH"),
    "material_count": len(bpy.data.materials),
    "camera_count": sum(1 for o in bpy.data.objects if o.type == "CAMERA"),
    "large_mesh_candidates": large,
    "facility_mesh_candidates": facility_candidates,
    "program_term_inventory": term_items,
    "all_object_names": sorted(o.name for o in bpy.data.objects),
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print(json.dumps({k: data[k] for k in ("revision", "source_revision", "object_count", "mesh_object_count", "material_count", "camera_count")}, indent=2))
print("LARGE_MESH_CANDIDATES", len(large))
for x in large:
    print(x["name"], x["bounds"]["size"], x["bounds"]["center"])
print("PROGRAM_TERM_ITEMS", len(term_items))
print("WROTE", OUT)
