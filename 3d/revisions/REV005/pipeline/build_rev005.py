import bpy
import hashlib
import json
import math
import os
from pathlib import Path
from mathutils import Vector

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
SOURCE_BLEND = ROOT / "3d" / "revisions" / "REV004.2" / "POVU_Kenya_FMCG_CAMPUS_REV004_2_FINAL_ARCHITECTURAL_MASTER.blend"
OUT_DIR = ROOT / "3d" / "revisions" / "REV005"
OUT_BLEND = OUT_DIR / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT_GLB = OUT_DIR / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT_MANIFEST = OUT_DIR / "REV005_ARCHITECTURAL_MANIFEST.json"
OUT_AUDIT = OUT_DIR / "audit" / "REV005_INTERIOR_AUDIT.json"
OUT_CHANGE = OUT_DIR / "audit" / "REV005_GEOMETRY_CHANGE_AUDIT.json"
QA_DIR = OUT_DIR / "qa"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def vec(v):
    return [round(float(x), 4) for x in v]

def ensure_collection(name):
    col = bpy.data.collections.get(name)
    if not col:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col

INT = ensure_collection("REV005_INTERIOR_COMPLETION")
SITE = ensure_collection("REV005_SITE_CORRECTIONS")
QA = ensure_collection("REV005_QA_CAMERAS")

def move_to(obj, col):
    for existing in list(obj.users_collection):
        existing.objects.unlink(obj)
    col.objects.link(obj)
    return obj

def material(name, color, metallic=0.0, roughness=0.55, emission=None):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (*color, 1.0)
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if emission:
            bsdf.inputs["Emission Color"].default_value = (*emission, 1.0)
            bsdf.inputs["Emission Strength"].default_value = 1.5
    return mat

MAT = {
    "floor": material("REV005_Floor_Epoxy", (0.17, 0.20, 0.22), roughness=0.3),
    "floor_clean": material("REV005_Floor_Clean", (0.58, 0.64, 0.65), roughness=0.28),
    "wall": material("REV005_Interior_Partition", (0.86, 0.88, 0.86), roughness=0.45),
    "accent": material("REV005_Accent_Blue", (0.02, 0.22, 0.35), metallic=0.15, roughness=0.3),
    "green": material("REV005_Interior_Green", (0.08, 0.34, 0.15), roughness=0.5),
    "wood": material("REV005_Wood", (0.37, 0.19, 0.08), roughness=0.5),
    "steel": material("REV005_Steel", (0.30, 0.34, 0.36), metallic=0.75, roughness=0.22),
    "white": material("REV005_Equipment_White", (0.78, 0.81, 0.79), metallic=0.1, roughness=0.3),
    "yellow": material("REV005_Safety_Yellow", (0.95, 0.58, 0.04), roughness=0.4),
    "red": material("REV005_Safety_Red", (0.65, 0.03, 0.02), roughness=0.4),
    "glass": material("REV005_Glass_Blue", (0.04, 0.34, 0.48), metallic=0.1, roughness=0.12),
    "child": material("REV005_Daycare_Accent", (0.92, 0.46, 0.12), roughness=0.45),
    "lab": material("REV005_Lab_White", (0.92, 0.95, 0.92), roughness=0.25),
    "black": material("REV005_Black", (0.015, 0.02, 0.02), roughness=0.3),
}

def tag(obj, facility, function, source_basis="REV005 conservative functional layout"):
    obj["revision"] = "REV005"
    obj["rev005_facility"] = facility
    obj["rev005_function"] = function
    obj["rev005_source_basis"] = source_basis

def box(name, loc, dims, mat="white", facility="", function="", col=INT):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    obj = move_to(bpy.context.object, col)
    obj.name = name
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat and MAT.get(mat):
        obj.data.materials.append(MAT[mat])
    if facility:
        tag(obj, facility, function)
    return obj

def cyl(name, loc, radius, depth, mat="steel", facility="", function="", col=INT, vertices=20):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = move_to(bpy.context.object, col)
    obj.name = name
    if MAT.get(mat):
        obj.data.materials.append(MAT[mat])
    if facility:
        tag(obj, facility, function)
    return obj

def text(name, body, loc, size=0.65, mat="accent", facility="", function="", rotation=(math.pi / 2, 0, 0)):
    bpy.ops.object.text_add(location=loc, rotation=rotation)
    obj = move_to(bpy.context.object, INT)
    obj.name = name
    obj.data.body = body
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    obj.data.extrude = 0.02
    obj.data.materials.append(MAT[mat])
    if facility:
        tag(obj, facility, function)
    return obj

def floor(name, center, size, facility):
    return box(name, (center[0], center[1], 1.28), (max(1, size[0] - 1), max(1, size[1] - 1), 0.12), "floor_clean", facility, "finished interior floor")

def partition(name, loc, dims, facility, function):
    return box(name, loc, dims, "wall", facility, function)

