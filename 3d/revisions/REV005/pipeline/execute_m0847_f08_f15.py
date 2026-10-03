import bpy, json, math, hashlib, sys
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-facility-gated/F08_F15_combined"
STAGE = OUT / "REV005_F08_F15_STAGED.blend"
SOURCE = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
R02 = ROOT / "output/rev005-facility-gated/F08_bottle_blow/R02/F08_R02_STAGED.blend"
V08 = REV / "pipeline/build_rev005_interior_remediation_v08.py"

FACILITY_MAP = {
 "F08":("Bottle blow molding","REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING",(52,10,38,24)),
 "F09":("Chemical compound / controlled receiving","REV005_V08_CLEAN_CHEMICAL_COMPOUND_CONTROLLED_RECEIVING",(56,80,38,30)),
 "F10":("ETP / water treatment","REV005_V08_CLEAN_ETP_WATER_TREATMENT",(108,35,40,32)),
 "F11":("Finished goods warehouse / dispatch","REV005_V08_CLEAN_FINISHED_GOODS_WAREHOUSE_DISPATCH",(80,-51,52,24)),
 "F12":("Glass Deck central command / training / café gallery","REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY",(70,24,40,24)),
 "F13":("Liquid filling / packaging","REV005_V08_CLEAN_LIQUID_FILLING_PACKAGING",(10,-2,50,20)),
 "F14":("Occupational health / first aid","REV005_V08_CLEAN_OCCUPATIONAL_HEALTH_FIRST_AID",(-18,-94,26,18)),
 "F15":("Packaging warehouse","REV005_V08_CLEAN_PACKAGING_WAREHOUSE",(-10,79,58,45)),
}
ARGS=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
RENDER_ONLY=set(ARGS)

def clear_col(col):
    for o in list(col.objects): bpy.data.objects.remove(o,do_unlink=True)

def get_col(name):
    global CURRENT
    c=bpy.data.collections.get(name)
    if c is None:
        c=bpy.data.collections.new(name); bpy.context.scene.collection.children.link(c)
    CURRENT=c
    return c

def new_box(n,x,y,z,w,d,h,m,f,rot=None): return box(n,(x,y,z),(w,d,h),m,f,rot)
def detail_pipe(n,a,b,f,r=.08,m="stainless"): return pipe(n,a,b,r,m,f)

def chair(n,x,y,f,material="purple"):
    new_box(n+"_SEAT",x,y,1.55,.62,.62,.14,material,f)
    new_box(n+"_BACK",x,y+.25,2.02,.62,.12,.92,material,f)
    for i,dx in enumerate((-.23,.23)):
        for j,dy in enumerate((-.23,.23)): new_box(n+f"_LEG_{i}_{j}",x+dx,y+dy,1.23,.07,.07,.58,"steel",f)

def shell(group,tag,x,y,w,d,h,door=3,glass=False):
    envelope(tag,x,y,w,d,h,group,glass)
    # Complete street-facing enclosure with a real, central service opening.
    seg=(w-door)/2
    new_box(tag+"_FRONT_L",x-(door+seg)/2,y-d/2,h/2,seg,.18,h, "wall",group)
    new_box(tag+"_FRONT_R",x+(door+seg)/2,y-d/2,h/2,seg,.18,h, "wall",group)
    new_box(tag+"_DOOR_JAMB_L",x-door/2,y-d/2,2.2,.12,.22,4.4,"steel",group)
    new_box(tag+"_DOOR_JAMB_R",x+door/2,y-d/2,2.2,.12,.22,4.4,"steel",group)
    new_box(tag+"_DOOR_HEADER",x,y-d/2,4.55,door,.22,.3,"steel",group)
    for i,xx in enumerate((x-w*.27,x+w*.27)):
        new_box(tag+f"_LED_{i}",xx,y,h-.34,4,.22,.08,"white",group)

def motor_pump(n,x,y,z,f):
    new_box(n+"_BASE",x,y,z,(1.7,1.05,.18)[0],.9,.18,"steel",f)
    cyl(n+"_MOTOR",(x-.42,y,z+.48),.38,.78,"blue",f,20,(math.pi/2,0,0))
    cyl(n+"_PUMP",(x+.38,y,z+.45),.3,.55,"stainless",f,20,(math.pi/2,0,0))
    cyl(n+"_FLANGE",(x+.68,y,z+.45),.22,.12,"steel",f,20,(0,math.pi/2,0))
    detail_pipe(n+"_SUCTION",(x+.68,y,z+.45),(x+.92,y,z+.45),f,.09,"teal")
    detail_pipe(n+"_DISCHARGE",(x+.38,y,z+.72),(x+.38,y,z+1.15),f,.08,"teal")

