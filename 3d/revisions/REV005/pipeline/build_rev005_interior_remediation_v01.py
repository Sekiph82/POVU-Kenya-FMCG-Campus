import bpy, hashlib, json, math, os
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d" / "revisions" / "REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT = ROOT / "output" / "rev005-interior-remediation-v01"
COL_NAME = "REV005_INTERIOR_REMEDIATION_V01"

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest().upper()

def mat(name, color, metallic=0.0, rough=0.45):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=(*color,1)
    m.use_nodes=True
    bsdf=m.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value=(*color,1)
        bsdf.inputs["Metallic"].default_value=metallic
        bsdf.inputs["Roughness"].default_value=rough
    return m

M={
 "steel":mat("REV005_RM_STEEL",(0.18,0.24,0.28),0.8,0.28),
 "stainless":mat("REV005_RM_STAINLESS",(0.55,0.62,0.65),0.9,0.2),
 "blue":mat("REV005_RM_PROCESS_BLUE",(0.04,0.22,0.55),0.35,0.3),
 "green":mat("REV005_RM_PROCESS_GREEN",(0.05,0.48,0.28),0.25,0.32),
 "yellow":mat("REV005_RM_SAFETY_YELLOW",(0.95,0.55,0.03),0.1,0.35),
 "red":mat("REV005_RM_FIRE_RED",(0.72,0.04,0.025),0.25,0.3),
 "white":mat("REV005_RM_CLEAN_WHITE",(0.82,0.86,0.88),0.1,0.35),
 "dark":mat("REV005_RM_DARK",(0.015,0.025,0.035),0.2,0.22),
 "cyan":mat("REV005_RM_CYAN",(0.02,0.55,0.72),0.4,0.25),
 "magenta":mat("REV005_RM_MAGENTA",(0.65,0.08,0.32),0.25,0.3),
 "wood":mat("REV005_RM_WOOD",(0.38,0.18,0.06),0.0,0.55),
}

def collection():
    c=bpy.data.collections.get(COL_NAME)
    if c:
        for o in list(c.objects): bpy.data.objects.remove(o,do_unlink=True)
    else:
        c=bpy.data.collections.new(COL_NAME); bpy.context.scene.collection.children.link(c)
    return c
C=collection()

def link(obj):
    for cc in list(obj.users_collection): cc.objects.unlink(obj)
    C.objects.link(obj)
    obj["REV005_REMEDIATION_V01"]=True
    return obj

def box(name, loc, dims, material="steel", facility=""):
    x,y,z=[v/2 for v in dims]
    verts=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]
    faces=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(verts,[],faces); me.update()
    o=link(bpy.data.objects.new(name,me)); o.location=loc
    o.data.materials.append(M[material]); o["facility"]=facility; o["functional_role"]=name
    return o

def cyl(name, loc, radius, depth, material="stainless", facility="", vertices=24):
    vs=[]
    for z in (-depth/2,depth/2):
        for i in range(vertices):
            a=math.tau*i/vertices; vs.append((radius*math.cos(a),radius*math.sin(a),z))
    fs=[]
    fs.append(tuple(range(vertices-1,-1,-1))); fs.append(tuple(range(vertices,2*vertices)))
    for i in range(vertices): j=(i+1)%vertices; fs.append((i,j,vertices+j,vertices+i))
    me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(vs,[],fs); me.update()
    o=link(bpy.data.objects.new(name,me)); o.location=loc; o.data.materials.append(M[material]); o["facility"]=facility; o["functional_role"]=name
    return o

def pipe(name,a,b,r=0.12,material="stainless",facility=""):
    a,b=Vector(a),Vector(b); d=b-a
    o=cyl(name,(a+b)/2,r,d.length,material,facility,16); o.rotation_euler=d.to_track_quat("Z","Y").to_euler(); return o

def machine(name,x,y,w,d,h,facility,material="steel"):
    body=box(name+"_FRAME",(x,y,1.25+h/2),(w,d,h),material,facility)
    box(name+"_CONTROL",(x,y-d/2-0.09,1.75+h*0.48),(w*0.38,0.12,0.55),"dark",facility)
    return body

