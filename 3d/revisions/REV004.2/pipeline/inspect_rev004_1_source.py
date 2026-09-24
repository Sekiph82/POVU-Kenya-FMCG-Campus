import bpy
import json
import sys
from mathutils import Vector

OUT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\revisions\REV004.2\audit\rev004_1_hog_livingwall_source.json"

KEYS = ("HOG", "HAND", "GROWTH", "LIVINGWALL", "LIVING_WALL", "VIP_LIVING", "WATERWALL", "WATER_WALL", "ENTRANCE")

def vec(v):
    return [round(float(x), 6) for x in v]

def bounds_world(obj):
    if not hasattr(obj, "bound_box"):
        return None
    pts = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    if not pts:
        return None
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return {"min": vec(lo), "max": vec(hi), "size": vec(hi - lo), "center": vec((lo + hi) / 2)}

def obj_record(obj):
    props = {}
    for k in obj.keys():
        if k == "_RNA_UI":
            continue
        value = obj[k]
        try:
            json.dumps(value)
            props[k] = value
        except TypeError:
            props[k] = str(value)
    return {
        "name": obj.name,
        "type": obj.type,
        "parent": obj.parent.name if obj.parent else None,
        "collection_names": [c.name for c in obj.users_collection],
        "location_local": vec(obj.location),
        "location_world": vec(obj.matrix_world.translation),
        "rotation_euler": vec(obj.rotation_euler),
        "dimensions_local": vec(obj.dimensions),
        "bounds_world": bounds_world(obj),
        "children": sorted(c.name for c in obj.children),
        "custom_properties": props,
        "hide_viewport": bool(obj.hide_viewport),
        "hide_render": bool(obj.hide_render),
    }

records = []
for obj in sorted(bpy.data.objects, key=lambda o: o.name.lower()):
    upper = obj.name.upper()
    if any(key in upper for key in KEYS):
        records.append(obj_record(obj))

collections = []
for col in sorted(bpy.data.collections, key=lambda c: c.name.lower()):
    names = [o.name for o in col.objects if any(key in o.name.upper() for key in KEYS)]
    if names:
        collections.append({"name": col.name, "matching_objects": sorted(names)})

anchors = []
for obj in sorted(bpy.data.objects, key=lambda o: o.name.lower()):
    if obj.type == "EMPTY" and ("PRES_" in obj.name.upper() or "NAV_" in obj.name.upper()):
        anchors.append(obj_record(obj))

payload = {
    "source_file": bpy.data.filepath,
    "scene_names": [s.name for s in bpy.data.scenes],
    "object_count": len(bpy.data.objects),
    "matching_object_count": len(records),
    "matching_objects": records,
    "matching_collections": collections,
    "camera_and_navigation_anchors": anchors,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
print("WROTE", OUT)
print("MATCHING", len(records), "ANCHORS", len(anchors))
