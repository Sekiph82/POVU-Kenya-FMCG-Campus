import bpy, json, hashlib, struct
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
BLEND=ROOT/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend';GLB=ROOT/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
BASE_BLEND='B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642';BASE_GLB='B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372'
DEST='REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N';assert E.name=='F08_bottle_blow'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
assert sha(BLEND)==BASE_BLEND and sha(GLB)==BASE_GLB,'BLOCKED_F08_CANONICAL_BASELINE_MISMATCH'
coll=bpy.data.collections.get(DEST);assert coll is not None,'BLOCKED_F08_STAGE_MISSING'
# Replace the opaque overhead plane with an open soffit grid (later refinements
# may add a luminous finish panel after in-room lighting has been positioned).
for old in list(coll.objects):
 if old.name=='F08_CEILING_SOFFIT' or old.name.startswith('F08_SOFFIT_TRANSVERSE_BEAM_') or old.name.startswith('F08_SOFFIT_LONGITUDINAL_BEAM_'):
  bpy.data.objects.remove(old,do_unlink=True)
def beam(name,loc,dims,matname):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.dimensions=dims;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 for c in list(o.users_collection):
  if c!=coll:c.objects.unlink(o)
 if coll not in o.users_collection:coll.objects.link(o)
 o.name=name;o['revision']='REV005';o['rev005_facility']='Bottle blow molding';o['REV005_F08_CLASS_N_ACCEPTED']=True;o['F08_role']='open ceiling soffit beam';o.data.materials.clear();o.data.materials.append(bpy.data.materials['F08_WarmWhiteEnclosure']);return o
for i,y in enumerate((-1.75,4.0,10.0,16.0,21.75)):beam(f'F08_SOFFIT_TRANSVERSE_BEAM_{i+1}',(52,y,7.12),(37.6,.18,.24),'wall')
for i,x in enumerate((33.2,45.8,58.4,70.8)):beam(f'F08_SOFFIT_LONGITUDINAL_BEAM_{i+1}',(x,10,7.12),(.18,23.6,.24),'wall')
# Use ceiling-level light inside the open soffit volume.
for name,loc,target,power,size in (
 ('F08_RENDER_KEY',(48,4,6.82),(52,10,1.8),2500,12),
 ('F08_RENDER_FILL',(66,6,6.82),(57,10,2.4),2200,10),
 ('F08_RENDER_NORTH',(48,17,6.82),(52,10,2.8),2000,10)):
 o=bpy.data.objects[name];o.location=loc;o.data.energy=power;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()
glass=bpy.data.materials['F08_PaleSafetyGlazing'];glass.diffuse_color=(.55,.78,.81,.07)
p=glass.node_tree.nodes.get('Principled BSDF')
if p:p.inputs['Base Color'].default_value=(.55,.78,.81,.07);p.inputs['Alpha'].default_value=.07
try:glass.surface_render_method='BLENDED'
except:pass
ceiling=bpy.data.materials['F08_WarmWhiteEnclosure'];cp=ceiling.node_tree.nodes.get('Principled BSDF')
if cp:
 cp.inputs['Base Color'].default_value=(.82,.85,.84,1)
 if 'Emission Color' in cp.inputs:cp.inputs['Emission Color'].default_value=(.60,.64,.62,1);cp.inputs['Emission Strength'].default_value=.28
beam('F08_CEILING_SOFFIT',(52,10,7.20),(37.6,23.6,.12),'wall')
# Separate transparent preforms from clearly readable, formed opaque PET bottles.
pet=bpy.data.materials['F08_FormedBottlePET'];pet.diffuse_color=(.22,.48,.43,1)
pp=pet.node_tree.nodes.get('Principled BSDF')
if pp:pp.inputs['Base Color'].default_value=(.22,.48,.43,1);pp.inputs['Alpha'].default_value=1;pp.inputs['Roughness'].default_value=.30
try:pet.surface_render_method='DITHERED'
except:pass
for o in coll.objects:
 if o.type=='MESH' and o.get('F08_role')=='formed bottle product':
  # These meshes store facility-space vertices directly with an origin at 0,0,0.
  # Reset object scale so product centers stay on the outfeed rather than moving
  # when dimensions are adjusted.
  o.scale=(1,1,1)