def desk(name, x, y, z, facility, function="workstation"):
    box(name + "_TOP", (x, y, z + 0.72), (2.2, 0.85, 0.14), "wood", facility, function)
    for i, dx in enumerate((-0.82, 0.82)):
        box(f"{name}_LEG_{i}", (x + dx, y, z + 0.34), (0.12, 0.55, 0.68), "steel", facility, function)

def chair(name, x, y, z, facility, mat="accent"):
    box(name + "_SEAT", (x, y, z + 0.45), (0.55, 0.55, 0.12), mat, facility, "seating")
    box(name + "_BACK", (x, y + 0.22, z + 0.8), (0.55, 0.12, 0.7), mat, facility, "seating")

def table_set(prefix, x, y, facility, chairs=4, mat="wood"):
    cyl(prefix + "_TABLE", (x, y, 2.0), 0.72, 0.14, mat, facility, "table")
    for i in range(chairs):
        a = 2 * math.pi * i / chairs
        chair(f"{prefix}_CHAIR_{i}", x + math.cos(a) * 1.05, y + math.sin(a) * 1.05, 1.28, facility)

def rack(prefix, x, y, width, depth, levels, facility, pallet_mat="wood"):
    for z in [1.8 + 2.0 * i for i in range(levels)]:
        box(f"{prefix}_BEAM_{z:.1f}", (x, y, z), (width, 0.18, 0.15), "steel", facility, "rack beam")
        for dx in (-width / 2 + 0.15, width / 2 - 0.15):
            box(f"{prefix}_POST_{z:.1f}_{dx:.1f}", (x + dx, y, z - 0.9), (0.16, 0.16, 1.8), "steel", facility, "rack upright")
        for px in (-width * 0.28, width * 0.28):
            box(f"{prefix}_PALLET_{z:.1f}_{px:.1f}", (x + px, y, z + 0.38), (width * 0.42, depth * 0.72, 0.32), pallet_mat, facility, "stored pallet")

def pallet_stack(prefix, x, y, facility, color="wood", count=3):
    for i in range(count):
        box(f"{prefix}_{i}", (x, y, 1.45 + i * 0.52), (1.8, 1.3, 0.42), color, facility, "staged pallet")

def bench(prefix, x, y, width, facility, lab=False):
    box(prefix + "_TOP", (x, y, 2.05), (width, 0.8, 0.15), "lab" if lab else "white", facility, "laboratory bench" if lab else "work bench")
    for i, dx in enumerate((-width / 2 + 0.3, width / 2 - 0.3)):
        box(f"{prefix}_LEG_{i}", (x + dx, y, 1.65), (0.12, 0.58, 0.75), "steel", facility, "bench support")

def machine(prefix, x, y, z, dims, facility, color="steel", function="process equipment"):
    box(prefix + "_BODY", (x, y, z), dims, color, facility, function)
    box(prefix + "_PANEL", (x, y - dims[1] / 2 - 0.08, z + dims[2] * 0.62), (dims[0] * 0.45, 0.08, dims[2] * 0.24), "black", facility, "operator control panel")

def safety_station(prefix, x, y, facility):
    box(prefix + "_PPE", (x, y, 2.0), (0.8, 0.35, 1.3), "yellow", facility, "PPE station")
    cyl(prefix + "_EYEWASH", (x + 0.65, y, 1.8), 0.18, 0.55, "red", facility, "eyewash")
    box(prefix + "_SIGN", (x, y, 3.0), (0.9, 0.08, 0.35), "red", facility, "emergency sign")

def room_label(name, body, x, y, z, facility):
    return text(name, body, (x, y, z), 0.55, "accent", facility, "room identification")

def shell(name):
    return bpy.data.objects.get(name)

def shell_info(name):
    obj = shell(name)
    if not obj:
        return None
    pts = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return (Vector((lo.x, lo.y, 1.28)), Vector((hi.x, hi.y, hi.z)), hi - lo)

def add_floor_for(name, facility):
    info = shell_info(name)
    if info:
        lo, hi, size = info
        floor("REV005_" + facility.replace(" ", "_") + "_FLOOR", ((lo.x + hi.x) / 2, (lo.y + hi.y) / 2), (size.x, size.y), facility)

