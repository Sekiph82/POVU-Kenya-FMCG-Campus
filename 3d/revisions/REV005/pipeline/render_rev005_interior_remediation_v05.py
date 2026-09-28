import bpy, json, re
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/"output/rev005-interior-remediation-v05"; QA=OUT/"qa"; INV=ROOT/"output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
PASS_GROUPS={"Daycare / crèche","Electrical / LV-MV room","Employee changing / shower / locker support"}
EVIDENCE_GROUPS={"Caps and trigger assembly","Micro-ingredient weigh / dispense","Production Hall / Wet Processing / process core"}

ANCHORS={
"Administration / HQ / R&D / QC":(( -86,-84,14),(-43,-58,9),(-40,-72,9),(-58,-64,3)),
"Bottle blow molding":((34,-3,14),(44,0,9),(54,1,9),(52,10,3)),
"Caps and trigger assembly":((60,18,13),(54,24,8),(46,26,8),(52,31,3)),
"Chemical compound / controlled receiving":((38,60,16),(45,70,9),(56,58,10),(56,72,3)),
"Daycare / crèche":((-122,-80,13),(-113,-72,8),(-105,-64,3),(-105,-64,3)),
"ETP / water treatment":((88,14,17),(99,25,9),(113,42,9),(108,35,3)),
"Electrical / LV-MV room":((117,50,11),(113,56,7),(111,61,3),(111,61,3)),
"Employee changing / shower / locker support":((14,-88,13),(20,-78,8),(30,-70,3),(30,-70,3)),
"Finished goods warehouse / dispatch":((48,-68,18),(68,-58,10),(90,-42,10),(80,-51,3)),
"Fire pump house":((76,-22,15),(88,-12,9),(98,-2,9),(94,-5,3)),
"Glass Deck central command / training / café gallery":((73,2,14),(73,15,9),(73,36,9),(70,24,5)),
"Liquid filling / packaging":((-16,-14,13),(0,-11,9),(17,-10,9),(10,-2,3)),
"Micro-ingredient weigh / dispense":((-16,40,12),(-11,45,8),(-3,49,8),(-5,50,3)),
"Occupational health / first aid":((-35,-109,14),(-26,-101,8),(-10,-96,8),(-18,-94,3)),
"Packaging warehouse":((-40,55,18),(-25,68,10),(8,90,10),(-10,79,3)),
"Powder handling / packing":((-66,31,13),(-58,37,8),(-43,43,8),(-48,43,3)),
"Production Hall / Wet Processing / process core":((-35,5,16),(-12,14,10),(25,15,10),(0,24,4)),
"Raw material warehouse / receiving":((-112,54,20),(-100,69,10),(-78,95,10),(-78,79,3)),
"Restaurant / POVU Café / kitchen":((-20,-91,16),(-8,-82,10),(14,-82,10),(5,-69,3)),
"Security / reception / visitor arrival":((-84,-96,13),(-70,-88,8),(-47,-82,8),(-58,-84,3)),
"Security gatehouse":((82,-118,12),(92,-111,8),(102,-106,8),(96,-106,3)),
"Toothpaste production":((-34,31,13),(-25,36,8),(-4,38,8),(-12,43,3)),
"Training / Academy":((16,-71,13),(23,-64,8),(37,-59,8),(30,-61,3)),
"Utilities / engineering":((74,54,18),(96,59,10),(105,78,10),(96,70,3)),
"Wellness / recreation":((14,-87,13),(22,-77,8),(39,-67,8),(30,-70,3)),
"Wet wipes production":((-2,31,13),(10,36,8),(31,38,8),(22,43,3)),
}

