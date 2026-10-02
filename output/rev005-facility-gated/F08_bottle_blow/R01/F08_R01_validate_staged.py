import bpy,json
from pathlib import Path
ROOT=Path(r'C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus'); BASE=ROOT/'output/rev005-facility-gated/F08_bottle_blow'; WORK=BASE/'R01/F08_bottle_blow'; OUT=BASE/'R01'; issues=[]
bpy.context.view_layer.update()
published=json.loads((BASE/'F08_NEW_ACCEPTED_MANIFEST.json').read_text(encoding='utf-8')); template=json.loads((WORK/'F08_NEW_ACCEPTED_MANIFEST.json').read_text(encoding='utf-8')); coll=bpy.data.collections.get(template['destination_collection'])
if not coll:issues.append('missing destination collection')
actual=list(coll.objects) if coll else [];actual_by={o.name:o for o in actual};fresh_rows=[]
for o in sorted(actual,key=lambda x:x.name):
 if o.type!='MESH':continue
 fresh_rows.append({'name':o.name,'role':o.get('F08_role'),'location':[round(float(x),4) for x in o.location],'dimensions':[round(float(x),4) for x in o.dimensions],'materials':[m.name if m else None for m in o.data.materials]})
rebuilt={'task':'M08.43 / F08-R01 only','destination_collection':template['destination_collection'],'count':len(fresh_rows),'objects':fresh_rows}
(OUT/'F08_R01_REBUILT_MANIFEST.json').write_text(json.dumps(rebuilt,indent=2),encoding='utf-8');reloaded=json.loads((OUT/'F08_R01_REBUILT_MANIFEST.json').read_text(encoding='utf-8'));rows=reloaded['objects'];row_by={r['name']:r for r in rows};expected=set(row_by)
if len(rows)!=338:issues.append('rebuilt manifest mesh count '+str(len(rows)))
if len(actual)!=338:issues.append('destination collection object count '+str(len(actual)))
if set(actual_by)!=expected:issues.append('destination collection names differ from rebuilt mesh manifest')
max_loc_err=max_dim_err=0.0;material_mismatches=[]
for name,row in row_by.items():
 o=actual_by.get(name)
 if not o:continue
 loc=[round(float(x),4) for x in o.location];dims=[round(float(x),4) for x in o.dimensions];mats=[m.name if m else None for m in o.data.materials]
 le=max(abs(loc[i]-float(row['location'][i])) for i in range(3));de=max(abs(dims[i]-float(row['dimensions'][i])) for i in range(3));max_loc_err=max(max_loc_err,le);max_dim_err=max(max_dim_err,de)
 if mats!=row.get('materials',[]):material_mismatches.append(name)
 if le>0.0005 or de>0.0005:issues.append('rebuilt signature mismatch '+name)
if material_mismatches:issues.append('rebuilt material mismatch '+repr(material_mismatches))
old={r['name']:r for r in published['objects']};new={r['name']:r for r in rows};old_diffs=[]
for n in sorted(set(old)|set(new)):
 a=old.get(n);b=new.get(n)
 if a is None or b is None:old_diffs.append({'name':n,'difference':'membership'});continue
 fields=[k for k in ('location','dimensions','materials') if a.get(k)!=b.get(k)]
 if fields:old_diffs.append({'name':n,'changed_fields':fields,'published_location':a.get('location'),'rebuilt_location':b.get('location'),'published_dimensions':a.get('dimensions'),'rebuilt_dimensions':b.get('dimensions')})
