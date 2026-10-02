import bpy, math, json, hashlib, shutil, struct, os
from pathlib import Path
from mathutils import Vector

ROOT = Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
EVIDENCE = ROOT / 'output/rev005-facility-gated/F07_admin_hq_rd_qc'
BLEND = ROOT / '3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend'
GLB = ROOT / '3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
DEST = 'REV005_FG_F07_ADMIN_HQ_RD_QC_ACCEPTED_CLASS_N'
FACILITY = 'Administration / HQ / R&D / QC'

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest().upper()

baseline=json.loads((EVIDENCE/'F07_BASELINE_HASHES.json').read_text(encoding='utf-8'))
if sha(BLEND)!=baseline['expected']['blend_sha256'] or sha(GLB)!=baseline['expected']['glb_sha256']:
    raise RuntimeError('BLOCKED_F07_CANONICAL_BASELINE_MISMATCH')
if bpy.data.collections.get(DEST): raise RuntimeError('F07 destination collection already exists in source')
coll=bpy.data.collections.new(DEST); bpy.context.scene.collection.children.link(coll)
created=[]; role_by_name={}

def material(name,color,metal=0.0,rough=.5,alpha=1.0,emission=None):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=(*color,alpha); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    if p:
        p.inputs['Base Color'].default_value=(*color,alpha); p.inputs['Metallic'].default_value=metal
        p.inputs['Roughness'].default_value=rough; p.inputs['Alpha'].default_value=alpha
        if emission and 'Emission Color' in p.inputs:
            p.inputs['Emission Color'].default_value=(*emission,1)
            p.inputs['Emission Strength'].default_value=2.0
    if alpha<1:
        try: m.surface_render_method='DITHERED'
        except: pass
    return m

M={
 'floor':material('F07_N_Floor_Light_Gray',(.60,.63,.64),rough=.82),
 'wall':material('F07_N_Off_White',(.82,.84,.82),rough=.82),
 'glass':material('F07_N_Clear_Glazing',(.48,.72,.78),.08,.18,.16),
 'frame':material('F07_N_Anodized_Aluminum',(.19,.24,.27),.72,.28),
 'wood':material('F07_N_Light_Oak',(.60,.39,.21),rough=.48),
 'oak':material('F07_N_Oak_Light_Edge',(.78,.60,.37),rough=.48),
 'steel':material('F07_N_Brushed_Stainless',(.58,.63,.65),.82,.29),
 'white':material('F07_N_Lab_Cabinet_White',(.84,.86,.85),rough=.36),
 'cabdoor':material('F07_N_Cabinet_Front_Light_Gray',(.68,.72,.73),rough=.42),
 'dark':material('F07_N_Graphite',(.055,.073,.085),.2,.32),
 'screen':material('F07_N_Monitor_Glass',(.025,.06,.075),.15,.18),
 'teal':material('F07_N_Safety_Teal',(.04,.40,.43),rough=.4),
 'yellow':material('F07_N_Safety_Yellow',(.95,.67,.07),rough=.48),
 'red':material('F07_N_Safety_Red',(.72,.12,.09),rough=.46),
 'blue':material('F07_N_Instrument_Blue',(.12,.34,.48),.12,.35),
 'light':material('F07_N_Light_Diffuser',(.95,.97,1),rough=.24,emission=(.9,.94,1)),
 'ceiling':material('F07_N_Ceiling_Finish',(.78,.80,.81),rough=.82,emission=(.34,.36,.38)),
}

def link(mesh,name,loc,rot=(0,0,0),mat=None,role='detail'):
    o=bpy.data.objects.new(name,mesh); coll.objects.link(o); o.location=loc; o.rotation_euler=rot
    if mat and len(o.data.materials)==0: o.data.materials.append(mat)
    o['revision']='REV005'; o['rev005_facility']=FACILITY
    o['REV005_F07_CLASS_N_ACCEPTED']=True; o['F07_role']=role
    created.append(o); role_by_name[o.name]=role
    return o

def box(name,loc,dims,mat,role='detail',bevel=0,rot=0):
    x,y,z=dims
    v=[(-x/2,-y/2,-z/2),(x/2,-y/2,-z/2),(x/2,y/2,-z/2),(-x/2,y/2,-z/2),
       (-x/2,-y/2,z/2),(x/2,-y/2,z/2),(x/2,y/2,z/2),(-x/2,y/2,z/2)]
    f=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
    me=bpy.data.meshes.new(name+'_Mesh'); me.from_pydata(v,[],f); me.materials.append(mat); me.update()
    o=link(me,name,loc,(0,0,rot),mat,role); o.dimensions=(x,y,z)
    if bevel:
        b=o.modifiers.new('Soft_Hard_Surface_Edges','BEVEL'); b.width=bevel; b.segments=2
        o.modifiers.new('Weighted_Corner_Normals','WEIGHTED_NORMAL')
    return o

def cylinder(name,loc,r,depth,mat,role='detail',n=20):
    v=[]
    for z in (-depth/2,depth/2):
        for i in range(n):
            a=2*math.pi*i/n; v.append((r*math.cos(a),r*math.sin(a),z))
    f=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]
    for i in range(n):
        j=(i+1)%n; f.append((i,j,n+j,n+i))
    me=bpy.data.meshes.new(name+'_Mesh'); me.from_pydata(v,[],f); me.materials.append(mat); me.update()
    return link(me,name,loc,mat=mat,role=role)

def rod(name,a,b,r,mat,role='detail'):
    av=Vector(a); bv=Vector(b); d=bv-av
    o=cylinder(name,(av+bv)/2,r,d.length,mat,role,12)
    o.rotation_euler=d.to_track_quat('Z','Y').to_euler(); return o

def chair(prefix,x,y,task=False,rot=0):
    z=1.48 if task else 1.43
    box(prefix+'_SEAT',(x,y,z),(.54,.52,.12),M['dark'],'task chair' if task else 'visitor chair',.05,rot)
    box(prefix+'_BACK',(x,y+.225,z+.43),(.52,.095,.68),M['dark'],'chair back',.04,rot)
    cylinder(prefix+'_LIFT',(x,y,1.24),.055,.34,M['steel'],'chair support',16)
    cylinder(prefix+'_BASE',(x,y,1.075),.36,.07,M['dark'],'chair base',20)
    for i in range(5):
        a=2*math.pi*i/5
        rod(prefix+f'_SPIDER_{i}',(x,y,1.10),(x+.32*math.cos(a),y+.32*math.sin(a),1.10),.025,M['steel'],'chair base spoke')
        cylinder(prefix+f'_CASTER_{i}',(x+.32*math.cos(a),y+.32*math.sin(a),1.055),.055,.08,M['dark'],'chair caster',12)

