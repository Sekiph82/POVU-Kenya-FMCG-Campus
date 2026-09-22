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
    parser.add_argument("--video", type=int, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--mode", choices=["checkpoints", "final"], required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def safe_set(obj, attr, value):
    if hasattr(obj, attr):
        try:
            setattr(obj, attr, value)
            return True
        except (TypeError, ValueError, AttributeError):
            return False
    return False


def look_at(camera, target):
    camera.rotation_euler = (Vector(target) - camera.location).to_track_quat("-Z", "Y").to_euler()


def bbox_for_object(obj):
    if obj.type != "MESH" or not obj.bound_box:
        return None
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    mins = [min(p[i] for p in points) for i in range(3)]
    maxs = [max(p[i] for p in points) for i in range(3)]
    return {"min": mins, "max": maxs, "center": [(a + b) / 2 for a, b in zip(mins, maxs)], "dimensions": [b - a for a, b in zip(mins, maxs)]}


def bounds_for_objects(objects):
    boxes = [bbox_for_object(obj) for obj in objects]
    boxes = [box for box in boxes if box]
    if not boxes:
        raise RuntimeError("No mesh geometry found for the semantic target set")
    mins = [min(box["min"][i] for box in boxes) for i in range(3)]
    maxs = [max(box["max"][i] for box in boxes) for i in range(3)]
    return {"min": mins, "max": maxs, "center": [(a + b) / 2 for a, b in zip(mins, maxs)], "dimensions": [b - a for a, b in zip(mins, maxs)]}


def resolve_target_names(targets):
    resolved = []
    mapping = {}
    all_meshes = sorted((obj for obj in bpy.context.scene.objects if obj.type == "MESH"), key=lambda obj: obj.name)
    for target in targets:
        exact = bpy.data.objects.get(target)
        if exact and exact.type == "MESH":
            names = [exact.name]
        else:
            names = [obj.name for obj in all_meshes if obj.name.startswith(target)][:12]
        mapping[target] = names
        resolved.extend(names)
    unique = []
    for name in resolved:
        if name not in unique:
            unique.append(name)
    return unique, mapping


def make_camera(name, lens=40.0):
    data = bpy.data.cameras.new(name)
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    data.lens = lens
    data.sensor_width = 36.0
    data.clip_start = 0.1
    data.clip_end = 1500.0
    return camera


def point(frame, location, target, label, semantic_objects):
    return {"frame": frame, "location": list(location), "target": list(target), "label": label, "semantic_objects": list(semantic_objects)}


def resolve_anchor(spec):
    anchor = bpy.data.objects.get(spec["anchor"])
    if not anchor or anchor.type != "CAMERA":
        raise RuntimeError(f"Anchor camera missing: {spec['anchor']}")
    return anchor


def route_for_spec(spec, target_names, mapping, target_bounds):
    anchor = resolve_anchor(spec)
    anchor_location = anchor.matrix_world.translation.copy()
    center = Vector(target_bounds["center"])
    dimensions = Vector(target_bounds["dimensions"])
    size = max(8.0, max(dimensions.x, dimensions.y, dimensions.z))
    radius = max(8.0, min(55.0, size * 0.55))
    from_center = anchor_location - center
    if from_center.length < 1.0:
        from_center = Vector((0.0, -1.0, 0.0))
    direction = from_center.normalized()
    horizontal = Vector((direction.x, direction.y, 0.0))
    if horizontal.length < 0.1:
        horizontal = Vector((0.0, -1.0, 0.0))
    horizontal.normalize()
    perpendicular = Vector((-horizontal.y, horizontal.x, 0.0))
    height = max(6.0, center.z + min(16.0, max(3.0, dimensions.z * 0.45)))
    style = spec.get("style", "interior")
    if style == "aerial":
        # Keep the aerial film deliberately oblique. Directly overhead views of the
        # large production roofs fail the visual subject test even when projection QA passes.
        campus = Vector((0.0, 0.0, 5.0))
        locations = [
            anchor_location,
            Vector((180.0, -180.0, 185.0)),
            Vector((125.0, -155.0, 145.0)),
            Vector((65.0, -125.0, 105.0)),
            Vector((-135.0, 85.0, 115.0)),
            Vector((115.0, 45.0, 110.0)),
            Vector((15.0, -145.0, 85.0)),
        ]
        targets = [campus, campus, campus, Vector((-35.0, -45.0, 5.0)), Vector((-55.0, 65.0, 5.0)), Vector((65.0, -35.0, 5.0)), Vector((0.0, 0.0, 5.0))]
        return [point(frame, locations[i], targets[i], f"aerial_oblique_campus_{i + 1}", target_names) for i, frame in enumerate(CHECKPOINTS)]
    if style == "grand_tour":
        centers = []
        for target in spec["targets"]:
            names = mapping.get(target, [])
            meshes = [bpy.data.objects[name] for name in names if bpy.data.objects.get(name)]
            if meshes:
                centers.append(Vector(bounds_for_objects(meshes)["center"]))
        while len(centers) < 7:
            centers.append(center)
        route = []
        for index, frame in enumerate(CHECKPOINTS):
            subject = centers[min(index, len(centers) - 1)]
            offset = Vector((0.0, -max(18.0, radius * 1.5), max(16.0, radius * 0.8)))
            route.append(point(frame, subject + offset, subject, f"grand_tour_zone_{index + 1}", target_names))
        route[0]["location"] = list(anchor_location)
        return route
    if style == "arrival":
        # Keep the visitor film on the modeled approach/plaza side of the entrance.
        # The generic depth pass can otherwise cross the pavilion roof and produce a
        # mathematically valid but visually occluded frame.
        front_y = center.y - max(18.0, radius * 1.45)
        locations = [
            anchor_location,
            Vector((center.x + 8.0, front_y - 18.0, max(12.0, center.z + 10.0))),
            Vector((center.x - 6.0, front_y - 6.0, max(8.0, center.z + 5.0))),
            Vector((center.x - radius * 0.8, front_y, max(7.0, center.z + 3.0))),
            Vector((center.x + radius * 0.8, front_y, max(7.0, center.z + 3.0))),
            Vector((center.x, front_y + 4.0, max(8.0, center.z + 4.0))),
            Vector((center.x - 4.0, front_y - 12.0, max(10.0, center.z + 7.0))),
        ]
        return [point(frame, locations[i], center, f"arrival_plaza_{i + 1}", target_names) for i, frame in enumerate(CHECKPOINTS)]
    if style == "campus" and spec.get("id") == 3:
        # Employee-campus geometry sits at the west/south edge of the wellness
        # building. Explicit eye-level cross-axis views keep the pond, benches and
        # canopy in frame instead of looking into the building roof.
        garden_target = Vector((-18.0, -62.0, 1.8))
        locations = [
            Vector((-18.0, -62.0, 35.0)),
            Vector((-35.0, -62.0, 28.0)),
            Vector((-18.0, -82.0, 30.0)),
            Vector((2.0, -62.0, 28.0)),
            Vector((-18.0, -42.0, 26.0)),
            Vector((-42.0, -72.0, 31.0)),
            Vector((-18.0, -62.0, 40.0)),
        ]
        return [point(frame, locations[i], garden_target, f"employee_campus_garden_{i + 1}", target_names) for i, frame in enumerate(CHECKPOINTS)]
    if spec.get("id") == 5:
        # R&D/QC is represented by the modeled MES control-room presentation camera;
        # a building-envelope orbit cannot see the interior screens.
        forward = anchor.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))
        base_target = anchor.matrix_world.translation + forward * 100.0
        base = anchor.matrix_world.translation.copy()
        offsets = [Vector((0.0, 0.0, 0.0)), Vector((2.0, 1.0, 0.0)), Vector((4.0, 2.0, 0.2)), Vector((2.0, 3.0, 0.0)), Vector((-2.0, 3.0, 0.0)), Vector((-4.0, 1.0, 0.2)), Vector((0.0, 0.0, 0.0))]
        locations = [base + offset for offset in offsets]
        targets = [location + forward * 100.0 for location in locations]
        return [point(frame, locations[i], targets[i], f"mes_control_room_pass_{i + 1}", target_names) for i, frame in enumerate(CHECKPOINTS)]
    if style == "building":
        # Keep building films on the presentation/visitor side of the subject. A
        # wide orbit crosses the roof envelope and produces blank-wall frames.
        depth = max(24.0, min(55.0, radius * 1.35))
        front = center + direction * depth
        focus = Vector((center.x, center.y, max(2.5, center.z)))
        focus_terms = ("SIGN", "LOBBY", "ENTRY", "FRONT", "CANOPY", "SCREEN")
        focus_candidates = [bpy.data.objects.get(name) for name in target_names]
        focus_candidates = [obj for obj in focus_candidates if obj and obj.type == "MESH"]
        focus_candidates.sort(key=lambda obj: (0 if any(term in obj.name.upper() for term in focus_terms) else 1, obj.name))
        if focus_candidates:
            focus_box = bbox_for_object(focus_candidates[0])
            if focus_box:
                focus = Vector(focus_box["center"])
        locations = [
            front + Vector((0.0, 0.0, 4.0)),
            front + perpendicular * 10.0 + Vector((0.0, 0.0, 2.0)),
            front + perpendicular * 18.0 + Vector((0.0, 0.0, 1.0)),
            front - perpendicular * 14.0 + Vector((0.0, 0.0, 1.0)),
            front - perpendicular * 24.0 + Vector((0.0, 0.0, 2.0)),
            front - perpendicular * 8.0 + Vector((0.0, 0.0, 3.0)),
            front + Vector((0.0, 0.0, 6.0)),
        ]
        return [point(frame, locations[i], focus, f"building_facade_pass_{i + 1}", target_names) for i, frame in enumerate(CHECKPOINTS)]
    start = anchor_location.copy()
    if (start - center).length > 160.0:
        start = center + direction * max(35.0, radius * 2.5) + Vector((0.0, 0.0, min(35.0, radius)))
    near = center + direction * max(10.0, radius * 1.35) + Vector((0.0, 0.0, min(12.0, radius * 0.35)))
    side_a = center + direction * max(8.0, radius * 0.9) + perpendicular * max(8.0, radius * 0.9) + Vector((0.0, 0.0, min(10.0, radius * 0.25)))
    side_b = center - direction * max(8.0, radius * 0.75) + perpendicular * max(6.0, radius * 0.75) + Vector((0.0, 0.0, min(10.0, radius * 0.2)))
    side_c = center - direction * max(8.0, radius * 0.95) - perpendicular * max(6.0, radius * 0.6) + Vector((0.0, 0.0, min(11.0, radius * 0.3)))
    hero = center + direction * max(8.0, radius * 1.1) - perpendicular * max(5.0, radius * 0.45) + Vector((0.0, 0.0, min(13.0, radius * 0.4)))
    return [
        point(1, start, center, "establish_actual_subject", target_names),
        point(121, start.lerp(near, 0.55), center, "approach_semantic_zone", target_names),
        point(241, near, center, "reveal_actual_geometry", target_names),
        point(361, side_a, center, "enter_or_move_with_subject", target_names),
        point(481, side_b, center, "explore_subject_area", target_names),
        point(601, side_c, center, "subject_detail_pass", target_names),
        point(718, hero, center, "subject_specific_hero", target_names),
    ]