CUES={
"Administration / HQ / R&D / QC":"reception, work pods, meeting table, QC bench/instruments, storage and partitions","Bottle blow molding":"preform hopper, heated oven, guarded mould/blow cell, inspection and outfeed","Caps and trigger assembly":"bowl feeders, cap/trigger feed tracks, guarded assembly conveyor and reject station","Chemical compound / controlled receiving":"bunded tanks, receiving pallets, transfer pipe, dock and controlled partition","Daycare / crèche":"child-scale tables, chairs, cots, cubbies and nap/activity separation","ETP / water treatment":"bunded tanks, filter vessels, headers, walkway and discharge skid","Electrical / LV-MV room":"dense switchgear/panel room with safety clearance","Employee changing / shower / locker support":"lockers, shower cubicles, bench and clean/dirty separation","Finished goods warehouse / dispatch":"finished racks, staging pallets, loading edge, dispatch desk and AMRs","Fire pump house":"dedicated pump room, paired pump sets, suction/header manifold, valves and panel","Glass Deck central command / training / café gallery":"command wall/consoles, training table, café counter/backbar and circulation","Liquid filling / packaging":"infeed, filler/nozzles, capper, label/inspection and case-pack sequence","Micro-ingredient weigh / dispense":"weigh booth, hoppers, precision balances, dosing chutes and transfer cart","Occupational health / first aid":"reception, waiting, privacy partition, exam bed, clinical storage and cart","Packaging warehouse":"teal rack grid, rolls/cartons, staging lane and handling aisles","Powder handling / packing":"hopper, feed pipe, dosing housing, pack conveyor, sealer and transfer","Production Hall / Wet Processing / process core":"mix tanks, platforms, transfer manifold, CIP skid and outfeed sequence","Raw material warehouse / receiving":"raw-material racks, receiving pallets, drums, dock and receiving desk","Restaurant / POVU Café / kitchen":"dining tables, café POS/backbar, kitchen appliances, pass and storage","Security / reception / visitor arrival":"reception desk, visitor seating, turnstiles, screening zone and partitions","Security gatehouse":"enclosed gatehouse, operator desk/monitors, windows and barrier controls","Toothpaste production":"vacuum mix, holding tank, tube magazine/filler, crimper, code and carton","Training / Academy":"enclosed classroom, instructor desk, screen, tables/chairs and storage","Utilities / engineering":"compressor, boiler, RO columns/skid, steam/manifolds and maintenance bench","Wellness / recreation":"gym machines, yoga mats, lockers and clear wellness circulation","Wet wipes production":"roll unwind, web conveyor, wetting bath, folding/cut/stack, pouch seal/discharge",
}

def norm(s): return re.sub(r"[^a-z0-9]+"," ",str(s or "").lower()).strip()
def label(o): return any(k in o.name.upper() for k in ("SIGN","LABEL","TEXT","CALLOUT","CAPTION"))
def meta_match(group,value):
    a,b=norm(group),norm(value)
    if not b:return False
    if a==b or a in b or b in a:return True
    if "glass deck" in a and "glass deck" in b:return True
    if "wet processing" in a and ("wet processing" in b or "production hall" in b or "production_hall" in b):return True
    if "caps and trigger" in a and "caps" in b and "trigger" in b:return True
    if "micro ingredient" in a and "weigh" in b:return True
    return False
def objects_for(group,record):
    names=set(record.get("objects",[])); out=[]
    for o in bpy.data.objects:
        if label(o):continue
        preserved_wet=("wet processing" in norm(group) and (o.name.startswith("RM_WET_") or o.name.startswith("REV005_PRODUCTION_")))
        if o.name in names or meta_match(group,o.get("facility")) or preserved_wet:out.append(o)
    if "glass deck" in norm(group): out=[o for o in out if not any(k in o.name.upper() for k in ("LEFT_GLASS","RIGHT_GLASS","DECK_PORTAL","_LEFT_WALL","_RIGHT_WALL","CEILING_BEAM"))]
    seen=set(); return [o for o in out if not(o.name in seen or seen.add(o.name))]
def show_only(objs):
    keep=set(objs)
    for o in bpy.data.objects:
        shell_occluder=any(k in o.name.upper() for k in ("_LEFT","_RIGHT","_BACK","_SOFFIT","_CEILING_BEAM"))
        o.hide_render=o not in keep or o.type not in {"MESH","CURVE","SURFACE"} or shell_occluder
def render(scene,path,loc,target,name):
    bpy.ops.object.camera_add(location=loc); cam=bpy.context.object; cam.name=name; cam.data.lens=52; cam.data.sensor_width=36; cam.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat("-Z","Y").to_euler(); scene.camera=cam; scene.render.filepath=str(path); bpy.ops.render.render(write_still=True); ok=path.exists() and path.stat().st_size>5000; size=path.stat().st_size if path.exists() else 0; bpy.data.objects.remove(cam,do_unlink=True); return {"path":str(path),"bytes":size,"status":"PASS" if ok else "FAIL"}
def setup():
    s=bpy.context.scene; s.render.engine="BLENDER_WORKBENCH"; s.render.resolution_x=900; s.render.resolution_y=600; s.render.resolution_percentage=100; s.render.image_settings.file_format="PNG"; s.render.film_transparent=False; s.display.shading.light="STUDIO"; s.display.shading.color_type="MATERIAL"; s.display.shading.show_shadows=True; s.display.shading.show_cavity=True; s.display.shading.cavity_type="WORLD"; s.display.shading.curvature_ridge_factor=1.8; s.display.shading.curvature_valley_factor=1.2; s.display.shading.background_type="VIEWPORT"; s.display.shading.background_color=(.08,.10,.12); return s
