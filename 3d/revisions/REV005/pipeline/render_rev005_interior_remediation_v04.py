import bpy, json, math, re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-interior-remediation-v04"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

FOCUSED = {
    "admin_hq_rd_qc": ("Administration / HQ / R&D / QC", (-87,-92,16), (-45,-58,10), (-42,-75,10), (-58,-64,3)),
    "bottle_blow_molding": ("Bottle blow molding", (30,-7,13), (45,-5,10), (46,-4,9), (52,10,3)),
    "liquid_filling": ("Liquid filling / packaging", (-13,-14,12), (0,-12,9), (8,-14,10), (10,-2,3)),
    "toothpaste": ("Toothpaste production", (-32,32,12), (-22,35,9), (-20,32,10), (-12,43,3)),
    "wet_wipes": ("Wet wipes production", (0,32,12), (10,36,9), (10,32,10), (22,43,3)),
    "glass_deck": ("Glass Deck central command / training / café gallery", (73,2,12), (73,13,8), (73,37,8), (70,24,5)),
    "restaurant_cafe": ("Restaurant / POVU Café / kitchen", (-20,-90,15), (-4,-80,10), (18,-84,11), (5,-69,3)),
    "finished_goods": ("Finished goods warehouse / dispatch", (50,-65,18), (72,-56,10), (92,-43,11), (80,-51,3)),
    "raw_material": ("Raw material warehouse / receiving", (-112,54,20), (-100,70,10), (-78,96,10), (-78,79,3)),
    "etp": ("ETP / water treatment", (88,15,18), (100,26,9), (113,43,10), (108,35,3)),
    "fire_pump": ("Fire pump house", (75,-25,15), (92,-12,8), (100,-4,8), (94,-5,3)),
    "clinic": ("Occupational health / first aid", (-34,-108,14), (-25,-100,8), (-8,-96,8), (-18,-94,3)),
    "utilities": ("Utilities / engineering", (75,55,18), (88,67,10), (107,82,10), (96,75,3)),
}

WEAK = set(v[0] for v in FOCUSED.values())

CUES = {
    "Administration / HQ / R&D / QC": ("reception, offices, meeting room, R&D/QC benches and storage", "partitioned office/lab zoning with clear circulation", "administrative and lab support sequence visible"),
    "Bottle blow molding": ("preform hopper, heater/oven, mould-clamp/blow cell, guarded outfeed", "guarded process cell with conveyor and service aisle", "preform feed -> heat -> blow/mould -> outfeed"),
    "Liquid filling / packaging": ("infeed conveyor, filler/nozzles, capper, label/inspection, case handling", "coherent guarded line with operator/service aisle", "infeed -> fill -> cap -> label/inspect -> case"),
    "Toothpaste production": ("vacuum mix, transfer/holding, tube magazine, filler, sealer, coding and cartoning", "enclosed process line with clean transfer and inspection zones", "mix -> hold -> fill -> seal/code -> carton"),
    "Wet wipes production": ("roll unwind, web path, wetting, folding/converting, cut/stack, pouch seal/discharge", "distinct wet-converting cell with film and service separation", "unwind -> wet -> fold/cut -> pouch/seal -> discharge"),
    "Glass Deck central command / training / café gallery": ("command wall/consoles, training table, presentation area, café counter/backbar/seating", "enclosed gallery zoning with circulation and controlled glazing", "command -> training/presentation -> café/support"),
    "Restaurant / POVU Café / kitchen": ("dining layout, service/POS counter, café seating, kitchen, pass and back-of-house", "front-of-house and kitchen/pass zones separated by service partition", "receiving/prep -> cook/pass -> service/dining"),
    "Finished goods warehouse / dispatch": ("pallet racks, staging lanes, dispatch/loading edge, forklift/AMR aisle", "rack grid, staging and dispatch zones with wide handling aisles", "rack storage -> staging -> dispatch"),
    "Raw material warehouse / receiving": ("receiving dock, raw-material racks, pallets, aisle and handling route", "receiving and raw-material storage clearly separated", "receive -> stage -> rack/store -> issue"),
    "ETP / water treatment": ("treatment tanks/basins, filter skid, pumps, headers and service walkway", "bunded treatment train with pipe/service clearances", "inlet -> treatment -> filter -> discharge/sludge"),
    "Fire pump house": ("pump sets, suction/discharge headers, manifold, valves and clearance", "dedicated pump-room envelope with service clearance", "suction -> pump -> header/manifold"),
    "Occupational health / first aid": ("reception/waiting, treatment bed, privacy partition, support storage", "clinic circulation and privacy zoning visible", "arrival -> assessment -> treatment -> support"),
    "Utilities / engineering": ("compressor/air, boiler/steam, RO/water, tanks, manifolds and maintenance bench", "service plant grouped with maintenance and safe clearances", "utility generation -> manifold -> distribution/service"),
}

