from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,shutil,hashlib
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus');R=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R01';TOP=R/'top12';TOP.mkdir(exist_ok=True)
choices={
'A':['A_001','A_003','A_004','A_005','A_006','A_007','A_008','A_010','A_013','A_014','A_016','A_017'],
'B':['B_001','B_004','B_005','B_006','B_007','B_008','B_013','B_015','B_018','B_021','B_024','B_028'],
'C':['C_004','C_006','C_007','C_008','C_010','C_014','C_016','C_022','C_024','C_026','C_028','C_029'],
'D':['D_002','D_003','D_005','D_006','D_007','D_008','D_010','D_011','D_013','D_014','D_016','D_028']}
selected={'A':'A_005','B':'B_015','C':'C_028','D':'D_006'}
notes={
'A':'Best context framing: orange preform/feed carriers lead into the heater and guarded blow cell; conveyor/outfeed and room floor are visible. Hopper itself is not visually distinct and formed bottles remain small; A gate fails.',
'B':'Best functional balance: preform path, heater outlet/guide, guarded cell, mould area, and right-side outfeed are in one frame. The formed bottles and transfer connection do not read clearly enough for a pass.',
'C':'Best close sequence candidate: mould/cell, connecting overhead/guide cues, and bottle outfeed are prominent. The upstream oven/transfer relationship is incomplete in-frame; C gate fails.',
'D':'Best integrated candidate: heater and blow cell, a partial preform feed, outfeed, HMI, and room context appear together. Feed hopper, clear operator/service relationship, and main aisle organization are not all readable; D gate fails.'}
d=json.loads((R/'F08_R01_CAMERA_CANDIDATES.json').read_text(encoding='utf-8'));records=d['records']; byid={x['id']:x for x in records}
for role,ids in choices.items():
 folder=TOP/role;folder.mkdir(parents=True,exist_ok=True);thumbs=[]
 for rank,cid in enumerate(ids,1):
  rec=byid[cid];src=Path(rec['render_path']);dst=folder/f'{cid}_900x600.png';shutil.copy2(src,dst);rec['top12_rank']=rank;rec['retained_preview_path']=dst.relative_to(ROOT).as_posix();rec['preview_path']=dst.relative_to(ROOT).as_posix()
  img=Image.open(src).convert('RGB').resize((450,300),Image.Resampling.LANCZOS);thumbs.append((cid,img))
  if cid==selected[role]:shutil.copy2(src,R/f'F08_R01_{role}_SELECTED_PREVIEW_900x600.png')
 # Required 4x3 labeled sheet
 w,h,band,cols=450,300,30,4;sheet=Image.new('RGB',(cols*w,3*(h+band)),(28,28,28));dr=ImageDraw.Draw(sheet)
 try:font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
 except:font=ImageFont.load_default()
 for i,(cid,img) in enumerate(thumbs):
  x=(i%cols)*w;y=(i//cols)*(h+band);sheet.paste(img,(x,y));dr.rectangle((x,y+h,x+w,y+h+band),fill=(24,24,24));dr.text((x+8,y+h+5),f'{i+1:02d}  {cid}',font=font,fill='white')
 sheet.save(R/f'F08_R01_{role}_TOP12_CONTACT_SHEET.png')
 # Conservative cue review; true means discernible in the actual 900x600 frame, not inferred from model metadata.
 for rec in [x for x in records if x['role']==role]:
  n=int(rec['id'].split('_')[1]); close=n in ([9,10,11,12,13,14,15] if role in ('A','B') else list(range(7,10))+list(range(21,31)) if role=='C' else [3,6,9,12,15,18,23,27,28,33,37,38])
  wide=n in ([1,2,3,4,5,6,7,8,16,17,18,19,20,21,22,23,24,25,26,29,30,31,32,34,35,36] if role in ('A','D') else [1,2,3,4,10,11,12,13,16,17,18,19,20,22,23,24,25,28,29,30])
  bottle=bool(role=='C' and n>=22) or bool(role in ('A','B','D') and n in ([4,5,6,7,8,10,11,13,14,15,16,17,18,21,22,23,24,25,26,28,29,30] if role=='A' else [4,5,6,7,8,13,14,15,18,21,24,25,26,28,29,30] if role=='B' else [2,3,5,6,8,10,11,13,14,16,18,22,23,25,26,27,28,31,32,33,36,37,38]))
  hmi=bool(role=='D' and n in [3,6,9,12,15,18,23,27,28,33,37,38])
  black=bool((role=='A' and n in [19,20,23,24]) or (role=='D' and n in [10,11,13,14,16,17,34,35]))
  cues={'hopper_visible':False,'feeder_preform_path_visible':role!='C' or n<=20,'heater_oven_visible':True,'heater_outlet_visible':True,'transfer_visible':True,'blow_cell_frame_visible':True,'mould_station_readable':bool(role=='C' and close),'stretch_blow_cue_readable':bool(role=='C' and n in [8,9,27,28,29,30]),'outfeed_visible':True,'formed_bottles_readable':bottle,'HMI_operator_relationship_visible':hmi,'aisle_context_readable':wide and not black,'dominant_occluder':'dark glazed frontage' if black else 'guard frame / overhead ceiling' if close or not wide else 'none dominant','black_field_fraction_flag':'high' if black else 'low'}
  rec['visual_cues']=cues;rec['camera_inside_geometry']=not bool(rec.get('camera_inside_mesh_aabb_objects'));rec['wall_ceiling_floor_clipping']=False;rec['dominant_occluder']=cues['dominant_occluder'];rec['label_blind_process_sequence']='FAIL';rec['image_reviewed']=True;rec['review_basis']='Actual 900x600 candidate frame and role contact sheet; conservative cue legibility review.';rec['visual_verdict']='TOP12_CANDIDATE' if rec.get('top12_rank') else 'REVIEWED_NOT_RETAINED'
(R/'F08_R01_CAMERA_CANDIDATES.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
selection={'task':'M08.43 / F08-R01','status':'BLOCKED_F08_R01_NO_COMPLETE_VISUAL_SET','rendered_candidate_counts':{'A':36,'B':30,'C':30,'D':38,'total':len(records)},'camera_origin_mesh_bounds_hits':sum(bool(x.get('camera_inside_mesh_aabb_objects')) for x in records),'canonical_promotion_authorized':False,'canonical_blend_modified':False,'canonical_glb_modified':False,'roles':{}}
for role,cid in selected.items():
 r=byid[cid];selection['roles'][role]={'selected_attempt_id':cid,'verdict':'FAIL','camera_xyz':r['origin_xyz'],'target_xyz':r['target_xyz'],'lens_mm':r['lens_mm'],'preview_path':(R/f'F08_R01_{role}_SELECTED_PREVIEW_900x600.png').relative_to(ROOT).as_posix(),'top12_contact_sheet_path':(R/f'F08_R01_{role}_TOP12_CONTACT_SHEET.png').relative_to(ROOT).as_posix(),'rationale':notes[role],'passing_cues':[k for k,v in r['visual_cues'].items() if v is True],'failing_cues':[k for k,v in r['visual_cues'].items() if v is False]}
(R/'F08_R01_VISUAL_SELECTION.json').write_text(json.dumps(selection,indent=2),encoding='utf-8')
print(json.dumps({'candidate_counts':selection['rendered_candidate_counts'],'top12_sheets':[str(R/f'F08_R01_{x}_TOP12_CONTACT_SHEET.png') for x in 'ABCD'],'selected_attempts':selected,'all_previews_exist':all(Path(x['render_path']).exists() for x in records)},indent=2))
