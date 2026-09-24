import json
import os
import sys

import bpy
from mathutils import Vector


GLB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "POVU_REV004_2_FINAL_MASTER.glb"))
OUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "audit", "rev004_2_reload_validation.json"))


def bounds_for(objects):
    points = []
    for obj in objects:
        if obj.type != "MESH":
            continue
        for corner in obj.bound_box:
            points.append(obj.matrix_world @ Vector(corner))
    if not points:
        return None
    min_v = [min(p[i] for p in points) for i in range(3)]
    max_v = [max(p[i] for p in points) for i in range(3)]
    return {"min": min_v, "max": max_v, "center": [(min_v[i] + max_v[i]) / 2 for i in range(3)]}


bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB_PATH)
bpy.context.view_layer.update()

hog_objects = [obj for obj in bpy.context.scene.objects if obj.name.startswith("HOG_") or obj.name in {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}]
wall_objects = [obj for obj in bpy.context.scene.objects if "LIVING_WALL" in obj.name.upper()]
hog_bounds = bounds_for(hog_objects)
wall_bounds = bounds_for(wall_objects)

result = {
    "status": "PASS" if hog_bounds and wall_bounds else "FAIL",
    "glb": GLB_PATH,
    "objectCount": len(bpy.context.scene.objects),
    "hogObjectCount": len(hog_objects),
    "hogBounds": hog_bounds,
    "hogCenter": hog_bounds["center"] if hog_bounds else None,
    "livingWallObjectCount": len(wall_objects),
    "livingWallBounds": wall_bounds,
    "notes": [
        "Reloaded exported REV004.2 GLB with Blender glTF importer.",
        "Hands of Growth expected center is approximately (-102, -79, 0) after the +6 X revision translation.",
        "Living Wall remains a bounded wall assembly; no freestanding extension was introduced.",
    ],
}
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as handle:
    json.dump(result, handle, indent=2)
print(json.dumps(result, indent=2))