def conveyor(name,x,y,length,width,facility,material="steel"):
    box(name+"_BED",(x,y,1.25),(length,width,0.22),material,facility)
    for i in range(5):
        xx=x-length/2+0.6+i*(length-1.2)/4
        cyl(name+f"_ROLLER_{i}",(xx,y,1.42),width*0.42,0.12,"dark",facility,16).rotation_euler[1]=math.pi/2
    box(name+"_GUARD_A",(x,y-width/2,1.72),(length,0.08,0.65),"yellow",facility)
    box(name+"_GUARD_B",(x,y+width/2,1.72),(length,0.08,0.65),"yellow",facility)

def tank(name,x,y,r,h,facility,material="stainless"):
    cyl(name+"_VESSEL",(x,y,1.25+h/2),r,h,material,facility,32)
    cyl(name+"_LID",(x,y,1.25+h+0.12),r*1.05,0.24,"steel",facility,32)
    pipe(name+"_OUTLET",(x,y-r,1.25+h*0.35),(x+2,y-r,1.25+h*0.35),0.12,"stainless",facility)
    box(name+"_MOTOR",(x,y,1.25+h+0.55),(0.55,0.55,0.65),"blue",facility)

def plaque(name,x,y,z,facility):
    # Small non-text visual identifier only; function is conveyed by geometry.
    return box(name,(x,y,z),(2.6,0.12,0.45),"yellow",facility)

def bounds(name):
    o=bpy.data.objects.get(name)
    if not o: return None
    pts=[o.matrix_world @ Vector(c) for c in o.bound_box]
    lo=Vector((min(p.x for p in pts),min(p.y for p in pts),min(p.z for p in pts))); hi=Vector((max(p.x for p in pts),max(p.y for p in pts),max(p.z for p in pts)))
    return lo,hi

def blow():
    f="Bottle Blow Molding"; x,y=52,10
    machine("RM_BLOW_MOULDING_PRESS",x-6,y,4.2,3.8,4.8,f,"blue")
    box("RM_BLOW_MOULDING_MOLD_STATION",(x-6,y-2.0,3.4),(2.4,0.3,2.8),"yellow",f)
    box("RM_BLOW_PREFORM_HOPPER",(x-11,y+2.0,3.8),(2.5,2.2,4.5),"stainless",f)
    pipe("RM_BLOW_HOPPER_FEED",(x-9.7,y+2,5.9),(x-7,y+0.8,5.5),0.22,"cyan",f)
    box("RM_BLOW_HEATER_COLUMN",(x-2,y+2,3.0),(1.5,1.4,3.6),"red",f)
    conveyor("RM_BLOW_BOTTLE_OUTFEED",x+4,y-0.5,10,1.7,f,"stainless")
    for i in range(6): cyl(f"RM_BLOW_PREFORM_{i}",(x-3+i*0.9,y-0.5,2.1),0.12,0.7,"cyan",f,16)
    plaque("RM_BLOW_PROCESS_PANEL",x-1,y+3.2,5.8,f)

def caps():
    f="Caps and Trigger Assembly"; x,y=52,31
    cyl("RM_CAPS_ROTARY_BOWL",(x-7,y+2.1,2.15),2.2,0.35,"stainless",f,32)
    cyl("RM_CAPS_BOWL_CENTER",(x-7,y+2.1,2.6),0.32,0.9,"blue",f,24)
    pipe("RM_CAPS_FEED_TRACK",(x-5.2,y+2.1,2.3),(x-2,y+0.4,2.3),0.18,"yellow",f)
    box("RM_TRIGGER_FEEDER",(x-7,y-2.3,2.6),(3.2,1.8,2.8),"magenta",f)
    conveyor("RM_CAP_TRIGGER_ASSEMBLY_LINE",x+4,y,13,1.8,f,"stainless")
    for i in range(4):
        box(f"RM_TRIGGER_PICK_PLACE_{i}",(x+0.2+i*2.3,y,2.7),(0.6,1.2,2.0),"blue",f)
        cyl(f"RM_CAP_FEEDER_{i}",(x+0.2+i*2.3,y+1.1,3.0),0.3,0.5,"yellow",f,20)
    box("RM_CAPS_REJECT_STATION",(x+10,y,2.0),(1.0,2.0,1.5),"red",f)

