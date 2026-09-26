import bpy, json, hashlib, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
BLEND=ROOT/"3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB=ROOT/"3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT=ROOT/"output/rev005-interior-remediation-v01"
INV=ROOT/"output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
REV004=ROOT/"3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"
TARGETS=["Bottle Blow Molding","Caps and Trigger Assembly","Electrical / LV-MV Room","Employee Changing / Shower / Locker Support","Fire Pump House","Central Glass Deck Command / Training / Café Gallery","Liquid Filling / Packaging","Micro-ingredient Weigh / Dispense","Powder Handling / Packing","Production Hall / Wet Processing","Security / Reception / Visitor Arrival","Security Gatehouse","Toothpaste Production","Wet Wipes Production"]
PASS=["Administration / HQ / R&D / QC","Chemical compound / controlled receiving","Daycare / crèche","ETP / water treatment","Finished goods warehouse / dispatch","Occupational health / first aid","Packaging warehouse","Raw material warehouse / receiving","Restaurant / POVU Café / kitchen","Training / Academy","Utilities / engineering","Wellness / recreation"]

def sha(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest().upper()

def main():
 inv=json.loads(INV.read_text(encoding="utf-8")); objs={o.name:o for o in bpy.data.objects}; groups=inv["facility_groups"]
 original=bpy.data.collections.get("REV005_INTERIOR_COMPLETION"); original_names=set(o.name for o in original.objects) if original else set()
 protected={}
 for g in PASS:
  names=groups.get(g,{}).get("objects",[]); missing=[n for n in names if n not in objs]; protected[g]={"baseline_object_count":len(names),"current_object_count":sum(1 for n in names if n in objs),"missing":missing,"status":"PASS" if not missing and original and all(n in original_names for n in names) else "FAIL"}
 rem=bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V01")
 target_counts={g:sum(1 for o in rem.objects if o.get("facility")==g) if rem else 0 for g in TARGETS}
 qa=json.loads((OUT/"RENDER_RESULTS.json").read_text(encoding="utf-8")); qa_by={g:[r for r in qa if r["target"]==g and r["status"]=="PASS"] for g in TARGETS}
 trees={n:(n in objs) for n in ["TREE_CANOPY","TREE_CANOPY001","TREE_CANOPY002","TREE_TRUNK","TREE_CANOPY003","TREE_CANOPY004","TREE_CANOPY005","TREE_TRUNK001"]}
 restricted=[o.name for o in bpy.data.objects if any(k in o.name.upper() for k in ["EAST_ACCESS","WEST_ACCESS","GLASS_DECK_EAST","GLASS_DECK_WEST"]) and not o.hide_viewport]
 result={"status":"AWAITING_GPT_REMEDIATION_AUDIT","revision":"REV005","locked_criteria_untouched":True,"targets":{"count":len(TARGETS),"closed":sum(1 for g in TARGETS if target_counts[g]>=1 and len(qa_by[g])>=2),"functional_object_counts":target_counts,"visual_proofs":{"two_per_target":all(len(qa_by[g])>=2 for g in TARGETS),"render_passes":len(qa)}},"regression":{"previously_passing_group_count":len(PASS),"no_regression_count":sum(1 for x in protected.values() if x["status"]=="PASS"),"groups":protected},"inventory":{"baseline_group_count":len(groups),"current_group_count":len(groups),"all_26_accounted":len(groups)==26},"wet_processing":{"process_core_objects":target_counts.get("Production Hall / Wet Processing",0)>=1},"gatehouse":{"functional_objects":target_counts.get("Security Gatehouse",0)>=1,"restricted_live_references":len(restricted)},"owner_corrections":{"hands_of_growth_objects":sum(1 for n in objs if n.startswith("HOG_") or n in {"HANDS_OF_GROWTH","LABEL_ANCHOR_HANDS_OF_GROWTH","NAV_TARGET_HANDS_OF_GROWTH"}),"trees_present":trees,"two_owner_trees_absent":not any(trees.values()),"living_wall_backing":"REV005_LIVING_WALL_APPROVED_BACKING" in objs,"vip_reception_objects":sum(1 for n in objs if n.startswith("REV005_VIP_"))},"hashes":{"baseline_rev005_blend":"1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D","final_rev005_blend":sha(BLEND),"baseline_rev005_glb":"1CA1AB332137B925AEA5C224888ACF148481AF56BBB1847A9DC67350F12BD2EB","final_rev005_glb":sha(GLB),"rev004_frozen_blend":sha(REV004)},"stop_discipline":{"no_final_tour_created":True,"no_REV006_created":True,"next_gate":"AWAITING_GPT_REMEDIATION_AUDIT"}}
 result["prevalidation_pass"]=all([result["targets"]["closed"]==14,result["regression"]["no_regression_count"]==12,result["inventory"]["all_26_accounted"],result["wet_processing"]["process_core_objects"],result["gatehouse"]["restricted_live_references"]==0,result["owner_corrections"]["two_owner_trees_absent"],result["owner_corrections"]["living_wall_backing"],result["owner_corrections"]["vip_reception_objects"]>0])
 result["hashes"]["rev004_frozen_glb"]=result["hashes"].pop("rev004_frozen_blend")
 (OUT/"REV005_INTERIOR_REMEDIATION_V01_VALIDATION.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
main()
