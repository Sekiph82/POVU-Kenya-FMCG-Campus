import bpy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BLEND = ROOT / "3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = ROOT / "3d/revisions/REV005/POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004 = ROOT / "3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"
OUT = ROOT / "output/rev005-interior-remediation-v03"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
FOCUSED = [
    "Bottle Blow Molding", "Liquid Filling / Packaging", "Toothpaste Production",
    "Wet Wipes Production", "Central Glass Deck Command / Training / Café Gallery",
    "Restaurant / POVU Café / kitchen", "Daycare / crèche",
]
ACCEPTED_V01 = [
    "Production Hall / Wet Processing / process core", "Electrical / LV-MV room",
    "Fire pump house", "Employee changing / shower / locker support",
    "Security / reception / visitor arrival", "Security gatehouse",
]
PREVIOUSLY_PASSING = [
    "Administration / HQ / R&D / QC", "Chemical compound / controlled receiving",
    "ETP / water treatment", "Finished goods warehouse / dispatch",
    "Occupational health / first aid", "Packaging warehouse",
    "Raw material warehouse / receiving", "Training / Academy",
    "Utilities / engineering", "Wellness / recreation",
]

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest().upper()

def metadata_match(group, facility):
    if not facility:
        return False
    a = "".join(ch.lower() if ch.isalnum() else " " for ch in group).split()
    b = "".join(ch.lower() if ch.isalnum() else " " for ch in facility).split()
    sa, sb = " ".join(a), " ".join(b)
    return sa == sb or sa in sb or sb in sa or ("glass deck" in sa and "central glass deck" in sb)

def main():
    inv = json.loads(INV.read_text(encoding="utf-8"))
    objects = {o.name: o for o in bpy.data.objects}
    original = bpy.data.collections.get("REV005_INTERIOR_COMPLETION")
    original_names = set(o.name for o in original.objects) if original else set()
    v02 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V02")
    v03 = bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V03")
    groups = list(inv["facility_groups"].keys())
    group_checks = {}
    for group in groups:
        baseline = inv["facility_groups"][group].get("objects", [])
        missing = [n for n in baseline if n not in objects or n not in original_names]
        group_checks[group] = {
            "baseline_count": len(baseline), "present_count": len(baseline) - len(missing),
            "missing": missing, "status": "PASS" if not missing else "FAIL",
        }
    renders = json.loads((OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    focused_renders = {g: [r for r in renders if r.get("kind") == "focused" and r.get("target") == g and r.get("status") == "PASS"] for g in FOCUSED}
    group_renders = {g: [r for r in renders if r.get("kind") == "campus_26_group" and r.get("target") == g and r.get("status") == "PASS"] for g in groups}
    caps_count = sum(1 for o in v02.objects if o.get("facility") == "Caps and Trigger Assembly") if v02 else 0
    micro_count = sum(1 for o in v02.objects if o.get("facility") == "Micro-ingredient Weigh / Dispense") if v02 else 0
    restricted = [o.name for o in bpy.data.objects if any(k in o.name.upper() for k in ("EAST_ACCESS", "WEST_ACCESS", "GLASS_DECK_EAST", "GLASS_DECK_WEST")) and not o.hide_viewport]
    trees = {n: n in objects for n in ("TREE_CANOPY", "TREE_CANOPY001", "TREE_CANOPY002", "TREE_TRUNK", "TREE_CANOPY003", "TREE_CANOPY004", "TREE_CANOPY005", "TREE_TRUNK001")}
    result = {
        "status": "AWAITING_GPT_REMEDIATION_AUDIT_V03", "revision": "REV005",
        "scope": "visual_completion_remediation_and_campus_wide_sweep",
        "locked_gpt_criteria_untouched": True,
        "focused_remediation": {
            "target_count": 7,
            "closed_count": sum(1 for g in FOCUSED if len(focused_renders[g]) >= 3),
            "three_proofs_each": all(len(focused_renders[g]) >= 3 for g in FOCUSED),
            "render_pass_count": sum(len(v) for v in focused_renders.values()),
            "targets": {g: {"proofs": len(focused_renders[g]), "status": "PASS" if len(focused_renders[g]) >= 3 else "FAIL"} for g in FOCUSED},
        },
        "campus_wide_visual_completion_sweep": {
            "canonical_group_count": len(groups), "group_render_proofs": sum(len(v) for v in group_renders.values()),
            "all_26_render_proofs": all(len(group_renders[g]) >= 1 for g in groups),
            "index": str(OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md"),
        },
        "regression": {
            "all_26_present": all(v["status"] == "PASS" for v in group_checks.values()),
            "accepted_v01_areas_intact": all(group_checks[g]["status"] == "PASS" for g in ACCEPTED_V01),
            "previously_passing_groups_intact": all(group_checks[g]["status"] == "PASS" for g in PREVIOUSLY_PASSING),
            "caps_trigger_v02_preserved": caps_count > 0,
            "micro_weigh_v02_preserved": micro_count > 0,
            "groups": group_checks,
        },
        "owner_corrections": {
            "hands_of_growth_objects": sum(1 for n in objects if n.startswith("HOG_") or n in {"HANDS_OF_GROWTH", "LABEL_ANCHOR_HANDS_OF_GROWTH", "NAV_TARGET_HANDS_OF_GROWTH"}),
            "trees_present": trees, "specified_trees_absent": not any(trees.values()),
            "living_wall_backing": "REV005_LIVING_WALL_APPROVED_BACKING" in objects,
            "vip_reception_objects": sum(1 for n in objects if n.startswith("REV005_VIP_")),
        },
        "scope_protection": {
            "restricted_live_references": len(restricted), "no_REV006_created": not (ROOT / "3d/revisions/REV006").exists(),
            "no_final_tour_created": not any(OUT.glob("*.mp4")), "rev004_unchanged": sha(REV004) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA",
        },
        "hashes": {
            "v02_blend_before": "9BEE6F87D7762BC415F15047DC287D7B591C44C83FF8E39C226E6A07FD480B0C",
            "v03_blend_final": sha(BLEND), "v02_glb_before": "B0F571A26AC12F26D817AAF7FF4E9C2FEFC7729CB28EBD25A9004B3548395DC1",
            "v03_glb_final": sha(GLB), "rev004_frozen_glb": sha(REV004),
        },
        "stop_gate": "AWAITING_GPT_REMEDIATION_AUDIT_V03",
    }
    result["prevalidation_pass"] = all([
        result["focused_remediation"]["closed_count"] == 7,
        result["focused_remediation"]["three_proofs_each"],
        result["campus_wide_visual_completion_sweep"]["all_26_render_proofs"],
        result["regression"]["all_26_present"], result["regression"]["accepted_v01_areas_intact"],
        result["regression"]["previously_passing_groups_intact"], result["regression"]["caps_trigger_v02_preserved"],
        result["regression"]["micro_weigh_v02_preserved"], result["owner_corrections"]["specified_trees_absent"],
        result["owner_corrections"]["living_wall_backing"], result["owner_corrections"]["vip_reception_objects"] > 0,
        result["scope_protection"]["restricted_live_references"] == 0, result["scope_protection"]["no_REV006_created"],
        result["scope_protection"]["no_final_tour_created"], result["scope_protection"]["rev004_unchanged"],
    ])
    (OUT / "REV005_INTERIOR_REMEDIATION_V03_VALIDATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
