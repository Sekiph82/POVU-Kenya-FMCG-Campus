import bpy
import hashlib
import json
import math
import re
from pathlib import Path
from mathutils import Vector

# V09 deliberately reuses only the geometry helper definitions from V08.  It
# does not import or call the V08 main routine, and it does not unhide retired
# legacy proxies.  The existing V08 clean collections are the replacement
# boundary for this image-by-image pass.
ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v09"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
BASELINE = OUT / "V09_BASELINE_HASHES.json"
INVENTORY = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

V08 = REV / "pipeline/build_rev005_interior_remediation_v08.py"
source = V08.read_text(encoding="utf-8")
exec(source.split("def main():", 1)[0], globals())
# The V08 prefix defines its own paths/material table; restore the V09 output
# boundary after executing those helper definitions.
ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v09"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
BASELINE = OUT / "V09_BASELINE_HASHES.json"
INVENTORY = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

REVISION = "V09"
REMEDIATION_GROUPS = [
    "Administration / HQ / R&D / QC", "Bottle blow molding", "Chemical compound / controlled receiving",
    "ETP / water treatment", "Finished goods warehouse / dispatch", "Glass Deck central command / training / café gallery",
    "Liquid filling / packaging", "Occupational health / first aid", "Packaging warehouse", "Powder handling / packing",
    "Production Hall / Wet Processing / process core", "Raw material warehouse / receiving", "Restaurant / POVU Café / kitchen",
    "Security / reception / visitor arrival", "Security gatehouse", "Toothpaste production", "Training / Academy",
    "Utilities / engineering", "Wellness / recreation", "Wet wipes production",
]
PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
}

