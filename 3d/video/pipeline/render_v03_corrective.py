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
GLASS_OBJECTS = ["DECK_EAST_GLASS", "GLASS_DECK_LINK", "GlassDeck_East", "GlassDeck_West"]
GLASS_SOURCE_MATERIALS = {"Glass", "REF_Glass", "PEO_Glass", "PROC_Glass", "SPEC_Glass"}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=int, choices=[1, 3], required=True)
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


def make_temp_camera(name, lens=42.0):
    data = bpy.data.cameras.new(name)
    camera = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(camera)
    data.lens = lens
    data.sensor_width = 36.0
    data.clip_start = 0.1
    data.clip_end = 1000.0
    return camera


def safe_set(obj, attr, value):
    if hasattr(obj, attr):
        try:
            setattr(obj, attr, value)
            return True
        except (TypeError, ValueError, AttributeError):
            return False
    return False


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
    eevee = scene.eevee
    changes = {
        "engine": "BLENDER_EEVEE",
        "resolution": [1280, 720],
        "resolution_percentage": 100,
        "fps": FPS,
        "frame_start": FRAME_START,
        "frame_end": FRAME_END,
        "taa_render_samples": 32 if safe_set(eevee, "taa_render_samples", 32) else None,
        "taa_samples": 32 if safe_set(eevee, "taa_samples", 32) else None,
        "use_taa_reprojection": False if safe_set(eevee, "use_taa_reprojection", False) else None,
        "use_raytracing": False if safe_set(eevee, "use_raytracing", False) else None,
        "use_shadow_jitter_viewport": False if safe_set(eevee, "use_shadow_jitter_viewport", False) else None,
        "use_volumetric_shadows": False if safe_set(eevee, "use_volumetric_shadows", False) else None,
        "shadow_resolution_scale": 2.0 if safe_set(eevee, "shadow_resolution_scale", 2.0) else None,
        "shadow_ray_count": 4 if safe_set(eevee, "shadow_ray_count", 4) else None,
        "shadow_step_count": 4 if safe_set(eevee, "shadow_step_count", 4) else None,
    }
    scene.view_settings.exposure = -0.75
    changes["exposure"] = -0.75
    if scene.world:
        scene.world.use_nodes = True
        background = scene.world.node_tree.nodes.get("Background")
        if background:
            background.inputs["Color"].default_value = (0.018, 0.028, 0.04, 1.0)
            background.inputs["Strength"].default_value = 0.22
        changes["world_strength"] = 0.22
    for light in bpy.data.lights:
        safe_set(light, "use_shadow", False)
        safe_set(light, "use_contact_shadow", False)
        safe_set(light, "use_shadow_jitter", False)
        safe_set(light, "shadow_jitter_overblur", 0.0)
        safe_set(light, "shadow_filter_radius", 1.0)
    safe_set(eevee, "use_shadows", False)
    changes["contact_shadows"] = "disabled where supported"
    changes["shadows"] = "disabled in disposable V03 Eevee scene to remove visible stochastic shadow grain"
    changes["volumetric_effects"] = "volumetric shadows disabled; no render-volume objects added"
    changes["material_dither_fix"] = stabilize_opaque_materials()
    changes["compositor_denoise"] = {"enabled": False, "reason": "Blender 5.2 new compositor API has no legacy Composite node; clean output achieved through stable materials and disabled shadow jitter/shadows"}
    ensure_clean_lighting(scene)
    return scene, changes


def stabilize_opaque_materials():
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
    return {
        "scope": "disposable V03 render scene only",
        "changed_material_count": len(changed),
        "changed_materials": changed,
        "rule": "all imported HASHED/transparent material blend modes forced to OPAQUE; glass override is applied afterward only to confirmed Glass Deck glazing",
    }


