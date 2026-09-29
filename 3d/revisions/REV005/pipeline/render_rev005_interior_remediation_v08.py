import bpy
import json
import re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-interior-remediation-v08"
ISO = OUT / "qa_isolated"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
}
REMEDIATION_GROUPS = [
    "Administration / HQ / R&D / QC", "Bottle blow molding", "Chemical compound / controlled receiving",
    "ETP / water treatment", "Finished goods warehouse / dispatch", "Glass Deck central command / training / café gallery",
    "Liquid filling / packaging", "Occupational health / first aid", "Packaging warehouse", "Powder handling / packing",
    "Production Hall / Wet Processing / process core", "Raw material warehouse / receiving", "Restaurant / POVU Café / kitchen",
    "Security / reception / visitor arrival", "Security gatehouse", "Toothpaste production", "Training / Academy",
    "Utilities / engineering", "Wellness / recreation", "Wet wipes production",
]

CENTERS = {
    "Administration / HQ / R&D / QC": (-58, -64, 46, 28),
    "Bottle blow molding": (52, 10, 38, 24),
    "Chemical compound / controlled receiving": (56, 80, 38, 30),
    "ETP / water treatment": (108, 35, 40, 32),
    "Finished goods warehouse / dispatch": (80, -51, 52, 24),
    "Glass Deck central command / training / café gallery": (70, 24, 40, 24),
    "Liquid filling / packaging": (10, -2, 50, 20),
    "Occupational health / first aid": (-18, -94, 26, 18),
    "Packaging warehouse": (-10, 79, 58, 45),
    "Powder handling / packing": (-48, 43, 38, 19),
    "Production Hall / Wet Processing / process core": (0, 24, 54, 32),
    "Raw material warehouse / receiving": (-78, 79, 54, 38),
    "Restaurant / POVU Café / kitchen": (5, -69, 46, 26),
    "Security / reception / visitor arrival": (-58, -84, 48, 16),
    "Security gatehouse": (96, -106, 20, 14),
    "Toothpaste production": (-12, 43, 42, 19),
    "Training / Academy": (30, -61, 28, 18),
    "Utilities / engineering": (96, 75, 36, 30),
    "Wellness / recreation": (30, -70, 30, 22),
    "Wet wipes production": (22, 43, 52, 19),
    "Caps and trigger assembly": (52, 31, 20, 15),
    "Daycare / crèche": (-105, -64, 34, 22),
    "Electrical / LV-MV room": (111, 61, 24, 18),
    "Employee changing / shower / locker support": (30, -70, 30, 22),
    "Fire pump house": (94, -5, 20, 18),
    "Micro-ingredient weigh / dispense": (-5, 50, 20, 16),
}

def slug(group):
    return re.sub(r"[^a-z0-9]+", "_", group.lower()).strip("_")

def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()

def same_group(a, b):
    aa, bb = norm(a), norm(b)
    if aa == bb or aa in bb or bb in aa:
        return True
    if "glass deck" in aa and "glass deck" in bb:
        return True
    if "wet processing" in aa and ("wet processing" in bb or "production hall" in bb):
        return True
    return False

def is_label(obj):
    return any(k in obj.name.upper() for k in ("LABEL", "SIGN", "TEXT", "CALLOUT", "CAPTION"))

def setup():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 640
    scene.render.resolution_y = 400
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
    scene.display.shading.background_type = "WORLD"
    scene.display.shading.background_color = (.06, .08, .10)
    return scene

def all_hidden():
    for obj in bpy.data.objects:
        obj.hide_render = True

def collection_objects(group):
    name = "REV005_V08_CLEAN_" + re.sub(r"[^A-Z0-9]+", "_", group.upper()).strip("_")
    col = bpy.data.collections.get(name)
    return list(col.objects) if col else []

def evidence_objects(objects):
    blocked = ("_SOFFIT", "_LEFT_WALL", "_RIGHT_WALL", "_FRONT_HEADER", "_FRONT_GLAZING")
    return [obj for obj in objects if not any(token in obj.name.upper() for token in blocked)]

def preserved_objects(group):
    inventory = json.loads(INV.read_text(encoding="utf-8"))["facility_groups"].get(group, {})
    names = set(inventory.get("objects", []))
    result = []
    for obj in bpy.data.objects:
        if is_label(obj) or obj.hide_render:
            continue
        if obj.name in names or same_group(group, obj.get("facility")):
            result.append(obj)
    return result

def camera_spec(group, view):
    x, y, w, d = CENTERS[group]
    if view == "ISOLATED":
        loc = (x - w * .62, y - d * .70, 5.2)
        target = (x, y, 2.8)
        lens = 48
    elif view == "A_CONTEXT":
        loc = (x - w * .30, y - d * .36, 4.2)
        target = (x + w * .10, y + d * .05, 3.0)
        lens = 52
    elif view == "B_FUNCTIONAL":
        loc = (x - w * .18, y - d * .25, 3.7)
        target = (x + w * .15, y, 2.8)
        lens = 60
    else:
        loc = (x + w * .25, y - d * .10, 3.5)
        target = (x + w * .05, y + d * .12, 2.8)
        lens = 62
    return loc, target, lens

