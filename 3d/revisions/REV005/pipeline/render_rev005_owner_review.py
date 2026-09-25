import bpy
import json
import math
from pathlib import Path
from mathutils import Vector

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT_DIR = ROOT / "output" / "rev005-owner-interior-review"
VIDEO = OUT_DIR / "POVU_REV005_OWNER_INTERIOR_REVIEW.mp4"
FRAME_DIR = OUT_DIR / "review_frames_v03"
VIDEO_FRAME_DIR = OUT_DIR / "video_frames_v03"
PLAN = OUT_DIR / "REV005_OWNER_INTERIOR_CAMERA_PLAN.json"

FPS = 30
SEGMENT_FRAMES = 60
TRANSITION_FRAMES = 8

# These are the actual tagged facility groups discovered in the canonical
# REV005_INTERIOR_COMPLETION collection. The review deliberately uses those
# groups as its inventory rather than inventing a smaller hand-picked route.
GROUPS = [
    ("Administration / HQ / R&D / QC", "Administration / HQ / R&D / QC", ("ADMIN", "HQ", "QC", "R&D", "OFFICE", "MEETING", "RECEPTION", "LAB")),
    ("Bottle blow molding", "Bottle Blow Molding", ("BLOW", "BOTTLE")),
    ("Caps and trigger assembly", "Caps and Trigger Assembly", ("CAP", "TRIGGER")),
    ("Chemical compound / controlled receiving", "Chemical Compound / Controlled Receiving", ("CHEMICAL",)),
    ("Daycare / crèche", "Daycare / Crèche", ("DAYCARE",)),
    ("ETP / water treatment", "ETP / Water Treatment", ("ETP", "MBBR", "FILTER", "WATER_TREAT")),
    ("Electrical / LV-MV room", "Electrical / LV-MV Room", ("LV_MV", "ELECTRICAL")),
    ("Employee changing / shower / locker support", "Employee Changing / Shower / Locker Support", ("LOCKER", "SHOWER", "CHANGING")),
    ("Finished goods warehouse / dispatch", "Finished Goods Warehouse / Dispatch", ("FG_", "FINISHED", "DISPATCH")),
    ("Fire pump house", "Fire Pump House", ("FIRE_PUMP", "FIRE PUMP")),
    ("Glass Deck central command / training / café gallery", "Central Glass Deck Command / Training / Café Gallery", ("GLASS_DECK_LINK", "COMMAND", "SKY_CAFE")),
    ("Liquid filling / packaging", "Liquid Filling / Packaging", ("LIQUID", "FILLING")),
    ("Micro-ingredient weigh / dispense", "Micro-ingredient Weigh / Dispense", ("WEIGH", "DISPENSE")),
    ("Occupational health / first aid", "Occupational Health / First Aid", ("CLINIC", "OCCUPATIONAL", "FIRST_AID")),
    ("Packaging warehouse", "Packaging Warehouse", ("PACKAGING", "PK_")),
    ("Powder handling / packing", "Powder Handling / Packing", ("POWDER",)),
    ("Production Hall / Wet Processing / process core", "Production Hall / Wet Processing", ("PROCESS", "TANK", "MIX", "FILL", "PACK", "WIPES", "TOOTHPASTE", "BLOW", "INJECTION", "CAP", "TRIGGER", "PRODUCTION_FLOOR")),
    ("Raw material warehouse / receiving", "Raw Material Warehouse / Receiving", ("RM_", "RAW MATERIAL", "RECEIVING")),
    ("Restaurant / POVU Café / kitchen", "Restaurant / POVU Café / Kitchen", ("RESTAURANT", "CAFE", "KITCHEN")),
    ("Security / reception / visitor arrival", "Security / Reception / Visitor Arrival", ("SECURITY", "VIP", "RECEPTION", "VISITOR", "ARRIVAL")),
    ("Security gatehouse", "Security Gatehouse", ("GATEHOUSE", "SECURITY")),
    ("Toothpaste production", "Toothpaste Production", ("TOOTHPASTE",)),
    ("Training / Academy", "Training / Academy", ("ACADEMY", "STUDIO", "TRAINING", "CLASSROOM")),
    ("Utilities / engineering", "Utilities / Engineering", ("UTILITY", "BOILER", "RO_", "COMPRESSOR", "GENERATOR", "STEAM", "AIR_")),
    ("Wellness / recreation", "Wellness / Recreation", ("WELLNESS", "GYM", "YOGA", "LOCKER", "SHOWER")),
    ("Wet wipes production", "Wet Wipes Production", ("WIPES",)),
]

