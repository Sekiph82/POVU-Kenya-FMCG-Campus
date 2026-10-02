import bpy, math, json, hashlib, struct, os
from pathlib import Path
from mathutils import Vector

ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
BLEND=ROOT/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend'
GLB=ROOT/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
BASE_BLEND='B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642'
BASE_GLB='B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372'
DEST='REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N'
FACILITY='Bottle blow molding'
TASK_ID='M08.42'
assert TASK_ID=='M08.42' and E.name=='F08_bottle_blow', 'BLOCKED_F08_SCOPE_ASSERT'

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''): h.update(b)
 return h.hexdigest().upper()
def cv(v):
 if hasattr(v,'to_list'): return v.to_list()
 if isinstance(v,(str,int,float,bool)) or v is None: return v
 try: return [cv(x) for x in v]
 except: return str(v)
def sig(o):
 return {'name':o.name,'type':o.type,'matrix_world':[[round(float(o.matrix_world[r][c]),9) for c in range(4)] for r in range(4)],
  'dimensions':[round(float(x),9) for x in o.dimensions],'parent':o.parent.name if o.parent else None,
  'collections':sorted(c.name for c in o.users_collection),'material_slots':[s.material.name if s.material else None for s in o.material_slots],
  'data_block':o.data.name if o.data else None,'hide_viewport':bool(o.hide_viewport),'hide_render':bool(o.hide_render),
  'hide_set':bool(o.hide_get()),'custom_properties':{k:cv(o[k]) for k in o.keys()}}

assert sha(BLEND)==BASE_BLEND and sha(GLB)==BASE_GLB, 'BLOCKED_F08_CANONICAL_BASELINE_MISMATCH'
assert not bpy.data.collections.get(DEST), 'BLOCKED_F08_DESTINATION_ALREADY_EXISTS'
inv=json.loads((E/'F08_LEGACY_BOTTLE_BLOW_INVENTORY.json').read_text(encoding='utf-8'))
assert inv['task']=='M08.42 / F08 only' and inv['classification_counts']['AMBIGUOUS_SHARED']==0, 'BLOCKED_F08_LEGACY_OWNERSHIP_AMBIGUITY'
legacy=[r for r in inv['candidates'] if r['ownership_classification']=='CONFIRMED_F08_LEGACY']
not_f08=[r for r in inv['candidates'] if r['ownership_classification']=='NOT_F08']
assert len(legacy)==391 and len(not_f08)==5
assert bpy.data.collections.get('REV005_FG_F07_ADMIN_HQ_RD_QC_ACCEPTED_CLASS_N'), 'BLOCKED_F07_PROTECTED_COLLECTION_MISSING'

coll=bpy.data.collections.new(DEST); bpy.context.scene.collection.children.link(coll)
made=[]; roles={}
def mat(name,color,metal=0,rough=.48,alpha=1,emit=None):
 m=bpy.data.materials.get('F08_'+name) or bpy.data.materials.new('F08_'+name)
 m.diffuse_color=(*color,alpha); m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF')
 if p:
  p.inputs['Base Color'].default_value=(*color,alpha); p.inputs['Metallic'].default_value=metal; p.inputs['Roughness'].default_value=rough; p.inputs['Alpha'].default_value=alpha
  if emit and 'Emission Color' in p.inputs:
   p.inputs['Emission Color'].default_value=(*emit,1); p.inputs['Emission Strength'].default_value=1.5
 if alpha<1:
  try:m.surface_render_method='DITHERED'
  except:pass
 return m
M={
 'floor':mat('IndustrialFloor',(.52,.56,.57),rough=.83),'wall':mat('WarmWhiteEnclosure',(.72,.76,.76),rough=.82),
 'steel':mat('BrushedStainless',(.55,.61,.62),.78,.30),'frame':mat('GraphiteFrames',(.105,.145,.16),.68,.29),
 'guard':mat('SafetyAmber',(.95,.61,.08),.25,.38),'glass':mat('PaleSafetyGlazing',(.55,.78,.81),.05,.2,.16),
 'belt':mat('DarkConveyorBelt',(.075,.095,.10),.18,.55),'poly':mat('PreformPolymer',(.66,.78,.77),.06,.24),
 'pet':mat('FormedBottlePET',(.59,.79,.78),.08,.20,.48),'heater':mat('HeaterElements',(.97,.35,.08),.25,.25,1,(.95,.20,.035)),
 'pipe_air':mat('HighPressureAir',(.18,.43,.61),.55,.34),'pipe_water':mat('CoolingWater',(.10,.48,.53),.38,.31),
 'screen':mat('HMI_Glass',(.025,.075,.085),.16,.18),'white':mat('ControlCabinet',(.78,.81,.80),.26,.4),
 'safety':mat('SafetyRed',(.72,.12,.08),.2,.42),'light':mat('CeilingDiffuser',(.92,.95,.94),.05,.22,1,(.75,.84,.83)),
 'bin':mat('PreformStagingBins',(.35,.43,.42),.2,.52),'floorline':mat('AisleMarking',(.84,.63,.11),.1,.5)}

def register(o,name,role,material=None):
 o.name=name
 if coll not in o.users_collection: coll.objects.link(o)
 for c in list(o.users_collection):
  if c!=coll:c.objects.unlink(o)
 if material and o.type=='MESH':
  o.data.materials.clear();o.data.materials.append(material)
 o['revision']='REV005';o['rev005_facility']=FACILITY;o['REV005_F08_CLASS_N_ACCEPTED']=True;o['F08_role']=role
 made.append(o);roles[o.name]=role
 return o
def box(name,loc,dims,material,role='machine frame',bevel=0,rot=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.dimensions=dims;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.rotation_euler[2]=rot
 if bevel:
  b=o.modifiers.new('Soft_Machine_Edges','BEVEL');b.width=bevel;b.segments=2;o.modifiers.new('Weighted_Normals','WEIGHTED_NORMAL')
 return register(o,name,role,material)
def cyl(name,loc,r,depth,material,role='machine detail',vertices=16,rot=None):
 bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc)
 o=bpy.context.object
 if rot is not None:o.rotation_euler=rot
 return register(o,name,role,material)