def lv():
    f="Electrical / LV-MV Room"; x,y=111,61
    for i in range(5):
        px=x-4+i*2
        box(f"RM_LV_SWITCHGEAR_{i}",(px,y+1.2,2.75),(1.45,1.2,3.4),"dark",f)
        box(f"RM_LV_PANEL_DOOR_{i}",(px,y+0.55,2.75),(1.0,0.08,2.4),"steel",f)
        box(f"RM_LV_BREAKER_WINDOW_{i}",(px,y+0.49,3.0),(0.38,0.05,0.75),"cyan",f)
        pipe(f"RM_LV_CABLE_{i}",(px,y+1.9,4.5),(px,y+1.9,5.4),0.09,"red",f)
    box("RM_LV_BUSBAR_TRUNK",(x,y+1.9,5.5),(9.0,0.18,0.18),"red",f)
    box("RM_LV_SERVICE_CLEARANCE",(x,y-1.5,1.36),(8.5,1.0,0.05),"yellow",f)
    box("RM_LV_REMOTE_SERVICE_PANEL",(x+3,y-1.0,2.4),(1.4,0.5,2.2),"blue",f)

def welfare():
    f="Employee Changing / Shower / Locker Support"
    for i,x in enumerate((23,27,31,35,39)):
        box(f"RM_WELFARE_LOCKER_BANK_{i}",(x,-77.0,2.5),(3.0,0.55,2.5),"steel",f)
        for j in range(3): box(f"RM_WELFARE_LOCKER_DOOR_{i}_{j}",(x-0.9+j*0.9,-77.33,2.5),(0.7,0.06,1.95),"blue",f)
    for i,x in enumerate((24,29,34,39)):
        box(f"RM_WELFARE_SHOWER_BACK_{i}",(x,-66.25,2.6),(3.2,0.12,2.8),"white",f)
        box(f"RM_WELFARE_SHOWER_SIDE_A_{i}",(x-1.54,-65.1,2.6),(0.12,2.3,2.8),"white",f)
        box(f"RM_WELFARE_SHOWER_SIDE_B_{i}",(x+1.54,-65.1,2.6),(0.12,2.3,2.8),"white",f)
        box(f"RM_WELFARE_SHOWER_OPEN_{i}",(x,-63.92,2.7),(1.5,0.05,2.4),"cyan",f)
        cyl(f"RM_WELFARE_SHOWER_HEAD_{i}",(x,-64.2,4.3),0.13,0.35,"stainless",f,16)
        box(f"RM_WELFARE_DRAIN_{i}",(x,-64.0,1.31),(0.65,0.18,0.03),"dark",f)
    box("RM_WELFARE_CLEAN_ENTRY",(30,-70.0,1.5),(16.0,0.16,2.6),"green",f)
    box("RM_WELFARE_DIRTY_ENTRY",(30,-73.0,1.5),(16.0,0.16,2.6),"yellow",f)
    bench("RM_WELFARE_CHANGE_BENCH",30,-74.4,10,f)

def bench(name,x,y,w,f):
    box(name+"_SEAT",(x,y,1.8),(w,0.75,0.18),"wood",f)
    for dx in (-w/2+0.4,w/2-0.4): box(name+"_LEG"+str(dx),(x+dx,y,1.45),(0.12,0.5,0.65),"steel",f)