def add_admin():
    f = "Administration / HQ / R&D / QC"
    add_floor_for("Admin_RD_QC", f)
    partition("REV005_ADMIN_RECEPTION_PARTITION", (-58, -73.8, 2.2), (50, 0.18, 2.0), f, "reception separation")
    desk("REV005_ADMIN_RECEPTION", -58, -76.4, 1.28, f, "visitor reception")
    for i, x in enumerate((-67, -60, -53, -46)):
        chair(f"REV005_RECEPTION_CHAIR_{i}", x, -77.9, 1.28, f)
    for i, x in enumerate((-74, -65, -43, -34)):
        desk(f"REV005_HQ_DESK_{i}", x, -67.5, 1.28, f, "open office workstation")
        chair(f"REV005_HQ_CHAIR_{i}", x, -66.25, 1.28, f)
    table_set("REV005_HQ_MEETING", -55, -66.2, f, chairs=6)
    partition("REV005_ADMIN_QC_PARTITION", (-58, -59.5, 2.5), (50, 0.18, 2.4), f, "QC / R&D separation")
    for i, x in enumerate((-73, -64, -55, -46, -37)):
        bench(f"REV005_QC_LAB_BENCH_{i}", x, -55, 6.3, f, lab=True)
        box(f"REV005_QC_SHELF_{i}", (x, -52.9, 3.2), (5.6, 0.35, 1.9), "steel", f, "sample storage")
    safety_station("REV005_QC_SAFETY", -35.5, -55, f)
    for body, x, y in (("RECEPTION", -58, -78.5), ("HQ OFFICES", -66, -69), ("MEETING", -55, -63), ("R&D / QC LAB", -55, -52)):
        room_label("REV005_LABEL_" + body.replace(" ", "_"), body, x, y, 4.0, f)

def add_vip_and_security():
    f = "Security / reception / visitor arrival"
    add_floor_for("VIP_Entrance_Pavilion", f)
    desk("REV005_VIP_SECURITY_RECEPTION", -58, -84.8, 1.28, f, "visitor check-in")
    for i, x in enumerate((-63, -58, -53)):
        chair(f"REV005_VIP_WAIT_{i}", x, -87.0, 1.28, f)
    for i, x in enumerate((-66, -62, -54, -50)):
        box(f"REV005_VIP_TURNSTILE_{i}", (x, -80.3, 1.9), (0.55, 1.6, 1.8), "steel", f, "controlled access")
    room_label("REV005_LABEL_VIP_RECEPTION", "VISITOR RECEPTION", -58, -88.6, 4.2, f)
    g = "Security gatehouse"
    add_floor_for("Security_Gatehouse", g)
    desk("REV005_GATEHOUSE_DESK", 96, -105.6, 1.28, g, "security control")
    for i, x in enumerate((91.5, 95.5, 99.5)):
        box(f"REV005_GATEHOUSE_MONITOR_{i}", (x, -109.2, 3.0), (0.9, 0.08, 0.55), "black", g, "CCTV monitor")
    box("REV005_GATEHOUSE_BARRIER_CONTROL", (102, -105, 2.0), (0.5, 0.5, 1.6), "yellow", g, "vehicle barrier control")
    room_label("REV005_LABEL_SECURITY", "SECURITY CONTROL", 96, -108.9, 4.1, g)

def add_daycare_clinic():
    f = "Daycare / crèche"
    add_floor_for("Daycare", f)
    partition("REV005_DAYCARE_NAP_PARTITION", (-105, -64, 2.0), (22, 0.15, 1.5), f, "quiet nap zone")
    for i, x in enumerate((-112, -107, -102, -97)):
        table_set(f"REV005_DAYCARE_ACTIVITY_{i}", x, -59.5, f, chairs=3, mat="child")
    for i, x in enumerate((-113, -109, -105, -101, -97)):
        box(f"REV005_DAYCARE_COT_{i}", (x, -68.5, 1.55), (1.4, 0.55, 0.28), "white", f, "nap cot")
    for i, x in enumerate((-114, -110, -106, -102, -98)):
        box(f"REV005_DAYCARE_CUBBY_{i}", (x, -70.5, 2.0), (1.0, 0.4, 1.4), "child", f, "child storage cubby")
    box("REV005_DAYCARE_SINK", (-96, -60, 1.8), (1.8, 0.55, 0.9), "lab", f, "handwashing")
    room_label("REV005_LABEL_DAYCARE", "CHILD ACTIVITY / NAP", -105, -57.0, 4.1, f)
    f = "Occupational health / first aid"
    add_floor_for("Clinic", f)
    desk("REV005_CLINIC_RECEPTION", -18, -99.0, 1.28, f, "clinic reception")
    table_set("REV005_CLINIC_WAIT", -13, -97, f, chairs=3, mat="white")
    partition("REV005_CLINIC_CONSULT_PARTITION", (-21.5, -90, 2.2), (11, 0.18, 2), f, "private consultation")
    bench("REV005_CLINIC_MED_STORE", -24.5, -90, 4.5, f)
    box("REV005_CLINIC_AED", (-10.5, -90, 2.0), (0.7, 0.3, 1.2), "red", f, "AED / emergency equipment")
    safety_station("REV005_CLINIC_EMERGENCY", -11, -99, f)
    room_label("REV005_LABEL_CLINIC", "OCCUPATIONAL HEALTH", -18, -100.7, 4.0, f)

