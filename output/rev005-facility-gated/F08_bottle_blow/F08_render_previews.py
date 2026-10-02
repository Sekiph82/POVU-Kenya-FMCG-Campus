import bpy, json
from pathlib import Path
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
assert E.name=='F08_bottle_blow'
scene=bpy.context.scene
scene.render.engine='BLENDER_EEVEE'
if hasattr(scene,'eevee') and hasattr(scene.eevee,'taa_render_samples'):scene.eevee.taa_render_samples=64
scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8'
rows=[]
for label in ('A_CONTEXT','B_FUNCTIONAL','C_SEQUENCE_DETAIL','D_INTEGRATED'):
 cam=bpy.data.objects.get('F08_CAMERA_'+label)
 if cam is None:raise RuntimeError('M08.42 / F08 only missing camera '+label)
 scene.camera=cam;out=E/f'F08_{label}_PREVIEW_900x600.png';scene.render.filepath=str(out)
 result=bpy.ops.render.render(write_still=True)
 if 'FINISHED' not in result or not out.exists():raise RuntimeError('F08 preview render failed '+label)
 rows.append({'name':label,'path':str(out.relative_to(ROOT)),'resolution':[900,600],'render_result':'FINISHED','camera_xyz':[round(float(x),3) for x in cam.location],'target_xyz':[round(float(x),3) for x in (cam.matrix_world.to_translation()+cam.matrix_world.to_3x3()@__import__('mathutils').Vector((0,0,-10))) ]})
(E/'F08_PREVIEW_RENDER_RESULTS.json').write_text(json.dumps({'task':'M08.42 / F08 only','state_source':'F08_STAGED.blend saved model; no visibility changes','renders':rows},indent=2),encoding='utf-8')
print('F08_PREVIEWS_RENDERED',len(rows))
