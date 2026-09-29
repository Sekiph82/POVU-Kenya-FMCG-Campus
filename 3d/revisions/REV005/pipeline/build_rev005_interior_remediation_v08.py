import bpy
import hashlib
import json
import math
import re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v08"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
BASELINE = OUT / "V08_BASELINE_HASHES.json"

PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
}
GROUPS = [
    "Administration / HQ / R&D / QC", "Bottle blow molding", "Chemical compound / controlled receiving",
    "ETP / water treatment", "Finished goods warehouse / dispatch", "Glass Deck central command / training / café gallery",
    "Liquid filling / packaging", "Occupational health / first aid", "Packaging warehouse", "Powder handling / packing",
    "Production Hall / Wet Processing / process core", "Raw material warehouse / receiving", "Restaurant / POVU Café / kitchen",
    "Security / reception / visitor arrival", "Security gatehouse", "Toothpaste production", "Training / Academy",
    "Utilities / engineering", "Wellness / recreation", "Wet wipes production",
]

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()

def same_group(a, b):
    aa, bb = norm(a), norm(b)
    if aa == bb or aa in bb or bb in aa:
        return True
    if "glass deck" in aa and "glass deck" in bb:
        return True
    if "wet processing" in aa and ("wet processing" in bb or "production hall" in bb):
        return True
    return False

def slug(group):
    return re.sub(r"[^A-Z0-9]+", "_", group.upper()).strip("_")

def mat(name, color, metal=0.0, rough=.4):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bs = m.node_tree.nodes.get("Principled BSDF")
    if bs:
        bs.inputs["Base Color"].default_value = (*color, 1)
        bs.inputs["Metallic"].default_value = metal
        bs.inputs["Roughness"].default_value = rough
    return m

M = {
    "floor": mat("REV005_V08_FLOOR", (.12, .17, .20), .1, .42),
    "wall": mat("REV005_V08_WALL", (.54, .62, .66), .05, .46),
    "glass": mat("REV005_V08_GLASS", (.04, .38, .56), .35, .16),
    "steel": mat("REV005_V08_STEEL", (.16, .22, .27), .8, .23),
    "stainless": mat("REV005_V08_STAINLESS", (.64, .70, .74), .88, .18),
    "blue": mat("REV005_V08_BLUE", (.02, .12, .42), .25, .28),
    "teal": mat("REV005_V08_TEAL", (.01, .48, .58), .2, .25),
    "orange": mat("REV005_V08_ORANGE", (.88, .24, .03), .12, .34),
    "yellow": mat("REV005_V08_YELLOW", (.98, .58, .01), .08, .34),
    "green": mat("REV005_V08_GREEN", (.02, .42, .18), .18, .32),
    "purple": mat("REV005_V08_PURPLE", (.56, .08, .35), .18, .34),
    "white": mat("REV005_V08_WHITE", (.88, .90, .91), .04, .32),
    "dark": mat("REV005_V08_DARK", (.01, .02, .025), .3, .2),
    "wood": mat("REV005_V08_WOOD", (.42, .19, .05), 0, .5),
    "warm": mat("REV005_V08_WARM", (.93, .40, .05), .05, .4),
    "red": mat("REV005_V08_RED", (.78, .03, .02), .05, .36),
    "soft": mat("REV005_V08_SOFT", (.06, .48, .70), .05, .48),
}

COLLECTIONS = {}
CURRENT = None

def link(obj, facility):
    for collection in list(obj.users_collection):
        collection.objects.unlink(obj)
    CURRENT.objects.link(obj)
    obj["REV005_V08_CLEAN"] = True
    obj["facility"] = facility
    return obj

def mesh(name, verts, faces, loc, material, facility):
    data = bpy.data.meshes.new(name + "_MESH")
    data.from_pydata(verts, [], faces)
    data.update()
    obj = link(bpy.data.objects.new(name, data), facility)
    obj.location = loc
    obj.data.materials.append(M[material])
    return obj