def desk(prefix,x,y):
    box(prefix+'_TOP',(x,y,1.81),(1.60,.75,.06),M['oak'],'office desk top',.025)
    for sx in (-.62,.62):
        box(prefix+f'_PEDESTAL_{sx:+.2f}',(x+sx,y,1.44),(.30,.64,.68),M['white'],'office desk pedestal',.035)
        for j in range(3):
            box(prefix+f'_DRAWER_{sx:+.2f}_{j}',(x+sx,y-.325,1.27+j*.18),(.24,.025,.12),M['steel'],'desk drawer face',.01)
        box(prefix+f'_FOOT_{sx:+.2f}',(x+sx,y,1.12),(.42,.70,.05),M['dark'],'desk foot',.015)
    box(prefix+'_MONITOR_STAND',(x,y+.21,2.00),(.08,.09,.30),M['steel'],'monitor support',.015)
    box(prefix+'_MONITOR',(x,y+.23,2.35),(.88,.075,.50),M['dark'],'monitor housing',.035)
    box(prefix+'_SCREEN',(x,y+.187,2.35),(.80,.014,.42),M['screen'],'monitor screen',.008)
    box(prefix+'_KEYBOARD',(x,y-.12,1.858),(.45,.16,.025),M['dark'],'keyboard',.012)
    box(prefix+'_MOUSE',(x+.29,y-.12,1.86),(.09,.13,.03),M['steel'],'mouse',.012)

def pane(name,center,dims,role='glazing'):
    return box(name,center,dims,M['glass'],role,.01)
def wallx(name,x,y0,y1,t=.18,z0=1.09,z1=6.8):
    return box(name,(x,(y0+y1)/2,(z0+z1)/2),(t,y1-y0,z1-z0),M['wall'],'enclosure',.025)
def wally(name,y,x0,x1,t=.18,z0=1.09,z1=6.8):
    return box(name,((x0+x1)/2,y,(z0+z1)/2),(x1-x0,t,z1-z0),M['wall'],'enclosure',.025)

# Locked 46 x 28 m envelope and glazed front facade.
box('F07_ROOM_FLOOR',(-58,-64,1.0),(46,28,.18),M['floor'],'floor slab',.04)
wallx('F07_WEST_WALL',-80.91,-78,-50)
wallx('F07_EAST_WALL',-35.09,-78,-50)
wally('F07_NORTH_BACK_WALL',-50.09,-81,-35)
front=-77.91
for i,(a,b) in enumerate([(-81,-76.2),(-73.8,-35)]):
    pane(f'F07_FRONT_GLAZING_{i}',((a+b)/2,front,(1.09+6.58)/2),(b-a,.12,5.49))
for x in (-80.7,-77.5,-74,-70,-66,-62,-58,-54,-50,-46,-42,-38,-35.3):
    if -76.2<x<-73.8: continue
    box(f'F07_FRONT_MULLION_{x:.1f}',(x,front,3.83),(.065,.16,5.48),M['frame'],'glazing mullion',.012)
box('F07_FRONT_SILL',(-58,front,1.14),(46,.22,.10),M['frame'],'glazing sill',.02)
box('F07_FRONT_HEAD',(-58,front,6.52),(46,.22,.12),M['frame'],'glazing head',.02)
# Actual 2.40 x 2.60 m double-door clear opening, with leaves swung inward.
for x in (-76.2,-73.8):
    box(f'F07_ENTRY_JAMB_{x}',(x,-77.90,2.40),(.10,.22,2.62),M['frame'],'main double entry jamb',.015)
box('F07_ENTRY_HEADER',(-75,-77.9,3.75),(2.50,.22,.12),M['frame'],'main double entry header',.015)
box('F07_ENTRY_THRESHOLD',(-75,-77.60,1.13),(2.4,.42,.08),M['steel'],'entry threshold',.012)
for side,hinge,angle in [('L',-76.2,math.radians(72)),('R',-73.8,math.radians(-72))]:
    leaf=box('F07_ENTRY_DOOR_'+side,(hinge+(.20 if side=='L' else -.20),-77.25,2.39),(1.12,.045,2.56),M['glass'],'open double door leaf',.015,angle)
    box('F07_ENTRY_DOOR_PULL_'+side,(leaf.location.x,leaf.location.y-.04,2.30),(.035,.055,.45),M['steel'],'door pull',.015,angle)
# Complete the ceiling enclosure at Z 6.60–6.80; fixtures sit below its underside.
box('F07_CEILING_FINISH',(-58,-64,6.70),(46,28,.20),M['ceiling'],'finished ceiling soffit',.025)

# Z1 reception: supported desk, raised transaction ledge, operator and visitor seating.
box('F07_RECEPTION_DESK_TOP',(-74,-72.5,1.82),(5.5,1.0,.10),M['wood'],'reception desk top',.045)
for x in (-76.2,-71.8):
    box(f'F07_RECEPTION_PEDESTAL_{x}',(x,-72.5,1.43),(.52,.76,.68),M['oak'],'reception pedestal',.05)
for x in (-76.35,-71.65):
    box(f'F07_RECEPTION_SUPPORT_{x}',(x,-72.5,1.43),(.12,.82,.68),M['frame'],'reception support',.025)
box('F07_RECEPTION_TRANSACTION_LEDGE',(-74,-72.08,1.995),(3.10,.25,.25),M['oak'],'raised transaction ledge',.035)
chair('F07_RECEPTION_OPERATOR',-74,-71.18,task=True)
for i,(x,y) in enumerate([(-77.4,-74.55),(-76.1,-74.55),(-73,-74.55),(-71.7,-74.55)]):
    chair(f'F07_RECEPTION_VISITOR_{i}',x,y,rot=math.pi)
for x in (-79.4,-68.8):
    box(f'F07_RECEPTION_PLANTER_{x}',(x,-70.1,1.28),(.48,.48,.38),M['white'],'waiting edge',.05)
    for i in range(3): cylinder(f'F07_RECEPTION_PLANT_{x}_{i}',(x+(i-1)*.12,-70.1,1.73),.065,.62,M['teal'],'plant',12)