SHELL_ROOTS = {
    "ADMIN_RD_QC", "BOTTLE_BLOWMOLDING", "CAPS_TRIGGERS", "CHEMICAL_COMPOUND", "CLINIC", "DAYCARE", "ETP",
    "FG_WAREHOUSE", "LIQUID_PACKING", "PACKAGING_WAREHOUSE", "POWDER_PACKAGING", "PRODUCTION_HALL", "RESTAURANT_WELLNESS",
    "RM_WAREHOUSE", "TOOTHPASTE", "UTILITY_HOUSE", "WETWIPES", "WELLNESS_PAVILION", "MULTIPURPOSE_STUDIO",
    "SECURITY_GATEHOUSE", "FIRE_PUMP_HOUSE", "FIRE_PUMP_HOUSE001", "LV_MV_ROOM", "GLASSDECK_EAST", "GLASSDECK_WEST",
}

ANCHORS = {
    "Administration / HQ / R&D / QC": ((-58, -64), 30),
    "Bottle blow molding": ((52, 10), 28),
    "Caps and trigger assembly": ((52, 31), 28),
    "Chemical compound / controlled receiving": ((56, 80), 36),
    "Daycare / crèche": ((-105, -64), 30),
    "ETP / water treatment": ((110, 34), 36),
    "Electrical / LV-MV room": ((111, 61), 24),
    "Employee changing / shower / locker support": ((30, -70), 28),
    "Finished goods warehouse / dispatch": ((80, -25), 55),
    "Fire pump house": ((112, -9), 28),
    "Glass Deck central command / training / café gallery": ((70, 20), 44),
    "Liquid filling / packaging": ((10, -2), 44),
    "Micro-ingredient weigh / dispense": ((-5, 50), 28),
    "Occupational health / first aid": ((-18, -94), 28),
    "Packaging warehouse": ((-12, 79), 62),
    "Powder handling / packing": ((-48, 43), 34),
    "Production Hall / Wet Processing / process core": ((0, 20), 62),
    "Raw material warehouse / receiving": ((-76, 79), 62),
    "Restaurant / POVU Café / kitchen": ((5, -68), 38),
    "Security / reception / visitor arrival": ((-58, -84), 34),
    "Security gatehouse": ((96, -106), 28),
    "Toothpaste production": ((-12, 43), 34),
    "Training / Academy": ((30, -61), 28),
    "Utilities / engineering": ((96, 75), 50),
    "Wellness / recreation": ((30, -70), 30),
    "Wet wipes production": ((22, 43), 38),
}

def upper(value):
    return value.upper().replace("-", "_")

def is_shell(obj):
    current = obj
    while current:
        if upper(current.name) in SHELL_ROOTS:
            return True
        current = current.parent
    name = upper(obj.name)
    return name.endswith(("_ROOF", "_WALL_NORTH", "_WALL_SOUTH", "_WALL_EAST", "_WALL_WEST"))

def is_renderable(obj):
    return obj.type in {"MESH", "CURVE", "SURFACE", "FONT"}

def bbox(objects):
    points = []
    for obj in objects:
        if not is_renderable(obj):
            continue
        points.extend(obj.matrix_world @ Vector(corner) for corner in obj.bound_box)
    if not points:
        return Vector((0, 0, 1.5)), Vector((10, 10, 4))
    low = Vector((min(point.x for point in points), min(point.y for point in points), min(point.z for point in points)))
    high = Vector((max(point.x for point in points), max(point.y for point in points), max(point.z for point in points)))
    return (low + high) * 0.5, high - low

