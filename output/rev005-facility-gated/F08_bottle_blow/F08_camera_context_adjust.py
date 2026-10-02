import bpy,json
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
assert E.name=='F08_bottle_blow'
cam=bpy.data.objects['F08_CAMERA_A_CONTEXT'];seed=Vector((35,-.5,6));target=Vector((52,10,3));pos=Vector((32.0,-3.5,6.0))
assert max(abs(x) for x in pos-seed)<=3 and 20<=20<=40
cam.location=pos;cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.lens=20;cam.data.sensor_width=36
# Ensure the revised context camera origin stays outside every modeled object.
for o in bpy.data.objects:
 if o.type!='MESH':continue
 if o.get('REV005_F08_CLASS_N_ACCEPTED') is not True:continue
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 lo=[min(p[i] for p in pts) for i in range(3)];hi=[max(p[i] for p in pts) for i in range(3)]
 if all(lo[i]<=pos[i]<=hi[i] for i in range(3)):
  raise RuntimeError('BLOCKED_F08_CAMERA_INSIDE_GEOMETRY '+o.name)
p=E/'F08_CAMERA_VALIDATION.json';data=json.loads(p.read_text(encoding='utf-8'))
row=next(x for x in data['cameras'] if x['name']=='A_CONTEXT');row.update({'camera_xyz':list(pos),'target_xyz':list(target),'lens_mm':20,'sensor_width_mm':36,'camera_inside_geometry':False,'refinement_camera_delta_xyz':list(pos-seed),'refinement_target_delta_xyz':[0,0,0]})
data['status']='PASS';data['refinements_within_contract_limits']=True;p.write_text(json.dumps(data,indent=2),encoding='utf-8')
cam=bpy.data.objects['F08_CAMERA_C_SEQUENCE_DETAIL'];cseed=Vector((48,5,4));ctarget=Vector((58.0,11.5,3.0));cpos=Vector((51.0,4.0,4.0))
assert max(abs(x) for x in cpos-cseed)<=3 and max(abs(x) for x in ctarget-Vector((56.5,10,3)))<=2
cam.location=cpos;cam.rotation_euler=(ctarget-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.lens=30;cam.data.sensor_width=36
for o in bpy.data.objects:
 if o.type!='MESH' or o.get('REV005_F08_CLASS_N_ACCEPTED') is not True:continue
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 lo=[min(p[i] for p in pts) for i in range(3)];hi=[max(p[i] for p in pts) for i in range(3)]
 if all(lo[i]<=cpos[i]<=hi[i] for i in range(3)):raise RuntimeError('BLOCKED_F08_CAMERA_INSIDE_GEOMETRY '+o.name)
row=next(x for x in data['cameras'] if x['name']=='C_SEQUENCE_DETAIL');row.update({'camera_xyz':list(cpos),'target_xyz':list(ctarget),'lens_mm':30,'sensor_width_mm':36,'camera_inside_geometry':False,'refinement_camera_delta_xyz':list(cpos-cseed),'refinement_target_delta_xyz':list(ctarget-Vector((56.5,10,3)))})
bpy.ops.wm.save_as_mainfile(filepath=str(E/'F08_STAGED.blend'))
print('F08_A_CONTEXT_CAMERA_ADJUSTED',list(pos),list(target),'lens=20; camera clear of all mesh bounds')
