import bpy, json, hashlib, struct
from pathlib import Path
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
E=ROOT/'output/rev005-facility-gated/F08_bottle_blow'
BLEND=ROOT/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend'
GLB=ROOT/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
OWNER=ROOT/'output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json'
F07=ROOT/'output/rev005-facility-gated/F07_admin_hq_rd_qc/F07_PROTECTION_AFTER.json'
EXPECTED_BLEND='B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642'
EXPECTED_GLB='B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372'
FACILITY='Bottle blow molding'
assert bpy.context.scene is not None

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def cv(v):
 if hasattr(v,'to_list'):return v.to_list()
 if isinstance(v,(str,int,float,bool)) or v is None:return v
 try:return [cv(x) for x in v]
 except:return str(v)
def sig(o):
 return {'name':o.name,'type':o.type,'matrix_world':[[round(float(o.matrix_world[r][c]),9) for c in range(4)] for r in range(4)],
 'dimensions':[round(float(x),9) for x in o.dimensions],'parent':o.parent.name if o.parent else None,
 'collections':sorted(c.name for c in o.users_collection),'material_slots':[s.material.name if s.material else None for s in o.material_slots],
 'data_block':o.data.name if o.data else None,'hide_viewport':bool(o.hide_viewport),'hide_render':bool(o.hide_render),
 'hide_set':bool(o.hide_get()),'custom_properties':{k:cv(o[k]) for k in o.keys()}}
assert sha(BLEND)==EXPECTED_BLEND, 'BLOCKED_F08_CANONICAL_BASELINE_MISMATCH_BLEND'
assert sha(GLB)==EXPECTED_GLB, 'BLOCKED_F08_CANONICAL_BASELINE_MISMATCH_GLB'
(E/'F08_BASELINE_HASHES.json').write_text(json.dumps({'task':'M08.42 / F08 only','status':'PASS','expected':{'blend_sha256':EXPECTED_BLEND,'glb_sha256':EXPECTED_GLB},'observed':{'blend_sha256':sha(BLEND),'glb_sha256':sha(GLB)},'blend_path':str(BLEND.relative_to(ROOT)),'glb_path':str(GLB.relative_to(ROOT))},indent=2),encoding='utf-8')
# F01-F06 and all previously protected historic/quarantine signatures from the last accepted run.
prior=json.loads(F07.read_text(encoding='utf-8'))
protected={k:[dict(r,hide_set=bool(bpy.data.objects[r['name']].hide_get())) for r in rows] for k,rows in prior['objects'].items()}
# Include the accepted F07 object set and exact saved retired legacy state.
f07coll='REV005_FG_F07_ADMIN_HQ_RD_QC_ACCEPTED_CLASS_N'
f07accepted=sorted((o for o in bpy.data.objects if f07coll in [c.name for c in o.users_collection] and o.type=='MESH'),key=lambda o:o.name)
f07retired=sorted((o for o in bpy.data.objects if o.get('REV005_F07_LEGACY_RETIRED') is True and o.get('REV005_F07_RETIRED_BY')=='F07_CLASS_N'),key=lambda o:o.name)
assert len(f07accepted)==789, f'F07_ACCEPTED_COUNT_MISMATCH {len(f07accepted)}'
assert len(f07retired)==446, f'F07_RETIRED_COUNT_MISMATCH {len(f07retired)}'
protected['F07_accepted']=[sig(o) for o in f07accepted]
protected['F07_exact_446_retired_legacy']=[sig(o) for o in f07retired]
# Snapshot visibility of all pre-existing collections and current view-layer tree flags.
collections={c.name:{'hide_viewport':bool(c.hide_viewport),'hide_render':bool(c.hide_render)} for c in bpy.data.collections}
def layer_snapshot(layer,prefix=''):
 out={}
 for c in layer.children:
  path=prefix+'/'+c.name
  out[path]={'exclude':bool(c.exclude),'hide_viewport':bool(c.hide_viewport)}
  out.update(layer_snapshot(c,path))
 return out