def rod(name,a,b,r,material,role='machine frame'):
 av=Vector(a);bv=Vector(b);d=bv-av;o=cyl(name,(av+bv)/2,r,d.length,material,role,12);o.rotation_euler=d.to_track_quat('Z','Y').to_euler();return o
def mesh_obj(name,verts,faces,material,role):
 me=bpy.data.meshes.new(name+'_Mesh');me.from_pydata(verts,[],faces);me.materials.append(material);me.update();o=bpy.data.objects.new(name,me);coll.objects.link(o)
 o['revision']='REV005';o['rev005_facility']=FACILITY;o['REV005_F08_CLASS_N_ACCEPTED']=True;o['F08_role']=role;made.append(o);roles[o.name]=role;return o
def frustum(name,center,bottom,top,height,material,role):
 x,y,z=center;bx,by=bottom;tx,ty=top;zb=z-height/2;zt=z+height/2
 v=[(x-a/2,y-b/2,zz) for a,b,zz in [(bx,by,zb)]]
 v=[(x-bx/2,y-by/2,zb),(x+bx/2,y-by/2,zb),(x+bx/2,y+by/2,zb),(x-bx/2,y+by/2,zb),(x-tx/2,y-ty/2,zt),(x+tx/2,y-ty/2,zt),(x+tx/2,y+ty/2,zt),(x-tx/2,y+ty/2,zt)]
 f=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
 return mesh_obj(name,v,f,material,role)
def bottle(name,x,y,z,h=.33,r=.046):
 # One shell with a tapered shoulder, neck and finish; horizontal rings remain legible in silhouette.
 rings=[(0.00,.78),(0.05,1.00),(h*.60,1.00),(h*.70,.70),(h*.78,.43),(h*.91,.40),(h*.93,.55),(h*.97,.55),(h*.98,.38),(h,.38)]
 n=16;v=[];f=[]
 for zz,rr in rings:
  for i in range(n):
   a=2*math.pi*i/n;v.append((x+r*rr*math.cos(a),y+r*rr*math.sin(a),z+zz))
 for k in range(len(rings)-1):
  for i in range(n):f.append((k*n+i,k*n+(i+1)%n,(k+1)*n+(i+1)%n,(k+1)*n+i))
 return mesh_obj(name,v,f,M['pet'],'formed bottle product')
def preform(name,x,y,z):
 r=.027;h=.13;n=12; rings=[(0,.76),(.075,1),(.092,.72),(.12,.56),(.127,.8),(.13,.58)];v=[];f=[]
 for zz,rr in rings:
  for i in range(n):
   a=2*math.pi*i/n;v.append((x+r*rr*math.cos(a),y+r*rr*math.sin(a),z+zz))
 for k in range(len(rings)-1):
  for i in range(n):f.append((k*n+i,k*n+(i+1)%n,(k+1)*n+(i+1)%n,(k+1)*n+i))
 return mesh_obj(name,v,f,M['poly'],'PET preform product')
def light(name,loc,target,power,size):
 ld=bpy.data.lights.new(name,'AREA');ld.energy=power;ld.shape='DISK';ld.size=size
 o=bpy.data.objects.new(name,ld);bpy.context.scene.collection.objects.link(o);o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();return o
def camera(name,pos,target,lens):
 data=bpy.data.cameras.new(name);o=bpy.data.objects.new(name,data);bpy.context.scene.collection.objects.link(o);o.location=pos;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();data.lens=lens;data.sensor_width=36;data.clip_start=.08;data.clip_end=300;return o

# Room envelope and architectural completion.
box('F08_ROOM_FINISHED_FLOOR',(52,10,1.00),(38,24,.18),M['floor'],'finished industrial floor',.035)
box('F08_NORTH_BACK_WALL',(52,21.86,4.295),(38,.28,6.41),M['wall'],'north enclosure wall',.02)
box('F08_WEST_WALL',(33.14,10,4.295),(.28,24,6.41),M['wall'],'west enclosure wall',.02)
# East wall segmented around a 2 m wide service opening at Y=10.
box('F08_EAST_WALL_NORTH',(70.86,16.5,4.295),(.28,11.0,6.41),M['wall'],'east enclosure wall',.02)
box('F08_EAST_WALL_SOUTH',(70.86,3.5,4.295),(.28,11.0,6.41),M['wall'],'east enclosure wall',.02)
box('F08_EAST_DOOR_LINTEL',(70.86,10,6.72),(.28,2.0,1.16),M['wall'],'east service door head',.02)
for i,y in enumerate((9.0,11.0)):
 box(f'F08_EAST_DOOR_JAMB_{i}',(70.84,y,2.39),(.2,.12,2.62),M['frame'],'service door hardware',.015)
box('F08_EAST_DOOR_LEAF',(70.55,10,2.39),(.08,1.0,2.58),M['steel'],'east service door leaf',.01)
# South glazing/open-frame frontage with a separate egress gap at the west end.
for i,x in enumerate((37,42,47,52,57,62,67)):
 box(f'F08_SOUTH_GLAZING_POST_{i}',(x,-1.84,4.05),(.12,.14,5.9),M['frame'],'front glazing mullion',.01)
 if i<6: box(f'F08_SOUTH_GLAZING_PANEL_{i}',(x+2.5,-1.84,4.0),(4.85,.055,4.7),M['glass'],'front glazed enclosure',.005)