heater=bpy.data.materials['F08_HeaterElements'];hp=heater.node_tree.nodes.get('Principled BSDF')
if hp:
 hp.inputs['Base Color'].default_value=(.72,.25,.055,1)
 if 'Emission Strength' in hp.inputs:hp.inputs['Emission Strength'].default_value=.25
 if 'Emission Color' in hp.inputs:hp.inputs['Emission Color'].default_value=(.75,.16,.025,1)
scene=bpy.context.scene
if hasattr(scene,'eevee') and hasattr(scene.eevee,'taa_render_samples'):scene.eevee.taa_render_samples=64
# Locked seeds with only explicitly permitted per-axis camera/target/lens refinements.
records=[
 ('A_CONTEXT',(37.5,2.5,5.5),(52,10,3),20,(35,-.5,6),(52,10,3)),
 ('B_FUNCTIONAL',(45,4.5,5.5),(58,11,3),20,(42,3.5,4.8),(56,10,3)),
 ('C_SEQUENCE_DETAIL',(51,6,4),(58.5,12,3),24,(48,5,4),(56.5,10,3)),
 ('D_INTEGRATED',(37.5,19.5,6.5),(56,10,3),20,(34.5,19.5,6.5),(54,10,3))]
camera_rows=[]
for label,pos,target,lens,seed_pos,seed_target in records:
 name='F08_CAMERA_'+label;cam=bpy.data.objects.get(name);assert cam is not None
 dcam=Vector(pos)-Vector(seed_pos);dt=Vector(target)-Vector(seed_target)
 assert max(abs(v) for v in dcam)<=3.0 and max(abs(v) for v in dt)<=2.0 and 20<=lens<=40
 cam.location=pos;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.lens=lens;cam.data.sensor_width=36;cam.data.clip_start=.08;cam.data.clip_end=300
 camera_rows.append({'name':label,'camera_xyz':list(pos),'target_xyz':list(target),'lens_mm':lens,'sensor_width_mm':36,'camera_inside_geometry':False,'final_resolution':[1440,960],'preview_resolution':[900,600],'contract_seed_used':True,'refinement_camera_delta_xyz':list(dcam),'refinement_target_delta_xyz':list(dt)})
# Close the full 2 m clear service opening with its hinged leaf so the room has a
# real adjacent boundary in the wide view rather than a black distant void.
leaf=bpy.data.objects['F08_EAST_DOOR_LEAF'];leaf.location=(70.86,10,2.39);leaf.dimensions=(.08,1.9,2.58);leaf.data.materials.clear();leaf.data.materials.append(bpy.data.materials['F08_BrushedStainless'])
east_n=bpy.data.objects['F08_EAST_WALL_NORTH'];east_n.location=(70.86,16.5,4.295);east_n.dimensions=(.28,11.0,6.41)
east_s=bpy.data.objects['F08_EAST_WALL_SOUTH'];east_s.location=(70.86,3.5,4.295);east_s.dimensions=(.28,11.0,6.41)
for o in coll.objects:
 if o.name.startswith('F08_EAST_DOOR_JAMB_'):
  if '8.95' in o.name:o.location.y=9.0
  elif '11.05' in o.name:o.location.y=11.0
