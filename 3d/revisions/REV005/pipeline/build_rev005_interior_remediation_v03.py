import bpy, hashlib, json, math
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v03"
COL = "REV005_INTERIOR_REMEDIATION_V03"
FOCUS_HIDE = {
    "Bottle Blow Molding", "Liquid Filling / Packaging", "Toothpaste Production",
    "Wet Wipes Production", "Central Glass Deck Command / Training / Café Gallery",
}

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

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
    "steel": mat("REV005_V03_STEEL", (.20, .27, .31), .85, .24),
    "stainless": mat("REV005_V03_STAINLESS", (.64, .70, .73), .9, .17),
    "blue": mat("REV005_V03_BLUE", (.02, .18, .55), .3, .28),
    "teal": mat("REV005_V03_TEAL", (.01, .55, .62), .25, .24),
    "orange": mat("REV005_V03_ORANGE", (.95, .25, .03), .15, .3),
    "yellow": mat("REV005_V03_YELLOW", (.98, .60, .01), .08, .34),
    "green": mat("REV005_V03_GREEN", (.04, .48, .22), .2, .3),
    "purple": mat("REV005_V03_PURPLE", (.56, .08, .38), .2, .3),
    "white": mat("REV005_V03_WHITE", (.86, .89, .90), .08, .3),
    "dark": mat("REV005_V03_DARK", (.012, .018, .026), .3, .18),
    "wood": mat("REV005_V03_WOOD", (.46, .22, .07), 0, .48),
    "warm": mat("REV005_V03_WARM", (.96, .44, .08), .05, .38),
    "soft": mat("REV005_V03_SOFT", (.08, .56, .78), .05, .48),
    "glass": mat("REV005_V03_GLASS", (.08, .48, .72), .35, .12),
    "floor": mat("REV005_V03_FLOOR", (.28, .34, .38), .15, .34),
}

