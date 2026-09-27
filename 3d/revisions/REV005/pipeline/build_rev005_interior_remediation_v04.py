import bpy, hashlib, json, math
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v04"
COL = "REV005_INTERIOR_REMEDIATION_V04"

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""): h.update(b)
    return h.hexdigest().upper()

def material(name, color, metal=0.0, rough=.4):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1); m.use_nodes = True
    bs = m.node_tree.nodes.get("Principled BSDF")
    if bs:
        bs.inputs["Base Color"].default_value = (*color, 1)
        bs.inputs["Metallic"].default_value = metal; bs.inputs["Roughness"].default_value = rough
    return m

M = {
    "steel": material("REV005_V04_STEEL", (.18,.24,.28), .85,.24),
    "stainless": material("REV005_V04_STAINLESS", (.62,.69,.72), .9,.18),
    "blue": material("REV005_V04_BLUE", (.02,.16,.52), .3,.28),
    "teal": material("REV005_V04_TEAL", (.01,.50,.60), .25,.24),
    "orange": material("REV005_V04_ORANGE", (.92,.24,.03), .15,.3),
    "yellow": material("REV005_V04_YELLOW", (.98,.57,.01), .08,.34),
    "green": material("REV005_V04_GREEN", (.03,.45,.20), .2,.3),
    "purple": material("REV005_V04_PURPLE", (.55,.07,.35), .2,.3),
    "white": material("REV005_V04_WHITE", (.88,.90,.91), .08,.3),
    "dark": material("REV005_V04_DARK", (.01,.016,.022), .3,.18),
    "wood": material("REV005_V04_WOOD", (.45,.21,.06), 0,.48),
    "warm": material("REV005_V04_WARM", (.94,.42,.06), .05,.38),
    "red": material("REV005_V04_RED", (.78,.03,.02), .05,.35),
    "soft": material("REV005_V04_SOFT", (.06,.50,.72), .05,.48),
    "glass": material("REV005_V04_GLASS", (.08,.44,.65), .35,.12),
    "floor": material("REV005_V04_FLOOR", (.25,.31,.35), .15,.34),
}

C = bpy.data.collections.get(COL)
if C:
    for o in list(C.objects): bpy.data.objects.remove(o, do_unlink=True)
else:
    C = bpy.data.collections.new(COL); bpy.context.scene.collection.children.link(C)

def link(o, facility):
    for c in list(o.users_collection): c.objects.unlink(o)
    C.objects.link(o); o["REV005_REMEDIATION_V04"] = True; o["facility"] = facility; return o

def mesh(name, verts, faces, loc, mat, facility):
    me = bpy.data.meshes.new(name + "_MESH"); me.from_pydata(verts, [], faces); me.update()
    o = link(bpy.data.objects.new(name, me), facility); o.location = loc; o.data.materials.append(M[mat]); return o

def box(name, loc, dims, mat, facility, rot=None):
    x,y,z = [v/2 for v in dims]
    vs=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]
    fs=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    o=mesh(name,vs,fs,loc,mat,facility)
    if rot: o.rotation_euler=rot
    return o

def cyl(name, loc, radius, depth, mat, facility, sides=20, rot=None):
    vs=[]
    for z in (-depth/2,depth/2):
        for i in range(sides):
            a=math.tau*i/sides; vs.append((radius*math.cos(a),radius*math.sin(a),z))
    fs=[tuple(range(sides-1,-1,-1)),tuple(range(sides,2*sides))]
    fs += [(i,(i+1)%sides,sides+(i+1)%sides,sides+i) for i in range(sides)]
    o=mesh(name,vs,fs,loc,mat,facility)
    if rot:o.rotation_euler=rot
    return o

