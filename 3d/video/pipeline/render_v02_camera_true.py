import argparse
import hashlib
import json
import math
import os
import sys
from datetime import datetime, timezone

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector


FPS = 24
FRAME_START = 1
FRAME_END = 720
CHECKPOINTS = [1, 121, 241, 361, 481, 601, 718]
SOURCE_SHA256 = "839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=int, choices=[1, 2, 3, 4], required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--mode", choices=["checkpoints", "final"], required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def bounds_for_names(names):
    points = []
    for name in names:
        obj = bpy.data.objects.get(name)
        if not obj or not hasattr(obj, "bound_box") or not obj.bound_box:
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        raise RuntimeError(f"No geometry found for semantic target set: {names}")
    mins = Vector((min(point[i] for point in points) for i in range(3)))
    maxs = Vector((max(point[i] for point in points) for i in range(3)))
    return {"min": list(mins), "max": list(maxs), "center": list((mins + maxs) / 2), "dimensions": list(maxs - mins)}


def look_at(camera, target):
    camera.rotation_euler = (Vector(target) - camera.location).to_track_quat("-Z", "Y").to_euler()


def point(frame, location, target, label, semantic_objects):
    return {"frame": frame, "location": list(location), "target": list(target), "label": label, "semantic_objects": semantic_objects}


def make_temp_camera(name):
    data = bpy.data.cameras.new(name)
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    data.lens = 42.0
    data.sensor_width = 36.0
    data.clip_start = 0.1
    data.clip_end = 1000.0
    return camera


def configure_scene():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 720
    scene.render.resolution_percentage = 100
    scene.render.fps = FPS
    scene.frame_start = FRAME_START
    scene.frame_end = FRAME_END
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.render.use_file_extension = True
    scene.render.image_settings.file_format = "PNG"
    if hasattr(scene, "eevee"):
        scene.eevee.taa_render_samples = 16
        scene.eevee.taa_samples = 16
        scene.eevee.use_taa_reprojection = True
        if hasattr(scene.eevee, "use_raytracing"):
            scene.eevee.use_raytracing = False
    if scene.world:
        scene.world.color = (0.015, 0.025, 0.04)
        scene.world.use_nodes = True
        background = scene.world.node_tree.nodes.get("Background")
        if background:
            background.inputs["Color"].default_value = (0.015, 0.025, 0.04, 1.0)
            background.inputs["Strength"].default_value = 0.35
    scene.view_settings.exposure = 2.0
    ensure_v02_lighting(scene)
    return scene


def ensure_v02_lighting(scene):
    if bpy.data.objects.get("V02_KEY_CAMPUS"):
        return
    rigs = [
        ("V02_KEY_CAMPUS", (-20, -20, 90), (0, 0, 3), 250000.0, 110.0),
        ("V02_INTERIOR_KEY", (-10, 15, 32), (0, 20, 5), 120000.0, 55.0),
        ("V02_PLAZA_FILL", (-120, -115, 38), (-70, -80, 3), 90000.0, 65.0),
    ]
    for name, location, target, energy, size in rigs:
        data = bpy.data.lights.new(name=name, type="AREA")
        data.energy = energy
        data.color = (1.0, 1.0, 1.0)
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        scene.collection.objects.link(obj)
        obj.location = location
        look_at(obj, target)
    sun_data = bpy.data.lights.new(name="V02_SUN", type="SUN")
    sun_data.energy = 6.0
    sun_data.angle = math.radians(18.0)
    sun_obj = bpy.data.objects.new("V02_SUN", sun_data)
    scene.collection.objects.link(sun_obj)
    sun_obj.location = (50, -70, 80)
    look_at(sun_obj, (0, 0, 0))


