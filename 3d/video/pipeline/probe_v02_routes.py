import argparse
import json
import os
import sys

import bpy
from mathutils import Vector


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def bbox(obj):
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    mins = [min(p[i] for p in points) for i in range(3)]
    maxs = [max(p[i] for p in points) for i in range(3)]
    return {"min": mins, "max": maxs, "center": [(a + b) / 2 for a, b in zip(mins, maxs)], "dimensions": [b - a for a, b in zip(mins, maxs)]}


def obj_record(obj):
    return {"name": obj.name, "type": obj.type, "location": list(obj.matrix_world.translation), "bbox": bbox(obj), "materials": [slot.material.name for slot in obj.material_slots if slot.material]}


def cam_record(obj):
    return {"name": obj.name, "location": list(obj.matrix_world.translation), "rotation_euler": list(obj.matrix_world.to_euler()), "lens": obj.data.lens, "sensor_width": obj.data.sensor_width, "clip_start": obj.data.clip_start, "clip_end": obj.data.clip_end}


def main():
    a = args()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=os.path.abspath(a.source))
    camera_names = [
        "PRES_15_MIXING_HALL", "QA_LANDMARK_CAMERA", "PRES_02_VIP_APPROACH", "PRES_04_POVU_PLAZA",
        "PRES_13_VIP_HERO", "PRES_16_GLASS_DECK_INTERIOR", "PRES_44_REFINED_VIP", "PRES_45_REFINED_PRODUCTION", "PRES_46_REFINED_GLASSDECK",
    ]
    object_names = [
        "HOG_PALM_L", "HOG_PALM_R", "HOG_TREE_TRUNK", "HOG_PLINTH", "POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER",
        "MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR", "GlassDeck_East", "GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_EAST_TIMBER_FLOOR",
        "GLASS_DECK_LINK", "GLASS_DECK_LINK_FLOOR", "POVU_PLAZA", "LIVING_WALL_PANEL", "POVU_VIP_SIGN", "POVU_PRODUCTION_SIGN",
        "Organic_Canopy", "POVU_CANOPY_LIGHT_RING",
    ] + [f"ProcessTank_{i:02d}" for i in range(1, 12)]
    for name in bpy.data.objects.keys():
        if name.startswith("HOG_FINGER_") or name.startswith("HOG_TREE_CROWN_"):
            object_names.append(name)
    report = {
        "cameras": {name: cam_record(bpy.data.objects[name]) for name in camera_names if name in bpy.data.objects and bpy.data.objects[name].type == "CAMERA"},
        "objects": {name: obj_record(bpy.data.objects[name]) for name in sorted(set(object_names)) if name in bpy.data.objects},
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.report)), exist_ok=True)
    with open(a.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(json.dumps({"camera_count": len(report["cameras"]), "object_count": len(report["objects"])}))


if __name__ == "__main__":
    main()