def fire_pump():
    f="Fire Pump House"; x,y=76,72
    for i,dx in enumerate((-3,0,3)):
        cyl(f"RM_FIRE_PUMP_{i}_MOTOR",(x+dx,y,2.2),0.85,1.6,"red",f,28)
        box(f"RM_FIRE_PUMP_{i}_BASE",(x+dx,y,1.42),(2.0,1.3,0.22),"steel",f)
        pipe(f"RM_FIRE_PUMP_{i}_SUCTION",(x+dx,y-0.85,2.0),(x+dx,y-2.8,2.0),0.18,"red",f)
        pipe(f"RM_FIRE_PUMP_{i}_DISCHARGE",(x+dx,y+0.85,2.7),(x+dx,y+2.6,2.7),0.18,"red",f)
    pipe("RM_FIRE_MANIFOLD",(x-3,y+2.6,2.7),(x+3,y+2.6,2.7),0.25,"red",f)
    box("RM_FIRE_CONTROLLER",(x+4.2,y,2.4),(1.2,0.7,2.2),"red",f)
    box("RM_FIRE_SERVICE_ACCESS",(x,y-3.4,1.34),(9.0,0.55,0.06),"yellow",f)

def glass():
    f="Central Glass Deck Command / Training / Café Gallery"; x=70
    for y in (4,14,24,34): box(f"RM_GLASS_COMMAND_SCREEN_{y}",(x-1.5,y,11.0),(0.12,4.0,2.0),"cyan",f)
    for y in (7,18):
        box(f"RM_GLASS_TRAINING_TABLE_{y}",(x,y,10.4),(4.8,2.0,0.22),"wood",f)
        for dx in (-1.7,1.7):
            for dy in (-1.2,1.2): cyl(f"RM_GLASS_TRAINING_CHAIR_{y}_{dx}_{dy}",(x+dx,y+dy,10.0),0.28,0.5,"blue",f,16)
    box("RM_GLASS_COMMAND_CONSOLE",(x,29,10.65),(6.0,1.0,1.2),"blue",f)
    for i,y in enumerate((27.3,28.4,29.5,30.6)): box(f"RM_GLASS_COMMAND_MONITOR_{i}",(x-2.0+i*1.3,28.3,11.5),(0.9,0.12,0.7),"dark",f)
    box("RM_GLASS_CAFE_COUNTER",(x,40,10.7),(6.0,1.2,1.5),"wood",f)
    for i in range(4): cyl(f"RM_GLASS_CAFE_STOOL_{i}",(x-2.2+i*1.45,38.7,10.1),0.3,0.8,"yellow",f,16)

def liquid():
    f="Liquid Filling / Packaging"; x,y=10,-2
    conveyor("RM_LIQUID_BOTTLE_CONVEYOR",x,y,38,2.0,f,"stainless")
    cyl("RM_LIQUID_FILLER_CAROUSEL",(x-8,y,2.15),2.8,0.5,"blue",f,32)
    for i in range(8):
        a=i*math.tau/8; cyl(f"RM_LIQUID_FILL_NOZZLE_{i}",(x-8+2.2*math.cos(a),y+2.2*math.sin(a),2.3),0.12,1.3,"cyan",f,16)
    machine("RM_LIQUID_CAPPER",x+4,y,2.2,2.1,2.2,f,"steel")
    machine("RM_LIQUID_LABELER",x+11,y,2.2,1.8,2.1,f,"green")
    machine("RM_LIQUID_CASE_PACKER",x+17,y,2.4,2.4,2.5,f,"blue")
    for i in range(5): box(f"RM_LIQUID_PRODUCT_{i}",(x-14+i*2.3,y,2.0),(0.55,0.55,1.0),"cyan",f)

def weigh():
    f="Micro-ingredient Weigh / Dispense"; x,y=-5,50
    box("RM_WEIGH_BOOTH",(x,y+2.2,2.8),(8.0,4.2,3.2),"white",f)
    box("RM_WEIGH_SCALE_TABLE",(x,y-1.4,1.8),(6.0,1.0,1.2),"steel",f)
    for i,dx in enumerate((-2,-0.7,0.7,2)):
        box(f"RM_WEIGH_BIN_{i}",(x+dx,y+2.2,4.4),(0.9,1.0,1.2),"blue",f)
        cyl(f"RM_WEIGH_HOPPER_{i}",(x+dx,y+2.2,5.4),0.34,0.7,"stainless",f,20)
    box("RM_WEIGH_BALANCE",(x,y-1.9,2.7),(1.2,0.7,0.7),"cyan",f)
    box("RM_WEIGH_TRANSFER_CART",(x+5,y-0.5,1.7),(1.8,1.2,1.0),"yellow",f)

