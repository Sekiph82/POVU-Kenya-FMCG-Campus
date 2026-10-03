import bpy,json,math
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
R=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R03'
SRC=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend'
assert bpy.data.filepath.lower()==str(SRC).lower(), (bpy.data.filepath,SRC)
scene=bpy.context.scene
# The exact stage is read-only. Camera objects are created/updated only in memory;
# this script deliberately does not save the .blend.
roles={
'A':{'name':'A_CONTEXT','xs':[48,50,52,54,56,53],'ys':[-8,-10.5,-13,-16],'zs':[6.25,7.0,7.75],'txs':[51,53,55],'ty':[9,10,11],'tz':[2.5,3.0,3.5],'lens':[14,16,18,20,22]},
'B':{'name':'B_FUNCTIONAL','xs':[52,54,56,58,60,57],'ys':[-5,-7,-9.5,-12],'zs':[6.25,6.6,7.0],'txs':[55,57.5,60],'ty':[9,10,11],'tz':[2.4,3.0,3.5],'lens':[18,20,22,24,28]},
'C':{'name':'C_SEQUENCE_DETAIL','xs':[54,55,56,58,60,57],'ys':[-4,-5.5,-7,-9],'zs':[6.0],'txs':[56,58,60],'ty':[9,10,11],'tz':[2.2,2.8,3.4],'lens':[20,22,24,28,32]},
'D':{'name':'D_INTEGRATED','xs':[46,48,50,54,58,52],'ys':[-8,-10,-12.5,-15],'zs':[6.25,7.0,8.0],'txs':[52,54.5,57],'ty':[9,10,11],'tz':[2.8,3.1,3.5],'lens':[14,16,18,20,22]},
}
scene.render.engine='BLENDER_EEVEE'
scene.eevee.taa_render_samples=4
scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8';scene.render.film_transparent=False
boxes=[]
for o in scene.objects:
 if o.type!='MESH': continue
 pts=[o.matrix_world@Vector(c) for c in o.bound_box]
 boxes.append((o.name,[min(p[i] for p in pts) for i in range(3)],[max(p[i] for p in pts) for i in range(3)]))
records=[]
for role,cfg in roles.items():
 name='F08_R03_CAMERA_'+cfg['name']
 cam=bpy.data.objects.get(name)
 if cam is None:
  data=bpy.data.cameras.new(name+'_DATA');cam=bpy.data.objects.new(name,data);scene.collection.objects.link(cam)
 out=R/'candidates'/role;out.mkdir(parents=True,exist_ok=True)
 for idx in range(24):
  i=idx
  x=cfg['xs'][i%6]; y=cfg['ys'][(i//6)%4]; z=cfg['zs'][i%len(cfg['zs'])]
  tx=cfg['txs'][(i*2+1)%len(cfg['txs'])]; ty=cfg['ty'][(i//2)%3]; tz=cfg['tz'][(i//3)%3]
  lens=cfg['lens'][(i*2+role.__len__())%len(cfg['lens'])]
  pos=Vector((x,y,z)); target=Vector((tx,ty,tz))
  cam.location=pos;cam.rotation_euler=(target-pos).to_track_quat('-Z','Y').to_euler()
  cam.data.lens=lens;cam.data.sensor_width=36;cam.data.clip_start=.08;cam.data.clip_end=300;scene.camera=cam
  hits=[n for n,lo,hi in boxes if all(lo[k]-.00001<=pos[k]<=hi[k]+.00001 for k in range(3))]
  key=f'{role}_{idx+1:03}';path=out/f'{key}_900x600.png'
  rec={'candidate_id':key,'role':role,'camera_object':name,'camera_xyz':[round(float(v),4) for v in pos],
       'target_xyz':[round(float(v),4) for v in target],'lens_mm':lens,'sensor_width_mm':36,
       'resolution':[900,600],'camera_inside_geometry':bool(hits),'camera_inside_geometry_objects':hits,
       'facade_glazing_clipping':'PENDING_DIRECT_VISUAL_REVIEW','hopper_visible':'PENDING_DIRECT_VISUAL_REVIEW',
       'elevator_feed_visible':'PENDING_DIRECT_VISUAL_REVIEW','oven_visible':'PENDING_DIRECT_VISUAL_REVIEW',
       'transfer_visible':'PENDING_DIRECT_VISUAL_REVIEW','mould_station_readable':'PENDING_DIRECT_VISUAL_REVIEW',
       'stretch_blow_readable':'PENDING_DIRECT_VISUAL_REVIEW','in_process_preform_readable':'PENDING_DIRECT_VISUAL_REVIEW',
       'formed_bottle_readable':'PENDING_DIRECT_VISUAL_REVIEW','outfeed_visible':'PENDING_DIRECT_VISUAL_REVIEW',
       'hmi_operator_relationship':'PENDING_DIRECT_VISUAL_REVIEW','aisle_context':'PENDING_DIRECT_VISUAL_REVIEW',
       'complete_label_blind_sequence':'PENDING_DIRECT_VISUAL_REVIEW','preview_path':str(path.relative_to(R)),
       'rendered':False,'retained_top8':False}
  if hits and role!='C': rec['render_error']='camera_origin_inside_mesh_aabb'
  else:
   scene.render.filepath=str(path);print('F08_R03_RENDER_BEGIN',key,flush=True)
   try:
    bpy.ops.render.render(write_still=True);rec['rendered']=path.exists()
    if not rec['rendered']: rec['render_error']='render_output_missing'
   except Exception as e:rec['render_error']=repr(e)
  records.append(rec)
  payload={'schema':'F08_R03_CAMERA_CANDIDATES_V1','task':'M08.45 / F08-R03','source_blend':'../R02/F08_R02_STAGED.blend','source_sha256':'0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25','candidate_minimum_per_role':18,'candidate_count_per_role':24,'camera_visibility_or_geometry_mutations':0,'blend_saved':False,'records':records}
  (R/'F08_R03_CAMERA_CANDIDATES.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
  print('F08_R03_RENDER_END',key,rec['rendered'],'AABB_HITS',len(hits),flush=True)
print('F08_R03_CAMERA_RENDER_BATCH_DONE',len(records),flush=True)