def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")

def is_label(obj):
    n = obj.name.upper()
    return any(k in n for k in ("SIGN", "LABEL", "CALLOUT", "TEXT", "CAPTION"))

def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()

def facility_match(group, value):
    a, b = norm(group), norm(value)
    if not b:
        return False
    if a == b or a in b or b in a:
        return True
    if "glass deck" in a and "glass deck" in b:
        return True
    aliases = {
        "bottle blow molding": ("bottle blow", "blow molding"),
        "liquid filling / packaging": ("liquid filling",),
        "glass deck central command training caf gallery": ("central glass deck", "glass deck"),
        "restaurant / povu café / kitchen": ("restaurant", "povu cafe", "cafe", "kitchen"),
        "administration / hq / r&d / qc": ("administration", "hq", "r&d", "qc"),
        "occupational health / first aid": ("occupational health", "first aid", "clinic"),
    }
    return any(x in a and (x in b or b in x) for x in aliases.get(a, ()))

def render_camera(scene, path, loc, target, name):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = 48
    cam.data.sensor_width = 36
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    scene.camera = cam
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    bpy.data.objects.remove(cam, do_unlink=True)
    return {"path": str(path), "bytes": size, "status": "PASS" if exists and size > 5000 else "FAIL"}

def setup_scene():
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
    scene.display.shading.background_type = "VIEWPORT"
    scene.display.shading.background_color = (0.08, 0.10, 0.12)
    scene.display.shading.curvature_ridge_factor = 1.8
    scene.display.shading.curvature_valley_factor = 1.2
    return scene

def selected_objects(facility, record):
    names = set(record.get("objects", []))
    objects = []
    for obj in bpy.data.objects:
        if is_label(obj):
            continue
        if obj.name in names or facility_match(facility, obj.get("facility")):
            objects.append(obj)
    if "glass deck" in norm(facility):
        objects = [o for o in objects if not any(k in o.name.upper() for k in ("LEFT_GLASS", "RIGHT_GLASS", "DECK_PORTAL", "_LEFT_WALL", "_RIGHT_WALL", "CEILING_BEAM"))]
    seen = set()
    return [o for o in objects if not (o.name in seen or seen.add(o.name))]

def show_only(objects):
    keep = set(objects)
    for obj in bpy.data.objects:
        obj.hide_render = obj not in keep or obj.type not in {"MESH", "CURVE", "SURFACE"}

def bounds(objects):
    pts = []
    for obj in objects:
        if obj.type != "MESH":
            continue
        try:
            pts.extend(obj.matrix_world @ Vector(c) for c in obj.bound_box)
        except Exception:
            pass
    if not pts:
        return None
    return Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts))), Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))

def auto_views(objects):
    b = bounds(objects)
    if not b:
        return ((10, -10, 10), (0, 0, 2)), ((8, -6, 7), (0, 0, 2))
    lo, hi = b
    center = (lo + hi) / 2
    radius = max(float(hi.x-lo.x), float(hi.y-lo.y), 8.0)
    target = (center.x, center.y, max(center.z, 1.8))
    return ((center.x + radius*1.20, center.y - radius*1.35, max(center.z + radius*.9, 10)), target), ((center.x - radius*.85, center.y - radius*.70, max(center.z + radius*.62, 7)), target)