def cone(name, loc, r1, r2, depth, mat, facility, sides=24):
    vs=[]
    for z,r in ((-depth/2,r1),(depth/2,r2)):
        for i in range(sides):
            a=math.tau*i/sides; vs.append((r*math.cos(a),r*math.sin(a),z))
    fs=[tuple(range(sides-1,-1,-1)),tuple(range(sides,2*sides))]
    fs += [(i,(i+1)%sides,sides+(i+1)%sides,sides+i) for i in range(sides)]
    return mesh(name,vs,fs,loc,mat,facility)

def pipe(name, a, b, radius, mat, facility):
    a,b=Vector(a),Vector(b); d=b-a
    o=cyl(name,(a+b)/2,radius,d.length,mat,facility,16); o.rotation_euler=d.to_track_quat("Z","Y").to_euler(); return o

def belt(name,x,y,length,width,facility,z=1.35):
    box(name+"_FRAME",(x,y,z),(length,width,.24),"stainless",facility)
    for i in range(8):
        xx=x-length/2+.6+i*(length-1.2)/7
        cyl(name+"_ROLLER_%02d"%i,(xx,y,z+.18),width*.4,.11,"dark",facility,16,(0,math.pi/2,0))
    box(name+"_GUARD_A",(x,y-width/2,z+.38),(length,.1,.62),"yellow",facility)
    box(name+"_GUARD_B",(x,y+width/2,z+.38),(length,.1,.62),"yellow",facility)

def wall_room(prefix,x,y,w,d,h,f):
    box(prefix+"_FLOOR",(x,y,1.05),(w,d,.18),"floor",f)
    box(prefix+"_BACK",(x,y+d/2,h/2),(w,.16,h),"white",f)
    box(prefix+"_LEFT",(x-w/2,y,h/2),(.16,d,h),"white",f)
    box(prefix+"_RIGHT",(x+w/2,y,h/2),(.16,d,h),"white",f)

def light(name,loc,f,mat="warm"):
    box(name+"_BODY",loc,(2.4,.3,.1),"white",f); box(name+"_GLOW",(loc[0],loc[1],loc[2]-.07),(1.8,.15,.04),mat,f)

def rack(prefix,x,y,levels, bays, f, mat="steel"):
    for b in range(bays):
        xx=x+b*2.2
        for z in range(levels):
            box(prefix+"_UPRIGHT_%02d_%02d"%(b,z),(xx,y,1.4+z*1.7),(.16,.18,3.1),mat,f)
            box(prefix+"_PALLET_%02d_%02d"%(b,z),(xx+0.9,y,1.4+z*1.7),(1.8,.9,.12),"wood",f)
            box(prefix+"_LOAD_%02d_%02d"%(b,z),(xx+0.9,y,1.85+z*1.7),(1.55,.72,.75),"white",f)
    for z in range(levels): box(prefix+"_BEAM_%02d"%z,(x+(bays-1)*1.1,y,2.65+z*1.7),(bays*2.2,.18,.16),mat,f)