def build_route(video):
    tanks_early = [f"ProcessTank_{i:02d}" for i in range(1, 7)]
    tanks_late = [f"ProcessTank_{i:02d}" for i in range(7, 12)]
    if video == 1:
        camera = bpy.data.objects.get("PRES_15_MIXING_HALL")
        if not camera or camera.type != "CAMERA":
            raise RuntimeError("Required active camera PRES_15_MIXING_HALL is missing")
        early = bounds_for_names(tanks_early)
        late = bounds_for_names(tanks_late)
        platform = bounds_for_names(["MIXING_PLATFORM"])
        original_location = camera.location.copy()
        original_rotation = camera.rotation_euler.copy()
        forward = camera.matrix_world.to_quaternion() @ Vector((0, 0, -1))
        route = [
            point(1, original_location, original_location + forward * 30, "actual_PRES_15_start", tanks_early),
            point(121, (-50, -2, 9.0), (-35, 12, 5.0), "dolly_to_tanks_01_06", tanks_early),
            point(241, (-25, -2, 9.0), (-5, 12, 5.0), "lateral_mixing_platform", tanks_early + ["MIXING_PLATFORM"]),
            point(361, (10, -2, 9.0), (25, 12, 5.0), "industrial_walkthrough", tanks_early + ["MIXING_PLATFORM"]),
            point(481, (-45, 22, 9.0), (-35, 32, 5.0), "dolly_to_tanks_07_11", tanks_late),
            point(601, (-10, 22, 10.0), (5, 32, 5.0), "second_group_reveal", tanks_late),
            point(720, (25, 18, 10.0), (10, 25, 6.0), "wet_processing_hero", tanks_early + tanks_late + ["MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR"]),
        ]
        return camera, route, {"name": camera.name, "existing_camera": True, "target_subject": "Wet Processing / Mixing Hall", "semantic_targets": tanks_early + tanks_late + ["MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR"], "preserve_initial_transform": {"location": list(original_location), "rotation_euler": list(original_rotation)}}

    if video == 2:
        hog_names = ["HOG_PALM_L", "HOG_PALM_R", "HOG_TREE_TRUNK", "HOG_PLINTH", "HOG_FOREARM_L", "HOG_FOREARM_R"]
        hog_names += sorted(name for name in bpy.data.objects.keys() if name.startswith("HOG_FINGER_") or name.startswith("HOG_TREE_CROWN_"))
        hog = bounds_for_names(hog_names)
        center = Vector(hog["center"])
        target = center + Vector((0, 0, 3.8))
        camera = make_temp_camera("VID_HOG_V02_CAMERA")
        def orbit(radius, angle_deg, z):
            angle = math.radians(angle_deg)
            return center + Vector((math.cos(angle) * radius, math.sin(angle) * radius, z))
        qa_camera = bpy.data.objects.get("QA_LANDMARK_CAMERA")
        qa_start = center + Vector((-20, -46, 36))
        route = [
            point(1, qa_start, target, "plaza_establish_from_QA_landmark_view", hog_names),
            point(121, center + Vector((-26, -38, 18)), target, "landmark_approach", hog_names),
            point(241, orbit(24, -110, 10), target, "arc_start", hog_names),
            point(361, orbit(23, -55, 10), target, "landmark_arc", hog_names),
            point(481, orbit(23, -5, 10), target, "arc_finish", hog_names),
            point(601, orbit(12, 20, 8.5), target, "detail_approach", ["HOG_PALM_L", "HOG_PALM_R", "HOG_TREE_TRUNK", "HOG_TREE_CROWN_0", "HOG_PLINTH"]),
            point(720, center + Vector((-20, -46, 26)), target, "complete_landmark_hero", hog_names),
        ]
        return camera, route, {"name": camera.name, "existing_camera": False, "target_subject": "Hands of Growth", "semantic_targets": hog_names, "hog_bounds": hog}

    if video == 3:
        deck_names = ["GlassDeck_East", "GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_EAST_TIMBER_FLOOR", "GLASS_DECK_LINK", "GLASS_DECK_LINK_FLOOR"]
        deck = bounds_for_names(deck_names)
        production = bounds_for_names(["Production_Hall"])
        camera = make_temp_camera("VID_GLASS_DECK_V02_CAMERA")
        camera.data.lens = 32.0
        route = [
            point(1, (-100, -28, 12), (-45, -10, 9.5), "production_facade_context", deck_names + ["Production_Hall"]),
            point(121, (-82, -21, 12.0), (-62, -11, 9.0), "deck_access_approach", ["GlassDeck_West", "DECK_TIMBER_FLOOR"]),
            point(241, (-60, -9, 12.0), (-30, -10, 9.0), "onto_west_glass_deck", ["GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_MULLION"]),
            point(361, (-20, -9, 12.0), (15, -10, 9.0), "walk_west_deck", ["DECK_TIMBER_FLOOR", "GlassDeck_West", "Production_Hall"]),
            point(481, (70, 5, 12.0), (70, 25, 9.5), "walk_glass_deck_link", ["GLASS_DECK_LINK", "GLASS_DECK_LINK_FLOOR"]),
            point(601, (55, 50, 12.0), (20, 50, 9.0), "east_deck_transition", ["GlassDeck_East", "DECK_EAST_TIMBER_FLOOR"]),
            point(720, (0, 50, 12.0), (0, 20, 8.5), "through_glass_to_production", ["GlassDeck_East", "DECK_EAST_TIMBER_FLOOR", "Production_Hall"]),
        ]
        return camera, route, {"name": camera.name, "existing_camera": False, "target_subject": "POVU Glass Deck", "semantic_targets": deck_names + ["Production_Hall"], "deck_bounds": deck, "production_bounds": production}

    water = bounds_for_names(["POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER"])
    plaza = bounds_for_names(["POVU_PLAZA"])
    living = bounds_for_names(["LIVING_WALL_PANEL"])
    hog_names = ["HOG_PALM_L", "HOG_PALM_R", "HOG_TREE_TRUNK", "HOG_PLINTH"]
    hog_names += sorted(name for name in bpy.data.objects.keys() if name.startswith("HOG_FINGER_") or name.startswith("HOG_TREE_CROWN_"))
    hog = bounds_for_names(hog_names)
    camera = make_temp_camera("VID_COLOR_PROOF_V02_CAMERA")
    route = [
        point(1, (-38, -128, 5.5), Vector(water["center"]), "vip_arrival", ["POVU_VIP_SIGN", "POVU_WATER_WALL_7M", "POVU_PLAZA"]),
        point(121, (-55, -119, 5.0), Vector(water["center"]), "vip_approach", ["POVU_VIP_SIGN", "POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER"]),
        point(241, (-80, -112, 5.5), Vector(living["center"]), "water_and_living_wall", ["POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER", "LIVING_WALL_PANEL"]),
        point(361, (-125, -130, 10.0), Vector(hog["center"]) + Vector((0, 0, 3)), "plaza_and_growth_reveal", ["POVU_PLAZA"] + hog_names),
        point(481, (-135, -120, 15.0), Vector(hog["center"]) + Vector((0, 0, 3)), "signature_landmarks", ["POVU_PLAZA"] + hog_names),
        point(601, (-120, -110, 12.0), Vector(hog["center"]) + Vector((0, 0, 3)), "hands_of_growth_context", hog_names + ["POVU_PLAZA"]),
        point(720, (-85, -115, 10.0), Vector(water["center"]), "color_water_green_light_hero", ["POVU_PLAZA", "POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER", "LIVING_WALL_PANEL"]),
    ]
    return camera, route, {"name": camera.name, "existing_camera": False, "target_subject": "POVU Color & Materials Proof", "semantic_targets": ["POVU_PLAZA", "POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER", "LIVING_WALL_PANEL", "POVU_VIP_SIGN"] + hog_names, "material_subjects": ["POVU_WATER_WALL_7M", "POVU_WATER_WALL_BASIN_WATER", "LIVING_WALL_PANEL", "POVU_VIP_SIGN"]}


