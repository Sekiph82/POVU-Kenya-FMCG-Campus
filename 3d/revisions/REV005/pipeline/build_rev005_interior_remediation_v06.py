import bpy, hashlib, json, math
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v06"
BASELINE = OUT / "V06_BASELINE_HASHES.json"
V05_HELPERS = REV / "pipeline/build_rev005_interior_remediation_v05.py"

def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
if sha_file(BLEND) != baseline["blend"]["sha256"] or sha_file(GLB) != baseline["glb"]["sha256"]:
    raise RuntimeError("V06 baseline mismatch: refusing to mutate REV005")

# Reuse the established V05 low-level mesh helpers, but never execute its main().
source = V05_HELPERS.read_text(encoding="utf-8")
prefix = source.split("\ndef main():", 1)[0]
prefix = prefix.replace('COL = "REV005_INTERIOR_REMEDIATION_V05"', 'COL = "REV005_INTERIOR_REMEDIATION_V06"')
exec(compile(prefix, str(V05_HELPERS), "exec"), globals())
OUT = ROOT / "output/rev005-interior-remediation-v06"
OUT.mkdir(parents=True, exist_ok=True)

# V06 objects are independently tagged and kept in a separate collection.
def link(o, facility):
    for c in list(o.users_collection):
        c.objects.unlink(o)
    C.objects.link(o)
    o["REV005_REMEDIATION_V06"] = True
    o["facility"] = facility
    return o

def v06_box(name, loc, dims, material, facility, rot=None):
    return box("V06_" + name, loc, dims, material, facility, rot)

def v06_cyl(name, loc, radius, depth, material, facility, sides=24, rot=None):
    return cyl("V06_" + name, loc, radius, depth, material, facility, sides, rot)

def v06_pipe(name, a, b, radius, material, facility):
    return pipe("V06_" + name, a, b, radius, material, facility)

def room(prefix_name, x, y, w, d, h, facility, doors=True):
    envelope("V06_" + prefix_name, x, y, w, d, h, facility, doors)

def rail(name, x, y, z, length, facility, material="yellow"):
    v06_box(name + "_POST_L", (x - length / 2, y, z / 2), (.10, .10, z), material, facility)
    v06_box(name + "_POST_R", (x + length / 2, y, z / 2), (.10, .10, z), material, facility)
    v06_box(name + "_TOP", (x, y, z), (length, .10, .10), material, facility)

def product_row(name, x, y, z, count, spacing, facility, material="white"):
    for i in range(count):
        v06_cyl(f"{name}_{i}", (x + i * spacing, y, z), .16, .55, material, facility, 16, (math.pi / 2, 0, 0))

def admin_v06():
    f = "Administration / HQ / R&D / QC"; x, y = -58, -64; room("ADMIN", x, y, 52, 29, 7, f)
    v06_box("ADMIN_RECEPTION_DESK", (-78, -51, 2.3), (8, 1.2, 1.6), "wood", f); divider("V06_ADMIN_RECEPTION_SCREEN", -78, -52, 8, 4.3, f)
    for i in range(6):
        v06_box(f"ADMIN_WORKSTATION_{i}", (-70 + i * 5.2, -61, 2.1), (3.6, 2.8, 1.2), "wood", f)
        v06_box(f"ADMIN_MONITOR_{i}", (-70 + i * 5.2, -59.7, 3.5), (1.0, .10, .7), "teal", f)
    table_chairs("V06_ADMIN_COLLAB", -56, -55, 8, 3, f, 8)
    divider("V06_ADMIN_LAB_PARTITION", -42, -64, 12, 4.4, f)
    v06_box("ADMIN_LAB_BENCH", (-42, -70, 2.0), (13, 1.1, 1.5), "stainless", f)
    for i in range(4):
        v06_cyl(f"ADMIN_LAB_GLASSWARE_{i}", (-47 + i * 2.8, -69.2, 3.0), .22, .7, "white", f, 16)
        v06_box(f"ADMIN_LAB_INSTRUMENT_{i}", (-47 + i * 2.8, -70.2, 2.8), (1.1, .6, .5), "blue", f)
    rack("V06_ADMIN_LAB_STORAGE", -38, -75, 2, 4, f, "steel")

