import bpy
import json
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
DIAG = OUT / "V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.json"

def bounds(obj):
    points = [obj.matrix_world @ Vector(p) for p in obj.bound_box]
    lo = Vector((min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)))
    hi = Vector((max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)))
    return lo, hi

def main():
    diag = json.loads(DIAG.read_text(encoding="utf-8"))
    names = sorted({pair["proxy"] for row in diag["groups"] for pair in row["proxy_containment_pairs"]})
    rows = []
    for name in names:
        obj = bpy.data.objects.get(name)
        if not obj:
            continue
        lo, hi = bounds(obj)
        ext = hi - lo
        rows.append({
            "name": obj.name,
            "facility": obj.get("facility"),
            "type": obj.type,
            "dimensions": [round(float(v), 3) for v in ext],
            "location": [round(float(v), 3) for v in obj.matrix_world.translation],
            "hide_render": obj.hide_render,
            "hide_viewport": obj.hide_viewport,
            "collections": [c.name for c in obj.users_collection],
        })
    rows.sort(key=lambda r: (str(r["facility"]), r["name"]))
    (OUT / "V07_PROXY_CANDIDATES.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(json.dumps(rows, indent=2))

main()
