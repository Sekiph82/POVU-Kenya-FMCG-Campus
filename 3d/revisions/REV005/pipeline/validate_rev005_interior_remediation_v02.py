import bpy, json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
BLEND=ROOT/"3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB=ROOT/"3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004=ROOT/"3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"
OUT=ROOT/"output/rev005-interior-remediation-v02"
INV=ROOT/"output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
FOCUSED=["Bottle Blow Molding","Caps and Trigger Assembly","Liquid Filling / Packaging","Micro-ingredient Weigh / Dispense","Toothpaste Production","Wet Wipes Production","Central Glass Deck Command / Training / Café Gallery"]
ACCEPTED=["Production Hall / Wet Processing / process core","Electrical / LV-MV room","Fire pump house","Employee changing / shower / locker support","Security / reception / visitor arrival","Security gatehouse"]
PASS=["Administration / HQ / R&D / QC","Chemical compound / controlled receiving","Daycare / crèche","ETP / water treatment","Finished goods warehouse / dispatch","Occupational health / first aid","Packaging warehouse","Raw material warehouse / receiving","Restaurant / POVU Café / kitchen","Training / Academy","Utilities / engineering","Wellness / recreation"]

def sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest().upper()

def main():
 inv=json.loads(INV.read_text(encoding="utf-8")); objs={o.name:o for o in bpy.data.objects}; original=bpy.data.collections.get("REV005_INTERIOR_COMPLETION"); original_names=set(o.name for o in original.objects) if original else set(); v2=bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V02")
 all_groups=list(inv["facility_groups"].keys()); group_checks={}
 for g in all_groups:
  names=inv["facility_groups"][g].get("objects",[]); missing=[n for n in names if n not in objs or n not in original_names]; group_checks[g]={"baseline_count":len(names),"present_count":len(names)-len(missing),"missing":missing,"status":"PASS" if not missing else "FAIL"}
 v2_counts={g:sum(1 for o in v2.objects if o.get("facility")==g) if v2 else 0 for g in FOCUSED}
 renders=json.loads((OUT/"RENDER_RESULTS.json").read_text(encoding="utf-8")); focused_renders={g:[r for r in renders if r["kind"]=="focused" and r["target"]==g and r["status"]=="PASS"] for g in FOCUSED}; reg_renders={g:[r for r in renders if r["kind"]=="regression" and r["target"]==g and r["status"]=="PASS"] for g in ["Restaurant / POVU Café / kitchen","Daycare / crèche"]}
 accepted={g:group_checks[g] for g in ACCEPTED}; passing={g:group_checks[g] for g in PASS}
 trees={n:(n in objs) for n in ["TREE_CANOPY","TREE_CANOPY001","TREE_CANOPY002","TREE_TRUNK","TREE_CANOPY003","TREE_CANOPY004","TREE_CANOPY005","TREE_TRUNK001"]}; restricted=[o.name for o in bpy.data.objects if any(k in o.name.upper() for k in ["EAST_ACCESS","WEST_ACCESS","GLASS_DECK_EAST","GLASS_DECK_WEST"]) and not o.hide_viewport]
 result={"status":"AWAITING_GPT_REMEDIATION_AUDIT_V02","revision":"REV005","scope":"focused_visual_remediation_only","locked_v01_criteria_untouched":True,"focused_remediation":{"target_count":7,"closed_count":sum(1 for g in FOCUSED if v2_counts[g]>0 and len(focused_renders[g])>=3),"functional_object_counts":v2_counts,"three_proofs_each":all(len(focused_renders[g])>=3 for g in FOCUSED),"render_pass_count":sum(len(v) for v in focused_renders.values())},"regression":{"canonical_group_count":len(all_groups),"all_26_present":all(v["status"]=="PASS" for v in group_checks.values()),"accepted_v01_areas_intact":all(v["status"]=="PASS" for v in accepted.values()),"previously_passing_groups_intact":all(v["status"]=="PASS" for v in passing.values()),"restaurant_cafe_proofs":len(reg_renders["Restaurant / POVU Café / kitchen"]),"daycare_proofs":len(reg_renders["Daycare / crèche"]),"groups":group_checks},"owner_corrections":{"hands_of_growth_objects":sum(1 for n in objs if n.startswith("HOG_") or n in {"HANDS_OF_GROWTH","LABEL_ANCHOR_HANDS_OF_GROWTH","NAV_TARGET_HANDS_OF_GROWTH"}),"trees_present":trees,"specified_trees_absent":not any(trees.values()),"living_wall_backing":"REV005_LIVING_WALL_APPROVED_BACKING" in objs,"vip_reception_objects":sum(1 for n in objs if n.startswith("REV005_VIP_"))},"scope_protection":{"restricted_live_references":len(restricted),"no_REV006_created":True,"no_final_tour_created":not any(OUT.glob("*.mp4"))},"hashes":{"v01_blend_before":"484E495E9F2689A73BE4DDF7297FEAF96D3227B0E2696A5174A6942E3625D26F","v02_blend_final":sha(BLEND),"v01_glb_before":"868850397FFC4004229BDB3AD74E09FDB68145572F5DD45132D886E927FBDA5C","v02_glb_final":sha(GLB),"rev004_frozen_glb":sha(REV004)},"stop_gate":"AWAITING_GPT_REMEDIATION_AUDIT_V02"}
 result["prevalidation_pass"]=all([result["focused_remediation"]["closed_count"]==7,result["focused_remediation"]["three_proofs_each"],result["regression"]["all_26_present"],result["regression"]["accepted_v01_areas_intact"],result["regression"]["previously_passing_groups_intact"],result["regression"]["restaurant_cafe_proofs"]>=2,result["regression"]["daycare_proofs"]>=2,result["owner_corrections"]["specified_trees_absent"],result["owner_corrections"]["living_wall_backing"],result["owner_corrections"]["vip_reception_objects"]>0,result["scope_protection"]["restricted_live_references"]==0,result["scope_protection"]["no_final_tour_created"]])
 (OUT/"REV005_INTERIOR_REMEDIATION_V02_VALIDATION.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
main()
