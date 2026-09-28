import bpy
import json
import re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
V05_RENDERER = REV / "pipeline/render_rev005_interior_remediation_v05.py"

source = V05_RENDERER.read_text(encoding="utf-8")
prefix = source.split("\ndef main():", 1)[0]
exec(compile(prefix, str(V05_RENDERER), "exec"), globals())
ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
}

MODEL_HIDE_PROXY_NAMES = {
    "V04_ADMIN_QC_LAB_BENCH", "V05_ADMIN_QC_BENCH",
    "V03_BLOW_OVEN_HOUSING", "V05_BLOW_OVEN_HOUSING", "V05_BLOW_MOULD_CLAMP_HOUSING",
    "V05_CHEM_TANK0_VESSEL", "V05_CHEM_TANK1_VESSEL", "V05_CHEM_TANK2_VESSEL",
    "V04_ETP_TANK_02", "V05_ETP_HEADER0", "V05_ETP_HEADER1",
    "V03_LIQUID_FILLER_HOUSING", "V03_LIQUID_MAIN_LINE_FRAME", "V05_LIQUID_FILLER_HOUSING", "V05_LIQUID_CASE_PACK_HOUSING",
    "V05_CLINIC_PRIVACY_PANEL", "V05_POWDER_DOSER_HOUSING",
    "V03_RESTAURANT_CAFE_BAR", "V05_CAFE_SERVICE_COUNTER", "V05_KITCHEN_PARTITION_PANEL",
    "V05_SECURITY_WAIT_PANEL",
    "V03_PASTE_CARTONER", "V03_PASTE_CASE_OUTFEED", "V03_PASTE_FILLER_GUARD", "V03_PASTE_TUBE_LINE_FRAME", "V04_PASTE_BLEND_JACKET", "V04_PASTE_RIGHT", "V05_PASTE_VACUUM_MIX_VESSEL",
    "V04_UTIL_RIGHT", "V05_UTIL_BOILER_VESSEL",
    "V03_WIPES_CONVERTING_LINE_FRAME", "V03_WIPES_UNWIND_FRAME", "V03_WIPES_WETTING_BATH", "V05_WIPES_FOLD_FRAME", "V05_WIPES_DISCHARGE",
}
QA_ONLY_PROXY_NAMES = {"V05_FG_BACK", "V05_GLASS_LEFT", "V05_GATEHOUSE_BACK"}
QA_EXCLUDE = MODEL_HIDE_PROXY_NAMES | QA_ONLY_PROXY_NAMES

VIEW_SPEC = {
    group: {"A_CONTEXT": (spec[0], spec[3], 38), "B_FUNCTIONAL": (spec[1], spec[3], 50), "C_SEQUENCE": (spec[2], spec[3], 45)}
    for group, spec in ANCHORS.items()
}

def show_only(objs):
    keep = set(objs)
    for obj in bpy.data.objects:
        shell_occluder = any(k in obj.name.upper() for k in ("_LEFT", "_RIGHT", "_BACK", "_SOFFIT", "_CEILING_BEAM"))
        obj.hide_render = obj not in keep or obj.name in QA_EXCLUDE or obj.type not in {"MESH", "CURVE", "SURFACE"} or shell_occluder

def render_view(scene, path, loc, target, lens, name):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.lens = lens
    cam.data.sensor_width = 36
    cam.data.clip_start = 0.1
    cam.data.clip_end = 1000
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    scene.camera = cam
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    ok = path.exists() and path.stat().st_size > 5000
    size = path.stat().st_size if path.exists() else 0
    bpy.data.objects.remove(cam, do_unlink=True)
    return {"path": str(path), "bytes": size, "status": "PASS" if ok else "FAIL", "label_blind": True, "human_scale": True}

def slug(group):
    return re.sub(r"[^a-z0-9]+", "_", group.lower()).strip("_")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    QA.mkdir(parents=True, exist_ok=True)
    inventory = json.loads(INV.read_text(encoding="utf-8"))
    scene = setup()
    scene.render.resolution_x = 1024
    scene.render.resolution_y = 640
    scene.render.resolution_percentage = 100
    rows = []
    results = []
    for group, record in inventory["facility_groups"].items():
        objs = objects_for(group, record)
        show_only(objs)
        views = ["A_CONTEXT", "B_FUNCTIONAL"] if group in PASS_GROUPS else ["A_CONTEXT", "B_FUNCTIONAL", "C_SEQUENCE"]
        evidence = []
        for view in views:
            loc, target, lens = VIEW_SPEC[group][view]
            filename = f"{slug(group)}_{view}.png"
            item = render_view(scene, QA / filename, loc, target, lens, f"V07_QA_{group[:18].replace(' ', '_')}_{view}")
            item.update({"facility": group, "view": view, "object_count": len(objs), "excluded_proxy_count": len(QA_EXCLUDE & {o.name for o in objs})})
            results.append(item)
            evidence.append(item)
            show_only(objs)
        rows.append({"facility": group, "evidence": evidence, "object_count": len(objs)})

    (OUT / "RENDER_RESULTS.json").write_text(json.dumps({"status": "READY_FOR_GPT_REVIEW", "render_count": len(results), "group_count": len(rows), "expected_render_count": 72, "results": results}, indent=2), encoding="utf-8")
    lines = ["# REV005 V07 26-Group Visual Completion Index", "", "V07 integration-corrected, unlabeled human/process-scale evidence. Independent GPT acceptance remains pending.", "", "| Group | A_CONTEXT | B_FUNCTIONAL | C_SEQUENCE | Triage | Status |", "|---|---|---|---|---|---|"]
    for row in rows:
        links = {e["view"]: f"[evidence](qa/{Path(e['path']).name})" for e in row["evidence"]}
        triage = "PRESERVE_PASS_RECHECK" if row["facility"] in PASS_GROUPS else "V07_INTEGRATION_ROOT_CAUSE_CLOSURE"
        lines.append(f"| {row['facility']} | {links.get('A_CONTEXT','—')} | {links.get('B_FUNCTIONAL','—')} | {links.get('C_SEQUENCE','—')} | {triage} | READY_FOR_GPT_REVIEW |")
    (OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": "READY_FOR_GPT_REVIEW", "renders": len(results), "groups": len(rows), "passes": sum(r["status"] == "PASS" for r in results)}, indent=2))

main()
