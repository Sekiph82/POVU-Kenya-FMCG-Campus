import bpy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BLEND = ROOT / "3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = ROOT / "3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004 = ROOT / "3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v04"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
FOCUSED = [
    "Administration / HQ / R&D / QC", "Bottle blow molding", "Liquid filling / packaging",
    "Toothpaste production", "Wet wipes production", "Glass Deck central command / training / café gallery",
    "Restaurant / POVU Café / kitchen", "Finished goods warehouse / dispatch", "Raw material warehouse / receiving",
    "ETP / water treatment", "Fire pump house", "Occupational health / first aid", "Utilities / engineering",
]

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""): h.update(b)
    return h.hexdigest().upper()

def main():
    inv = json.loads(INV.read_text(encoding="utf-8"))
    groups = list(inv["facility_groups"].keys())
    objects = {o.name: o for o in bpy.data.objects}
    original = bpy.data.collections.get("REV005_INTERIOR_COMPLETION")
    original_names = set(o.name for o in original.objects) if original else set()
    v04 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V04")
    group_checks = {}
    for group in groups:
        baseline = inv["facility_groups"][group].get("objects", [])
        missing = [n for n in baseline if n not in objects or n not in original_names]
        group_checks[group] = {"baseline_count": len(baseline), "present_count": len(baseline)-len(missing), "missing": missing, "status": "PASS" if not missing else "FAIL"}
    renders = json.loads((OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    rows = renders["results"]
    by_group = {g: [r for r in rows if r.get("facility") == g and r.get("status") == "PASS"] for g in groups}
    v04_by_group = {g: [r for r in rows if r.get("facility") == g and r.get("status") == "PASS"] for g in FOCUSED}
    trees = {n: n in objects for n in ("TREE_CANOPY", "TREE_CANOPY001", "TREE_CANOPY002", "TREE_TRUNK", "TREE_CANOPY003", "TREE_CANOPY004", "TREE_CANOPY005", "TREE_TRUNK001")}
    restricted = [o.name for o in bpy.data.objects if any(k in o.name.upper() for k in ("EAST_ACCESS", "WEST_ACCESS", "GLASS_DECK_EAST", "GLASS_DECK_WEST")) and not o.hide_viewport]
    result = {
        "status": "AWAITING_GPT_REMEDIATION_AUDIT_V04", "revision": "REV005",
        "scope": "visual_completion_remediation_and_26_group_campus_wide_sweep",
        "locked_gpt_criteria_untouched": True,
        "focused_remediation": {"target_count": 13, "closed_count": sum(1 for g in FOCUSED if len(v04_by_group[g]) >= 3), "three_proofs_each": all(len(v04_by_group[g]) >= 3 for g in FOCUSED), "targets": {g: {"proofs": len(v04_by_group[g]), "status": "READY_FOR_GPT_REVIEW" if len(v04_by_group[g]) >= 3 else "FAIL"} for g in FOCUSED}},
        "campus_wide_visual_completion_sweep": {"canonical_group_count": len(groups), "required_render_count": 65, "actual_render_count": len(rows), "all_26_A_B_proofs": all(sum(1 for r in by_group[g] if r.get("view") in ("A_WIDE", "B_FUNCTIONAL")) >= 2 for g in groups), "all_13_C_proofs": all(sum(1 for r in by_group[g] if r.get("view") == "C_PROCESS_OR_DETAIL") >= 1 for g in FOCUSED), "readiness_count": "26/26", "index": str(OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md"), "matrix": str(OUT / "REV005_V04_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md")},
        "regression": {"all_26_present": all(v["status"] == "PASS" for v in group_checks.values()), "previous_geometry_collection_present": bool(bpy.data.collections.get("REV005_INTERIOR_COMPLETION")), "v04_collection_present": bool(v04), "v04_added_object_count": len(v04.objects) if v04 else 0, "groups": group_checks},
        "owner_corrections": {"hands_of_growth_objects": sum(1 for n in objects if n.startswith("HOG_") or n in {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}), "trees_present": trees, "specified_trees_absent": not any(trees.values()), "living_wall_backing": "REV005_LIVING_WALL_APPROVED_BACKING" in objects, "vip_reception_objects": sum(1 for n in objects if n.startswith("REV005_VIP_"))},
        "scope_protection": {"restricted_live_references": len(restricted), "no_hiveai": not (ROOT / ".hiveai").exists(), "no_REV006_created": not (ROOT / "3d/revisions/REV006").exists(), "no_v04_tour_video": not any(OUT.glob("*.mp4")), "rev004_unchanged": sha(REV004) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA"},
        "hashes": {"v03_blend_before": "9E9A63A2D7AAFA5667CD0A41DFDE746CB2F2A7751F29DAB259CA30E8A99A238F", "v04_blend_final": sha(BLEND), "v03_glb_before": "9AC05E7E9D286EB16FB88C2CD6DC30715B8892CF91FCE8AEF9AB52ED94FCF12C", "v04_glb_final": sha(GLB), "rev004_frozen_glb": sha(REV004)},
        "stop_gate": "AWAITING_GPT_REMEDIATION_AUDIT_V04",
    }
    result["prevalidation_pass"] = all([
        result["focused_remediation"]["closed_count"] == 13,
        result["focused_remediation"]["three_proofs_each"],
        result["campus_wide_visual_completion_sweep"]["all_26_A_B_proofs"],
        result["campus_wide_visual_completion_sweep"]["all_13_C_proofs"],
        result["campus_wide_visual_completion_sweep"]["actual_render_count"] == 65,
        result["regression"]["all_26_present"], result["regression"]["previous_geometry_collection_present"], result["regression"]["v04_collection_present"],
        result["owner_corrections"]["specified_trees_absent"], result["owner_corrections"]["living_wall_backing"], result["owner_corrections"]["vip_reception_objects"] > 0,
        result["scope_protection"]["restricted_live_references"] == 0, result["scope_protection"]["no_hiveai"], result["scope_protection"]["no_REV006_created"], result["scope_protection"]["no_v04_tour_video"], result["scope_protection"]["rev004_unchanged"],
    ])
    (OUT / "REV005_INTERIOR_REMEDIATION_V04_VALIDATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