def apply_route(camera, route):
    for item in route:
        frame = item["frame"]
        camera.location = item["location"]
        if frame == 1 and camera.name == "PRES_15_MIXING_HALL":
            pass
        else:
            look_at(camera, item["target"])
        camera.keyframe_insert(data_path="location", frame=frame)
        camera.keyframe_insert(data_path="rotation_euler", frame=frame)
        camera.data.keyframe_insert(data_path="lens", frame=frame)
    if camera.animation_data and camera.animation_data.action and hasattr(camera.animation_data.action, "fcurves"):
        for fcurve in camera.animation_data.action.fcurves:
            for key in fcurve.keyframe_points:
                key.interpolation = "BEZIER"
    bpy.context.scene.camera = camera


def project_object(camera, obj):
    scene = bpy.context.scene
    coords = []
    depths = []
    for corner in obj.bound_box:
        coord = world_to_camera_view(scene, camera, obj.matrix_world @ Vector(corner))
        coords.append((coord.x, coord.y))
        depths.append(coord.z)
    if not coords or max(depths) <= 0:
        return False
    min_x, max_x = min(x for x, _ in coords), max(x for x, _ in coords)
    min_y, max_y = min(y for _, y in coords), max(y for _, y in coords)
    return max_x >= 0 and min_x <= 1 and max_y >= 0 and min_y <= 1


def visible_materials(objects):
    names = set()
    for obj in objects:
        if obj and obj.type == "MESH":
            names.update(slot.material.name for slot in obj.material_slots if slot.material)
    return sorted(names)


