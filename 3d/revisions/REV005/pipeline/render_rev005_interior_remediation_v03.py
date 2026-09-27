import bpy, json, math, re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
BLEND = ROOT / "3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT = ROOT / "output/rev005-interior-remediation-v03"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
FOCUSED = {
    "01_blow_molding": ("Bottle Blow Molding", (30,-7,13), (45,-5,10), (46,-4,9), (52,10,3)),
    "02_liquid_filling": ("Liquid Filling / Packaging", (-13,-14,12), (0,-12,9), (8,-14,10), (10,-2,3)),
    "03_toothpaste": ("Toothpaste Production", (-32,32,12), (-22,35,9), (-20,32,10), (-12,43,3)),
    "04_wet_wipes": ("Wet Wipes Production", (0,32,12), (10,36,9), (10,32,10), (22,43,3)),
    "05_glass_deck": ("Central Glass Deck Command / Training / Café Gallery", (84,1,28), (78,9,18), (78,34,19), (70,24,12)),
    "06_restaurant_cafe": ("Restaurant / POVU Café / kitchen", (-20,-90,15), (-4,-80,10), (18,-84,11), (5,-69,3)),
    "07_daycare": ("Daycare / crèche", (-125,-78,14), (-115,-68,9), (-102,-72,9), (-105,-64,3)),
}
REG_PREFIXES = {
    "Restaurant / POVU Café / kitchen": ("REV005_RESTAURANT", "REV005_CAFE", "REV005_KITCHEN", "REV005_DINING", "V03_RESTAURANT"),
    "Daycare / crèche": ("REV005_DAYCARE", "V03_DAYCARE"),
}

def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")

