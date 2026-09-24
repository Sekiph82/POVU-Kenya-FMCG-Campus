"""Build the REV004 architectural finalization from the untouched REV003 GLB."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import bpy
from mathutils import Vector


BASE_Z = 1.2


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def collection(name: str):
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col


def link_only(obj, col):
    for existing in list(obj.users_collection):
        existing.objects.unlink(obj)
    col.objects.link(obj)


def material(name, color, metallic=0.0, roughness=0.45, transmission=0.0):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
    mat.diffuse_color = (*color, 1.0)
    nodes = mat.node_tree.nodes if mat.use_nodes else []
    shader = next((node for node in nodes if node.type == "BSDF_PRINCIPLED"), None)
    if shader:
        if shader.inputs.get("Base Color"):
            shader.inputs["Base Color"].default_value = (*color, 1.0)
        if shader.inputs.get("Metallic"):
            shader.inputs["Metallic"].default_value = metallic
        if shader.inputs.get("Roughness"):
            shader.inputs["Roughness"].default_value = roughness
        if shader.inputs.get("Transmission Weight"):
            shader.inputs["Transmission Weight"].default_value = transmission
        elif shader.inputs.get("Transmission"):
            shader.inputs["Transmission"].default_value = transmission
    return mat


MATS = {}


def initialize_materials():
    global MATS
    MATS = {
        "graphite": material("MAT_ARCH_GRAPHITE", (0.035, 0.045, 0.055), 0.35, 0.28),
        "neutral": material("MAT_ARCH_LIGHT_NEUTRAL", (0.72, 0.75, 0.78), 0.05, 0.38),
        "champagne": material("MAT_ARCH_CHAMPAGNE", (0.55, 0.28, 0.09), 0.75, 0.24),
        "glass": material("MAT_ARCH_GLASS", (0.12, 0.42, 0.50), 0.15, 0.12, 0.35),
        "wood": material("MAT_TIMBER", (0.20, 0.08, 0.035), 0.0, 0.55),
        "water": material("MAT_WATER_SURFACE", (0.02, 0.42, 0.56), 0.1, 0.12, 0.2),
        "paving": material("MAT_PEDESTRIAN_PAVING", (0.18, 0.20, 0.21), 0.0, 0.7),
        "green": material("MAT_TREE_FOLIAGE", (0.045, 0.24, 0.07), 0.0, 0.8),
        "stainless": material("MAT_STAINLESS", (0.48, 0.52, 0.55), 0.8, 0.22),
    }


def mark(obj, semantic_id, category, role, source=None, **extra):
    obj["rev004_semantic_id"] = semantic_id
    obj["rev004_category"] = category
    obj["remotion_role"] = role
    if source:
        obj["rev004_source_object"] = source
    for key, value in extra.items():
        obj[key] = value


def assign(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def box(name, location, dimensions, mat, col, category, role, **props):
    bpy.ops.mesh.primitive_cube_add(location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    link_only(obj, col)
    mark(obj, name, category, role, **props)
    return obj


def empty(name, location, col, category, role, **props):
    obj = bpy.data.objects.get(name)
    if obj is None:
        obj = bpy.data.objects.new(name, None)
        col.objects.link(obj)
    obj.location = location
    obj.empty_display_type = "PLAIN_AXES"
    obj.empty_display_size = 1.0
    mark(obj, name, category, role, **props)
    return obj


def text_mesh(name, body, location, scale, mat, col, category, role):
    curve = bpy.data.curves.new(name + "_CURVE", type="FONT")
    curve.body = body
    curve.align_x = "CENTER"
    curve.align_y = "CENTER"
    curve.size = scale
    curve.extrude = 0.015
    obj = bpy.data.objects.new(name, curve)
    col.objects.link(obj)
    obj.location = location
    obj.rotation_euler[0] = math.radians(90.0)
    assign(obj, mat)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.convert(target="MESH")
    mark(obj, name, category, role)
    obj.select_set(False)
    return obj


def look_at(camera, target):
    direction = Vector(target) - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def camera(name, location, target, col, route):
    existing = bpy.data.objects.get(name)
    if existing and existing.type == "CAMERA":
        cam_obj = existing
    else:
        data = bpy.data.cameras.new(name + "_DATA")
        cam_obj = bpy.data.objects.new(name, data)
        col.objects.link(cam_obj)
    cam_obj.location = location
    cam_obj.data.lens = 38
    cam_obj.data.sensor_width = 36
    look_at(cam_obj, target)
    mark(cam_obj, name, "camera", route, route=route, target=list(target))
    return cam_obj


def hide_group(names):
    for name in names:
        obj = bpy.data.objects.get(name)
        if obj:
            obj.hide_render = True
            obj.hide_set(True)


def rename_if_present(old, new):
    obj = bpy.data.objects.get(old)
    if obj and bpy.data.objects.get(new) is None:
        obj.name = new
    return obj or bpy.data.objects.get(new)


def entrance(prefix, center_x, front_y, width, height, purpose, col):
    center_z = BASE_Z + height / 2
    glass = MATS["glass"]
    graphite = MATS["graphite"]
    champagne = MATS["champagne"]
    box(prefix + "_DOOR_L", (center_x - width * 0.24, front_y, center_z), (width * 0.48, 0.14, height), glass, col, "entrance", "architectural_glass_door", purpose=purpose)
    box(prefix + "_DOOR_R", (center_x + width * 0.24, front_y, center_z), (width * 0.48, 0.14, height), glass, col, "entrance", "architectural_glass_door", purpose=purpose)
    box(prefix + "_FRAME_L", (center_x - width / 2, front_y, center_z), (0.22, 0.30, height + 0.25), graphite, col, "entrance", "door_frame", purpose=purpose)
    box(prefix + "_FRAME_R", (center_x + width / 2, front_y, center_z), (0.22, 0.30, height + 0.25), graphite, col, "entrance", "door_frame", purpose=purpose)
    box(prefix + "_FRAME_TOP", (center_x, front_y, BASE_Z + height + 0.12), (width + 0.44, 0.30, 0.24), champagne, col, "entrance", "entrance_portal", purpose=purpose)
    box(prefix + "_MULLION", (center_x, front_y - 0.02, center_z), (0.12, 0.18, height), graphite, col, "entrance", "door_mullion", purpose=purpose)
    box(prefix + "_THRESHOLD", (center_x, front_y - 0.35, BASE_Z + 0.10), (width + 0.5, 0.9, 0.20), champagne, col, "entrance", "door_threshold", purpose=purpose)
    box(prefix + "_CANOPY", (center_x, front_y - 1.65, BASE_Z + height + 1.0), (width + 4.0, 3.4, 0.28), graphite, col, "entrance", "entrance_canopy", purpose=purpose)
    box(prefix + "_CANOPY_ACCENT", (center_x, front_y - 3.05, BASE_Z + height + 0.82), (width + 3.0, 0.12, 0.16), champagne, col, "entrance", "entrance_accent", purpose=purpose)
    text_mesh(prefix + "_SIGNAGE", purpose, (center_x, front_y - 0.18, BASE_Z + height + 0.48), 0.55, champagne, col, "signage", "building_signage")


def stair_run(prefix, start, direction, width, steps, step_depth, top_z, col, purpose):
    rise = (top_z - BASE_Z) / steps
    for i in range(steps):
        x = start[0] + direction[0] * step_depth * i
        y = start[1] + direction[1] * step_depth * i
        depth = step_depth + 0.08
        dims = (width, depth, rise * (i + 1)) if abs(direction[1]) > abs(direction[0]) else (depth, width, rise * (i + 1))
        z = BASE_Z + rise * (i + 1) / 2
        box(f"{prefix}_STEP_{i+1:02d}", (x, y, z), dims, MATS["paving"], col, "glass_deck_access", "physical_stair_step", purpose=purpose, step=i + 1)
    empty(prefix, (start[0] + direction[0] * step_depth * (steps - 1), start[1] + direction[1] * step_depth * (steps - 1), top_z), col, "glass_deck_access", "stair_route", purpose=purpose, steps=steps)


def split_production_shell(src, col):
    if not src or src.type != "MESH" or not src.data.polygons:
        return []
    groups = defaultdict(list)
    for poly in src.data.polygons:
        normal = poly.normal
        if normal.z > 0.5:
            group = "ROOF"
        elif normal.z < -0.5:
            group = "FLOOR"
        elif normal.y < -0.5:
            group = "WALL_SOUTH"
        elif normal.y > 0.5:
            group = "WALL_NORTH"
        elif normal.x < 0:
            group = "WALL_WEST"
        else:
            group = "WALL_EAST"
        groups[group].append(poly)
    created = []
    for group, polygons in groups.items():
        verts = []
        faces = []
        mats = []
        for poly in polygons:
            offset = len(verts)
            verts.extend([tuple(src.data.vertices[index].co) for index in poly.vertices])
            faces.append(tuple(offset + j for j in range(len(poly.vertices))))
            mats.append(poly.material_index)
        mesh = bpy.data.meshes.new(f"PRODUCTION_{group}_MESH")
        mesh.from_pydata(verts, [], faces)
        mesh.update()
        obj = bpy.data.objects.new(f"PRODUCTION_{group}", mesh)
        col.objects.link(obj)
        obj.matrix_world = src.matrix_world.copy()
        for mat in src.data.materials:
            mesh.materials.append(mat)
        for index, poly in enumerate(mesh.polygons):
            poly.material_index = mats[index] if mats[index] < len(mesh.materials) else 0
        mark(obj, obj.name, "production_shell", "sectional_reveal", source=src.name, section=group)
        created.append(obj)
    src.hide_render = True
    src.hide_set(True)
    mark(src, "Production_Hall_SOURCE_SHELL", "production_shell", "preserved_source_shell", source=src.name, replaced_by=[o.name for o in created])
    return created


def add_label_anchor(name, obj, col, role):
    if not obj:
        return None
    bounds = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box] if obj.bound_box else [obj.matrix_world.translation]
    center = sum(bounds, Vector()) / len(bounds)
    return empty(name, (center.x, center.y, center.z + max(1.0, obj.dimensions.z * 0.25)), col, "label_anchor", role, source_object=obj.name)


def object_record(obj):
    if obj.type == "MESH" and obj.bound_box:
        points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        bounds = {
            "min": [round(min(p[i] for p in points), 4) for i in range(3)],
            "max": [round(max(p[i] for p in points), 4) for i in range(3)],
        }
    else:
        bounds = None
    return {
        "object_name": obj.name,
        "type": obj.type,
        "category": obj.get("rev004_category"),
        "parent": obj.parent.name if obj.parent else None,
        "world_position": [round(v, 4) for v in obj.matrix_world.translation],
        "world_bounds": bounds,
        "materials": [slot.material.name for slot in getattr(obj, "material_slots", []) if slot.material],
        "visible": not obj.hide_render,
        "intended_remotion_role": obj.get("remotion_role"),
        "source_object": obj.get("rev004_source_object"),
    }


def build_manifest(args, source_sha, new_objects, totem_table):
    categories = defaultdict(list)
    for obj in bpy.context.scene.objects:
        if obj.get("rev004_category"):
            categories[obj["rev004_category"]].append(object_record(obj))
    payload = {
        "manifest": "REV004_ARCHITECTURAL_MANIFEST",
        "revision": "REV004_FINAL_ARCHITECTURAL_MASTER",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "blender_version": bpy.app.version_string,
        "source": {
            "path": args.input,
            "sha256": source_sha,
            "revision": "REV003",
        },
        "output": {
            "blend": args.blend,
            "glb": args.glb,
        },
        "counts": {
            "object_count": len(bpy.data.objects),
            "mesh_object_count": sum(1 for obj in bpy.data.objects if obj.type == "MESH"),
            "mesh_data_count": len(bpy.data.meshes),
            "material_count": len(bpy.data.materials),
            "camera_count": sum(1 for obj in bpy.data.objects if obj.type == "CAMERA"),
        },
        "smart_totem_placement_table": totem_table,
        "categories": {key: sorted(value, key=lambda item: item["object_name"].lower()) for key, value in sorted(categories.items())},
        "new_objects": sorted(new_objects),
        "known_limitations": [
            "REV003 imported as GLB has no native editable Blender source; REV004 preserves the GLB as the source of truth and adds a separate structured finalization layer.",
            "The original Production_Hall shell was preserved but hidden in favor of face-separated REV004 roof, floor, and wall objects for future sectional reveals.",
            "Final material appearance remains subject to the later Remotion/Three.js material system; REV004 establishes deterministic semantic groups.",
        ],
    }
    with open(args.manifest, "w", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--blend", required=True)
    parser.add_argument("--glb", required=True)
    parser.add_argument("--manifest", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    args.input = os.path.abspath(args.input)
    args.blend = os.path.abspath(args.blend)
    args.glb = os.path.abspath(args.glb)
    args.manifest = os.path.abspath(args.manifest)

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=args.input)
    initialize_materials()
    final_col = collection("REV004_ARCHITECTURAL_FINALIZATION")
    source_sha = sha256(Path(args.input))
    new_objects = []

    # Existing REV003 geometry remains in place; semantic properties make it deterministic for Remotion.
    role_map = {
        "POVU_WATER_WALL_7M": ("water_wall", "WATER_WALL_STRUCTURE"),
        "POVU_WATER_WALL_BASIN": ("water_wall", "WATER_WALL_BASIN"),
        "POVU_WATER_WALL_BASIN_WATER": ("water_wall", "WATER_WALL_BASIN"),
        "POVU_WATER_WALL_CREST": ("water_wall", "WATER_WALL_TOP_FEED"),
        "POVU_WATER_WALL_FRAME": ("water_wall", "WATER_WALL_STRUCTURE"),
        "POVU_VIP_SIGN": ("water_wall", "WATER_WALL_POVU_SIGNAGE"),
        "VIP_Waterfall": ("water_wall", "WATER_WALL_WATER_SURFACE"),
        "VIP_LivingWall": ("living_wall", "LIVING_WALL_STRUCTURE"),
        "LIVING_WALL_PANEL": ("living_wall", "LIVING_WALL_STRUCTURE"),
        "HOG_TREE_TRUNK": ("hands_of_growth", "HOG_TREE_TRUNK"),
        "HOG_TREE_CROWN_0": ("hands_of_growth", "HOG_TREE_CROWN"),
        "HOG_PLINTH": ("hands_of_growth", "HOG_PLINTH"),
        "GlassDeck_East": ("glass_deck", "GLASS_DECK_GLAZING"),
        "GlassDeck_West": ("glass_deck", "GLASS_DECK_GLAZING"),
        "GLASS_DECK_LINK": ("glass_deck", "GLASS_DECK_FRAME"),
        "DECK_TIMBER_FLOOR": ("glass_deck", "GLASS_DECK_FLOOR"),
        "GLASS_DECK_LINK_FLOOR": ("glass_deck", "GLASS_DECK_FLOOR"),
        "Production_Hall": ("production_shell", "PRODUCTION_BUILDING_SHELL"),
        "SOLAR_INVERTER": ("solar", "SOLAR_INVERTER"),
        "MIXING_PLATFORM": ("machine", "MIXING_PLATFORM"),
        "PROCESS_EPOXY_FLOOR": ("machine", "PROCESS_EPOXY_FLOOR"),
    }
    for name, (category, role) in role_map.items():
        obj = bpy.data.objects.get(name)
        if obj:
            mark(obj, role, category, role, source=name)

    # VIP entrance: Living Wall | real automatic double-glass door | Water Wall framing.
    entrance("VIP_ENTRANCE", -58.0, -92.0, 7.0, 6.2, "VIP ENTRANCE", final_col)
    new_objects.extend(["VIP_ENTRANCE_DOOR_L", "VIP_ENTRANCE_DOOR_R", "VIP_ENTRANCE_CANOPY", "VIP_ENTRANCE_SIGNAGE"])
    box("VIP_ENTRANCE_LOBBY_FLOOR", (-58.0, -77.2, 1.34), (8.5, 4.0, 0.16), MATS["wood"], final_col, "entrance", "lobby_depth")
    new_objects.append("VIP_ENTRANCE_LOBBY_FLOOR")

    # Occupied-building entrances, with distinct hierarchy and industrial personnel doors.
    entrance("ADMIN_HQ_ENTRANCE", -58.0, -79.1, 6.0, 5.4, "ADMIN / HQ", final_col)
    entrance("R_D_QC_ENTRANCE", -76.0, -79.1, 5.0, 4.8, "R&D + QC", final_col)
    entrance("RESTAURANT_ENTRANCE", 5.0, -80.7, 5.5, 4.8, "RESTAURANT / CAFE", final_col)
    entrance("WELLNESS_ENTRANCE", 16.0, -80.7, 4.5, 4.4, "EMPLOYEE WELLNESS", final_col)
    entrance("DAYCARE_ENTRANCE", -105.0, -72.3, 4.5, 4.2, "DAYCARE", final_col)
    entrance("PRODUCTION_PERSONNEL_ENTRANCE", 28.0, -16.35, 4.0, 4.0, "PRODUCTION PERSONNEL", final_col)
    entrance("RM_PERSONNEL_ENTRANCE", -76.0, 57.7, 4.0, 4.0, "RAW MATERIALS", final_col)
    entrance("PACKAGING_PERSONNEL_ENTRANCE", -12.0, 57.7, 4.0, 4.0, "PACKAGING", final_col)
    entrance("FG_PERSONNEL_ENTRANCE", 80.0, -55.3, 4.0, 4.0, "FINISHED GOODS", final_col)
    new_objects.extend([name for name in (obj.name for obj in final_col.objects) if "ENTRANCE" in obj.name])

    # Move the existing framing walls laterally so the approach reads:
    # Living Wall | VIP Entrance | Water Wall.
    for obj in bpy.context.scene.objects:
        upper = obj.name.upper()
        if any(term in upper for term in ("POVU_WATER_WALL", "WATERWALL_", "WATER_CURTAIN", "VIP_WATER_", "VIP_WATERFALL", "WATERFALL_LIGHT", "POVU_VIP_SIGN")):
            obj.location.x += 16.0
        elif any(term in upper for term in ("VIP_LIVINGWALL", "LIVING_WALL_PANEL", "LIVING_WALL_FOLIAGE")):
            obj.location.x -= 16.0
    living_wall = bpy.data.objects.get("VIP_LivingWall")
    if living_wall:
        living_wall.location.x = -68.0
        living_wall.location.y = -92.4
        living_wall.dimensions.x = 6.0
        assign(living_wall, MATS["green"])
    for obj in bpy.context.scene.objects:
        if obj.name == "LIVING_WALL_PANEL001" or obj.name in {f"LIVING_WALL_FOLIAGE{index:03d}" for index in range(12, 24)}:
            obj.location.x -= 20.0

    # Smart Totem hierarchy: one flagship plus four restrained campus decision-point totems.
    vip_body = rename_if_present("SMART_TOTEM_PREMIUM_0", "SMART_TOTEM_VIP_BODY")
    vip_screen = rename_if_present("SMART_TOTEM_PREMIUM_SCREEN_0", "SMART_TOTEM_VIP_SCREEN")
    vip_glow = rename_if_present("SMART_TOTEM_PREMIUM_GLOW_0", "SMART_TOTEM_VIP_LIGHT")
    for obj, role in ((vip_body, "SMART_TOTEM_VIP_BODY"), (vip_screen, "SMART_TOTEM_VIP_SCREEN"), (vip_glow, "SMART_TOTEM_VIP_LIGHT")):
        if obj:
            obj.scale.x *= 1.35
            obj.scale.y *= 1.35
            mark(obj, role, "smart_totem", role, type="flagship", location="VIP approach")
    campus_names = []
    for index in range(4):
        suffix = f"{index:02d}"
        body = rename_if_present(f"WAYFIND_TOTEM_{suffix}", f"SMART_TOTEM_CAMPUS_{index + 1:02d}_BODY")
        screen = rename_if_present(f"WAYFIND_SCREEN_{suffix}", f"SMART_TOTEM_CAMPUS_{index + 1:02d}_SCREEN")
        for obj, role in ((body, "body"), (screen, "screen")):
            if obj:
                mark(obj, f"SMART_TOTEM_CAMPUS_{index + 1:02d}_{role.upper()}", "smart_totem", role, type="campus")
        campus_names.append(f"SMART_TOTEM_CAMPUS_{index + 1:02d}")
    hide_group([
        "SMART_TOTEM", "SMART_TOTEM_SCREEN", "SMART_TOTEM_GLOW",
        "SMART_TOTEM001", "SMART_TOTEM001_SCREEN", "SMART_TOTEM001_GLOW",
        "SMART_TOTEM002", "SMART_TOTEM002_SCREEN", "SMART_TOTEM002_GLOW",
        "SMART_TOTEM_PREMIUM_1", "SMART_TOTEM_PREMIUM_SCREEN_1", "SMART_TOTEM_PREMIUM_GLOW_1",
        "WAYFIND_TOTEM_04", "WAYFIND_SCREEN_04",
    ])
    totem_table = [
        {"id": "SMART_TOTEM_VIP", "type": "flagship", "location": "VIP approach / POVU Plaza south edge", "purpose": "welcome and visitor information", "nearest_destination": "VIP Entrance", "reason": "single premium arrival marker"},
        {"id": "SMART_TOTEM_CAMPUS_01", "type": "campus", "location": "Plaza west decision point", "purpose": "wayfinding", "nearest_destination": "Hands of Growth", "reason": "plaza landmark junction"},
        {"id": "SMART_TOTEM_CAMPUS_02", "type": "campus", "location": "Plaza east decision point", "purpose": "wayfinding", "nearest_destination": "HQ / R&D", "reason": "front-of-house destination junction"},
        {"id": "SMART_TOTEM_CAMPUS_03", "type": "campus", "location": "Protected spine / production transition", "purpose": "visitor-to-production guidance", "nearest_destination": "Glass Deck", "reason": "controlled visitor transition"},
        {"id": "SMART_TOTEM_CAMPUS_04", "type": "campus", "location": "Production / logistics edge", "purpose": "safety and service wayfinding", "nearest_destination": "Production Hall", "reason": "industrial circulation decision point"},
    ]

    # Physical Glass Deck access: East stair, West stair, and central stair/lift.
    stair_run("GLASS_DECK_EAST_STAIR", (55.0, 68.0), (0.0, -1.0), 5.0, 12, 1.0, 8.2, final_col, "East stair to Glass Deck")
    stair_run("GLASS_DECK_WEST_STAIR", (-55.0, -28.0), (0.0, 1.0), 5.0, 12, 1.0, 8.2, final_col, "West stair to Glass Deck")
    stair_run("GLASS_DECK_CENTRAL_STAIR", (0.0, 28.0), (0.0, -1.0), 5.0, 12, 1.0, 8.2, final_col, "Central stair to Glass Deck")
    box("GLASS_DECK_CENTRAL_LIFT", (8.0, 20.0, 4.7), (4.0, 4.0, 7.0), MATS["glass"], final_col, "glass_deck_access", "central_lift", purpose="Central stair + lift")
    box("GLASS_DECK_CENTRAL_LIFT_FRAME", (8.0, 20.0, 8.25), (4.3, 4.3, 0.18), MATS["champagne"], final_col, "glass_deck_access", "central_lift_frame", purpose="Central stair + lift")
    new_objects.extend(["GLASS_DECK_EAST_STAIR", "GLASS_DECK_WEST_STAIR", "GLASS_DECK_CENTRAL_STAIR", "GLASS_DECK_CENTRAL_LIFT"])
    for name, role in (("GlassDeck_East", "GLASS_DECK_EAST_ZONE"), ("GlassDeck_West", "GLASS_DECK_WEST_ZONE"), ("GLASS_DECK_LINK", "GLASS_DECK_CENTRAL_LINK")):
        obj = bpy.data.objects.get(name)
        if obj:
            mark(obj, role, "glass_deck", role, access_concept="represented")

    # Face-separated production shell for future roof/wall reveals while preserving the source object hidden.
    new_shell = split_production_shell(bpy.data.objects.get("Production_Hall"), final_col)
    new_objects.extend(obj.name for obj in new_shell)

    # Solar and vegetation semantic grouping.
    for obj in bpy.context.scene.objects:
        upper = obj.name.upper()
        if upper.startswith("SOLAR_ARRAY") or upper.startswith("SOLARPANEL") or upper.startswith("SOLAR_CARPORT_PANEL"):
            mark(obj, "SOLAR_PANEL_SURFACE_" + obj.name, "solar", "SOLAR_PANEL_SURFACE", source=obj.name)
        elif upper.startswith("SOLAR_POST") or upper.startswith("SOLAR_CARPORT_POST"):
            mark(obj, "SOLAR_SUPPORT_" + obj.name, "solar", "SOLAR_SUPPORT", source=obj.name)
        elif "FRAME" in upper and "SOLAR" in upper:
            mark(obj, "SOLAR_PANEL_FRAME_" + obj.name, "solar", "SOLAR_PANEL_FRAME", source=obj.name)
        elif "TREE_TRUNK" in upper:
            mark(obj, "TREE_TRUNK_" + obj.name, "landscape", "TREE_TRUNK", source=obj.name)
        elif "TREE_CROWN" in upper or "FOLIAGE" in upper:
            mark(obj, "TREE_FOLIAGE_" + obj.name, "landscape", "TREE_FOLIAGE", source=obj.name)
        elif any(term in upper for term in ("GRASS", "SHRUB", "PLANTER", "CANOPY_BRANCH")):
            mark(obj, "LANDSCAPE_" + obj.name, "landscape", "LANDSCAPE_ELEMENT", source=obj.name)

    # Reassert landmark semantics after the broad vegetation pass.
    for name, role in (("HOG_TREE_TRUNK", "HOG_TREE_TRUNK"), ("HOG_TREE_CROWN_0", "HOG_TREE_CROWN"), ("HOG_PLINTH", "HOG_PLINTH")):
        obj = bpy.data.objects.get(name)
        if obj:
            mark(obj, role, "hands_of_growth", role, source=name)
    for obj in bpy.context.scene.objects:
        if "LIVING_WALL" in obj.name.upper():
            mark(obj, "LIVING_WALL_" + obj.name, "living_wall", "LIVING_WALL_VEGETATION", source=obj.name)

    # Exact semantic bridge anchors for later Water Wall animation bindings.
    water_roles = {
        "WATER_WALL_STRUCTURE": "POVU_WATER_WALL_7M",
        "WATER_WALL_WATER_SURFACE": "VIP_Waterfall",
        "WATER_WALL_BASIN": "POVU_WATER_WALL_BASIN",
        "WATER_WALL_TOP_FEED": "POVU_WATER_WALL_CREST",
        "WATER_WALL_POVU_SIGNAGE": "POVU_VIP_SIGN",
    }
    for semantic_name, source_name in water_roles.items():
        source = bpy.data.objects.get(source_name)
        if source:
            bridge = empty(semantic_name, source.matrix_world.translation, final_col, "water_wall", semantic_name, source_object=source_name)
            new_objects.append(bridge.name)

    # Machine identities and world-space label anchors.
    for obj in bpy.context.scene.objects:
        upper = obj.name.upper()
        if any(term in upper for term in ("PROCESSTANK_", "MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR", "FILL", "BOTTLE", "CLOSURE", "TRIGGER", "POWDER", "TOOTHPASTE", "WIPES", "CONVEYOR", "PALLET", "AMR", "AGV")):
            mark(obj, "MACHINE_" + obj.name, "machine", "machine_highlight_target", source=obj.name)
    for index in range(1, 12):
        obj = bpy.data.objects.get(f"ProcessTank_{index:02d}")
        if obj:
            anchor = add_label_anchor(f"LABEL_ANCHOR_PROCESS_TANK_{index:02d}", obj, final_col, "world_tracked_machine_label")
            new_objects.append(anchor.name)
    for name in ("MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR", "Bottle_BlowMolding", "Caps_Triggers", "TOOTHPASTE_HOMOGENIZER", "WetWipes", "AMR_SPINE"):
        obj = bpy.data.objects.get(name)
        anchor = add_label_anchor("LABEL_ANCHOR_" + name.upper(), obj, final_col, "world_tracked_machine_label")
        if anchor:
            new_objects.append(anchor.name)

    # Presentation cameras and navigation route targets.
    cameras = {
        "PRES_HANDS_OF_GROWTH": ((-135.0, -116.0, 27.0), (-108.0, -79.0, 5.0), "Hands of Growth hero approach and arc"),
        "PRES_VIP_ENTRANCE": ((-58.0, -116.0, 8.5), (-58.0, -92.0, 4.3), "VIP entrance / Living Wall / Water Wall"),
        "PRES_GLASS_DECK_EAST_ACCESS": ((45.0, 72.0, 5.0), (55.0, 62.0, 4.5), "East Glass Deck stair"),
        "PRES_GLASS_DECK_WEST_ACCESS": ((-58.0, -36.0, 13.0), (-55.0, -17.0, 5.5), "West Glass Deck stair"),
        "PRES_GLASS_DECK_CENTRAL_ACCESS": ((15.0, 32.0, 13.0), (4.0, 20.0, 5.5), "Central stair and lift"),
    }
    for name, (location, target, route) in cameras.items():
        cam = camera(name, location, target, final_col, route)
        new_objects.append(cam.name)
    for route_name, target in {
        "CAMPUS_AERIAL": (0.0, 0.0, 0.0), "MAIN_ARRIVAL": (-85.0, -88.0, 2.0), "VIP_APPROACH": (-58.0, -91.0, 4.0),
        "VIP_ENTRANCE": (-58.0, -79.0, 4.0), "WATER_WALL": (-58.0, -92.5, 4.0), "LIVING_WALL": (-58.0, -91.2, 6.0),
        "HANDS_OF_GROWTH": (-108.0, -79.0, 5.0), "POVU_PLAZA": (-76.0, -77.0, 1.5), "ORGANIC_CANOPY": (-65.0, -55.0, 3.0),
        "GLASS_DECK_EXTERIOR": (25.0, 51.0, 10.0), "GLASS_DECK_INTERIOR": (0.0, 20.0, 10.0), "PRODUCTION_HALL": (0.0, 20.0, 7.0),
        "WET_PROCESSING": (0.0, 20.0, 5.0), "SOLAR_FIELD": (75.0, 104.0, 2.5),
    }.items():
        new_objects.append(empty("NAV_TARGET_" + route_name, target, final_col, "navigation_target", route_name, route=route_name).name)

    # Camera route annotations on existing presentation cameras.
    existing_route_cameras = {
        "PRES_01_CAMPUS_HERO": "Campus aerial", "PRES_02_VIP_APPROACH": "VIP approach", "PRES_03_WATER_ENTRANCE": "Water Wall / VIP entrance",
        "PRES_04_POVU_PLAZA": "POVU Plaza", "PRES_05_EMPLOYEE_CAMPUS": "Employee campus", "PRES_07_GLASS_DECK": "Glass Deck exterior",
        "PRES_08_PROCESS_HALL": "Production Hall", "PRES_15_MIXING_HALL": "Wet Processing", "PRES_16_GLASS_DECK_INTERIOR": "Glass Deck interior",
        "PRES_37_SOLAR": "Solar field", "PRES_38_RESTAURANT_CAFE": "Restaurant / Cafe", "PRES_39_WELLNESS_RECREATION": "Wellness",
        "PRES_40_DAYCARE": "Daycare", "PRES_41_CLINIC": "Occupational health", "PRES_42_EMPLOYEE_GARDENS": "Employee gardens",
    }
    for name, route in existing_route_cameras.items():
        obj = bpy.data.objects.get(name)
        if obj:
            mark(obj, name, "camera", route, route=route)

    # Material semantic registry for future Remotion overrides.
    for key, mat in MATS.items():
        mat["rev004_material_role"] = key
        mat["remotion_override_ready"] = True

    bpy.context.scene["REV004_SOURCE_SHA256"] = source_sha
    bpy.context.scene["REV004_ARCHITECTURAL_STATUS"] = "FINALIZATION_COMPLETE_PENDING_QA"
    bpy.context.scene["REV004_SMART_TOTEM_COUNT"] = 5
    bpy.context.scene["REV004_SMART_TOTEM_FLAGSHIP_COUNT"] = 1
    bpy.context.scene["REV004_SMART_TOTEM_CAMPUS_COUNT"] = 4

    Path(args.blend).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=args.blend)
    bpy.ops.export_scene.gltf(filepath=args.glb, export_format="GLB", export_cameras=True, export_lights=True, export_apply=True)
    build_manifest(args, source_sha, new_objects, totem_table)
    print(json.dumps({
        "source_sha256": source_sha,
        "blend": args.blend,
        "glb": args.glb,
        "glb_sha256": sha256(Path(args.glb)),
        "object_count": len(bpy.data.objects),
        "mesh_object_count": sum(1 for obj in bpy.data.objects if obj.type == "MESH"),
        "material_count": len(bpy.data.materials),
        "camera_count": sum(1 for obj in bpy.data.objects if obj.type == "CAMERA"),
        "new_object_count": len(new_objects),
    }))


if __name__ == "__main__":
    main()