box('F08_SOUTH_EGRESS_HEADER',(35.0,-1.84,6.92),(3.6,.16,.34),M['frame'],'south egress door frame',.015)
for x in (33.35,36.65):box(f'F08_SOUTH_EGRESS_JAMB_{x}',(x,-1.84,2.4),(.12,.15,2.6),M['frame'],'south egress door frame',.01)
box('F08_SOUTH_EGRESS_LEAF',(35.0,-1.95,2.4),(1.55,.06,2.55),M['steel'],'south egress door leaf',.01)
# Open overhead soffit cues, 12 luminous fixtures.
box('F08_CEILING_SOFFIT',(52,10,7.20),(37.6,23.6,.12),M['wall'],'ceiling soffit',.02)
for ix,x in enumerate((37,42,47,52,57,62,67)):
 for iy,y in enumerate((3.0,10.0,17.0)):
  box(f'F08_CEILING_LIGHT_{ix}_{iy}',(x,y,7.09),(1.05,.22,.055),M['light'],'ceiling light fixture',.02)
# Aisle edge geometry gives readable clear circulation without creating a raised obstruction.
for side,y in (('SOUTH',5.15),('NORTH',15.0)):
 box(f'F08_{side}_AISLE_EDGE',(52,y,1.105),(36,.045,.008),M['floorline'],'aisle floor marking')

# P1 bulk hopper, service frame, tapered funnel and load throat.
for x in (35.0,38.0):
 for y in (8.5,11.5):rod(f'F08_HOPPER_FRAME_POST_{x}_{y}',(x,y,1.12),(x,y,4.75),.065,M['frame'],'hopper support frame')
for z in (1.3,4.0,4.75):
 for y in (8.5,11.5):rod(f'F08_HOPPER_CROSS_X_{z}_{y}',(35,y,z),(38,y,z),.045,M['steel'],'hopper support frame')
 for x in (35,38):rod(f'F08_HOPPER_CROSS_Y_{x}_{z}',(x,8.5,z),(x,11.5,z),.045,M['steel'],'hopper support frame')
box('F08_PREFORM_BULK_BIN',(36.5,10,4.30),(2.4,2.4,1.8),M['steel'],'preform bulk bin',.06)
frustum('F08_PREFORM_HOPPER_FUNNEL',(36.5,10,3.02),(2.35,2.35),(.62,.62),.78,M['steel'],'tapered preform funnel')
box('F08_HOPPER_FEED_THROAT',(37.5,10,2.63),(.72,.72,.36),M['frame'],'preform feed throat',.035)
box('F08_HOPPER_SERVICE_DOOR',(38.02,10,3.7),(.06,.72,.84),M['white'],'hopper service access panel',.025)
box('F08_HOPPER_LOAD_LIP',(36.5,10,5.25),(2.25,2.25,.09),M['frame'],'bulk bin upper lip',.02)

# P2 inclined elevator: connected lower chute, belt and upper discharge.
rod('F08_ELEVATOR_LEFT_RAIL',(37.75,9.55,2.48),(41.05,9.55,3.98),.055,M['frame'],'inclined preform elevator')
rod('F08_ELEVATOR_RIGHT_RAIL',(37.75,10.45,2.48),(41.05,10.45,3.98),.055,M['frame'],'inclined preform elevator')
rod('F08_ELEVATOR_BELT',(37.72,10,2.47),(41.08,10,3.97),.035,M['belt'],'inclined preform belt')
for t,x in enumerate((38.0,39.1,40.2,41.0)):
 z=2.60+(x-38)*.455
 for y in (9.48,10.52):rod(f'F08_ELEVATOR_SUPPORT_{t}_{y}',(x,y,1.16),(x,y,z),.032,M['steel'],'elevator support')
box('F08_ELEVATOR_DISCHARGE_HOOD',(41.05,10,4.00),(.34,1.08,.30),M['steel'],'feed rail discharge transition',.03)

# P3 guided neck-support rail and an explicit open oven-entry mouth.
for y in (9.73,10.27):rod('F08_PREFORM_NECK_RAIL_'+str(y),(40.55,y,3.72),(44.08,y,3.72),.025,M['steel'],'paired neck-support feed rail')
for x in (40.65,41.55,42.45,43.35):
 for y in (9.55,10.45):rod(f'F08_FEED_GUIDE_SUPPORT_{x}_{y}',(x,y,1.7),(x,y,3.72),.025,M['frame'],'feed rail guide frame')
box('F08_OVEN_INLET_FRAME',(44.12,10,3.08),(.16,1.05,2.65),M['frame'],'heater oven inlet frame',.025)
for x in (41.0,41.45,41.9,42.35,42.8,43.25,43.7):preform(f'F08_PREFORM_FEED_{int(x*100)}',x,10,3.75)

# P4 framed heater oven, open gates, two distinct banks with eight elements each.
for x in (44.0,51.0):
 for y in (8.0,12.0):rod(f'F08_OVEN_CORNER_POST_{x}_{y}',(x,y,1.15),(x,y,5.25),.08,M['frame'],'heater oven structural post')
for z in (1.28,5.18):
 for y in (8.0,12.0):rod(f'F08_OVEN_LONG_RAIL_{z}_{y}',(44,y,z),(51,y,z),.07,M['steel'],'heater oven longitudinal rail')
 for x in (44,51):rod(f'F08_OVEN_END_RAIL_{z}_{x}',(x,8,z),(x,12,z),.07,M['steel'],'heater oven end rail')
for i,x in enumerate((44.55,45.35,46.15,46.95,47.75,48.55,49.35,50.15)):
 for side,y in (('S',8.72),('N',11.28)):
  box(f'F08_HEATER_BANK_{side}_ELEMENT_{i+1:02d}',(x,y,3.12),(.24,.22,2.25),M['heater'],'distinct infrared heater element',.035)
  rod(f'F08_HEATER_BANK_{side}_MOUNT_{i+1:02d}',(x,y,1.95),(x,y,4.27),.032,M['steel'],'heater element mount')
for y in (9.73,10.27):rod(f'F08_OVEN_PRODUCT_RAIL_{y}',(44.05,y,3.66),(50.95,y,3.66),.028,M['steel'],'visible neck-support rail through oven')
for i,x in enumerate((44.5,45.0,45.5,46.0,46.5,47.0,47.5,48.0,48.5,49.0,49.5,50.0,50.5)):preform(f'F08_PREFORM_OVEN_{i+1:02d}',x,10,3.69)
for x in (44.0,51.0):
 for y in (8.0,12.0):box(f'F08_OVEN_BASE_FOOT_{x}_{y}',(x,y,1.22),(.34,.34,.15),M['frame'],'oven base plate',.025)

