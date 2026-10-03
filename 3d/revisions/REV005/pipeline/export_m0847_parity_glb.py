import bpy, json, struct, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
REV=ROOT/"3d/revisions/REV005"
BASE_BLEND=ROOT/"output/rev005-facility-gated/F08_F15_combined/CANONICAL_BASELINE_BEFORE_M0847.blend"
BASE_GLB=ROOT/"output/rev005-facility-gated/F08_F15_combined/CANONICAL_BASELINE_BEFORE_M0847.glb"
CANDIDATE=ROOT/"output/rev005-facility-gated/F08_F15_combined/M0847_PROMOTION_CANDIDATE.blend"
OUT=ROOT/"output/rev005-facility-gated/F08_F15_combined"
DEST=OUT/"M0847_PROMOTION_CANDIDATE_PARITY.glb"
COLS={
 "F10":"REV005_V08_CLEAN_ETP_WATER_TREATMENT",
 "F12":"REV005_V08_CLEAN_GLASS_DECK_CENTRAL_COMMAND_TRAINING_CAF_GALLERY",
 "F13":"REV005_V08_CLEAN_LIQUID_FILLING_PACKAGING",
 "F14":"REV005_V08_CLEAN_OCCUPATIONAL_HEALTH_FIRST_AID",
}

def glb_names(p):
 data=Path(p).read_bytes();pos=12
 while pos+8<=len(data):
  n,t=struct.unpack_from("<II",data,pos);pos+=8;chunk=data[pos:pos+n];pos+=n
  if t==0x4E4F534A:
   j=json.loads(chunk.decode("utf-8").rstrip("\x00 "))
   return {x.get("name") for x in j.get("nodes",[]) if x.get("name")},j
 raise RuntimeError("GLB JSON chunk absent")

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()

def main():
 baseline_names,_=glb_names(BASE_GLB)
 bpy.ops.wm.open_mainfile(filepath=str(BASE_BLEND))
 old_target=set()
 for fid,cname in COLS.items():
  col=bpy.data.collections.get(cname)
  if not col: raise RuntimeError("baseline target collection missing: "+cname)
  old_target.update(o.name for o in col.objects)
 removed=baseline_names & old_target
 bpy.ops.wm.open_mainfile(filepath=str(CANDIDATE))
 added=set()
 target_objects=[]
 for fid,cname in COLS.items():
  col=bpy.data.collections.get(cname)
  if not col: raise RuntimeError("candidate target collection missing: "+cname)
  for o in col.objects: added.add(o.name);target_objects.append(o)
 allow=(baseline_names-removed)|added
 all_objects={o.name:o for o in bpy.data.objects}
 missing_blend=sorted(allow-set(all_objects))
 if missing_blend: raise RuntimeError("expected baseline or new GLB nodes absent from candidate Blend: "+repr(missing_blend[:30]))
 for o in bpy.context.selected_objects: o.select_set(False)
 # Export the exact old visible node set, replacing only the four authorized
 # facility sets. Selection makes visibility policy explicit and deterministic.
 for name in allow:
  o=all_objects[name]
  for c in o.users_collection:
   c.hide_render=False;c.hide_viewport=False
  o.hide_render=False;o.hide_viewport=False;o.hide_set(False);o.select_set(True)
 bpy.context.view_layer.objects.active=next(iter(all_objects[n] for n in allow if all_objects[n].type=="MESH"),None)
 bpy.ops.export_scene.gltf(filepath=str(DEST),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True,use_selection=True,use_visible=False)
 output_names,_=glb_names(DEST)
 missing=sorted(allow-output_names);extra=sorted(output_names-allow)
 if missing or extra: raise RuntimeError(f"exact GLB node parity failed: missing={len(missing)} {missing[:20]} extra={len(extra)} {extra[:20]}")
 report={"status":"PASS_EXACT_CANONICAL_NODE_SET_PARITY","baseline_blend_sha256":sha(BASE_BLEND),"baseline_glb_sha256":sha(BASE_GLB),"candidate_blend_sha256":sha(CANDIDATE),"candidate_glb_sha256":sha(DEST),"baseline_glb_named_nodes":len(baseline_names),"replaced_old_target_nodes":len(removed),"new_target_nodes":len(added),"expected_final_nodes":len(allow),"candidate_glb_nodes":len(output_names),"missing_nodes":missing,"extra_nodes":extra,"promoted_collections":{k:{"collection":v,"objects":len(bpy.data.collections[v].objects),"mesh_objects":sum(o.type=="MESH" for o in bpy.data.collections[v].objects)} for k,v in COLS.items()},"export_mode":"selected node set = baseline GLB minus replaced target facility nodes plus four new builder-pass collections"}
 (OUT/"M08_47_EXACT_GLB_NODE_PARITY.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
 print(json.dumps(report,indent=2))

main()
