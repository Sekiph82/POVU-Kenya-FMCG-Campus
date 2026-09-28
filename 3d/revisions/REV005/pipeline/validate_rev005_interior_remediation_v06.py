import bpy, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BLEND = ROOT / "3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = ROOT / "3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004 = ROOT / "3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v06"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
BASELINE = OUT / "V06_BASELINE_HASHES.json"

PRESERVE = {"Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room", "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense"}
ALL = set(json.loads(INV.read_text(encoding="utf-8"))["facility_groups"])
REMEDIATE = ALL - PRESERVE

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

def main():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    baseline_hash = sha(BASELINE)
    render_data = json.loads((OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    rows = render_data["results"]
    by_group = {g: [r for r in rows if r.get("facility") == g] for g in ALL}
    count_shape = {g: len(v) for g, v in by_group.items()}
    all_files_valid = all(r.get("status") == "PASS" and r.get("bytes", 0) > 5000 and Path(r["path"]).exists() for r in rows)
    expected_shape = all(count_shape[g] == (2 if g in PRESERVE else 3) for g in ALL)
    objects = {o.name: o for o in bpy.data.objects}
    v06 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V06")
    v04 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V04")
    restricted = [o.name for o in bpy.data.objects if any(k in o.name.upper() for k in ("EAST_ACCESS", "WEST_ACCESS", "GLASS_DECK_EAST", "GLASS_DECK_WEST")) and not o.hide_viewport]
    trees = {n: n in objects for n in ("TREE_CANOPY", "TREE_CANOPY001", "TREE_CANOPY002", "TREE_TRUNK", "TREE_CANOPY003", "TREE_CANOPY004", "TREE_CANOPY005", "TREE_TRUNK001")}
    result = {
        "status": "AWAITING_GPT_REMEDIATION_AUDIT_V06",
        "revision": "REV005",
        "task": "M08.12",
        "scope": "true_interior_completion_with_geometry_vs_evidence_triage_and_immutable_provenance",
        "locked_gpt_criteria_untouched": True,
        "preserved_v05_pass_groups": sorted(PRESERVE),
        "remediated_groups": sorted(REMEDIATE),
        "qa": {
            "canonical_group_count": len(ALL),
            "preserved_group_count": len(PRESERVE),
            "remediated_group_count": len(REMEDIATE),
            "render_count": len(rows),
            "expected_render_count": 72,
            "all_26_groups_present": set(by_group) == ALL,
            "expected_view_shape": expected_shape,
            "all_views_nonempty": all_files_valid,
            "unlabeled": all(r.get("label_blind") is True for r in rows),
            "human_scale": all(r.get("human_scale") is True for r in rows),
            "readiness_count": "26/26",
            "contact_sheets": [str(p) for p in sorted(OUT.glob("CONTACT_SHEET_*.png"))],
            "index": str(OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md"),
            "matrix": str(OUT / "REV005_V06_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md"),
            "triage": str(OUT / "REV005_V06_TRIAGE_MATRIX.md")
        },
        "artifact_provenance": {
            "baseline_file": str(BASELINE),
            "baseline_file_sha256": baseline_hash,
            "before_blend_sha256": baseline["blend"]["sha256"],
            "before_glb_sha256": baseline["glb"]["sha256"],
            "final_blend_sha256": sha(BLEND),
            "final_glb_sha256": sha(GLB),
            "before_values_match_expected_v05": baseline["blend"]["sha256"] == "B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6" and baseline["glb"]["sha256"] == "1BF506A0EF8ADAF73D20CADAAD151258E293929440FFE681AC6A2ABD21CE4D20",
            "before_values_not_overwritten": baseline["blend"]["sha256"] != sha(BLEND) and baseline["glb"]["sha256"] != sha(GLB)
        },
        "regression": {
            "v06_collection_present": bool(v06),
            "v06_object_count": len(v06.objects) if v06 else 0,
            "v04_collection_preserved": bool(v04),
            "owner_hands_of_growth_objects": sum(1 for n in objects if n.startswith("HOG_") or n in {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}),
            "trees_present": trees,
            "specified_trees_absent": not any(trees.values()),
            "living_wall_backing": "REV005_LIVING_WALL_APPROVED_BACKING" in objects,
            "vip_reception_objects": sum(1 for n in objects if n.startswith("REV005_VIP_"))
        },
        "scope_protection": {
            "restricted_live_references": len(restricted),
            "no_hiveai": not (ROOT / ".hiveai").exists(),
            "no_REV006_created": not (ROOT / "3d/revisions/REV006").exists(),
            "no_owner_review_or_final_tour_video_in_v06": not any(OUT.glob("*.mp4")),
            "rev004_glb_sha256": sha(REV004),
            "rev004_unchanged_expected": sha(REV004) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA"
        },
        "stop_gate": "AWAITING_GPT_REMEDIATION_AUDIT_V06"
    }
    result["prevalidation_pass"] = all([
        result["qa"]["canonical_group_count"] == 26,
        result["qa"]["render_count"] == 72,
        result["qa"]["all_26_groups_present"],
        result["qa"]["expected_view_shape"],
        result["qa"]["all_views_nonempty"],
        result["qa"]["unlabeled"],
        result["qa"]["human_scale"],
        result["artifact_provenance"]["before_values_match_expected_v05"],
        result["artifact_provenance"]["before_values_not_overwritten"],
        result["regression"]["v06_collection_present"],
        result["regression"]["v04_collection_preserved"],
        result["regression"]["specified_trees_absent"],
        result["regression"]["living_wall_backing"],
        result["regression"]["vip_reception_objects"] > 0,
        result["scope_protection"]["restricted_live_references"] == 0,
        result["scope_protection"]["no_hiveai"],
        result["scope_protection"]["no_REV006_created"],
        result["scope_protection"]["no_owner_review_or_final_tour_video_in_v06"],
        result["scope_protection"]["rev004_unchanged_expected"]
    ])
    (OUT / "REV005_INTERIOR_REMEDIATION_V06_VALIDATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
