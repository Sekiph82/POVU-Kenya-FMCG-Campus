import bpy,json
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');BASE=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R01';scene=bpy.context.scene
spec={
'A':('F08_CAMERA_A_CONTEXT',[(x,y,z) for x in [36,38,40,42,44,46] for y,z in [(0,6.2),(2.5,6.7),(5,7.0)]],[16,18,20,22,24],[54,57,60],[9,10,11],[2.6,3,3.4]),
'B':('F08_CAMERA_B_FUNCTIONAL',[(x,y,6.5) for x in [43,44.5,46,47.5,49,50,51] for y in [1.5,3.5,5.5]][:21],[18,20,22,24,28,32],[54,56.5,59],[9,10,11],[2.6,3,3.5]),
'C':('F08_CAMERA_C_SEQUENCE_DETAIL',[(x,y,6.01) for x in [48,49,50,51,52,53,54,55] for y in [2.5,4.25,6]][:21],[20,22,24,26,28,30,32],[56,58.5,61],[9,10,11],[2.5,3,3.5]),
'D':('F08_CAMERA_D_INTEGRATED',([(x,y,6.5) for y in [0,2.25,4.5] for x in [40,43,47,50,54]]+[(x,y,6.5) for y in [16,18,20] for x in [40,43,47,50,54]])[:20],[16,18,20,22,24],[52,54.5,57],[9,10,11],[2.8,3.15,3.5]),
}
path=BASE/'F08_R01_CAMERA_CANDIDATES.json';data=json.loads(path.read_text(encoding='utf-8'));records=data['records'];done={r['id'] for r in records}
def hits(p):
 result=[]
 for ob in scene.objects:
  if ob.type!='MESH':continue
  cs=[ob.matrix_world@Vector(c) for c in ob.bound_box];lo=[min(c[i] for c in cs) for i in range(3)];hi=[max(c[i] for c in cs) for i in range(3)]
  if all(lo[i]-1e-5<=p[i]<=hi[i]+1e-5 for i in range(3)):result.append(ob.name)
 return result
scene.render.engine='BLENDER_EEVEE';scene.eevee.taa_render_samples=8;scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8'
for role,(camname,positions,lenses,txs,tys,tzs) in spec.items():
 cam=bpy.data.objects[camname];outdir=BASE/'candidates'/role;outdir.mkdir(parents=True,exist_ok=True)
 for j,pos0 in enumerate(positions,1):
  key=f'{role}_{18+j:03d}' if role in ('A','D') else f'{role}_{9+j:03d}'
  if key in done:continue
  lens=lenses[(j-1)%len(lenses)];target=Vector((txs[(j//2)%len(txs)],tys[(j-1)%len(tys)],tzs[(j//3)%len(tzs)]));pos=Vector(pos0)
  cam.location=pos;cam.rotation_euler=(target-pos).to_track_quat('-Z','Y').to_euler();cam.data.lens=lens;cam.data.sensor_width=36;scene.camera=cam
  filepath=outdir/f'{key}_900x600.png';scene.render.filepath=str(filepath)
  rec={'id':key,'role':role,'camera_object':cam.name,'origin_xyz':[round(v,4) for v in pos],'target_xyz':[round(v,4) for v in target],'lens_mm':lens,'sensor_width_mm':36,'resolution':[900,600],'camera_inside_mesh_aabb_objects':hits(pos),'wall_ceiling_clipping':False,'visibility_changed':False,'render_path':str(filepath),'rendered':False,'visual_cues':{'all_process_stages_readable':None,'preform_heating_readable':None,'stretch_blow_molding_readable':None,'formed_bottle_discharge_readable':None,'conveyor_flow_readable':None,'aisle_or_access_readable':None,'critical_equipment_obstructed':None,'black_or_empty_field':None},'visual_verdict':'PENDING_IMAGE_REVIEW'}
  print('R01_RENDER_BEGIN',key,'camera_aabb_hits',rec['camera_inside_mesh_aabb_objects'],flush=True)
  try: result=bpy.ops.render.render(write_still=True);rec['rendered']=filepath.exists();rec['render_result']=str(result)
  except Exception as e:rec['render_error']=repr(e)
  records.append(rec);done.add(key);path.write_text(json.dumps(data,indent=2),encoding='utf-8');print('R01_RENDER_END',key,rec['rendered'],flush=True)
print('R01_SUPPLEMENT_DONE',len(records),flush=True)