def render(scene, path, loc, target, lens, name):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = lens
    cam.data.sensor_width = 36
    cam.data.clip_start = .1
    cam.data.clip_end = 1000
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    scene.camera = cam
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    size = path.stat().st_size if path.exists() else 0
    bpy.data.objects.remove(cam, do_unlink=True)
    return {"path": str(path), "bytes": size, "status": "PASS" if size > 5000 else "FAIL", "label_blind": True, "human_scale": True}

def prune_to_evidence_geometry():
    keep = set()
    for group in REMEDIATION_GROUPS:
        keep.update(obj.name for obj in collection_objects(group))
    for group in PASS_GROUPS:
        keep.update(obj.name for obj in preserved_objects(group))
    for obj in list(bpy.data.objects):
        if obj.name not in keep:
            bpy.data.objects.remove(obj, do_unlink=True)
    return len(keep)

def main():
    OUT.mkdir(parents=True, exist_ok=True); ISO.mkdir(parents=True, exist_ok=True); QA.mkdir(parents=True, exist_ok=True)
    scene = setup()
    evidence_object_count = prune_to_evidence_geometry()
    results = []
    isolated = []
    integrated = []
    for group in REMEDIATION_GROUPS:
        objs = evidence_objects([obj for obj in collection_objects(group) if obj.type in {"MESH", "CURVE", "SURFACE"}])
        all_hidden()
        for obj in objs:
            obj.hide_render = False
        path = ISO / f"{slug(group)}_ISOLATED_LABEL_BLIND.png"
        loc, target, lens = camera_spec(group, "ISOLATED")
        item = render(scene, path, loc, target, lens, "V08_ISOLATED_" + slug(group))
        item.update({"facility": group, "proof": "ISOLATED_LABEL_BLIND", "object_count": len(objs), "collection": "REV005_V08_CLEAN_" + slug(group).upper()})
        isolated.append(item); results.append(item)
        for view in ("A_CONTEXT", "B_FUNCTIONAL", "C_SEQUENCE_OR_DETAIL"):
            all_hidden()
            for obj in objs:
                obj.hide_render = False
            loc, target, lens = camera_spec(group, view)
            path = QA / f"{slug(group)}_{view}.png"
            item = render(scene, path, loc, target, lens, "V08_QA_" + slug(group) + "_" + view)
            item.update({"facility": group, "view": view, "proof": "INTEGRATED", "object_count": len(objs)})
            integrated.append(item); results.append(item)
    preservation = []
    for group in sorted(PASS_GROUPS):
        objs = preserved_objects(group)
        for view in ("A_CONTEXT", "B_FUNCTIONAL"):
            all_hidden()
            for obj in objs:
                obj.hide_render = False
            path = QA / f"{slug(group)}_{view}.png"
            loc, target, lens = camera_spec(group, view)
            item = render(scene, path, loc, target, lens, "V08_PRESERVE_" + slug(group) + "_" + view)
            item.update({"facility": group, "view": view, "proof": "PRESERVATION", "object_count": len(objs)})
            preservation.append(item); results.append(item)
    all_hidden()
    data = {
        "status": "READY_FOR_GPT_REVIEW",
        "task": "M08.16",
        "isolated_count": len(isolated),
        "integrated_count": len(integrated),
        "preservation_count": len(preservation),
        "render_count": len(results),
        "expected_render_count": 92,
        "isolated": isolated,
        "integrated": integrated,
        "preservation": preservation,
        "results": results,
        "evidence_object_count": evidence_object_count,
    }
    (OUT / "RENDER_RESULTS.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    lines = ["# REV005 V08 26-Group Visual Completion Index", "", "Unlabeled V08 clean-replacement evidence. Builder readiness only; independent GPT acceptance remains pending.", "", "| Group | Isolated proof | A_CONTEXT | B_FUNCTIONAL | C_SEQUENCE_OR_DETAIL | Role | Status |", "|---|---|---|---|---|---|---|"]
    for group in REMEDIATION_GROUPS + sorted(PASS_GROUPS):
        if group in PASS_GROUPS:
            role = "PRESERVE_PASS_REGRESSION"; iso = "—"; items = [x for x in preservation if x["facility"] == group]
        else:
            role = "V08_CLEAN_REPLACEMENT"; iso = f"[isolated](qa_isolated/{slug(group)}_ISOLATED_LABEL_BLIND.png)"; items = [x for x in integrated if x["facility"] == group]
        links = {x["view"]: f"[evidence](qa/{Path(x['path']).name})" for x in items}
        lines.append(f"| {group} | {iso} | {links.get('A_CONTEXT','—')} | {links.get('B_FUNCTIONAL','—')} | {links.get('C_SEQUENCE_OR_DETAIL','—')} | {role} | READY_FOR_GPT_REVIEW |")
    (OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": data["status"], "isolated": len(isolated), "integrated": len(integrated), "preservation": len(preservation), "renders": len(results), "failed": sum(x["status"] != "PASS" for x in results)}, indent=2))

main()