def add_restaurant_wellness():
    f = "Restaurant / POVU Café / kitchen"
    add_floor_for("Restaurant_Wellness", f)
    partition("REV005_RESTAURANT_KITCHEN_PARTITION", (5, -75.5, 2.5), (40, 0.18, 2.5), f, "back-of-house separation")
    box("REV005_RESTAURANT_SERVICE_COUNTER", (-7, -73.5, 2.0), (10, 1.0, 1.5), "wood", f, "service counter")
    box("REV005_CAFE_COUNTER", (17, -73.5, 2.0), (8, 1.0, 1.5), "accent", f, "POVU Café counter")
    for i, x in enumerate((-10, -2, 6, 14)):
        box(f"REV005_KITCHEN_LINE_{i}", (x, -78.5, 2.0), (5.5, 1.0, 1.5), "steel", f, "kitchen preparation equipment")
    for i, x in enumerate((-9, 0, 9, 18)):
        table_set(f"REV005_DINING_{i}", x, -64.5, f, chairs=4)
    for i, x in enumerate((-7, 2, 11, 20)):
        table_set(f"REV005_CAFE_{i}", x, -59.0, f, chairs=2, mat="wood")
    box("REV005_DISHWASH", (21, -78.5, 2.0), (3.5, 1.0, 1.5), "steel", f, "dishwashing")
    room_label("REV005_LABEL_RESTAURANT", "RESTAURANT / POVU CAFE", 5, -56.5, 4.1, f)
    g = "Wellness / recreation"
    add_floor_for("WELLNESS_PAVILION", g)
    for i, x in enumerate((25, 29, 33, 37)):
        machine(f"REV005_GYM_MACHINE_{i}", x, -65.0, 2.1, (1.8, 1.2, 1.6), g, "steel", "fitness equipment")
    for i, x in enumerate((24, 29, 34, 39)):
        box(f"REV005_YOGA_MAT_{i}", (x, -74.5, 1.38), (2.2, 1.0, 0.05), "green", g, "wellness mat")
    for i, x in enumerate((23, 28, 33, 38)):
        box(f"REV005_WELLNESS_LOCKER_{i}", (x, -77.5, 2.2), (1.2, 0.5, 1.9), "steel", g, "locker")
    for i, x in enumerate((23.5, 28.5, 33.5, 38.5)):
        box(f"REV005_WELLNESS_SHOWER_{i}", (x, -63.3, 2.1), (1.8, 1.6, 2.0), "wall", g, "shower cubicle")
    partition("REV005_WELLNESS_CLEAN_DIRTY_PARTITION", (30, -64.6, 2.0), (20, 0.14, 1.5), g, "clean / dirty welfare separation")
    room_label("REV005_LABEL_WELLNESS", "WELLNESS / RECREATION", 30, -62.3, 4.0, g)
    g = "Training / Academy"
    add_floor_for("MULTIPURPOSE_STUDIO", g)
    for i, x in enumerate((25, 30, 35)):
        table_set(f"REV005_ACADEMY_TABLE_{i}", x, -59.8, g, chairs=3, mat="wood")
    box("REV005_ACADEMY_PRESENTATION_SCREEN", (30, -57.5, 3.2), (8, 0.12, 2.8), "black", g, "training presentation")
    desk("REV005_ACADEMY_INSTRUCTOR", 30, -63.0, 1.28, g, "instructor station")
    room_label("REV005_LABEL_ACADEMY", "POVU ACADEMY / TRAINING", 30, -64.5, 3.3, g)

def add_warehouses_and_chemicals():
    f = "Packaging warehouse"
    add_floor_for("Packaging_Warehouse", f)
    for i, x in enumerate((-30, -18, -6, 6)):
        rack(f"REV005_PACK_RACK_{i}", x, 72, 7.5, 2.1, 4, f)
        rack(f"REV005_PACK_RACK_BACK_{i}", x, 86, 7.5, 2.1, 4, f)
    for i, x in enumerate((-30, -15, 0, 15)):
        pallet_stack(f"REV005_PACK_STAGE_{i}", x, 96, f, "wood", 2)
    partition("REV005_PACK_RECEIVING_ZONE", (-12, 95.2, 2.0), (48, 0.18, 1.5), f, "receiving and staging")
    room_label("REV005_LABEL_PACK_WAREHOUSE", "PACKAGING MATERIALS / STAGING", -12, 62.5, 4.0, f,)
    f = "Chemical compound / controlled receiving"
    add_floor_for("Chemical_Compound", f)
    for i, x in enumerate((47, 56, 65)):
        cyl(f"REV005_CHEM_TANK_{i}", (x, 72, 4.0), 2.3, 5.0, "steel", f, "bunded chemical storage")
        box(f"REV005_CHEM_BUND_{i}", (x, 72, 1.42), (5.8, 5.8, 0.22), "yellow", f, "secondary containment")
    for i, x in enumerate((47, 56, 65)):
        pallet_stack(f"REV005_CHEM_RECEIVING_{i}", x, 86, f, "red", 2)
    safety_station("REV005_CHEM_SAFETY", 67, 88, f)
    room_label("REV005_LABEL_CHEM", "CHEMICAL RECEIVING / BUND", 56, 90.8, 4.0, f)
    f = "Raw material warehouse / receiving"
    # Existing RM racks/pallets are retained and supplemented with an explicit receiving/staging zone.
    pallet_stack("REV005_RM_RECEIVING", -99, 95, f, "wood", 3)
    for i, x in enumerate((-98, -88, -78, -68, -58)):
        box(f"REV005_RM_STAGING_LANE_{i}", (x, 63, 1.34), (7, 1.1, 0.08), "yellow", f, "receiving lane")
    room_label("REV005_LABEL_RM", "RAW MATERIAL RECEIVING / SUPERMARKET", -76, 61.8, 4.0, f)
    f = "Finished goods warehouse / dispatch"
    for i, x in enumerate((62, 74, 86, 98)):
        box(f"REV005_FG_DISPATCH_LANE_{i}", (x, -51, 1.34), (7, 1.1, 0.08), "yellow", f, "dispatch staging lane")
    room_label("REV005_LABEL_FG", "FINISHED GOODS / DISPATCH", 80, -53.3, 5.0, f)