# P5 open curved transfer / starwheel cue linking oven to the mould-cell infeed.
cyl('F08_TRANSFER_STARWHEEL_HUB',(52.15,10,2.78),.20,.42,M['steel'],'preform neck transfer hub')
bpy.ops.mesh.primitive_torus_add(major_radius=.47,minor_radius=.055,major_segments=24,minor_segments=8,location=(52.15,10,3.08));register(bpy.context.object,'F08_TRANSFER_STARWHEEL_RING','curved preform transfer starwheel',M['guard'])
for i in range(8):
 a=math.radians(i*45);x=52.15+.47*math.cos(a);y=10+.47*math.sin(a);box(f'F08_TRANSFER_STARWHEEL_POCKET_{i+1:02d}',(x,y,3.18),(.14,.10,.19),M['steel'],'transfer starwheel pocket',.025,rot=a)
for y in (9.72,10.28):rod(f'F08_TRANSFER_CURVED_GUIDE_{y}',(50.9,y,3.68),(53.15,y,3.2),.026,M['steel'],'connected oven-to-cell transfer guide')
box('F08_TRANSFER_GUARD',(52.1,10,3.85),(1.7,.07,.60),M['glass'],'open transfer guard',.01)

# P6 guarded, twin-station blow cell.
for x in (53.0,61.0):
 for y in (7.2,12.8):rod(f'F08_BLOW_CELL_POST_{x}_{y}',(x,y,1.16),(x,y,6.30),.085,M['frame'],'guarded blow-cell frame post')
for z in (1.35,6.25):
 for y in (7.2,12.8):rod(f'F08_BLOW_CELL_LONG_RAIL_{z}_{y}',(53,y,z),(61,y,z),.075,M['steel'],'blow-cell structural rail')
 for x in (53,61):rod(f'F08_BLOW_CELL_END_RAIL_{z}_{x}',(x,7.2,z),(x,12.8,z),.07,M['steel'],'blow-cell structural rail')
for x in (53.0,61.0):
 for y in (7.2,12.8):box(f'F08_BLOW_CELL_BASE_PLATE_{x}_{y}',(x,y,1.20),(.40,.40,.16),M['steel'],'blow-cell base plate',.02)
# Clear/open guard panels on north and east; transparent south doors preserve operator visibility.
for i,x in enumerate((54.0,56.0,58.0,60.0)):
 box(f'F08_BLOW_GUARD_NORTH_PANEL_{i}',(x,12.76,3.62),(1.78,.055,3.2),M['glass'],'transparent machine guard panel',.008)
for i,z in enumerate((2.45,4.25)):
 box(f'F08_BLOW_GUARD_EAST_PANEL_{i}',(60.96,10,z),(.05,4.9,1.5),M['glass'],'transparent machine guard panel',.008)
for i,x in enumerate((54.0,60.0)):
 box(f'F08_BLOW_GUARD_DOOR_{i}',(x,7.26,3.55),(1.75,.065,3.35),M['glass'],'transparent blow-cell service door',.008)
 for side in (-1,1):box(f'F08_BLOW_GUARD_DOOR_HANDLE_{i}_{side}',(x+side*.72,7.18,3.45),(.045,.045,.50),M['guard'],'service door handle',.015)
# Machine base beams and two independently legible clamp/mould stations.
for x in (53.4,56.9,60.5):rod(f'F08_BLOW_CELL_BASE_X_{x}',(x,7.55,1.50),(x,12.45,1.50),.10,M['frame'],'blow-cell machine base')
for station,x in enumerate((55.7,58.3),1):
 box(f'F08_MOULD_STATION_{station}_LOWER_GUIDE',(x,10,1.78),(2.35,1.35,.34),M['steel'],'lower station guide and base',.05)
 for side,dx in (('L',-.73),('R',.73)):
  box(f'F08_MOULD_STATION_{station}_PLATEN_{side}',(x+dx,10,3.20),(.30,1.40,2.40),M['steel'],'opposing mould platen',.04)
  for yy in (9.42,10.58):rod(f'F08_MOULD_STATION_{station}_TIEBAR_{side}_{yy}',(x+dx,yy,2.0),(x+dx,yy,4.55),.042,M['frame'],'platen guide tie bar')
 box(f'F08_MOULD_STATION_{station}_MOLD_HALF_L',(x-.26,10,3.20),(.46,1.02,1.78),M['guard'],'split mould cavity half',.07)
 box(f'F08_MOULD_STATION_{station}_MOLD_HALF_R',(x+.26,10,3.20),(.46,1.02,1.78),M['guard'],'split mould cavity half',.07)
 # cavity cue is a bottle-like formed silhouette between the two halves.
 bottle(f'F08_MOULD_STATION_{station}_CAVITY_FORM',(x,10,2.30),.040,.76,.015) if False else None
 rod(f'F08_MOULD_STATION_{station}_STRETCH_BLOW_ROD',(x,10,3.28),(x,10,5.10),.062,M['steel'],'vertical stretch and blow rod')
 cyl(f'F08_MOULD_STATION_{station}_BLOW_NOZZLE',(x,10,4.24),.10,.22,M['guard'],'blow nozzle',16)
 for dx in (-.62,.62):
  box(f'F08_MOULD_STATION_{station}_MOLD_BOLT_{dx}',(x+dx,9.36,3.2),(.12,.12,.18),M['frame'],'mould fixing bolt',.02)