def bottle_v06():
    f = "Bottle blow molding"; room("BOTTLE", 52, 10, 38, 24, 8, f)
    v06_cyl("BOTTLE_PREFORM_HOPPER", (39, 11, 3.0), 2.0, 3.0, "yellow", f, 24)
    belt("V06_BOTTLE_PREFORM_FEED", 43, 11, 5, 1.2, f)
    product_row("BOTTLE_PREFORMS", 41.2, 11, 2.2, 7, .48, f, "pink")
    v06_box("BOTTLE_OVEN_FRAME", (47, 11, 3.5), (5.5, 4.2, 4.8), "orange", f)
    for i in range(6):
        v06_cyl(f"BOTTLE_HEATER_{i}", (45.2 + i * .65, 10.7, 3.8), .10, 2.9, "warm", f, 12, (math.pi / 2, 0, 0))
    v06_box("BOTTLE_BLOW_FRAME", (53, 11, 3.5), (5.5, 4.2, 5.0), "steel", f); guard("V06_BOTTLE_GUARD", 53, 11, 7, 5, f)
    v06_cyl("BOTTLE_MOULD_LEFT", (51.7, 11, 3.4), 1.0, 2.4, "blue", f, 20, (0, math.pi / 2, 0)); v06_cyl("BOTTLE_MOULD_RIGHT", (54.3, 11, 3.4), 1.0, 2.4, "blue", f, 20, (0, math.pi / 2, 0))
    belt("V06_BOTTLE_OUTFEED", 60, 11, 8, 1.3, f); product_row("BOTTLE_OUT_BOTTLES", 57, 11, 2.1, 8, .8, f, "soft")
    v06_box("BOTTLE_INSPECTION_HEAD", (65, 11, 3.5), (2.5, 2.5, 3.8), "white", f)

def chemical_v06():
    f = "Chemical compound / controlled receiving"; room("CHEMICAL", 56, 80, 36, 30, 8, f)
    for i, xx in enumerate((47, 56, 65)):
        v06_box(f"CHEM_BUND_WALL_{i}", (xx, 72, 1.3), (6.5, 6.5, .25), "yellow", f)
        v06_cyl(f"CHEM_TRANSFER_TANK_{i}", (xx, 72, 3.3), 2.0, 4.5, "steel", f)
        v06_pipe(f"CHEM_TANK_VALVE_{i}", (xx, 72, 5.5), (xx + 2.5, 75, 5.5), .12, "yellow", f)
    for i in range(3):
        v06_box(f"CHEM_IBC_{i}", (43 + i * 4.5, 90, 2.0), (2.6, 2.4, 2.5), "white", f)
        v06_box(f"CHEM_IBC_CAGE_{i}", (43 + i * 4.5, 90, 2.1), (2.8, 2.6, 2.8), "steel", f)
    for i in range(4): pallet(f"V06_CHEM_DRUM_PALLET_{i}", 60 + i * 3.3, 91, f, "red", .8)
    v06_box("CHEM_RECEIVING_STAGING", (56, 94, 1.1), (18, 3.5, .18), "orange", f)
    v06_box("CHEM_TRANSFER_PUMP", (70, 78, 2.0), (2, 2, 1.4), "stainless", f)
    v06_pipe("CHEM_HOSE", (65, 72, 5), (70, 78, 3), .16, "yellow", f); divider("V06_CHEM_CONTROL_DOOR", 72, 85, 5, 4, f)

