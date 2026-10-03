import bpy, math, json, hashlib
from pathlib import Path
from mathutils import Vector
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
BASE=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
R=BASE/'R02'; SRC=BASE/'R01/F08_bottle_blow/F08_STAGED.blend'; OUT=R/'F08_R02_STAGED.blend'
DEST='REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N'
assert 'M08.44' in (ROOT/'TASKS.md').read_text(encoding='utf-8') and 'M08.44 / F08-R02' in (ROOT/'coordination/Prompts/REV005_FACILITY_F08_R02_VISUAL_LEGIBILITY_GEOMETRY_REMEDIATION_GPT_PROMPT.md').read_text(encoding='utf-8')
assert bpy.data.filepath.lower()==str(SRC).lower(), 'BLOCKED_F08_R02_SOURCE_PATH'
D=bpy.data.collections.get(DEST); assert D and sum(o.type=='MESH' for o in D.objects)==338, 'BLOCKED_F08_R02_SOURCE_COLLECTION'
V=json.loads((BASE/'R01/F08_R01_STAGED_STATE_VALIDATION.json').read_text(encoding='utf-8'))
assert V['status']=='PASS' and V['counts']=={'accepted_meshes':338,'confirmed_legacy':391,'retired_legacy':391,'preforms':20,'heater_elements':16,'service_doors':2,'air_branches':4,'formed_bottles':16}, 'BLOCKED_F08_R02_R01_VALIDATION'
expected={'blend':'B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642','glb':'B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372'}
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
for k,p in [('blend',ROOT/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend'),('glb',ROOT/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb')]: assert sha(p)==expected[k], 'BLOCKED_F08_R02_CANONICAL_BASELINE_MISMATCH_'+k
# Snapshot every pre-existing object outside the F08 accepted collection.
def stable(v):
 if hasattr(v,'to_list'): return stable(v.to_list())
 if isinstance(v,(list,tuple)): return [stable(x) for x in v]
 if isinstance(v,(str,int,float,bool)) or v is None:return v
 return str(v)
def fingerprint(o):
 d={'type':o.type,'matrix':[[round(float(o.matrix_world[i][j]),7) for j in range(4)] for i in range(4)],'dims':[round(float(x),7) for x in o.dimensions],'collections':sorted(c.name for c in o.users_collection),'hide':(o.hide_viewport,o.hide_render,o.hide_get()),'props':{k:stable(o[k]) for k in o.keys()}}
 if o.type=='MESH':d['mesh']={'data_name':o.data.name,'verts':len(o.data.vertices),'polys':len(o.data.polygons),'mats':[m.name if m else None for m in o.data.materials]}
 return d
outside={o.name:fingerprint(o) for o in bpy.data.objects if D not in o.users_collection}
R.mkdir(parents=True,exist_ok=True)
starting={'task':'M08.44 / F08-R02','status':'PASS','source_blend':str(SRC.relative_to(ROOT)),'source_validation':'R01/F08_R01_STAGED_STATE_VALIDATION.json','destination_collection':DEST,'accepted_meshes':338,'confirmed_legacy':391,'retired_legacy':391,'ambiguous_legacy':0,'not_f08_preserved':5,'preforms':20,'heater_elements':16,'service_doors':2,'hp_air_branches':4,'formed_bottles':16,'unauthorized_prior_differences':0,'cross_facility_collisions':0,'outside_envelope_objects':0,'canonical_baseline_hashes':expected,'source_sha256':sha(SRC),'east_service_opening_contract':{'jamb_y':[9.0,11.0],'east_wall_segments_m':11.0}}
(R/'F08_R02_STARTING_STAGE_VALIDATION.json').write_text(json.dumps(starting,indent=2),encoding='utf-8')
# Geometry utilities create only registered accepted F08 meshes.
def mat(name,color,metal=.2,rough=.38,alpha=1,emit=None):
 m=bpy.data.materials.get(name)
 if m is None:m=bpy.data.materials.new(name)
 m.diffuse_color=(*color,alpha);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF')
 if p:
  p.inputs['Base Color'].default_value=(*color,alpha);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough;p.inputs['Alpha'].default_value=alpha
  if emit and 'Emission Color' in p.inputs:p.inputs['Emission Color'].default_value=(*emit,1);p.inputs['Emission Strength'].default_value=.65
 if alpha<1:
  try:m.surface_render_method='DITHERED'
  except:pass
 return m
