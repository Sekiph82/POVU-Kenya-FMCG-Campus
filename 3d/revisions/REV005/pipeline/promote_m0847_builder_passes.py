import bpy, hashlib, json, struct
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
REV=ROOT/"3d/revisions/REV005"
BLEND=REV/"POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB=REV/"POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
STAGE=ROOT/"output/rev005-facility-gated/F08_F15_combined/REV005_F08_F15_STAGED.blend"
OUT=ROOT/"output/rev005-facility-gated/F08_F15_combined"
CANDIDATE=OUT/"M0847_PROMOTION_CANDIDATE.blend"
CANDIDATE_GLB=OUT/"M0847_PROMOTION_CANDIDATE.glb"
PROMOTE={
 "F10":"REV005_V08_CLEAN_ETP_WATER_TREATMENT",
 "F12":"REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY",
 "F13":"REV005_V08_CLEAN_LIQUID_FILLING_PACKAGING",
 "F14":"REV005_V08_CLEAN_OCCUPATIONAL_HEALTH_FIRST_AID",
}

def sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest().upper()

def bounds_and_signature(obj):
 mat=tuple(round(float(v),6) for row in obj.matrix_world for v in row)
 geometry=""
 if obj.type=="MESH" and obj.data:
  payload=repr((len(obj.data.vertices),len(obj.data.edges),len(obj.data.polygons),tuple(round(float(x),6) for v in obj.data.vertices for x in v.co),tuple(tuple(p.vertices) for p in obj.data.polygons))).encode()
  geometry=hashlib.sha256(payload).hexdigest().upper()
 mats=tuple(m.name if m else None for m in (obj.data.materials if getattr(obj,"data",None) and hasattr(obj.data,"materials") else []))
 return {"type":obj.type,"matrix_world":mat,"geometry_sha256":geometry,"materials":mats,"hide_render":obj.hide_render,"hide_viewport":obj.hide_viewport}

def read_glb_names(path):
 data=path.read_bytes()
 if data[:4]!=b"glTF": raise RuntimeError("candidate is not a GLB")
 pos=12; names=[]
 while pos+8<=len(data):
  n,kind=struct.unpack_from("<II",data,pos); pos+=8
  chunk=data[pos:pos+n];pos+=n
  if kind==0x4E4F534A:
   j=json.loads(chunk.decode("utf-8"));names=[x.get("name") for x in j.get("nodes",[]) if x.get("name")];return names,j
 raise RuntimeError("GLB JSON chunk absent")

def main():
 initial={"blend":sha(BLEND),"glb":sha(GLB)}
 bpy.ops.wm.open_mainfile(filepath=str(BLEND))
 scene=bpy.context.scene
 protected_before={o.name:bounds_and_signature(o) for o in bpy.data.objects if not any(o.name in set(bpy.data.collections[n].objects.keys()) for n in PROMOTE.values() if bpy.data.collections.get(n))}
 old_counts={}
 for fid,cname in PROMOTE.items():
  col=bpy.data.collections.get(cname)
  if col is None: raise RuntimeError(f"existing target collection absent: {cname}")
  objs=list(col.objects);old_counts[fid]=len(objs)
  linked_elsewhere=[o.name for o in objs if any(c!=col for c in o.users_collection)]
  if linked_elsewhere: raise RuntimeError(f"target collection has cross-linked objects; preserve/inspect before mutation: {linked_elsewhere[:12]}")
  for o in objs: bpy.data.objects.remove(o,do_unlink=True)
  bpy.data.collections.remove(col)
 with bpy.data.libraries.load(str(STAGE),link=False) as (src,dst):
  absent=[c for c in PROMOTE.values() if c not in src.collections]
  if absent: raise RuntimeError(f"candidate source collections absent: {absent}")
  dst.collections=list(PROMOTE.values())
 added={}
 for fid,cname in PROMOTE.items():
  col=next((c for c in dst.collections if c and c.name==cname),None)
  if col is None: raise RuntimeError(f"append did not return {cname}")
  col.hide_render=False;col.hide_viewport=False
  scene.collection.children.link(col)
  names=[o.name for o in col.objects]
  suffixed=[n for n in names if n.endswith(".001") or n.endswith(".002")]
  if suffixed: raise RuntimeError(f"unexpected imported name collision in {fid}: {suffixed[:12]}")
  added[fid]={"collection":cname,"objects":len(names),"meshes":sum(o.type=="MESH" for o in col.objects),"names":names}
 bpy.context.scene["M08_47_BUILDER_PASS_PROMOTIONS"]=json.dumps(list(PROMOTE))
 bpy.context.scene["M08_47_STATUS"]="AWAITING_GPT_F08_F15_FINAL_AUDIT_WITH_RECORDED_BLOCKERS"
 bpy.ops.wm.save_as_mainfile(filepath=str(CANDIDATE),check_existing=False)
 try:
  bpy.ops.export_scene.gltf(filepath=str(CANDIDATE_GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True,use_selection=False,use_visible=True)
  visibility="use_visible=True"
 except TypeError:
  bpy.ops.export_scene.gltf(filepath=str(CANDIDATE_GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True,use_selection=False)
  visibility="operator_fallback_without_use_visible"
 names,j=read_glb_names(CANDIDATE_GLB)
 present=set(names)
 glb={}
 for fid,item in added.items():
  expected=set(item["names"])
  mesh_names={o.name for o in bpy.data.collections[item["collection"]].objects if o.type=="MESH"}
  missing=mesh_names-present
  glb[fid]={"blend_meshes":len(mesh_names),"glb_mesh_objects_found":len(mesh_names&present),"missing_mesh_objects":sorted(missing)}
  if missing: raise RuntimeError(f"GLB membership mismatch for {fid}: {sorted(missing)[:20]}")
 protected_after={o.name:bounds_and_signature(o) for o in bpy.data.objects if not any(o.name in set(bpy.data.collections[n].objects.keys()) for n in PROMOTE.values() if bpy.data.collections.get(n))}
 removed=sorted(set(protected_before)-set(protected_after));new=sorted(set(protected_after)-set(protected_before))
 changed=sorted(n for n in set(protected_before)&set(protected_after) if protected_before[n]!=protected_after[n])
 if removed or new or changed: raise RuntimeError(f"out-of-scope signature drift: removed={removed[:10]} new={new[:10]} changed={changed[:10]}")
 report={"status":"PROMOTION_CANDIDATE_VALIDATED","task":"M08.47","initial_canonical_hashes":initial,"candidate_hashes":{"blend":sha(CANDIDATE),"glb":sha(CANDIDATE_GLB)},"candidate_paths":{"blend":str(CANDIDATE.relative_to(ROOT)),"glb":str(CANDIDATE_GLB.relative_to(ROOT))},"promoted_builder_pass_collections":added,"previous_object_counts":old_counts,"glb_parity":glb,"export_visibility":visibility,"non_promoted_scene_signature":{"baseline_objects":len(protected_before),"final_objects":len(protected_after),"removed":removed,"new":new,"changed":changed,"result":"PASS"},"canonical_files_mutated":False,"note":"Candidate only. Apply to canonical files only after all reported parity/protection checks complete."}
 (OUT/"M08_47_PROMOTION_CANDIDATE_VALIDATION.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps({"status":report["status"],"candidate_hashes":report["candidate_hashes"],"promotion_counts":{k:{"objects":v["objects"],"meshes":v["meshes"]} for k,v in added.items()},"glb_parity":glb,"protected_scene":"PASS"},indent=2))

main()
