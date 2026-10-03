import json,shutil
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus'); R=ROOT/'output/rev005-facility-gated/F08_bottle_blow/R02'; J=R/'F08_R02_CAMERA_CANDIDATES.json'
chosen={
'A':['A_001','A_002','A_003','A_004','A_005','A_006','A_007','A_010'],
'B':['B_002','B_004','B_005','B_006','B_007','B_008','B_014','B_020'],
'C':['C_004','C_005','C_006','C_007','C_008','C_009','C_020','C_021'],
'D':['D_001','D_002','D_003','D_006','D_007','D_008','D_009','D_010']}
selected={'A':'A_006','B':'B_005','C':'C_007','D':'D_003'}
reasons={
'A':'Shows the oven, transfer area, guarded cell, outfeed direction, and room context; the upstream bulk hopper remains visually indistinct/out of frame, so the required complete context sequence fails.',
'B':'Shows the heater outlet, transfer, cell, and outfeed in one functional view; mould clamp/stretch-blow and formed-bottle transformation are not sufficiently readable at 900x600.',
'C':'Best sequence detail candidate for oven edge, transfer guide, mould stations, and discharge; no single readable preform-to-bottle transformation is established in frame.',
'D':'Shows the room, process direction, HMI-side aisle, and cell context; the bulk source hopper is not identifiable and the complete bulk-to-outfeed sequence is not label-blind readable.'}
cues={
'A':{'hopper_visibly_distinct':False,'elevator_feed_visible':True,'oven_visible':True,'transfer_visible':True,'blow_cell_visible':True,'outfeed_visible':True,'room_context_visible':True,'complete_process_sequence_readable':False},
'B':{'heater_outlet_visible':True,'transfer_visible':True,'blow_cell_visible':True,'mould_station_readable':True,'stretch_blow_readable':False,'outfeed_visible':True,'formed_bottles_readable':False,'transformation_inferable':False,'complete_role_readable':False},
'C':{'oven_transfer_visible':True,'mould_clamp_readable':True,'stretch_blow_cue_visible':True,'preform_to_bottle_transformation_readable':False,'discharge_outfeed_visible':True,'complete_role_readable':False},
'D':{'hopper_visibly_distinct':False,'feed_visible':True,'oven_visible':True,'blow_cell_visible':True,'outfeed_visible':True,'hmi_operator_side_visible':True,'aisle_context_visible':True,'complete_sequence_readable':False}}
j=json.loads(J.read_text(encoding='utf-8')); by={x['id']:x for x in j['records']}; assert len(by)==96 and all(x['rendered'] and not x['camera_inside_mesh_aabb_objects'] for x in j['records'])
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
for role,ids in chosen.items():
 assert len(ids)==8
 imgs=[]
 for cid in ids:
  rec=by[cid]; src=R/rec['render_path']; assert src.exists(); imgs.append((cid,src))
 w,h,lab,cols=300,200,28,4; sheet=Image.new('RGB',(cols*w,2*(h+lab)),(28,28,28));d=ImageDraw.Draw(sheet)
 for n,(cid,path) in enumerate(imgs):
  im=Image.open(path).convert('RGB').resize((w,h),Image.Resampling.LANCZOS);x=(n%cols)*w;y=(n//cols)*(h+lab);sheet.paste(im,(x,y));d.text((x+8,y+h+5),cid,fill='white',font=font)
 sheet.save(R/f'F08_R02_{role}_TOP8_CONTACT_SHEET.png')
 chosen_rec=by[selected[role]]; src=R/chosen_rec['render_path']; shutil.copy2(src,R/f'F08_R02_{role}_SELECTED_PREVIEW_900x600.png')
 for cid,_ in imgs:by[cid]['retained_top8']=True
 chosen_rec['visual_verdict']='FAIL';chosen_rec['visual_cues']=cues[role];chosen_rec['visual_rationale']=reasons[role]
for role,ids in chosen.items():
 for rec in j['records']:
  if rec['role']==role:rec['retained_top8']=rec['id'] in ids
j['retained_strongest_8_by_role']=chosen
j['visual_review_method']='Manual review of all 96 rendered 900x600 images via four 24-image review sheets; no visibility changes.'
J.write_text(json.dumps(j,indent=2),encoding='utf-8')
roles={}
for role in 'ABCD':
 rec=by[selected[role]];roles[role]={'selected_attempt_id':selected[role],'verdict':'FAIL','origin_xyz':rec['origin_xyz'],'target_xyz':rec['target_xyz'],'lens_mm':rec['lens_mm'],'selected_preview_path':f'F08_R02_{role}_SELECTED_PREVIEW_900x600.png','top8_contact_sheet_path':f'F08_R02_{role}_TOP8_CONTACT_SHEET.png','strongest_8_candidate_ids':chosen[role],'passing_cues':[k for k,v in cues[role].items() if v is True],'failing_cues':[k for k,v in cues[role].items() if v is False],'rationale':reasons[role]}
selection={'task':'M08.44 / F08-R02','status':'BLOCKED_F08_R02_VISUAL_ACCEPTANCE','stage_blend':'F08_R02_STAGED.blend','canonical_promotion_authorized':False,'canonical_blend_modified':False,'canonical_glb_modified':False,'candidate_counts':{r:24 for r in 'ABCD'},'camera_origin_mesh_bounds_hits':0,'camera_visibility_mutations':0,'all_roles_pass':False,'roles':roles,'complete_label_blind_sequence':'bulk preforms → elevator/feed → IR heating → transfer → clamp/mould + stretch/blow → formed bottles → inspection/outfeed','complete_sequence_pass':False,'stop_reason':'No selected role set provides a complete readable label-blind process sequence with an identifiable bulk hopper, readable blow transformation, and sufficiently legible formed-bottle outfeed. R02 remains stage-only for independent GPT facility audit.'}
(R/'F08_R02_VISUAL_SELECTION.json').write_text(json.dumps(selection,indent=2),encoding='utf-8')
print('Top8 sheets and selected previews created; selection blocked as evidence requires.')