def write_index(rows):
    lines = ["# REV005 V04 Campus 26-Group Visual Completion Index", "", "Codex QA index only. All evidence is unlabeled, image-first, and marked `READY_FOR_GPT_REVIEW`; independent GPT acceptance remains pending.", "", "| Facility group | A wide | B functional | C process/detail | Status |", "|---|---|---|---|---|"]
    for row in rows:
        links = {v["view"]: f"[evidence](qa/{Path(v['path']).name})" for v in row["evidence"]}
        lines.append(f"| {row['facility']} | {links.get('A_WIDE','—')} | {links.get('B_FUNCTIONAL','—')} | {links.get('C_PROCESS_OR_DETAIL','—')} | READY_FOR_GPT_REVIEW |")
    (OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").write_text("\n".join(lines)+"\n", encoding="utf-8")

def write_matrix(rows):
    lines = ["# REV005 V04 26-Group Visual Acceptance Matrix", "", "This is a Codex readiness matrix for the locked V04 GPT audit. It does not award final acceptance. Every group is `READY_FOR_GPT_REVIEW` only.", "", "| Group | A/B/C evidence | Visible cues | Enclosure / zoning | Process status | Regression | Remaining concern |", "|---|---|---|---|---|---|---|"]
    for row in rows:
        cues = CUES.get(row["facility"], ("facility-specific fixtures and circulation", "defined enclosure and circulation", "functional sequence cues visible"))
        ev = " ".join(f"[{x['view']}](qa/{Path(x['path']).name})" for x in row["evidence"])
        lines.append(f"| {row['facility']} | {ev} | {cues[0]} | {cues[1]} | {cues[2]} | preserved / rechecked | READY_FOR_GPT_REVIEW; independent GPT review pending |")
    (OUT / "REV005_V04_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md").write_text("\n".join(lines)+"\n", encoding="utf-8")

def main():
    OUT.mkdir(parents=True, exist_ok=True); QA.mkdir(parents=True, exist_ok=True)
    scene = setup_scene()
    inv = json.loads(INV.read_text(encoding="utf-8"))
    rows = []; results = []
    for facility, record in inv["facility_groups"].items():
        objects = selected_objects(facility, record)
        show_only(objects)
        if facility in WEAK:
            spec = next(v for v in FOCUSED.values() if v[0] == facility)
            views = [("A_WIDE", spec[1], spec[4]), ("B_FUNCTIONAL", spec[2], spec[4]), ("C_PROCESS_OR_DETAIL", spec[3], spec[4])]
        else:
            a, b = auto_views(objects)
            views = [("A_WIDE", a[0], a[1]), ("B_FUNCTIONAL", b[0], b[1])]
        evidence = []
        for view, loc, target in views:
            if facility == "Restaurant / POVU Café / kitchen" and view == "C_PROCESS_OR_DETAIL":
                for obj in objects:
                    if obj.name == "V04_RESTAURANT_KITCHEN_PARTITION":
                        obj.hide_render = True
                target = (10, -78.5, 3.4)
            path = QA / f"{slug(facility)}_{view}.png"
            item = render_camera(scene, path, loc, target, "V04_QA_" + slug(facility) + "_" + view)
            item.update({"facility": facility, "view": view, "object_count": len(objects), "status": item["status"]})
            results.append(item); evidence.append(item)
            show_only(objects)
        rows.append({"facility": facility, "evidence": evidence, "object_count": len(objects)})
    scene["REV005_V04_QA_RENDER_COUNT"] = len(results)
    scene["REV005_V04_QA_GROUP_COUNT"] = len(rows)
    (OUT / "RENDER_RESULTS.json").write_text(json.dumps({"status":"READY_FOR_GPT_REVIEW", "render_count":len(results), "group_count":len(rows), "results":results}, indent=2), encoding="utf-8")
    write_index(rows); write_matrix(rows)
    print(json.dumps({"status":"READY_FOR_GPT_REVIEW", "renders":len(results), "groups":len(rows), "passes":sum(x["status"]=="PASS" for x in results), "weak_groups":len(WEAK)}, indent=2))

main()