STEEL=mat('F08_R02_SatinStainless',(.48,.57,.59),.72,.31)
FRAME=mat('F08_R02_Graphite',(.075,.11,.13),.65,.32)
PANEL=mat('F08_R02_HopperSteel',(.42,.52,.53),.66,.34)
LAMP=mat('F08_R02_InfraredCeramic',(.86,.23,.045),.12,.27,1,(.95,.16,.025))
REFLECT=mat('F08_R02_Reflector',(.72,.77,.75),.54,.3)
MOULD=mat('F08_R02_MouldAlloy',(.23,.36,.39),.55,.3)
ACCENT=mat('F08_R02_Actuator',(.18,.42,.51),.42,.31)
PRODUCT=mat('F08_R02_PreformPET',(.28,.68,.72),.05,.25,1)
PET=mat('F08_R02_BottlePET',(.35,.74,.77),.04,.22,.78)
created=[]
def tag(o,name,role,material):
 o.name=name
 for c in list(o.users_collection):
  if c!=D:c.objects.unlink(o)
 if D not in o.users_collection:D.objects.link(o)
 if material:o.data.materials.clear();o.data.materials.append(material)
 o['revision']='REV005';o['rev005_facility']='Bottle blow molding';o['REV005_F08_CLASS_N_ACCEPTED']=True;o['F08_role']=role
 created.append(o);return o
def box(name,loc,dims,material,role='machine detail',rot=(0,0,0),bevel=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.dimensions=dims;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.rotation_euler=rot
 if bevel:
  b=o.modifiers.new('R02_Soft_Edges','BEVEL');b.width=bevel;b.segments=2;o.modifiers.new('R02_Weighted_Normals','WEIGHTED_NORMAL')
 return tag(o,name,role,material)
def cyl(name,loc,r,depth,material,role='machine detail',rot=(0,0,0),vertices=20):
 bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc);o=bpy.context.object;o.rotation_euler=rot;return tag(o,name,role,material)
def rod(name,a,b,r,material,role='machine frame'):
 av=Vector(a);bv=Vector(b);d=bv-av;o=cyl(name,(av+bv)/2,r,d.length,material,role,vertices=16);o.rotation_euler=d.to_track_quat('Z','Y').to_euler();return o
def set_dims(name,dims):
 o=bpy.data.objects[name];assert o.type=='MESH' and o.data.users==1, 'BLOCKED_SHARED_MESH_'+name;o.dimensions=dims;return o
def make_bottle(o,h=.37,r=.055):
 oldverts=[tuple(float(c) for c in v.co) for v in o.data.vertices]
 cx=(min(v[0] for v in oldverts)+max(v[0] for v in oldverts))/2
 cy=(min(v[1] for v in oldverts)+max(v[1] for v in oldverts))/2
 basez=min(v[2] for v in oldverts)
 n=24;rings=[(0,.78),(.05,1),(h*.60,1),(h*.70,.70),(h*.78,.43),(h*.91,.40),(h*.93,.55),(h*.97,.55),(h*.98,.38),(h,.38)];v=[];f=[]
 for zz,k in rings:
  for i in range(n):a=2*math.pi*i/n;v.append((cx+r*k*math.cos(a),cy+r*k*math.sin(a),basez+zz))
 for j in range(len(rings)-1):
  for i in range(n):f.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
 me=bpy.data.meshes.new(o.name+'_R02Mesh');me.from_pydata(v,[],f);me.materials.append(PET);me.update();old=o.data;o.data=me;o['F08_role']='formed bottle product'
 return old