def powder():
    f="Powder Handling / Packing"; x,y=-48,43
    box("RM_POWDER_BAG_DUMP",(x-9,y,2.7),(3.6,3.2,3.1),"steel",f)
    box("RM_POWDER_DUST_HOOD",(x-9,y,4.7),(4.0,3.5,0.35),"yellow",f)
    pipe("RM_POWDER_AUGER",(x-6.8,y,3.1),(x-2,y,3.1),0.32,"stainless",f)
    tank("RM_POWDER_HOPPER",x,y,1.7,3.4,f,"stainless")
    machine("RM_POWDER_VFFS_BAGGER",x+6,y,2.6,2.4,3.2,f,"blue")
    conveyor("RM_POWDER_PACKOUT",x+13,y,10,1.7,f,"stainless")
    for i in range(4): box(f"RM_POWDER_BAG_{i}",(x+9+i*1.2,y,2.0),(0.65,0.5,1.0),"white",f)

def wet_process():
    f="Production Hall / Wet Processing"; x,y=0,24
    for i,dx in enumerate((-22,-10,2,14,26)):
        tank(f"RM_WET_MIX_TANK_{i}",x+dx,y,2.7,5.8,f,"stainless")
        box(f"RM_WET_PLATFORM_{i}",(x+dx,y,1.45),(6.8,6.0,0.18),"steel",f)
        for sx in (-2.8,2.8):
            for sy in (-2.4,2.4): box(f"RM_WET_RAIL_{i}_{sx}_{sy}",(x+dx+sx,y+sy,3.1),(0.12,0.12,3.3),"yellow",f)
    pipe("RM_WET_TRANSFER_MANIFOLD",(-22,y+3.2,6.0),(26,y+3.2,6.0),0.35,"blue",f)
    box("RM_WET_CIP_SKID",(40,y,2.8),(7.0,4.0,3.1),"green",f)
    for i in range(3): pipe(f"RM_WET_CIP_PIPE_{i}",(37,y-1.2+i*1.2,4),(29,y-1.2+i*1.2,6),0.15,"green",f)
    conveyor("RM_WET_PROCESS_OUTFEED",0,y-9,46,2.0,f,"stainless")

def reception():
    f="Security / Reception / Visitor Arrival"; x,y=-58,-84
    box("RM_RECEPTION_SECURITY_DESK",(x,y+2,1.8),(7.0,1.2,1.4),"blue",f)
    box("RM_RECEPTION_CHECKIN_SCREEN",(x,y+1.3,3.0),(1.2,0.12,0.9),"cyan",f)
    for i,dx in enumerate((-5,-2,2,5)): cyl(f"RM_RECEPTION_VISITOR_SEAT_{i}",(x+dx,y-2.4,1.7),0.45,0.7,"wood",f,16)
    for i in range(3):
        box(f"RM_RECEPTION_TURNSTILE_{i}",(x-5+i*5,y+4.0,2.2),(0.7,1.6,2.0),"steel",f)
        pipe(f"RM_RECEPTION_TURNSTILE_ARM_{i}",(x-5+i*5,y+3.2,2.0),(x-5+i*5,y+4.6,2.0),0.08,"yellow",f)
    box("RM_RECEPTION_CCTV_WALL",(x,y+5.3,3.4),(8.0,0.15,2.6),"dark",f)
    for i in range(4): box(f"RM_RECEPTION_CCTV_{i}",(x-2.8+i*1.8,y+5.18,3.5),(1.4,0.06,0.8),"cyan",f)