def admin():
    f="Administration / HQ / R&D / QC"; x,y=-58,-64
    wall_room("V04_ADMIN",x,y,52,29,6.2,f)
    box("V04_ADMIN_RECEPTION",(-78,-51.5,2.2),(8,1.2,1.7),"wood",f)
    box("V04_ADMIN_RECEPTION_BACK",(-78,-53.0,3.9),(8,.22,3.1),"glass",f)
    for i in range(6): box("V04_ADMIN_OFFICE_POD_%02d"%i,(-70+i*5.4,-61,2.1),(3.8,3.0,1.35),"wood",f)
    box("V04_ADMIN_MEETING_TABLE",(-56,-55,2.15),(8,3,.25),"wood",f)
    for i in range(8): cyl("V04_ADMIN_MEETING_SEAT_%02d"%i,(-59.5+(i%4)*2.3,-53.0+(i//4)*4.0,1.75),.34,.7,"teal",f,16)
    box("V04_ADMIN_QC_LAB_BENCH",(-42,-70,2.0),(13,1.1,1.5),"stainless",f)
    for i in range(5):
        box("V04_ADMIN_QC_INSTRUMENT_%02d"%i,(-47+i*2.4,-69.3,3.0),(.8,.45,.55),"blue",f)
        cyl("V04_ADMIN_QC_SAMPLE_%02d"%i,(-47+i*2.4,-70.7,2.55),.18,.35,"red",f,16)
    rack("V04_ADMIN_QC_STORAGE",-38,-75,2,4,f,"steel")
    box("V04_ADMIN_LAB_PARTITION",(-42,-64,3.2),(.18,12,4.2),"glass",f)
    for i in range(7): light("V04_ADMIN_LIGHT_%02d"%i,(-80+i*7,-64,7.1),f)

def bottle():
    f="Bottle Blow Molding"; x,y=52,10
    # Add machine interfaces, safety cage, preform bins and air/service bridge to V03 line.
    box("V04_BLOW_PREFORM_BIN",(x-15,y+2,1.8),(2.2,2.0,1.5),"yellow",f)
    for i in range(4): cyl("V04_BLOW_PREFORM_BIN_%02d"%i,(x-15.7+i*.45,y+1.3,2.7),.14,.9,"teal",f,16)
    box("V04_BLOW_OVEN_SERVICE_DECK",(x-6.3,y-3.5,2.2),(6.5,.5,.18),"steel",f)
    for i in range(3): pipe("V04_BLOW_OVEN_DUCT_%02d"%i,(x-8+i*1.6,y+2.3,6.5),(x-8+i*1.6,y+2.3,8.1),.12,"stainless",f)
    for side in (-1,1):
        box("V04_BLOW_CAGE_SIDE_%s"%side,(x+1,y+3.0,4.2),(.12,6.0,5.8),"yellow",f)
    belt("V04_BLOW_PREFORM_TRANSFER",x-2,y+.7,4.5,1.0,f,1.45)
    box("V04_BLOW_BOTTLE_INSPECTION",(x+7.0,y+.8,3.6),(1.4,2.4,4.8),"white",f)
    for i in range(6): light("V04_BLOW_LIGHT_%02d"%i,(x-13+i*5.2,y-5.8,8.2),f)

def liquid():
    f="Liquid Filling / Packaging"; x,y=10,-2
    wall_room("V04_LIQUID",x,y,43,15,6.2,f)
    for i in range(4):
        box("V04_LIQUID_CAP_HOPPER_%02d"%i,(x-2+i*2.0,y+2.5,5.2),(.9,1.1,1.4),"purple",f)
        pipe("V04_LIQUID_CAP_DROP_%02d"%i,(x-2+i*2.0,y+2.5,4.5),(x-2+i*2.0,y,3.5),.08,"teal",f)
    for i in range(3):
        cyl("V04_LIQUID_LABEL_REEL_%02d"%i,(x+8+i*1.0,y+2.2,3.5),.65,.24,"white",f,24,(0,math.pi/2,0))
    box("V04_LIQUID_ROBOT_BASE",(x+12,y+2.4,1.9),(1.5,1.5,.8),"steel",f)
    pipe("V04_LIQUID_ROBOT_ARM",(x+12,y+2.4,2.4),(x+14,y,3.4),.15,"yellow",f)
    box("V04_LIQUID_CASE_MAGAZINE",(x+16,y+2.6,2.5),(3.0,1.6,2.8),"orange",f)
    for i in range(6): light("V04_LIQUID_LIGHT_%02d"%i,(x-17+i*6.5,y-5.8,7.2),f)

def paste():
    f="Toothpaste Production"; x,y=-12,43
    wall_room("V04_PASTE",x,y,38,15,6.2,f)
    cyl("V04_PASTE_BLEND_JACKET",(x-13,y+2.4,3.4),2.4,4.4,"green",f,32)
    for i in range(3): pipe("V04_PASTE_JACKET_PIPE_%02d"%i,(x-14+i*1.2,y+2.4,5.0),(x-14+i*1.2,y+2.4,6.7),.1,"teal",f)
    for i in range(8):
        cyl("V04_PASTE_TUBE_PUCK_%02d"%i,(x+5+i*1.25,y-.8,2.0),.28,.16,"yellow",f,20)
        cyl("V04_PASTE_TUBE_%02d"%i,(x+5+i*1.25,y-.8,2.5),.13,1.0,"white",f,16)
    box("V04_PASTE_TUBE_MAGAZINE_RACK",(x+2,y+2.8,3.0),(3.4,.4,4.0),"steel",f)
    box("V04_PASTE_CRIMPER_GUARD",(x+10,y+2.0,3.0),(2.6,1.0,3.8),"purple",f)
    box("V04_PASTE_CARTON_CASE_STAGE",(x+18,y+2.0,2.0),(5,2.6,1.2),"wood",f)
    for i in range(6): light("V04_PASTE_LIGHT_%02d"%i,(x-16+i*6.0,y-5.8,7.2),f)

def wipes():
    f="Wet Wipes Production"; x,y=22,43
    wall_room("V04_WIPES",x,y,47,15,6.2,f)
    box("V04_WIPES_WEB_TABLE",(x-7,y-1.9,2.5),(10,.35,.16),"white",f)
    for i in range(6): pipe("V04_WIPES_WEB_GUIDE_%02d"%i,(x-15+i*2.0,y-1.8,4.8),(x-14+i*2.0,y-1.8,4.2),.07,"white",f)
    box("V04_WIPES_FOLDING_PLOW_FRAME",(x-3,y+2.5,3.2),(2.4,1.2,3.8),"steel",f)
    for i in range(3): box("V04_WIPES_FOLDING_BLADE_%02d"%i,(x-3+i*.45,y-2.1,3.0),(.12,2.0,1.8),"yellow",f)
    box("V04_WIPES_POUCH_FILM_PATH",(x+9,y-2.0,4.5),(8,.12,.12),"white",f)
    box("V04_WIPES_SEALING_JAWS",(x+13,y-1.9,3.1),(2.0,.8,2.6),"red",f)
    for i in range(6): light("V04_WIPES_LIGHT_%02d"%i,(x-19+i*7,y-5.8,7.2),f)

def glass():
    f="Central Glass Deck Command / Training / Café Gallery"; x=70
    # Make the deck read as an enclosed interior rather than a line of isolated props.
    box("V04_GLASS_DECK_FLOOR",(x,24,1.05),(9.5,45,.18),"floor",f)
    box("V04_GLASS_DECK_LEFT_WALL",(x-4.7,24,8.5),(.16,45,15),"glass",f)
    box("V04_GLASS_DECK_RIGHT_WALL",(x+4.7,24,8.5),(.16,45,15),"glass",f)
    box("V04_GLASS_DECK_COMMAND_WALL",(x,36.8,8.5),(8.2,.18,10.5),"blue",f)
    for i in range(4):
        box("V04_GLASS_DECK_COMMAND_CONSOLE_%02d"%i,(x-3.0+i*2.0,33.8,2.2),(1.3,1.0,1.4),"steel",f)
        box("V04_GLASS_DECK_COMMAND_MONITOR_%02d"%i,(x-3.0+i*2.0,33.3,4.1),(1.1,.12,1.0),"teal",f)
    box("V04_GLASS_DECK_TRAINING_TABLE",(x,23.5,2.0),(6.0,2.0,.22),"wood",f)
    for i in range(8):
        cyl("V04_GLASS_DECK_TRAINING_SEAT_%02d"%i,(x-3.0+(i%4)*2.0,21.8+(i//4)*3.4,1.5),.32,.65,"purple",f,16)
    box("V04_GLASS_DECK_CAFE_COUNTER",(x,5.8,2.2),(8.0,1.0,1.7),"wood",f)
    box("V04_GLASS_DECK_CAFE_BACKBAR",(x,7.1,5.0),(8.0,.18,5.2),"blue",f)
    box("V04_GLASS_DECK_CEILING_BEAM",(x,24,16.9),(9.5,45,.25),"steel",f)
    for yy in (4,14,24,34,44): light("V04_GLASS_DECK_LIGHT_%02d"%yy,(x,yy,16.5),f)
    for yy in (11,28): box("V04_GLASS_DECK_ZONE_PARTITION_%02d"%yy,(x,yy,12.5),(7.6,.16,3.0),"glass",f)
    for i in range(6): cyl("V04_GLASS_DECK_CAFE_STOOL_%02d"%i,(x-2.5+i*.95,4.0,10.8),.28,.7,"purple",f,16)
    for i in range(3): box("V04_GLASS_DECK_CAFE_APPLIANCE_%02d"%i,(x-2+i*1.5,5.3,12.1),(.7,.4,.8),"stainless",f)
    box("V04_GLASS_DECK_COMMAND_RISER",(x,34.8,10.4),(8,4,.18),"steel",f)

def restaurant():
    f="Restaurant / POVU Café / kitchen"; x,y=5,-69
    wall_room("V04_RESTAURANT",x,y,45,25,6.2,f)
    box("V04_RESTAURANT_PASS_WINDOW",(5,-75.9,3.8),(14,.22,1.5),"warm",f)
    for i in range(4):
        box("V04_RESTAURANT_KITCHEN_APPLIANCE_%02d"%i,(-10+i*8,-78.5,2.5),(3.5,1.0,2.2),"stainless",f)
        cyl("V04_RESTAURANT_EXHAUST_%02d"%i,(-10+i*8,-78.3,4.7),.42,1.2,"steel",f,20)
    box("V04_RESTAURANT_DISHWASH",(20,-78.5,2.3),(3.2,1.0,1.8),"blue",f)
    for i in range(4):
        box("V04_RESTAURANT_TABLE_RUNNER_%02d"%i,(-12+i*10,-64,2.18),(2.4,.22,.05),"warm",f)
        light("V04_RESTAURANT_LIGHT_%02d"%i,(-12+i*10,-69,7.2),f)

def finished_goods():
    f="Finished Goods Warehouse / Dispatch"; x,y=80,-51
    wall_room("V04_FG",x,y,48,22,8.0,f)
    for row in (-58,-51,-44): rack("V04_FG_RACK_%s"%row,60,row,3,9,f,"steel")
    for i in range(6): box("V04_FG_STAGE_PALLET_%02d"%i,(71+i*2.1,-40.5,1.25),(1.7,1.4,.18),"wood",f)
    for i in range(6): box("V04_FG_STAGE_CASE_%02d"%i,(71+i*2.1,-40.5,1.8),(1.2,1.0,1.0),"white",f)
    box("V04_FG_DISPATCH_DESK",(96,-41.5,2.0),(4,1.0,1.4),"wood",f)
    box("V04_FG_LOADING_DOCK",(80,-40.1,3.2),(12,.18,4.2),"orange",f)
    for i in range(3):
        box("V04_FG_AMR_%02d"%i,(85+i*4,-47,1.0),(1.5,2.2,.4),"blue",f)
        cyl("V04_FG_AMR_WHEEL_%02d"%i,(85+i*4,-48.1,.85),.25,.15,"dark",f,16,(math.pi/2,0,0))
    for i in range(6): light("V04_FG_LIGHT_%02d"%i,(60+i*8,-51,9),f)

def raw_material():
    f="Raw Material Warehouse / Receiving"; x,y=-78,79
    wall_room("V04_RM",x,y,50,36,8.0,f)
    for row in (67,75,83,91): rack("V04_RM_RACK_%s"%row,-99,row,3,9,f,"steel")
    for i in range(6):
        box("V04_RM_RECEIVING_PALLET_%02d"%i,(-98+i*3.2,96,1.25),(2.2,1.8,.18),"wood",f)
        box("V04_RM_RECEIVING_SACK_%02d"%i,(-98+i*3.2,96,2.0),(1.2,1.0,1.2),"white",f)
    box("V04_RM_RECEIVING_DOCK",(-78,96.6,3.2),(16,.18,4.2),"orange",f)
    box("V04_RM_SAMPLING_BOOTH",(-57,89,2.2),(4,3,2.2),"glass",f)
    for i in range(5): light("V04_RM_LIGHT_%02d"%i,(-98+i*10,79,9),f)

def etp():
    f="ETP / Water Treatment"; x,y=108,35
    wall_room("V04_ETP",x,y,36,30,7.0,f)
    for i,(xx,yy,rr) in enumerate(((96,26,2.3),(105,26,2.0),(114,26,2.5))):
        cyl("V04_ETP_TANK_%02d"%i,(xx,yy,3.0),rr,4.0,"teal",f,32)
        box("V04_ETP_TANK_LID_%02d"%i,(xx,yy,5.15),(1.2,1.2,.25),"steel",f)
    for i in range(3): cyl("V04_ETP_FILTER_%02d"%i,(99+i*2.5,37,3.4),.75,4.2,"stainless",f,24)
    for i in range(3): pipe("V04_ETP_HEADER_%02d"%i,(96+i*6,26,5.2),(96+i*6,37,5.2),.12,"yellow",f)
    for i in range(3):
        box("V04_ETP_PUMP_SKID_%02d"%i,(99+i*5,45,1.8),(3.0,1.5,1.0),"blue",f)
        cyl("V04_ETP_PUMP_%02d"%i,(99+i*5,45,2.7),.55,.9,"orange",f,24,(math.pi/2,0,0))
    box("V04_ETP_OPERATOR_PLATFORM",(117,36,1.4),(2.0,18,.14),"steel",f)
    for i in range(5): light("V04_ETP_LIGHT_%02d"%i,(94+i*7,35,8.0),f)

def fire_pump():
    f="Fire Pump House"
    for k,(x,y) in enumerate(((94,-5),(94,70))):
        wall_room("V04_FIRE_%02d"%k,x,y,18,16,6.5,f)
        for i in range(2):
            cyl("V04_FIRE_PUMP_%02d_%02d"%(k,i),(x-3+i*6,y-1,2.0),.85,2.2,"red",f,28,(math.pi/2,0,0))
            box("V04_FIRE_PUMP_BASE_%02d_%02d"%(k,i),(x-3+i*6,y-1,1.35),(3.0,1.7,.25),"steel",f)
        pipe("V04_FIRE_SUCTION_%02d"%k,(x-7,y+2.5,2.4),(x+7,y+2.5,2.4),.18,"stainless",f)
        pipe("V04_FIRE_DISCHARGE_%02d"%k,(x-3,y-1,3.0),(x-3,y+3.8,4.8),.16,"yellow",f)
        pipe("V04_FIRE_DISCHARGE2_%02d"%k,(x+3,y-1,3.0),(x+3,y+3.8,4.8),.16,"yellow",f)
        for i in range(4): cyl("V04_FIRE_VALVE_%02d_%02d"%(k,i),(x-6+i*4,y+2.5,2.4),.32,.18,"red",f,20,(math.pi/2,0,0))
        box("V04_FIRE_PANEL_%02d"%k,(x+6,y-5,2.6),(1.1,.25,2.0),"blue",f)
        for i in range(3): light("V04_FIRE_LIGHT_%02d_%02d"%(k,i),(x-6+i*6,y,7.5),f)

def clinic():
    f="Occupational Health / First Aid"; x,y=-18,-94
    wall_room("V04_CLINIC",x,y,22,16,5.8,f)
    box("V04_CLINIC_RECEPTION",(-25,-100.5,2.1),(5,1.0,1.5),"wood",f)
    box("V04_CLINIC_PRIVACY",(-13,-94,2.7),(.18,8,3.0),"glass",f)
    box("V04_CLINIC_EXAM_BED",(-11,-99,1.6),(2.2,5.0,.55),"white",f)
    box("V04_CLINIC_EXAM_BACK",(-11,-101.2,2.7),(2.2,.18,1.4),"blue",f)
    box("V04_CLINIC_TREATMENT_CART",(-8,-97,2.0),(1.2,.8,1.3),"stainless",f)
    for i in range(3): box("V04_CLINIC_MEDICAL_CABINET_%02d"%i,(-25+i*2.0,-88.0,2.2),(1.5,.5,2.0),"white",f)
    for i in range(4): cyl("V04_CLINIC_WAIT_SEAT_%02d"%i,(-25+i*1.7,-91,1.7),.32,.7,"teal",f,16)
    box("V04_CLINIC_SINK",(-27,-96,2.0),(1.6,.6,1.1),"stainless",f)
    for i in range(4): light("V04_CLINIC_LIGHT_%02d"%i,(-26+i*5,-94,6.8),f)

def utilities():
    f="Utilities / engineering"; x,y=96,75
    wall_room("V04_UTIL",x,y,32,28,7.5,f)
    cyl("V04_UTIL_COMPRESSOR",(85,68,2.4),1.5,3.0,"blue",f,28,(math.pi/2,0,0))
    box("V04_UTIL_COMPRESSOR_SKID",(85,68,1.25),(5,3,.25),"steel",f)
    cyl("V04_UTIL_BOILER",(96,68,3.4),1.8,4.2,"orange",f,28)
    pipe("V04_UTIL_STEAM_HEADER",(96,68,5.6),(96,82,5.6),.16,"yellow",f)
    for i in range(3): cyl("V04_UTIL_RO_COLUMN_%02d"%i,(106+i*2.0,68,3.0),.65,3.8,"stainless",f,24)
    box("V04_UTIL_RO_SKID",(108,70,1.3),(7,3,.25),"steel",f)
    for i in range(4): pipe("V04_UTIL_MANIFOLD_%02d"%i,(84+i*8,82,4.8),(84+i*8,82,6.5),.10,"teal",f)
    box("V04_UTIL_MAINT_BENCH",(88,84,2.0),(8,1.0,1.3),"wood",f)
    for i in range(5): box("V04_UTIL_TOOL_%02d"%i,(85+i*1.4,83.3,2.8),(.45,.25,.55),"yellow",f)
    for i in range(5): light("V04_UTIL_LIGHT_%02d"%i,(84+i*6,75,8.5),f)

def main():
    before_blend, before_glb = sha(BLEND), sha(GLB)
    for fn in (admin,bottle,liquid,paste,wipes,glass,restaurant,finished_goods,raw_material,etp,fire_pump,clinic,utilities): fn()
    scene=bpy.context.scene
    scene["REV005_REMEDIATION_V04_STATUS"]="AWAITING_GPT_REMEDIATION_AUDIT_V04"
    scene["REV005_REMEDIATION_V04_COLLECTION"]=COL
    scene["REV005_REV004_FROZEN"]=True
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True)
    OUT.mkdir(parents=True,exist_ok=True)
    result={"status":"BUILT","revision":"REV005","collection":COL,"before_blend_sha256":before_blend,"before_glb_sha256":before_glb,"after_blend_sha256":sha(BLEND),"after_glb_sha256":sha(GLB),"object_count":len(C.objects),"blend":str(BLEND),"glb":str(GLB),"no_hiveai":not (ROOT/".hiveai").exists(),"no_rev006":True,"no_tour":True}
    (OUT/"BUILD_RESULT.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
main()