def box_mesh(name, loc, dims, material):
    x, y, z = [v / 2 for v in dims]
    vs = [(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]
    fs = [(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    me = bpy.data.meshes.new(name + "_MESH")
    me.from_pydata(vs, [], fs); me.update()
    obj = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = loc
    obj.data.materials.append(material)
    return obj

def camera(name, loc, target):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = 48
    cam.data.sensor_width = 36
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    return cam

def render(scene, path, loc, target, name):
    cam = camera(name, loc, target)
    scene.camera = cam
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    bpy.data.objects.remove(cam, do_unlink=True)
    return {"path": str(path), "bytes": size, "status": "PASS" if exists and size > 5000 else "FAIL"}

def base_setup():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 900
    scene.render.resolution_y = 600
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.curvature_ridge_factor = 1.8
    scene.display.shading.curvature_valley_factor = 1.2
    return scene

def is_label(obj):
    n = obj.name.upper()
    return any(k in n for k in ("SIGN", "LABEL", "CALLOUT", "TEXT", "CAPTION"))

def show_objects(objects):
    selected = set(objects)
    for obj in bpy.data.objects:
        obj.hide_render = obj not in selected or obj.type not in {"MESH", "CURVE", "SURFACE", "FONT"}
    for obj in selected:
        obj.hide_render = False

def matching_facility(facility):
    objects = []
    prefixes = REG_PREFIXES.get(facility, ())
    for obj in bpy.data.objects:
        if is_label(obj):
            continue
        if obj.get("facility") == facility or (prefixes and any(obj.name.startswith(p) for p in prefixes)):
            objects.append(obj)
    if "Central Glass Deck" in facility:
        objects = [o for o in objects if not any(k in o.name for k in ("LEFT_GLASS", "RIGHT_GLASS", "DECK_PORTAL"))]
    return objects

def facility_metadata_match(group, obj_facility):
    if not obj_facility:
        return False
    a = re.sub(r"[^a-z0-9]+", " ", group.lower()).strip()
    b = re.sub(r"[^a-z0-9]+", " ", obj_facility.lower()).strip()
    if a == b or a in b or b in a:
        return True
    return ("glass deck" in a and "central glass deck" in b) or ("central glass deck" in a and "glass deck" in b)

def add_qa_floor(key, center, width=30, depth=20):
    mat = bpy.data.materials.get("REV005_V03_FLOOR") or bpy.data.materials.new("V03_QA_FLOOR")
    floor = box_mesh("V03_QA_FLOOR_" + key, (center[0], center[1], 1.08), (width, depth, .10), mat)
    return floor

def world_bounds(objects):
    pts = []
    for obj in objects:
        if obj.type != "MESH" or obj.hide_render:
            continue
        try:
            pts.extend([obj.matrix_world @ Vector(c) for c in obj.bound_box])
        except Exception:
            continue
    if not pts:
        return None
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi

def main():
    OUT.mkdir(parents=True, exist_ok=True); QA.mkdir(parents=True, exist_ok=True)
    scene = base_setup()
    v03 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V03")
    v02 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V02")
    results = []
    for key, (facility, wide, functional, process, center) in FOCUSED.items():
        objs = matching_facility(facility)
        show_objects(objs)
        floor = None
        if not any(o.name.startswith("V03_") and o.get("facility") == facility for o in objs):
            floor = add_qa_floor(key, center, 28 if key != "07_glass_deck" else 10, 20 if key != "07_glass_deck" else 48)
            floor.hide_render = False
        for view, loc, target in (("A_WIDE", wide, center), ("B_FUNCTIONAL", functional, center), ("C_PROCESS_OR_DETAIL", process, center)):
            if facility == "Restaurant / POVU Café / kitchen" and view == "C_PROCESS_OR_DETAIL":
                for obj in objs:
                    if obj.name == "V03_RESTAURANT_KITCHEN_PARTITION":
                        obj.hide_render = True
                target = (10, -78.5, 3.4)
            path = QA / (key + "_" + view + ".png")
            row = render(scene, path, loc, target, "V03_QA_" + key + "_" + view)
            row.update({"kind": "focused", "target": facility, "view": view})
            results.append(row)
        if floor:
            bpy.data.objects.remove(floor, do_unlink=True)
    # One unlabeled visual proof for every canonical facility group.
    inv = json.loads(INV.read_text(encoding="utf-8"))
    group_rows = []
    for facility, record in inv["facility_groups"].items():
        names = set(record.get("objects", []))
        objs = [bpy.data.objects[n] for n in names if n in bpy.data.objects and not is_label(bpy.data.objects[n])]
        objs += [o for o in bpy.data.objects if facility_metadata_match(facility, o.get("facility")) and not is_label(o)]
        if "Glass Deck" in facility:
            objs = [o for o in objs if not any(k in o.name for k in ("LEFT_GLASS", "RIGHT_GLASS", "DECK_PORTAL"))]
        # For hospitality groups, inventory object names are authoritative and the V03 additions use facility metadata.
        seen = set(); objs = [o for o in objs if not (o.name in seen or seen.add(o.name))]
        show_objects(objs)
        bounds = world_bounds(objs)
        if bounds is None:
            group_rows.append({"facility": facility, "status": "FAIL", "reason": "no_renderable_geometry"})
            continue
        lo, hi = bounds; center = (lo + hi) / 2; dims = hi - lo
        radius = max(float(dims.x), float(dims.y), 8.0)
        if "Glass Deck" in facility:
            loc = (84, 1, 28); target = (70, 24, 11)
        else:
            loc = (center.x + radius * 1.25, center.y - radius * 1.45, max(center.z + radius * .95, 10.0))
            target = (center.x, center.y, max(center.z, 1.8))
        path = QA / ("26GROUP_" + slug(facility) + ".png")
        row = render(scene, path, loc, target, "V03_QA_26GROUP_" + slug(facility))
        row.update({"kind": "campus_26_group", "target": facility, "object_count": len(objs)})
        results.append(row); group_rows.append(row)
    scene["REV005_V03_QA_RENDER_COUNT"] = len(results)
    (OUT / "RENDER_RESULTS.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    (OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").write_text(
        "# REV005 V03 Campus-Wide Visual Completion Index\n\n"
        "Unlabeled Workbench QA renders for the 26 canonical facility groups. The facility names below are index metadata only; the renders contain no facility-identifying callouts.\n\n"
        + "\n".join("| %s | [%s](qa/%s) | %s |" % (r["target"], Path(r["path"]).name, Path(r["path"]).name, r.get("status", "FAIL")) for r in group_rows)
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"renders": len(results), "focused": sum(r["kind"] == "focused" for r in results), "campus_groups": len(group_rows), "passes": sum(r.get("status") == "PASS" for r in results), "group_passes": sum(r.get("status") == "PASS" for r in group_rows)}, indent=2))

main()
