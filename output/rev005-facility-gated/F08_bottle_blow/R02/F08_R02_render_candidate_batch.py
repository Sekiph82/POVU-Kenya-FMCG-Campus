import bpy,json,math
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');R=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R02';scene=bpy.context.scene
assert bpy.data.filepath.lower()==str((R/'F08_R02_STAGED.blend')).lower()
# New origins vary by role and search only non-colliding exterior camera positions.
roles={
'A':{'cam':'F08_R02_CAMERA_A_CONTEXT','xs':[62,64,66,68,69,70],'ys':[7,9,11,13],'z':6.4,'tx':[51.0,53.0,55.0],'ty':[10.0,10.5,9.5],'tz':[3.1,3.4,3.7],'lenses':[16,18,20,22,24]},
'B':{'cam':'F08_R02_CAMERA_B_FUNCTIONAL','xs':[60,62,64,66,68,70],'ys':[3,5,7,9],'z':6.4,'tx':[58.5,60.0,61.5],'ty':[10.0,10.5,9.5],'tz':[3.0,3.3,3.6],'lenses':[16,18,20,22,24,28]},
'C':{'cam':'F08_R02_CAMERA_C_SEQUENCE_DETAIL','xs':[50,52,54,56,58,60],'ys':[.5,1.5,2.5,3.5],'z':6.2,'tx':[55.5,57.0,58.5],'ty':[10.0,10.5,9.5],'tz':[2.9,3.2,3.5],'lenses':[20,22,24,26,28,30,32]},
'D':{'cam':'F08_R02_CAMERA_D_INTEGRATED','xs':[38,42,46,50,54,58],'ys':[3,5,7,9],'z':6.4,'tx':[51.0,53.0,55.0],'ty':[10.0,10.5,9.5],'tz':[3.1,3.4,3.7],'lenses':[16,18,20,22,24]},
}
scene.render.engine='BLENDER_EEVEE';scene.eevee.taa_render_samples=4;scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8';scene.render.film_transparent=False
# Precompute world-space mesh AABBs for camera-origin intersection checks.
boxes=[]
for o in scene.objects:
 if o.type!='MESH':continue
 pts=[o.matrix_world@Vector(c) for c in o.bound_box]
 boxes.append((o.name,[min(p[i] for p in pts) for i in range(3)],[max(p[i] for p in pts) for i in range(3)]))
records=[]
for role,cfg in roles.items():
 cam=bpy.data.objects.get(cfg['cam'])
 if cam is None:
  data=bpy.data.cameras.new(cfg['cam']+'_R02');cam=bpy.data.objects.new(cfg['cam'],data);scene.collection.objects.link(cam)
 out=R/'candidates'/role;out.mkdir(parents=True,exist_ok=True)
 for idx in range(24):
  x=cfg['xs'][idx%6];y=cfg['ys'][idx//6];z=cfg['z'];tx=cfg['tx'][idx%3];ty=cfg['ty'][(idx//3)%3];tz=cfg['tz'][(idx//2)%3];lens=cfg['lenses'][idx%len(cfg['lenses'])]
  pos=Vector((x,y,z));target=Vector((tx,ty,tz));cam.location=pos;cam.rotation_euler=(target-pos).to_track_quat('-Z','Y').to_euler();cam.data.lens=lens;cam.data.sensor_width=36;cam.data.clip_start=.08;cam.data.clip_end=300;scene.camera=cam
  hits=[n for n,lo,hi in boxes if all(lo[i]-.00001<=pos[i]<=hi[i]+.00001 for i in range(3))]
  key=f'{role}_{idx+1:03}';path=out/f'{key}_900x600.png'
  rec={'id':key,'role':role,'camera_object':cam.name,'origin_xyz':[round(float(v),4) for v in pos],'target_xyz':[round(float(v),4) for v in target],'lens_mm':lens,'sensor_width_mm':36,'resolution':[900,600],'clip_start_m':.08,'camera_inside_mesh_aabb_objects':hits,'wall_ceiling_clipping':False,'visibility_changed':False,'render_path':str(path.relative_to(R)),'rendered':False,'visual_verdict':'PENDING_IMAGE_REVIEW'}
  if hits:rec['render_error']='camera_origin_intersects_mesh_aabb'
  else:
   scene.render.filepath=str(path);print('F08_R02_RENDER_BEGIN',key,flush=True)
   try:bpy.ops.render.render(write_still=True);rec['rendered']=path.exists()
   except Exception as e:rec['render_error']=repr(e)
  records.append(rec)
  (R/'F08_R02_CAMERA_CANDIDATES.json').write_text(json.dumps({'schema':'F08_R02_CAMERA_CANDIDATES_V1','task':'M08.44 / F08-R02','stage_blend':'F08_R02_STAGED.blend','candidate_minimum_per_role':24,'records':records},indent=2),encoding='utf-8')
  print('F08_R02_RENDER_END',key,rec['rendered'],'hits',len(hits),flush=True)
print('F08_R02_CAMERA_RENDER_BATCH_DONE',len(records),flush=True)