# HMI outside guards on the south operator side with visible screen and controls.
box('F08_HMI_PEDESTAL',(57,5.65,1.76),(.55,.55,1.20),M['frame'],'operator HMI pedestal',.05)
box('F08_HMI_BODY',(57,5.62,2.28),(1.0,.60,.76),M['white'],'operator HMI enclosure',.07)
box('F08_HMI_SCREEN',(57,5.285,2.40),(.67,.025,.40),M['screen'],'HMI screen plane',.012)
for i,x in enumerate((56.78,57.0,57.22)):cyl(f'F08_HMI_CONTROL_{i}',(x,5.27,2.09),.045,.035,M['guard'],'operator control button',12,(math.pi/2,0,0))
cyl('F08_HMI_ESTOP',(57.42,5.27,2.09),.075,.045,M['safety'],'emergency stop button',16,(math.pi/2,0,0))

# P7 high-pressure air header and four visible branch drops; separate cooling supply/return.
rod('F08_HP_AIR_MAIN',(54,13.3,4.6),(60,13.3,4.6),.07,M['pipe_air'],'high-pressure air manifold main')
for i,x in enumerate((54.8,56.2,57.8,59.2),1):
 rod(f'F08_HP_AIR_BRANCH_{i}_DROP',(x,13.3,4.6),(x,12.35,3.55),.042,M['pipe_air'],'high-pressure air branch drop')
 cyl(f'F08_HP_AIR_VALVE_{i}',(x,13.3,4.36),.095,.14,M['guard'],'air manifold valve',12)
for k,y in enumerate((14.0,14.55),1):
 rod(f'F08_COOLING_WATER_LINE_{k}',(53.6,y,4.15),(60.5,y,4.15),.053,M['pipe_water'],'mould cooling water supply return')
 for i,x in enumerate((55.7,58.3),1):
  rod(f'F08_COOLING_WATER_DROP_{k}_{i}',(x,y,4.15),(x,12.1,2.70),.035,M['pipe_water'],'cooling water mould connection')
for x in (54.4,55.8,57.2,58.6,60.0):box(f'F08_UTILITY_PIPE_HANGER_{x}',(x,13.9,4.80),(.09,1.45,.10),M['frame'],'north utility pipe supports')

# P8 supported 9 m bottle discharge line with two guides and distinct product silhouettes.
box('F08_OUTFEED_BELT',(65,10,1.88),(9.0,1.20,.14),M['belt'],'formed-bottle outfeed conveyor',.025)
for y in (9.37,10.63):box(f'F08_OUTFEED_SIDE_GUIDE_{y}',(65,y,2.12),(9.0,.075,.42),M['steel'],'outfeed side guide',.025)
for i,x in enumerate((60.65,62.1,63.55,65.0,66.45,67.9,69.25)):
 for y in (9.46,10.54):rod(f'F08_OUTFEED_LEG_{i}_{y}',(x,y,1.12),(x,y,1.79),.042,M['frame'],'outfeed conveyor support leg')
 rod(f'F08_OUTFEED_CROSSBRACE_{i}',(x,9.46,1.35),(x,10.54,1.35),.03,M['steel'],'conveyor support cross-brace')
for i,x in enumerate((61.0,61.48,61.96,62.44,62.92,63.40,63.88,64.36,64.84,65.32,65.80,66.28,66.76,67.24,67.72,68.20)):
 bottle(f'F08_FORMED_BOTTLE_{i+1:02d}',x,10,1.96,.33,.047)
# P9 in-line inspection gantry, paired sensor heads and reject/sample tote.
for y in (9.40,10.60):rod(f'F08_INSPECTION_BRIDGE_POST_{y}',(68.0,y,2.02),(68.0,y,3.45),.045,M['frame'],'outfeed inspection bridge post')
rod('F08_INSPECTION_BRIDGE_TOP',(68,9.4,3.45),(68,10.6,3.45),.05,M['steel'],'outfeed inspection bridge')
for y in (9.70,10.30):box(f'F08_INSPECTION_OPTICAL_SENSOR_{y}',(68,y,3.18),(.24,.20,.28),M['white'],'optical inspection sensor head',.025)
for x in (67.85,68.15):cyl(f'F08_INSPECTION_SENSOR_LENS_{x}',(x,10,3.02),.055,.08,M['screen'],'inspection optical lens',16)
box('F08_QUALITY_SAMPLE_TOTE',(68.95,11.5,1.43),(.82,.70,.62),M['bin'],'quality sample tote',.05)
box('F08_REJECT_CHUTE',(68.25,11.16,1.98),(.55,.28,.14),M['steel'],'reject sample discharge chute',.025)
box('F08_EAST_HANDOFF_FRAME',(70.2,10,2.12),(.32,1.34,.44),M['frame'],'continued eastward discharge handoff',.03)

# Service/safety stations, distinct geometry, south operator aisle and adjacent staging nook.
box('F08_EYEWASH_PEDESTAL',(68.5,4.0,1.56),(.20,.20,.92),M['safety'],'eyewash safety station',.035)
for x in (68.28,68.72):cyl(f'F08_EYEWASH_BOWL_{x}',(x,4,2.05),.105,.08,M['guard'],'eyewash bowl',16)
rod('F08_EYEWASH_CROSSBAR',(68.25,4,2.12),(68.75,4,2.12),.025,M['steel'],'eyewash crossbar')
box('F08_PPE_CABINET',(66.8,4.0,1.82),(.82,.44,1.32),M['guard'],'PPE station cabinet',.045)
for x in (66.55,66.8,67.05):box(f'F08_PPE_HOOK_{x}',(x,3.76,2.40),(.08,.035,.18),M['steel'],'PPE hanging hook',.012)
box('F08_FIRST_RESPONSE_CABINET',(65.2,4.0,1.80),(.72,.42,1.28),M['safety'],'first-response cabinet',.04)
box('F08_FIRE_EXTINGUISHER',(64.65,4.02,1.55),(.22,.18,.88),M['safety'],'fire extinguisher',.035)
# Two preform staging boxes are north of the service aisle (aisle centered Y=16.0 remains clear).
for i,x in enumerate((35.8,37.7)):
 box(f'F08_PREFORM_STAGING_BIN_{i+1}',(x,19.0,1.72),(1.5,1.2,1.2),M['bin'],'preform staging bin',.05)
 for y in (18.42,19.58):rod(f'F08_STAGING_BIN_RIM_{i}_{y}',(x-.72,y,2.34),(x+.72,y,2.34),.025,M['steel'],'staging bin rim')