COLLECTION = bpy.data.collections.get(COL)
if COLLECTION:
    for obj in list(COLLECTION.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
else:
    COLLECTION = bpy.data.collections.new(COL)
    bpy.context.scene.collection.children.link(COLLECTION)

def link(obj, facility):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    COLLECTION.objects.link(obj)
    obj["REV005_REMEDIATION_V03"] = True
    obj["facility"] = facility
    return obj

def mesh(name, verts, faces, loc, material, facility):
    me = bpy.data.meshes.new(name + "_MESH")
    me.from_pydata(verts, [], faces)
    me.update()
    obj = link(bpy.data.objects.new(name, me), facility)
    obj.location = loc
    obj.data.materials.append(M[material])
    return obj

def box(name, loc, dims, material, facility, rot=None):
    x, y, z = [v / 2 for v in dims]
    vs = [(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]
    fs = [(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    obj = mesh(name, vs, fs, loc, material, facility)
    if rot:
        obj.rotation_euler = rot
    return obj

def cyl(name, loc, radius, depth, material, facility, sides=20, rot=None):
    vs = []
    for z in (-depth / 2, depth / 2):
        for i in range(sides):
            a = math.tau * i / sides
            vs.append((radius * math.cos(a), radius * math.sin(a), z))
    fs = [tuple(range(sides - 1, -1, -1)), tuple(range(sides, sides * 2))]
    fs += [(i, (i + 1) % sides, sides + (i + 1) % sides, sides + i) for i in range(sides)]
    obj = mesh(name, vs, fs, loc, material, facility)
    if rot:
        obj.rotation_euler = rot
    return obj

def cone(name, loc, r1, r2, depth, material, facility, sides=24):
    verts = []
    for z, radius in ((-depth / 2, r1), (depth / 2, r2)):
        for i in range(sides):
            a = math.tau * i / sides
            verts.append((radius * math.cos(a), radius * math.sin(a), z))
    faces = [tuple(range(sides - 1, -1, -1)), tuple(range(sides, sides * 2))]
    faces += [(i, (i + 1) % sides, sides + (i + 1) % sides, sides + i) for i in range(sides)]
    return mesh(name, verts, faces, loc, material, facility)

def pipe(name, a, b, radius, material, facility):
    a, b = Vector(a), Vector(b)
    d = b - a
    obj = cyl(name, (a + b) / 2, radius, d.length, material, facility, 16)
    obj.rotation_euler = d.to_track_quat("Z", "Y").to_euler()
    return obj

def belt(name, x, y, length, width, facility, z=1.35):
    box(name + "_FRAME", (x, y, z), (length, width, .25), "stainless", facility)
    for i in range(7):
        xx = x - length / 2 + .6 + i * (length - 1.2) / 6
        cyl(name + "_ROLLER_%02d" % i, (xx, y, z + .18), width * .40, .12, "dark", facility, 16, (0, math.pi/2, 0))
    box(name + "_GUARD_A", (x, y - width/2, z + .38), (length, .10, .62), "yellow", facility)
    box(name + "_GUARD_B", (x, y + width/2, z + .38), (length, .10, .62), "yellow", facility)

def light_fixture(name, loc, facility, color="warm"):
    box(name + "_BODY", loc, (2.2, .32, .10), "white", facility)
    box(name + "_GLOW", (loc[0], loc[1], loc[2] - .07), (1.7, .16, .04), color, facility)

def wall_pair(prefix, x, y, width, depth, height, facility, back=True):
    box(prefix + "_LEFT", (x - width/2, y, height/2), (.16, depth, height), "white", facility)
    box(prefix + "_RIGHT", (x + width/2, y, height/2), (.16, depth, height), "white", facility)
    if back:
        box(prefix + "_BACK", (x, y + depth/2, height/2), (width, .16, height), "white", facility)

def hide_old_target_layers():
    for collection_name in ("REV005_INTERIOR_REMEDIATION_V01", "REV005_INTERIOR_REMEDIATION_V02"):
        old = bpy.data.collections.get(collection_name)
        if not old:
            continue
        for obj in old.objects:
            if obj.get("facility") in FOCUS_HIDE:
                obj.hide_viewport = True
                obj.hide_render = True

def blow_molding():
    f = "Bottle Blow Molding"; x, y = 52, 10
    box("V03_BLOW_FLOOR", (x, y, 1.10), (34, 15, .18), "floor", f)
    box("V03_BLOW_BACK_WALL", (x, y + 7.3, 5.0), (34, .16, 7.8), "white", f)
    # Preform feed, hopper and heated oven.
    cone("V03_BLOW_PREFORM_HOPPER", (x - 13, y + 2.7, 5.4), 1.65, .35, 2.1, "stainless", f, 28)
    box("V03_BLOW_HOPPER_FRAME", (x - 13, y + 2.7, 3.0), (3.8, 3.5, 2.5), "steel", f)
    belt("V03_BLOW_PREFORM_INFEED", x - 10.5, y + 1.1, 5.5, 1.1, f, 1.45)
    box("V03_BLOW_OVEN_HOUSING", (x - 6.3, y, 3.8), (6.2, 5.2, 5.6), "orange", f)
    box("V03_BLOW_OVEN_WINDOW", (x - 6.3, y - 2.63, 4.0), (4.8, .10, 2.8), "glass", f)
    for i in range(7):
        box("V03_BLOW_HEATER_%02d" % i, (x - 8.5 + i * .72, y - 2.73, 4.0), (.25, .12, 2.0), "yellow", f)
    for i in range(6):
        cyl("V03_BLOW_HEATED_PREFORM_%02d" % i, (x - 8.4 + i * .70, y - 1.9, 2.2), .18, 1.35, "teal", f, 16)
    # Clamp/mould station with visible split moulds and air header.
    box("V03_BLOW_CLAMP_GUARD", (x + 1.0, y, 4.0), (5.8, 5.5, 6.0), "blue", f)
    box("V03_BLOW_CLAMP_WINDOW", (x + 1.0, y - 2.78, 4.0), (4.5, .12, 3.7), "glass", f)
    for side in (-1, 1):
        box("V03_BLOW_MOULD_HALF_%s" % ("L" if side < 0 else "R"), (x + 1.0 + side * 1.25, y - 3.0, 3.5), (1.6, .35, 3.2), "stainless", f)
    pipe("V03_BLOW_AIR_HEADER", (x - .6, y + 2.0, 6.5), (x + 2.6, y + 2.0, 6.5), .16, "teal", f)
    for i in range(3):
        pipe("V03_BLOW_AIR_DROP_%02d" % i, (x - .2 + i * 1.4, y + 2.0, 6.5), (x - .2 + i * 1.4, y + 1.1, 4.8), .08, "teal", f)
    # Formed-bottle outfeed, inspection and palletized cases.
    belt("V03_BLOW_BOTTLE_OUTFEED", x + 9.5, y - .6, 11, 1.8, f, 1.45)
    for i in range(8):
        xx = x + 5.0 + i * 1.2
        cyl("V03_BLOW_FORMED_BOTTLE_%02d" % i, (xx, y - .6, 2.1), .34, 1.20, "teal", f, 20)
        cyl("V03_BLOW_BOTTLE_NECK_%02d" % i, (xx, y - .6, 2.85), .12, .30, "white", f, 16)
    box("V03_BLOW_VISION_FRAME", (x + 6.0, y - .6, 3.8), (.22, 2.6, 4.0), "yellow", f)
    box("V03_BLOW_CASE_PACKER", (x + 13.5, y + 2.3, 2.8), (3.2, 3.2, 3.8), "green", f)
    for i in range(4):
        box("V03_BLOW_FINISHED_CASE_%02d" % i, (x + 17 + (i%2)*1.4, y + 2.2 + (i//2)*1.3, 1.9), (1.1, 1.0, 1.1), "white", f)
    for i in range(5): light_fixture("V03_BLOW_LIGHT_%02d" % i, (x - 13 + i * 6.2, y - 5.8, 8.0), f)

def liquid_filling():
    f = "Liquid Filling / Packaging"; x, y = 10, -2
    box("V03_LIQUID_FLOOR", (x, y, 1.10), (43, 15, .18), "floor", f)
    box("V03_LIQUID_BACK_WALL", (x, y + 7.3, 4.8), (43, .16, 7.2), "white", f)
    belt("V03_LIQUID_BOTTLE_INFEED", x - 17, y, 8, 1.8, f)
    # Filler enclosure and nozzles.
    box("V03_LIQUID_FILLER_HOUSING", (x - 9, y, 4.2), (6.8, 5.7, 5.7), "blue", f)
    box("V03_LIQUID_FILLER_FRONT_GUARD", (x - 9, y - 2.9, 4.1), (5.6, .12, 3.5), "glass", f)
    cyl("V03_LIQUID_ROTARY_CAROUSEL", (x - 9, y, 2.0), 2.6, .38, "stainless", f, 32)
    for i in range(10):
        a = math.tau * i / 10; px = x - 9 + 2.05 * math.cos(a); py = y + 2.05 * math.sin(a)
        cyl("V03_LIQUID_BOTTLE_%02d" % i, (px, py, 2.4), .28, .95, "teal", f, 18)
        pipe("V03_LIQUID_NOZZLE_%02d" % i, (px, py, 4.9), (px, py, 2.9), .08, "yellow", f)
    box("V03_LIQUID_HEAD_BRIDGE", (x - 9, y, 5.2), (6.0, .34, .25), "steel", f)
    belt("V03_LIQUID_MAIN_LINE", x + 4.5, y, 23, 1.8, f)
    # Capper, labeler, inspection and case packer are physically joined by the belt.
    box("V03_LIQUID_CAPPER_GUARD", (x - 1.0, y, 3.0), (2.4, 2.8, 3.8), "purple", f)
    cyl("V03_LIQUID_CAPPER_HEAD", (x - 1.0, y, 5.0), .65, .24, "yellow", f, 24)
    box("V03_LIQUID_LABELER_HOOD", (x + 5.5, y, 3.0), (2.4, 2.8, 3.8), "green", f)
    for side in (-1, 1):
        cyl("V03_LIQUID_LABEL_REEL_%s" % ("IN" if side < 0 else "OUT"), (x + 5.5 + side * .85, y + 1.48, 4.0), .78, .24, "white", f, 24, (0, math.pi/2, 0))
    box("V03_LIQUID_VISION_INSPECTION", (x + 9, y, 3.0), (1.3, 2.0, 3.8), "orange", f)
    box("V03_LIQUID_INSPECTION_CAMERA", (x + 9, y - 1.5, 5.0), (.34, .34, .34), "dark", f)
    box("V03_LIQUID_CASE_PACKER", (x + 14.5, y, 3.0), (3.4, 3.2, 4.0), "blue", f)
    for i in range(6):
        box("V03_LIQUID_PACKED_CASE_%02d" % i, (x + 14 + (i%3)*1.2, y + 1.0 + (i//3)*1.0, 2.0), (.85, .72, 1.0), "white", f)
    belt("V03_LIQUID_CASE_OUTFEED", x + 21, y, 7, 2.0, f)
    box("V03_LIQUID_OPERATOR_BAY", (x + 1.5, y - 4.4, 1.9), (5.0, 1.5, .14), "wood", f)
    for i in range(6): light_fixture("V03_LIQUID_LIGHT_%02d" % i, (x - 17 + i * 6.5, y - 5.7, 8.0), f)

def toothpaste():
    f = "Toothpaste Production"; x, y = -12, 43
    box("V03_PASTE_FLOOR", (x, y, 1.10), (38, 15, .18), "floor", f)
    box("V03_PASTE_BACK_WALL", (x, y + 7.3, 4.8), (38, .16, 7.2), "white", f)
    cyl("V03_PASTE_VACUUM_MIXER", (x - 13, y, 3.5), 2.2, 4.5, "stainless", f, 32)
    box("V03_PASTE_MIXER_LID", (x - 13, y, 5.95), (1.2, 1.2, .65), "blue", f)
    for i in range(3): pipe("V03_PASTE_MIXER_PIPE_%02d" % i, (x - 14.0 + i * 1.0, y + 1.6, 5.2), (x - 14.0 + i * 1.0, y + 1.6, 6.8), .10, "teal", f)
    pipe("V03_PASTE_TRANSFER_MAIN", (x - 10.7, y, 3.5), (x - 6.0, y, 3.5), .24, "stainless", f)
    cyl("V03_PASTE_HOLDING_TANK", (x - 5, y, 3.4), 1.7, 4.0, "green", f, 28)
    box("V03_PASTE_HOLDING_SKID", (x - 5, y, 1.55), (4.0, 3.6, .24), "steel", f)
    pipe("V03_PASTE_FEED_TO_FILLER", (x - 3.3, y, 3.4), (x + 1.0, y, 3.4), .20, "teal", f)
    # Tube magazine and a guided tube-filling/sealing/cartoning line.
    box("V03_PASTE_TUBE_MAGAZINE", (x + 1.6, y + 2.0, 3.2), (2.8, 1.6, 4.0), "white", f)
    for i in range(6):
        cyl("V03_PASTE_EMPTY_TUBE_%02d" % i, (x + .6 + i * .38, y + 1.15, 3.1), .13, 1.9, "white", f, 16)
    belt("V03_PASTE_TUBE_LINE", x + 9, y, 19, 1.8, f)
    box("V03_PASTE_FILLER_GUARD", (x + 5.3, y, 3.2), (2.5, 2.8, 4.2), "blue", f)
    for i in range(4):
        pipe("V03_PASTE_FILL_NOZZLE_%02d" % i, (x + 4.5 + i * .45, y, 5.0), (x + 4.5 + i * .45, y, 3.0), .07, "yellow", f)
    box("V03_PASTE_SEALER", (x + 9.2, y, 3.0), (2.0, 2.6, 3.8), "purple", f)
    for i in range(5):
        box("V03_PASTE_CRIMP_JAW_%02d" % i, (x + 8.4 + i * .35, y - .7, 3.7), (.16, .18, .7), "yellow", f)
    box("V03_PASTE_CODER_INSPECTION", (x + 12.5, y, 3.0), (1.5, 2.4, 3.8), "orange", f)
    box("V03_PASTE_CARTONER", (x + 16, y, 3.2), (3.0, 3.0, 4.2), "blue", f)
    for i in range(6):
        cyl("V03_PASTE_FILLED_TUBE_%02d" % i, (x + 3.5 + i * 1.6, y - .8, 2.25), .15, 1.05, "white", f, 16)
    box("V03_PASTE_CASE_OUTFEED", (x + 21, y, 1.8), (6.0, 2.3, .25), "stainless", f)
    for i in range(4): box("V03_PASTE_FINISHED_CASE_%02d" % i, (x + 19 + i * 1.3, y + .3, 2.1), (1.0, 1.0, 1.0), "white", f)
    for i in range(6): light_fixture("V03_PASTE_LIGHT_%02d" % i, (x - 16 + i * 6.0, y - 5.8, 8.0), f)

def wet_wipes():
    f = "Wet Wipes Production"; x, y = 22, 43
    box("V03_WIPES_FLOOR", (x, y, 1.10), (47, 15, .18), "floor", f)
    box("V03_WIPES_BACK_WALL", (x, y + 7.3, 4.8), (47, .16, 7.2), "white", f)
    # Large parent roll/unwind with a visible web path.
    box("V03_WIPES_UNWIND_FRAME", (x - 18, y, 4.0), (3.0, 4.3, 6.0), "steel", f)
    cyl("V03_WIPES_PARENT_ROLL", (x - 18, y - 1.9, 3.5), 2.0, .85, "white", f, 32, (0, math.pi/2, 0))
    cyl("V03_WIPES_ROLL_CORE", (x - 18, y - 2.35, 3.5), .33, 1.0, "dark", f, 20, (0, math.pi/2, 0))
    pipe("V03_WIPES_WEB_01", (x - 18, y - 2.0, 4.8), (x - 13, y - 2.0, 4.4), .10, "white", f)
    # Wetting/impregnation station with bath and nip rollers.
    box("V03_WIPES_WETTING_BATH", (x - 11, y, 1.75), (4.3, 3.5, .75), "green", f)
    for i in range(3):
        cyl("V03_WIPES_NIP_ROLL_%02d" % i, (x - 11 + i * 1.0, y - 1.5, 3.4), .90, .75, "teal", f, 28, (0, math.pi/2, 0))
    pipe("V03_WIPES_LOTION_FEED", (x - 8, y + 2.8, 5.7), (x - 10, y + 1.4, 2.2), .14, "green", f)
    # Folding plow, longitudinal web, cutter/stacker and pouch packaging.
    box("V03_WIPES_FOLDING_GUARD", (x - 5, y, 3.0), (3.8, 3.8, 4.3), "purple", f)
    box("V03_WIPES_FOLDING_PLOW", (x - 5, y - 2.0, 3.3), (2.4, .20, 2.4), "yellow", f)
    pipe("V03_WIPES_WEB_02", (x - 12, y - 1.8, 3.9), (x - 3, y - 1.8, 3.9), .09, "white", f)
    belt("V03_WIPES_CONVERTING_LINE", x + 6, y, 19, 1.8, f)
    box("V03_WIPES_CUTTER", (x + 0.5, y, 3.0), (1.8, 2.8, 4.0), "blue", f)
    box("V03_WIPES_STACKER", (x + 5, y, 3.0), (2.0, 2.8, 4.0), "purple", f)
    for i in range(6): box("V03_WIPES_STACK_%02d" % i, (x + 5 + i * .27, y - .7, 2.2), (.18, 1.0, .75), "white", f)
    box("V03_WIPES_FILM_REEL_FRAME", (x + 9.5, y + 2.2, 3.4), (2.2, 1.6, 4.8), "steel", f)
    cyl("V03_WIPES_FILM_REEL", (x + 9.5, y + 1.2, 4.3), 1.0, .50, "white", f, 28, (0, math.pi/2, 0))
    box("V03_WIPES_POUCH_PACKER", (x + 12, y, 3.2), (3.5, 3.1, 4.4), "orange", f)
    for i in range(4):
        box("V03_WIPES_SEAL_BAR_%02d" % i, (x + 11.0 + i * .55, y - 1.5, 3.7), (.18, .12, 1.0), "yellow", f)
    belt("V03_WIPES_PACK_OUT", x + 19, y, 7, 1.8, f)
    for i in range(5): box("V03_WIPES_FINISHED_POUCH_%02d" % i, (x + 17 + i * .9, y, 2.1), (.65, .80, .30), "white", f)
    for i in range(7): light_fixture("V03_WIPES_LIGHT_%02d" % i, (x - 19 + i * 6.2, y - 5.8, 8.0), f)

def glass_deck():
    f = "Central Glass Deck Command / Training / Café Gallery"; x = 70
    box("V03_GLASS_DECK_FLOOR", (x, 24, 10.15), (10.5, 47, .18), "floor", f)
    box("V03_GLASS_DECK_LEFT_GLASS", (x - 5.1, 24, 13.5), (.12, 46, 6.5), "glass", f)
    box("V03_GLASS_DECK_RIGHT_GLASS", (x + 5.1, 24, 13.5), (.12, 46, 6.5), "glass", f)
    for yy in (2.0, 14.5, 27.0, 39.5):
        box("V03_GLASS_DECK_PORTAL_LEFT_%02d" % int(yy*10), (x - 4.5, yy, 13.2), (.45, .18, 6.2), "steel", f)
        box("V03_GLASS_DECK_PORTAL_RIGHT_%02d" % int(yy*10), (x + 4.5, yy, 13.2), (.45, .18, 6.2), "steel", f)
    # Command/operations zone.
    box("V03_GLASS_COMMAND_MONITOR_WALL", (x, 39.5, 13.8), (8.0, .22, 4.0), "glass", f)
    for i in range(6):
        box("V03_GLASS_COMMAND_DISPLAY_%02d" % i, (x - 3.1 + i * 1.25, 39.25, 14.0), (.95, .08, 1.45), "teal", f)
    box("V03_GLASS_COMMAND_CONSOLE_1", (x - 2.2, 36.8, 11.4), (3.6, 1.2, 1.15), "blue", f)
    box("V03_GLASS_COMMAND_CONSOLE_2", (x + 2.2, 36.8, 11.4), (3.6, 1.2, 1.15), "blue", f)
    for i in range(6):
        cyl("V03_GLASS_COMMAND_OPERATOR_SEAT_%02d" % i, (x - 3.3 + i * 1.3, 35.2, 10.8), .32, .72, "yellow", f, 16)
        box("V03_GLASS_COMMAND_TERMINAL_%02d" % i, (x - 3.3 + i * 1.3, 36.0, 12.2), (.5, .08, .42), "white", f)
    # Training/collaboration zone with presentation surface.
    box("V03_GLASS_TRAINING_SCREEN", (x, 23.0, 13.1), (7.0, .20, 1.9), "glass", f)
    for i in range(4):
        box("V03_GLASS_TRAINING_SLIDE_%02d" % i, (x - 2.3 + i * 1.55, 22.86, 13.1), (1.05, .08, .85), "teal", f)
    box("V03_GLASS_TRAINING_TABLE_MAIN", (x, 18.0, 11.0), (6.5, 2.8, .28), "wood", f)
    for i in range(8):
        angle = math.tau * i / 8
        cyl("V03_GLASS_TRAINING_CHAIR_%02d" % i, (x + 4.2 * math.cos(angle), 18 + 2.2 * math.sin(angle), 10.6), .34, .72, "yellow", f, 16)
    for i in range(3): light_fixture("V03_GLASS_TRAINING_LIGHT_%02d" % i, (x - 3 + i * 3, 18, 16.2), f)
    # Café/gallery zone with backbar, service counter and circulation tables.
    box("V03_GLASS_CAFE_COUNTER", (x, 6.0, 11.4), (7.6, 1.3, 1.65), "wood", f)
    box("V03_GLASS_CAFE_BACKBAR", (x, 7.5, 13.5), (7.0, .25, 3.6), "green", f)
    for i in range(4):
        box("V03_GLASS_CAFE_SHELF_%02d" % i, (x, 7.25, 12.2 + i * .65), (5.9, .18, .12), "white", f)
    cyl("V03_GLASS_CAFE_ESPRESSO", (x - 2.0, 5.15, 12.3), .48, .85, "stainless", f, 24)
    box("V03_GLASS_CAFE_DISPLAY_CASE", (x + 1.8, 5.15, 12.2), (2.0, .65, 1.0), "glass", f)
    for i in range(4):
        cyl("V03_GLASS_CAFE_STOOL_%02d" % i, (x - 2.4 + i * 1.6, 3.8, 10.8), .34, .72, "purple", f, 16)
    for i in range(2):
        cyl("V03_GLASS_GALLERY_TABLE_%02d" % i, (x - 2.5 + i * 5, 10.0, 10.8), .80, .18, "wood", f, 24)
        for j in range(3): cyl("V03_GLASS_GALLERY_SEAT_%02d_%02d" % (i, j), (x - 2.5 + i * 5 + (j-1)*1.1, 8.7, 10.5), .28, .65, "yellow", f, 16)
    for i in range(3): light_fixture("V03_GLASS_CAFE_LIGHT_%02d" % i, (x - 3 + i * 3, 5.5, 16.2), f)

def restaurant():
    f = "Restaurant / POVU Café / kitchen"; x, y = 5, -69
    box("V03_RESTAURANT_FLOOR", (x, y, 1.05), (45, 25, .18), "floor", f)
    wall_pair("V03_RESTAURANT_ENCLOSURE", x, y, 43, 24, 6.0, f, True)
    box("V03_RESTAURANT_KITCHEN_PARTITION", (x, -75.5, 3.0), (41, .18, 3.8), "glass", f)
    # Service counter/pass and kitchen back line.
    box("V03_RESTAURANT_SERVICE_COUNTER", (-7, -73.5, 2.1), (10.0, 1.2, 1.65), "wood", f)
    box("V03_RESTAURANT_SERVICE_BACKBAR", (-7, -75.0, 4.0), (10.0, .30, 3.4), "green", f)
    for i in range(4): box("V03_RESTAURANT_SERVICE_SHELF_%02d" % i, (-7, -74.8, 3.0 + i*.55), (7.5, .16, .12), "white", f)
    for i in range(4):
        box("V03_RESTAURANT_KITCHEN_STATION_%02d" % i, (-10 + i*8, -78.5, 2.1), (5.5, 1.2, 1.65), "stainless", f)
        cyl("V03_RESTAURANT_KITCHEN_HOOD_%02d" % i, (-10 + i*8, -78.0, 4.8), .55, 1.8, "steel", f, 20)
    box("V03_RESTAURANT_PASS", (5, -76.7, 4.0), (16, .35, .85), "warm", f)
    # Dining layout and café bar seating.
    for i, xx in enumerate((-12, -2, 8, 18)):
        box("V03_RESTAURANT_DINING_TABLE_%02d" % i, (xx, -64.0, 2.05), (3.2, 1.7, .18), "wood", f)
        for j, yy in enumerate((-65.35, -62.65)):
            cyl("V03_RESTAURANT_DINING_CHAIR_%02d_%02d" % (i,j), (xx, yy, 1.75), .36, .72, "teal", f, 16)
    box("V03_RESTAURANT_CAFE_BAR", (18, -69, 2.2), (11.0, 1.0, 1.75), "wood", f)
    for i in range(6):
        cyl("V03_RESTAURANT_BAR_STOOL_%02d" % i, (13.5 + i*1.8, -67.6, 1.65), .32, .8, "purple", f, 16)
    for i in range(4):
        box("V03_RESTAURANT_WALL_PANEL_%02d" % i, (-14 + i*9, -57.1, 3.3), (5.0, .12, 2.2), "glass", f)
        light_fixture("V03_RESTAURANT_LIGHT_%02d" % i, (-14 + i*9, -69, 6.7), f)
    box("V03_RESTAURANT_CIRCULATION_RUG", (5, -69, 1.20), (8, 13, .06), "warm", f)

def daycare():
    f = "Daycare / crèche"; x, y = -105, -64
    box("V03_DAYCARE_FLOOR", (x, y, 1.02), (27, 20, .18), "soft", f)
    wall_pair("V03_DAYCARE_ENCLOSURE", x, y, 26, 19, 5.5, f, True)
    box("V03_DAYCARE_LOW_PARTITION", (x, -64, 2.1), (22, .18, 1.7), "warm", f)
    # Activity, reading/play and rest zones with child scale.
    box("V03_DAYCARE_PLAY_RUG", (x - 5, -58.0, 1.18), (8.5, 5.5, .08), "warm", f)
    for i in range(6):
        box("V03_DAYCARE_PLAY_BLOCK_%02d" % i, (x - 7 + (i%3)*1.5, -58 + (i//3)*1.4, 1.5), (1.0, 1.0, .7), "teal" if i%2 else "yellow", f)
    box("V03_DAYCARE_READING_SHELF", (x + 8.0, -58.0, 2.3), (1.2, 4.5, 2.2), "wood", f)
    for i in range(4): box("V03_DAYCARE_READING_BIN_%02d" % i, (x + 7.3, -59.3 + i*.9, 2.2), (.18, .55, .42), "purple", f)
    box("V03_DAYCARE_SOFT_NOOK", (x + 7.4, -65.0, 1.65), (3.5, 3.2, .35), "purple", f)
    for i in range(4):
        box("V03_DAYCARE_SOFT_BACK_%02d" % i, (x + 5.9 + i*1.0, -66.4, 2.35), (.85, .25, 1.0), "soft", f)
    box("V03_DAYCARE_CAREGIVER_DESK", (x - 1.0, -66.5, 2.1), (3.4, 1.1, 1.5), "wood", f)
    box("V03_DAYCARE_CAREGIVER_SCREEN", (x - 1.0, -65.8, 3.5), (2.4, .12, 1.2), "glass", f)
    for i in range(4):
        light_fixture("V03_DAYCARE_LIGHT_%02d" % i, (x - 9 + i*6, y, 6.3), f, "soft")
    # Visible child-height wash station and cubby frontage.
    box("V03_DAYCARE_HANDWASH", (x + 8.0, -70.5, 1.9), (3.5, .75, 1.5), "white", f)
    for i in range(5):
        box("V03_DAYCARE_CUBBY_FACE_%02d" % i, (x - 8 + i*3.6, -72.0, 2.2), (2.0, .18, 1.7), "wood", f)

def main():
    before_blend = sha(BLEND)
    before_glb = sha(GLB)
    hide_old_target_layers()
    for fn in (blow_molding, liquid_filling, toothpaste, wet_wipes, glass_deck, restaurant, daycare):
        fn()
    scene = bpy.context.scene
    scene["REV005_REMEDIATION_V03_STATUS"] = "AWAITING_GPT_REMEDIATION_AUDIT_V03"
    scene["REV005_REMEDIATION_V03_COLLECTION"] = COL
    scene["REV005_REV004_FROZEN"] = True
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND))
    bpy.ops.export_scene.gltf(filepath=str(GLB), export_format="GLB", export_cameras=True, export_lights=True, export_apply=True, export_extras=True)
    OUT.mkdir(parents=True, exist_ok=True)
    result = {
        "status": "BUILT", "revision": "REV005", "collection": COL,
        "focused_targets": sorted(FOCUS_HIDE | {"Restaurant / POVU Café / kitchen", "Daycare / crèche"}),
        "pre_blend_sha256": before_blend, "pre_glb_sha256": before_glb,
        "post_blend_sha256": sha(BLEND), "post_glb_sha256": sha(GLB),
        "object_count": len(COLLECTION.objects), "blend": str(BLEND), "glb": str(GLB),
        "no_rev006": True, "no_final_tour": True,
    }
    (OUT / "BUILD_RESULT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