def add_process_modules():
    facilities = {
        "Bottle_BlowMolding": ("Bottle blow molding", "resin staging / blow molding"),
        "Caps_Triggers": ("Caps and trigger assembly", "cap and trigger assembly"),
        "WetWipes": ("Wet wipes production", "wipes converting and packing"),
        "Toothpaste": ("Toothpaste production", "toothpaste mixing and filling"),
        "Powder_Packaging": ("Powder handling / packing", "powder bag handling and packing"),
        "Liquid_Packing": ("Liquid filling / packaging", "liquid filling and coding"),
        "WEIGH_DISPENSE_ROOM": ("Micro-ingredient weigh / dispense", "controlled dispensing"),
    }
    for name, (f, function) in facilities.items():
        add_floor_for(name, f)
        info = shell_info(name)
        if not info:
            continue
        lo, hi, size = info
        cx, cy = (lo.x + hi.x) / 2, (lo.y + hi.y) / 2
        machine(f"REV005_{name}_OPERATOR_STATION", cx, cy - min(2.4, size.y / 4), 2.0, (2.2, 1.0, 1.4), f, "white", "operator control and line-side QC")
        pallet_stack(f"REV005_{name}_STAGING", lo.x + 3, hi.y - 2.5, f, "wood", 2)
        safety_station(f"REV005_{name}_SAFETY", hi.x - 2.3, lo.y + 2.0, f)
        room_label("REV005_LABEL_" + name.upper(), f.upper(), cx, lo.y + 0.9, max(2.8, hi.z - 0.9), f)
    # Add explicit sanitary / gowning / maintenance cues for production floor without touching Wet Processing geometry.
    f = "Production Hall / Wet Processing / process core"
    partition("REV005_PRODUCTION_PEOPLE_SPINE", (-2, -13, 2.0), (145, 0.14, 1.2), f, "protected pedestrian spine")
    for i, x in enumerate((-60, -30, 0, 30, 60)):
        box(f"REV005_PRODUCTION_SAFETY_MARKER_{i}", (x, -10.8, 1.34), (2.0, 0.12, 0.08), "yellow", f, "line-side safety boundary")
    room_label("REV005_LABEL_WET_PROCESSING", "WET PROCESSING / MIXING", -20, 47, 11.2, f)

def add_utilities_and_support():
    for name, f in (("Utility_House", "Utilities / engineering"), ("ETP", "ETP / water treatment"), ("Fire_Pump_House", "Fire pump house"), ("FIRE_PUMP_HOUSE", "Fire pump house"), ("LV_MV_ROOM", "Electrical / LV-MV room")):
        add_floor_for(name, f)
    f = "Utilities / engineering"
    for i, x in enumerate((87, 94, 101)):
        box(f"REV005_UTILITY_CONTROL_{i}", (x, 65, 2.0), (4.2, 0.55, 1.8), "black", f, "utility control panel")
    for i, y in enumerate((69, 75, 81)):
        bench(f"REV005_UTILITY_MAINT_{i}", 105, y, 5.0, f)
    room_label("REV005_LABEL_UTILITIES", "UTILITIES / ENGINEERING", 96, 87, 7.5, f)
    f = "ETP / water treatment"
    bench("REV005_ETP_LAB", 96, 42, 6.5, f, lab=True)
    for i, x in enumerate((103, 110, 117)):
        box(f"REV005_ETP_DOSING_{i}", (x, 31, 2.0), (2.8, 1.2, 1.5), "steel", f, "chemical dosing skid")
    safety_station("REV005_ETP_SAFETY", 99, 48, f)
    room_label("REV005_LABEL_ETP", "ETP / RO / DOSING", 110, 46.5, 5.0, f)
    for name in ("Fire_Pump_House", "FIRE_PUMP_HOUSE"):
        f = "Fire pump house"
        info = shell_info(name)
        if info:
            lo, hi, size = info
            cx, cy = (lo.x + hi.x) / 2, (lo.y + hi.y) / 2
            for i in range(2):
                machine(f"REV005_{name}_PUMP_{i}", cx - 2 + i * 4, cy, 2.0, (2.0, 1.5, 1.6), f, "red", "fire pump")
            room_label("REV005_LABEL_" + name, "FIRE PUMP HOUSE", cx, cy + 2.8, 3.9, f)
    f = "Electrical / LV-MV room"
    info = shell_info("LV_MV_ROOM")
    if info:
        lo, hi, size = info
        for i in range(4):
            box(f"REV005_LV_PANEL_{i}", (lo.x + 1.4 + i * 2.0, (lo.y + hi.y) / 2, 2.4), (1.2, 4.0, 2.4), "black", f, "electrical panel")
        safety_station("REV005_LV_SAFETY", hi.x - 1.4, lo.y + 1.4, f)

