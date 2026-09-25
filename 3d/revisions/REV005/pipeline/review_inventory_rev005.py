import bpy
import json
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT_DIR = ROOT / "output" / "rev005-owner-interior-review"
OUT = OUT_DIR / "REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

def world_center(obj):
    obj.update_tag()
    bpy.context.view_layer.update()
    corners = [obj.matrix_world @ __import__("mathutils").Vector(corner) for corner in obj.bound_box]
    if not corners:
        return [round(x, 3) for x in obj.location]
    center = sum(corners, __import__("mathutils").Vector()) / len(corners)
    return [round(float(x), 3) for x in center]

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND), load_ui=False)
    interior = bpy.data.collections.get("REV005_INTERIOR_COMPLETION")
    objects = []
    groups = {}
    if interior:
        for obj in sorted(interior.objects, key=lambda item: item.name):
            facility = str(obj.get("rev005_facility", "")).strip()
            record = {
                "name": obj.name,
                "type": obj.type,
                "facility": facility,
                "center": world_center(obj),
                "dimensions": [round(float(v), 3) for v in obj.dimensions],
            }
            objects.append(record)
            if facility:
                groups.setdefault(facility, []).append(obj.name)
    result = {
        "revision": "REV005",
        "source_blend": str(BLEND),
        "collection": "REV005_INTERIOR_COMPLETION",
        "collection_object_count": len(objects),
        "facility_group_count": len(groups),
        "facility_groups": {key: {"object_count": len(value), "objects": value} for key, value in sorted(groups.items())},
        "objects": objects,
        "all_scene_object_count": len(bpy.data.objects),
        "all_scene_camera_count": sum(1 for obj in bpy.data.objects if obj.type == "CAMERA"),
    }
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("collection_object_count", "facility_group_count", "all_scene_object_count", "all_scene_camera_count")}, indent=2))

if __name__ == "__main__":
    main()
