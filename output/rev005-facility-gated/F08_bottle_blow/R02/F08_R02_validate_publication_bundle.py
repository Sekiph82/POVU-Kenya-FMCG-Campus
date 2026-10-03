import json,hashlib
from pathlib import Path
from PIL import Image
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');R=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R02'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
tech=json.loads((R/'F08_R02_VALIDATION.json').read_text());col=json.loads((R/'F08_R02_COLLISION_VALIDATION.json').read_text());dim=json.loads((R/'F08_R02_DIMENSIONAL_VALIDATION.json').read_text());prot=json.loads((R/'F08_R02_PROTECTION_DIFF.json').read_text());sel=json.loads((R/'F08_R02_VISUAL_SELECTION.json').read_text());cams=json.loads((R/'F08_R02_CAMERA_CANDIDATES.json').read_text());manifest=json.loads((R/'F08_R02_ACCEPTED_MANIFEST.json').read_text())
assert tech['accepted_meshes']==391 and col['status']==dim['status']==prot['status']=='PASS'
assert len(manifest['objects'])==391 and manifest['count']==391
assert len(cams['records'])==96 and all(x['rendered'] and not x['camera_inside_mesh_aabb_objects'] and not x['visibility_changed'] for x in cams['records'])
assert all(sum(x['role']==role for x in cams['records'])==24 for role in 'ABCD')
for role,ids in cams['retained_strongest_8_by_role'].items():
 assert len(ids)==8 and all((R/'candidates'/role/f'{cid}_900x600.png').exists() for cid in ids)
 sheet=Image.open(R/f'F08_R02_{role}_TOP8_CONTACT_SHEET.png');assert sheet.size==(1200,456)
 assert Image.open(R/f'F08_R02_{role}_SELECTED_PREVIEW_900x600.png').size==(900,600)
 assert sel['roles'][role]['verdict']=='FAIL'
assert sel['status']=='BLOCKED_F08_R02_VISUAL_ACCEPTANCE' and not sel['canonical_promotion_authorized']
blend=ROOT/'3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend';glb=ROOT/'3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb'
hashes={'canonical_blend_sha256':sha(blend),'canonical_glb_sha256':sha(glb),'r02_staged_blend_sha256':sha(R/'F08_R02_STAGED.blend')}
assert hashes['canonical_blend_sha256']=='B2C248A0EE3EB0322CC76A626FB101FB2AA6851C724BE9865836EBA626009642'
assert hashes['canonical_glb_sha256']=='B5C73F9294AAC384711A9493F48FA74A699508A2059077C40626AC19E3E28372'
tech.update({'status':'BLOCKED_F08_R02_VISUAL_ACCEPTANCE','technical_status':'PASS','visual_status':'FAIL','camera_candidate_counts':{r:24 for r in 'ABCD'},'all_candidate_renders_pass_file_check':True,'selected_role_verdicts':{r:sel['roles'][r]['verdict'] for r in 'ABCD'},'canonical_promotion_authorized':False,'glb_parity_prepromotion':'NOT_RUN_VISUAL_GATE_FAILED','canonical_hashes_unchanged':True,'hashes':hashes,'f09_started':False})
(R/'F08_R02_VALIDATION.json').write_text(json.dumps(tech,indent=2),encoding='utf-8')
(R/'F08_R02_CANONICAL_BASELINE_RECHECK.json').write_text(json.dumps({'task':'M08.44 / F08-R02','status':'PASS','canonical_modified':False,**hashes},indent=2),encoding='utf-8')
print('R02 publication evidence verification: PASS; task state BLOCKED_F08_R02_VISUAL_ACCEPTANCE; hashes',json.dumps(hashes))