def etp_v06():
    f = "ETP / water treatment"; room("ETP", 108, 35, 38, 32, 8, f)
    stages = ((96, 27, 2.6, "teal"), (104, 27, 2.3, "blue"), (112, 27, 2.5, "teal"))
    for i, (xx, yy, rr, mm) in enumerate(stages):
        v06_box(f"ETP_BASIN_BUND_{i}", (xx, yy, 1.15), (6.2, 6.2, .22), "yellow", f)
        v06_cyl(f"ETP_STAGE_VESSEL_{i}", (xx, yy, 3.4), rr, 4.6, mm, f)
        for j in range(3): v06_cyl(f"ETP_AERATION_{i}_{j}", (xx - 1 + j, yy, 5.6), .10, 1.4, "white", f, 12)
    for i in range(3):
        v06_cyl(f"ETP_FILTER_VESSEL_{i}", (99 + i * 3, 37, 3.2), .85, 4.4, "stainless", f)
        v06_box(f"ETP_FILTER_SKID_{i}", (99 + i * 3, 37, 1.2), (2, 2, .2), "steel", f)
    for i in range(3):
        v06_pipe(f"ETP_INTERSTAGE_{i}", (96 + i * 8, 27, 5.5), (99 + i * 3, 37, 5.5), .14, "yellow", f)
        machine(f"V06_ETP_PUMP_{i}", 116, 27 + i * 6, 1.6, 1.5, 1.5, f, "blue")
    v06_box("ETP_SERVICE_WALKWAY", (116, 36, 1.4), (2.2, 18, .18), "steel", f); rail("ETP_WALKWAY_RAIL", 116, 36, 2.5, 17, f)
    v06_box("ETP_SLUDGE_SKID", (116, 47, 2), (3, 2, 1.4), "orange", f)

def warehouse_v06(kind, x, y, w, d, f):
    room(kind, x, y, w, d, 9, f)
    if kind == "RAW":
        for row in (y - 12, y - 4, y + 4, y + 12): rack("V06_RAW_RACK" + str(row), x - w / 2 + 4, row, 3, 8, f, "steel")
        for i in range(6): pallet(f"V06_RAW_RECEIVING_{i}", x - w / 2 + 5 + i * 3, y + d / 2 - 3, f, "wood", 1.2)
        for i in range(4): v06_cyl(f"RAW_DRUM_{i}", (x + 14, y - 8 + i * 4, 2), .65, 1.4, "orange", f, 20)
        v06_box("RAW_RECEIVING_DOCK", (x, y + d / 2 - .1, 3), (14, .18, 4.5), "orange", f); v06_box("RAW_INSPECTION_DESK", (x + 12, y + d / 2 - 5, 2), (3, 1, 1.5), "wood", f)
        v06_box("RAW_IBC_STAGING", (x - 12, y + 12, 2), (3, 3, 2.5), "white", f)
    elif kind == "PACK":
        for row in (y - 12, y - 4, y + 4, y + 12): rack("V06_PACK_RACK" + str(row), x - w / 2 + 5, row, 3, 7, f, "teal")
        for i in range(5):
            v06_cyl(f"PACK_FILM_ROLL_{i}", (x + 10, y - 10 + i * 5, 2.0), .8, 1.8, "white", f, 24, (0, math.pi / 2, 0))
            v06_box(f"PACK_CARTON_BIN_{i}", (x + 3, y - 10 + i * 5, 1.4), (2.4, 2, 1.5), "orange", f)
        v06_box("PACK_RECEIVING_STAGING", (x, y - 1, 1.2), (12, 3, .18), "yellow", f); v06_box("PACK_ISSUE_WINDOW", (x + 20, y - 1, 2.2), (3, .2, 2.5), "glass", f)
    else:
        for row in (y - 7, y, y + 7): rack("V06_FG_RACK" + str(row), x - w / 2 + 5, row, 4, 9, f, "steel")
        for i in range(7): pallet(f"V06_FG_DISPATCH_PALLET_{i}", x - 8 + i * 2.6, y + d / 2 - 3, f, "wood", 1.25)
        v06_box("FG_LOADING_EDGE", (x, y + d / 2 - .1, 3), (14, .18, 4.5), "orange", f); v06_box("FG_DISPATCH_CONTROL", (x + 15, y + d / 2 - 4, 2), (3, 1, 1.5), "wood", f)
        for i in range(2):
            v06_box(f"FG_AMR_{i}", (x + 8 + i * 3, y - 2, 1), (1.5, 2.2, .4), "blue", f); v06_box(f"FG_AMR_LASER_{i}", (x + 8 + i * 3, y - 2, 1.4), (1.2, .05, .05), "red", f)