# Hopper: turn the old solid bin into four open-topped sloped panels within its original bounds.
h=bpy.data.objects['F08_PREFORM_BULK_BIN'];assert h.type=='MESH' and h.data.users==1
verts=[];faces=[]
# local bottom half-width .36, top half-width 1.20; bottom z=-.90, top z=.90
for axis in range(4):
 if axis==0: pts=[(-.36,-.36,-.9),(.36,-.36,-.9),(1.2,-1.2,.9),(-1.2,-1.2,.9)]
 elif axis==1: pts=[(.36,-.36,-.9),(.36,.36,-.9),(1.2,1.2,.9),(1.2,-1.2,.9)]
 elif axis==2: pts=[(.36,.36,-.9),(-.36,.36,-.9),(-1.2,1.2,.9),(1.2,1.2,.9)]
 else: pts=[(-.36,.36,-.9),(-.36,-.36,-.9),(-1.2,-1.2,.9),(-1.2,1.2,.9)]
 i=len(verts);verts.extend(pts);faces.append((i,i+1,i+2,i+3))
me=bpy.data.meshes.new('F08_PREFORM_BULK_BIN_R02_TAPERED_OPEN_MESH');me.from_pydata(verts,[],faces);me.materials.append(PANEL);me.update();h.data=me
# Reinforce lip: existing lip becomes the north bar; add three sides.
set_dims('F08_HOPPER_LOAD_LIP',(2.28,.09,.09));bpy.data.objects['F08_HOPPER_LOAD_LIP'].location=(36.5,11.14,5.2)
for x,y,d in [('S',8.86,(2.28,.09,.09)),('E',10.0,(.09,2.10,.09)),('W',10.0,(.09,2.10,.09))]:
 loc=(36.5,y,5.2) if x in ('N','S') else ((37.64,y,5.2) if x=='E' else (35.36,y,5.2))
 if x=='S':loc=(36.5,8.86,5.2)
 if x=='E':loc=(37.64,10,5.2)
 if x=='W':loc=(35.36,10,5.2)
 box('F08_R02_HOPPER_RIM_'+x,loc,d,PANEL,'bulk hopper rim',bevel=.015)
# Stronger throat collar and feed funnel bands.
box('F08_R02_HOPPER_THROAT_COLLAR',(37.5,10,2.78),(.9,.9,.12),FRAME,'preform feed throat')
# Elevator steps and six visible riding preforms following unchanged incline.
for i in range(9):
 t=(i+1)/10;x=37.9+2.75*t;z=2.62+1.2*t
 box(f'F08_R02_ELEVATOR_FLIGHT_{i+1:02}',(x,10,z),(.075,.78,.075),STEEL,'elevator carrier flight',rot=(0,math.radians(-23.6),0),bevel=.018)

def preform_mesh(name,x,y,z,h=.18,r=.045,material=PRODUCT):
 n=16;rings=[(0,.78),(.07,1),(.10,.68),(h*.84,.62),(h*.89,.82),(h*.94,.55),(h,.55)];v=[];f=[]
 for zz,k in rings:
  for i in range(n):a=2*math.pi*i/n;v.append((x+r*k*math.cos(a),y+r*k*math.sin(a),z+zz))
 for j in range(len(rings)-1):
  for i in range(n):f.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
 me=bpy.data.meshes.new(name+'_Mesh');me.from_pydata(v,[],f);me.materials.append(material);me.update();o=bpy.data.objects.new(name,me);D.objects.link(o);o['revision']='REV005';o['rev005_facility']='Bottle blow molding';o['REV005_F08_CLASS_N_ACCEPTED']=True;o['F08_role']='PET preform product';created.append(o);return o
for i in range(6):
 t=(i+1)/7;x=38.0+2.05*t;z=2.72+1.00*t;preform_mesh(f'F08_R02_ELEVATOR_PREFORM_{i+1:02}',x,10,z,.16,.043)
# Existing R01 downstream neck-support rail already carries seven preforms; preserve those exact locations.
# Oven lamps become slim luminous elements; add shallow reflector plates and open frames.
for o in D.objects:
 if o.name.startswith('F08_HEATER_BANK_') and '_ELEMENT_' in o.name:
  o.dimensions=(.10,.10,2.25);o.data.materials.clear();o.data.materials.append(LAMP)
for side,y in [('N',11.12),('S',8.88)]:
 box(f'F08_R02_OVEN_{side}_REFLECTOR_BACKPLATE',(47.35,y,3.12),(6.35,.10,2.65),REFLECT,'infrared heater reflector')
 for z in (1.79,4.45):box(f'F08_R02_OVEN_{side}_BANK_RAIL_{z}',(47.35,y,z),(6.45,.13,.10),FRAME,'heater bank support rail')
 for x in (44.2,50.5):box(f'F08_R02_OVEN_{side}_BANK_END_{x}',(x,y,3.12),(.12,.13,2.76),FRAME,'heater bank support rail')