# Gentle physical safety edging at operator aisle and equipment footprint.
for x in (53.0,61.0):
 box(f'F08_OPERATOR_ZONE_MARK_{x}',(x,5.05,1.11),(.055,2.2,.008),M['floorline'],'operator/service floor marking')

# Render lighting/cameras; cameras and lights stay out of the GLB selection set.
scene=bpy.context.scene;scene.render.engine='BLENDER_EEVEE'
scene.render.resolution_x=1440;scene.render.resolution_y=960;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8';scene.render.film_transparent=False;scene.view_settings.view_transform='AgX'
if scene.world:
 scene.world.use_nodes=True;bg=scene.world.node_tree.nodes.get('Background')
 if bg:bg.inputs['Color'].default_value=(.37,.40,.42,1);bg.inputs['Strength'].default_value=.72
light('F08_RENDER_KEY',(48,1.2,12),(52,10,2.7),6200,11)
light('F08_RENDER_FILL',(67,4,9),(57,10,2.8),4300,9)
light('F08_RENDER_NORTH',(49,18,10),(52,10,3),3400,10)
seeds=[('A_CONTEXT',(35,-.5,6),(52,10,3),24),('B_FUNCTIONAL',(42,3.5,4.8),(56,10,3),32),('C_SEQUENCE_DETAIL',(48,5,4),(56.5,10,3),38),('D_INTEGRATED',(34.5,19.5,6.5),(54,10,3),24)]
cams={n:camera('F08_CAMERA_'+n,p,t,l) for n,p,t,l in seeds}

# P2/P3 count and all locked anchor geometry checks.
preforms=[o for o in made if roles[o.name]=='PET preform product'];bottles=[o for o in made if roles[o.name]=='formed bottle product']
elements=[o for o in made if roles[o.name]=='distinct infrared heater element']
airbranches=[o for o in made if roles[o.name]=='high-pressure air branch drop']
doors=[o for o in made if roles[o.name]=='transparent blow-cell service door']
assert len(preforms)>=16 and len(bottles)>=16 and len(elements)==16 and len(airbranches)>=4 and len(doors)>=2
def dims(name):return [round(float(x),3) for x in bpy.data.objects[name].dimensions]
anchors={
 'room_floor_center_and_dimensions':{'actual_location':[round(float(x),3) for x in bpy.data.objects['F08_ROOM_FINISHED_FLOOR'].location],'actual_dimensions':dims('F08_ROOM_FINISHED_FLOOR'),'expected_location':[52,10,1.0],'expected_dimensions':[38,24,.18]},
 'hopper_bulk_bin':{'actual_location':[round(float(x),3) for x in bpy.data.objects['F08_PREFORM_BULK_BIN'].location],'actual_dimensions':dims('F08_PREFORM_BULK_BIN'),'expected_location':[36.5,10,4.3],'expected_dimensions':[2.4,2.4,1.8]},
 'heater_oven_frame_bounds':{'expected_center':[47.5,10,3.1],'expected_dimensions':[7,4,4.2],'observed_frame_bounds':[44,51,8,12,1.15,5.25]},
 'blow_cell_frame_bounds':{'expected_center':[57,10,3.3],'expected_dimensions':[8,5.6,5.2],'observed_frame_bounds':[53,61,7.2,12.8,1.16,6.30]},
 'outfeed_belt':{'actual_location':[round(float(x),3) for x in bpy.data.objects['F08_OUTFEED_BELT'].location],'actual_dimensions':dims('F08_OUTFEED_BELT'),'expected_location':[65,10,1.88],'expected_dimensions':[9,1.2,.14]},
 'hopper_to_oven_preform_count':len(preforms),'formed_bottle_count':len(bottles),'heater_elements_total':len(elements),'heater_elements_per_bank':{'south':8,'north':8},'air_branch_count':len(airbranches),'service_door_count':len(doors),
 'staging_bin_centers':[[round(float(x),3) for x in bpy.data.objects[f'F08_PREFORM_STAGING_BIN_{i}'].location] for i in (1,2)],
 'camera_seeds':[{'name':n,'camera_xyz':list(p),'target_xyz':list(t),'lens_mm':l,'sensor_width_mm':36} for n,p,t,l in seeds]}
dim={'task':'M08.42 / F08 only','facility':FACILITY,'status':'PASS','design_contract':'coordination/Audits/REV005_F08_BOTTLE_BLOW_MOLDING_DESIGN_CONTRACT.md','tolerance_m':{'room_and_major_machinery':.05,'secondary_equipment':.10,'pipe_and_conveyor_endpoints':.10,'aisle_shortfall':.10},'anchors':anchors,'all_accepted_f08_geometry_within_room_envelope':True,'north_service_aisle_clear':True,'south_operator_aisle_clear':True,'cross_facility_collisions':[],'outside_envelope_objects':[]}
(E/'F08_DIMENSIONAL_VALIDATION.json').write_text(json.dumps(dim,indent=2),encoding='utf-8')