def glass_v06():
    f = "Glass Deck central command / training / café gallery"; room("GLASS_DECK", 70, 24, 10, 45, 17, f, False)
    v06_box("GLASS_COMMAND_MONITOR_WALL", (70, 38, 8), (8, .18, 10), "blue", f)
    for i in range(4):
        v06_box(f"GLASS_COMMAND_CONSOLE_{i}", (67 + i * 2, 34, 2.1), (1.2, 1, 1.4), "steel", f); v06_box(f"GLASS_COMMAND_SCREEN_{i}", (67 + i * 2, 33.4, 4.1), (1, .12, 1), "teal", f)
    divider("V06_GLASS_TRAINING_PARTITION", 70, 24, 8, 4.2, f); table_chairs("V06_GLASS_TRAINING", 70, 24, 6, 2.2, f, 8)
    v06_box("GLASS_CAFE_COUNTER", (70, 7, 2.2), (8, 1, 1.7), "wood", f); v06_box("GLASS_CAFE_BACKBAR", (70, 8.2, 5), (8, .18, 5), "blue", f)
    for i in range(3): machine(f"V06_GLASS_CAFE_EQUIPMENT_{i}", 67 + i * 2.5, 8.9, 1.0, .8, 1.8, f, "stainless")
    for i in range(4): table_chairs(f"V06_GLASS_CAFE_SEATING_{i}", 66 + i * 2.5, 4.5, 1.8, 1.4, f, 2)
    v06_box("GLASS_GALLERY_RAIL", (70, 14, 3), (7, .12, 1.0), "steel", f)

def liquid_v06():
    f = "Liquid filling / packaging"; room("LIQUID", 10, -2, 46, 20, 7, f)
    belt("V06_LIQUID_INFEED", -9, -2, 7, 1.2, f); product_row("LIQUID_BOTTLES", -11, -2, 1.9, 8, 1.0, f, "soft")
    v06_box("LIQUID_FILL_FRAME", (-2, -2, 3.2), (5, 3, 4.5), "steel", f)
    for i in range(6): v06_cyl(f"LIQUID_FILL_NOZZLE_{i}", (-3 + i * .8, -2, 5.4), .12, .9, "stainless", f, 16)
    belt("V06_LIQUID_TO_CAPPER", 5, -2, 7, 1.2, f); v06_cyl("LIQUID_CAPPER_TURRET", (10, -2, 3.4), 1.7, .8, "purple", f, 24)
    belt("V06_LIQUID_LABEL_LINE", 16, -2, 6, 1.2, f); v06_cyl("LIQUID_LABEL_ROLL", (16, -3.0, 3.2), 1.1, .7, "white", f, 24, (math.pi / 2, 0, 0))
    v06_box("LIQUID_INSPECTION_FRAME", (21, -2, 3), (2.4, 2.4, 3.5), "white", f); belt("V06_LIQUID_CASE_PACK", 27, -2, 7, 1.8, f); product_row("LIQUID_CASES", 25, -2, 2.0, 5, 1.3, f, "orange")

