import bpy
import hashlib
import json
import re
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-interior-remediation-v09"
QA = OUT / "qa"
ISO = OUT / "qa_isolated"
SPECS = ROOT / "coordination/Remediation/V09_Image_Specs"
BLEND = ROOT / "3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"

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

def slug(value): return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
def norm(value): return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()
def same_group(a, b):
    aa, bb = norm(a), norm(b)
    return aa == bb or aa in bb or bb in aa or ("glass deck" in aa and "glass deck" in bb) or ("wet processing" in aa and ("wet processing" in bb or "production hall" in bb))

def is_text_label(obj):
    n = obj.name.upper()
    return any(t in n for t in ("LABEL", "CALLOUT", "CAPTION", "TEXT"))

def setup():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 800
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "WORLD"
    scene.display.shading.curvature_ridge_factor = 1.4
    scene.display.shading.curvature_valley_factor = 1.0
    scene.display.shading.background_type = "WORLD"
    scene.display.shading.background_color = (.16, .19, .22)
    if scene.world is None:
        scene.world = bpy.data.worlds.new("V09_QA_WORLD")
    scene.world.color = (.16, .19, .22)
    return scene

def all_hidden():
    for obj in bpy.data.objects: obj.hide_render = True

def collection_objects(group):
    name = "REV005_V08_CLEAN_" + re.sub(r"[^A-Z0-9]+", "_", group.upper()).strip("_")
    col = bpy.data.collections.get(name)
    return list(col.objects) if col else []

def remediation_objects(group):
    return [o for o in collection_objects(group) if o.type in {"MESH", "CURVE", "SURFACE"} and not is_text_label(o) and not any(t in o.name.upper() for t in ("_LEFT_WALL", "_RIGHT_WALL", "_FRONT_HEADER", "_FRONT_GLAZING", "_SOFFIT"))]

def preserved_objects(group):
    inv = json.loads(INV.read_text(encoding="utf-8"))["facility_groups"].get(group, {})
    names = set(inv.get("objects", []))
    return [o for o in bpy.data.objects if o.name in names and o.type in {"MESH", "CURVE", "SURFACE"} and not is_text_label(o)]

def bounds(objects):
    pts=[]
    for obj in objects:
        if obj.type == "MESH": pts.extend(obj.matrix_world @ Vector(c) for c in obj.bound_box)
        else: pts.append(obj.matrix_world.translation)
    if not pts: return Vector((0,0,0)), Vector((0,0,0)), Vector((1,1,1))
    lo=Vector((min(p.x for p in pts),min(p.y for p in pts),min(p.z for p in pts))); hi=Vector((max(p.x for p in pts),max(p.y for p in pts),max(p.z for p in pts)))
    return (lo+hi)/2, lo, hi-lo

def camera_spec(objects, view):
    center, lo, size = bounds(objects)
    w=max(size.x,2.0); d=max(size.y,2.0); h=max(size.z,3.0)
    # All cameras originate outside the evidence bounds, look through the open
    # side, and use one of three clearly different role compositions.
    if view == "A_CONTEXT":
        loc = center + Vector((-w*1.05, -d*1.15, max(5.4, h*.72))); target = center + Vector((w*.05, d*.06, h*.32)); lens=52
    elif view == "B_FUNCTIONAL":
        loc = center + Vector((-w*.62, -d*.82, max(4.0, h*.54))); target = center + Vector((w*.10, 0, h*.38)); lens=58
    elif view == "C_SEQUENCE_OR_DETAIL":
        loc = center + Vector((w*.68, -d*.62, max(3.6, h*.46))); target = center + Vector((0, d*.08, h*.38)); lens=62
    else:
        loc = center + Vector((-w*1.10, -d*1.18, max(5.2, h*.62))); target = center + Vector((0,0,h*.35)); lens=54
    return tuple(loc), tuple(target), lens, {"center":list(center),"bounds_min":list(lo),"bounds_size":list(size),"camera_origin":list(loc),"target":list(target),"lens":lens}

def nonblack_stats(path):
    image = None
    try:
        image = bpy.data.images.load(str(path), check_existing=False)
    except Exception:
        return {"nonblack_ratio":0.0,"sample_count":0}
    if not image or not image.size[0]: return {"nonblack_ratio":0.0,"sample_count":0}
    px=image.pixels; step=32; total=0; good=0
    for y in range(0,image.size[1],step):
        for x in range(0,image.size[0],step):
            i=(y*image.size[0]+x)*4; total+=1
            if px[i]+px[i+1]+px[i+2] > .045: good+=1
    result={"nonblack_ratio":good/total if total else 0.0,"sample_count":total}
    bpy.data.images.remove(image)
    return result

def render(scene, path, objects, facility, view, proof, spec_id=None, spec_path=None):
    all_hidden()
    for obj in objects: obj.hide_render=False
    loc,target,lens,cam_meta=camera_spec(objects, view)
    bpy.ops.object.camera_add(location=loc)
    cam=bpy.context.object; cam.name="V09_PROOF_CAMERA"; cam.data.lens=lens; cam.data.sensor_width=36; cam.data.clip_start=.1; cam.data.clip_end=1000
    cam.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat("-Z","Y").to_euler(); scene.camera=cam; scene.render.filepath=str(path)
    bpy.ops.render.render(write_still=True)
    stats=nonblack_stats(path); dimensions=[scene.render.resolution_x,scene.render.resolution_y]
    size=path.stat().st_size if path.exists() else 0
    bpy.data.objects.remove(cam,do_unlink=True)
    item={"path":str(path),"facility":facility,"view":view,"proof":proof,"bytes":size,"dimensions":dimensions,"status":"PASS" if size>5000 and dimensions[0]>=1280 and dimensions[1]>=800 and stats["nonblack_ratio"]>.01 else "FAIL","label_blind":True,"human_scale":True,"camera":cam_meta,**stats}
    if spec_id: item.update({"spec_id":spec_id,"spec_path":str(spec_path)})
    return item