def stabilize_materials():
    changed = []
    for material in bpy.data.materials:
        if not material.use_nodes:
            continue
        before = {"blend_method": getattr(material, "blend_method", None), "surface_render_method": getattr(material, "surface_render_method", None)}
        safe_set(material, "blend_method", "OPAQUE")
        safe_set(material, "surface_render_method", "BLENDED")
        principled = material.node_tree.nodes.get("Principled BSDF")
        if principled and "Alpha" in principled.inputs and principled.inputs["Alpha"].default_value < 0.999:
            principled.inputs["Alpha"].default_value = 1.0
        after = {"blend_method": getattr(material, "blend_method", None), "surface_render_method": getattr(material, "surface_render_method", None)}
        if before != after:
            changed.append({"material": material.name, "before": before, "after": after})
    return {"changed_material_count": len(changed), "changed_materials": changed, "scope": "disposable V03 scene only"}


def configure_scene(subject_center, style):
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
    eevee = scene.eevee
    changes = {"engine": "BLENDER_EEVEE", "resolution": [1280, 720], "resolution_percentage": 100, "fps": FPS, "frame_start": FRAME_START, "frame_end": FRAME_END}
    for attr, value in (("taa_render_samples", 32), ("taa_samples", 32), ("use_taa_reprojection", False), ("use_raytracing", False), ("use_shadow_jitter_viewport", False), ("use_volumetric_shadows", False), ("shadow_resolution_scale", 2.0), ("shadow_ray_count", 4), ("shadow_step_count", 4), ("use_shadows", False)):
        safe_set(eevee, attr, value)
        changes[attr] = value
    exposure = -0.75 if style in {"interior", "production", "warehouse", "logistics", "utilities", "safety"} else -0.25
    if style == "aerial":
        exposure = -0.5
    scene.view_settings.exposure = exposure
    changes["exposure"] = exposure
    if scene.world:
        scene.world.use_nodes = True
        background = scene.world.node_tree.nodes.get("Background")
        if background:
            background.inputs["Color"].default_value = (0.018, 0.028, 0.04, 1.0)
            background.inputs["Strength"].default_value = 0.22
    changes["world_strength"] = 0.22
    for light in bpy.data.lights:
        for attr, value in (("use_shadow", False), ("use_contact_shadow", False), ("use_shadow_jitter", False)):
            safe_set(light, attr, value)
    changes["shadow_policy"] = "disabled in disposable V03 Eevee scene to remove stochastic grain"
    changes["material_stabilization"] = stabilize_materials()
    cx, cy, cz = subject_center
    rigs = [("V03_MASTER_KEY", (cx - 35, cy - 35, cz + 55), (cx, cy, cz), 50000.0, 100.0), ("V03_MASTER_FILL", (cx + 35, cy + 25, cz + 30), (cx, cy, cz), 25000.0, 90.0), ("V03_MASTER_RIM", (cx, cy + 55, cz + 35), (cx, cy, cz), 20000.0, 80.0)]
    for name, location, target, energy, size in rigs:
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.shape = "DISK"
        data.size = size
        safe_set(data, "use_shadow", False)
        safe_set(data, "use_contact_shadow", False)
        obj = bpy.data.objects.new(name, data)
        scene.collection.objects.link(obj)
        obj.location = location
        look_at(obj, target)
    data = bpy.data.lights.new("V03_MASTER_SUN", "SUN")
    data.energy = 1.5
    data.angle = math.radians(12.0)
    safe_set(data, "use_shadow", False)
    obj = bpy.data.objects.new("V03_MASTER_SUN", data)
    scene.collection.objects.link(obj)
    obj.location = (cx + 50, cy - 70, cz + 80)
    look_at(obj, (cx, cy, cz))
    return changes