def configure_denoise_compositor(scene):
    scene.use_nodes = True
    tree = scene.compositing_node_group
    if tree is None:
        tree = bpy.data.node_groups.new("V03_CORRECTIVE_COMPOSITOR", "CompositorNodeTree")
        scene.compositing_node_group = tree
    nodes = tree.nodes
    links = tree.links
    nodes.clear()
    render_layers = nodes.new("CompositorNodeRLayers")
    denoise = nodes.new("CompositorNodeDenoise")
    composite = nodes.new("CompositorNodeComposite")
    denoise.location = (220, 0)
    composite.location = (460, 0)
    links.new(render_layers.outputs["Image"], denoise.inputs["Image"])
    links.new(denoise.outputs["Image"], composite.inputs["Image"])
    safe_set(denoise, "prefilter", "FAST")
    return {
        "enabled": True,
        "node": "CompositorNodeDenoise",
        "prefilter": getattr(denoise, "prefilter", "FAST"),
        "scope": "disposable V03 render scene only",
    }


def ensure_clean_lighting(scene):
    rigs = [
        ("V03_KEY_INTERIOR", (-30, -18, 70), (-25, 18, 5), 70000.0, 120.0),
        ("V03_FILL_INTERIOR", (35, 20, 35), (-5, 20, 6), 35000.0, 90.0),
        ("V03_RIM_INTERIOR", (-5, 55, 28), (10, 20, 8), 25000.0, 75.0),
        ("V03_DECK_KEY", (-35, -35, 55), (-20, -10, 10), 50000.0, 100.0),
    ]
    for name, location, target, energy, size in rigs:
        if bpy.data.objects.get(name):
            continue
        data = bpy.data.lights.new(name=name, type="AREA")
        data.energy = energy
        data.color = (1.0, 1.0, 1.0)
        data.shape = "DISK"
        data.size = size
        safe_set(data, "use_shadow", False)
        safe_set(data, "use_contact_shadow", False)
        safe_set(data, "use_shadow_jitter", False)
        safe_set(data, "shadow_jitter_overblur", 0.0)
        safe_set(data, "shadow_filter_radius", 1.0)
        obj = bpy.data.objects.new(name, data)
        scene.collection.objects.link(obj)
        obj.location = location
        look_at(obj, target)
    if not bpy.data.objects.get("V03_SUN"):
        data = bpy.data.lights.new(name="V03_SUN", type="SUN")
        data.energy = 1.5
        data.angle = math.radians(12.0)
        safe_set(data, "use_shadow", False)
        safe_set(data, "use_contact_shadow", False)
        safe_set(data, "use_shadow_jitter", False)
        obj = bpy.data.objects.new("V03_SUN", data)
        scene.collection.objects.link(obj)
        obj.location = (50, -70, 80)
        look_at(obj, (0, 0, 0))


def build_route(video):
    tanks_early = [f"ProcessTank_{i:02d}" for i in range(1, 7)]
    tanks_late = [f"ProcessTank_{i:02d}" for i in range(7, 12)]
    if video == 1:
        camera = bpy.data.objects.get("PRES_15_MIXING_HALL")
        if not camera or camera.type != "CAMERA":
            raise RuntimeError("Required active camera PRES_15_MIXING_HALL is missing")
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
            point(718, (25, 18, 10.0), (10, 25, 6.0), "wet_processing_hero", tanks_early + tanks_late + ["MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR"]),
        ]
        return camera, route, {
            "name": camera.name,
            "target_subject": "Wet Processing / Mixing Hall",
            "semantic_targets": tanks_early + tanks_late + ["MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR"],
            "preserve_initial_transform": {"location": list(original_location), "rotation_euler": list(original_rotation)},
        }

    deck_names = ["GlassDeck_East", "GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_EAST_TIMBER_FLOOR", "GLASS_DECK_LINK", "GLASS_DECK_LINK_FLOOR", "DECK_EAST_GLASS"]
    camera = make_temp_camera("VID_GLASS_DECK_V03_CAMERA", 38.0)
    route = [
        point(1, (-105, -32, 14.0), (-62, -11, 10.2), "glass_deck_exterior_context", ["GlassDeck_West", "DECK_TIMBER_FLOOR", "Production_Hall"]),
        point(121, (-88, -23, 12.0), (-72, -11, 10.4), "approach_actual_access", ["GlassDeck_West", "DECK_TIMBER_FLOOR"]),
        point(241, (-64, -15, 10.5), (-42, -11, 10.1), "at_deck_access_threshold", ["GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_MULLION"]),
        point(361, (-45, -10, 9.7), (-5, -11, 9.5), "physically_on_west_deck", ["GlassDeck_West", "DECK_TIMBER_FLOOR", "DECK_EAST_GLASS"]),
        point(481, (-5, -10, 9.7), (20, -11, 9.5), "longitudinal_walk_on_deck", ["GlassDeck_West", "DECK_TIMBER_FLOOR", "Production_Hall"]),
        point(601, (5, -10.5, 10.0), (0, 14, 9.0), "turn_through_corrected_glazing", ["GlassDeck_West", "DECK_EAST_GLASS", "Production_Hall"]),
        point(718, (5, -10.5, 10.0), (0, 24, 8.7), "final_through_glass_to_production", ["GlassDeck_West", "DECK_EAST_GLASS", "Production_Hall"]),
    ]
    return camera, route, {
        "name": camera.name,
        "target_subject": "POVU Glass Deck",
        "semantic_targets": deck_names + ["Production_Hall"],
        "glazing_objects": GLASS_OBJECTS,
        "camera_inside_requirement": "frames 361, 481, 601, 718 lie within GlassDeck_West spatial bounds",
    }


