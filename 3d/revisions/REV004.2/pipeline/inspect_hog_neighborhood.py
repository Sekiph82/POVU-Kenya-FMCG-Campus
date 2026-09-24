import bpy
import json
from mathutils import Vector

OUT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\revisions\REV004.2\audit\hog_neighborhood.json"

def bounds(obj):
    if not hasattr(obj, "bound_box"):
        return None
    pts = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return {"min": [round(v, 3) for v in lo], "max": [round(v, 3) for v in hi], "center": [round(v, 3) for v in (lo + hi) / 2], "size": [round(v, 3) for v in hi - lo]}

items = []
for obj in bpy.data.objects:
    b = bounds(obj)
    if not b or obj.type not in {"MESH", "EMPTY"}:
        continue
    c = b["center"]
    if -145 <= c[0] <= -75 and -125 <= c[1] <= -45:
        items.append({"name": obj.name, "type": obj.type, "center": c, "bounds": b, "parent": obj.parent.name if obj.parent else None, "role": obj.get("role"), "category": obj.get("category")})
items.sort(key=lambda x: (x["center"][1], x["center"][0], x["name"]))
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)
print("WROTE", OUT, "ITEMS", len(items))