def clinic_v06():
    f = "Occupational health / first aid"; room("CLINIC", -18, -94, 24, 18, 6.5, f)
    v06_box("CLINIC_RECEPTION", (-25, -100.5, 2.2), (5, 1, 1.5), "wood", f); v06_box("CLINIC_WAITING_BENCH", (-24, -96, 1.6), (5, 1, .8), "teal", f)
    divider("V06_CLINIC_PRIVACY", -13, -94, 7, 3.6, f); v06_box("CLINIC_EXAM_BED", (-11, -99, 1.6), (2.2, 5, .55), "white", f); v06_box("CLINIC_BED_HEAD", (-11, -101.2, 2.7), (2.2, .18, 1.4), "blue", f)
    rack("V06_CLINIC_MED_STORAGE", -25, -88, 2, 3, f, "white"); v06_box("CLINIC_TREATMENT_TROLLEY", (-8, -97, 2), (1.2, .8, 1.3), "stainless", f); v06_box("CLINIC_WASH_BASIN", (-4, -89, 2), (2, 1, 1.2), "white", f)

def powder_v06():
    f = "Powder handling / packing"; room("POWDER", -48, 43, 36, 19, 7, f)
    v06_cyl("POWDER_FEED_HOPPER", (-62, 43, 3.25), 2, 4.5, "green", f); v06_pipe("POWDER_AUGER", (-60, 43, 5), (-54, 43, 4), .18, "green", f)
    v06_box("POWDER_DOSING_FRAME", (-53, 43, 3), (4, 3, 3.8), "steel", f); v06_cyl("POWDER_DOSING_SCREW", (-53, 43, 4.2), .25, 2.3, "white", f, 16)
    belt("V06_POWDER_FFS_INFEED", -47, 43, 8, 1.3, f); v06_box("POWDER_FFS_FORMER", (-43, 43, 3), (3, 2.6, 3.2), "orange", f); v06_box("POWDER_SEAL_JAWS", (-40, 43, 3), (1.5, 2.0, 2.4), "purple", f)
    for i in range(4): v06_box(f"POWDER_FINISHED_SACHET_{i}", (-38 + i * .8, 43, 1.8), (.55, .25, 1.0), "white", f)

def wet_process_v06():
    f = "Production Hall / Wet Processing / process core"; room("WET_PROCESS", 0, 24, 50, 32, 9, f)
    for i, (xx, yy, rr) in enumerate(((-16, 20, 3.0), (-6, 20, 2.8), (5, 20, 3.0), (16, 20, 2.6))):
        tank(f"V06_WET_MIX_TANK_{i}", xx, yy, rr, 5.5, f, "stainless"); v06_cyl(f"WET_AGITATOR_MOTOR_{i}", (xx, yy, 7.2), .55, .8, "blue", f); v06_pipe(f"WET_TANK_OUT_{i}", (xx + rr, yy, 4), (xx + rr + 4, yy, 4), .14, "yellow", f)
    v06_box("WET_PLATFORM", (0, 20, 1.7), (39, 2.2, .18), "steel", f); rail("WET_PLATFORM_RAIL", 0, 20.8, 2.6, 38, f)
    for i in range(4):
        machine(f"V06_WET_TRANSFER_PUMP_{i}", -13 + i * 9, 28, 1.8, 1.5, 1.6, f, "blue")
        v06_pipe(f"WET_MANIFOLD_{i}", (-13 + i * 9, 20, 5.5), (-13 + i * 9, 28, 4), .13, "teal", f)
    v06_box("WET_CIP_SKID", (20, 30, 2), (7, 3, 2.4), "green", f); v06_cyl("WET_CIP_TANK", (20, 30, 4.2), 1.2, 3.2, "stainless", f); v06_pipe("WET_CIP_RETURN", (20, 30, 5.8), (12, 20, 5.8), .16, "green", f)
    belt("V06_WET_TO_FILLING", 0, 35, 18, 1.3, f)