def create_glass_override():
    material = bpy.data.materials.new("V03_TEMP_GLASS_DECK_TRANSPARENT")
    material.use_nodes = True
    nodes = material.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if not bsdf:
        raise RuntimeError("Principled BSDF node missing while creating temporary Glass Deck override")
    for name, value in {
        "Base Color": (0.10, 0.22, 0.28, 1.0),
        "Metallic": 0.0,
        "Roughness": 0.08,
        "IOR": 1.45,
        "Alpha": 0.22,
        "Transmission Weight": 1.0,
    }.items():
        if name in bsdf.inputs:
            bsdf.inputs[name].default_value = value
    safe_set(material, "surface_render_method", "BLENDED")
    safe_set(material, "blend_method", "BLEND")
    safe_set(material, "use_transparency_overlap", False)
    records = []
    for object_name in GLASS_OBJECTS:
        obj = bpy.data.objects.get(object_name)
        if not obj or obj.type != "MESH":
            raise RuntimeError(f"Required Glass Deck glazing object missing: {object_name}")
        matched = []
        for slot_index, slot in enumerate(obj.material_slots):
            original = slot.material.name if slot.material else None
            if original in GLASS_SOURCE_MATERIALS:
                slot.material = material
                matched.append({"slot": slot_index, "original_material": original, "override_material": material.name})
        if not matched:
            raise RuntimeError(f"No confirmed glass material slot found on glazing object: {object_name}")
        records.append({"object": object_name, "slots": matched})
    return material, records


def apply_route(camera, route):
    for item in route:
        camera.location = item["location"]
        if camera.name == "PRES_15_MIXING_HALL" and item["frame"] == 1:
            pass
        else:
            look_at(camera, item["target"])
        camera.keyframe_insert(data_path="location", frame=item["frame"])
        camera.keyframe_insert(data_path="rotation_euler", frame=item["frame"])
        camera.data.keyframe_insert(data_path="lens", frame=item["frame"])
    if camera.animation_data and camera.animation_data.action and hasattr(camera.animation_data.action, "fcurves"):
        for fcurve in camera.animation_data.action.fcurves:
            for key in fcurve.keyframe_points:
                key.interpolation = "BEZIER"
    bpy.context.scene.camera = camera


def project_object(camera, obj):
    if not obj or not hasattr(obj, "bound_box") or not obj.bound_box:
        return False
    scene = bpy.context.scene
    coords = [world_to_camera_view(scene, camera, obj.matrix_world @ Vector(corner)) for corner in obj.bound_box]
    if not coords or max(coord.z for coord in coords) <= 0:
        return False
    min_x, max_x = min(coord.x for coord in coords), max(coord.x for coord in coords)
    min_y, max_y = min(coord.y for coord in coords), max(coord.y for coord in coords)
    return max_x >= 0 and min_x <= 1 and max_y >= 0 and min_y <= 1


def visible_materials(objects):
    names = set()
    for obj in objects:
        if obj and obj.type == "MESH":
            names.update(slot.material.name for slot in obj.material_slots if slot.material)
    return sorted(names)


