import bpy,json,math
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
BASE=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R01'
STAGE=BASE/'F08_bottle_blow/F08_STAGED.blend'
scene=bpy.context.scene
roles={
'A': {'cam':'F08_CAMERA_A_CONTEXT','z':6.5,'lenses':[16,18,20,22,24], 'grid':[(x,y) for x in [40,43,46,50,53,56] for y in [-0.5,2,4.5]][:18], 'target_y':[9,10,11], 'target_x':[54,57,60], 'target_z':[2.6,3,3.4]},
'B': {'cam':'F08_CAMERA_B_FUNCTIONAL','z':6.5,'lenses':[18,20,22,24,28,32], 'grid':[(x,y) for x in [43,47,51] for y in [1.5,3.5,5.5]], 'target_y':[9,10,11], 'target_x':[54,56.5,59], 'target_z':[2.6,3,3.5]},
'C': {'cam':'F08_CAMERA_C_SEQUENCE_DETAIL','z':6.1,'lenses':[20,22,24,26,28,30,32], 'grid':[(x,y) for x in [48,51.5,55] for y in [2.5,4.25,6]], 'target_y':[9,10,11], 'target_x':[56,58.5,61], 'target_z':[2.5,3,3.5]},
'D': {'cam':'F08_CAMERA_D_INTEGRATED','z':6.5,'lenses':[16,18,20,22,24], 'grid':[(x,y) for y in [0,2.25,4.5] for x in [40,47,54]]+[(x,y) for y in [16,18,20] for x in [40,47,54]], 'target_y':[9,10,11], 'target_x':[52,54.5,57], 'target_z':[2.8,3.15,3.5]},
}
def in_any_mesh_aabb(p):
    hits=[]
    for ob in scene.objects:
        if ob.type!='MESH': continue
        corners=[ob.matrix_world@Vector(c) for c in ob.bound_box]
        lo=[min(c[i] for c in corners) for i in range(3)]; hi=[max(c[i] for c in corners) for i in range(3)]
        if all(lo[i]-1e-5<=p[i]<=hi[i]+1e-5 for i in range(3)): hits.append(ob.name)
    return hits
scene.render.engine='BLENDER_EEVEE';scene.eevee.taa_render_samples=8
scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8'
scene.render.film_transparent=False
index_path=BASE/'F08_R01_CAMERA_CANDIDATES.json'
all_records=json.loads(index_path.read_text(encoding='utf-8'))['records'] if index_path.exists() else []
completed={r['id'] for r in all_records if r.get('rendered')}
for role,cfg in roles.items():
    outdir=BASE/'candidates'/role;outdir.mkdir(parents=True,exist_ok=True)
    cam=bpy.data.objects[cfg['cam']]
    for idx,(x,y) in enumerate(cfg['grid'],1):
        # 18 deterministic probes per family; vary target and lens as well as origin.
        key=f'{role}_{idx:03d}'
        if key in completed: continue
        lens=cfg['lenses'][(idx-1)%len(cfg['lenses'])]
        ty=cfg['target_y'][(idx-1)%len(cfg['target_y'])];tx=cfg['target_x'][(idx//3)%len(cfg['target_x'])];tz=cfg['target_z'][(idx//2)%len(cfg['target_z'])]
        pos=Vector((x,y,cfg['z'])); target=Vector((tx,ty,tz))
        cam.location=pos;cam.rotation_euler=(target-pos).to_track_quat('-Z','Y').to_euler();cam.data.lens=lens;cam.data.sensor_width=36;scene.camera=cam
        filepath=outdir/f'{key}_900x600.png'; scene.render.filepath=str(filepath)
        rec={'id':key,'role':role,'camera_object':cam.name,'origin_xyz':[round(v,4) for v in pos],'target_xyz':[round(v,4) for v in target],'lens_mm':lens,'sensor_width_mm':36,'resolution':[900,600],'camera_inside_mesh_aabb_objects':in_any_mesh_aabb(pos),'wall_ceiling_clipping':False,'visibility_changed':False,'render_path':str(filepath),'rendered':False,'visual_cues':{'all_process_stages_readable':None,'preform_heating_readable':None,'stretch_blow_molding_readable':None,'formed_bottle_discharge_readable':None,'conveyor_flow_readable':None,'aisle_or_access_readable':None,'critical_equipment_obstructed':None,'black_or_empty_field':None},'visual_verdict':'PENDING_IMAGE_REVIEW'}
        print('R01_RENDER_BEGIN',key,'camera_aabb_hits',rec['camera_inside_mesh_aabb_objects'],flush=True)
        try:
            result=bpy.ops.render.render(write_still=True)
            rec['rendered']=bool(filepath.exists());rec['render_result']=str(result)
        except Exception as e: rec['render_error']=repr(e)
        all_records.append(rec)
        index_path.write_text(json.dumps({'schema':'F08_R01_CAMERA_CANDIDATES_V1','note':'Candidate metadata only; all choices require actual rendered-image review.','records':all_records},indent=2),encoding='utf-8')
        print('R01_RENDER_END',key,rec['rendered'],flush=True)
print('R01_BATCH_DONE',len(all_records),flush=True)
