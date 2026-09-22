import argparse
import hashlib
import json
import os
import sys
from collections import Counter

import bpy
from mathutils import Vector


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def bbox(obj):
    if obj.type != "MESH" or not obj.bound_box:
        return None
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    mins = [min(point[i] for point in corners) for i in range(3)]
    maxs = [max(point[i] for point in corners) for i in range(3)]
    return {"min": mins, "max": maxs, "center": [(a + b) / 2 for a, b in zip(mins, maxs)]}


def record(obj):
    return {
        "name": obj.name,
        "type": obj.type,
        "collection": obj.users_collection[0].name if obj.users_collection else None,
        "parent": obj.parent.name if obj.parent else None,
        "location_world": list(obj.matrix_world.translation),
        "dimensions_world": list(obj.dimensions),
        "bbox_world": bbox(obj),
        "materials": [slot.name if slot else None for slot in getattr(obj.data, "materials", [])],
        "hide_viewport": obj.hide_viewport,
        "hide_render": obj.hide_render,
    }


def main():
    a = args()
    source = os.path.abspath(a.source)
    with open(source, "rb") as handle:
        source_sha = hashlib.sha256(handle.read()).hexdigest()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    objects = [record(obj) for obj in bpy.context.scene.objects]
    materials = sorted({material for obj in objects for material in obj["materials"] if material})
    collections = sorted({obj["collection"] for obj in objects if obj["collection"]})
    report = {
        "source": source,
        "source_sha256": source_sha,
        "object_count": len(objects),
        "object_type_counts": dict(Counter(obj["type"] for obj in objects)),
        "material_count": len(materials),
        "materials": materials,
        "collections": collections,
        "objects": objects,
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.report)), exist_ok=True)
    with open(a.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(json.dumps({"source_sha256": source_sha, "object_count": len(objects), "materials": len(materials), "collections": len(collections)}))


if __name__ == "__main__":
    main()