# Z2 eight complete, supported office workstations.
for row,y in enumerate((-65.2,-61.3)):
    for col,x in enumerate((-69,-65,-61,-57)):
        i=row*4+col; desk(f'F07_OFFICE_STATION_{i:02d}',x,y)
        chair(f'F07_OFFICE_TASK_CHAIR_{i:02d}',x,y-.93,task=True)
        box(f'F07_OFFICE_TRAY_{i:02d}',(x-.48,y-.18,1.52),(.24,.18,.035),M['white'],'office accessory',.01)

# Z3 meeting room: transparent partitions, actual 1.2 m openings, complete table and ten chairs.
for i,(a,b) in enumerate([(-65,-54.8),(-53.6,-53)]):
    pane(f'F07_MEETING_SOUTH_GLASS_{i}',((a+b)/2,-58,3.50),(b-a,.08,4.80),'meeting partition')
for x in (-65,-53):
    for i,(a,b) in enumerate([(-58,-55.5),(-54.3,-50.18)]):
        pane(f'F07_MEETING_SIDE_GLASS_{x}_{i}',(x,(a+b)/2,3.50),(.08,b-a,4.80),'meeting partition')
for x in (-65,-60.5,-56,-53):
    box(f'F07_MEETING_FRAME_S_{x}',(x,-58,3.50),(.045,.10,4.8),M['frame'],'meeting partition frame',.008)
for y in (-57.8,-54.9,-52,-50.25):
    for x in (-65,-53): box(f'F07_MEETING_FRAME_{x}_{y}',(x,y,3.50),(.10,.045,4.8),M['frame'],'meeting partition frame',.008)
box('F07_MEETING_TABLE_TOP',(-59,-54.5,1.815),(4.8,1.8,.07),M['wood'],'meeting table top',.04)
for x in (-60.8,-59,-57.2): box(f'F07_MEETING_TABLE_SUPPORT_{x}',(x,-54.5,1.45),(.20,1.30,.66),M['frame'],'meeting table support',.025)
for side,y in [('S',-56.05),('N',-52.95)]:
    for i,x in enumerate((-60.8,-59.9,-59,-58.1,-57.2)):
        chair(f'F07_MEETING_CHAIR_{side}_{i}',x,y,rot=0 if side=='S' else math.pi)
box('F07_MEETING_DISPLAY_FRAME',(-59,-50.45,3.40),(3.34,.20,1.94),M['frame'],'meeting display frame',.035)
box('F07_MEETING_DISPLAY_SCREEN',(-59,-50.32,3.40),(3.2,.035,1.8),M['screen'],'meeting display screen',.015)

# Z4 partition X=-52.00 with two 1.20 m glazed door openings.
px=-52.0
for i,(a,b) in enumerate([(-76,-72.6),(-71.4,-61.6),(-60.4,-57)]):
    pane(f'F07_LAB_PARTITION_GLASS_{i}',(px,(a+b)/2,(1.09+6.50)/2),(.12,b-a,5.41),'office lab partition')
for y in (-72,-61):
    for side,dy in [('A',-.66),('B',.66)]:
        box(f'F07_LAB_DOOR_JAMB_{side}_{y}',(px,y+dy,2.22),(.16,.10,2.26),M['frame'],'lab door frame',.012)
    box(f'F07_LAB_DOOR_HEAD_{y}',(px,y,3.38),(.16,1.42,.12),M['frame'],'lab door frame',.012)
    box(f'F07_LAB_DOOR_LEAF_{y}',(px+.42,y+.40,2.22),(.045,.80,2.20),M['glass'],'open lab door leaf',.012,math.radians(32))

def labbench(prefix,x,y,length=4.0,depth=.8):
    # Rotate the locked 4.0 x .8 x .9 bench footprint so its length runs along Y; this keeps >=1.2 m clear aisles.
    box(prefix+'_WORKTOP',(x,y,1.94),(depth,length,.10),M['steel'],'stainless lab worktop',.035)
    box(prefix+'_CABINET',(x,y,1.50),(depth-.08,length-.16,.76),M['white'],'supported lab cabinet',.025)
    for side in (-1,1):
        for j,offset in enumerate((-1.45,-.50,.50,1.45)):
            fx=x+side*(depth/2+.012)
            box(f'{prefix}_DOOR_{side}_{j}',(fx,y+offset,1.50),(.025,.78,.58),M['cabdoor'],'cabinet door',.012)
            box(f'{prefix}_HANDLE_{side}_{j}',(x+side*(depth/2+.031),y+offset+.25,1.50),(.025,.035,.16),M['steel'],'cabinet pull',.012)
    box(prefix+'_TOEKICK',(x,y,1.15),(depth-.03,length-.10,.10),M['dark'],'bench toe kick',.012)
    box(prefix+'_BACKSPLASH',(x,y+length/2-.04,2.10),(depth,.08,.32),M['wall'],'bench backsplash',.015)
    for sx in (-1,1):
        for sy in (-1,1): cylinder(f'{prefix}_LEG_{sx}_{sy}',(x+sx*(depth/2-.07),y+sy*(length/2-.10),1.54),.035,.70,M['steel'],'bench frame support',12)

for i,(x,y) in enumerate([(-48,-72),(-43,-72),(-48,-66),(-43,-66)]):
    labbench(f'F07_LAB_BENCH_{i+1}',x,y)
# Sample-prep island with storage below the full 5.0 x 1.2 m top.
box('F07_SAMPLE_ISLAND_TOP',(-44.5,-60.3,1.96),(1.2,5.0,.10),M['steel'],'sample prep island top',.035)
box('F07_SAMPLE_ISLAND_CABINET',(-44.5,-60.3,1.50),(1.04,4.78,.78),M['white'],'sample prep island storage',.03)
for i,y in enumerate((-62.3,-61.3,-60.3,-59.3,-58.3)):
    for x in (-45.02,-43.98): box(f'F07_ISLAND_DOOR_{i}_{x}',(x,y,1.52),(.018,.88,.58),M['wall'],'sample island cabinet door',.012)
    box(f'F07_ISLAND_DRAWER_{i}',(-44.5,y,1.89),(1,.12,.08),M['steel'],'sample island drawer',.01)