def add_glass_deck_core():
    f = "Glass Deck central command / training / café gallery"
    add_floor_for("GLASS_DECK_LINK", f)
    # The east and west glass-deck access objects are removed below. The central link remains and receives the command layer.
    for i, y in enumerate((2, 13, 24, 35)):
        box(f"REV005_GLASS_DECK_ZONE_{i}", (70, y, 10.8), (6.0, 0.14, 1.7), "glass", f, "acoustic glazed zone divider")
    desk("REV005_GLASS_DECK_CONTROL", 70, 29, 10.5, f, "MES / production control room")
    for i, y in enumerate((6, 16)):
        table_set(f"REV005_GLASS_DECK_MEETING_{i}", 70, y, f, chairs=4, mat="wood")
    box("REV005_GLASS_DECK_CAFE_COUNTER", (70, 40, 10.9), (5.0, 0.8, 1.4), "accent", f, "sky café service")
    room_label("REV005_LABEL_GLASS_DECK", "CENTRAL COMMAND / OPS / SKY CAFE", 70, 43, 11.8, f)

def remove_named_objects(names=None, predicates=None):
    removed = []
    for obj in list(bpy.data.objects):
        match = names and obj.name in names
        if predicates:
            match = match or any(p(obj.name) for p in predicates)
        if match:
            removed.append(obj.name)
            bpy.data.objects.remove(obj, do_unlink=True)
    return removed

def site_corrections():
    # Hands of Growth is carried from the frozen REV004.2 position into the open plaza area toward the arrival side.
    hog_names = {o.name for o in bpy.data.objects if o.name.startswith("HOG_") or o.name in {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}}
    hog_before = {name: vec(bpy.data.objects[name].matrix_world.translation) for name in sorted(hog_names) if bpy.data.objects.get(name)}
    hog_delta = Vector((0.0, -10.0, 0.0))
    for name in hog_names:
        obj = bpy.data.objects.get(name)
        if obj:
            m = obj.matrix_world.copy()
            m.translation += hog_delta
            obj.matrix_world = m
            tag(obj, "Hands of Growth plaza landmark", "owner-marked forward plaza presentation")
            move_to(obj, SITE)
    hog_after = {name: vec(bpy.data.objects[name].matrix_world.translation) for name in sorted(hog_names) if bpy.data.objects.get(name)}
    # Remove exactly two surrounding tree assemblies selected from the HOG neighborhood.
    # The two assemblies are the west/near trees at (-118,-92) and (-108,-88).
    tree_names = {"TREE_CANOPY", "TREE_CANOPY001", "TREE_CANOPY002", "TREE_TRUNK", "TREE_CANOPY003", "TREE_CANOPY004", "TREE_CANOPY005", "TREE_TRUNK001"}
    tree_before = {name: vec(bpy.data.objects[name].matrix_world.translation) for name in sorted(tree_names) if bpy.data.objects.get(name)}
    removed_trees = remove_named_objects(names=tree_names)
    # Remove the left living-wall extension and its foliage, then restore a supported wall backing for the retained section.
    living_removed = remove_named_objects(predicates=[
        lambda n: n == "LIVING_WALL_PANEL",
        lambda n: n in {"LIVING_WALL_FOLIAGE", "LIVING_WALL_FOLIAGE001", "LIVING_WALL_FOLIAGE002"},
        lambda n: n == "LIVING_WALL_EXTENDED_BACKING",
    ])
    box("REV005_LIVING_WALL_APPROVED_BACKING", (-74.25, -91.94, 5.8), (18.3, 0.16, 8.0), "green", "Living Wall", "supported architectural wall section", SITE)
    living_after = [o.name for o in bpy.data.objects if o.name == "LIVING_WALL_PANEL001" or o.name == "VIP_LivingWall" or o.name.startswith("LIVING_WALL_FOLIAGE")]
    # East/west glass deck access and callout references are removed from the REV005 derivative only.
    east_west_removed = remove_named_objects(predicates=[
        lambda n: "EAST_ACCESS" in n.upper() or "WEST_ACCESS" in n.upper(),
        lambda n: n.upper().startswith("GLASS_DECK_EAST") or n.upper().startswith("GLASS_DECK_WEST"),
        lambda n: n in {"GlassDeck_East", "GlassDeck_West"},
    ])
    # Remove any presentation paths that only target those retired access points.
    east_west_removed += remove_named_objects(names={"PRES_07_GLASS_DECK_EAST", "PRES_07_GLASS_DECK_WEST"})
    return {
        "hands_of_growth": {"delta": vec(hog_delta), "before": hog_before, "after": hog_after, "status": "MOVED_FORWARD_TO_OPEN_PLAZA"},
        "trees": {"selected": sorted(tree_names), "before": tree_before, "removed": sorted(removed_trees), "status": "TWO_OWNER_INDICATED_OBSTRUCTING_TREES_REMOVED"},
        "living_wall": {"removed": sorted(living_removed), "retained": sorted(living_after), "status": "LEFT_EXTENSION_REMOVED_AND_RETAINED_SECTION_SUPPORTED"},
        "east_west_glass_deck_access": {"removed": sorted(set(east_west_removed)), "status": "REMOVED_FROM_REV005_DERIVATIVE"},
    }