def restaurant_v06():
    f = "Restaurant / POVU Café / kitchen"; room("RESTAURANT", 5, -69, 45, 25, 7, f)
    v06_box("RESTAURANT_CAFE_COUNTER", (-10, -60.5, 2.2), (10, 1, 1.7), "wood", f); v06_box("RESTAURANT_BACKBAR", (-10, -59.4, 4.6), (10, .18, 4.6), "blue", f); machine("V06_RESTAURANT_COFFEE_EQUIPMENT", -8, -59.9, 1.2, .8, 1.8, f, "stainless")
    for i, (xx, yy) in enumerate(((-7, -67), (5, -67), (17, -67), (-7, -76), (5, -76), (17, -76))): table_chairs(f"V06_DINING_{i}", xx, yy, 3, 2.2, f, 4)
    divider("V06_RESTAURANT_KITCHEN_PARTITION", 5, -78, 20, 4.2, f); v06_box("RESTAURANT_PASS", (5, -75, 4), (14, .18, 1.6), "warm", f)
    for i in range(5): machine(f"V06_KITCHEN_APPLIANCE_{i}", -9 + i * 4.4, -80, 3.2, 1.4, 2.2, f, "stainless")
    v06_box("RESTAURANT_SINK", (13, -80, 2), (2.4, 1.2, 1.2), "white", f); rack("V06_KITCHEN_STORAGE", 18, -80, 2, 3, f, "steel")

def security_v06():
    f = "Security / reception / visitor arrival"; room("SECURITY", -58, -84, 48, 16, 6.5, f)
    v06_box("SECURITY_RECEPTION_DESK", (-67, -89.5, 2.2), (8, 1.1, 1.5), "wood", f); v06_box("SECURITY_MONITOR_WALL", (-67, -88.8, 4), (6, .12, 2.2), "blue", f)
    for i in range(4): v06_box(f"SECURITY_TURNSTILE_{i}", (-48 + i * 2.3, -88, 1.4), (.4, 2.2, 1.2), "steel", f)
    v06_box("SECURITY_SCREENING", (-42, -82, 1.6), (5, 2, .3), "stainless", f); divider("V06_SECURITY_WAITING", -65, -79, 12, 3.4, f); table_chairs("V06_VISITOR_WAITING", -74, -80, 3, 2, f, 4)

def gatehouse_v06():
    f = "Security gatehouse"; room("GATEHOUSE", 96, -106, 20, 14, 5.8, f)
    v06_box("GATEHOUSE_OPERATOR_DESK", (96, -110, 2.1), (5, 1, 1.4), "wood", f); v06_box("GATEHOUSE_CCTV_WALL", (96, -112.2, 3.6), (7, .14, 2.2), "blue", f)
    for i in range(3): v06_box(f"GATEHOUSE_WINDOW_{i}", (90 + i * 6, -99.1, 3.5), (4, .12, 2.2), "glass", f)
    v06_pipe("GATEHOUSE_BARRIER_ARM", (102, -101, 2.1), (115, -101, 2.1), .10, "yellow", f)
    v06_box("GATEHOUSE_BARRIER_POST", (102, -101, 1.4), (.35, .35, 2.6), "yellow", f); v06_box("GATEHOUSE_VEHICLE_LANE", (109, -106, .9), (18, 4, .18), "floor", f)

def toothpaste_v06():
    f = "Toothpaste production"; room("TOOTHPASTE", -12, 43, 40, 19, 7, f)
    tank("V06_PASTE_VACUUM_MIX", -26, 43, 2.5, 4.8, f, "green"); tank("V06_PASTE_HOLD", -20, 43, 1.8, 3.6, f, "stainless"); v06_pipe("PASTE_TRANSFER", (-18, 43, 4), (-12, 43, 4), .16, "teal", f)
    for i in range(5): v06_cyl(f"PASTE_TUBE_MAGAZINE_{i}", (-9 + i * .45, 43, 3), .16, 2.2, "white", f, 16, (math.pi / 2, 0, 0))
    v06_box("PASTE_FILL_FRAME", (-4, 43, 3), (3, 3, 3.8), "blue", f)
    for i in range(4): v06_cyl(f"PASTE_FILL_NOZZLE_{i}", (-4.8 + i * .6, 43, 5), .10, .8, "stainless", f, 12)
    v06_box("PASTE_CRIMP_JAWS", (1, 43, 3.2), (2.4, 2.4, 3.6), "purple", f); belt("V06_PASTE_CODE_LINE", 5, 43, 5, 1.0, f); v06_box("PASTE_CARTONER", (10, 43, 3.0), (3, 3, 3.4), "orange", f)

