import bpy, sys
from mathutils import Vector
OUT=sys.argv[sys.argv.index("--")+1]
s=bpy.context.scene
n="VID_01_POVU_Campus_Aerial"
o=bpy.data.objects.get(n)
if o:bpy.data.objects.remove(o,do_unlink=True)
d=bpy.data.cameras.new(n+"_DATA");c=bpy.data.objects.new(n,d);s.collection.objects.link(c);s.camera=c;c.data.lens=48;c.data.sensor_width=36
def look(t):c.rotation_euler=(Vector(t)-c.location).to_track_quat("-Z","Y").to_euler()
for f,loc,t in [(0,(245,-285,185),(-20,-5,0)),(120,(205,-250,160),(-35,-15,0)),(288,(145,-205,130),(-45,-25,0)),(480,(85,-165,105),(-50,-35,0)),(719,(35,-135,88),(-55,-45,0))]:
 c.location=loc;look(t);c.keyframe_insert("location",frame=f);c.keyframe_insert("rotation_euler",frame=f)
s.frame_start=0;s.frame_end=719;s.render.fps=24;s.render.engine="BLENDER_EEVEE";s.render.resolution_x=1280;s.render.resolution_y=720;s.render.resolution_percentage=100
s.render.image_settings.file_format="FFMPEG";s.render.ffmpeg.format="MPEG4";s.render.ffmpeg.codec="H264";s.render.ffmpeg.constant_rate_factor="MEDIUM";s.render.ffmpeg.ffmpeg_preset="GOOD";s.render.filepath=OUT
bpy.ops.wm.save_as_mainfile(filepath="//POVU_VID01_Render.blend");bpy.ops.render.render(animation=True)
print("POVU_VIDEO01_DONE",OUT)