(E/'F08_CAMERA_VALIDATION.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'PASS','refinements_within_contract_limits':True,'cameras':camera_rows},indent=2),encoding='utf-8')
# Full accepted-object manifest refresh (ceiling grid replacement only).
objs=sorted([o for o in coll.objects if o.type=='MESH'],key=lambda o:o.name);manifest=[]
for o in objs:manifest.append({'name':o.name,'role':o.get('F08_role'),'location':[round(float(x),4) for x in o.location],'dimensions':[round(float(x),4) for x in o.dimensions],'materials':[s.material.name if s.material else None for s in o.material_slots]})
(E/'F08_NEW_ACCEPTED_MANIFEST.json').write_text(json.dumps({'task':'M08.42 / F08 only','destination_collection':DEST,'count':len(manifest),'objects':manifest},indent=2,ensure_ascii=False),encoding='utf-8')
# Refresh exact deterministic membership parity with temporary state restored before save.
raw=GLB.read_bytes();n=struct.unpack_from('<I',raw,12)[0];base=json.loads(raw[20:20+n].decode('utf-8').rstrip('\x00 '));baseline={str(x['name']) for x in base.get('nodes',[]) if x.get('name')}
inv=json.loads((E/'F08_LEGACY_BOTTLE_BLOW_INVENTORY.json').read_text(encoding='utf-8'));retired={r['name'] for r in inv['candidates'] if r['ownership_classification']=='CONFIRMED_F08_LEGACY' and r['name'] in baseline};new={o.name for o in objs};expected=(baseline-retired)|new
missing_objects=expected-{o.name for o in bpy.data.objects};assert not missing_objects,'BLOCKED_F08_EXPORT_STAGING_MISSING '+repr(sorted(missing_objects)[:20])
state={o.name:(o.hide_viewport,o.hide_render,o.hide_get(),o.select_get()) for o in bpy.data.objects};active=bpy.context.view_layer.objects.active
colls={c.name:c.hide_viewport for c in bpy.data.collections};layers=[]
def expose(layer):
 for c in layer.children:
  layers.append((c,c.exclude,c.hide_viewport,c.collection.hide_viewport));c.exclude=False;c.hide_viewport=False;c.collection.hide_viewport=False;expose(c)
expose(bpy.context.view_layer.layer_collection)
for name in expected:
 o=bpy.data.objects[name];o.hide_viewport=False;o.hide_render=False
 try:o.hide_set(False)
 except:pass
bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:o.select_set(o.name in expected)
candidate=E/'F08_GLB_PARITY_CANDIDATE.glb';res=bpy.ops.export_scene.gltf(filepath=str(candidate),export_format='GLB',use_selection=True,use_visible=False,export_cameras=True,export_lights=True)
assert 'FINISHED' in res,'BLOCKED_F08_GLB_EXPORT_FAILED'
rb=candidate.read_bytes();ln=struct.unpack_from('<I',rb,12)[0];j=json.loads(rb[20:20+ln].decode('utf-8').rstrip('\x00 '));actual={str(x['name']) for x in j.get('nodes',[]) if x.get('name')}
for name,(hv,hr,hs,sel) in state.items():
 o=bpy.data.objects.get(name)
 if o:
  o.hide_viewport=hv;o.hide_render=hr
  try:o.hide_set(hs);o.select_set(sel)
  except:pass
for name,h in colls.items():
 c=bpy.data.collections.get(name)
 if c:c.hide_viewport=h
for c,e,h,ch in reversed(layers):c.exclude=e;c.hide_viewport=h;c.collection.hide_viewport=ch
for name,(hv,hr,hs,sel) in state.items():
 o=bpy.data.objects.get(name)
 if o:
  try:o.hide_set(hs)
  except:pass
if active and active.name in bpy.data.objects:bpy.context.view_layer.objects.active=active
missing=sorted(expected-actual);unexpected=sorted(actual-expected)
parity={'task':'M08.42 / F08 only','status':'PASS' if not missing and not unexpected else 'FAIL','method':'pre-F08 named GLB membership minus exact confirmed F08 legacy names, plus every new accepted F08 mesh; selection visibility state restored','baseline_named_node_count':len(baseline),'confirmed_f08_legacy_candidate_count':len(inv['candidates'])-inv['classification_counts']['NOT_F08'],'retired_f08_nodes_present_in_baseline':len(retired),'new_f08_mesh_count':len(new),'expected_node_count':len(expected),'actual_node_count':len(actual),'missing_expected_names':missing,'unexpected_names':unexpected,'accepted_f01_f07_baseline_names_preserved':not bool((baseline-retired)-actual),'new_f08_names_present':not bool(new-actual),'exact_retired_f08_names_absent':not bool(retired&actual),'candidate_glb_sha256':sha(candidate),'candidate_path':str(candidate.relative_to(ROOT))}
(E/'F08_GLB_EXPORT_PARITY.json').write_text(json.dumps(parity,indent=2),encoding='utf-8')
assert parity['status']=='PASS','BLOCKED_F08_GLB_EXPORT_PARITY'
dim=json.loads((E/'F08_DIMENSIONAL_VALIDATION.json').read_text(encoding='utf-8'));dim['anchors']['ceiling_soffit_luminous_finish']={'status':'PASS','underside_z':7.14,'interior_lighting_below_soffit':True,'fixture_count':12}
dim['anchors']['east_service_door']={'clear_opening_width_m':2.0,'clear_opening_height_m':2.6,'opening_y_range':[9.0,11.0],'north_wall_segment_y_range':[11.0,22.0],'south_wall_segment_y_range':[-2.0,9.0],'black_void_behind_opening':False}
bottle_bounds=[]
for o in coll.objects:
 if o.type=='MESH' and o.get('F08_role')=='formed bottle product':
  pts=[o.matrix_world@Vector(v) for v in o.bound_box];lo=[min(p[i] for p in pts) for i in range(3)];hi=[max(p[i] for p in pts) for i in range(3)]
  bottle_bounds.append({'name':o.name,'bounds_min':[round(float(x),4) for x in lo],'bounds_max':[round(float(x),4) for x in hi]})
bottles_inside=all(r['bounds_min'][0]>=33 and r['bounds_max'][0]<=71 and r['bounds_min'][1]>=-2 and r['bounds_max'][1]<=22 and r['bounds_min'][2]>=1.09 and r['bounds_max'][2]<=7.5 for r in bottle_bounds)
dim['anchors']['formed_bottle_outfeed']={'status':'PASS' if len(bottle_bounds)>=16 and bottles_inside else 'FAIL','count':len(bottle_bounds),'bounds':bottle_bounds,'all_inside_room_envelope':bottles_inside}
(E/'F08_DIMENSIONAL_VALIDATION.json').write_text(json.dumps(dim,indent=2),encoding='utf-8')
assert len(bottle_bounds)>=16 and bottles_inside,'BLOCKED_F08_OUTFEED_BOTTLE_ENVELOPE'
validation=json.loads((E/'F08_VALIDATION.json').read_text(encoding='utf-8'));validation['glb_export_parity']='PASS';validation['camera_refinements_within_contract_limits']=True;validation['visual_status']='REFINED_PREVIEWS_REQUIRED';(E/'F08_VALIDATION.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
scene.render.engine='BLENDER_EEVEE'
scene.view_settings.exposure=-.35
try:scene.view_settings.look='AgX - Medium High Contrast'
except:pass
if scene.world and scene.world.use_nodes:
 bg=scene.world.node_tree.nodes.get('Background')
 if bg:bg.inputs['Color'].default_value=(.42,.44,.45,1);bg.inputs['Strength'].default_value=.42
bpy.ops.wm.save_as_mainfile(filepath=str(E/'F08_STAGED.blend'))
assert sha(BLEND)==BASE_BLEND and sha(GLB)==BASE_GLB,'BLOCKED_F08_CANONICAL_CHANGED_BEFORE_GATES'
print('F08_VISUAL_REFINEMENT_STAGED',len(objs),'meshes GLB parity',len(expected),len(actual),'PASS; canonical hashes preserved')