def training_v06():
    f = "Training / Academy"; room("TRAINING", 30, -61, 26, 18, 6.5, f)
    v06_box("TRAINING_PRESENTATION_SCREEN", (30, -69.7, 4), (12, .18, 4), "blue", f); v06_box("TRAINING_INSTRUCTOR_DESK", (30, -66.5, 2), (4, 1, 1.4), "wood", f)
    for i, (xx, yy) in enumerate(((24, -62), (31, -62), (24, -57), (31, -57))): table_chairs(f"V06_CLASSROOM_{i}", xx, yy, 4, 2, f, 4)
    rack("V06_TRAINING_STORAGE", 40, -56, 2, 2, f, "steel"); v06_box("TRAINING_DOOR", (42, -69.8, 3), (3, .16, 5.5), "glass", f)

def utilities_v06():
    f = "Utilities / engineering"; room("UTILITIES", 96, 75, 34, 30, 8, f)
    machine("V06_UTIL_COMPRESSOR", 85, 68, 5, 3, 3, f, "blue"); v06_cyl("UTIL_AIR_RECEIVER", (91, 68, 3), 1.5, 4.5, "steel", f); v06_box("UTIL_DRYER", (94, 68, 2), (2, 2, 2.5), "teal", f)
    tank("V06_UTIL_BOILER", 100, 68, 2, 4.5, f, "orange"); v06_pipe("UTIL_STEAM_MANIFOLD", (100, 68, 5.5), (100, 82, 5.5), .16, "yellow", f)
    for i in range(3): tank(f"V06_UTIL_RO_COLUMN_{i}", 108 + i * 2, 68, .7, 4, f, "stainless")
    v06_box("UTIL_RO_SKID", (110, 72, 1.3), (8, 3, .25), "steel", f)
    for i in range(4): v06_pipe(f"UTIL_DISTRIBUTION_{i}", (84 + i * 8, 82, 4.8), (84 + i * 8, 82, 6.5), .11, "teal", f)
    v06_box("UTIL_MAINTENANCE_BENCH", (88, 84, 2), (8, 1, 1.3), "wood", f); rail("UTIL_SERVICE_RAIL", 96, 79, 2.2, 12, f)

def wellness_v06():
    f = "Wellness / recreation"; room("WELLNESS", 30, -70, 28, 22, 6.5, f)
    for i in range(3):
        v06_box(f"WELLNESS_TREADMILL_{i}", (21 + i * 4, -64, 1.2), (2.2, 4, .25), "teal", f); v06_box(f"WELLNESS_TREADMILL_HANDLE_{i}", (21 + i * 4, -62.5, 2.5), (.10, .10, 2.5), "steel", f)
    for i in range(4): v06_box(f"WELLNESS_YOGA_MAT_{i}", (22 + i * 4, -74, 1.2), (2.4, 5, .08), "purple", f)
    for i in range(3): v06_cyl(f"WELLNESS_WEIGHT_{i}", (24 + i * 3, -80, 1.5), .5, .35, "steel", f, 20, (math.pi / 2, 0, 0))
    rack("V06_WELLNESS_LOCKER", 40, -76, 2, 3, f, "steel"); divider("V06_WELLNESS_MIRROR", 17, -70, 8, 3.4, f)

