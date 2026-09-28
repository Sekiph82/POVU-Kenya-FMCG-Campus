import bpy, hashlib, json, math
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v05"
COL = "REV005_INTERIOR_REMEDIATION_V05"

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest().upper()

def mat(name,color,metal=0.0,rough=.4):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    if bs: bs.inputs["Base Color"].default_value=(*color,1); bs.inputs["Metallic"].default_value=metal; bs.inputs["Roughness"].default_value=rough
    return m

M={
 "floor":mat("REV005_V05_FLOOR",(.20,.25,.28),.1,.45), "wall":mat("REV005_V05_WALL",(.70,.75,.77),.05,.5),
 "glass":mat("REV005_V05_GLASS",(.05,.40,.55),.35,.16), "steel":mat("REV005_V05_STEEL",(.18,.25,.30),.85,.24),
 "stainless":mat("REV005_V05_STAINLESS",(.65,.70,.72),.9,.18), "blue":mat("REV005_V05_BLUE",(.02,.16,.52),.25,.3),
 "teal":mat("REV005_V05_TEAL",(.01,.48,.58),.25,.25), "orange":mat("REV005_V05_ORANGE",(.90,.23,.03),.12,.34),
 "yellow":mat("REV005_V05_YELLOW",(.98,.58,.02),.08,.35), "green":mat("REV005_V05_GREEN",(.02,.42,.18),.2,.32),
 "purple":mat("REV005_V05_PURPLE",(.55,.08,.35),.18,.34), "white":mat("REV005_V05_WHITE",(.88,.90,.91),.05,.32),
 "dark":mat("REV005_V05_DARK",(.015,.02,.025),.3,.2), "wood":mat("REV005_V05_WOOD",(.42,.19,.05),0,.5),
 "warm":mat("REV005_V05_WARM",(.93,.40,.05),.05,.4), "red":mat("REV005_V05_RED",(.78,.03,.02),.05,.36),
 "soft":mat("REV005_V05_SOFT",(.06,.48,.70),.05,.48), "pink":mat("REV005_V05_PINK",(.75,.20,.45),.05,.4),
}
C=bpy.data.collections.get(COL)
if C:
    for o in list(C.objects): bpy.data.objects.remove(o,do_unlink=True)
else:
    C=bpy.data.collections.new(COL); bpy.context.scene.collection.children.link(C)

def link(o,f):
    for c in list(o.users_collection): c.objects.unlink(o)
    C.objects.link(o); o["REV005_REMEDIATION_V05"]=True; o["facility"]=f; return o
def mesh(name,verts,faces,loc,material,f):
    me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(verts,[],faces); me.update(); o=link(bpy.data.objects.new(name,me),f); o.location=loc; o.data.materials.append(M[material]); return o
def box(name,loc,dims,material,f,rot=None):
    x,y,z=[v/2 for v in dims]; vs=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]; fs=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]; o=mesh(name,vs,fs,loc,material,f)
    if rot:o.rotation_euler=rot
    return o
def cyl(name,loc,radius,depth,material,f,sides=24,rot=None):
    vs=[]
    for z in (-depth/2,depth/2):
        for i in range(sides):
            a=math.tau*i/sides; vs.append((radius*math.cos(a),radius*math.sin(a),z))
    fs=[tuple(range(sides-1,-1,-1)),tuple(range(sides,2*sides))]+[(i,(i+1)%sides,sides+(i+1)%sides,sides+i) for i in range(sides)]
    o=mesh(name,vs,fs,loc,material,f)
    if rot:o.rotation_euler=rot
    return o
def pipe(name,a,b,r,material,f):
    a,b=Vector(a),Vector(b); d=b-a; o=cyl(name,(a+b)/2,r,d.length,material,f,16); o.rotation_euler=d.to_track_quat("Z","Y").to_euler(); return o
def light(prefix,x,y,z,f):
    box(prefix+"_FIXTURE",(x,y,z),(3,.28,.12),"white",f); box(prefix+"_GLOW",(x,y,z-.08),(2.2,.12,.05),"warm",f)
