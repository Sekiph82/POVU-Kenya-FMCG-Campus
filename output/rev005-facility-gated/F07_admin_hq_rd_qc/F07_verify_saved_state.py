import bpy, hashlib, json, struct
from pathlib import Path
root=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus')
e=root/'output/rev005-facility-gated/F07_admin_hq_rd_qc'
blend=root/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend'
glb=root/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
col=bpy.data.collections.get('REV005_FG_F07_ADMIN_HQ_RD_QC_ACCEPTED_CLASS_N')
new=[o for o in col.objects if o.type=='MESH'] if col else []
retired=[o for o in bpy.data.objects if o.get('REV005_F07_LEGACY_RETIRED') is True]
raw=glb.read_bytes(); n=struct.unpack_from('<I',raw,12)[0]
g=json.loads(raw[20:20+n].decode('utf-8').rstrip('\x00 ')); names={str(x['name']) for x in g.get('nodes',[]) if x.get('name')}
p= json.loads((e/'F07_GLB_EXPORT_PARITY.json').read_text())
checks={'saved_destination_collection_exists':col is not None,'new_f07_mesh_count':len(new),'new_f07_mesh_count_pass':len(new)==789,'retired_legacy_count':len(retired),'retired_legacy_count_pass':len(retired)==446,'all_retired_hidden':all(o.hide_viewport and o.hide_render for o in retired),'glb_actual_node_count':len(names),'glb_parity_expected':p['expected_node_count'],'glb_node_membership_exact':len(names)==p['expected_node_count'] and not p['missing_expected_names'] and not p['unexpected_names'],'blend_sha256':sha(blend),'glb_sha256':sha(glb),'blend_hash_matches_final_hashes':sha(blend)==json.loads((e/'F07_FINAL_HASHES.json').read_text())['blend_sha256'],'glb_hash_matches_final_hashes':sha(glb)==json.loads((e/'F07_FINAL_HASHES.json').read_text())['glb_sha256']}
checks['status']='PASS' if all(v for k,v in checks.items() if k.endswith('_pass') or k.endswith('_exact') or k.endswith('_hidden') or k.endswith('_exists') or k.startswith('blend_hash_matches') or k.startswith('glb_hash_matches')) else 'FAIL'
(e/'F07_FINAL_STATE_CHECK.json').write_text(json.dumps(checks,indent=2))
print('F07_FINAL_STATE_CHECK',checks['status'],json.dumps(checks))
