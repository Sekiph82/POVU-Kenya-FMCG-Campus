import bpy
import json
import math
from pathlib import Path
from mathutils import Vector

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
MANIFEST = REV / "REV005_ARCHITECTURAL_MANIFEST.json"

def aim(cam, loc, target):
    cam.location = loc
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

def main():
    aim(bpy.data.objects["REV005_QA_RESTAURANT_CAFE"], (5, -54, 6.5), (5, -64, 2.0))
    aim(bpy.data.objects["REV005_QA_LIVING_WALL"], (-55, -105, 8.0), (-74, -92, 5.5))
    aim(bpy.data.objects["REV005_QA_HANDS_OF_GROWTH"], (-120, -106, 14.0), (-102, -89, 4.5))
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["qa_camera_correction"] = {"restaurant_cafe": "Dining and café seating view", "living_wall": "Front elevation showing retained wall section", "hands_of_growth": "Wider plaza view showing independent landmark and cleared sightline"}
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("FINALIZED_QA_CAMERAS")

if __name__ == "__main__":
    main()