def box(name, loc, dims, material, facility, rot=None):
    x, y, z = [v / 2 for v in dims]
    verts = [(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]
    faces = [(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    obj = mesh(name, verts, faces, loc, material, facility)
    if rot:
        obj.rotation_euler = rot
    return obj

def cyl(name, loc, radius, depth, material, facility, sides=20, rot=None):
    verts = []
    for z in (-depth / 2, depth / 2):
        for i in range(sides):
            a = math.tau * i / sides
            verts.append((radius * math.cos(a), radius * math.sin(a), z))
    faces = [tuple(range(sides - 1, -1, -1)), tuple(range(sides, 2 * sides))]
    faces += [(i, (i + 1) % sides, sides + (i + 1) % sides, sides + i) for i in range(sides)]
    obj = mesh(name, verts, faces, loc, material, facility)
    if rot:
        obj.rotation_euler = rot
    return obj

def pipe(name, a, b, radius, material, facility):
    a, b = Vector(a), Vector(b)
    d = b - a
    obj = cyl(name, (a + b) / 2, radius, d.length, material, facility, 14)
    obj.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    return obj

def envelope(prefix, x, y, w, d, h, facility, glazing=False):
    box(prefix + "_FLOOR", (x, y, 1.0), (w, d, .18), "floor", facility)
    box(prefix + "_BACK_WALL", (x, y + d / 2, h / 2), (w, .18, h), "wall", facility)
    box(prefix + "_LEFT_WALL", (x - w / 2, y, h / 2), (.18, d, h), "wall", facility)
    box(prefix + "_RIGHT_WALL", (x + w / 2, y, h / 2), (.18, d, h), "wall", facility)
    box(prefix + "_SOFFIT", (x, y, h - .15), (w, d, .18), "steel", facility)
    if glazing:
        box(prefix + "_FRONT_GLAZING", (x, y - d / 2, h / 2), (w, .12, h - .4), "glass", facility)
    else:
        box(prefix + "_FRONT_HEADER", (x, y - d / 2, h - .8), (w, .16, 1.0), "steel", facility)

def partition(name, x, y, w, h, facility):
    box(name + "_PANEL", (x, y, h / 2), (w, .12, h), "glass", facility)
    box(name + "_POST", (x, y, h / 2), (.14, .18, h), "steel", facility)

def desk(name, x, y, w, d, facility, material="wood"):
    box(name + "_TOP", (x, y, 2.05), (w, d, .16), material, facility)
    for dx in (-w * .38, w * .38):
        box(name + "_LEG_" + str(dx), (x + dx, y, 1.1), (.12, d * .7, 1.8), "steel", facility)

def rack(name, x, y, levels, bays, facility, load="white"):
    for bay in range(bays):
        xx = x + bay * 2.5
        for level in range(levels):
            z = 2.2 + level * 1.8
            box(f"{name}_POST_{bay}_{level}", (xx, y, z), (.14, .18, 3.3), "steel", facility)
            box(f"{name}_LOAD_{bay}_{level}", (xx + 1.0, y, z), (1.9, .9, .7), load, facility)
        box(f"{name}_BEAM_{bay}", (xx + 1.0, y, 1.6 + levels * 1.8), (2.4, .18, .16), "steel", facility)

def conveyor(name, x, y, length, width, facility, z=1.55, material="stainless"):
    box(name + "_BED", (x, y, z), (length, width, .22), material, facility)
    for i in range(7):
        px = x - length / 2 + .5 + i * (length - 1.0) / 6
        cyl(name + f"_ROLLER_{i}", (px, y, z + .2), width * .36, .12, "dark", facility, 14, (0, math.pi / 2, 0))
    for yy in (y - width / 2, y + width / 2):
        box(name + "_GUARD_" + str(yy), (x, yy, z + .75), (length, .10, 1.25), "yellow", facility)

def machine(name, x, y, w, d, h, facility, material="blue"):
    box(name + "_BODY", (x, y, 1.0 + h / 2), (w, d, h), material, facility)
    box(name + "_SERVICE_PANEL", (x, y - d / 2 - .06, 1.0 + h * .62), (w * .55, .10, h * .25), "teal", facility)
    box(name + "_BASE", (x, y, 1.12), (w + .35, d + .35, .20), "steel", facility)

def tank(name, x, y, r, h, facility, material="stainless"):
    cyl(name + "_VESSEL", (x, y, 1.0 + h / 2), r, h, material, facility, 26)
    cyl(name + "_LID", (x, y, 1.0 + h + .12), r * .72, .18, "steel", facility, 22)
    cyl(name + "_AGITATOR", (x, y, 1.0 + h + .42), .12, .55, "dark", facility, 14)

def rails(prefix, x, y, length, facility):
    for yy in (y - 1.0, y + 1.0):
        box(prefix + "_RAIL_" + str(yy), (x, yy, 2.3), (length, .08, 1.6), "yellow", facility)
    for i in range(5):
        box(prefix + "_POST_" + str(i), (x - length / 2 + i * length / 4, y, 1.55), (.08, 2.1, 1.2), "yellow", facility)

def bottles(prefix, x, y, count, facility, z=2.0):
    for i in range(count):
        xx = x + i * 1.15
        cyl(f"{prefix}_BOTTLE_{i}", (xx, y, z), .28, .95, "soft", facility, 16)
        cyl(f"{prefix}_NECK_{i}", (xx, y, z + .6), .13, .25, "white", facility, 14)

def hide_legacy(group):
    hidden = []
    for obj in bpy.data.objects:
        if obj.get("REV005_V08_CLEAN"):
            continue
        if same_group(group, obj.get("facility")):
            obj.hide_render = True
            obj.hide_viewport = True
            obj["REV005_V08_LEGACY_RETIRED"] = True
            obj["REV005_V08_RETIRED_GROUP"] = group
            hidden.append(obj.name)
    return sorted(hidden)

def new_collection(group):
    name = "REV005_V08_CLEAN_" + slug(group)
    old = bpy.data.collections.get(name)
    if old:
        for obj in list(old.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(old)
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    COLLECTIONS[group] = col
    return col

def admin():
    f = GROUPS[0]; envelope("V08_ADMIN", -58, -64, 46, 28, 7, f, True)
    desk("V08_ADMIN_RECEPTION", -77, -51.5, 8, 1.2, f)
    partition("V08_ADMIN_RECEPTION_PARTITION", -77, -54, 8, 4, f)
    for i in range(6):
        desk(f"V08_ADMIN_WORKSTATION_{i}", -71 + i * 4.6, -61, 3.2, 2.4, f)
        box(f"V08_ADMIN_MONITOR_{i}", (-71 + i * 4.6, -59.8, 2.8), (1.0, .10, .65), "teal", f)
    desk("V08_ADMIN_MEETING", -57, -55, 9, 3, f)
    for i in range(8): cyl(f"V08_ADMIN_MEETING_CHAIR_{i}", (-61 + (i % 4) * 2.6, -57 + (i // 4) * 4.2, 1.5), .32, .65, "purple", f, 14)
    partition("V08_ADMIN_LAB_PARTITION", -42, -64, 12, 4.5, f)
    for i in range(3):
        desk(f"V08_QC_LAB_BENCH_{i}", -47 + i * 4.2, -70, 3.4, 1.0, f, "stainless")
        for j in range(3): cyl(f"V08_QC_LAB_INSTR_{i}_{j}", (-48 + i * 4.2 + j * .7, -69.5, 2.8), .22, .55, "blue", f, 14)
    rack("V08_QC_LAB_STORAGE", -39, -75, 2, 4, f, "white")

def bottle():
    f = GROUPS[1]; envelope("V08_BOTTLE", 52, 10, 38, 24, 8, f)
    machine("V08_PREFORM_HOPPER", 38, 10, 3, 3, 3.6, f, "yellow")
    conveyor("V08_PREFORM_FEED", 43, 10, 6, 1.2, f); machine("V08_HEATER_OVEN", 48, 10, 5, 4, 4.8, f, "orange")
    for i in range(5): cyl(f"V08_HEATER_COIL_{i}", (46.4 + i * .8, 8.0, 4.8), .10, 2.6, "red", f, 12, (math.pi / 2, 0, 0))
    machine("V08_GUARDED_BLOW_MOULD", 55, 10, 6, 4, 5.5, f, "blue")
    for xx in (52, 58):
        box(f"V08_MOULD_FRAME_{xx}", (xx, 8.0, 3.8), (.14, .14, 4.8), "yellow", f)
    conveyor("V08_FORMED_BOTTLE_OUTFEED", 64, 10, 9, 1.5, f); bottles("V08_OUTFEED", 61, 10, 7, f)
    desk("V08_BLOW_OPERATOR", 70, 16, 4, 1, f)

def chemical():
    f = GROUPS[2]; envelope("V08_CHEMICAL", 56, 80, 38, 30, 8, f)
    box("V08_CHEM_DOCK", (56, 94.7, 3), (18, .16, 4.5), "orange", f)
    for i, xx in enumerate((46, 56, 66)):
        box(f"V08_BUND_{i}", (xx, 74, 1.16), (7, 7, .22), "yellow", f)
        tank(f"V08_CHEM_TANK_{i}", xx, 74, 2.1, 5.2, f, "stainless")
        machine(f"V08_TRANSFER_PUMP_{i}", xx + 3.5, 74, 1.2, 1.2, 1.2, f, "blue")
    for i in range(6):
        cyl(f"V08_CHEM_DRUM_{i}", (43 + i * 4.2, 90, 1.7), .7, 1.4, "red", f, 18)
    for i in range(3):
        box(f"V08_CHEM_IBC_{i}", (72, 88 - i * 4, 2.0), (2.2, 2.2, 2.2), "white", f)
    pipe("V08_CHEM_TRANSFER_HEADER", (46, 74, 6), (66, 74, 6), .16, "yellow", f)
    pipe("V08_CHEM_TRANSFER_TO_DOCK", (66, 74, 6), (70, 90, 3), .14, "yellow", f)
    partition("V08_CONTROLLED_ACCESS", 72, 84, 7, 4.4, f)
    desk("V08_CHEM_RECEIVING_DESK", 44, 85, 4, 1, f)

def etp():
    f = GROUPS[3]; envelope("V08_ETP", 108, 35, 40, 32, 8, f)
    for i, (xx, label) in enumerate(((96, "EQUALISATION"), (105, "AERATION"), (114, "CLARIFIER"))):
        box(f"V08_ETP_BUND_{label}", (xx, 27, 1.1), (7, 7, .22), "yellow", f)
        tank(f"V08_ETP_{label}", xx, 27, 2.4, 4.8, f, "teal")
        box(f"V08_ETP_MOTOR_{label}", (xx, 27, 6.0), (1, 1, .5), "dark", f)
    for i in range(4):
        tank(f"V08_ETP_FILTER_{i}", 99 + i * 3.5, 38, .85, 4.5, f, "stainless")
        machine(f"V08_ETP_PUMP_{i}", 99 + i * 3.5, 44, 1.0, 1.2, 1.2, f, "blue")
    for x1, y1, x2, y2 in ((96,27,105,27),(105,27,114,27),(114,27,99,38),(113,38,113,47)):
        pipe("V08_ETP_PROCESS_PIPE", (x1, y1, 5.5), (x2, y2, 5.5), .16, "yellow", f)
    rails("V08_ETP_WALKWAY", 118, 37, 18, f)
    box("V08_ETP_SLUDGE_BIN", (118, 47, 2), (3, 2, 2), "orange", f)
    box("V08_ETP_DISCHARGE", (116, 48, 2), (2, 1.5, 1.4), "blue", f)

def warehouse(kind, group, x, y, w, d, load):
    f = group; envelope("V08_" + kind, x, y, w, d, 9, f)
    if kind == "RAW":
        for i, row in enumerate((y - 11, y - 3, y + 5, y + 13)): rack(f"V08_RAW_RACK_{i}", x - w / 2 + 4, row, 3, 7, f, "orange")
        box("V08_RAW_RECEIVING_DOCK", (x, y + d / 2 - .1, 3), (16, .18, 4.5), "orange", f)
        for i in range(6): cyl(f"V08_RAW_DRUM_{i}", (x + 11, y - 9 + i * 3.2, 1.7), .7, 1.4, "orange", f, 18)
        for i in range(3): box(f"V08_RAW_IBC_{i}", (x + 16, y + 7 - i * 4, 2), (2.2, 2.2, 2.2), "white", f)
        desk("V08_RAW_INSPECTION", x + 12, y + d / 2 - 5, 4, 1, f)
    elif kind == "PACK":
        for i, row in enumerate((y - 13, y - 5, y + 3, y + 11)): rack(f"V08_PACK_RACK_{i}", x - w / 2 + 4, row, 3, 7, f, "teal")
        for i in range(5):
            cyl(f"V08_PACK_FILM_ROLL_{i}", (x + 11, y - 10 + i * 5, 2.0), 1.0, 1.2, "white", f, 20, (0, math.pi / 2, 0))
            box(f"V08_PACK_CARTONS_{i}", (x + 16, y - 10 + i * 5, 1.7), (2.0, 2.0, 1.5), "orange", f)
        conveyor("V08_PACK_ISSUE_TO_PRODUCTION", x - 2, y + 1, 14, 1.5, f)
    else:
        for i, row in enumerate((y - 8, y, y + 8)): rack(f"V08_FG_RACK_{i}", x - w / 2 + 4, row, 4, 8, f, "steel")
        box("V08_FG_CONSOLIDATION", (x, y + 8, 1.2), (12, 4, .2), "yellow", f)
        for i in range(8):
            box(f"V08_FG_PALLET_{i}", (x - 9 + i * 2.5, y + d / 2 - 3, 1.8), (1.8, 1.4, 1.6), "white", f)
        box("V08_FG_LOADING_EDGE", (x, y + d / 2 - .1, 3), (15, .18, 4.5), "orange", f)
        for i in range(2): box(f"V08_FG_AMR_{i}", (x + 7 + i * 3, y - 2, 1.1), (1.6, 2.3, .45), "blue", f)
        desk("V08_FG_DISPATCH_CONTROL", x + 15, y + d / 2 - 4, 4, 1, f)

def glass():
    f = GROUPS[5]; envelope("V08_GLASS_DECK", 70, 24, 40, 24, 7, f, True)
    box("V08_COMMAND_MONITOR_WALL", (70, 34, 4.8), (28, .16, 3.6), "blue", f)
    for i in range(5):
        desk(f"V08_COMMAND_CONSOLE_{i}", 58 + i * 6, 31, 4, 1.4, f, "steel")
        box(f"V08_COMMAND_SCREEN_{i}", (58 + i * 6, 30.2, 3.9), (2.2, .12, 1.2), "teal", f)
    desk("V08_TRAINING_TABLE", 70, 24, 15, 4, f)
    for i in range(8): cyl(f"V08_TRAINING_SEAT_{i}", (63 + (i % 4) * 4.6, 20 + (i // 4) * 7, 1.5), .33, .7, "purple", f, 14)
    box("V08_TRAINING_SCREEN", (70, 17, 4.5), (12, .12, 3.5), "soft", f)
    box("V08_CAFE_COUNTER", (70, 10, 2.0), (14, 1.2, 1.7), "wood", f)
    box("V08_CAFE_BACKBAR", (70, 11.2, 4.3), (14, .16, 4.6), "blue", f)
    for i in range(4): cyl(f"V08_CAFE_SEAT_{i}", (64 + i * 4, 7.5, 1.5), .35, .7, "orange", f, 14)

def liquid():
    f = GROUPS[6]; envelope("V08_LIQUID", 10, -2, 50, 20, 7, f)
    conveyor("V08_LIQUID_BOTTLE_INFEED", -10, -2, 8, 1.4, f); bottles("V08_LIQUID_INFEED", -12, -2, 6, f)
    machine("V08_LIQUID_FILLER", -3, -2, 5, 3, 4.5, f)
    for i in range(6): cyl(f"V08_FILL_NOZZLE_{i}", (-5 + i * .8, -2, 5.2), .13, .9, "stainless", f, 14)
    conveyor("V08_LIQUID_CAP_FEED", 5, -2, 7, 1.4, f); machine("V08_LIQUID_CAPPER", 10, -2, 4, 3, 4, f, "purple")
    conveyor("V08_LIQUID_LABEL_INSPECTION", 17, -2, 8, 1.4, f); box("V08_LABEL_ROLL", (15, -3.3, 3.2), (1.1, .8, 3), "white", f)
    machine("V08_LIQUID_VISION", 21, -2, 2.5, 2.4, 3.7, f, "white"); conveyor("V08_LIQUID_CASE_PACK", 28, -2, 8, 1.8, f); machine("V08_LIQUID_CASE_SEALER", 34, -2, 3.5, 3, 3.4, f, "orange")
    for i in range(3): box(f"V08_LIQUID_CASE_OUT_{i}", (39 + i * 2, -2, 1.9), (1.7, 1.5, 1.4), "white", f)

def powder():
    f = GROUPS[9]; envelope("V08_POWDER", -48, 43, 38, 19, 7, f)
    tank("V08_POWDER_HOPPER", -62, 43, 2.0, 4.5, f, "green")
    pipe("V08_POWDER_AUGER", (-60, 43, 5), (-54, 43, 4), .18, "green", f)
    machine("V08_POWDER_DOSER", -52, 43, 4, 3, 3.8, f, "blue")
    conveyor("V08_POWDER_FFS", -46, 43, 8, 1.3, f)
    box("V08_POWDER_FORM_FILL_SEAL", (-41, 43, 3.0), (3, 2.6, 3.5), "orange", f)
    for i in range(4):
        box(f"V08_POWDER_SACHET_{i}", (-37 + i * 1.2, 43, 1.9), (.8, .7, 1.3), "white", f)
    box("V08_POWDER_DUST_HOOD", (-52, 43, 6.1), (10, 3.8, .18), "steel", f)
    conveyor("V08_POWDER_OUTFEED", -36, 43, 6, 1.4, f)

def clinic():
    f = GROUPS[7]; envelope("V08_CLINIC", -18, -94, 26, 18, 6.5, f)
    desk("V08_CLINIC_RECEPTION", -25, -100, 6, 1.1, f)
    for i in range(3): cyl(f"V08_CLINIC_WAIT_{i}", (-26 + i * 2.2, -96, 1.5), .35, .7, "teal", f, 14)
    partition("V08_CLINIC_PRIVACY", -12, -94, 8, 4.5, f)
    box("V08_CLINIC_EXAM_BED", (-10, -99, 1.6), (2.4, 5, .6), "white", f)
    box("V08_CLINIC_CURTAIN_RAIL", (-10, -96, 3.6), (7, .10, .10), "steel", f)
    box("V08_CLINIC_CURTAIN", (-10, -96, 2.8), (6, .06, 2.0), "soft", f)
    desk("V08_CLINIC_TREATMENT_CART", -7, -98, 1.4, .8, f, "stainless")
    box("V08_CLINIC_SINK", (-25, -89, 2.0), (2.0, .8, 1.2), "stainless", f)
    rack("V08_CLINIC_MED_STORAGE", -23, -88, 2, 3, f, "white")

def restaurant():
    f = GROUPS[12]; envelope("V08_RESTAURANT", 5, -69, 46, 26, 7, f, True)
    box("V08_CAFE_COUNTER", (-10, -60.5, 2.1), (10, 1.1, 1.6), "wood", f); box("V08_CAFE_BACKBAR", (-10, -59.3, 4.5), (10, .18, 4.6), "blue", f)
    for i, (xx, yy) in enumerate(((-5,-67),(7,-67),(19,-67),(-5,-76),(7,-76),(19,-76))):
        desk(f"V08_DINING_TABLE_{i}", xx, yy, 3.5, 2.3, f)
        for j in range(4): cyl(f"V08_DINING_SEAT_{i}_{j}", (xx - 2 + (j % 2) * 4, yy - 1.8 + (j // 2) * 3.6, 1.45), .30, .65, "purple", f, 14)
    partition("V08_KITCHEN_PARTITION", 5, -78, 20, 4.2, f)
    box("V08_KITCHEN_PASS", (5, -75, 3.9), (14, .18, 1.6), "warm", f)
    for i in range(5): machine(f"V08_KITCHEN_APPLIANCE_{i}", -8 + i * 4, -81, 3, 1.5, 2.2, f, "stainless")
    rack("V08_KITCHEN_STORAGE", 17, -81, 2, 3, f, "steel")

def security():
    f = GROUPS[13]; envelope("V08_SECURITY", -58, -84, 48, 16, 6.5, f, True)
    desk("V08_SECURITY_RECEPTION", -68, -89.5, 8, 1.1, f)
    for i in range(4): box(f"V08_CCTV_SCREEN_{i}", (-71 + i * 2.2, -88.8, 4.0), (1.5, .10, 1.1), "blue", f)
    for i in range(4): box(f"V08_TURNSTILE_{i}", (-48 + i * 2.5, -88, 1.5), (.4, 2.2, 1.3), "steel", f)
    box("V08_SECURITY_SCREENING", (-42, -82, 1.6), (5, 2, .3), "stainless", f)
    partition("V08_VISITOR_PARTITION", -65, -79, 12, 3.4, f)
    for i in range(3): cyl(f"V08_VISITOR_SEAT_{i}", (-63 + i * 5, -81, 1.5), .35, .7, "purple", f, 14)

def gatehouse():
    f = GROUPS[14]; envelope("V08_GATEHOUSE", 96, -106, 20, 14, 5.8, f, True)
    desk("V08_GATEHOUSE_OPERATOR", 96, -110, 5, 1, f); box("V08_GATEHOUSE_CCTV", (96, -112.2, 3.5), (7, .12, 2.2), "blue", f)
    for i, xx in enumerate((91, 96, 101)): box(f"V08_GATE_WINDOW_{i}", (xx, -99.1, 3.5), (3.6, .10, 2.1), "glass", f)
    box("V08_GATE_BARRIER_ARM", (107, -101, 1.4), (10, .15, .15), "yellow", f)
    box("V08_GATE_BARRIER_POST", (102, -101, 1.4), (.22, .22, 2.3), "yellow", f)
    box("V08_VEHICLE_LANE", (106, -106, 1.0), (18, 4, .10), "floor", f)

def toothpaste():
    f = GROUPS[15]; envelope("V08_PASTE", -12, 43, 42, 19, 7, f)
    tank("V08_PASTE_VACUUM_MIX", -26, 43, 2.5, 4.8, f, "green"); tank("V08_PASTE_HOLD", -20, 43, 1.8, 3.8, f)
    pipe("V08_PASTE_TRANSFER", (-18, 43, 4), (-13, 43, 4), .16, "teal", f)
    box("V08_TUBE_MAGAZINE", (-9, 43, 3.1), (3, 2, 4.2), "steel", f)
    for i in range(5): cyl(f"V08_TUBE_{i}", (-9 + (i % 2) * .8, 41.9, 2.0 + (i // 2) * 1.0), .18, .9, "white", f, 14, (math.pi / 2, 0, 0))
    machine("V08_PASTE_FILL", -4, 43, 3, 3, 3.8, f)
    for i in range(5): cyl(f"V08_PASTE_NOZZLE_{i}", (-5 + i * .45, 41.4, 4), .10, .7, "stainless", f, 12)
    machine("V08_PASTE_CRIMP", 1, 43, 2.5, 2.5, 3.5, f, "purple"); conveyor("V08_PASTE_CODE", 6, 43, 5, 1, f); box("V08_PASTE_CODE_HEAD", (6, 42.3, 3), (1, .4, .8), "red", f)
    machine("V08_PASTE_CARTONER", 11, 43, 3.5, 3, 3.4, f, "orange"); conveyor("V08_PASTE_CARTON_OUT", 16, 43, 5, 1.4, f)

def training():
    f = GROUPS[16]; envelope("V08_TRAINING", 30, -61, 28, 18, 6.5, f, True)
    box("V08_CLASS_SCREEN", (30, -69.6, 4), (12, .12, 4), "soft", f); desk("V08_INSTRUCTOR", 30, -66, 4, 1, f)
    for i, (xx, yy) in enumerate(((24,-62),(32,-62),(24,-57),(32,-57))):
        desk(f"V08_CLASS_TABLE_{i}", xx, yy, 4, 2, f)
        for j in range(2): cyl(f"V08_CLASS_SEAT_{i}_{j}", (xx - 1.8 + j * 3.6, yy - 1.8, 1.45), .3, .65, "purple", f, 14)
    rack("V08_CLASS_STORAGE", 40, -56, 2, 2, f, "steel")

def utilities():
    f = GROUPS[17]; envelope("V08_UTILITIES", 96, 75, 36, 30, 8, f)
    machine("V08_COMPRESSOR", 84, 68, 5, 3, 3, f, "blue"); tank("V08_AIR_RECEIVER", 91, 68, 1.8, 4.5, f, "steel")
    tank("V08_BOILER", 99, 68, 2.0, 4.8, f, "orange"); pipe("V08_STEAM_HEADER", (99, 68, 6), (99, 83, 6), .16, "yellow", f)
    for i in range(3): tank(f"V08_RO_COLUMN_{i}", 106 + i * 2, 68, .7, 4.0, f, "stainless")
    box("V08_RO_SKID", (108, 73, 1.25), (8, 3, .25), "steel", f)
    for i in range(4): pipe(f"V08_UTILITY_MANIFOLD_{i}", (84 + i * 8, 82, 4.8), (84 + i * 8, 82, 6.5), .11, "teal", f)
    desk("V08_MAINTENANCE_BENCH", 88, 84, 8, 1, f)

def wellness():
    f = GROUPS[18]; envelope("V08_WELLNESS", 30, -70, 30, 22, 6.5, f, True)
    for i in range(4): box(f"V08_YOGA_MAT_{i}", (22 + i * 4, -75, 1.15), (2.4, 5, .08), "purple", f)
    for i in range(3):
        machine(f"V08_CARDIO_{i}", 24 + i * 6, -64, 2.2, 2.2, 2.6, f, "teal")
        box(f"V08_CARDIO_HANDLE_{i}", (24 + i * 6, -64, 4), (1.2, .12, 1.2), "steel", f)
    for i in range(3): box(f"V08_WEIGHT_{i}", (20 + i * 3, -68, 2), (1.0, .8, 2.0), "steel", f)
    rack("V08_WELLNESS_LOCKERS", 40, -76, 2, 3, f, "white"); box("V08_WELLNESS_MIRROR", (30, -80.8, 3.5), (16, .08, 3.2), "glass", f)

def wet_processing():
    f = GROUPS[10]; envelope("V08_WET_PROCESS", 0, 24, 54, 32, 9, f)
    for i, xx in enumerate((-18, -7, 4, 15)):
        tank(f"V08_MIX_TANK_{i}", xx, 26, 3.1, 6.0, f, "stainless")
        rails(f"V08_TANK_PLATFORM_{i}", xx, 26, 5, f)
    for xx in (-18, -7, 4, 15): pipe("V08_PROCESS_MANIFOLD", (xx, 26, 5.5), (xx + 8, 35, 5.5), .16, "yellow", f)
    machine("V08_CIP_SKID", 25, 34, 7, 3, 3.8, f, "teal"); tank("V08_CIP_TANK", 25, 27, 2.0, 4.5, f, "blue")
    pipe("V08_CIP_RETURN", (25, 27, 5.5), (15, 26, 5.5), .16, "blue", f); machine("V08_TRANSFER_PUMP", 34, 25, 2, 2, 2.2, f, "blue")
    conveyor("V08_WET_TO_FILLING", 38, 24, 10, 1.6, f); rails("V08_WET_SERVICE_AISLE", 0, 41, 42, f)

def wipes():
    f = GROUPS[19]; envelope("V08_WIPES", 22, 43, 52, 19, 7, f)
    for i, xx in enumerate((0, 4)):
        cyl(f"V08_PARENT_ROLL_{i}", (xx, 43, 3.5), 1.7, 1.1, "white", f, 26, (0, math.pi / 2, 0))
        box(f"V08_UNWIND_STAND_{i}", (xx, 43, 2), (.16, 2.4, 4), "steel", f)
    conveyor("V08_WEB_UNWIND", 9, 43, 8, 1.0, f)
    box("V08_WETTING_IMPREGNATION", (17, 43, 2.5), (4, 2.6, 1.4), "green", f)
    for i in range(3): pipe(f"V08_WETTING_SPRAY_{i}", (16 + i, 42.2, 4), (16 + i, 43.8, 4), .12, "teal", f)
    conveyor("V08_WEB_FOLDING", 25, 43, 8, 1.0, f); box("V08_FOLDING_ROLLERS", (25, 43, 3.2), (3, 2, 3), "steel", f)
    box("V08_CUT_STACK", (32, 43, 2.6), (3, 2.5, 2.8), "yellow", f); conveyor("V08_POUCH_FORM", 39, 43, 7, 1.2, f)
    cyl("V08_POUCH_FILM_ROLL", (39, 41.4, 3.2), 1.2, 1.0, "white", f, 22, (0, math.pi / 2, 0)); machine("V08_POUCH_SEALER", 47, 43, 3.5, 2.6, 3.4, f, "red"); conveyor("V08_PACK_DISCHARGE", 54, 43, 6, 1.4, f)
    for i in range(4): box(f"V08_WIPE_PACK_{i}", (52 + i * 1.2, 43, 2), (.8, .8, 1.2), "soft", f)

BUILDERS = {
    GROUPS[0]: admin, GROUPS[1]: bottle, GROUPS[2]: chemical, GROUPS[3]: etp,
    GROUPS[4]: lambda: warehouse("FG", GROUPS[4], 80, -51, 52, 24, "white"),
    GROUPS[5]: glass, GROUPS[6]: liquid, GROUPS[7]: clinic,
    GROUPS[8]: lambda: warehouse("PACK", GROUPS[8], -10, 79, 58, 45, "teal"),
    GROUPS[9]: lambda: powder(), GROUPS[10]: wet_processing,
    GROUPS[11]: lambda: warehouse("RAW", GROUPS[11], -78, 79, 54, 38, "orange"),
    GROUPS[12]: restaurant, GROUPS[13]: security, GROUPS[14]: gatehouse,
    GROUPS[15]: toothpaste, GROUPS[16]: training, GROUPS[17]: utilities,
    GROUPS[18]: wellness, GROUPS[19]: wipes,
}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    before_blend, before_glb = sha(BLEND), sha(GLB)
    if before_blend != baseline["blend"]["sha256"] or before_glb != baseline["glb"]["sha256"]:
        raise RuntimeError("V08 baseline mismatch; refusing to mutate REV005")
    hidden_map = {}
    for group in GROUPS:
        new_collection(group)
        hidden_map[group] = hide_legacy(group)
        global CURRENT
        CURRENT = COLLECTIONS[group]
        BUILDERS[group]()
        CURRENT.hide_render = False
        CURRENT.hide_viewport = False
    scene = bpy.context.scene
    scene["REV005_REMEDIATION_V08_STATUS"] = "AWAITING_GPT_REMEDIATION_AUDIT_V08"
    scene["REV005_REMEDIATION_V08_METHOD"] = "clean_replacement_subcollections_with_isolated_label_blind_gate"
    scene["REV005_V08_BASELINE_BLEND_SHA256"] = before_blend
    scene["REV005_V08_BASELINE_GLB_SHA256"] = before_glb
    scene["REV005_V08_CLEAN_GROUP_COUNT"] = len(GROUPS)
    scene["REV005_V08_PRESERVED_PASS_GROUPS"] = sorted(PASS_GROUPS)
    temp_blend = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER_V08.tmp.blend"
    if temp_blend.exists():
        temp_blend.unlink()
    bpy.ops.wm.save_as_mainfile(filepath=str(temp_blend), check_existing=False)
    temp_blend.replace(BLEND)
    kwargs = dict(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True, use_selection=False)
    try:
        bpy.ops.export_scene.gltf(**kwargs, use_visible=True)
        export_visibility = "use_visible=True"
    except TypeError:
        bpy.ops.export_scene.gltf(**kwargs)
        export_visibility = "operator_fallback_without_use_visible"
    result = {
        "status": "V08_CLEAN_REPLACEMENTS_BUILT",
        "task": "M08.16",
        "revision": "REV005",
        "baseline_file": str(BASELINE),
        "before_blend_sha256": before_blend,
        "before_glb_sha256": before_glb,
        "clean_collections": {group: COLLECTIONS[group].name for group in GROUPS},
        "clean_object_counts": {group: len(COLLECTIONS[group].objects) for group in GROUPS},
        "legacy_hidden_by_group": hidden_map,
        "legacy_hidden_count": sum(len(v) for v in hidden_map.values()),
        "export_visibility": export_visibility,
        "final_blend_sha256": sha(BLEND),
        "final_glb_sha256": sha(GLB),
    }
    (OUT / "BUILD_RESULT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