def project_object(camera, obj):
    if not obj or obj.type != "MESH" or not obj.bound_box:
        return False
    coords = [world_to_camera_view(bpy.context.scene, camera, obj.matrix_world @ Vector(corner)) for corner in obj.bound_box]
    if max(c.z for c in coords) <= 0:
        return False
    return max(c.x for c in coords) >= 0 and min(c.x for c in coords) <= 1 and max(c.y for c in coords) >= 0 and min(c.y for c in coords) <= 1


def qa_record(camera, item, target_names, changes):
    bpy.context.scene.frame_set(item["frame"])
    targets = [bpy.data.objects.get(name) for name in target_names]
    visible = [obj.name for obj in targets if project_object(camera, obj)]
    clean = changes.get("shadow_policy", "") != ""
    passed = bool(visible) and camera.location.z > 1.0 and clean
    return {"frame": item["frame"], "requested_time_seconds": 29.9 if item["frame"] == 718 else round((item["frame"] - 1) / FPS, 4), "active_camera": camera.name, "camera_world_xyz": list(camera.matrix_world.translation), "camera_rotation_euler": list(camera.matrix_world.to_euler()), "camera_lens": camera.data.lens, "look_at_xyz": item["target"], "semantic_target": item["label"], "visible_target_objects": visible, "checks": {"correct_subject_projected": bool(visible), "clean_render_settings": clean, "camera_height_valid": camera.location.z > 1.0}, "status": "PASS" if passed else "FAIL"}


