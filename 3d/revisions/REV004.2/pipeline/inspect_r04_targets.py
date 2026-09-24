import bpy
import json
from mathutils import Vector

OUT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\revisions\REV004.2\audit\r04_target_catalog.json"
TERMS = ("SOLAR", "PRES_", "NAV_TARGET", "ADMIN", "R_D_QC", "TRAIN", "ACADEMY", "MULTI", "EXPERIENCE", "STUDIO", "RESTAURANT", "CAFE", "WELLNESS", "RECREATION", "DAYCARE", "CLINIC", "VIP", "HOG", "HANDS", "LIVING", "WATER", "GLASS_DECK", "PRODUCTION", "RM_", "RAW", "CHEMICAL", "IBC", "PROCESS", "TANK", "MIX", "FILL", "BOTTLE", "CAPPER", "CAP_", "CAPS", "TRIGGER", "CLOSURE", "SACHET", "LIQUID", "POWDER", "TOOTHPASTE", "WIPES", "PACK", "ROBOT", "PALLET", "AMR", "FG_", "DISPATCH", "DOCK", "ETP", "UTILITY", "AIR_", "COMPRESS", "FIRE", "MUSTER", "SMART_TOTEM", "GARDEN", "CANOPY", "POND", "BENCH", "MES")

def bounds(obj):
    if not hasattr(obj, "bound_box"):
        return None
    pts = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    if not pts:
        return None
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return {"min": [round(float(v), 3) for v in lo], "max": [round(float(v), 3) for v in hi], "center": [round(float(v), 3) for v in (lo + hi) / 2]}

items = []
for obj in sorted(bpy.data.objects, key=lambda o: o.name.lower()):
    upper = obj.name.upper()
    if not any(term in upper for term in TERMS):
        continue
    items.append({"name": obj.name, "type": obj.type, "world": [round(float(v), 3) for v in obj.matrix_world.translation], "bounds": bounds(obj), "parent": obj.parent.name if obj.parent else None, "role": obj.get("role"), "category": obj.get("category")})
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"source": bpy.data.filepath, "count": len(items), "items": items}, f, indent=2)
print("WROTE", OUT, "ITEMS", len(items))