def clean_collection(group):
    name = "REV005_V08_CLEAN_" + slug(group)
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    for obj in list(col.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    COLLECTIONS[group] = col
    return col

def pbox(name, x, y, z, w, d, h, facility, material="steel"):
    return box("V09_" + name, (x, y, z), (w, d, h), material, facility)

def pcyl(name, x, y, z, r, h, facility, material="stainless", rot=None):
    return cyl("V09_" + name, (x, y, z), r, h, material, facility, 20, rot)

def ppipe(name, a, b, facility, radius=.12, material="steel"):
    return pipe("V09_" + name, a, b, radius, material, facility)

def pallet(name, x, y, facility, material="wood", load="white"):
    pbox(name + "_BASE", x, y, 1.2, 2.0, 1.4, .18, facility, material)
    for ix in (-.65, .65):
        for iy in (-.45, .45): pbox(name + f"_BLOCK_{ix}_{iy}", x + ix, y + iy, 1.42, .22, .22, .3, facility, material)
    pbox(name + "_LOAD", x, y, 2.05, 1.55, 1.1, 1.15, facility, load)

def chair(name, x, y, facility, material="purple"):
    pbox(name + "_SEAT", x, y, 1.55, .7, .7, .14, facility, material)
    pbox(name + "_BACK", x, y + .28, 2.05, .7, .12, 1.0, facility, material)
    for dx in (-.25, .25): pbox(name + f"_LEG_{dx}", x + dx, y, 1.2, .08, .08, .6, facility, "steel")

def screen(name, x, y, z, facility):
    pbox(name + "_PANEL", x, y, z, 2.0, .10, 1.15, facility, "dark")
    pbox(name + "_STAND", x, y, z - .8, .12, .12, 1.0, facility, "steel")

def light_strip(name, x, y, z, w, facility):
    pbox(name, x, y, z, w, .16, .08, facility, "white")

def machine_frame(name, x, y, w, d, h, facility, body="blue"):
    pbox(name + "_BASE", x, y, 1.15, w + .5, d + .45, .22, facility, "steel")
    for dx in (-w/2, w/2):
        for dy in (-d/2, d/2): pbox(name + f"_POST_{dx}_{dy}", x + dx, y + dy, 1 + h/2, .14, .14, h, facility, "steel")
    pbox(name + "_TOP", x, y, 1 + h, w, d, .16, facility, "steel")
    pbox(name + "_BODY", x, y, 1 + h*.45, w*.7, d*.65, h*.7, facility, body)
    pbox(name + "_PANEL", x, y - d*.38, 2.2, w*.3, .08, .7, facility, "teal")

def guard(name, x, y, w, d, h, facility):
    for xx in (x-w/2, x+w/2):
        for yy in (y-d/2, y+d/2): pbox(name + f"_POST_{xx}_{yy}", xx, yy, 1+h/2, .1, .1, h, facility, "yellow")
    pbox(name + "_TOP", x, y, 1+h, w, .08, .08, facility, "yellow")

def doorway(name, x, y, facility):
    pbox(name + "_HEADER", x, y, 5.8, 3.0, .18, .45, facility, "steel")
    pbox(name + "_L", x-1.4, y, 3.0, .18, .18, 5.5, facility, "steel")
    pbox(name + "_R", x+1.4, y, 3.0, .18, .18, 5.5, facility, "steel")

def label_free_safety(facility, x, y):
    pbox("SAFETY_EYEWASH", x, y, 1.7, .35, .35, .6, facility, "teal")
    pbox("PPE_STATION", x+.7, y, 2.0, .8, .35, 1.35, facility, "yellow")

def env(prefix, x, y, w, d, h, facility, glazing=False):
    envelope("V09_" + prefix, x, y, w, d, h, facility, glazing)
    doorway(prefix + "_ENTRY", x, y-d/2-.04, facility)
    light_strip(prefix + "_LIGHT_0", x-w*.25, y, h-.4, w*.32, facility)
    light_strip(prefix + "_LIGHT_1", x+w*.25, y, h-.4, w*.32, facility)

def build_admin():
    f=REMEDIATION_GROUPS[0]; env("ADMIN",-58,-64,46,28,7,f,True)
    desk("V09_ADMIN_RECEPTION",-77,-53,7,1.3,f); partition("V09_RECEPTION_PARTITION",-77,-55,8,4,f)
    for i in range(6):
        x=-71+i*4.6; desk(f"V09_ADMIN_WORKSTATION_{i}",x,-61,3.2,2.2,f); screen(f"V09_ADMIN_MONITOR_{i}",x,-59.8,2.8,f); chair(f"V09_ADMIN_CHAIR_{i}",x,-62.5,f)
    desk("V09_MEETING_TABLE",-57,-55,9,3,f,"wood")
    for i in range(8): chair(f"V09_MEETING_CHAIR_{i}",-61+(i%4)*2.6,-57+(i//4)*4.0,f)
    partition("V09_LAB_PARTITION",-42,-64,12,4.6,f)
    for i in range(3):
        desk(f"V09_QC_BENCH_{i}",-47+i*4.2,-70,3.5,1,f,"stainless")
        for j in range(3): pcyl(f"V09_LAB_INSTR_{i}_{j}",-48+i*4.2+j*.7,-69.5,2.8,.22,.55,f,"blue")
    rack("V09_QC_SHELF",-39,-75,2,4,f,"white")

def build_bottle():
    f=REMEDIATION_GROUPS[1]; env("BLOW",52,10,38,24,8,f)
    machine_frame("PREFORM_HOPPER",38,10,3.2,3,3.8,f,"yellow"); pbox("HOPPER_FUNNEL",38,10,4.1,2.2,2.2,1.1,f,"stainless")
    conveyor("V09_PREFORM_FEED",43,10,6,1.2,f); machine_frame("HEATER_OVEN",48,10,5,4,4.8,f,"orange")
    for i in range(8): pcyl(f"V09_HEATER_BANK_{i}",46.3+i*.48,8.1,4.8,.1,2.7,f,"red",(math.pi/2,0,0))
    machine_frame("BLOW_CELL",56,10,6,4.2,5.4,f,"blue"); guard("BLOW_GUARD",56,10,6.8,5,5.8,f)
    for xx in (53.8,58.2): pbox(f"V09_MOULD_CLAMP_{xx}",xx,8.2,3.7,.25,1.1,4.4,f,"yellow")
    pbox("BLOW_AIR_MANIFOLD",56,7.5,6.0,4,.18,.22,f,"teal"); ppipe("BLOW_AIR_DROP",(56,7.5,6),(56,10,4.4),f,.12,"teal")
    conveyor("V09_BOTTLE_OUTFEED",65,10,10,1.5,f); bottles("V09_FORMED",61,10,8,f); doorway("BLOW_SERVICE_DOOR",71,18,f)

def build_chemical():
    f=REMEDIATION_GROUPS[2]; env("CHEM",56,80,38,30,8,f)
    pbox("DOCK_APRON",56,94.5,1.2,18,3,.18,f,"orange")
    for i,xx in enumerate((46,56,66)):
        pbox(f"BUND_{i}",xx,74,1.16,7,7,.22,f,"yellow"); tank(f"V09_BULK_TANK_{i}",xx,74,2.1,5.2,f,"stainless")
        machine_frame(f"TRANSFER_PUMP_{i}",xx+3.6,74,1.2,1.2,1.5,f,"blue")
        ppipe(f"PUMP_TO_HEADER_{i}",(xx+3.6,74,3),(76,74,3),f,.13,"yellow")
    for i in range(6): pcyl(f"V09_RECEIVING_DRUM_{i}",43+i*4.2,90,1.7,.7,1.4,f,"red")
    for i in range(3):
        pbox(f"V09_IBC_CAGE_{i}",72,88-i*4,2.1,2.4,2.4,2.4,f,"steel"); pbox(f"V09_IBC_{i}",72,88-i*4,2.1,1.9,1.9,1.9,f,"white")
    ppipe("TRANSFER_HEADER",(46,74,6),(66,74,6),f,.16,"yellow"); ppipe("TRANSFER_TO_DOCK",(66,74,6),(70,90,3),f,.14,"yellow")
    partition("V09_CONTROLLED_ACCESS",72,84,7,4.4,f); desk("V09_RECEIVING_CHECK",44,85,4,1,f); label_free_safety(f,77,91)

def build_etp():
    f=REMEDIATION_GROUPS[3]; env("ETP",108,35,40,32,8,f)
    stages=[(94,"INFLUENT_EQUALISATION",3.5),(105,"AERATION_TREATMENT",4.2),(116,"CLARIFICATION",3.8)]
    for x,n,r in stages:
        pbox(n+"_BASIN",x,34,1.12,7,8,.25,f,"concrete" if "concrete" in M else "floor"); tank(n+"_VESSEL",x,34,r,3.6,f,"stainless"); rails(n+"_RAILS",x,34,7,f)
        pbox(n+"_ACCESS",x,30,4.2,6,.9,.16,f,"steel")
    for i,x in enumerate((94,105,116)): machine_frame(f"ETP_PUMP_{i}",x,27,1.4,1.3,1.5,f,"blue")
    ppipe("ETP_INFLUENT",(86,36,2),(94,34,2),f,.16,"teal"); ppipe("ETP_AERATION",(98,34,5),(105,34,5),f,.14,"teal"); ppipe("ETP_CLARIFIER",(109,34,5),(116,34,5),f,.14,"teal")
    machine_frame("FILTRATION_SKID",124,37,4,3,3.5,f,"blue"); ppipe("ETP_DISCHARGE",(120,34,2),(126,37,2),f,.14,"teal"); machine_frame("SLUDGE_PUMP",124,29,1.6,1.4,1.4,f,"orange")

def build_warehouse(group, x, y, w, d, load, label, raw=False):
    f=group; env(label,x,y,w,d,8,f)
    rack("V09_RACK_A",x-w*.3,y+3,3,5,f,load); rack("V09_RACK_B",x+w*.05,y+3,3,5,f,load)
    for i in range(4): pallet(f"V09_PALLET_{i}",x-w*.28+i*2.5,y-d*.25,f,"wood",load)
    conveyor("V09_MATERIAL_FLOW",x,y-d*.2,w*.55,1.6,f)
    if raw:
        pbox("RECEIVING_DOCK",x-w*.15,y+d*.36,1.25,12,2,.22,f,"orange"); desk("INSPECTION_DESK",x-w*.35,y+d*.18,4,1,f); pbox("QUARANTINE_BAY",x+w*.25,y+d*.18,1.2,8,4,.18,f,"yellow")
        machine_frame("FORKLIFT_CHARGE",x+w*.35,y,2,2,1.5,f,"green")
    else:
        desk("DISPATCH_CONTROL",x+w*.28,y-d*.18,4,1,f); doorway("LOADING_DOCK",x+w*.25,y-d*.48,f); machine_frame("AMR_DISPATCH",x,y-d*.1,2.2,1.8,1.2,f,"orange")

def build_finished(): build_warehouse(REMEDIATION_GROUPS[4],80,-51,52,24,"white","FINISHED_GOODS",False)

def build_glass():
    f=REMEDIATION_GROUPS[5]; env("GLASS_DECK",70,24,40,24,8,f,True)
    pbox("COMMAND_CONSOLE",60,17,1.8,8,1.8,1.1,f,"dark")
    for i in range(4): screen(f"COMMAND_SCREEN_{i}",57+i*2.2,15.8,4.0,f)
    for i in range(6): chair(f"COMMAND_CHAIR_{i}",57+i*2.0,19,f)
    pbox("TRAINING_SCREEN",73,34.8,4.2,6,.15,3.2,f,"dark"); pbox("TRAINING_TABLE",74,27,1.7,10,3,.16,f,"wood")
    for i in range(8): chair(f"TRAINING_CHAIR_{i}",70+(i%4)*2.4,25+(i//4)*4,f)
    pbox("CAFE_COUNTER",87,17,2.0,7,1.1,1.5,f,"wood"); pbox("CAFE_BACKBAR",87,18,3.8,7,.3,3.2,f,"steel"); pbox("CAFE_DISPLAY",87,16.3,3.0,2,.3,1.2,f,"white")
    for i in range(4):
        pbox(f"CAFE_TABLE_{i}",80+(i%2)*5,20+(i//2)*4,1.7,2.1,1.2,.14,f,"wood"); chair(f"CAFE_CHAIR_{i}A",79.2+(i%2)*5,20+(i//2)*4,f,"wood"); chair(f"CAFE_CHAIR_{i}B",80.8+(i%2)*5,20+(i//2)*4,f,"wood")

def build_liquid():
    f=REMEDIATION_GROUPS[6]; env("LIQUID",10,-2,50,20,8,f)
    conveyor("V09_BOTTLE_INFEED",-10,-2,9,1.5,f); machine_frame("FILLER",0,-2,6,3,4.3,f,"stainless")
    for i in range(8): pcyl(f"FILL_NOZZLE_{i}",-2.8+i*.8,-2,5.2,.1,.8,f,"steel")
    machine_frame("CAPPER",10,-2,4,3,3.2,f,"blue"); pcyl("CAP_BOWL",8,-4.5,4.4,1.2,1.0,f,"yellow"); conveyor("CAP_CHUTE",10,-3,3,.4,f)
    machine_frame("LABEL_INSPECT",20,-2,4,2.6,3.0,f,"orange"); pcyl("LABEL_ROLL",18,-3.5,4.3,1.0,.45,f,"white",(math.pi/2,0,0)); screen("INSPECTION_MONITOR",21,-3.5,3.6,f)
    machine_frame("CASE_PACK",30,-2,5,3.5,3.4,f,"teal"); conveyor("CASE_OUTFEED",39,-2,9,1.8,f); bottles("V09_FILLED_BOTTLES",-7,-2,8,f); guard("LINE_GUARD",16,-2,30,3,2.8,f)

def build_clinic():
    f=REMEDIATION_GROUPS[7]; env("CLINIC",-18,-94,26,18,7,f,True)
    desk("CLINIC_RECEPTION",-26,-88,4,1,f); chair("CLINIC_WAIT_A",-24,-91,f); chair("CLINIC_WAIT_B",-21,-91,f); partition("CLINIC_PRIVACY",-15,-94,6,3.6,f)
    pbox("EXAM_BED",-11,-97,1.8,2.2,6,.35,f,"white"); pbox("EXAM_PILLOW",-11,-99,2.1,2,.8,.3,f,"soft"); machine_frame("TREATMENT_TROLLEY",-14,-97,1.2,.8,1.0,f,"stainless"); pbox("CLINIC_SINK",-4,-98,1.9,1.8,1,.8,f,"stainless"); pbox("MED_CABINET",-4,-91,2.8,2,.6,2.8,f,"white")

def build_packaging():
    f=REMEDIATION_GROUPS[8]; env("PACKAGING_WH",-10,79,58,45,8,f)
    rack("CARTON_RACKS",-22,80,4,6,f,"white"); rack("FILM_RACKS",4,80,3,5,f,"blue")
    for i in range(5): pcyl(f"FILM_ROLL_{i}",0+i*3,67,2.5,1.0,2.0,f,"soft",(math.pi/2,0,0))
    for i in range(6): pallet(f"CARTON_PALLET_{i}",-22+i*3,100,f,"wood","white")
    conveyor("PACKAGING_ISSUE_FLOW",-4,68,34,1.6,f); desk("MATERIAL_ISSUE_DESK",18,72,4,1,f); doorway("PACKAGING_RECEIVING",-31,100,f)

def build_powder():
    f=REMEDIATION_GROUPS[9]; env("POWDER",-48,43,38,19,8,f)
    pbox("BULK_HOPPER",-61,44,4.0,4,4,5.5,f,"stainless"); pcyl("HOPPER_CONE",-61,44,1.8,2.2,1.8,f,"stainless"); machine_frame("AUGER_DOSER",-54,43,3,2.5,3.0,f,"blue"); ppipe("AUGER_TRANSFER",(-59,44,4),(-55,43,3),f,.18,"stainless")
    machine_frame("FFS_SACHET",-47,43,4,3,4.2,f,"orange"); guard("DUST_HOOD",-47,43,5,4,5.6,f); conveyor("SACHET_OUTFEED",-39,43,8,1.4,f); bottles("POWDER_SACHETS",-41,43,7,f,1.9)

def build_wet():
    f=REMEDIATION_GROUPS[10]; env("WET_PROCESS",0,24,54,32,8,f)
    for i,x in enumerate((-17,-6,5,16)):
        tank(f"MIX_TANK_{i}",x,27,3.0,5.0,f,"stainless"); rails(f"MIX_RAIL_{i}",x,27,6,f); machine_frame(f"TANK_GEARBOX_{i}",x,27,1.2,1.2,1.0,f,"blue")
        pbox(f"TANK_PLATFORM_{i}",x,27,4.0,6,5,.16,f,"steel")
    machine_frame("CIP_SKID",24,18,5,3,3.2,f,"teal"); tank("CIP_TANK",24,26,2.0,3.2,f,"stainless")
    for i,x in enumerate((-17,-6,5,16)):
        ppipe(f"TANK_HEADER_{i}",(x,24,3),(x,19,3),f,.13,"yellow"); ppipe(f"TANK_BRANCH_{i}",(x,19,3),(24,19,3),f,.13,"yellow")
    ppipe("CIP_SUPPLY",(24,28,4),(16,28,4),f,.14,"teal"); ppipe("CIP_RETURN",(16,26,2),(24,26,2),f,.14,"teal"); conveyor("WET_TRANSFER_PATH",28,33,12,1.5,f)

def build_raw(): build_warehouse(REMEDIATION_GROUPS[11],-78,79,54,38,"orange","RAW_MATERIALS",True)

def build_restaurant():
    f=REMEDIATION_GROUPS[12]; env("RESTAURANT",5,-69,46,26,7,f,True)
    for i in range(6):
        x=-10+(i%3)*7; y=-75+(i//3)*8; pbox(f"DINING_TABLE_{i}",x,y,1.7,3.2,1.6,.14,f,"wood")
        for j in range(4): chair(f"DINING_CHAIR_{i}_{j}",x-1.8+(j%2)*3.6,y-1.3+(j//2)*2.6,f,"wood")
    pbox("CAFE_POS",20,-61,2.0,3,.8,1.4,f,"wood"); pbox("CAFE_BACKBAR",24,-61,3.5,6,.45,3.2,f,"steel"); pbox("SERVICE_COUNTER",20,-64,2.0,7,.9,1.4,f,"wood")
    machine_frame("KITCHEN_PREP",19,-75,5,3,2.8,f,"stainless"); machine_frame("COOK_LINE",28,-75,5,3,3.0,f,"orange"); pbox("COOK_HOOD",28,-75,5.5,6,3,.3,f,"steel"); pbox("KITCHEN_SINK",12,-75,1.8,2,1,.8,f,"stainless"); pbox("PASS",20,-71,3.0,6,.3,1.2,f,"white")

def build_security():
    f=REMEDIATION_GROUPS[13]; env("SECURITY",-58,-84,48,16,7,f,True)
    doorway("SECURITY_ENTRY",-80,-84,f); desk("SECURITY_DESK",-59,-80,4,1,f); screen("CCTV_WALL",-59,-87,4.2,f)
    for i in range(4): pbox(f"TURNSTILE_{i}",-67+i*4,-83,1.9,.55,1.6,1.8,f,"steel")
    for i in range(3): chair(f"WAIT_{i}",-63+i*5,-88,f); pbox(f"WAIT_BACK_{i}",-63+i*5,-88.3,2.1,.7,.12,1.0,f,"purple")
    pbox("ACCESS_SCREEN",-50,-82,2.7,1.6,.12,1.6,f,"teal"); pbox("QUEUE_BARRIER",-55,-86,1.8,12,.08,.08,f,"yellow")

def build_gatehouse():
    f=REMEDIATION_GROUPS[14]; env("GATEHOUSE",96,-106,20,14,6,f,True)
    desk("GATE_OPERATOR",96,-108,3.5,1,f); chair("GATE_CHAIR",96,-109,f); screen("GATE_CCTV",96,-106,3.3,f)
    pbox("VEHICLE_LANE",96,-116,1.05,8,28,.12,f,"floor"); pbox("ROAD_MARKING",96,-116,1.14,.18,25,.04,f,"yellow"); pbox("BARRIER_ARM",96,-100,3.0,8,.15,.15,f,"red"); pcyl("BARRIER_POST",92,-100,2,.35,2,f,"steel"); doorway("GATE_DOOR",101,-112,f)

def build_toothpaste():
    f=REMEDIATION_GROUPS[15]; env("TOOTHPASTE",-12,43,42,19,8,f)
    machine_frame("VACUUM_MIX",-27,43,4,3,4.0,f,"stainless"); tank("HOLDING_TANK",-20,47,2.0,4.2,f,"stainless"); machine_frame("TUBE_FEED",-14,43,3,2.5,2.8,f,"blue"); conveyor("TUBE_MAGAZINE",-14,40,6,1.2,f)
    machine_frame("TUBE_FILL",-7,43,4,3,3.8,f,"teal");
    for i in range(7): pcyl(f"TUBE_{i}",-9+i*.65,42,2.0,.16,1.1,f,"white")
    machine_frame("CRIMP_CODE",2,43,4,3,3.6,f,"orange"); pbox("CRIMP_HEAD",2,43,4.3,2,.8,.5,f,"steel"); machine_frame("CARTON_OUTFEED",12,43,4,3,3.0,f,"blue"); conveyor("TOOTHPASTE_FLOW",17,43,7,1.5,f); guard("TOOTHPASTE_GUARD",-1,43,25,3,2.6,f)

def build_training():
    f=REMEDIATION_GROUPS[16]; env("TRAINING",30,-61,28,18,7,f,False)
    pbox("INSTRUCTOR_LECTERN",21,-67,1.8,1.2,.8,1.2,f,"wood"); pbox("TRAINING_BOARD",30,-69.8,4.0,7,.12,3.0,f,"dark")
    for i in range(10):
        x=24+(i%5)*3.0; y=-62+(i//5)*5.0; pbox(f"LEARNER_DESK_{i}",x,y,1.7,2.0,.9,.14,f,"wood"); chair(f"LEARNER_CHAIR_{i}",x,y+1.1,f)
    rack("TRAINING_STORAGE",41,-67,2,3,f,"white"); doorway("TRAINING_DOOR",30,-70,f)

def build_utilities():
    f=REMEDIATION_GROUPS[17]; env("UTILITIES",96,75,36,30,8,f)
    machine_frame("COMPRESSOR",85,67,4,3,3.0,f,"blue"); pcyl("AIR_RECEIVER",91,67,3.5,2.1,5.0,f,"stainless"); machine_frame("AIR_DRYER",97,67,2.5,2,2.8,f,"teal"); ppipe("AIR_HEADER",(85,71,6),(108,71,6),f,.16,"yellow")
    machine_frame("BOILER",87,82,5,4,4.2,f,"orange"); pbox("BOILER_BURNER",87,79.5,2.5,1.4,.4,1.2,f,"red"); ppipe("STEAM_HEADER",(90,82,6),(108,82,6),f,.16,"red")
    machine_frame("RO_SKID",104,76,6,3,3.5,f,"white");
    for i in range(3): pcyl(f"RO_MEMBRANE_{i}",102+i*2,76,3.2,.55,3.8,f,"stainless",(0,math.pi/2,0))
    machine_frame("RO_PUMP",111,76,1.5,1.4,1.4,f,"blue"); ppipe("RO_PRODUCT",(108,76,4),(116,76,4),f,.12,"teal"); ppipe("RO_REJECT",(108,78,3),(116,78,3),f,.12,"yellow");
    for i in range(4): pbox(f"UTILITY_MANIFOLD_VALVE_{i}",104+i*1.8,88,2.2,.3,.3,.6,f,"yellow")

def build_wellness():
    f=REMEDIATION_GROUPS[18]; env("WELLNESS",30,-70,30,22,7,f,True)
    for i in range(3):
        x=20+i*6; machine_frame(f"TREADMILL_{i}",x,-68,2.2,4,1.2,f,"blue"); pbox(f"TREAD_DECK_{i}",x,-68,1.65,1.6,2.6,.12,f,"dark"); pbox(f"TREAD_CONSOLE_{i}",x,-66.5,3.3,1.0,.3,.9,f,"teal")
    for i in range(2): pcyl(f"BIKE_FLYWHEEL_{i}",22+i*6,-75,1.8,.7,.25,f,"steel",(math.pi/2,0,0)); pbox(f"BIKE_UPRIGHT_{i}",22+i*6,-75,2.3,.12,.12,1.5,f,"steel")
    rack("DUMBBELL_RACK",38,-76,2,3,f,"steel"); pbox("BENCH",40,-71,1.5,3,.8,.35,f,"soft");
    for i in range(4): pbox(f"YOGA_MAT_{i}",22+i*4,-62,1.35,2.2,1,.05,f,"soft")
    for i in range(4): pbox(f"LOCKER_{i}",19+i*4,-79,2.2,1.2,.5,1.9,f,"white"); pbox(f"MIRROR_{i}",19+i*4,-80,3.5,1.2,.05,2.4,f,"glass")

def build_wipes():
    f=REMEDIATION_GROUPS[19]; env("WET_WIPES",22,43,52,19,8,f)
    machine_frame("PARENT_ROLL",-1,43,3,3,3.6,f,"white"); pcyl("PARENT_ROLL_CORE",-1,41.4,3.6,1.3,.5,f,"steel",(math.pi/2,0,0));
    for i,x in enumerate((4,10,16)): pbox(f"WEB_ROLLER_{i}",x,43,3,.35,2.2,4.0,f,"steel"); ppipe(f"WEB_PATH_{i}",(x,42,3),(x+3,42,3),f,.12,"soft")
    machine_frame("WETTING_MANIFOLD",21,43,4,3,3.0,f,"teal"); pbox("SPRAY_BAR",21,42,4.8,3,.2,.2,f,"blue");
    machine_frame("FOLD_CUT_STACK",29,43,5,3,3.6,f,"orange"); pbox("CUTTER_HEAD",29,43,4.4,2,.5,.4,f,"steel"); machine_frame("POUCH_FILM_FEED",38,43,3,3,3.0,f,"white");
    machine_frame("SEAL_JAWS",46,43,4,3,3.5,f,"blue"); pbox("SEAL_JAW_TOP",46,43,4.4,2.4,.3,.4,f,"steel"); conveyor("WIPES_OUTFEED",56,43,9,1.5,f); bottles("FINISHED_POUCHES",53,43,7,f,2.0)

BUILDERS = {
    REMEDIATION_GROUPS[0]: build_admin, REMEDIATION_GROUPS[1]: build_bottle, REMEDIATION_GROUPS[2]: build_chemical,
    REMEDIATION_GROUPS[3]: build_etp, REMEDIATION_GROUPS[4]: build_finished, REMEDIATION_GROUPS[5]: build_glass,
    REMEDIATION_GROUPS[6]: build_liquid, REMEDIATION_GROUPS[7]: build_clinic, REMEDIATION_GROUPS[8]: build_packaging,
    REMEDIATION_GROUPS[9]: build_powder, REMEDIATION_GROUPS[10]: build_wet, REMEDIATION_GROUPS[11]: build_raw,
    REMEDIATION_GROUPS[12]: build_restaurant, REMEDIATION_GROUPS[13]: build_security, REMEDIATION_GROUPS[14]: build_gatehouse,
    REMEDIATION_GROUPS[15]: build_toothpaste, REMEDIATION_GROUPS[16]: build_training, REMEDIATION_GROUPS[17]: build_utilities,
    REMEDIATION_GROUPS[18]: build_wellness, REMEDIATION_GROUPS[19]: build_wipes,
}

def restore_preserved():
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))["facility_groups"]
    restored = {}
    names_by_group = {}
    for group in sorted(PASS_GROUPS):
        names = set(inv.get(group, {}).get("objects", [])); names_by_group[group] = sorted(names)
        found = 0
        for obj in bpy.data.objects:
            if obj.name in names:
                obj.hide_render = False
                obj.hide_viewport = False
                obj["REV005_V09_PRESERVED_EXACT"] = True
                obj["REV005_V09_PRESERVED_GROUP"] = group
                found += 1
        restored[group] = {"inventory_count": len(names), "restored_count": found, "missing": sorted(names - {o.name for o in bpy.data.objects if o.name in names})}
    return restored, names_by_group

def mark_v09(objects):
    for obj in objects:
        if obj.get("REV005_V08_CLEAN"):
            obj["REV005_V09_REMEDIATED"] = True
            obj["REV005_V09_IMAGE_BY_IMAGE"] = True
            obj["REV005_V09_LEGACY_PROXY_RETIRED"] = True

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    before_blend, before_glb = sha(BLEND), sha(GLB)
    if before_blend != baseline["blend"]["sha256"] or before_glb != baseline["glb"]["sha256"]:
        raise RuntimeError("V09 baseline mismatch; refusing to mutate REV005")
    scene = bpy.context.scene
    built = {}
    for group, builder in BUILDERS.items():
        clean_collection(group)
        CURRENT = COLLECTIONS[group]
        globals()["CURRENT"] = CURRENT
        builder()
        objs = list(CURRENT.objects)
        mark_v09(objs)
        built[group] = {"collection": CURRENT.name, "object_count": len(objs)}
    restored, names_by_group = restore_preserved()
    scene["REV005_REMEDIATION_V09_STATUS"] = "AWAITING_GPT_REMEDIATION_AUDIT_V09"
    scene["REV005_V09_TASK"] = "M08.18"
    scene["REV005_V09_SPEC_COUNT"] = 72
    scene["REV005_V09_ISOLATED_COUNT"] = 20
    scene["REV005_V09_RENDER_COUNT"] = 92
    scene["REV005_V09_BASELINE_BLEND_SHA256"] = before_blend
    scene["REV005_V09_BASELINE_GLB_SHA256"] = before_glb
    scene["REV005_V09_PRESERVED_EXACT_OBJECTS"] = json.dumps(names_by_group, sort_keys=True)
    temp = REV / ".POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER_V09.tmp.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(temp), check_existing=False)
    temp.replace(BLEND)
    export_visibility = "use_visible=True"
    try:
        bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True, use_selection=False, use_visible=True)
    except TypeError:
        bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True, use_selection=False)
        export_visibility = "operator_fallback_without_use_visible"
    report = {"status": "AWAITING_GPT_REMEDIATION_AUDIT_V09", "task": "M08.18", "baseline_blend": before_blend, "baseline_glb": before_glb, "blend_after": sha(BLEND), "glb_after": sha(GLB), "builders": built, "preserved": restored, "export_visibility": export_visibility, "no_rev004_mutation": True, "no_rev006": True, "no_hiveai": not any(p.name.lower()==".hiveai" for p in ROOT.iterdir())}
    (OUT / "V09_BUILD_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"status": report["status"], "groups": len(built), "preserved": restored, "blend_after": report["blend_after"], "glb_after": report["glb_after"]}, indent=2))

main()
