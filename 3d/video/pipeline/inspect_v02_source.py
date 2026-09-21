import argparse
import hashlib
import json
import os
import sys
from collections import Counter

import bpy
from mathutils import Vector


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def world_bbox(obj):
    if not obj.bound_box:
        return None
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    mins = [min(point[i] for point in corners) for i in range(3)]
    maxs = [max(point[i] for point in corners) for i in range(3)]
    return {"min": mins, "max": maxs, "center": [(a + b) / 2 for a, b in zip(mins, maxs)]}


def object_record(obj):
    materials = []
    if hasattr(obj.data, "materials"):
        materials = [slot.name if slot else None for slot in obj.data.materials]
    record = {
        "name": obj.name,
        "type": obj.type,
        "collection": obj.users_collection[0].name if obj.users_collection else None,
        "parent": obj.parent.name if obj.parent else None,
        "location_world": list(obj.matrix_world.translation),
        "bbox_world": world_bbox(obj),
        "dimensions_world": list(obj.dimensions),
        "materials": materials,
        "visible_viewport": not obj.hide_viewport,
        "visible_render": not obj.hide_render,
    }
    return record


def main():
    args = parse_args()
    source = os.path.abspath(args.source)
    with open(source, "rb") as handle:
        source_bytes = handle.read()
    source_hash = hashlib.sha256(source_bytes).hexdigest()

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    objects = list(bpy.context.scene.objects)
    names = [obj.name for obj in objects]
    mesh_objects = [obj for obj in objects if obj.type == "MESH"]
    cameras = [obj for obj in objects if obj.type == "CAMERA"]
    materials = sorted({slot.name for obj in mesh_objects for slot in obj.data.materials if slot})

    required_exact = [
        "HOG_PALM_L", "HOG_PALM_R", "HOG_TREE_TRUNK", "HOG_PLINTH",
        "POVU_WATER_WALL_7M", "QA_LANDMARK_CAMERA", "PRES_15_MIXING_HALL",
        "MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR",
    ] + [f"ProcessTank_{i:02d}" for i in range(1, 12)]
    required_patterns = {
        "HOG_FINGER_*": "HOG_FINGER_",
        "HOG_TREE_CROWN_*": "HOG_TREE_CROWN_",
        "HOG_FOREARM_L": "HOG_FOREARM_L",
        "HOG_FOREARM_R": "HOG_FOREARM_R",
    }
    exact_results = {name: name in names for name in required_exact}
    pattern_results = {pattern: sorted(name for name in names if name.startswith(prefix)) for pattern, prefix in required_patterns.items()}
    related = sorted(
        name for name in names
        if any(token in name.upper() for token in (
            "GLASS", "DECK", "VIP", "PLAZA", "LIVING", "WATER", "CANOPY", "SIGN", "LANDSCAPE", "PRODUCTION"
        ))
    )
    inventory_names = sorted(set(required_exact + [name for values in pattern_results.values() for name in values]))
    inventory = {name: object_record(bpy.data.objects[name]) for name in inventory_names if name in bpy.data.objects}
    report = {
        "source_path": source,
        "file_size_bytes": len(source_bytes),
        "sha256": source_hash,
        "format": "GLB imported by Blender",
        "object_count": len(objects),
        "mesh_count": len(mesh_objects),
        "material_count": len(materials),
        "camera_count": len(cameras),
        "object_type_counts": dict(Counter(obj.type for obj in objects)),
        "required_exact": exact_results,
        "required_patterns": pattern_results,
        "all_required_present": all(exact_results.values()) and all(pattern_results.values()),
        "related_scene_objects": related,
        "semantic_inventory": inventory,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(json.dumps({
        "sha256": source_hash,
        "object_count": len(objects),
        "mesh_count": len(mesh_objects),
        "material_count": len(materials),
        "camera_count": len(cameras),
        "all_required_present": report["all_required_present"],
    }))


if __name__ == "__main__":
    main()