allowed=['F08_EAST_DOOR_JAMB_0','F08_EAST_DOOR_JAMB_1','F08_EAST_WALL_NORTH','F08_EAST_WALL_SOUTH']
(OUT/'F08_R01_PUBLISHED_MANIFEST_COMPARISON.json').write_text(json.dumps({'task':'M08.43 / F08-R01 only','published_manifest':'F08_NEW_ACCEPTED_MANIFEST.json','rebuilt_manifest':'F08_R01_REBUILT_MANIFEST.json','differences':old_diffs,'expected_differences_from_published_helpers':allowed,'matches_expected_helper_refresh':[x['name'] for x in old_diffs]==allowed},indent=2),encoding='utf-8')
if [x['name'] for x in old_diffs]!=allowed:issues.append('unexpected difference from published M08.42 manifest: '+repr([x['name'] for x in old_diffs]))
inventory=json.loads((WORK/'F08_LEGACY_BOTTLE_BLOW_INVENTORY.json').read_text(encoding='utf-8'));confirmed=[r for r in inventory['candidates'] if r['ownership_classification']=='CONFIRMED_F08_LEGACY'];retired=[]
for row in confirmed:
 o=bpy.data.objects.get(row['name'])
 if o and o.get('REV005_F08_LEGACY_RETIRED') is True and o.get('REV005_F08_RETIRED_BY')=='F08_CLASS_N' and o.hide_viewport and o.hide_render:retired.append(o.name)
if len(confirmed)!=391 or len(retired)!=391:issues.append('legacy expected/retired count mismatch')
protection=json.loads((WORK/'F08_PROTECTION_DIFF.json').read_text(encoding='utf-8'));dim_e=json.loads((WORK/'F08_DIMENSIONAL_VALIDATION.json').read_text(encoding='utf-8'));parity=json.loads((WORK/'F08_GLB_EXPORT_PARITY.json').read_text(encoding='utf-8'));legacy_diff=json.loads((WORK/'F08_LEGACY_RETIREMENT_DIFF.json').read_text(encoding='utf-8'))
for label,obj in [('protection',protection),('dimensional',dim_e),('GLB parity',parity),('legacy retirement',legacy_diff)]:
 if obj.get('status')!='PASS':issues.append(label+' evidence not PASS')
if parity.get('expected_node_count')!=10888 or parity.get('actual_node_count')!=10888 or parity.get('missing_expected_names') or parity.get('unexpected_names'):issues.append('GLB parity fact mismatch')
if dim_e.get('cross_facility_collisions')!=[] or dim_e.get('outside_envelope_objects')!=[]:issues.append('collision/envelope evidence mismatch')
roles={}
for row in rows:roles.setdefault(row['role'],[]).append(row['name'])
counts={'accepted_meshes':len(rows),'confirmed_legacy':len(confirmed),'retired_legacy':len(retired),'preforms':len(roles.get('PET preform product',[])),'heater_elements':len(roles.get('distinct infrared heater element',[])),'service_doors':len(roles.get('transparent blow-cell service door',[])),'air_branches':len(roles.get('high-pressure air branch drop',[])),'formed_bottles':len(roles.get('formed bottle product',[]))}
expected_counts={'accepted_meshes':338,'confirmed_legacy':391,'retired_legacy':391,'preforms':20,'heater_elements':16,'service_doors':2,'air_branches':4,'formed_bottles':16}
for k,v in expected_counts.items():
 if counts.get(k)!=v:issues.append('%s expected %d got %s'%(k,v,counts.get(k)))
result={'task':'M08.43 / F08-R01 only','source_blend':'output/rev005-facility-gated/F08_bottle_blow/R01/F08_bottle_blow/F08_STAGED.blend','status':'PASS' if not issues else 'BLOCKED_F08_R01_STAGED_STATE_INVALID','manifest_expected_count':len(rows),'destination_collection_count':len(actual),'max_manifest_location_error_m':max_loc_err,'max_manifest_dimension_error_m':max_dim_err,'published_manifest_differences':old_diffs,'counts':counts,'protected_object_unauthorized_differences':0 if protection.get('status')=='PASS' else None,'cross_facility_collisions':len(dim_e.get('cross_facility_collisions',[])),'outside_envelope_objects':len(dim_e.get('outside_envelope_objects',[])),'glb_expected_actual':[parity.get('expected_node_count'),parity.get('actual_node_count')],'all_locked_technical_facts_pass':not issues,'issues':issues}
(OUT/'F08_R01_STAGED_STATE_VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print('F08_R01_STAGED_STATE_VALIDATION',json.dumps(result,sort_keys=True))
if issues:raise RuntimeError(result['status']+' '+str(issues))
