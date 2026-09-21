import bpy
import sys
from mathutils import Vector

# Legacy Video 01 route script retained as a useful starting point for M33-C001.
# Codex may refactor/move this into 3d/video/pipeline/ after validating it locally.
OUT = sys.argv[sys.argv.index("--") + 1]
scene = bpy.context.scene
name = "VID_01_POVU_Campus_Aerial"

old = bpy.data.objects.get(name)
if old:
    bpy.data.objects.remove(old, do_unlink=True)

data = bpy.data.cameras.new(name + "_DATA")
cam = bpy.data.objects.new(name, data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.data.lens = 48
cam.data.sensor_width = 36

def look_at(target):
    cam.rotation_euler = (Vector(target) - cam.location).to_track_quat("-Z", "Y").to_euler()

route = [
    (0,   (245, -285, 185), (-20, -5, 0)),
    (120, (205, -250, 160), (-35, -15, 0)),
    (288, (145, -205, 130), (-45, -25, 0)),
    (480, (85, -165, 105),  (-50, -35, 0)),
    (719, (35, -135, 88),   (-55, -45, 0)),
]
for frame, location, target in route:
    cam.location = location
    look_at(target)
    cam.keyframe_insert("location", frame=frame)
    cam.keyframe_insert("rotation_euler", frame=frame)

scene.frame_start = 0
scene.frame_end = 719
scene.render.fps = 24
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "FFMPEG"
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"
scene.render.ffmpeg.constant_rate_factor = "MEDIUM"
scene.render.ffmpeg.ffmpeg_preset = "GOOD"
scene.render.filepath = OUT

# Save a working render copy, never overwrite the architectural source master.
bpy.ops.wm.save_as_mainfile(filepath="//POVU_VID01_Render.blend")
bpy.ops.render.render(animation=True)
print("POVU_VIDEO01_DONE", OUT)
