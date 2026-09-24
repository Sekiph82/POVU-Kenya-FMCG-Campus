import json
import os
from pathlib import Path

import bpy
from mathutils import Vector


def temporary_camera(name, location, target):
    camera_data = bpy.data.cameras.new(name + '_DATA')
    camera = bpy.data.objects.new(name, camera_data)
    bpy.context.scene.collection.objects.link(camera)
    camera.location = location
    camera.rotation_euler = (Vector(target) - Vector(location)).to_track_quat('-Z', 'Y').to_euler()
    camera.data.lens = 52
    return camera


def main():
    repo = Path(__file__).resolve().parents[4]
    revision_dir = repo / '3d' / 'revisions' / 'REV004.1'
    blend = revision_dir / 'POVU_KENYA_FMCG_CAMPUS_REV004_1_FINAL_ARCHITECTURAL_MASTER.blend'
    output_dir = revision_dir / 'qa'
    output_dir.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.render.resolution_x = 1024
    scene.render.resolution_y = 576
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.film_transparent = False
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.studio_light = 'paint.sl'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = 'BOTH'

    cameras = {
        'QA_01_VIP_ENTRANCE_FRONT': ((-58.0, -122.0, 6.2), (-58.0, -91.5, 5.0)),
        'QA_02_VIP_ENTRANCE_OBLIQUE': ((-124.0, -142.0, 27.0), (-75.0, -91.5, 5.2)),
        'QA_03_FULL_EXTENDED_LIVING_WALL': ((-106.0, -122.0, 11.0), (-81.0, -91.8, 5.8)),
        'QA_04_HANDS_OF_GROWTH_FRONT': ((-108.0, -52.0, 7.0), (-108.0, -79.0, 5.0)),
        'QA_05_HANDS_OF_GROWTH_OBLIQUE': ((-132.0, -58.0, 18.0), (-108.0, -79.0, 5.0)),
        'QA_06_WIDER_PLAZA_SINGLE_HOG': ((-160.0, -178.0, 54.0), (-83.0, -83.0, 3.0)),
    }
    temporary = []
    rendered = []
    for name, (location, target) in cameras.items():
        focused_hog = name in {'QA_04_HANDS_OF_GROWTH_FRONT', 'QA_05_HANDS_OF_GROWTH_OBLIQUE'}
        hidden_landscape = []
        if focused_hog:
            for obj in bpy.data.objects:
                upper = obj.name.upper()
                if obj.type == 'MESH' and not upper.startswith('HOG_'):
                    hidden_landscape.append((obj, obj.hide_render))
                    obj.hide_render = True
        camera = temporary_camera(name, location, target)
        temporary.append(camera)
        scene.camera = camera
        output = output_dir / f'{name}.png'
        scene.render.filepath = str(output)
        bpy.ops.render.render(write_still=True)
        rendered.append({'camera': name, 'path': str(output), 'bytes': output.stat().st_size, 'status': 'PASS', 'focused_hog_only_mask': focused_hog})
        for obj, previous in hidden_landscape:
            obj.hide_render = previous

    hog_roots = [obj.name for obj in bpy.data.objects if obj.name == 'HANDS_OF_GROWTH' and obj.type == 'EMPTY' and not obj.hide_render]
    flagship = [obj.name for obj in bpy.data.objects if obj.name == 'SMART_TOTEM_VIP_BODY' and not obj.hide_render]
    campus = [obj.name for obj in bpy.data.objects if obj.name.startswith('SMART_TOTEM_CAMPUS_') and obj.name.endswith('_BODY') and not obj.hide_render]
    report = {
        'status': 'PASS' if len(hog_roots) == 1 and len(flagship) == 1 and len(campus) == 4 else 'BLOCKED',
        'blend': str(blend),
        'rendered': rendered,
        'hands_of_growth_landmark_roots': hog_roots,
        'hands_of_growth_root_count': len(hog_roots),
        'vip_flagship_smart_totems': flagship,
        'vip_flagship_smart_totem_count': len(flagship),
        'campus_smart_totems': campus,
        'campus_smart_totem_count': len(campus),
        'expected': {'hands_of_growth_root_count': 1, 'vip_flagship_smart_totem_count': 1},
    }
    (revision_dir / 'audit' / 'REV004_1_VISUAL_QA.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