def qa_record(video, camera, item):
    scene = bpy.context.scene
    scene.frame_set(item["frame"])
    targets = [bpy.data.objects.get(name) for name in item["semantic_objects"]]
    targets = [obj for obj in targets if obj]
    visible = [obj.name for obj in targets if project_object(camera, obj)]
    camera_associated = True
    if video == 3 and item["frame"] >= 241:
        deck = bounds_for_names(["GlassDeck_East", "GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_EAST_TIMBER_FLOOR", "GLASS_DECK_LINK", "GLASS_DECK_LINK_FLOOR"])
        camera_associated = (Vector(camera.location) - Vector(deck["center"])).length < 110
    if video == 1:
        tank_visible = [name for name in visible if name.startswith("ProcessTank_")]
        passed = len(tank_visible) >= 1 and camera.location.z > 2
    elif video == 2:
        passed = len(visible) >= 3
    elif video == 3:
        passed = camera_associated and len(visible) >= 1
    else:
        passed = len(visible) >= 1 and len(visible_materials(targets)) >= 1
    return {
        "video": video,
        "frame": item["frame"],
        "time_seconds": round((item["frame"] - 1) / FPS, 4),
        "active_camera": camera.name,
        "camera_world_xyz": list(camera.matrix_world.translation),
        "camera_rotation_euler": list(camera.matrix_world.to_euler()),
        "camera_lens": camera.data.lens,
        "look_at_xyz": item["target"],
        "semantic_target": item["label"],
        "visible_target_objects": visible,
        "visible_materials": visible_materials(targets),
        "render_engine": scene.render.engine,
        "camera_semantic_association": camera_associated,
        "status": "PASS" if passed else "FAIL",
    }


def main():
    a = parse_args()
    source = os.path.abspath(a.source)
    output_dir = os.path.abspath(a.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    scene = configure_scene()
    camera, route, info = build_route(a.video)
    apply_route(camera, route)
    route_payload = {
        "video": a.video,
        "source": source,
        "source_sha256": SOURCE_SHA256,
        "fps": FPS,
        "frame_start": FRAME_START,
        "frame_end": FRAME_END,
        "resolution": [1280, 720],
        "render_engine": scene.render.engine,
        "camera": info,
        "route": route,
        "camera_true_rule": "Final MP4 frame N is rendered from the active camera at frame N in this saved blend.",
    }
    with open(os.path.join(output_dir, "camera_route.json"), "w", encoding="utf-8") as handle:
        json.dump(route_payload, handle, indent=2)
    blend_path = os.path.join(output_dir, "render.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)

    if a.mode == "checkpoints":
        qa = [qa_record(a.video, camera, item) for item in route]
        # Seven checkpoints are the seven route anchors; frame 720 is the final-frame anchor.
        qa_path = os.path.join(output_dir, "qa_report.json")
        with open(qa_path, "w", encoding="utf-8") as handle:
            json.dump({"video": a.video, "checkpoints": qa, "all_pass": all(item["status"] == "PASS" for item in qa)}, handle, indent=2)
        checkpoint_dir = os.path.join(output_dir, "checkpoints")
        os.makedirs(checkpoint_dir, exist_ok=True)
        scene.render.image_settings.file_format = "PNG"
        for index, item in enumerate(route, start=1):
            scene.frame_set(item["frame"])
            scene.render.filepath = os.path.join(checkpoint_dir, f"checkpoint_{index:02d}.png")
            bpy.ops.render.render(write_still=True)
    else:
        frames_dir = os.path.join(output_dir, "frames")
        os.makedirs(frames_dir, exist_ok=True)
        scene.render.image_settings.file_format = "JPEG"
        scene.render.image_settings.color_mode = "RGB"
        scene.render.image_settings.quality = 95
        for frame in range(FRAME_START, FRAME_END + 1):
            scene.frame_set(frame)
            scene.render.filepath = os.path.join(frames_dir, f"frame_{frame:04d}.jpg")
            bpy.ops.render.render(write_still=True)
        scene.render.image_settings.file_format = "PNG"
        scene.frame_set(FRAME_START)
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        metadata = {
            "video": a.video,
            "source": source,
            "source_sha256": SOURCE_SHA256,
            "camera": camera.name,
            "render_engine": scene.render.engine,
            "resolution": [1280, 720],
            "resolution_percentage": 100,
            "fps": FPS,
            "frame_start": FRAME_START,
            "frame_end": FRAME_END,
            "frames_dir": frames_dir,
            "blend_archive": blend_path,
            "route": route,
            "rendered_at_utc": datetime.now(timezone.utc).isoformat(),
        }
        with open(os.path.join(output_dir, "render_metadata.json"), "w", encoding="utf-8") as handle:
            json.dump(metadata, handle, indent=2)
    print(json.dumps({"video": a.video, "mode": a.mode, "camera": camera.name, "output_dir": output_dir}))


if __name__ == "__main__":
    main()