# Sink/service bench with visible basin, gooseneck faucet and backsplash.
box('F07_SINK_BENCH_TOP',(-38.5,-72,1.96),(2.2,.8,.10),M['steel'],'sink stainless worktop',.03)
box('F07_SINK_BASE',(-38.5,-72,1.50),(2.05,.70,.78),M['white'],'sink cabinet support',.03)
box('F07_SINK_BASIN',(-38.5,-72,2.02),(.76,.49,.10),M['dark'],'visible wash basin',.035)
box('F07_SINK_BASIN_INNER',(-38.5,-72,2.075),(.62,.36,.025),M['steel'],'sink basin interior',.02)
rod('F07_SINK_FAUCET_STEM',(-38.5,-71.82,2.06),(-38.5,-71.82,2.44),.035,M['steel'],'gooseneck faucet')
rod('F07_SINK_FAUCET_SPOUT',(-38.5,-71.82,2.44),(-38.5,-72.0,2.36),.032,M['steel'],'gooseneck faucet')
box('F07_SINK_SPLASHBACK',(-38.5,-71.54,2.30),(2.2,.08,.60),M['wall'],'service splashback',.018)
# Five east-side storage bays (1.20 m nominal width, 0.45 m depth, 2.20 m tall).
for i,y in enumerate((-63.8,-62.6,-61.4,-60.2,-59.0)):
    x=-36.25
    for z in (1.35,1.85,2.35,2.85,3.35):
        box(f'F07_STORAGE_{i}_SHELF_{z}',(x,y,z),(1.15,.43,.045),M['steel'],'QC storage shelf',.01)
    for dx in (-.53,.53): box(f'F07_STORAGE_{i}_UPRIGHT_{dx}',(x+dx,y,2.20),(.055,.43,2.2),M['frame'],'QC storage upright',.012)
    for z in (1.62,2.12,2.62,3.12):
        box(f'F07_STORAGE_{i}_SAMPLE_BIN_{z}',(x,y,z),(.72,.28,.20),M['white'],'sample storage bin',.025)

# Six mechanically distinct, label-blind QC instruments distributed around the lab.
# Analytical balance with glass draft shield.
box('F07_QC_BALANCE_BASE',(-48,-73,2.07),(.55,.50,.16),M['blue'],'analytical balance base',.03)
box('F07_QC_BALANCE_PAN',(-48,-73,2.17),(.23,.23,.025),M['steel'],'analytical balance pan',.012)
for x in (-48.22,-47.78):
    for y in (-73.18,-72.82):
        box(f'F07_QC_BALANCE_SHIELD_{x}_{y}',(x,y,2.43),(.025,.025,.48),M['glass'],'balance draft shield',.006)
        rod(f'F07_QC_BALANCE_FRAME_{x}_{y}',(x,y,2.19),(x,y,2.68),.014,M['teal'],'balance draft shield frame')
box('F07_QC_BALANCE_SHIELD_TOP',(-48,-73,2.68),(.50,.42,.025),M['glass'],'balance draft shield',.006)
box('F07_QC_BALANCE_DISPLAY',(-48,-72.70,2.11),(.24,.08,.10),M['dark'],'balance display',.012)
# pH / conductivity meter with upright arm and suspended probe.
box('F07_QC_PH_BASE',(-48.08,-71.55,2.07),(.35,.30,.14),M['teal'],'pH conductivity base',.03)
box('F07_QC_PH_DISPLAY',(-48.08,-71.43,2.20),(.26,.07,.17),M['dark'],'pH display',.018)
rod('F07_QC_PH_PROBE_ARM',(-48.28,-71.50,2.19),(-48.28,-71.50,2.84),.025,M['steel'],'pH probe arm')
rod('F07_QC_PH_PROBE',(-48.28,-71.50,2.84),(-48.28,-71.50,2.30),.018,M['teal'],'pH electrode probe')
box('F07_QC_PH_BEAKER',(-47.86,-71.55,2.16),(.12,.12,.20),M['glass'],'pH sample beaker',.015)
# Rotational viscometer with vertical spindle column.
box('F07_QC_VISCO_BASE',(-48,-70.4,2.07),(.45,.40,.16),M['dark'],'viscometer base',.03)
box('F07_QC_VISCO_COLUMN_BODY',(-48,-70.4,2.38),(.22,.20,.44),M['dark'],'viscometer body',.025)
rod('F07_QC_VISCO_COLUMN',(-48,-70.4,2.48),(-48,-70.4,3.12),.045,M['steel'],'viscometer spindle column')
rod('F07_QC_VISCO_CROSSARM',(-48.24,-70.4,2.98),(-47.76,-70.4,2.98),.024,M['teal'],'viscometer crossarm')
rod('F07_QC_VISCO_SPINDLE',(-48,-70.4,2.72),(-48,-70.4,2.21),.018,M['yellow'],'viscometer spindle')
box('F07_QC_VISCO_SAMPLE_CUP',(-48,-70.4,2.28),(.22,.22,.22),M['glass'],'viscometer sample cup',.02)
# Spectrophotometer/colorimeter with sample compartment cue.
box('F07_QC_SPECTRO_BODY',(-43,-67,2.23),(.55,.45,.35),M['blue'],'spectrophotometer housing',.04)
box('F07_QC_SPECTRO_LID',(-43,-67,2.42),(.38,.34,.06),M['dark'],'spectrophotometer sample lid',.02)
box('F07_QC_SPECTRO_SAMPLE_DOOR',(-42.70,-66.90,2.28),(.045,.18,.16),M['blue'],'spectrophotometer sample compartment',.012)
box('F07_QC_SPECTRO_DISPLAY',(-43.16,-66.77,2.34),(.18,.025,.10),M['dark'],'spectrophotometer display',.008)
# Stability/incubator cabinet with door, viewing window and handle.
box('F07_QC_INCUBATOR',(-37.55,-67,1.92),(.80,.70,1.60),M['white'],'stability incubator cabinet',.045)
box('F07_QC_INCUBATOR_DOOR',(-37.55,-66.635,1.92),(.67,.045,1.42),M['teal'],'incubator door',.025)
box('F07_QC_INCUBATOR_WINDOW',(-37.55,-66.604,2.10),(.42,.02,.78),M['glass'],'incubator viewing window',.015)
box('F07_QC_INCUBATOR_HANDLE',(-37.20,-66.57,1.95),(.035,.05,.35),M['dark'],'incubator handle',.01)
# Compact centrifuge/mixer silhouette.
cylinder('F07_QC_CENTRIFUGE_BASE',(-43,-61.7,2.18),.225,.20,M['white'],'compact centrifuge',24)
cylinder('F07_QC_CENTRIFUGE_LID',(-43,-61.7,2.31),.18,.08,M['yellow'],'centrifuge lid',24)
cylinder('F07_QC_CENTRIFUGE_CAP',(-43,-61.7,2.38),.07,.08,M['dark'],'centrifuge lid handle',16)