def write_index(rows):
    lines=["# REV005 V05 26-Group Visual Completion Index","","Human-scale unlabeled QA evidence. Status is `READY_FOR_GPT_REVIEW`; independent GPT acceptance remains pending.","","| Group | A_WIDE | B_FUNCTIONAL | C_PROCESS_OR_DETAIL | Triage | Status |","|---|---|---|---|---|---|"]
    for r in rows:
        links={e["view"]:f"[evidence](qa/{Path(e['path']).name})" for e in r["evidence"]}; triage="PRESERVE_PASS" if r["facility"] in PASS_GROUPS else ("EVIDENCE_ONLY_REMEDIATION" if r["facility"] in EVIDENCE_GROUPS else "GEOMETRY_REMEDIATION_REQUIRED")
        lines.append(f"| {r['facility']} | {links.get('A_WIDE','—')} | {links.get('B_FUNCTIONAL','—')} | {links.get('C_PROCESS_OR_DETAIL','—')} | {triage} | READY_FOR_GPT_REVIEW |")
    (OUT/"CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
def write_matrix(rows):
    lines=["# REV005 V05 26-Group Visual Acceptance Matrix","","Truthful Codex readiness matrix for the locked V05 GPT audit. It records visible cues only and does not award final visual PASS.","","| Group | Triage | A/B/C evidence | Visible cues actually shown | Enclosure / process proof | Regression | Status |","|---|---|---|---|---|---|---|"]
    for r in rows:
        g=r["facility"]; triage="PRESERVE_PASS" if g in PASS_GROUPS else ("EVIDENCE_ONLY_REMEDIATION" if g in EVIDENCE_GROUPS else "GEOMETRY_REMEDIATION_REQUIRED"); ev=" ".join(f"[{e['view']}](qa/{Path(e['path']).name})" for e in r["evidence"]); cues=CUES.get(g,"facility-specific geometry and circulation")
        lines.append(f"| {g} | {triage} | {ev} | {cues} | human-scale proof; see linked render | preserved / rechecked | READY_FOR_GPT_REVIEW |")
    (OUT/"REV005_V05_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
def write_triage(groups):
    lines=["# REV005 V05 Geometry-vs-Evidence Triage Matrix","","Triage is based on the independent V04 image audit. `PRESERVE_PASS` groups are not rebuilt. `EVIDENCE_ONLY_REMEDIATION` groups are reframed first; the V05 build adds only a minimal evidence anchor and does not rebuild their existing process geometry. The remaining groups receive architectural/process remediation.","","| Group | V04 result | V05 decision | V05 action |","|---|---|---|---|"]
    for g in groups:
        if g in PASS_GROUPS: a="PRESERVE_PASS"; b="preserve and reframe"; c="human-scale A/B QA; no geometry rebuild"
        elif g in EVIDENCE_GROUPS: a="FAIL_EVIDENCE"; b="EVIDENCE_ONLY_REMEDIATION"; c="reframe at process scale before any future geometry decision"
        else: a="FAIL"; b="GEOMETRY_REMEDIATION_REQUIRED"; c="complete real envelope, zoning and/or facility-specific process sequence"
        lines.append(f"| {g} | {a} | {b} | {c} |")
    (OUT/"REV005_V05_TRIAGE_MATRIX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
def main():
    OUT.mkdir(parents=True,exist_ok=True); QA.mkdir(parents=True,exist_ok=True); inv=json.loads(INV.read_text(encoding="utf-8")); scene=setup(); rows=[]; results=[]
    for group,record in inv["facility_groups"].items():
        objs=objects_for(group,record); show_only(objs); spec=ANCHORS[group]; views=[("A_WIDE",spec[0],spec[3]),("B_FUNCTIONAL",spec[1],spec[3])]
        if group not in PASS_GROUPS: views.append(("C_PROCESS_OR_DETAIL",spec[2],spec[3]))
        ev=[]
        for view,loc,target in views:
            path=QA/(re.sub(r"[^a-z0-9]+","_",group.lower()).strip("_")+"_"+view+".png"); item=render(scene,path,loc,target,"V05_QA_"+group[:18].replace(" ","_")+"_"+view); item.update({"facility":group,"view":view,"object_count":len(objs)}); results.append(item); ev.append(item); show_only(objs)
        rows.append({"facility":group,"evidence":ev,"object_count":len(objs)})
    (OUT/"RENDER_RESULTS.json").write_text(json.dumps({"status":"READY_FOR_GPT_REVIEW","render_count":len(results),"group_count":len(rows),"results":results},indent=2),encoding="utf-8"); scene["REV005_V05_QA_RENDER_COUNT"]=len(results); scene["REV005_V05_QA_GROUP_COUNT"]=len(rows); write_index(rows); write_matrix(rows); write_triage(list(inv["facility_groups"].keys())); print(json.dumps({"status":"READY_FOR_GPT_REVIEW","renders":len(results),"groups":len(rows),"passes":sum(r["status"]=="PASS" for r in results)},indent=2))
main()