def pose(position, target):
    direction = Vector(target) - Vector(position)
    quaternion = direction.to_track_quat("-Z", "Y")
    return Vector(position), quaternion.to_euler()

def add_keyframe(camera, frame, position, target):
    location, rotation = pose(position, target)
    camera.location = location
    camera.rotation_euler = rotation
    camera.keyframe_insert(data_path="location", frame=frame)
    camera.keyframe_insert(data_path="rotation_euler", frame=frame)

def object_group(obj, group_key):
    return str(obj.get("rev005_facility", "")).strip() == group_key

def build_segment(group_key, label, terms, all_objects):
    tagged = [obj for obj in all_objects if object_group(obj, group_key)]
    anchor_xy, source_radius = ANCHORS[group_key]
    anchor = Vector((anchor_xy[0], anchor_xy[1], 0))
    source = []
    for obj in all_objects:
        if not is_renderable(obj) or is_shell(obj) or object_group(obj, group_key):
            continue
        name = upper(obj.name)
        obj_center, _ = bbox([obj])
        if any(term in name for term in terms) and (Vector((obj_center.x, obj_center.y, 0)) - anchor).length <= source_radius:
            source.append(obj)
    selected = sorted({obj.name: obj for obj in tagged + source}.values(), key=lambda item: item.name)
    focus = [obj for obj in selected if not upper(obj.name).endswith("_FLOOR") and "LABEL" not in upper(obj.name)]
    if not focus:
        focus = selected
    center, dimensions = bbox(focus)
    if not selected:
        raise RuntimeError(f"No objects resolved for canonical facility group: {group_key}")
    scale = max(float(dimensions.x), float(dimensions.y), 8.0)
    wide_distance = max(scale * 0.9, 12.0)
    detail_distance = max(min(scale * 0.38, 30.0), 6.5)
    detail = focus[min(len(focus) - 1, max(0, len(focus) // 2))]
    detail_center, detail_dimensions = bbox([detail])
    if detail_dimensions.length < 0.1:
        detail_center = center
    target_a = center + Vector((0, 0, max(1.2, min(4.0, float(dimensions.z) * 0.28))))
    target_b = detail_center + Vector((0, 0, max(1.3, min(3.0, float(detail_dimensions.z) * 0.45))))
    position_a = center + Vector((wide_distance * 0.82, -wide_distance, max(7.0, wide_distance * 0.58)))
    position_mid = center + Vector((wide_distance * 0.52, -wide_distance * 0.78, max(5.0, wide_distance * 0.42)))
    position_b = detail_center + Vector((detail_distance * 0.72, -detail_distance, max(4.5, detail_distance * 0.62)))
    return {
        "group_key": group_key,
        "label": label,
        "selected_names": [obj.name for obj in selected],
        "tagged_count": len(tagged),
        "source_count": len(source),
        "center": [round(float(v), 3) for v in center],
        "dimensions": [round(float(v), 3) for v in dimensions],
        "target_a": [round(float(v), 3) for v in target_a],
        "target_b": [round(float(v), 3) for v in target_b],
        "position_a": [round(float(v), 3) for v in position_a],
        "position_mid": [round(float(v), 3) for v in position_mid],
        "position_b": [round(float(v), 3) for v in position_b],
    }

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_FRAME_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND), load_ui=False)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.background_type = "WORLD"
    scene.render.film_transparent = False
    scene.camera = bpy.data.objects.get("REV005_OWNER_REVIEW_CAMERA")
    if scene.camera:
        bpy.data.objects.remove(scene.camera, do_unlink=True)
    bpy.ops.object.camera_add(location=(0, -40, 20))
    camera = bpy.context.object
    camera.name = "REV005_OWNER_REVIEW_CAMERA"
    camera.data.lens = 47
    camera.data.clip_end = 2000
    scene.camera = camera

    renderables = [obj for obj in bpy.data.objects if is_renderable(obj)]
    segments = []
    for group_key, label, terms in GROUPS:
        segments.append(build_segment(group_key, label, terms, renderables))
    for segment_index, segment in enumerate(segments):
        start = segment_index * (SEGMENT_FRAMES + TRANSITION_FRAMES)
        mid = start + SEGMENT_FRAMES // 2
        end = start + SEGMENT_FRAMES - 1
        segment["start_frame"] = start
        segment["mid_frame"] = mid
        segment["end_frame"] = end
        add_keyframe(camera, start, segment["position_a"], segment["target_a"])
        add_keyframe(camera, mid, segment["position_mid"], segment["target_a"])
        add_keyframe(camera, end, segment["position_b"], segment["target_b"])
    # Blender 5.2 stores keyframes behind layered Actions; the default
    # Bezier interpolation is sufficient for the smooth review route.

    visibility = {segment["start_frame"]: set(segment["selected_names"]) for segment in segments}
    visibility_by_frame = {}
    for segment in segments:
        for frame in range(segment["start_frame"], segment["end_frame"] + 1):
            visibility_by_frame[frame] = set(segment["selected_names"])

    old_world = tuple(scene.world.color) if scene.world else (0.08, 0.08, 0.08)
    if scene.world is None:
        scene.world = bpy.data.worlds.new("REV005_REVIEW_WORLD")
    world = scene.world

    def update_visibility(scene_arg):
        frame = scene_arg.frame_current
        active = visibility_by_frame.get(frame, set())
        for obj in renderables:
            obj.hide_render = obj.name not in active
        if active:
            world.color = (0.48, 0.55, 0.62)
        else:
            world.color = (0.005, 0.005, 0.005)

    bpy.app.handlers.frame_change_pre.clear()
    bpy.app.handlers.frame_change_pre.append(update_visibility)

    plan = {
        "revision": "REV005",
        "source_blend": str(BLEND),
        "video": str(VIDEO),
        "fps": FPS,
        "segment_frames": SEGMENT_FRAMES,
        "transition_frames": TRANSITION_FRAMES,
        "facility_count": len(segments),
        "segments": segments,
    }
    PLAN.write_text(json.dumps(plan, indent=2), encoding="utf-8")

    # Representative evidence: one orientation frame and one functional frame
    # for every canonical facility group, rendered before the MP4.
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    for segment in segments:
        for view_name, frame in (("A", segment["start_frame"] + 32), ("B", segment["mid_frame"] + 32)):
            scene.frame_set(frame)
            scene.render.filepath = str(FRAME_DIR / f"{segment['start_frame']:05d}_{view_name}_{segment['label'].replace('/', '_').replace(' ', '_')}.png")
            bpy.ops.render.render(write_still=True)

    # Workbench source frames are rendered at half target dimensions for
    # throughput; ffmpeg performs the final 1920x1080 H.264 encode with a
    # high-quality scaler after this review-only render completes.
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    # Blender 5.2 omits the FFMPEG image-setting enum in this build. Render
    # the locked-scene frames losslessly; the caller encodes them with the
    # installed ffmpeg binary without touching the canonical blend.
    scene.render.image_settings.file_format = "PNG"
    scene.render.fps = FPS
    scene.frame_start = 0
    scene.frame_end = segments[-1]["end_frame"]
    scene.render.filepath = str(VIDEO_FRAME_DIR / "frame_")
    scene.frame_set(0)
    bpy.ops.render.render(animation=True)
    world.color = old_world
    print(json.dumps({"video": str(VIDEO), "frames": scene.frame_end - scene.frame_start + 1, "facility_count": len(segments), "frame_dir": str(FRAME_DIR), "video_frame_dir": str(VIDEO_FRAME_DIR)}, indent=2))

if __name__ == "__main__":
    main()