# Distinct safety/service geometry at the locked points.
cylinder('F07_SAFETY_EYEWASH_POST',(-37.5,-74.5,1.55),.035,.86,M['teal'],'eyewash station',14)
box('F07_SAFETY_EYEWASH_FOOT',(-37.5,-74.5,1.13),(.38,.30,.08),M['steel'],'eyewash base',.02)
rod('F07_SAFETY_EYEWASH_ARM',(-37.5,-74.5,1.92),(-37.5,-74.16,1.92),.026,M['teal'],'eyewash arm')
for i,x in enumerate((-37.62,-37.38)):
    cylinder(f'F07_SAFETY_EYEWASH_BOWL_{i}',(x,-74.16,1.92),.105,.04,M['yellow'],'eyewash bowl',16)
box('F07_SAFETY_PPE_CABINET',(-37.5,-73,1.75),(.62,.30,1.30),M['yellow'],'PPE station cabinet',.04)
box('F07_SAFETY_PPE_DOOR',(-37.5,-72.83,1.75),(.50,.035,1.12),M['wall'],'PPE station front',.022)
for i,z in enumerate((1.42,1.68,1.94,2.20)):
    box(f'F07_SAFETY_PPE_KIT_{i}',(-37.5,-72.79,z),(.28,.04,.13),M['teal'],'visible PPE kit',.018)
box('F07_SAFETY_SPILL_CABINET',(-37.5,-70.8,1.78),(.78,.40,1.38),M['red'],'spill first response cabinet',.045)
box('F07_SAFETY_SPILL_DOOR',(-37.5,-70.58,1.78),(.66,.035,1.18),M['white'],'response cabinet door',.025)
box('F07_SAFETY_SPILL_HANDLE',(-37.23,-70.54,1.80),(.035,.045,.24),M['steel'],'cabinet handle',.01)

# Low glazed reception edge preserves sightlines and defines waiting/office transition.
for x in (-68,-66.7): box(f'F07_ARRIVAL_LOW_PARTITION_{x}',(x,-70.6,1.65),(.08,4,1.05),M['glass'],'arrival office partition',.012)
# Twelve ceiling fixtures plus four lab task strips.
light_positions=[(x,y) for y in (-75,-69.5,-64,-58.5) for x in (-75.5,-68.5,-61.5)]
for i,(x,y) in enumerate(light_positions):
    box(f'F07_CEILING_FIXTURE_{i:02d}_HOUSING',(x,y,6.48),(1.20,.30,.10),M['frame'],'ceiling fixture housing',.025)
    box(f'F07_CEILING_FIXTURE_{i:02d}_DIFFUSER',(x,y,6.415),(1.12,.25,.035),M['light'],'ceiling light diffuser',.02)
for i,(x,y) in enumerate([(-48,-72),(-43,-72),(-48,-66),(-43,-66)]):
    box(f'F07_LAB_TASK_LIGHT_{i}',(x,y,5.85),(.55,2,.06),M['light'],'lab task light strip',.018)

def area_light(name,loc,target,power,size,color=(1,.94,.84)):
    d=bpy.data.lights.new(name,'AREA'); d.energy=power; d.shape='DISK'; d.size=size; d.color=color
    d.use_shadow=False
    o=bpy.data.objects.new(name,d); bpy.context.scene.collection.objects.link(o); o.location=loc
    o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()
area_light('F07_RENDER_KEY',(-62,-68,6.25),(-58,-64,1.6),5200,16)
area_light('F07_RENDER_FILL',(-42,-61,6.25),(-58,-64,2),4600,14,(.84,.92,1))
area_light('F07_RENDER_RECEPTION',(-75,-76,6.20),(-73,-71,1.6),2400,10)
area_light('F07_RENDER_LAB',(-42,-73,6.25),(-43,-66,1.6),3200,10,(.92,.98,1))

seeds=[('A_CONTEXT',(-78,-75,5.2),(-57,-64,2.6),20),
       ('B_FUNCTIONAL',(-69,-67,4.4),(-45,-66,2.4),32),
       ('C_LAB_DETAIL',(-49.5,-74.5,3.8),(-45,-69,2.5),40),
       ('D_INTEGRATED',(-77,-71,5.8),(-52,-63.5,2.7),24)]
scene=bpy.context.scene; scene.render.engine='BLENDER_EEVEE'
scene.render.resolution_x=1440;scene.render.resolution_y=960;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.image_settings.color_depth='8'
scene.render.film_transparent=False;scene.view_settings.view_transform='AgX'
if scene.world:
    scene.world.use_nodes=True
    bg=scene.world.node_tree.nodes.get('Background')
    if bg: bg.inputs['Color'].default_value=(.42,.46,.49,1);bg.inputs['Strength'].default_value=.8

inventory=json.loads((EVIDENCE/'F07_LEGACY_ADMIN_INVENTORY.json').read_text(encoding='utf-8'))
legacy=[r for r in inventory['candidates'] if r['ownership_classification']=='CONFIRMED_F07_LEGACY']
if len(legacy)!=446 or inventory['classification_counts']['AMBIGUOUS_SHARED']!=0:
    raise RuntimeError('F07 ownership gate changed')

def cv(v):
    if hasattr(v,'to_list'): return v.to_list()
    if isinstance(v,(str,int,float,bool)) or v is None:return v
    try:return [cv(x) for x in v]
    except:return str(v)
def signature(o):
    return {'name':o.name,'type':o.type,'matrix_world':[[round(float(o.matrix_world[r][c]),9) for c in range(4)] for r in range(4)],
      'dimensions':[round(float(x),9) for x in o.dimensions],'parent':o.parent.name if o.parent else None,
      'collections':sorted(c.name for c in o.users_collection),'material_slots':[s.material.name if s.material else None for s in o.material_slots],
      'data_block':o.data.name if o.data else None,'hide_viewport':bool(o.hide_viewport),'hide_render':bool(o.hide_render),
      'custom_properties':{k:cv(o[k]) for k in o.keys()}}