layers=layer_snapshot(bpy.context.view_layer.layer_collection)
# Parse exact pre-F08 GLB named-node membership.
b=b'\x00'; raw=GLB.read_bytes(); jlen=struct.unpack_from('<I',raw,12)[0]; gltf=json.loads(raw[20:20+jlen].decode('utf-8').rstrip('\x00 '))
glb_names=sorted({str(n['name']) for n in gltf.get('nodes',[]) if n.get('name')})
# Owner inventory supplies known current F08 candidates; no historical count is assumed.
owner=json.loads(OWNER.read_text(encoding='utf-8'))
owner_names=set(owner.get('facilities',{}).get(FACILITY,{}).get('objects',[]))
legacy_coll='REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING'
candidates={};
for o in bpy.data.objects:
 cols={c.name for c in o.users_collection}; props={k:cv(o[k]) for k in o.keys()}
 meta=props.get('rev005_facility')==FACILITY
 legacy_facility=str(props.get('facility','')).strip().casefold()=='bottle blow molding'
 in_coll=legacy_coll in cols
 owner_match=o.name in owner_names
 low=o.name.lower()
 named=('bottle_blow' in low or 'bottleblow' in low or 'preform' in low or 'blow_mold' in low)
 retired_group=str(props.get('REV005_V08_RETIRED_GROUP','')).strip().casefold()
 prior_f08=retired_group=='bottle blow molding'
 other_retired=bool(retired_group) and not prior_f08
 current_v09=bool(props.get('REV005_V09_REMEDIATED') or props.get('REV005_V09_IMAGE_BY_IMAGE')) and (legacy_facility or meta or in_coll)
 reason=[]
 if meta or legacy_facility:reason.append('facility_metadata_exact')
 if in_coll:reason.append('legacy_collection_exact')
 if owner_match:reason.append('owner_inventory_exact_name')
 if named:reason.append('current_name_provenance')
 if current_v09:reason.append('current_V09_bottle_blow_provenance')
 if prior_f08:reason.append('prior_retired_group_exact_bottle_blow')
 if reason:
  hard=meta or legacy_facility or in_coll or owner_match or prior_f08 or current_v09
  cls='CONFIRMED_F08_LEGACY' if hard else ('NOT_F08' if other_retired else 'AMBIGUOUS_SHARED')
  row=sig(o); row['facility_metadata']=props.get('rev005_facility',props.get('facility'));row['candidate_reasons']=reason
  row['in_pre_f08_glb']=o.name in glb_names;row['ownership_classification']=cls
  candidates[o.name]=row
counts={k:sum(1 for r in candidates.values() if r['ownership_classification']==k) for k in ('CONFIRMED_F08_LEGACY','AMBIGUOUS_SHARED','NOT_F08')}
inv={'task':'M08.42 / F08 only','status':'INVENTORIED','legacy_collection_expected':'REV005_V08_CLEAN_BOTTLE_BLOW_MOLDING','legacy_collection_present':bpy.data.collections.get(legacy_coll) is not None,'legacy_collection_member_count':len(bpy.data.collections[legacy_coll].all_objects) if bpy.data.collections.get(legacy_coll) else 0,'owner_inventory_candidate_count':len(owner_names),'candidate_count':len(candidates),'classification_counts':counts,'pre_f08_glb_named_node_count':len(glb_names),'pre_f08_glb_names':glb_names,'candidates':[candidates[n] for n in sorted(candidates)]}
(E/'F08_LEGACY_BOTTLE_BLOW_INVENTORY.json').write_text(json.dumps(inv,indent=2,ensure_ascii=False),encoding='utf-8')
prot={'task':'M08.42 / F08 only','baseline_hashes':{'blend_sha256':EXPECTED_BLEND,'glb_sha256':EXPECTED_GLB},'status':'PRE_MUTATION_SNAPSHOT','counts':{k:len(v) for k,v in protected.items()},'objects':protected,'preexisting_collection_visibility':collections,'preexisting_layer_visibility':layers}
(E/'F08_PROTECTION_BEFORE.json').write_text(json.dumps(prot,indent=2,ensure_ascii=False),encoding='utf-8')
print('F08_PREFLIGHT_SNAPSHOT PASS',sha(BLEND),sha(GLB),'protected',sum(len(v) for v in protected.values()),'F07 accepted',len(f07accepted),'F07 retired',len(f07retired),'candidates',len(candidates),counts,'GLB nodes',len(glb_names))