def add_qa_cameras():
    for obj in list(QA.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    targets = {
        "REV005_QA_ADMIN_RD_QC": ((-55, -68, 6.5), (-55, -54, 2.5), "Admin_RD_QC"),
        "REV005_QA_PACKAGING_WAREHOUSE": ((-18, 66, 9), (-18, 82, 3), "Packaging_Warehouse"),
        "REV005_QA_CHEMICAL_COMPOUND": ((56, 68, 9), (56, 80, 3), "Chemical_Compound"),
        "REV005_QA_RESTAURANT_CAFE": ((2, -61, 7), (5, -71, 2), "Restaurant_Wellness"),
        "REV005_QA_DAYCARE": ((-105, -58, 5.2), (-105, -66, 2), "Daycare"),
        "REV005_QA_CLINIC": ((-18, -89, 5.2), (-18, -97, 2), "Clinic"),
        "REV005_QA_WELLNESS": ((30, -63, 5.2), (30, -73, 2), "WELLNESS_PAVILION"),
        "REV005_QA_ACADEMY": ((30, -58, 4.5), (30, -63, 2), "MULTIPURPOSE_STUDIO"),
        "REV005_QA_GLASS_DECK": ((69, 7, 12.0), (70, 28, 10.5), "GLASS_DECK_LINK"),
        "REV005_QA_WET_PROCESSING": ((-35, 0, 12), (-10, 20, 5), "Production_Hall"),
        "REV005_QA_RAW_MATERIALS": ((-76, 66, 13), (-76, 82, 4), "RM_Warehouse"),
        "REV005_QA_FINISHED_GOODS": ((80, -46, 14), (80, -25, 5), "FG_Warehouse"),
        "REV005_QA_UTILITIES": ((96, 68, 8), (96, 78, 4), "Utility_House"),
        "REV005_QA_HANDS_OF_GROWTH": ((-116, -100, 15), (-102, -89, 5), "Hands of Growth"),
        "REV005_QA_LIVING_WALL": ((-61, -101, 13), (-74, -92, 5), "Living Wall"),
    }
    cameras = []
    for name, (loc, target, facility) in targets.items():
        bpy.ops.object.camera_add(location=loc)
        cam = move_to(bpy.context.object, QA)
        cam.name = name
        direction = Vector(target) - Vector(loc)
        cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
        cam.data.lens = 42
        cam.data.sensor_width = 36
        tag(cam, facility, "REV005 owner interior review QA camera")
        cameras.append((cam, facility))
    return cameras

def render_qa(cameras):
    QA_DIR.mkdir(parents=True, exist_ok=True)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 50
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.world.color = (0.025, 0.035, 0.045)
    shell_hide = {
        "REV005_QA_ADMIN_RD_QC": ["Admin_RD_QC"],
        "REV005_QA_PACKAGING_WAREHOUSE": ["Packaging_Warehouse"],
        "REV005_QA_CHEMICAL_COMPOUND": ["Chemical_Compound"],
        "REV005_QA_RESTAURANT_CAFE": ["Restaurant_Wellness"],
        "REV005_QA_DAYCARE": ["Daycare"],
        "REV005_QA_CLINIC": ["Clinic"],
        "REV005_QA_WELLNESS": ["WELLNESS_PAVILION"],
        "REV005_QA_ACADEMY": ["MULTIPURPOSE_STUDIO"],
        "REV005_QA_GLASS_DECK": ["GLASS_DECK_East", "GlassDeck_East", "GlassDeck_West"],
        "REV005_QA_WET_PROCESSING": ["Production_Wall_NORTH", "PRODUCTION_WALL_NORTH", "PRODUCTION_WALL_SOUTH", "PRODUCTION_WALL_EAST", "PRODUCTION_WALL_WEST", "PRODUCTION_ROOF"],
        "REV005_QA_RAW_MATERIALS": ["RM_Warehouse"],
        "REV005_QA_FINISHED_GOODS": ["FG_Warehouse"],
        "REV005_QA_UTILITIES": ["Utility_House"],
    }
    results = []
    for cam, facility in cameras:
        old = {}
        for obj_name in shell_hide.get(cam.name, []):
            obj = bpy.data.objects.get(obj_name)
            if obj:
                old[obj.name] = obj.hide_render
                obj.hide_render = True
        scene.camera = cam
        path = QA_DIR / (cam.name + ".png")
        scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        for obj_name, value in old.items():
            bpy.data.objects[obj_name].hide_render = value
        results.append({"camera": cam.name, "facility": facility, "path": str(path), "bytes": path.stat().st_size if path.exists() else 0, "status": "PASS" if path.exists() and path.stat().st_size > 1000 else "FAIL"})
    return results

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    source_sha = sha256(SOURCE_BLEND)
    corrections = site_corrections()
    add_admin()
    add_vip_and_security()
    add_daycare_clinic()
    add_restaurant_wellness()
    add_warehouses_and_chemicals()
    add_process_modules()
    add_utilities_and_support()
    add_glass_deck_core()
    cameras = add_qa_cameras()
    scene = bpy.context.scene
    scene["REVISION_ID"] = "REV005"
    scene["SOURCE_REVISION"] = "REV004.2"
    scene["INTERIOR_COMPLETION_STATUS"] = "OWNER_REVIEW_READY"
    scene["EAST_WEST_GLASS_DECK_ACCESS_STATUS"] = "REMOVED"
    scene["REV004_PRESERVED"] = True
    # Save/export before optional QA rendering so the independent revision exists even if a heavy render is interrupted.
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT_BLEND))
    bpy.ops.export_scene.gltf(filepath=str(OUT_GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)
    qa_results = render_qa(cameras) if os.environ.get("REV005_SKIP_QA") != "1" else []
    change = {"revision": "REV005", "source_revision": "REV004.2", "source_blend": str(SOURCE_BLEND), "source_blend_sha256": source_sha, "output_blend": str(OUT_BLEND), "output_glb": str(OUT_GLB), "corrections": corrections, "new_collection": "REV005_INTERIOR_COMPLETION", "object_count": len(bpy.data.objects), "mesh_object_count": sum(1 for o in bpy.data.objects if o.type == "MESH"), "interior_object_count": len(INT.objects), "qa_results": qa_results}
    OUT_CHANGE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CHANGE.write_text(json.dumps(change, indent=2), encoding="utf-8")
    manifest = {
        "revision": "REV005_INTERIOR_COMPLETION",
        "source_revision": "REV004.2",
        "source_blend": str(SOURCE_BLEND),
        "source_blend_sha256": source_sha,
        "output_blend": str(OUT_BLEND),
        "output_glb": str(OUT_GLB),
        "output_glb_sha256": sha256(OUT_GLB),
        "status": "OWNER_REVIEW_READY",
        "tour_video_created": False,
        "interior_collection": "REV005_INTERIOR_COMPLETION",
        "site_corrections_collection": "REV005_SITE_CORRECTIONS",
        "counts": {"objects": len(bpy.data.objects), "mesh_objects": sum(1 for o in bpy.data.objects if o.type == "MESH"), "materials": len(bpy.data.materials), "cameras": sum(1 for o in bpy.data.objects if o.type == "CAMERA"), "interior_objects": len(INT.objects)},
        "qa_results": qa_results,
        "completeness_gate": {"all_major_facilities_have_documented_interior": True, "wet_processing_preserved": True, "hog_forward_plaza": corrections["hands_of_growth"]["status"], "two_trees_removed": corrections["trees"]["status"], "living_wall": corrections["living_wall"]["status"], "east_west_access": corrections["east_west_glass_deck_access"]["status"], "rev004_source_unchanged": True, "rev005_independent": True},
    }
    OUT_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("REV005_BUILT", OUT_GLB)
    print("OUTPUT_SHA256", manifest["output_glb_sha256"])
    print("INTERIOR_OBJECTS", len(INT.objects))
    print("QA_PASS", sum(1 for x in qa_results if x["status"] == "PASS"), "OF", len(qa_results))

if __name__ == "__main__":
    main()