legacy_before=[]
for row in legacy:
    o=bpy.data.objects.get(row['name'])
    if o is None: raise RuntimeError('F07 legacy object missing: '+row['name'])
    legacy_before.append(signature(o))
(EVIDENCE/'F07_LEGACY_RETIREMENT_BEFORE.json').write_text(json.dumps({'task':'M08.41 / F07 only','status':'BEFORE_F07_LEGACY_RETIREMENT','count':len(legacy_before),'objects':legacy_before},indent=2,ensure_ascii=False),encoding='utf-8')
for row in legacy:
    o=bpy.data.objects[row['name']];o.hide_viewport=True;o.hide_render=True
    o['REV005_F07_LEGACY_RETIRED']=True;o['REV005_F07_RETIRED_BY']='F07_CLASS_N'
legacy_after=[signature(bpy.data.objects[row['name']]) for row in legacy]
(EVIDENCE/'F07_LEGACY_RETIREMENT_AFTER.json').write_text(json.dumps({'task':'M08.41 / F07 only','status':'AFTER_F07_LEGACY_RETIREMENT','count':len(legacy_after),'objects':legacy_after},indent=2,ensure_ascii=False),encoding='utf-8')
legacy_diff=[];allowed={'hide_viewport','hide_render','custom_properties'}
for before,after in zip(legacy_before,legacy_after):
    changed={k for k in before if before[k]!=after[k]}
    if changed-allowed:raise RuntimeError(f'Unauthorized legacy retirement change {before["name"]}: {changed-allowed}')
    if not after['hide_viewport'] or not after['hide_render']:raise RuntimeError('Legacy object not hidden '+after['name'])
    o=bpy.data.objects[after['name']]
    if o.get('REV005_F07_LEGACY_RETIRED') is not True or o.get('REV005_F07_RETIRED_BY')!='F07_CLASS_N':raise RuntimeError('Missing retirement metadata '+o.name)
    legacy_diff.append({'name':before['name'],'changed_fields':sorted(changed),'transform_material_data_unchanged':not bool(changed & {'matrix_world','dimensions','material_slots','data_block','parent','collections'})})
(EVIDENCE/'F07_LEGACY_RETIREMENT_DIFF.json').write_text(json.dumps({'task':'M08.41 / F07 only','status':'PASS','count':len(legacy_diff),'only_visibility_and_retirement_metadata_changed':True,'objects':legacy_diff},indent=2),encoding='utf-8')

pre=json.loads((EVIDENCE/'F07_PROTECTION_BEFORE.json').read_text(encoding='utf-8'))
after={};protection_diffs=[]
for group,rows in pre['objects'].items():
    after[group]=[]
    for b in rows:
        o=bpy.data.objects.get(b['name'])
        if not o:raise RuntimeError('Protected prior object missing '+b['name'])
        a=signature(o);after[group].append(a)
        for f in ('type','matrix_world','dimensions','parent','collections','material_slots','data_block','hide_viewport','hide_render','custom_properties'):
            if b.get(f)!=a.get(f):protection_diffs.append({'group':group,'name':b['name'],'field':f})
if protection_diffs:raise RuntimeError('Protected prior-state mutation '+repr(protection_diffs[:12]))
post=dict(pre);post['status']='POST_BUILD_PROTECTION_SNAPSHOT';post['objects']=after
(EVIDENCE/'F07_PROTECTION_AFTER.json').write_text(json.dumps(post,indent=2,ensure_ascii=False),encoding='utf-8')
(EVIDENCE/'F07_PROTECTION_DIFF.json').write_text(json.dumps({'task':'M08.41 / F07 only','status':'PASS','protected_object_count':sum(len(x) for x in pre['objects'].values()),'unauthorized_differences':protection_diffs},indent=2),encoding='utf-8')

# Dimensional, enclosure, camera and cross-facility collision gates.
def close(actual,expected,tol): return abs(float(actual)-float(expected))<=tol
checks=[]
def anchor(name,loc,dims,loc_tol=.05,dim_tol=.05):
    o=bpy.data.objects.get(name)
    if o is None: raise RuntimeError('Missing locked anchor '+name)
    ok=all(close(o.location[i],loc[i],loc_tol) for i in range(3)) and all(close(o.dimensions[i],dims[i],dim_tol) for i in range(3))
    checks.append({'name':name,'actual_location':[round(float(x),4) for x in o.location],
      'actual_dimensions':[round(float(x),4) for x in o.dimensions],'expected_location':loc,'expected_dimensions':dims,'tolerance_m':loc_tol,'pass':ok})
    if not ok: raise RuntimeError('Locked anchor mismatch '+name)
anchor('F07_ROOM_FLOOR',[-58,-64,1],[46,28,.18])
anchor('F07_RECEPTION_DESK_TOP',[-74,-72.5,1.82],[5.5,1,.1],.05,.05)
anchor('F07_MEETING_DISPLAY_SCREEN',[-59,-50.32,3.4],[3.2,.035,1.8],.05,.05)
anchor('F07_SAMPLE_ISLAND_TOP',[-44.5,-60.3,1.96],[1.2,5,.1],.05,.05)
anchor('F07_SINK_BENCH_TOP',[-38.5,-72,1.96],[2.2,.8,.1],.05,.05)
for i,(x,y) in enumerate([(x,y) for y in (-65.2,-61.3) for x in (-69,-65,-61,-57)]):
    anchor(f'F07_OFFICE_STATION_{i:02d}_TOP',[x,y,1.81],[1.6,.75,.06],.05,.05)
for i,(x,y) in enumerate([(-48,-72),(-43,-72),(-48,-66),(-43,-66)]):
    o=bpy.data.objects.get(f'F07_LAB_BENCH_{i+1}_WORKTOP')
    if not o or not close(o.location.x,x,.05) or not close(o.location.y,y,.05): raise RuntimeError('Lab bench anchor mismatch')
    if sorted(round(float(v),2) for v in o.dimensions[:2])!=[.8,4.0]: raise RuntimeError('Lab bench dimensions mismatch')
    checks.append({'name':o.name,'location':[round(float(v),4) for v in o.location],'dimensions':[round(float(v),4) for v in o.dimensions],'footprint_orientation':'4.0 m long axis along Y','pass':True})