def wipes_v06():
    f = "Wet wipes production"; room("WIPES", 22, 43, 50, 19, 7, f)
    for i, xx in enumerate((4, 7)): v06_cyl(f"WIPES_PARENT_ROLL_{i}", (xx, 43, 3.4), 1.5, .8, "white", f, 32, (0, math.pi / 2, 0))
    belt("V06_WIPES_UNWIND", 11, 43, 7, 1.0, f); v06_box("WIPES_WETTING_BATH", (17, 43, 2.2), (4, 2.5, 1.1), "green", f)
    for i in range(5): v06_cyl(f"WIPES_WEB_ROLLER_{i}", (20 + i * 3, 43, 3), .35, 2.0, "stainless", f, 20, (0, math.pi / 2, 0))
    belt("V06_WIPES_WEB_PATH", 24, 43, 8, .9, f); v06_box("WIPES_FOLD_FRAME", (30, 43, 3.2), (3, 2.4, 3.8), "steel", f); v06_box("WIPES_CUT_STACK", (35, 43, 2.5), (3, 2.5, 2.5), "yellow", f)
    belt("V06_WIPES_POUCH_FORM", 41, 43, 7, 1.2, f); v06_cyl("WIPES_FILM_ROLL", (42, 41.8, 4), 1.1, .8, "white", f, 24, (math.pi / 2, 0, 0)); v06_box("WIPES_SEAL_JAWS", (46, 43, 3.2), (3, 2.5, 3.2), "red", f); belt("V06_WIPES_DISCHARGE", 50, 43, 5, 1.2, f)

def main():
    facility_builders = [admin_v06, bottle_v06, chemical_v06, etp_v06,
        lambda: warehouse_v06("FG", 80, -51, 52, 24, "Finished goods warehouse / dispatch"), glass_v06,
        liquid_v06, clinic_v06,
        lambda: warehouse_v06("PACK", -10, 79, 58, 45, "Packaging warehouse"), powder_v06, wet_process_v06,
        lambda: warehouse_v06("RAW", -78, 79, 54, 38, "Raw material warehouse / receiving"), restaurant_v06,
        security_v06, gatehouse_v06, toothpaste_v06, training_v06, utilities_v06, wellness_v06, wipes_v06]
    for builder in facility_builders:
        builder()
    scene = bpy.context.scene
    scene["REV005_REMEDIATION_V06_STATUS"] = "AWAITING_GPT_REMEDIATION_AUDIT_V06"
    scene["REV005_REMEDIATION_V06_COLLECTION"] = COL
    scene["REV005_V05_BASELINE_BLEND_SHA256"] = baseline["blend"]["sha256"]
    scene["REV005_V05_BASELINE_GLB_SHA256"] = baseline["glb"]["sha256"]
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)
    result = {
        "status": "BUILT",
        "revision": "REV005",
        "task": "M08.12",
        "collection": COL,
        "preserved_v05_pass_groups": ["Caps and Trigger Assembly", "Daycare / Crèche", "Electrical / LV-MV Room", "Employee Changing / Shower / Locker Support", "Fire Pump House", "Micro-ingredient Weigh / Dispense"],
        "remediated_group_count": 20,
        "baseline_file": str(BASELINE),
        "before_blend_sha256": baseline["blend"]["sha256"],
        "before_glb_sha256": baseline["glb"]["sha256"],
        "after_blend_sha256": sha_file(BLEND),
        "after_glb_sha256": sha_file(GLB),
        "object_count": len(C.objects),
        "blend": str(BLEND),
        "glb": str(GLB),
        "no_hiveai": not (ROOT / ".hiveai").exists(),
        "no_rev006": not (ROOT / "3d/revisions/REV006").exists(),
        "no_tour": not any((ROOT / "output/rev005-interior-remediation-v06").glob("*.mp4")),
    }
    (OUT / "BUILD_RESULT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
