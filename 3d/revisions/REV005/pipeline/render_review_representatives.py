import bpy
import json
from pathlib import Path
from mathutils import Vector

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
OUT_DIR = ROOT / "output" / "rev005-owner-interior-review"
BLEND = ROOT / "3d" / "revisions" / "REV005" / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
PLAN = OUT_DIR / "REV005_OWNER_INTERIOR_CAMERA_PLAN.json"
FRAME_DIR = OUT_DIR / "review_frames_v03_fixed"

def renderable(obj):
    return obj.type in {"MESH", "CURVE", "SURFACE", "FONT"}

def main():
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(BLEND), load_ui=False)
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.background_type = "WORLD"
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    if scene.world is None:
        scene.world = bpy.data.worlds.new("REV005_REVIEW_WORLD")
    scene.world.color = (0.48, 0.55, 0.62)
    bpy.ops.object.camera_add(location=(0, -40, 20))
    camera = bpy.context.object
    camera.name = "REV005_OWNER_REVIEW_STILL_CAMERA"
    camera.data.lens = 47
    camera.data.clip_end = 2000
    scene.camera = camera
    renderables = [obj for obj in bpy.data.objects if renderable(obj)]
    count = 0
    for segment in plan["segments"]:
        active = set(segment["selected_names"])
        for obj in renderables:
            obj.hide_render = obj.name not in active
        for view_name, position_key, target_key in (("A", "position_a", "target_a"), ("B", "position_b", "target_b")):
            position = Vector(segment[position_key])
            target = Vector(segment[target_key])
            camera.location = position
            camera.rotation_euler = (target - position).to_track_quat("-Z", "Y").to_euler()
            scene.render.filepath = str(FRAME_DIR / f"{segment['start_frame']:05d}_{view_name}_{segment['label'].replace('/', '_').replace(' ', '_')}.png")
            bpy.ops.render.render(write_still=True)
            count += 1
    print(json.dumps({"frames": count, "directory": str(FRAME_DIR)}, indent=2))

if __name__ == "__main__":
    main()