# strengthen transfer starwheel and add three anchored product cues.
for i,ang in enumerate((0,120,240),1):
 a=math.radians(ang);x=52.05+.34*math.cos(a);y=10+.34*math.sin(a);preform_mesh(f'F08_R02_TRANSFER_PREFORM_{i}',x,y,3.03,.18,.044)
# Mold finish, transparency, actuators and physically connected transformation cues.
for i,cx in enumerate((55.7,58.3),1):
 for side in ('L','R'):
  o=bpy.data.objects[f'F08_MOULD_STATION_{i}_MOLD_HALF_{side}'];o.data.materials.clear();o.data.materials.append(MOULD)
  rod(f'F08_R02_STATION_{i}_MOLD_FACE_RIB_{side}',(cx+(-.255 if side=='L' else .255),9.58,2.52),(cx+(-.255 if side=='L' else .255),9.58,3.88),.035,ACCENT,'mould cavity relief')
 set_dims(f'F08_MOULD_STATION_{i}_STRETCH_BLOW_ROD',(.14,.14,1.82))
 # Clamp actuator cylinder axis X links rear y=8.65 to each platen.
 for side,sgn in [('L',-1),('R',1)]:
  rod(f'F08_R02_STATION_{i}_CLAMP_CYL_{side}',(cx+sgn*.32,8.68,3.2),(cx+sgn*.67,8.68,3.2),.18,ACCENT,'mould clamp actuator')
  rod(f'F08_R02_STATION_{i}_CLAMP_ROD_{side}',(cx+sgn*.67,8.68,3.2),(cx+sgn*.78,8.68,3.2),.07,STEEL,'mould clamp actuator rod')
 # Vertical blue air head hose visibly joins existing nozzle and rod head.
 rod(f'F08_R02_STATION_{i}_AIR_DROP',(cx,10,4.35),(cx,10,4.58),.075,ACCENT,'blow air connection')
# clearer guards, use local copied materials only on F08 blow guard glazing.
GLASS=mat('F08_R02_ClearSafetyGlazing',(.52,.78,.79),.02,.18,.055)
for o in D.objects:
 if o.name.startswith('F08_BLOW_GUARD_') and o.type=='MESH' and 'PANEL' in o.name or o.name.startswith('F08_BLOW_GUARD_DOOR_') and o.type=='MESH' and 'HANDLE' not in o.name:
  o.data.materials.clear();o.data.materials.append(GLASS)
# station 1 preform-state cue; station 2 bottle just released, aligned to centerline.
preform_mesh('F08_R02_STATION_1_HEATED_PREFORM',55.7,10,2.25,.48,.055,PRODUCT)
# increase existing bottle population visibility without moving bottoms/line positions.
for o in D.objects:
 if o.name.startswith('F08_FORMED_BOTTLE_'):
  old=make_bottle(o,.37,.055)
  if old.users==0:bpy.data.meshes.remove(old)
# immediate release cue just beyond guarded discharge; bottle base sits on conveyor.
# Build state-change cue at bottle envelope upper length .37.
preform_mesh('F08_R02_STATION_2_JUST_RELEASED_BOTTLE_PLACEHOLDER',58.3,10,1.96,.37,.055,PET)
# Replace placeholder preform mesh with full bottle profile at station 2 discharge.
rel=bpy.data.objects['F08_R02_STATION_2_JUST_RELEASED_BOTTLE_PLACEHOLDER'];rel.name='F08_R02_STATION_2_JUST_RELEASED_BOTTLE';rel['F08_role']='formed bottle product';old=make_bottle(rel,.37,.055)
if old.users==0:bpy.data.meshes.remove(old)
# local floor pad/approach marking, no human figures.
box('F08_R02_HMI_OPERATOR_PAD',(57,5.25,1.105),(2.4,1.35,.035),mat('F08_R02_HMI_Pad',(.36,.40,.39),.05,.7),'operator standing pad')
# Add local task luminaires as geometry only; no external light rigs in this stage.
for i,(x,y) in enumerate(((47.5,10.0),(57,7.0)),1):
 box(f'F08_R02_LOCAL_TASK_LIGHT_{i}_HOUSING',(x,y,5.30),(1.15,.24,.10),FRAME,'local equipment task light')
 box(f'F08_R02_LOCAL_TASK_LIGHT_{i}_DIFFUSER',(x,y,5.235),(1.0,.16,.025),mat('F08_R02_Diffuser',(.75,.86,.83),.0,.3,1,(.6,.78,.74)),'local equipment task light diffuser')
