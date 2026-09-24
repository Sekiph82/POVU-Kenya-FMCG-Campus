import bpy
from mathutils import Vector

OUT = r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo\3d\revisions\REV004.2\audit"

def look_at(cam, target):
    direction = Vector(target) - cam.location
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()

def render(name, location, target, lens=52):
    scene = bpy.context.scene
    cam_data = bpy.data.cameras.new(name + "_DATA")
    cam = bpy.data.objects.new(name, cam_data)
    scene.collection.objects.link(cam)
    cam.location = location
    cam.data.lens = lens
    look_at(cam, target)
    scene.camera = cam
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.filepath = f"{OUT}\\{name}.png"
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.studio_light = 'paint.sl'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = 'BOTH'
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam, do_unlink=True)

render('source_hands_approach', (-135, -116, 27), (-108, -79, 5), 52)
render('source_vip_living_wall', (-90, -128, 18), (-68, -92, 5.5), 52)
render('source_vip_oblique', (-120, -108, 16), (-58, -92, 5), 52)