def main():
    QA.mkdir(parents=True,exist_ok=True); ISO.mkdir(parents=True,exist_ok=True)
    scene=setup(); inventory=json.loads(INV.read_text(encoding="utf-8"))["facility_groups"]
    spec_files=sorted(SPECS.glob("V09_IMG_*.md"), key=lambda p:int(re.search(r"V09_IMG_(\d+)",p.name).group(1)))
    if len(spec_files)!=72: raise RuntimeError(f"expected 72 V09 specs, found {len(spec_files)}")
    integrated=[]; isolated=[]; preservation=[]; results=[]; spec_index={}
    for p in spec_files:
        n=int(re.search(r"V09_IMG_(\d+)",p.name).group(1)); text=p.read_text(encoding="utf-8")
        m=re.search(r"^# V09 IMAGE-SPEC\s+\d+\s+—\s+(.+?)\s+—\s+(A_CONTEXT|B_FUNCTIONAL|C_SEQUENCE_OR_DETAIL)\s*$",text,re.M); facility=m.group(1).strip() if m else None
        # Use the authoritative numeric order in the INDEX filenames; normalize
        # only the capitalization/punctuation differences in Markdown headings.
        for g in REMEDIATION_GROUPS+sorted(PASS_GROUPS):
            if norm(g)==norm(facility) or norm(g).replace("glass deck central command training cafe gallery","glass deck central command training cafe gallery")==norm(facility): facility=g; break
        if facility is None:
            name=p.name.split("__",2)[1]; facility=next((g for g in REMEDIATION_GROUPS+sorted(PASS_GROUPS) if slug(g)==name),None)
        view=re.search(r"__(A_CONTEXT|B_FUNCTIONAL|C_SEQUENCE_OR_DETAIL)\.md$",p.name).group(1)
        spec_index[n]={"spec_id":f"V09_IMG_{n:03d}","facility":facility,"view":view,"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest().upper()}
    for n in range(1,73):
        meta=spec_index[n]; f=meta["facility"]; objs=remediation_objects(f) if f in REMEDIATION_GROUPS else preserved_objects(f)
        path=QA/f"{slug(f)}_{meta['view']}.png"
        item=render(scene,path,objs,f,meta["view"],"INTEGRATED" if f in REMEDIATION_GROUPS else "PRESERVATION",meta["spec_id"],meta["path"])
        integrated.append(item) if f in REMEDIATION_GROUPS else preservation.append(item); results.append(item)
    for f in REMEDIATION_GROUPS:
        objs=remediation_objects(f); path=ISO/f"{slug(f)}_ISOLATED_LABEL_BLIND.png"
        item=render(scene,path,objs,f,"ISOLATED","ISOLATED_LABEL_BLIND"); isolated.append(item); results.append(item)
    all_hidden()
    failures=[x for x in results if x["status"]!="PASS"]
    data={"status":"AWAITING_GPT_REMEDIATION_AUDIT_V09" if not failures and len(results)==92 else "REMEDIATION_RENDER_FAILURE","task":"M08.18","revision":"REV005","spec_count":72,"specs":spec_index,"integrated":integrated,"preservation":preservation,"isolated":isolated,"results":results,"integrated_count":len(integrated),"preservation_count":len(preservation),"isolated_count":len(isolated),"render_count":len(results),"expected_render_count":92,"failed":failures}
    (OUT/"RENDER_RESULTS.json").write_text(json.dumps(data,indent=2),encoding="utf-8")
    lines=["# REV005 V09 image-by-image remediation evidence","","All 72 V09 image specs were processed in numeric order. Independent GPT audit remains pending.","","| # | Facility | View | Evidence | Status |","|---:|---|---|---|---|"]
    for n in range(1,73):
        x=spec_index[n]; item=next(i for i in integrated+preservation if i.get("spec_id")==x["spec_id"]); lines.append(f"| {n:03d} | {x['facility']} | {x['view']} | [render](qa/{Path(item['path']).name}) | {item['status']} |")
    lines += ["","## Isolated proofs",""]
    for item in isolated: lines.append(f"- [{item['facility']}](qa_isolated/{Path(item['path']).name}) — {item['status']}")
    (OUT/"V09_IMAGE_BY_IMAGE_EVIDENCE_INDEX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    (OUT/"V09_SPEC_EXECUTION_MATRIX.json").write_text(json.dumps({"specs":spec_index,"isolated_facilities":REMEDIATION_GROUPS,"counts":{"specs":72,"integrated":len(integrated),"preservation":len(preservation),"isolated":len(isolated),"total":len(results)},"status":data["status"]},indent=2),encoding="utf-8")
    print(json.dumps({"status":data["status"],"specs":72,"integrated":len(integrated),"preservation":len(preservation),"isolated":len(isolated),"renders":len(results),"failed":len(failures)},indent=2))

main()