def drums_ibcs(f,cx,cy):
    for i in range(6):
        x=cx-12+(i%3)*3.3; y=cy+8+(i//3)*3
        cyl(f"CHEM_DRUM_{i}",(x,y,1.82),.62,1.55,"red",f,24)
        cyl(f"CHEM_DRUM_LID_{i}",(x,y,2.62),.64,.10,"steel",f,24)
        cyl(f"CHEM_DRUM_BUNG_{i}",(x+.2,y-.12,2.7),.09,.05,"yellow",f,16)
    for i in range(3):
        x=cx+12; y=cy+8-i*3.4
        new_box(f"CHEM_IBC_CAGE_{i}",x,y,2.1,2.15,2.15,2.15,"steel",f)
        new_box(f"CHEM_IBC_TANK_{i}",x,y,2.1,1.74,1.74,1.75,"white",f)
        cyl(f"CHEM_IBC_CAP_{i}",(x,y,3.02),.2,.12,"yellow",f)
        for yy in (y-.85,y+.85): new_box(f"CHEM_IBC_CAGE_BAR_{i}_{yy}",x,yy,2.1,2.1,.06,2.12,"stainless",f)

def build_f09():
    f=GROUPS["F09"][0];cx,cy,w,d=56,80,38,30;shell(f,"CHEM_V10",cx,cy,w,d,8,4)
    # Three distinct tanks in continuous spill containment.
    for x in (46,56,66):
        new_box(f"BUND_WALL_{x}",x,74,1.18,7.2,7.2,.22,"yellow",f)
        tank(f"CHEM_BULK_TANK_{x}",x,74,2.15,5.2,f)
        new_box(f"TANK_LEGACY_LADDER_{x}",x-2.15,74,3.2,.14,.14,4.5,"steel",f)
        for z in (1.5,3.5,5.5): new_box(f"TANK_BAND_{x}_{z}",x,74,z,4.3,4.3,.1,"blue",f)
    new_box("CHEM_BUND_SUMP",69.1,70.6,1.09,.9,.9,.1,"dark",f)
    drums_ibcs(f,cx,cy)
    for i,(x,y) in enumerate(((51,71),(63,71))):
        motor_pump(f"CHEM_TRANSFER_PUMP_SKID_{i}",x,y,1.2,f)
        cyl(f"CHEM_ISOLATION_VALVE_{i}",(x+.95,y,2.36),.3,.18,"yellow",f,18,(0,math.pi/2,0))
    detail_pipe("CHEM_RAISED_HEADER",(44,71,3.1),(68,71,3.1),f,.11,"yellow")
    detail_pipe("CHEM_DOCK_TRANSFER",(44,71,3.1),(44,91,3.1),f,.11,"yellow")
    for i,(a,b) in enumerate([((44,91,3.1),(47,91,3.1)),((47,91,3.1),(50,89,2.8)),((52,71,3.1),(52,74,4.1)),((62,71,3.1),(62,74,4.1))]): detail_pipe(f"CHEM_HOSE_ROUTE_{i}",a,b,f,.09,"teal")
    new_box("CHEM_RECEIVING_DOCK",49,94.3,1.08,24,2.2,.16,"orange",f)
    new_box("CHEM_CHECK_DESK",43.5,86,2.1,2.6,1.1,1.1,"wood",f)
    new_box("CHEM_ACCESS_GATE",72,84,2.1,.18,5.5,2.2,"yellow",f)
    for x in (72.1,75.4): new_box(f"CHEM_GATE_POST_{x}",x,84,2.8,.16,.18,3.2,"steel",f)
    new_box("CHEM_EYEWASH_BASIN",76,91,1.25,.7,.5,.3,"teal",f)
    detail_pipe("CHEM_EYEWASH_STAND",(76,91,1.4),(76,91,2.2),f,.04,"yellow")

def basin(n,x,y,w,d,h,f,water=True):
    # Open process basin with thick concrete rim and visible liquid surface.
    new_box(n+"_BASE",x,y,1.18,w,d,.3,"concrete",f)
    for xx in (x-w/2,x+w/2): new_box(n+f"_WALL_X_{xx}",xx,y,1.18+h/2,.3,d,h,"concrete",f)
    for yy in (y-d/2,y+d/2): new_box(n+f"_WALL_Y_{yy}",x,yy,1.18+h/2,w,.3,h,"concrete",f)
    if water: new_box(n+"_WATER",x,y,1.24+h*.32,w-.7,d-.7,.07,"teal",f)

def rails_local(n,x,y,length,f):
    for xx in (x-length/2,x+length/2):
        for yy in (y-1.4,y+1.4): new_box(n+f"_POST_{xx}_{yy}",xx,yy,2.25,.1,.1,1.25,"yellow",f)
    for yy in (y-1.4,y+1.4):
        for z in (2.45,3.0): new_box(n+f"_RAIL_{yy}_{z}",x,yy,z,length,.08,.08,"yellow",f)

def build_f10():
    f=GROUPS["F10"][0];cx,cy,w,d=108,35,40,32;shell(f,"ETP_V10",cx,cy,w,d,8,4)
    basin("ETP_EQUALISATION_OPEN_BASIN",94,39,8,9,2.2,f)
    cyl("ETP_LEVEL_FLOAT",(92,39,2.7),.12,1.3,"yellow",f)
    basin("ETP_AERATION_BASIN",105,39,8,9,2.5,f)
    detail_pipe("ETP_AIR_HEADER",(101,34,2.1),(109,34,2.1),f,.12,"teal")
    for i in range(8):
        x=102+(i%4)*1.7;y=37+(i//4)*3
        detail_pipe(f"ETP_DIFFUSER_DROP_{i}",(x,y,1.45),(x,y,2.25),f,.045,"stainless")
        cyl(f"ETP_AERATION_DISC_{i}",(x,y,1.48),.22,.08,"blue",f,16)
    # Circular clarifier, access bridge and scraper arm are visibly distinct.
    cyl("ETP_CLARIFIER_CONCRETE_BOWL",(116,39,1.6),4.5,1.15,"concrete",f,48)
    cyl("ETP_CLARIFIER_WATER",(116,39,2.2),4.15,.09,"teal",f,48)
    cyl("ETP_CLARIFIER_CENTRAL_FEED",(116,39,2.8),.48,1.15,"stainless",f,28)
    new_box("ETP_CLARIFIER_BRIDGE",116,39,3.25,8.7,.32,.22,"steel",f)
    new_box("ETP_CLARIFIER_SCRAPER",116,39,2.52,7.2,.16,.12,"yellow",f,rot=(0,0,math.radians(18)))
    for x in (94,105,116): rails_local(f"ETP_WALKWAY_{x}",x,31,7,f)
    for i,x in enumerate((124,127)):
        tank(f"ETP_PRESSURE_FILTER_{i}",x,42,1.25,4.1,f)
        new_box(f"ETP_FILTER_LEG_{i}",x,42,1.05,.14,.14,.9,"steel",f)
    motor_pump("ETP_INFLUENT_PUMP_SKID",91,29,1.1,f)
    motor_pump("ETP_RETURN_PUMP_SKID",108,29,1.1,f)
    motor_pump("ETP_SLUDGE_PUMP_SKID",122,29,1.1,f)
    tank("ETP_SLUDGE_HOLDING_TANK",125,32,1.4,3.0,f,"blue")
    for i,(a,b) in enumerate([((90,39,2.4),(94,39,2.4)),((98,39,3.2),(101,39,3.2)),((109,39,3.4),(112,39,3.4)),((120,39,2.6),(123,42,2.6)),((125,42,3.5),(126,32,3.5)),((125,32,3.0),(127,32,3.0))]): detail_pipe(f"ETP_INTERSTAGE_{i}",a,b,f,.12,"teal")

def pallet_case(n,x,y,z,f,wrap="white"):
    new_box(n+"_PALLET",x,y,z+.15,1.45,1.15,.25,"wood",f)
    for i in range(6):
        xx=x-.46+(i%3)*.46; yy=y-.25+(i//3)*.5
        new_box(n+f"_CASE_{i}",xx,yy,z+.58,.42,.45,.58,wrap,f)
    new_box(n+"_STRETCH_FILM",x,y,z+.58,1.42,1.12,.08,"soft",f)

def forklift(n,x,y,f):
    new_box(n+"_CHASSIS",x,y,1.05,2.2,1.15,.55,"yellow",f)
    new_box(n+"_REAR_COUNTERWEIGHT",x-0.72,y,1.28,.62,1.05,.7,"orange",f)
    for dx in (-.72,.76):
        for dy in (-.58,.58): cyl(n+f"_TIRE_{dx}_{dy}",(x+dx,y+dy,.72),.34,.2,"dark",f,20,(math.pi/2,0,0))
    for dx in (.42,.78): new_box(n+f"_MAST_{dx}",x+dx,y-.35,2.25,.09,.14,2.6,"steel",f)
    new_box(n+"_OVERHEAD_GUARD",x+.62,y,3.45,1.45,1.45,.12,"yellow",f)
    for z in (1.05,1.28): new_box(n+f"_FORK_{z}",x+1.45,y,z,.95,.12,.08,"steel",f)
    new_box(n+"_SEAT",x-.18,y+.08,1.5,.5,.5,.18,"dark",f)

def build_f11():
    f=GROUPS["F11"][0];cx,cy,w,d=80,-51,52,24;shell(f,"FG_V10",cx,cy,w,d,8,5)
    rack("FG_FINISHED_CASE_RACK_A",66,-51,3,5,f,"white")
    rack("FG_FINISHED_CASE_RACK_B",76,-51,3,5,f,"soft")
    for i in range(4):
        x=63+i*3.8
        pallet_case(f"FG_STORAGE_PALLET_{i}",x,-57,1.1,f)
    # Two painted consolidation lanes lead to shipping doors.
    for i,x in enumerate((84,91)):
        new_box(f"FG_STAGING_LANE_{i}",x,-56,1.105,5.5,9,.025,"yellow",f)
        for j in range(3): pallet_case(f"FG_OUTBOUND_GROUP_{i}_{j}",x,-58+j*2.3,1.15,f,"white" if j%2 else "soft")
    for x in (96,100):
        new_box(f"FG_DOCK_DOOR_{x}",x,-62.85,3.1,3.4,.15,5.6,"dark",f)
        for xx in (x-1.8,x+1.8): new_box(f"FG_DOCK_JAMB_{x}_{xx}",xx,-62.78,3,.16,.24,5.6,"yellow",f)
        new_box(f"FG_DOCK_LEVELLER_{x}",x,-62,1.23,3.5,1.2,.22,"steel",f)
    new_box("FG_DISPATCH_CHECK_DESK",94,-49,2.05,3.3,1.25,1.2,"wood",f)
    new_box("FG_DISPATCH_MONITOR",94,-48.4,3.1,1.25,.12,.75,"dark",f)
    new_box("FG_CONSOLIDATION_SCALE",88,-49,1.22,2.1,2.1,.18,"steel",f)
    forklift("FG_FORKLIFT_PARKED",72,-58,f)

def screen_detail(n,x,y,z,f,w=1.5,h=.9):
    new_box(n+"_DISPLAY",x,y,z,w,.09,h,"dark",f)
    new_box(n+"_BEZEL",x,y+.06,z,w+.08,.07,h+.08,"steel",f)
    new_box(n+"_STAND",x,y,z-h*.65,.1,.22,h*.45,"steel",f)

def build_f12():
    f=GROUPS["F12"][0];cx,cy,w,d=70,24,40,24;shell(f,"GLASS_V10",cx,cy,w,d,8,3,True)
    # Three non-overlapping but connected zones, with floor inlays as spatial cues.
    for n,x,ww,m in (("COMMAND",59,10,"blue"),("TRAINING",72,12,"wood"),("CAFE",86,10,"warm")):
        new_box(f"GLASS_{n}_FLOOR_INLAY",x,24,1.115,ww,20,.035,m,f)
    for i in range(4):
        x=55+i*2.3
        new_box(f"GLASS_COMMAND_CONSOLE_{i}",x,17,1.65,1.65,.85,1.05,"blue",f)
        screen_detail(f"GLASS_OPERATOR_MONITOR_{i}",x,16.48,2.75,f,.72,.5)
        chair(f"GLASS_OPERATOR_CHAIR_{i}",x,18.7,f,"purple")
    for i in range(4): screen_detail(f"GLASS_COMMAND_WALL_DISPLAY_{i}",55+i*2.4,34.75,5.0,f,2.1,1.25)
    new_box("GLASS_COMMAND_EQUIPMENT_RACK",64,33.4,2.6,1.1,.55,3.1,"steel",f)
    new_box("GLASS_TRAINING_PRESENTATION",72,34.55,4.2,7,.18,3.3,"dark",f)
    for j,x in enumerate((70,76)):
        new_box(f"GLASS_TRAINING_TABLE_{j}",x,27,1.72,4.5,1.7,.14,"wood",f)
        for k in range(4): chair(f"GLASS_TRAINING_CHAIR_{j}_{k}",x-1.55+k*1.0,25.4,f)
    new_box("GLASS_CAFE_COUNTER",86,18.6,2.0,6.2,1.0,1.35,"wood",f)
    new_box("GLASS_CAFE_BACKBAR",86,19.25,3.5,6.2,.25,3.1,"steel",f)
    for i,x in enumerate((84,86,88)):
        new_box(f"GLASS_CAFE_SHELF_{i}",x,19.08,2.6,.09,.12,1.9,"yellow",f)
    for i,x in enumerate((84.2,86,87.8)):
        cyl(f"GLASS_ESPRESSO_GROUP_{i}",(x,18.0,2.85),.35,.55,"dark",f,18)
    new_box("GLASS_GALLERY_WALL",90,30,3.2,.18,6,4.5,"white",f)
    for i in range(3): new_box(f"GLASS_GALLERY_ART_{i}",89.86,27+i*2.0,3.2, .06,1.25,1.2,"warm",f)
    for i,(x,y) in enumerate(((82,22),(87,22),(82,26),(87,26),(82,30),(87,30))):
        new_box(f"GLASS_CAFE_TABLE_{i}",x,y,1.72,1.25,1.1,.14,"wood",f)
        for j,dx in enumerate((-.85,.85)): chair(f"GLASS_CAFE_SEAT_{i}_{j}",x+dx,y,f,"purple")
    # Mullions and a door retain the glazed architectural identity.
    for x in (50,60,70,80,90): new_box(f"GLASS_FRONT_MULLION_{x}",x,12,4.0,.12,.16,7.5,"steel",f)

def build_f13():
    f=GROUPS["F13"][0];cx,cy,w,d=10,-2,50,20;shell(f,"LIQUID_V10",cx,cy,w,d,8,4)
    conveyor("LIQUID_BOTTLE_INFEED",-9,-2,8,1.7,f,1.65)
    # Infeed bottles.
    bottles("LIQUID_INFEED_BOTTLE",-12,-2,8,f,2.15)
    # Filler frame: bridge, four legs, rail, manifold and eight heads.
    for x in (-3.5,3.5):
        for y in (-3.0,-1.0): new_box(f"LIQUID_FILLER_COLUMN_{x}_{y}",x,y,3.0,.14,.14,3.9,"steel",f)
    new_box("LIQUID_FILLER_BRIDGE",0,-2,4.85,7.3,2.5,.28,"stainless",f)
    detail_pipe("LIQUID_PRODUCT_MANIFOLD",(-2.8,-2,5.6),(2.8,-2,5.6),f,.14,"teal")
    for i in range(8):
        x=-2.8+i*.8
        detail_pipe(f"LIQUID_FILL_HEAD_{i}",(x,-2,5.5),(x,-2,3.0),f,.07,"stainless")
        cyl(f"LIQUID_FILL_NOZZLE_{i}",(x,-2,2.96),.12,.18,"yellow",f,18)
    bottles("LIQUID_UNDER_FILLER",-2.9,-2,8,f,2.15)
    conveyor("LIQUID_TRANSFER_CONVEYOR",10,-2,8,1.7,f,1.65)
    # Cap bowl and descending chute meet the neck path.
    cyl("LIQUID_CAP_FEED_BOWL",(8,-4.6,4.2),1.0,.65,"yellow",f,32)
    detail_pipe("LIQUID_CAP_CHUTE",(8,-4.2,4.1),(10,-2,3.15),f,.12,"yellow")
    new_box("LIQUID_CAPPER_HEAD",10,-2,3.8,1.6,1.7,.65,"blue",f)
    for x in (12,16,20,24,28,32):
        conveyor(f"LIQUID_LINE_SEGMENT_{x}",x,-2,4,1.7,f,1.65)
    # Label applicator, roll, inspection camera, packer and finished cases.
    new_box("LIQUID_LABEL_APPLICATOR_FRAME",18,-2,3.0,2.2,2.6,3.4,"steel",f)
    cyl("LIQUID_LABEL_ROLL",(17,-3.45,4.2),.62,.25,"white",f,28,(math.pi/2,0,0))
    new_box("LIQUID_LABEL_WEB",18,-3.0,3.0,.08,.08,2.2,"soft",f)
    new_box("LIQUID_INSPECTION_CAMERA",22,-3.15,4.1,.55,.45,.48,"dark",f)
    detail_pipe("LIQUID_CAMERA_BRACKET",(22,-3.1,4.1),(22,-2,4.1),f,.05,"steel")
    new_box("LIQUID_CASE_PACKER_FRAME",29,-2,3.1,4.6,3.5,3.7,"teal",f)
    for i in range(4): pallet_case(f"LIQUID_CASE_GROUP_{i}",31+i*.9,-2,1.7,f,"white")
    bottles("LIQUID_FINISHED_BOTTLE",24,-2,8,f,2.15)
    new_box("LIQUID_HMI_PANEL",3,-4.4,2.5,.65,.12,1.0,"dark",f)
    for x in (-6,3,13,23,33):
        new_box(f"LIQUID_GUARD_POST_{x}",x,-.75,2.45,.09,.09,1.8,"yellow",f)

def build_f14():
    f=GROUPS["F14"][0];cx,cy,w,d=-18,-94,26,18;shell(f,"CLINIC_V10",cx,cy,w,d,7,2.8,True)
    # Reception / waiting zone.
    desk("CLINIC_V10_RECEPTION",-26,-89,3.5,1.05,f,"white")
    for i in range(4): chair(f"CLINIC_V10_WAIT_CHAIR_{i}",-25+i*1.6,-92,f,"purple")
    new_box("CLINIC_PRIVACY_TRACK",-13,-96,4.0,5.2,.08,.08,"steel",f)
    for y in (-94.2,-95.0,-95.8,-96.6): new_box(f"CLINIC_CURTAIN_FOLD_{y}",-13,y,2.8,5.0,.05,2.4,"soft",f)
    new_box("CLINIC_EXAM_BED_FRAME",-11,-98,1.55,2.2,5.2,.35,"steel",f)
    new_box("CLINIC_EXAM_MATTRESS",-11,-98,1.82,2.0,4.9,.25,"white",f)
    new_box("CLINIC_EXAM_HEAD_SUPPORT",-11,-100.1,2.04,1.9,.65,.18,"soft",f)
    new_box("CLINIC_BEDSIDE_TROLLEY_TOP",-14,-98,1.78,1.2,.72,.1,"stainless",f)
    new_box("CLINIC_BEDSIDE_TROLLEY_SHELF",-14,-98,1.25,1.15,.68,.09,"white",f)
    screen_detail("CLINIC_VITAL_MONITOR",-14,-97.6,2.65,f,.68,.5)
    new_box("CLINIC_MONITOR_STAND",-14,-97.6,1.98,.08,.08,1.2,"steel",f)
    new_box("CLINIC_SINK_COUNTER",-6,-99,1.72,3.2,.72,.12,"white",f)
    new_box("CLINIC_SINK_BASIN",-6,-99,1.82,.82,.48,.18,"stainless",f)
    detail_pipe("CLINIC_SINK_TAP",(-6,-99,1.9),(-6,-99,2.25),f,.035,"stainless")
    new_box("CLINIC_UNDERCOUNTER_CABINET",-6,-99,1.25,2.8,.62,.85,"white",f)
    new_box("CLINIC_WALL_MED_CABINET",-6,-91,3.5,2.7,.45,1.6,"white",f)
    for z in (3.0,3.6,4.2): new_box(f"CLINIC_SUPPLY_SHELF_{z}",-6,-90.65,z,2.8,.12,.08,"steel",f)
    new_box("CLINIC_HANDWASH_DISPENSER",-8,-90.6,2.65,.28,.25,.58,"teal",f)

def build_f15():
    f=GROUPS["F15"][0];cx,cy,w,d=-10,79,58,45;shell(f,"PKG_V10",cx,cy,w,d,9,5)
    rack("PKG_CARTON_RACKS",-27,82,3,5,f,"white")
    rack("PKG_CLOSURE_LABEL_RACKS",-8,82,3,4,f,"soft")
    # Packaging-specific rolls, mixed components and cartons.
    for i in range(8):
        x=-1+(i%4)*2.3;y=65+(i//4)*3.0
        cyl(f"PKG_FILM_ROLL_{i}",(x,y,2.2),.82,1.35,"blue",f,32,(math.pi/2,0,0))
        cyl(f"PKG_FILM_CORE_{i}",(x,y-.73,2.2),.18,.12,"wood",f,20,(math.pi/2,0,0))
    for i in range(6):
        x=10+(i%3)*2.2;y=84+(i//3)*2.0
        pallet_case(f"PKG_CARTON_PALLET_{i}",x,y,1.1,f,"white")
        new_box(f"PKG_CLOSURE_BIN_{i}",x,y+1.0,2.9,1.1,.8,.7,"yellow",f)
    # Receive/check side and issue-to-production side are separated by a clear aisle.
    new_box("PKG_INBOUND_MARKING",-27,96,1.11,11,8,.025,"orange",f)
    new_box("PKG_INBOUND_CHECK_DESK",-25,91,2.0,3.0,1.1,1.0,"wood",f)
    new_box("PKG_ISSUE_LANE",8,69,1.12,5,18,.03,"yellow",f)
    conveyor("PKG_ISSUE_TO_LINE_CONVEYOR",9,69,15,1.8,f,1.55)
    new_box("PKG_ISSUE_DESK",12,76,2.0,2.8,1.0,1.0,"blue",f)
    forklift("PKG_FORKLIFT_PARKED",-2,93,f)
    new_box("PKG_RECEIVING_DOCK",-27,100.9,1.12,14,1.4,.2,"steel",f)
    for x in (-32,-23):
        new_box(f"PKG_LOADING_DOOR_{x}",x,101.3,3.2,3.8,.14,5.4,"dark",f)
    new_box("PKG_PRODUCTION_ISSUE_OPENING",12,101.3,2.9,4.8,.12,4.5,"steel",f)

def add_camera_and_render(fid, group, name, bounds, role, qa_dir):
    cx,cy,w,d=bounds
    # Outward origin is behind the cutaway frontage and above the wall line.
    offsets={"A":(-w*.58,-d*1.65, max(18,d*.8)),"B":(-w*.42,-d*.82, max(10,d*.42)),"C":(-w*.1,-d*.60, max(7,d*.28))}
    dx,dy,z=offsets[role]
    target=Vector((cx,cy,2.9 if role!="C" else 3.1))
    if fid=="F09" and role=="C": target=Vector((56,82,2.7));dx=-29;dy=4;z=10
    if fid=="F11" and role=="B": target=Vector((91,-54,2.8));dx=-10;dy=-d*1.0;z=11
    if fid=="F11" and role=="C": target=Vector((91,-55,2.8));dx=7;dy=-d*1.1;z=10
    if fid=="F12" and role=="B": dx=-w*.3;dy=-d*1.5;z=12
    if fid=="F12" and role=="C": target=Vector((66,21,3.0));dx=-16;dy=-20;z=11
    if fid=="F13" and role=="B": target=Vector((12,-2,3));dx=-10;dy=-d*.9;z=10
    if fid=="F13" and role=="C": target=Vector((23,-2,2.65));dx=8;dy=-d*.85;z=8
    if fid=="F14" and role=="C": target=Vector((-11,-98,2.5));dx=7;dy=-d*.8;z=8
    if fid=="F15" and role=="C": target=Vector((7,70,2.4));dx=10;dy=-d*.7;z=10
    sc=bpy.data.scenes["M0847_QA_RENDER"]
    camdata=bpy.data.cameras.new(f"M0847_{fid}_{role}_DATA"); cam=bpy.data.objects.new(f"M0847_{fid}_{role}_CAMERA",camdata); sc.collection.objects.link(cam)
    cam.location=(cx+dx,cy+dy,z); cam.rotation_euler=(target-Vector(cam.location)).to_track_quat("-Z","Y").to_euler(); camdata.lens={"A":28,"B":38,"C":52}[role]
    if fid=="F12" and role=="B": camdata.lens=28
    if fid=="F12" and role=="C": camdata.lens=30
    camdata.clip_start=.1;camdata.clip_end=300
    sc.camera=cam
    # Render isolated target collection plus camera and dedicated QA lighting.
    old={o:o.hide_render for o in QA_OBJECTS}
    for o in QA_OBJECTS: o.hide_render=o not in set(group.objects)
    # QA cutaway only: preserve front facade and roof in saved model, reveal interior for evidence.
    qa_hidden=[]
    for o in group.objects:
        if any(s in o.name for s in ("_FRONT_L","_FRONT_R","_FRONT_HEADER","_FRONT_GLAZING","_SOFFIT")) or (fid=="F09" and role=="C" and "_LEFT_WALL" in o.name):
            o.hide_render=True;qa_hidden.append(o.name)
    # Add broad soft keys to retain material and shadow separation.
    lights=[]
    for i,(loc,power,size) in enumerate([((cx-w*.25,cy-d*.5,13),3800,11),((cx+w*.35,cy-d*.1,10),2600,8),((cx,cy+d*.45,12),2400,9)]):
        ld=bpy.data.lights.new(f"M0847_{fid}_{role}_AREA_{i}","AREA");ld.energy=power;ld.shape="DISK";ld.size=size
        lo=bpy.data.objects.new(ld.name,ld);sc.collection.objects.link(lo);lo.location=loc;lo.rotation_euler=(target-Vector(loc)).to_track_quat("-Z","Y").to_euler();lights.append(lo)
    sc.render.engine="BLENDER_EEVEE";sc.eevee.taa_render_samples=32
    sc.render.resolution_x=1280;sc.render.resolution_y=800;sc.render.resolution_percentage=100
    sc.view_settings.view_transform="AgX"
    if sc.world: sc.world.color=(.25,.25,.25)
    p=qa_dir/f"{fid}_{role}.png";sc.render.filepath=str(p)
    bpy.ops.render.render(write_still=True,scene=sc.name)
    # Camera-origin clearance against exact target mesh geometry via per-object world bounds.
    origin=Vector(cam.location);inside=[]
    for o in group.objects:
        if o.type!="MESH" or o.hide_render: continue
        pts=[o.matrix_world@Vector(v) for v in o.bound_box]
        lo=Vector((min(v.x for v in pts),min(v.y for v in pts),min(v.z for v in pts)))
        hi=Vector((max(v.x for v in pts),max(v.y for v in pts),max(v.z for v in pts)))
        if all(lo[i]-.02<=origin[i]<=hi[i]+.02 for i in range(3)): inside.append(o.name)
    for l in lights: bpy.data.objects.remove(l,do_unlink=True)
    for o,v in old.items(): o.hide_render=v
    return {"role":role,"camera_world":list(cam.location),"target":list(target),"camera_origin_inside_mesh_aabbs":inside,"qa_hidden_shell_objects":qa_hidden,"png":str(p.relative_to(ROOT)),"resolution":[1280,800],"camera_clear":not inside}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for fid in FACILITY_MAP:
        (OUT/fid).mkdir(exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(SOURCE))
    exec(V08.read_text(encoding="utf-8").split("def main():",1)[0], globals())
    globals()["V08_GROUPS"] = GROUPS
    globals()["GROUPS"] = FACILITY_MAP
    # Reapply the M08.47 evidence boundary after importing V08 utility definitions.
    globals()["OUT"] = ROOT / "output/rev005-facility-gated/F08_F15_combined"
    M["concrete"] = mat("M0847_Concrete",(.37,.39,.38),.04,.75)
    # The exact F08 R02 stage is the sole F08 starting state; do not reconstruct its anchors.
    expected="0BA679DDE639B8DC1C048D3025E313A89F66ACC5F8E7EFF3DD752066BA049F25"
    actual=hashlib.sha256(R02.read_bytes()).hexdigest().upper()
    if actual!=expected: raise RuntimeError(f"F08 R02 source SHA mismatch: {actual}")
    old_f08=bpy.data.collections[GROUPS["F08"][1]]
    for o in old_f08.objects: o.hide_render=True;o.hide_viewport=True
    with bpy.data.libraries.load(str(R02),link=False) as (src,dst):
        want="REV005_FG_F08_BOTTLE_BLOW_ACCEPTED_CLASS_N"
        if want not in src.collections: raise RuntimeError("F08 R02 destination collection absent")
        dst.collections=[want]
    f08col=next((c for c in dst.collections if c),None)
    if f08col is None: raise RuntimeError("F08 R02 collection append failed")
    bpy.context.scene.collection.children.link(f08col)
    # One exact, bounded replacement pass for each F09–F15 clean collection.
    builders={"F09":build_f09,"F10":build_f10,"F11":build_f11,"F12":build_f12,"F13":build_f13,"F14":build_f14,"F15":build_f15}
    facilities={"F08":f08col}
    for fid in ("F09","F10","F11","F12","F13","F14","F15"):
        _,cn,_=GROUPS[fid];col=get_col(cn);clear_col(col);builders[fid]();facilities[fid]=col
    # Add a visible mould-state bridge/detail only within the exact authorized R02 collection.
    CURRENT=f08col; globals()["CURRENT"]=CURRENT
    f="Bottle blow molding"
    # Opposed open mould halves, tie bars, stretch rods and transfer continuity.
    for i,cx in enumerate((55.7,58.3)):
        for side,sgn in (("L",-1),("R",1)):
            box(f"M0847_F08_STATION_{i+1}_OPEN_MOULD_{side}",(cx+sgn*.36,9.58,3.05),(.22,.62,1.55),"blue",f)
            box(f"M0847_F08_STATION_{i+1}_CAVITY_{side}",(cx+sgn*.23,9.24,3.05),(.08,.06,1.18),"yellow",f)
        for y in (8.6,11.4):
            cyl(f"M0847_F08_STATION_{i+1}_TIEBAR_{y}",(cx,y,3.05),.1,3.5,"steel",f,18,(0,math.pi/2,0))
        cyl(f"M0847_F08_STATION_{i+1}_STRETCH_ROD",(cx,10,4.18),.12,1.42,"stainless",f)
        detail_pipe(f"M0847_F08_STATION_{i+1}_AIR_NOZZLE",(cx,10,4.98),(cx,10,4.45),f,.11,"teal")
    cyl("M0847_F08_HEATED_PREFORM_BODY",(55.7,9.05,2.05),.055,.42,"orange",f,24)
    cyl("M0847_F08_HEATED_PREFORM_NECK",(55.7,9.05,2.30),.072,.10,"white",f,24)
    cyl("M0847_F08_RELEASED_BOTTLE_BODY",(58.3,9.05,1.92),.16,.38,"soft",f,28)
    bpy.ops.mesh.primitive_cone_add(vertices=28,radius1=.16,radius2=.075,depth=.13,location=(58.3,9.05,2.175))
    link(bpy.context.object,f); bpy.context.object.name="M0847_F08_RELEASED_BOTTLE_SHOULDER"
    cyl("M0847_F08_RELEASED_BOTTLE_NECK",(58.3,9.05,2.29),.075,.10,"white",f,24)
    cyl("M0847_F08_RELEASED_BOTTLE_BASE",(58.3,9.05,1.71),.16,.045,"blue",f,28)
    # Save stage before evidence rendering; render visibility never enters Blend/GLB.
    bpy.context.scene["M08_47_STATUS"]="STAGED_FOR_BUILDER_VISUAL_REVIEW"
    bpy.context.scene["M08_47_F08_R02_SOURCE_SHA256"]=actual
    bpy.context.scene["M08_47_CANONICAL_START_SHA256"]=hashlib.sha256(SOURCE.read_bytes()).hexdigest().upper()
    bpy.ops.wm.save_as_mainfile(filepath=str(STAGE),check_existing=False)
    # Render through a temporary scene that links only authorized facility
    # collections; the saved staged Blend retains the complete campus untouched.
    global QA_OBJECTS
    QA_OBJECTS={o for c in facilities.values() for o in c.objects}
    qasc=bpy.data.scenes.new("M0847_QA_RENDER")
    qasc.world=bpy.context.scene.world
    for c in facilities.values(): qasc.collection.children.link(c)
    indexpath=OUT/"M08_47_EVIDENCE_INDEX.json"
    if RENDER_ONLY and indexpath.exists(): evidence=json.loads(indexpath.read_text(encoding="utf-8"))
    else: evidence={"schema":"M08_47_F08_F15_EVIDENCE_V1","source_sha256":{"f08_r02":actual,"canonical_blend":hashlib.sha256(SOURCE.read_bytes()).hexdigest().upper()},"facilities":{}}
    for fid,(name,cn,bounds) in GROUPS.items():
        if fid not in evidence["facilities"]: evidence["facilities"][fid]={"name":name,"collection":cn if fid!="F08" else facilities[fid].name,"mesh_count":sum(o.type=="MESH" for o in facilities[fid].objects),"views":[]}
        roles=[r for r in ("A","B","C") if not RENDER_ONLY or f"{fid}_{r}" in RENDER_ONLY]
        for role in roles:
            view=add_camera_and_render(fid,facilities[fid],name,bounds,role,OUT/fid)
            oldviews=[x for x in evidence["facilities"][fid]["views"] if x["role"]!=role]
            evidence["facilities"][fid]["views"]=oldviews+[view]
    indexpath.write_text(json.dumps(evidence,indent=2),encoding="utf-8")
    print(json.dumps({"status":"STAGED_FOR_BUILDER_VISUAL_REVIEW","blend":str(STAGE),"facilities":{k:{"meshes":v["mesh_count"],"camera_clear":all(x["camera_clear"] for x in v["views"]),"images":[x["png"] for x in v["views"]]} for k,v in evidence["facilities"].items()}},indent=2))

main()