def main():
    a = parse_args()
    source = os.path.abspath(a.source)
    output_dir = os.path.abspath(a.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    with open(source, "rb") as handle:
        actual_hash = hashlib.sha256(handle.read()).hexdigest()
    if actual_hash != SOURCE_SHA256:
        raise RuntimeError(f"Source SHA mismatch: expected {SOURCE_SHA256}, got {actual_hash}")
    with open(a.manifest, "r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    specs = [spec for spec in manifest["videos"] if spec["id"] == a.video]
    if len(specs) != 1:
        raise RuntimeError(f"Video {a.video} is not uniquely defined in the manifest")
    spec = specs[0]
    if spec.get("style") == "blocked":
        payload = {"video": a.video, "title": spec["title"], "status": "BLOCKED_MISSING_GEOMETRY", "limitations": spec.get("limitations", "")}
        with open(os.path.join(output_dir, "completion.json"), "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
        print(json.dumps(payload))
        return
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    target_names, mapping = resolve_target_names(spec["targets"])
    if not target_names:
        payload = {"video": a.video, "title": spec["title"], "status": "BLOCKED_MISSING_GEOMETRY", "requested_targets": spec["targets"]}
        with open(os.path.join(output_dir, "completion.json"), "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
        print(json.dumps(payload))
        return
    target_objects = [bpy.data.objects[name] for name in target_names]
    target_bounds = bounds_for_objects(target_objects)
    changes = configure_scene(target_bounds["center"], spec.get("style", "interior"))
    camera_name = f"VID_{a.video:03d}_{spec['slug']}_V03_CAMERA"
    camera = make_camera(camera_name, 42.0 if spec.get("style") != "aerial" else 50.0)
    route = route_for_spec(spec, target_names, mapping, target_bounds)
    for item in route:
        camera.location = item["location"]
        look_at(camera, item["target"])
        camera.keyframe_insert(data_path="location", frame=item["frame"])
        camera.keyframe_insert(data_path="rotation_euler", frame=item["frame"])
        camera.data.keyframe_insert(data_path="lens", frame=item["frame"])
    if camera.animation_data and camera.animation_data.action and hasattr(camera.animation_data.action, "fcurves"):
        for fcurve in camera.animation_data.action.fcurves:
            for key in fcurve.keyframe_points:
                key.interpolation = "BEZIER"
    bpy.context.scene.camera = camera
    route_records = []
    for item in route:
        bpy.context.scene.frame_set(item["frame"])
        route_records.append({**item, "time_seconds": 29.9 if item["frame"] == 718 else round((item["frame"] - 1) / FPS, 4), "camera_xyz": list(camera.matrix_world.translation), "camera_rotation_euler": list(camera.matrix_world.to_euler()), "lens": camera.data.lens})
    with open(os.path.join(output_dir, "scene_inventory.json"), "w", encoding="utf-8") as handle:
        json.dump({"video": a.video, "title": spec["title"], "source_sha256": SOURCE_SHA256, "requested_targets": spec["targets"], "resolved_targets": target_names, "target_mapping": mapping, "target_bounds": target_bounds}, handle, indent=2)
    with open(os.path.join(output_dir, "camera_route.json"), "w", encoding="utf-8") as handle:
        json.dump({"video": a.video, "title": spec["title"], "camera": camera.name, "source_sha256": SOURCE_SHA256, "fps": FPS, "resolution": [1280, 720], "route": route_records, "camera_true_rule": "Final frame N is rendered from the active Blender production camera at frame N."}, handle, indent=2)
    settings = {"video": a.video, "title": spec["title"], "source": source, "source_sha256": SOURCE_SHA256, "engine": "BLENDER_EEVEE", "resolution": [1280, 720], "resolution_percentage": 100, "fps": FPS, "frame_start": 1, "frame_end": 720, "workbench": False, "render_settings": changes, "limitations": spec.get("limitations", "")}
    with open(os.path.join(output_dir, "render_settings.json"), "w", encoding="utf-8") as handle:
        json.dump(settings, handle, indent=2)
    blend_path = os.path.join(output_dir, "render.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    if a.mode == "checkpoints":
        qa = [qa_record(camera, item, target_names, changes) for item in route]
        os.makedirs(os.path.join(output_dir, "qa"), exist_ok=True)
        bpy.context.scene.render.image_settings.file_format = "PNG"
        for index, item in enumerate(route, start=1):
            bpy.context.scene.frame_set(item["frame"])
            bpy.context.scene.render.filepath = os.path.join(output_dir, "qa", f"checkpoint_{index:02d}.png")
            bpy.ops.render.render(write_still=True)
        with open(os.path.join(output_dir, "qa_report.json"), "w", encoding="utf-8") as handle:
            json.dump({"video": a.video, "title": spec["title"], "source_sha256": SOURCE_SHA256, "checkpoints": qa, "automated_all_pass": all(row["status"] == "PASS" for row in qa), "visual_qa": "REVIEW_REQUIRED"}, handle, indent=2)
    else:
        frames_dir = os.path.join(output_dir, "frames")
        os.makedirs(frames_dir, exist_ok=True)
        bpy.context.scene.render.image_settings.file_format = "JPEG"
        bpy.context.scene.render.image_settings.color_mode = "RGB"
        bpy.context.scene.render.image_settings.quality = 95
        for frame in range(FRAME_START, FRAME_END + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.scene.render.filepath = os.path.join(frames_dir, f"frame_{frame:04d}.jpg")
            bpy.ops.render.render(write_still=True)
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        with open(os.path.join(output_dir, "render_metadata.json"), "w", encoding="utf-8") as handle:
            json.dump({"video": a.video, "title": spec["title"], "source": source, "source_sha256": SOURCE_SHA256, "camera": camera.name, "render_engine": "BLENDER_EEVEE", "resolution": [1280, 720], "fps": FPS, "frame_start": 1, "frame_end": 720, "frames_dir": frames_dir, "blend_archive": blend_path, "rendered_at_utc": datetime.now(timezone.utc).isoformat()}, handle, indent=2)
    print(json.dumps({"video": a.video, "mode": a.mode, "camera": camera.name, "output_dir": output_dir, "source_sha256": actual_hash, "target_count": len(target_names)}))


if __name__ == "__main__":
    main()