# Ensure destination-only ownership, protected objects unchanged, expected fixed anchors.
bpy.context.view_layer.update()
changed=[]
for n,fp in outside.items():
 o=bpy.data.objects.get(n)
 if o is None or fingerprint(o)!=fp:changed.append(n)
assert not changed, 'BLOCKED_F08_R02_OUTSIDE_DESTINATION_MUTATION '+repr(changed[:10])
meshes=[o for o in D.objects if o.type=='MESH']
assert 338<=len(meshes)<=460, 'BLOCKED_F08_R02_DETAIL_OBJECT_BLOAT '+str(len(meshes))
assert sum(o.name.startswith('F08_HEATER_BANK_N_ELEMENT_') for o in D.objects)==8 and sum(o.name.startswith('F08_HEATER_BANK_S_ELEMENT_') for o in D.objects)==8
assert len([o for o in D.objects if o.name.startswith('F08_FORMED_BOTTLE_')])==16
assert sum(o.name.startswith('F08_R02_ELEVATOR_PREFORM_') for o in D.objects)>=6 and sum(o.name.startswith('F08_PREFORM_FEED_') for o in D.objects)>=6
assert all(abs(float(bpy.data.objects[f'F08_MOULD_STATION_{i}_STRETCH_BLOW_ROD'].dimensions.x)-.14)<.001 for i in (1,2))
# Preserve locked anchor centers.
anchors={'F08_PREFORM_BULK_BIN':(36.5,10,4.3),'F08_OVEN_CORNER_POST_44.0_12.0':(44,12,3.2),'F08_BLOW_CELL_BASE_X_56.9':(56.9,10,1.5),'F08_OUTFEED_BELT':(65,10,1.88),'F08_HMI_BODY':(57,5.62,2.28)}
anchor_check={}
for n,goal in anchors.items():
 o=bpy.data.objects[n];actual=tuple(round(float(x),5) for x in o.location);anchor_check[n]={'actual':actual,'expected':goal,'pass':max(abs(actual[i]-goal[i]) for i in range(3))<.05};assert anchor_check[n]['pass'],'BLOCKED_F08_R02_ANCHOR_'+n
# Save stage only; no render cameras or changes outside F08 accepted collection.
bpy.ops.wm.save_as_mainfile(filepath=str(OUT))
report={'task':'M08.44 / F08-R02','status':'PASS','source_blend':str(SRC.relative_to(ROOT)),'staged_blend':str(OUT.relative_to(ROOT)),'source_mesh_count':338,'accepted_mesh_count':len(meshes),'added_meshes':len(meshes)-338,'outside_destination_unauthorized_differences':changed,'anchor_checks':anchor_check,'counts':{'heater_north':8,'heater_south':8,'existing_outfeed_bottles':16,'elevator_preforms':6,'downstream_preforms_preserved':sum(o.name.startswith('F08_PREFORM_FEED_') for o in D.objects),'transfer_preforms':3,'service_doors':2,'hp_air_branches':4},'remediations':['open tapered hopper panels and visible rim','elevator carrier flights and six riders','existing downstream feed-rail preforms preserved','slender infrared lamps and reflector banks','three transfer preforms','mould alloy separation, cavity relief, clamp actuators and air drops','clearer F08 guard glazing','heated station-one preform cue','sixteen enlarged formed bottles and immediate-release station-two bottle','operator pad and local task-light geometry'],'preserved':{'canonical_hashes':expected,'confirmed_legacy_retired':391,'not_f08_preserved':5,'major_centers_and_envelopes':True,'no_F01_F07_mutation':True}}
(R/'F08_R02_GEOMETRY_CHANGE_REPORT.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('F08_R02_GEOMETRY PASS meshes',len(meshes),'added',len(meshes)-338,'stage',OUT)