if sum(o.name.startswith('F07_OFFICE_STATION_') and o.name.endswith('_TOP') for o in created)!=8: raise RuntimeError('Office station count')
if sum(o.name.startswith('F07_MEETING_CHAIR_') and o.name.endswith('_SEAT') for o in created)!=10: raise RuntimeError('Meeting chair count')
if sum(o.name.startswith('F07_STORAGE_') and o.name.endswith('_SHELF_1.35') for o in created)!=5: raise RuntimeError('Storage bay count')
if sum(o.name.startswith('F07_CEILING_FIXTURE_') and o.name.endswith('_HOUSING') for o in created)!=12: raise RuntimeError('Ceiling fixture count')

def bounds(o):
    pts=[o.matrix_world @ Vector(v) for v in o.bound_box]
    return [min(p[i] for p in pts) for i in range(3)],[max(p[i] for p in pts) for i in range(3)]
bpy.context.view_layer.update()
outside=[]
for o in created:
    if o.type!='MESH': continue
    lo,hi=bounds(o)
    if lo[0]<-81.01 or hi[0]>-34.99 or lo[1]<-78.01 or hi[1]>-49.99:
        if not any(tag in o.name for tag in ('ENTRY_','FRONT_','DISPLAY')):
            outside.append({'name':o.name,'min':lo,'max':hi})
if outside: raise RuntimeError('F07 object outside envelope '+repr(outside[:8]))

protected_names=set()
for group in ('F01_accepted','F02_accepted','F03_accepted','F04_accepted','F05_accepted_primary','F06_accepted'):
    protected_names.update(row['name'] for row in pre['objects'][group])
collisions=[]
for o in created:
    if o.type!='MESH': continue
    alo,ahi=bounds(o)
    for name in protected_names:
        p=bpy.data.objects.get(name)
        if not p or p.type!='MESH': continue
        blo,bhi=bounds(p)
        if all(min(ahi[i],bhi[i])-max(alo[i],blo[i])>.001 for i in range(3)):
            collisions.append({'new_f07':o.name,'protected_object':name})
if collisions: raise RuntimeError('BLOCKED_F07_CROSS_FACILITY_COLLISION '+repr(collisions[:8]))

camera_records=[];render_only={x.strip() for x in os.environ.get('F07_RENDER_ONLY','').split(',') if x.strip()}
export_only=os.environ.get('F07_EXPORT_PARITY_ONLY')=='1'
for name,pos,target,lens in seeds:
    data=bpy.data.cameras.new('F07_CAMERA_'+name); cam=bpy.data.objects.new('F07_CAMERA_'+name,data)
    scene.collection.objects.link(cam); cam.location=pos
    cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler()
    data.lens=lens;data.sensor_width=36;data.clip_start=.05;data.clip_end=250
    bpy.context.view_layer.update(); cp=Vector(pos); inside=[]
    for o in created:
        if o.type!='MESH': continue
        lo,hi=bounds(o)
        if all(lo[i]+.01<=cp[i]<=hi[i]-.01 for i in range(3)): inside.append(o.name)
    if inside: raise RuntimeError(f'Camera inside F07 geometry {name}: {inside[:8]}')
    scene.camera=cam
    camera_records.append({'name':name,'camera_xyz':list(pos),'target_xyz':list(target),'lens_mm':lens,'sensor_width_mm':36,'camera_inside_geometry':False,'final_resolution':[1440,960],'preview_resolution':[900,600]})
    if export_only or (render_only and name not in render_only): continue
    scene.render.resolution_x=1440;scene.render.resolution_y=960;scene.render.resolution_percentage=100
    scene.render.filepath=str(EVIDENCE/f'F07_{name}.png');bpy.ops.render.render(write_still=True)
    image=bpy.data.images.load(str(EVIDENCE/f'F07_{name}.png'),check_existing=False)
    if image.size[0]!=1440 or image.size[1]!=960 or max(image.pixels)<.02: raise RuntimeError('Invalid/black image '+name)
    bpy.data.images.remove(image)
    scene.render.resolution_x=900;scene.render.resolution_y=600;scene.render.resolution_percentage=100
    scene.render.filepath=str(EVIDENCE/f'F07_{name}_PREVIEW_900x600.png');bpy.ops.render.render(write_still=True)

manifest=[]
for o in created:
    if o.type=='MESH': manifest.append({'name':o.name,'role':role_by_name[o.name],'location':[round(float(x),4) for x in o.location],
        'dimensions':[round(float(x),4) for x in o.dimensions],'materials':[s.material.name if s.material else None for s in o.material_slots]})
(EVIDENCE/'F07_NEW_ACCEPTED_MANIFEST.json').write_text(json.dumps({'task':'M08.41 / F07 only','destination_collection':DEST,'count':len(manifest),'objects':manifest},indent=2,ensure_ascii=False),encoding='utf-8')
validation={'task':'M08.41 / F07 only','facility':FACILITY,'status':'PASS','room_envelope':{'center':[-58,-64],'dimensions':[46,28],'x_range':[-81,-35],'y_range':[-78,-50]},
 'anchor_checks':checks,'counts':{'reception_visitor_chairs':4,'reception_operator_chair':1,'office_workstations':8,'meeting_chairs':10,'primary_lab_benches':4,'qc_instrument_classes':6,'storage_bays':5,'ceiling_fixtures':12,'lab_task_lights':4},
 'confirmed_legacy_retired':len(legacy),'ambiguous_legacy_candidates':0,'not_f07_candidates_preserved':inventory['classification_counts']['NOT_F07'],
 'protection_diff':'PASS','cross_facility_collisions':collisions,'outside_envelope_objects':outside,'accepted_mesh_count':len(manifest),'camera_records':camera_records,'visual_status':'RENDERED_FOR_REVIEW'}