def gatehouse():
    f="Security Gatehouse"; x,y=96,-106
    box("RM_GATEHOUSE_CONTROL_DESK",(x,y,1.75),(6.0,1.1,1.4),"blue",f)
    for i in range(3): box(f"RM_GATEHOUSE_MONITOR_{i}",(x-2+i*2,y-0.7,3.1),(1.3,0.12,0.8),"cyan",f)
    box("RM_GATEHOUSE_RADIO_CONSOLE",(x+4,y+1.4,2.0),(1.0,0.7,1.5),"yellow",f)
    box("RM_GATEHOUSE_BARRIER_CONTROL",(x+6.4,y,1.9),(0.6,0.6,1.6),"red",f)
    pipe("RM_GATEHOUSE_BOOM_BARRIER",(x+7.3,y,2.4),(x+12,y,2.4),0.12,"yellow",f)
    box("RM_GATEHOUSE_VISITOR_WINDOW",(x,y+2.7,3.4),(5.5,0.12,1.5),"white",f)

def toothpaste():
    f="Toothpaste Production"; x,y=-12,43
    tank("RM_TOOTHPASTE_VACUUM_MIXER",x-7,y,2.0,3.8,f,"stainless")
    box("RM_TOOTHPASTE_VACUUM_HEAD",(x-7,y,5.4),(0.9,0.9,1.0),"blue",f)
    pipe("RM_TOOTHPASTE_TRANSFER",(x-5,y,2.5),(x-1,y,2.5),0.24,"stainless",f)
    tank("RM_TOOTHPASTE_HOLDING_TANK",x+1,y,1.5,3.2,f,"green")
    conveyor("RM_TOOTHPASTE_TUBE_LINE",x+8,y,13,1.8,f,"stainless")
    machine("RM_TOOTHPASTE_TUBE_FILLER",x+5,y,2.3,2.0,2.5,f,"blue")
    machine("RM_TOOTHPASTE_CARTONER",x+11,y,2.3,1.8,2.4,f,"yellow")
    for i in range(5): cyl(f"RM_TOOTHPASTE_TUBE_{i}",(x+4+i*1.4,y,2.0),0.14,1.0,"white",f,16)

def wipes():
    f="Wet Wipes Production"; x,y=22,43
    box("RM_WIPES_UNWIND_STAND",(x-13,y,3.0),(2.0,3.0,4.0),"steel",f)
    cyl("RM_WIPES_ROLL",(x-12,y-1.7,3.0),1.3,0.6,"white",f,32).rotation_euler[1]=math.pi/2
    tank("RM_WIPES_LOTION_TANK",x-7,y+2,1.5,3.0,f,"green")
    pipe("RM_WIPES_LOTION_FEED",(x-7,y+0.5,4),(x-4,y,3),0.18,"green",f)
    machine("RM_WIPES_FOLD_CUT",x-2,y,2.4,2.4,2.8,f,"blue")
    machine("RM_WIPES_STACKER",x+4,y,2.4,2.1,2.6,f,"magenta")
    machine("RM_WIPES_POUCH_PACKER",x+10,y,2.5,2.4,3.0,f,"yellow")
    conveyor("RM_WIPES_PACKOUT",x+14,y,8,1.6,f,"stainless")

def main():
    pre=sha(BLEND)
    for fn in (blow,caps,lv,welfare,fire_pump,glass,liquid,weigh,powder,wet_process,reception,gatehouse,toothpaste,wipes): fn()
    scene=bpy.context.scene
    scene["REV005_REMEDIATION_V01_STATUS"]="AWAITING_GPT_REMEDIATION_AUDIT"
    scene["REV005_REMEDIATION_V01_COLLECTION"]=COL_NAME
    scene["REV004_PRESERVED"]=True
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True)
    OUT.mkdir(parents=True,exist_ok=True)
    result={"status":"BUILT","collection":COL_NAME,"pre_sha256":pre,"post_blend_sha256":sha(BLEND),"post_glb_sha256":sha(GLB),"object_count":len(C.objects),"blend":str(BLEND),"glb":str(GLB)}
    (OUT/"BUILD_RESULT.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))

main()
