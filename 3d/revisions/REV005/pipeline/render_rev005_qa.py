import bpy
import json
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
QA_DIR = REV / "qa"
MANIFEST = REV / "REV005_ARCHITECTURAL_MANIFEST.json"

SHELL_HIDE = {
    "REV005_QA_ADMIN_RD_QC": ["Admin_RD_QC"],
    "REV005_QA_PACKAGING_WAREHOUSE": ["Packaging_Warehouse"],
    "REV005_QA_CHEMICAL_COMPOUND": ["Chemical_Compound"],
    "REV005_QA_RESTAURANT_CAFE": ["Restaurant_Wellness"],
    "REV005_QA_DAYCARE": ["Daycare"],
    "REV005_QA_CLINIC": ["Clinic"],
    "REV005_QA_WELLNESS": ["WELLNESS_PAVILION"],
    "REV005_QA_ACADEMY": ["MULTIPURPOSE_STUDIO"],
    "REV005_QA_WET_PROCESSING": ["PRODUCTION_WALL_NORTH", "PRODUCTION_WALL_SOUTH", "PRODUCTION_WALL_EAST", "PRODUCTION_WALL_WEST", "PRODUCTION_ROOF"],
    "REV005_QA_RAW_MATERIALS": ["RM_Warehouse"],
    "REV005_QA_FINISHED_GOODS": ["FG_Warehouse"],
    "REV005_QA_UTILITIES": ["Utility_House"],
}

def keep_source_object(camera_name, obj):
    if obj.type not in {"MESH", "CURVE", "FONT", "SURFACE"}:
        return True
    if any(col.name == "REV005_INTERIOR_COMPLETION" for col in obj.users_collection):
        return True
    if camera_name in {"REV005_QA_HANDS_OF_GROWTH", "REV005_QA_LIVING_WALL"}:
        return True
    n = obj.name.upper()
    if camera_name == "REV005_QA_WET_PROCESSING":
        return any(term in n for term in ("PROCESS", "TANK", "MIX", "FILL", "PACK", "POWDER", "WIPES", "TOOTHPASTE", "BLOW", "INJECTION", "CAP", "TRIGGER", "PRODUCTION_FLOOR"))
    if camera_name == "REV005_QA_RAW_MATERIALS":
        return n.startswith("RM_")
    if camera_name == "REV005_QA_FINISHED_GOODS":
        return n.startswith("FG_")
    if camera_name == "REV005_QA_UTILITIES":
        return any(n.startswith(prefix) for prefix in ("UTILITY", "RO_", "STEAM", "GENERATOR", "SCREW_COMPRESSOR", "BOILER", "LV_MV", "AIR_", "FIRE"))
    return False

def main():
    QA_DIR.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 640
    scene.render.resolution_y = 360
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    results = []
    cameras = [o for o in bpy.data.objects if o.type == "CAMERA" and o.name.startswith("REV005_QA_")]
    for cam in sorted(cameras, key=lambda o: o.name):
        old = {}
        isolated = cam.name not in {"REV005_QA_HANDS_OF_GROWTH", "REV005_QA_LIVING_WALL"}
        if isolated:
            for obj in bpy.data.objects:
                if obj.type in {"MESH", "CURVE", "FONT", "SURFACE"}:
                    old[obj.name] = obj.hide_render
                    obj.hide_render = not keep_source_object(cam.name, obj)
        for obj_name in SHELL_HIDE.get(cam.name, []):
            obj = bpy.data.objects.get(obj_name)
            if obj:
                old[obj.name] = obj.hide_render
                obj.hide_render = True
        scene.camera = cam
        path = QA_DIR / (cam.name + ".png")
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        for obj_name, value in old.items():
            if bpy.data.objects.get(obj_name):
                bpy.data.objects[obj_name].hide_render = value
        results.append({"camera": cam.name, "facility": cam.get("rev005_facility"), "path": str(path), "bytes": path.stat().st_size if path.exists() else 0, "status": "PASS" if path.exists() and path.stat().st_size > 1000 else "FAIL"})
    report = {"revision": "REV005", "renderer": "BLENDER_WORKBENCH", "results": results, "status": "PASS" if results and all(x["status"] == "PASS" for x in results) else "BLOCKED"}
    (REV / "audit" / "REV005_VISUAL_QA_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest["qa_results"] = results
        manifest["visual_qa_report"] = str(REV / "audit" / "REV005_VISUAL_QA_REPORT.json")
        manifest["visual_qa_status"] = report["status"]
        MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