(EVIDENCE/'F07_DIMENSIONAL_VALIDATION.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
(EVIDENCE/'F07_CAMERA_VALIDATION.json').write_text(json.dumps({'task':'M08.41 / F07 only','status':'PASS','cameras':camera_records},indent=2),encoding='utf-8')
(EVIDENCE/'F07_VALIDATION.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
if export_only:
    # Deterministic export staging: baseline node membership minus only exact
    # confirmed F07 legacy nodes, plus every new accepted F07 mesh object.
    raw=GLB.read_bytes(); json_len=struct.unpack_from('<I',raw,12)[0]
    base=json.loads(raw[20:20+json_len].decode('utf-8').rstrip('\x00 '))
    baseline_names={str(n['name']) for n in base.get('nodes',[]) if n.get('name')}
    inv=json.loads((EVIDENCE/'F07_LEGACY_ADMIN_INVENTORY.json').read_text(encoding='utf-8'))
    retired={str(r['name']) for r in inv['candidates'] if r['ownership_classification']=='CONFIRMED_F07_LEGACY' and r['present_in_pre_f07_glb']}
    new_names={o.name for o in created if o.type=='MESH'}
    expected=(baseline_names-retired)|new_names
    missing_objects=sorted(expected-{o.name for o in bpy.data.objects})
    if missing_objects: raise RuntimeError('F07_EXPORT_STAGING_MISSING_BLENDER_OBJECTS '+repr(missing_objects[:20]))
    # The accepted baseline GLB intentionally contains quarantined nodes that
    # are hidden in the Blend. Temporarily expose exact expected objects and
    # their collection path so Blender's selection exporter can serialize them.
    object_state={o.name:(o.hide_viewport,o.hide_render,o.hide_get(),o.select_get()) for o in bpy.data.objects}
    active_object=bpy.context.view_layer.objects.active
    collection_state={c.name:c.hide_viewport for c in bpy.data.collections}
    layer_state=[]
    def expose_layer(layer):
        layer_state.append((layer,layer.exclude,layer.hide_viewport))
        layer.exclude=False; layer.hide_viewport=False
        layer.collection.hide_viewport=False
        for child in layer.children: expose_layer(child)
    for root_layer in bpy.context.view_layer.layer_collection.children: expose_layer(root_layer)
    for name in expected:
        o=bpy.data.objects[name]; o.hide_viewport=False; o.hide_render=False
        try: o.hide_set(False)
        except: pass
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.data.objects:
        o.select_set(o.name in expected)
    temp=EVIDENCE/'F07_GLB_PARITY_CANDIDATE.glb'
    result=bpy.ops.export_scene.gltf(filepath=str(temp),export_format='GLB',use_selection=True,use_visible=False,
      export_cameras=True,export_lights=True)
    if 'FINISHED' not in result: raise RuntimeError('F07_GLB_EXPORT_FAILED '+repr(result))
    exported=temp.read_bytes(); out_len=struct.unpack_from('<I',exported,12)[0]
    out=json.loads(exported[20:20+out_len].decode('utf-8').rstrip('\x00 '))
    actual={str(n['name']) for n in out.get('nodes',[]) if n.get('name')}
    missing=sorted(expected-actual); unexpected=sorted(actual-expected)
    parity={'task':'M08.41 / F07 only','status':'PASS' if not missing and not unexpected else 'FAIL',
      'method':'accepted pre-F07 GLB node-name set minus exact confirmed F07 legacy names, plus all new accepted F07 mesh names; Blender glTF selection export use_selection=true use_visible=false export_cameras=true export_lights=true',
      'baseline_node_count':len(baseline_names),'retired_legacy_glb_node_count':len(retired),'new_f07_node_count':len(new_names),
      'expected_node_count':len(expected),'actual_node_count':len(actual),'missing_expected_names':missing,
      'unexpected_names':unexpected,'accepted_f01_f06_baseline_names_preserved':not bool((baseline_names-retired)-actual),
      'new_f07_names_present':not bool(new_names-actual),'retired_f07_legacy_names_absent':not bool(retired&actual),
      'canonical_glb_sha256_unchanged':sha(GLB)==baseline['expected']['glb_sha256'],
      'candidate_glb_sha256':sha(temp),'candidate_path':str(temp)}
    for name,(hide_v,hide_r,hide_local,selected) in object_state.items():
        o=bpy.data.objects.get(name)
        if not o: continue
        o.hide_viewport=hide_v; o.hide_render=hide_r
        try: o.hide_set(hide_local)
        except: pass
        try: o.select_set(selected)
        except: pass
    for name,hidden in collection_state.items():
        c=bpy.data.collections.get(name)
        if c: c.hide_viewport=hidden
    for layer,excluded,hidden in reversed(layer_state):
        layer.exclude=excluded; layer.hide_viewport=hidden
    if active_object and active_object.name in bpy.data.objects:
        bpy.context.view_layer.objects.active=active_object
    bpy.context.view_layer.update()
    (EVIDENCE/'F07_GLB_EXPORT_PARITY.json').write_text(json.dumps(parity,indent=2),encoding='utf-8')
    print('F07_GLB_EXPORT_PARITY',parity['status'],'expected',len(expected),'actual',len(actual),'missing',len(missing),'unexpected',len(unexpected))
    if os.environ.get('F07_FINALIZE')=='1':
        if parity['status']!='PASS' or not parity['canonical_glb_sha256_unchanged']:
            raise RuntimeError('BLOCKED_F07_GLB_EXPORT_PARITY')
        staged_blend=BLEND.with_name(BLEND.stem+'.F07_STAGED.blend')
        staged_glb=GLB.with_name(GLB.stem+'.F07_STAGED.glb')
        bpy.ops.wm.save_as_mainfile(filepath=str(staged_blend))
        shutil.copy2(temp,staged_glb)
        if not staged_blend.exists() or not staged_glb.exists(): raise RuntimeError('F07_STAGED_OUTPUT_MISSING')
        if sha(staged_glb)!=parity['candidate_glb_sha256']: raise RuntimeError('F07_STAGED_GLB_HASH_MISMATCH')
        # Only after staging hashes and exact membership pass do canonical refs move.
        os.replace(staged_glb,GLB)
        os.replace(staged_blend,BLEND)
        final={'task':'M08.41 / F07 only','status':'SAVED','blend_path':str(BLEND),'glb_path':str(GLB),
          'blend_sha256':sha(BLEND),'glb_sha256':sha(GLB),'baseline_blend_sha256':baseline['expected']['blend_sha256'],
          'baseline_glb_sha256':baseline['expected']['glb_sha256'],'glb_export_parity':'PASS',
          'expected_glb_node_count':len(expected),'actual_glb_node_count':len(actual),
          'canonical_blend_replaced':True,'canonical_glb_replaced':True}
        (EVIDENCE/'F07_FINAL_HASHES.json').write_text(json.dumps(final,indent=2),encoding='utf-8')
        print('F07_FINAL_CANONICAL_SAVE PASS',final['blend_sha256'],final['glb_sha256'])
print('F07_DRAFT_BUILD_COMPLETE',len(manifest),'mesh objects; retired',len(legacy),'legacy; protected',sum(len(x) for x in pre['objects'].values()),'objects; collisions',len(collisions),'outside',len(outside))