def envelope(prefix,x,y,w,d,h,f,doors=True):
    box(prefix+"_FLOOR",(x,y,1.05),(w,d,.18),"floor",f)
    box(prefix+"_BACK",(x,y+d/2,h/2),(w,.18,h),"wall",f)
    box(prefix+"_LEFT",(x-w/2,y,h/2),(.18,d,h),"wall",f)
    box(prefix+"_RIGHT",(x+w/2,y,h/2),(.18,d,h),"wall",f)
    for xx in (x-w*.28,x,x+w*.28): box(prefix+"_SOFFIT_"+str(xx),(xx,y,h-.18),(w*.16,d-.8,.18),"steel",f)
    for i in range(max(2,int(w//10))): light(prefix+"_LIGHT_"+str(i),x-w/2+5+i*10,y,h-.5,f)
    if doors:
        box(prefix+"_DOOR_L",(x-2,y-d/2+.10,3.0),(.12,.16,5.2),"glass",f); box(prefix+"_DOOR_R",(x+2,y-d/2+.10,3.0),(.12,.16,5.2),"glass",f); box(prefix+"_DOOR_HEADER",(x,y-d/2+.10,5.55),(4.2,.16,.16),"steel",f)
def divider(name,x,y,w,h,f):
    box(name+"_PANEL",(x,y,h/2),(w,.14,h),"glass",f); box(name+"_POST",(x,y, h/2),(.16,.22,h),"steel",f)
def table_chairs(prefix,x,y,w,d,f,count=4,material="wood"):
    box(prefix+"_TABLE",(x,y,2.0),(w,d,.24),material,f)
    for i in range(count):
        ang=math.tau*i/count; cyl(prefix+"_CHAIR_"+str(i),(x+math.cos(ang)*(w*.55),y+math.sin(ang)*(d*.8),1.45),.34,.7,"teal",f,16)
def rack(prefix,x,y,levels,bays,f,material="steel"):
    for b in range(bays):
        xx=x+b*2.4
        for z in range(levels):
            box(prefix+"_UPRIGHT_"+str(b)+"_"+str(z),(xx,y,1.5+z*1.8),(.16,.2,3.2),material,f)
            box(prefix+"_PALLET_"+str(b)+"_"+str(z),(xx+1.0,y,1.55+z*1.8),(2,.95,.14),"wood",f)
            box(prefix+"_LOAD_"+str(b)+"_"+str(z),(xx+1.0,y,2.0+z*1.8),(1.55,.72,.75),"white",f)
    for z in range(levels): box(prefix+"_BEAM_"+str(z),(x+(bays-1)*1.2,y,2.7+z*1.8),(bays*2.4,.18,.16),material,f)
def pallet(prefix,x,y,f,material="wood",height=1.0):
    box(prefix+"_BASE",(x,y,1.25),(2.0,1.6,.18),material,f); box(prefix+"_LOAD",(x,y,1.25+height/2),(1.5,1.2,height),"white",f)
def guard(prefix,x,y,l,w,f):
    box(prefix+"_A",(x,y-w/2,2.2),(l,.12,2.0),"yellow",f); box(prefix+"_B",(x,y+w/2,2.2),(l,.12,2.0),"yellow",f)
def belt(prefix,x,y,l,w,f,z=1.45):
    box(prefix+"_BED",(x,y,z),(l,w,.25),"stainless",f); guard(prefix,x,y,l,w,f)
    for i in range(7): cyl(prefix+"_ROLLER"+str(i),(x-l/2+.6+i*(l-1.2)/6,y,z+.2),w*.38,.10,"dark",f,16,(0,math.pi/2,0))
def machine(prefix,x,y,w,d,h,f,material="blue"):
    box(prefix+"_HOUSING",(x,y,h/2+1),(w,d,h),material,f); box(prefix+"_PANEL",(x,y-d/2-.08,h*.65+1),(w*.55,.12,h*.28),"teal",f); box(prefix+"_BASE",(x,y,1.28),(w+.4,d+.4,.22),"steel",f)
def tank(prefix,x,y,r,h,f,material="steel"):
    cyl(prefix+"_VESSEL",(x,y,h/2+1),r,h,material,f,28); cyl(prefix+"_LID",(x,y,h+1.1),r*.7,.18,"steel",f,24); pipe(prefix+"_OUT",(x,y+r*.7,h*.62+1),(x+3,y+r*.7,h*.62+1),.12,"yellow",f)

def admin():
    f="Administration / HQ / R&D / QC"; x,y=-58,-64; envelope("V05_ADMIN",x,y,52,29,7,f)
    box("V05_ADMIN_RECEPTION",(-78,-51.2,2.2),(8,1.2,1.7),"wood",f); divider("V05_ADMIN_RECEPTION_GLASS",-78,-52.2,8,4.2,f)
    for i in range(6): box("V05_ADMIN_WORKPOD"+str(i),(-70+i*5.4,-61,2.15),(3.8,2.8,1.35),"wood",f)
    table_chairs("V05_ADMIN_MEETING",-56,-55,8,3,f,8)
    divider("V05_ADMIN_LAB_PARTITION",-42,-64,12,4.3,f)
    box("V05_ADMIN_QC_BENCH",(-42,-70,2.0),(13,1.1,1.5),"stainless",f)
    for i in range(6): box("V05_ADMIN_QC_INSTR"+str(i),(-47+i*2.0,-69.3,3.0),(.7,.4,.55),"blue",f)
    rack("V05_ADMIN_LAB_STORAGE",-38,-75,2,4,f)

def restaurant():
    f="Restaurant / POVU Café / kitchen"; x,y=5,-69; envelope("V05_RESTAURANT",x,y,45,25,7,f)
    box("V05_CAFE_SERVICE_COUNTER",(-10,-60.5,2.2),(10,1.0,1.7),"wood",f); box("V05_CAFE_BACKBAR",(-10,-59.4,4.6),(10,.18,4.6),"blue",f)
    box("V05_CAFE_POS",(-7,-61.2,3.1),(.7,.5,.8),"teal",f)
    for i,(xx,yy) in enumerate(((-7,-67),(5,-67),(17,-67),(-7,-76),(5,-76),(17,-76))): table_chairs("V05_DINING"+str(i),xx,yy,3,2.2,f,4)
    divider("V05_KITCHEN_PARTITION",5,-78,20,4.2,f); box("V05_PASS",(5,-75.0,4.0),(14,.18,1.6),"warm",f)
    for i in range(5): machine("V05_KITCHEN_APPLIANCE"+str(i),-9+i*4.4,-80,3.2,1.4,2.2,f,"stainless")
    rack("V05_KITCHEN_STORAGE",18,-80,2,3,f,"steel")

def clinic():
    f="Occupational health / first aid"; x,y=-18,-94; envelope("V05_CLINIC",x,y,24,18,6.5,f)
    box("V05_CLINIC_RECEPTION",(-25,-100.5,2.2),(5,1.0,1.5),"wood",f); box("V05_CLINIC_WAIT_TABLE",(-24,-96,1.5),(3,2,.2),"wood",f)
    for i in range(3): cyl("V05_CLINIC_WAIT"+str(i),(-26+i*1.8,-94,1.6),.32,.7,"teal",f,16)
    divider("V05_CLINIC_PRIVACY",-13,-94,7,3.6,f); box("V05_CLINIC_BED",(-11,-99,1.6),(2.2,5,.55),"white",f); box("V05_CLINIC_BACK",(-11,-101.2,2.7),(2.2,.18,1.4),"blue",f)
    rack("V05_CLINIC_MED_STORAGE",-25,-88,2,3,f,"white"); box("V05_CLINIC_TREATMENT_CART",(-8,-97,2.0),(1.2,.8,1.3),"stainless",f)

def training():
    f="Training / Academy"; x,y=30,-61; envelope("V05_TRAINING",x,y,26,18,6.5,f)
    box("V05_TRAINING_SCREEN",(30,-69.7,4.0),(12,.18,4.0),"blue",f); box("V05_TRAINING_INSTRUCTOR",(30,-66.5,2.0),(4,1,1.4),"wood",f)
    for i,(xx,yy) in enumerate(((24,-62),(31,-62),(24,-57),(31,-57))): table_chairs("V05_CLASS"+str(i),xx,yy,4,2,f,4)
    rack("V05_TRAINING_STORAGE",40,-56,2,2,f,"steel")

def wellness():
    f="Wellness / recreation"; x,y=30,-70; envelope("V05_WELLNESS",x,y,28,22,6.5,f)
    for i in range(4): box("V05_YOGA_MAT"+str(i),(22+i*4,-74,1.2),(2.4,5,.08),"purple",f)
    for i in range(3): machine("V05_GYM_MACHINE"+str(i),24+i*6,-64,2.2,2.0,2.6,f,"teal")
    rack("V05_WELLNESS_LOCKER",40,-76,2,3,f,"steel")

def security():
    f="Security / reception / visitor arrival"; x,y=-58,-84; envelope("V05_SECURITY",x,y,48,16,6.5,f)
    box("V05_SECURITY_DESK",(-67,-89.5,2.2),(8,1.1,1.5),"wood",f); box("V05_SECURITY_SCREEN",(-67,-88.8,4.0),(6,.12,2.2),"blue",f)
    for i in range(4): box("V05_TURNSTILE"+str(i),(-48+i*2.3,-88,1.4),(.4,2.2,1.2),"steel",f)
    box("V05_SECURITY_SCREENING",(-42,-82,1.6),(5,2,.3),"stainless",f); divider("V05_SECURITY_WAIT",-65,-79,12,3.4,f); table_chairs("V05_VISITOR_WAIT",-74,-80,3,2,f,4)

def gatehouse():
    f="Security gatehouse"; x,y=96,-106; envelope("V05_GATEHOUSE",x,y,20,14,5.8,f)
    box("V05_GATE_DESK",(96,-110,2.1),(5,1,1.4),"wood",f); box("V05_GATE_MONITOR_WALL",(96,-112.2,3.6),(7,.14,2.2),"blue",f)
    for i in range(2): box("V05_GATE_BARRIER"+str(i),(106+i*4,-101,1.3),(.2,6,2.2),"yellow",f)
    for i in range(3): box("V05_GATE_WINDOW"+str(i),(90+i*6,-99.1,3.5),(4,.12,2.2),"glass",f)

def glass():
    f="Glass Deck central command / training / café gallery"; x,y=70,24; envelope("V05_GLASS",x,y,10,45,17,f,False)
    box("V05_GLASS_COMMAND_WALL",(70,38,8.0),(8,.18,10),"blue",f)
    for i in range(4):
        box("V05_GLASS_CONSOLE"+str(i),(67+i*2,34,2.1),(1.2,1,1.4),"steel",f); box("V05_GLASS_MONITOR"+str(i),(67+i*2,33.45,4.1),(1.0,.12,1),"teal",f)
    table_chairs("V05_GLASS_TRAINING",70,24,6,2.2,f,8)
    box("V05_GLASS_CAFE_COUNTER",(70,7,2.2),(8,1,1.7),"wood",f); box("V05_GLASS_CAFE_BACKBAR",(70,8.2,5),(8,.18,5),"blue",f)
    for i in range(4): cyl("V05_GLASS_CAFE_SEAT"+str(i),(67+i*2,4.5,1.5),.3,.65,"purple",f,16)

def warehouse(kind,x,y,w,d,f):
    envelope("V05_"+kind,x,y,w,d,9,f)
    if kind=="RAW":
        for row in (y-12,y-4,y+4,y+12): rack("V05_RAW_RACK"+str(row),x-w/2+4,row,3,8,f,"steel")
        for i in range(6): pallet("V05_RAW_RECEIVE"+str(i),x-w/2+5+i*3,y+d/2-3,f,"wood",1.2)
        box("V05_RAW_DOCK",(x,y+d/2-.1,3),(14,.18,4.5),"orange",f); box("V05_RAW_RECEIVE_DESK",(x+12,y+d/2-5,2),(3,1,1.5),"wood",f)
        for i in range(4): cyl("V05_RAW_DRUM"+str(i),(x+14,y-8+i*4,2),.65,1.4,"orange",f,20)
    elif kind=="PACK":
        for row in (y-12,y-4,y+4,y+12): rack("V05_PACK_RACK"+str(row),x-w/2+5,row,3,7,f,"teal")
        for i in range(5): box("V05_PACK_ROLL"+str(i),(x+10,y-10+i*5,2),(1.6,2.4,1.8),"white",f)
        for i in range(5): pallet("V05_PACK_CARTON"+str(i),x-w/2+5+i*3,y+d/2-3,f,"wood",.9)
        box("V05_PACK_STAGING",(x,y-1,1.2),(10,3,.18),"yellow",f)
    else:
        for row in (y-7,y,y+7): rack("V05_FG_RACK"+str(row),x-w/2+5,row,4,9,f,"steel")
        for i in range(7): pallet("V05_FG_STAGE"+str(i),x-8+i*2.6,y+d/2-3,f,"wood",1.25)
        box("V05_FG_LOADOUT",(x,y+d/2-.1,3),(14,.18,4.5),"orange",f); box("V05_FG_DISPATCH_DESK",(x+15,y+d/2-4,2),(3,1,1.5),"wood",f)
        for i in range(2): box("V05_FG_AMR"+str(i),(x+8+i*3,y-2,1),(1.5,2.2,.4),"blue",f)

def chemical():
    f="Chemical compound / controlled receiving"; x,y=56,80; envelope("V05_CHEM",x,y,36,30,8,f)
    for i,xx in enumerate((47,56,65)):
        box("V05_CHEM_BUND"+str(i),(xx,72,1.25),(6,6,.25),"yellow",f); tank("V05_CHEM_TANK"+str(i),xx,72,2.1,5,f,"steel")
    for i in range(5): pallet("V05_CHEM_RECEIVE"+str(i),45+i*4,91,f,"red",1.1)
    box("V05_CHEM_DOCK",(56,94.6,3.2),(18,.18,4.4),"orange",f); box("V05_CHEM_TRANSFER",(70,78,2),(2,2,1.5),"stainless",f); pipe("V05_CHEM_TRANSFER_PIPE",(65,72,5),(70,78,3),.16,"yellow",f)
    divider("V05_CHEM_CONTROL",72,85,5,4,f)

def bottle():
    f="Bottle blow molding"; x,y=52,10; envelope("V05_BOTTLE",x,y,38,24,8,f)
    machine("V05_BLOW_PREFORM_HOPPER",39,11,3,3,3.6,f,"yellow"); belt("V05_BLOW_PREFORM_FEED",43,11,5,1.2,f); machine("V05_BLOW_OVEN",47,11,5,4,4.6,f,"orange");
    for i in range(3): pipe("V05_BLOW_HEAT_DUCT"+str(i),(45+i*1.5,13,6),(45+i*1.5,13,7.6),.12,"stainless",f)
    machine("V05_BLOW_MOULD_CLAMP",53,11,5,4,5,f,"blue"); guard("V05_BLOW_GUARD",53,11,7,5,f); belt("V05_BLOW_OUTFEED",60,11,8,1.3,f); machine("V05_BLOW_INSPECTION",65,11,2.5,2.5,4,f,"white")

def liquid():
    f="Liquid filling / packaging"; x,y=10,-2; envelope("V05_LIQUID",x,y,46,20,7,f)
    belt("V05_LIQUID_INFEED",-9,-2,7,1.2,f); machine("V05_LIQUID_FILLER",-2,-2,5,3,4.5,f,"blue")
    for i in range(6): cyl("V05_LIQUID_NOZZLE"+str(i),(-3+i*.8,-2,5.4),.12,.9,"stainless",f,16)
    belt("V05_LIQUID_TO_CAPPER",5,-2,7,1.2,f); machine("V05_LIQUID_CAPPER",10,-2,4,3,4.0,f,"purple"); belt("V05_LIQUID_LABEL",16,-2,6,1.2,f); machine("V05_LIQUID_INSPECT",21,-2,2.4,2.4,3.5,f,"white"); belt("V05_LIQUID_CASE",27,-2,7,1.8,f); machine("V05_LIQUID_CASE_PACK",31,-2,3,3,3.2,f,"orange")

def powder():
    f="Powder handling / packing"; x,y=-48,43; envelope("V05_POWDER",x,y,36,19,7,f)
    tank("V05_POWDER_HOPPER",-62,43,2,4.5,f,"green"); pipe("V05_POWDER_FEED",(-60,43,5),(-54,43,4),.18,"green",f); machine("V05_POWDER_DOSER",-53,43,4,3,3.8,f,"blue"); belt("V05_POWDER_PACK",-47,43,8,1.3,f); machine("V05_POWDER_SEAL",-41,43,3,2.6,3.2,f,"orange"); box("V05_POWDER_TRANSFER",(-36,43,2),(3,2,1.6),"white",f)

def toothpaste():
    f="Toothpaste production"; x,y=-12,43; envelope("V05_PASTE",x,y,40,19,7,f)
    tank("V05_PASTE_VACUUM_MIX",-26,43,2.5,4.8,f,"green"); tank("V05_PASTE_HOLD",-20,43,1.8,3.6,f,"stainless"); pipe("V05_PASTE_TRANSFER",(-18,43,4),(-12,43,4),.16,"teal",f); box("V05_PASTE_TUBE_MAG",(-9,43,3),(3,2,4),"steel",f); machine("V05_PASTE_FILL",-4,43,3,3,3.8,f,"blue"); machine("V05_PASTE_CRIMP",1,43,2.4,2.4,3.6,f,"purple"); belt("V05_PASTE_CODE",5,43,5,1.0,f); machine("V05_PASTE_CARTON",10,43,3,3,3.4,f,"orange")

def wipes():
    f="Wet wipes production"; x,y=22,43; envelope("V05_WIPES",x,y,50,19,7,f)
    for i,xx in enumerate((4,7)): cyl("V05_WIPES_ROLL"+str(i),(xx,43,3.4),1.5,.8,"white",f,32,(0,math.pi/2,0))
    belt("V05_WIPES_UNWIND",11,43,7,1.0,f); box("V05_WIPES_WETTING",(17,43,2.2),(4,2.5,1.1),"green",f); belt("V05_WIPES_WEB",24,43,8,.9,f); box("V05_WIPES_FOLD_FRAME",(30,43,3.2),(3,2.4,3.8),"steel",f); box("V05_WIPES_CUT_STACK",(35,43,2.5),(3,2.5,2.5),"yellow",f); belt("V05_WIPES_POUCH",41,43,7,1.2,f); machine("V05_WIPES_SEAL",46,43,3,2.5,3.2,f,"red"); box("V05_WIPES_DISCHARGE",(50,43,2),(3,2,1.6),"white",f)

def etp():
    f="ETP / water treatment"; x,y=108,35; envelope("V05_ETP",x,y,38,32,8,f)
    for i,(xx,yy,r) in enumerate(((96,27,2.4),(104,27,2.2),(112,27,2.4))): box("V05_ETP_BUND"+str(i),(xx,yy,1.2),(6,6,.2),"yellow",f); tank("V05_ETP_TANK"+str(i),xx,yy,r,4.5,f,"teal")
    for i in range(3): tank("V05_ETP_FILTER"+str(i),99+i*3,37,.8,4.0,f,"stainless")
    for i in range(3): pipe("V05_ETP_HEADER"+str(i),(96+i*7,27,5.5),(96+i*7,37,5.5),.14,"yellow",f)
    box("V05_ETP_WALKWAY",(116,36,1.4),(2,18,.16),"steel",f); box("V05_ETP_DISCHARGE",(116,47,2),(2,1.5,1.4),"blue",f)

def fire():
    f="Fire pump house"
    for k,(x,y) in enumerate(((94,-5),(94,70))):
        envelope("V05_FIRE"+str(k),x,y,20,18,7,f)
        for i in range(2): machine("V05_FIRE_PUMP"+str(k)+"_"+str(i),x-3+i*6,y,2.6,2.0,2.0,f,"red")
        pipe("V05_FIRE_SUCTION"+str(k),(x-7,y+3,3),(x+7,y+3,3),.18,"stainless",f); pipe("V05_FIRE_HEADER"+str(k),(x-3,y,4),(x+3,y,4),.18,"yellow",f)
        for i in range(4): cyl("V05_FIRE_VALVE"+str(k)+"_"+str(i),(x-6+i*4,y+3,3),.3,.2,"red",f,20,(math.pi/2,0,0))
        box("V05_FIRE_PANEL"+str(k),(x+6,y-5,2.6),(1.1,.25,2.2),"blue",f)

def utilities():
    f="Utilities / engineering"; x,y=96,75; envelope("V05_UTIL",x,y,34,30,8,f)
    machine("V05_UTIL_COMPRESSOR",85,68,5,3,3.0,f,"blue"); tank("V05_UTIL_BOILER",96,68,2.0,4.5,f,"orange"); pipe("V05_UTIL_STEAM",96,68,96,82,.16,"yellow",f) if False else pipe("V05_UTIL_STEAM",(96,68,5.5),(96,82,5.5),.16,"yellow",f)
    for i in range(3): tank("V05_UTIL_RO"+str(i),106+i*2,68,.7,4,f,"stainless")
    box("V05_UTIL_RO_SKID",(108,72,1.3),(8,3,.25),"steel",f)
    for i in range(4): pipe("V05_UTIL_MANIFOLD"+str(i),(84+i*8,82,4.8),(84+i*8,82,6.5),.11,"teal",f)
    box("V05_UTIL_MAINT_BENCH",(88,84,2),(8,1,1.3),"wood",f)

def preserve_markers():
    # V05 records the evidence-only decision without changing the three V04 PASS models.
    for f,x,y in (("Caps and Trigger Assembly",52,31),("Micro-ingredient Weigh / Dispense",-5,50),("Production Hall / Wet Processing / process core",-5,-12)):
        box("V05_EVIDENCE_ANCHOR_"+f[:4].upper(),(x,y,1.08),(.2,.2,.12),"floor",f)

def main():
    before_blend, before_glb=sha(BLEND),sha(GLB)
    for fn in (admin,restaurant,clinic,training,wellness,security,gatehouse,glass,lambda:warehouse("RAW",-78,79,54,38,"Raw material warehouse / receiving"),lambda:warehouse("PACK",-10,79,58,45,"Packaging warehouse"),lambda:warehouse("FG",80,-51,52,24,"Finished goods warehouse / dispatch"),chemical,bottle,liquid,powder,toothpaste,wipes,etp,fire,utilities,preserve_markers): fn()
    scene=bpy.context.scene; scene["REV005_REMEDIATION_V05_STATUS"]="AWAITING_GPT_REMEDIATION_AUDIT_V05"; scene["REV005_REMEDIATION_V05_COLLECTION"]=COL; scene["REV005_REV004_FROZEN"]=True
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)); bpy.ops.export_scene.gltf(filepath=str(GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True)
    OUT.mkdir(parents=True,exist_ok=True)
    result={"status":"BUILT","revision":"REV005","collection":COL,"before_blend_sha256":before_blend,"before_glb_sha256":before_glb,"after_blend_sha256":sha(BLEND),"after_glb_sha256":sha(GLB),"object_count":len(C.objects),"blend":str(BLEND),"glb":str(GLB),"no_hiveai":not(ROOT/".hiveai").exists(),"no_rev006":not(ROOT/"3d/revisions/REV006").exists(),"no_tour":not any((ROOT/"output/rev005-interior-remediation-v05").glob("*.mp4"))}
    (OUT/"BUILD_RESULT.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
main()