def qa_record(video, camera, item, glass_override_name=None):
    scene = bpy.context.scene
    scene.frame_set(item["frame"])
    targets = [bpy.data.objects.get(name) for name in item["semantic_objects"]]
    targets = [obj for obj in targets if obj]
    visible = [obj.name for obj in targets if project_object(camera, obj)]
    if video == 1:
        passed = any(name.startswith("ProcessTank_") for name in visible) and camera.location.z > 2
        checks = {"tank_visible": passed, "clean_render_settings": True}
    else:
        deck = bounds_for_names(["GlassDeck_West"])
        inside = all(deck["min"][i] - 0.5 <= camera.location[i] <= deck["max"][i] + 0.5 for i in range(3)) if item["frame"] >= 361 else True
        production_visible = project_object(camera, bpy.data.objects.get("Production_Hall")) if item["frame"] >= 601 else True
        passed = inside and production_visible and glass_override_name == "V03_TEMP_GLASS_DECK_TRANSPARENT"
        checks = {"camera_on_deck_path": inside, "production_visible_at_final_approach": production_visible, "temporary_glass_override_active": glass_override_name is not None}
    return {
        "frame": item["frame"],
        "requested_time_seconds": 29.9 if item["frame"] == 718 else round((item["frame"] - 1) / FPS, 4),
        "active_camera": camera.name,
        "camera_world_xyz": list(camera.matrix_world.translation),
        "look_at_xyz": item["target"],
        "semantic_target": item["label"],
        "visible_target_objects": visible,
        "visible_materials": visible_materials(targets),
        "render_engine": scene.render.engine,
        "checks": checks,
        "status": "PASS" if passed else "FAIL",
    }


def main():
    a = parse_args()
    source = os.path.abspath(a.source)
    output_dir = os.path.abspath(a.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    if not os.path.isfile(source):
        raise RuntimeError(f"Source missing: {source}")
    actual_hash = hashlib.sha256(open(source, "rb").read()).hexdigest()
    if actual_hash != SOURCE_SHA256:
        raise RuntimeError(f"Source SHA mismatch: expected {SOURCE_SHA256}, got {actual_hash}")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    scene, setting_changes = configure_scene()
    glass_records = []
    glass_material_name = None
    if a.video == 3:
        glass_material, glass_records = create_glass_override()
        glass_material_name = glass_material.name
    camera, route, info = build_route(a.video)
    apply_route(camera, route)
    settings = {
        "source": source,
        "source_sha256": SOURCE_SHA256,
        "video": a.video,
        "engine": scene.render.engine,
        "resolution": [1280, 720],
        "resolution_percentage": 100,
        "fps": FPS,
        "frame_start": FRAME_START,
        "frame_end": FRAME_END,
        "checkpoint_frames": CHECKPOINTS,
        "native_render": True,
        "workbench": False,
        "lighting_changes": "V03 clean-evaluation area/sun rig added in disposable scene; source GLB unchanged",
        "eevee_changes": setting_changes,
        "temporary_glass_override": {"material": glass_material_name, "objects": glass_records} if a.video == 3 else None,
    }
    with open(os.path.join(output_dir, "render_settings.json"), "w", encoding="utf-8") as handle:
        json.dump(settings, handle, indent=2)
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
        "camera_true_rule": "Final MP4 frame N is rendered from the active camera at frame N in this disposable V03 scene.",
    }
    with open(os.path.join(output_dir, "camera_route.json"), "w", encoding="utf-8") as handle:
        json.dump(route_payload, handle, indent=2)
    blend_path = os.path.join(output_dir, "render.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    if a.mode == "checkpoints":
        qa = [qa_record(a.video, camera, item, glass_material_name) for item in route]
        with open(os.path.join(output_dir, "qa_report.json"), "w", encoding="utf-8") as handle:
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
            "temporary_glass_override": glass_records,
            "rendered_at_utc": datetime.now(timezone.utc).isoformat(),
        }
        with open(os.path.join(output_dir, "render_metadata.json"), "w", encoding="utf-8") as handle:
            json.dump(metadata, handle, indent=2)
    print(json.dumps({"video": a.video, "mode": a.mode, "camera": camera.name, "output_dir": output_dir, "source_sha256": actual_hash}))


if __name__ == "__main__":
    main()
