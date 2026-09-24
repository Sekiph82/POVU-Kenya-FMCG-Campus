import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter
from mathutils import Vector

import bpy


KEYWORDS = {
    "entrance": ["entrance", "entry", "door", "gate", "lobby", "arrival", "security"],
    "vip": ["vip", "water", "living", "totem", "hands", "hog", "plaza"],
    "glass_deck": ["glass", "deck", "stair", "lift", "mezz", "sky"],
    "production": ["production", "process", "tank", "mix", "fill", "pack", "pallet", "conveyor"],
    "logistics": ["warehouse", "receiv", "dispatch", "truck", "loading", "dock", "raw", "finished"],
    "solar": ["solar", "pv", "panel", "inverter"],
    "landscape": ["tree", "foliage", "grass", "garden", "canopy", "landscape", "shrub", "plant"],
    "safety": ["fire", "emergency", "egress", "muster", "bollard", "pedestrian", "crossing"],
}


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def world_bbox(obj):
    if not hasattr(obj, "bound_box") or not obj.bound_box:
        return None
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    lo = [min(p[i] for p in points) for i in range(3)]
    hi = [max(p[i] for p in points) for i in range(3)]
    return {"min": [round(v, 4) for v in lo], "max": [round(v, 4) for v in hi]}


def semantic_hits(name):
    low = name.lower()
    return [group for group, terms in KEYWORDS.items() if any(term in low for term in terms)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    args = parser.parse_args(argv)

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=os.path.abspath(args.input))

    objects = []
    groups = Counter()
    for obj in sorted(bpy.context.scene.objects, key=lambda o: o.name.lower()):
        groups[obj.type] += 1
        objects.append({
            "name": obj.name,
            "type": obj.type,
            "parent": obj.parent.name if obj.parent else None,
            "location": [round(v, 4) for v in obj.matrix_world.translation],
            "dimensions": [round(v, 4) for v in obj.dimensions],
            "bounds": world_bbox(obj),
            "visible": not obj.hide_get() and not obj.hide_render,
            "materials": [slot.material.name for slot in getattr(obj, "material_slots", []) if slot.material],
            "semantic_groups": semantic_hits(obj.name),
        })

    meshes = [m for m in bpy.data.meshes]
    materials = [m for m in bpy.data.materials]
    cameras = [o.name for o in bpy.data.objects if o.type == "CAMERA"]
    payload = {
        "input": os.path.abspath(args.input),
        "source_sha256": digest(args.input),
        "blender_version": bpy.app.version_string,
        "scene_name": bpy.context.scene.name,
        "object_count": len(bpy.data.objects),
        "mesh_object_count": sum(1 for o in bpy.data.objects if o.type == "MESH"),
        "mesh_data_count": len(meshes),
        "material_count": len(materials),
        "camera_count": len(cameras),
        "light_count": sum(1 for o in bpy.data.objects if o.type == "LIGHT"),
        "objects_by_type": dict(groups),
        "camera_names": cameras,
        "material_names": sorted(m.name for m in materials),
        "object_names": [o["name"] for o in objects],
        "keyword_hits": {
            group: [o["name"] for o in objects if group in o["semantic_groups"]]
            for group in KEYWORDS
        },
        "objects": objects,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")
    print(json.dumps({k: payload[k] for k in ("source_sha256", "blender_version", "object_count", "mesh_object_count", "material_count", "camera_count", "light_count")}))


if __name__ == "__main__":
    main()