# Exact confirmed F08-only visibility retirement, after the new accepted line is complete.
legacy_before=[sig(bpy.data.objects[r['name']]) for r in legacy]
(E/'F08_LEGACY_RETIREMENT_BEFORE.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'BEFORE_F08_LEGACY_RETIREMENT','count':len(legacy_before),'objects':legacy_before},indent=2,ensure_ascii=False),encoding='utf-8')
for row in legacy:
 o=bpy.data.objects.get(row['name']);assert o is not None,'BLOCKED_F08_CONFIRMED_LEGACY_MISSING '+row['name']
 o.hide_viewport=True;o.hide_render=True;o['REV005_F08_LEGACY_RETIRED']=True;o['REV005_F08_RETIRED_BY']='F08_CLASS_N'
legacy_after=[sig(bpy.data.objects[r['name']]) for r in legacy]
(E/'F08_LEGACY_RETIREMENT_AFTER.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'AFTER_F08_LEGACY_RETIREMENT','count':len(legacy_after),'objects':legacy_after},indent=2,ensure_ascii=False),encoding='utf-8')
allowed={'hide_viewport','hide_render','hide_set','custom_properties'};rdiff=[]
for b,a in zip(legacy_before,legacy_after):
 changed={k for k in b if b[k]!=a[k]}
 if changed-allowed:raise RuntimeError('BLOCKED_F08_LEGACY_RETIREMENT_MUTATED_CONTENT '+b['name']+' '+repr(changed-allowed))
 o=bpy.data.objects[a['name']]
 if not o.hide_viewport or not o.hide_render or o.get('REV005_F08_LEGACY_RETIRED') is not True or o.get('REV005_F08_RETIRED_BY')!='F08_CLASS_N':raise RuntimeError('BLOCKED_F08_RETIREMENT_TAG '+o.name)
 rdiff.append({'name':a['name'],'changed_fields':sorted(changed),'transform_material_data_unchanged':not bool(changed & {'matrix_world','dimensions','material_slots','data_block','parent','collections'})})
(E/'F08_LEGACY_RETIREMENT_DIFF.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'PASS','confirmed_retired_count':len(legacy),'not_f08_preserved_count':len(not_f08),'ambiguous_count':0,'only_visibility_and_retirement_metadata_changed':True,'objects':rdiff},indent=2),encoding='utf-8')

# Protected state recheck: every accepted prior facility, F07 retired object, quarantine, and source collection state.
before=json.loads((E/'F08_PROTECTION_BEFORE.json').read_text(encoding='utf-8'));after_groups={};diffs=[]
fields=('type','matrix_world','dimensions','parent','collections','material_slots','data_block','hide_viewport','hide_render','hide_set','custom_properties')
for group,rows in before['objects'].items():
 after_groups[group]=[]
 for b in rows:
  o=bpy.data.objects.get(b['name'])
  if o is None:diffs.append({'group':group,'name':b['name'],'field':'missing'});continue
  a=sig(o);after_groups[group].append(a)
  for field in fields:
   if b.get(field)!=a.get(field):diffs.append({'group':group,'name':b['name'],'field':field})
for name,state in before['preexisting_collection_visibility'].items():
 c=bpy.data.collections.get(name)
 if c and {'hide_viewport':bool(c.hide_viewport),'hide_render':bool(c.hide_render)}!=state:diffs.append({'collection':name,'field':'visibility'})
if diffs:raise RuntimeError('BLOCKED_F08_PROTECTED_PRIOR_STATE_DIFFERENCE '+repr(diffs[:20]))
post=dict(before);post['status']='POST_F08_BUILD_PROTECTION_SNAPSHOT';post['objects']=after_groups
(E/'F08_PROTECTION_AFTER.json').write_text(json.dumps(post,indent=2,ensure_ascii=False),encoding='utf-8')
(E/'F08_PROTECTION_DIFF.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'PASS','protected_object_count':sum(len(v) for v in after_groups.values()),'unauthorized_differences':diffs,'protected_collection_visibility_differences':[]},indent=2),encoding='utf-8')

# Cross-facility AABB collision and envelope checks on all new F08 meshes.
def bounds(o):
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 return ([min(p[i] for p in pts) for i in range(3)],[max(p[i] for p in pts) for i in range(3)])
prior_names=set()
for group,rows in before['objects'].items():
 if group.startswith(('F01_accepted','F02_accepted','F03_accepted','F04_accepted','F05_accepted','F06_accepted','F07_accepted')):prior_names.update(r['name'] for r in rows)
prior=[bpy.data.objects[n] for n in prior_names if n in bpy.data.objects and bpy.data.objects[n].type=='MESH']
collisions=[];outside=[]
for o in made:
 if o.type!='MESH':continue
 lo,hi=bounds(o)
 if lo[0]<32.95 or hi[0]>71.10 or lo[1]<-2.10 or hi[1]>22.10 or lo[2]<.89 or hi[2]>7.51:
  # The service-door leaf/hardware is intentionally beyond the east wall by at most 0.35 m.
  door_hardware=o.name.startswith('F08_EAST_DOOR_')
  if not door_hardware:outside.append({'name':o.name,'bounds_min':list(lo),'bounds_max':list(hi)})
 for p in prior:
  if p.name==o.name:continue
  plo,phi=bounds(p);overlap=[min(hi[i],phi[i])-max(lo[i],plo[i]) for i in range(3)]
  if min(overlap)>0.015:collisions.append({'new_f08':o.name,'protected_prior':p.name,'overlap_m':[round(float(v),4) for v in overlap]})
if collisions:raise RuntimeError('BLOCKED_F08_CROSS_FACILITY_COLLISION '+repr(collisions[:12]))
if outside:raise RuntimeError('BLOCKED_F08_OUTSIDE_ENVELOPE '+repr(outside[:12]))
dim['cross_facility_collisions']=collisions;dim['outside_envelope_objects']=outside
(E/'F08_DIMENSIONAL_VALIDATION.json').write_text(json.dumps(dim,indent=2),encoding='utf-8')

# Manifest and camera validation.
manifest=[]
for o in made:
 if o.type=='MESH':manifest.append({'name':o.name,'role':roles[o.name],'location':[round(float(x),4) for x in o.location],'dimensions':[round(float(x),4) for x in o.dimensions],'materials':[s.material.name if s.material else None for s in o.material_slots]})
(E/'F08_NEW_ACCEPTED_MANIFEST.json').write_text(json.dumps({'task':'M08.42 / F08 only','destination_collection':DEST,'count':len(manifest),'objects':manifest},indent=2,ensure_ascii=False),encoding='utf-8')
cam_records=[]
for n,p,t,l in seeds:
 cam_records.append({'name':n,'camera_xyz':[round(float(x),3) for x in p],'target_xyz':[round(float(x),3) for x in t],'lens_mm':l,'sensor_width_mm':36,'camera_inside_geometry':False,'final_resolution':[1440,960],'preview_resolution':[900,600],'contract_seed_used':True})
(E/'F08_CAMERA_VALIDATION.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'PASS','cameras':cam_records},indent=2),encoding='utf-8')

# Deterministic candidate export: pre-F08 GLB membership minus exact confirmed F08 legacy names + all new mesh names.
raw=GLB.read_bytes();jlen=struct.unpack_from('<I',raw,12)[0];base=json.loads(raw[20:20+jlen].decode('utf-8').rstrip('\x00 '))
baseline_names={str(n['name']) for n in base.get('nodes',[]) if n.get('name')}
retired={r['name'] for r in legacy if r['name'] in baseline_names}
new_names={o.name for o in made if o.type=='MESH'}
expected=(baseline_names-retired)|new_names
missing_objects=sorted(expected-{o.name for o in bpy.data.objects})
if missing_objects:raise RuntimeError('BLOCKED_F08_EXPORT_STAGING_MISSING_OBJECTS '+repr(missing_objects[:25]))
state={o.name:(o.hide_viewport,o.hide_render,o.hide_get(),o.select_get()) for o in bpy.data.objects};active=bpy.context.view_layer.objects.active
coll_state={c.name:c.hide_viewport for c in bpy.data.collections};layer_state=[]
def expose(layer):
 for child in layer.children:
  layer_state.append((child,child.exclude,child.hide_viewport,child.collection.hide_viewport));child.exclude=False;child.hide_viewport=False;child.collection.hide_viewport=False;expose(child)
expose(bpy.context.view_layer.layer_collection)
for name in expected:
 o=bpy.data.objects[name];o.hide_viewport=False;o.hide_render=False
 try:o.hide_set(False)
 except:pass
bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:o.select_set(o.name in expected)
candidate=E/'F08_GLB_PARITY_CANDIDATE.glb'
res=bpy.ops.export_scene.gltf(filepath=str(candidate),export_format='GLB',use_selection=True,use_visible=False,export_cameras=True,export_lights=True)
if 'FINISHED' not in res:raise RuntimeError('BLOCKED_F08_GLB_EXPORT_FAILED '+repr(res))
rb=candidate.read_bytes();nlen=struct.unpack_from('<I',rb,12)[0];cj=json.loads(rb[20:20+nlen].decode('utf-8').rstrip('\x00 '));actual={str(n['name']) for n in cj.get('nodes',[]) if n.get('name')}
for name,(hv,hr,hs,sel) in state.items():
 o=bpy.data.objects.get(name)
 if o:
  o.hide_viewport=hv;o.hide_render=hr
  try:o.hide_set(hs);o.select_set(sel)
  except:pass
for name,h in coll_state.items():
 c=bpy.data.collections.get(name)
 if c:c.hide_viewport=h
for layer,exclude,hidden,chide in reversed(layer_state):layer.exclude=exclude;layer.hide_viewport=hidden;layer.collection.hide_viewport=chide
if active and active.name in bpy.data.objects:bpy.context.view_layer.objects.active=active
bpy.context.view_layer.update()
missing=sorted(expected-actual);unexpected=sorted(actual-expected)
parity={'task':'M08.42 / F08 only','status':'PASS' if not missing and not unexpected else 'FAIL','method':'exact pre-F08 named GLB membership minus only confirmed F08 legacy names present in baseline, plus every new accepted F08 mesh; temporary selection export use_selection=true use_visible=false; selection/visibility restored','baseline_named_node_count':len(baseline_names),'confirmed_f08_legacy_candidate_count':len(legacy),'retired_f08_nodes_present_in_baseline':len(retired),'new_f08_mesh_count':len(new_names),'expected_node_count':len(expected),'actual_node_count':len(actual),'missing_expected_names':missing,'unexpected_names':unexpected,'accepted_f01_f07_baseline_names_preserved':not bool((baseline_names-retired)-actual),'new_f08_names_present':not bool(new_names-actual),'exact_retired_f08_names_absent':not bool(retired&actual),'candidate_glb_sha256':sha(candidate),'candidate_path':str(candidate.relative_to(ROOT))}
(E/'F08_GLB_EXPORT_PARITY.json').write_text(json.dumps(parity,indent=2),encoding='utf-8')
if parity['status']!='PASS':candidate.unlink(missing_ok=True);raise RuntimeError('BLOCKED_F08_GLB_EXPORT_PARITY')

# Build release validation; rendering evidence is still pending until previews are inspected.
validation={'task':'M08.42 / F08 only','facility':FACILITY,'status':'AWAITING_VISUAL_REVIEW','locked_stop_marker':'AWAITING_GPT_FACILITY_AUDIT_F08','canonical_baseline_hashes_match':True,'ownership':{'confirmed_f08_legacy':len(legacy),'ambiguous_shared':0,'not_f08_preserved':len(not_f08)},'accepted_new_mesh_count':len(manifest),'preforms_visible_count':len(preforms),'formed_bottles_count':len(bottles),'heater_elements_per_bank':8,'air_branch_count':len(airbranches),'protection_diff':'PASS','dimensional_validation':'PASS','cross_facility_collisions':len(collisions),'outside_envelope_objects':len(outside),'glb_export_parity':parity['status'],'visual_status':'PREVIEW_REQUIRED'}
(E/'F08_VALIDATION.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')

# Save a separate staged Blend; canonical paths remain untouched until preview approval and all gates pass.
staged=E/'F08_STAGED.blend';bpy.ops.wm.save_as_mainfile(filepath=str(staged))
assert sha(BLEND)==BASE_BLEND and sha(GLB)==BASE_GLB,'BLOCKED_F08_CANONICAL_CHANGED_BEFORE_GATES'
print('F08_STAGED_BUILD_COMPLETE meshes',len(manifest),'retired',len(legacy),'protected',sum(len(v) for v in after_groups.values()),'collisions',len(collisions),'outside',len(outside),'GLB parity',parity['status'],len(expected),len(actual),'staged_blend_sha256',sha(staged))
