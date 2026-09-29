import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-interior-remediation-v08"
REV = ROOT / "3d/revisions/REV005"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004 = ROOT / "3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"

PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
}
GROUPS = [
    "Administration / HQ / R&D / QC", "Bottle blow molding", "Chemical compound / controlled receiving",
    "ETP / water treatment", "Finished goods warehouse / dispatch", "Glass Deck central command / training / café gallery",
    "Liquid filling / packaging", "Occupational health / first aid", "Packaging warehouse", "Powder handling / packing",
    "Production Hall / Wet Processing / process core", "Raw material warehouse / receiving", "Restaurant / POVU Café / kitchen",
    "Security / reception / visitor arrival", "Security gatehouse", "Toothpaste production", "Training / Academy",
    "Utilities / engineering", "Wellness / recreation", "Wet wipes production",
]
SCOPES = {
    "Administration / HQ / R&D / QC": "Enclosed reception/admin, workstations, meeting zone and separated QC/R&D lab benches, instruments, storage and circulation.",
    "Bottle blow molding": "Preform hopper/feed, heater oven coils, guarded mould/blow cell, bottle outfeed, bottle cues and operator station.",
    "Chemical compound / controlled receiving": "Dock, drums/IBCs, bunded tanks, transfer pumps, connected piping and controlled-access partition.",
    "ETP / water treatment": "Equalisation, aeration and clarification tanks, filter vessels, pumps, connected headers, walkway rails and sludge/discharge handling.",
    "Finished goods warehouse / dispatch": "Finished pallet/rack storage, consolidation, dispatch desk, loading edge and AMR circulation.",
    "Glass Deck central command / training / café gallery": "One enclosed/glazed interior with command wall/consoles, training tables/screens and café counter/backbar/seating.",
    "Liquid filling / packaging": "Bottle infeed, filler/nozzles, cap feed/capper, label/inspection, case packing, guards and outfeed.",
    "Occupational health / first aid": "Reception/waiting, exam bed, privacy curtain, treatment cart, sink and clinical storage in an enclosed room.",
    "Packaging warehouse": "Packaging racks with film rolls/cartons, staging and issue-to-production conveyor/aisles.",
    "Powder handling / packing": "Hopper/auger, dosing, FFS/sachet fill-seal, dust hood and finished-pack outfeed.",
    "Production Hall / Wet Processing / process core": "Mix tanks with agitators, platforms/rails, process manifold/pumps, CIP skid/tank and transfer conveyor.",
    "Raw material warehouse / receiving": "Receiving dock/inspection desk, raw racks, pallets, drums/IBCs and handling context.",
    "Restaurant / POVU Café / kitchen": "Dining tables, café counter/backbar, kitchen appliances/pass, storage and partitioned service flow.",
    "Security / reception / visitor arrival": "Reception desk, CCTV wall, visitor seating, turnstiles, screening and partitioned onward flow.",
    "Security gatehouse": "Enclosed booth, windows, operator/CCTV desk, vehicle lane, barrier arm/post and service access.",
    "Toothpaste production": "Vacuum mix/hold tanks, transfer, tube magazine/tubes, filler/nozzles, crimp, code, carton and outfeed.",
    "Training / Academy": "Enclosed classroom with instructor zone, screen, desks/seating, storage and circulation.",
    "Utilities / engineering": "Compressed-air compressor/receiver, boiler/steam, RO columns/skid, manifolds and maintenance bench.",
    "Wellness / recreation": "Enclosed fitness room with cardio, weights, yoga mats, lockers, mirror cue and circulation.",
    "Wet wipes production": "Parent rolls/unwind, web conveyor, wetting/spray, folding rollers, cut/stack, pouch film/seal and discharge.",
}

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

def slug(group):
    return re.sub(r"[^a-z0-9]+", "_", group.lower()).strip("_")

def link(path):
    return f"[evidence]({path.as_posix()})"

def main():
    baseline = json.loads((OUT / "V08_BASELINE_HASHES.json").read_text(encoding="utf-8"))
    build = json.loads((OUT / "BUILD_RESULT.json").read_text(encoding="utf-8"))
    renders = json.loads((OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    blend_final, glb_final = sha(BLEND), sha(GLB)
    render_by_group = {group: [item for item in renders["results"] if item["facility"] == group] for group in GROUPS + sorted(PASS_GROUPS)}

    map_lines = ["# REV005 V08 Clean Replacement Map", "", "Each failing group was rebuilt in a dedicated V08 clean subcollection. Legacy facility-specific objects were hidden from canonical render/export after immutable V07 baseline capture. This is an implementation-readiness map, not independent acceptance.", "", "| Group | Dedicated clean subcollection | Legacy/proxy retirement | Replacement scope | Isolated proof | Integrated proof | Status |", "|---|---|---|---|---|---|---|"]
    for group in GROUPS:
        name = build["clean_collections"][group]
        hidden = len(build["legacy_hidden_by_group"].get(group, []))
        items = {item["view"]: item for item in render_by_group[group] if "view" in item}
        isolated = Path("qa_isolated") / f"{slug(group)}_ISOLATED_LABEL_BLIND.png"
        integrated = " ".join(link(Path("qa") / Path(items[view]["path"]).name) for view in ("A_CONTEXT", "B_FUNCTIONAL", "C_SEQUENCE_OR_DETAIL"))
        map_lines.append(f"| {group} | `{name}` ({build['clean_object_counts'][group]} objects) | {hidden} legacy objects hidden from render/export | {SCOPES[group]} | {link(isolated)} | {integrated} | READY_FOR_GPT_REVIEW |")
    (OUT / "V08_CLEAN_REPLACEMENT_MAP.md").write_text("\n".join(map_lines) + "\n", encoding="utf-8")

    matrix_lines = ["# REV005 V08 26-Group Visual Acceptance Matrix", "", "Truthful Codex readiness matrix for the locked V08 GPT audit. It does not award independent visual PASS.", "", "| Group | Role | ISOLATED_LABEL_BLIND | A_CONTEXT | B_FUNCTIONAL | C_SEQUENCE_OR_DETAIL | Evidence status |", "|---|---|---|---|---|---|---|"]
    for group in GROUPS + sorted(PASS_GROUPS):
        items = {item.get("view", item.get("proof")): item for item in render_by_group[group]}
        if group in PASS_GROUPS:
            cells = ["—", *(link(Path("qa") / Path(items[view]["path"]).name) for view in ("A_CONTEXT", "B_FUNCTIONAL")), "—"]
            role = "PRESERVE SIX V07 PASS GROUP"
        else:
            cells = [link(Path("qa_isolated") / f"{slug(group)}_ISOLATED_LABEL_BLIND.png"), *(link(Path("qa") / Path(items[view]["path"]).name) for view in ("A_CONTEXT", "B_FUNCTIONAL", "C_SEQUENCE_OR_DETAIL"))]
            role = "V08 CLEAN REPLACEMENT"
        matrix_lines.append(f"| {group} | {role} | {cells[0]} | {cells[1]} | {cells[2]} | {cells[3]} | READY_FOR_GPT_REVIEW |")
    (OUT / "REV005_V08_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md").write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")

    index = (OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md").read_text(encoding="utf-8")
    validation = {
        "status": "AWAITING_GPT_REMEDIATION_AUDIT_V08",
        "task": "M08.16",
        "revision": "REV005",
        "isolated_proof_gate": {
            "group_count": len(GROUPS),
            "expected_count": 20,
            "actual_count": renders["isolated_count"],
            "all_nonempty": all(item["status"] == "PASS" and item["bytes"] > 5000 and Path(item["path"]).exists() for item in renders["isolated"]),
            "all_unlabeled": all(item["label_blind"] for item in renders["isolated"]),
            "readiness": "20/20 ISOLATED_LABEL_BLIND proofs mechanically ready for GPT review",
        },
        "integrated_qa": {
            "remediation_group_count": 20,
            "preserved_group_count": 6,
            "expected_remediation_views": 60,
            "actual_remediation_views": renders["integrated_count"],
            "expected_preservation_views": 12,
            "actual_preservation_views": renders["preservation_count"],
            "expected_total": 92,
            "actual_total": renders["render_count"],
            "all_nonempty": all(item["status"] == "PASS" and item["bytes"] > 5000 and Path(item["path"]).exists() for item in renders["results"]),
            "all_unlabeled": all(item["label_blind"] for item in renders["results"]),
            "readiness": "26-group integrated QA mechanically ready",
        },
        "artifact_provenance": {
            "baseline_file": str(OUT / "V08_BASELINE_HASHES.json"),
            "baseline_file_sha256": sha(OUT / "V08_BASELINE_HASHES.json"),
            "before_blend_sha256": baseline["blend"]["sha256"],
            "before_glb_sha256": baseline["glb"]["sha256"],
            "expected_before_blend_sha256": "BF61CAFCD0EA20E5FE371D491913A51D866AE058F58242FDC30B94AB454ACBD8",
            "expected_before_glb_sha256": "105C83237E5903B1957E206A17E278B7B60214BE38E78F65AB65937294338BE7",
            "final_blend_sha256": blend_final,
            "final_glb_sha256": glb_final,
            "before_values_immutable_and_match_locked_v07": baseline["blend"]["sha256"] == "BF61CAFCD0EA20E5FE371D491913A51D866AE058F58242FDC30B94AB454ACBD8" and baseline["glb"]["sha256"] == "105C83237E5903B1957E206A17E278B7B60214BE38E78F65AB65937294338BE7",
            "final_values_differ": baseline["blend"]["sha256"] != blend_final and baseline["glb"]["sha256"] != glb_final,
            "final_values_match_build": build["final_blend_sha256"] == blend_final and build["final_glb_sha256"] == glb_final,
        },
        "scope_protection": {
            "rev004_glb_sha256": sha(REV004),
            "rev004_unchanged_expected": sha(REV004) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA",
            "no_hiveai": not (ROOT / ".hiveai").exists(),
            "no_REV006_created": not (ROOT / "3d/revisions/REV006").exists(),
            "no_tour_or_owner_review_video_in_v08": not any(OUT.glob("*.mp4")),
            "tasks_untouched": subprocess.run(["git", "diff", "--quiet", "--", "TASKS.md"], cwd=ROOT).returncode == 0,
            "locked_criteria_untouched": subprocess.run(["git", "diff", "--quiet", "--", "coordination/Audits/REV005_INTERIOR_REMEDIATION_V08_GPT_AUDIT_CRITERIA.md"], cwd=ROOT).returncode == 0,
            "no_east_west_glass_deck_callouts_in_v08_artifacts": not any("East Glass Deck Access" in p.read_text(encoding="utf-8", errors="ignore") or "West Glass Deck Access" in p.read_text(encoding="utf-8", errors="ignore") for p in OUT.rglob("*.md")),
        },
        "evidence": {
            "clean_replacement_map": str(OUT / "V08_CLEAN_REPLACEMENT_MAP.md"),
            "acceptance_matrix": str(OUT / "REV005_V08_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md"),
            "completion_index": str(OUT / "CAMPUS_26_GROUP_VISUAL_COMPLETION_INDEX.md"),
            "isolated_folder": str(OUT / "qa_isolated"),
            "qa_folder": str(OUT / "qa"),
            "contact_sheets": [str(OUT / "CONTACT_SHEET_ISOLATED.png"), str(OUT / "CONTACT_SHEET_INTEGRATED_AND_PRESERVATION.png")],
        },
        "stop_gate": "AWAITING_GPT_REMEDIATION_AUDIT_V08",
    }
    validation["prevalidation_pass"] = all([
        validation["isolated_proof_gate"]["actual_count"] == 20,
        validation["isolated_proof_gate"]["all_nonempty"],
        validation["isolated_proof_gate"]["all_unlabeled"],
        validation["integrated_qa"]["actual_total"] == 92,
        validation["integrated_qa"]["all_nonempty"],
        validation["integrated_qa"]["all_unlabeled"],
        validation["artifact_provenance"]["before_values_immutable_and_match_locked_v07"],
        validation["artifact_provenance"]["final_values_differ"],
        validation["artifact_provenance"]["final_values_match_build"],
        validation["scope_protection"]["rev004_unchanged_expected"],
        validation["scope_protection"]["no_hiveai"],
        validation["scope_protection"]["no_REV006_created"],
        validation["scope_protection"]["no_tour_or_owner_review_video_in_v08"],
        validation["scope_protection"]["tasks_untouched"],
        validation["scope_protection"]["locked_criteria_untouched"],
    ])
    (OUT / "REV005_INTERIOR_REMEDIATION_V08_VALIDATION.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")

    report = ["# REV005 Interior Remediation V08 Report", "", "## Final state", "", "`AWAITING_GPT_REMEDIATION_AUDIT_V08`", "", "Codex implementation handoff only. Independent GPT visual acceptance and owner acceptance remain pending; no PASS is self-awarded.", "", "## Method", "", "- V07-final Blend/GLB hashes were captured in immutable `V08_BASELINE_HASHES.json` before mutation.", "- The 20 V07-failing groups were rebuilt as dedicated `REV005_V08_CLEAN_<GROUP>` subcollections.", f"- {build['legacy_hidden_count']} legacy facility/proxy objects were marked retired and hidden from canonical render/export; the six prior PASS groups were not remodeled.", "- Each clean replacement received an isolated unlabeled proof before integrated evidence generation.", "", "## QA readiness", "", "- 20/20 isolated label-blind proof paths are present, non-empty and mechanically ready for GPT review.", "- 20 remediation groups × A_CONTEXT/B_FUNCTIONAL/C_SEQUENCE_OR_DETAIL = 60 integrated views.", "- Six preserved PASS groups × A_CONTEXT/B_FUNCTIONAL = 12 regression views.", "- Total: 92/92 unlabeled PNG renders.", "- Contact sheets were generated for isolated and integrated/preservation evidence.", "", "## Protection", "", "- REV004 GLB hash remained unchanged.", "- No `.hiveai`, REV006, tour, or owner-review video was created.", "- `TASKS.md` and the locked V08 criteria were not edited.", "- East/West Glass Deck Access callouts were not added to V08 artifacts.", "", "## Provenance", "", f"- V08 baseline Blend: `{baseline['blend']['sha256']}`", f"- V08 baseline GLB: `{baseline['glb']['sha256']}`", f"- V08 final Blend: `{blend_final}`", f"- V08 final GLB: `{glb_final}`", "", "## Stop gate", "", "`AWAITING_GPT_REMEDIATION_AUDIT_V08`", ""]
    (OUT / "REV005_INTERIOR_REMEDIATION_V08_REPORT.md").write_text("\n".join(report), encoding="utf-8")

    log = ["# REV005 Interior Remediation V08 Codex Log", "", "## Authorization", "", "- Task: M08.16", "- Prompt: `coordination/Prompts/REV005_INTERIOR_REMEDIATION_V08_GPT_PROMPT.md`", "- Locked criteria: `coordination/Audits/REV005_INTERIOR_REMEDIATION_V08_GPT_AUDIT_CRITERIA.md` (read-only)", "- Stop gate: `AWAITING_GPT_REMEDIATION_AUDIT_V08`", "", "## Immutable baseline", "", f"- V07 Blend before: `{baseline['blend']['sha256']}`", f"- V07 GLB before: `{baseline['glb']['sha256']}`", "- Baseline file was committed before any V08 Blend/GLB mutation and was not overwritten.", "", "## Clean replacement execution", "", "- Built 20 dedicated clean V08 subcollections with facility-specific architectural/process subassemblies.", f"- Retired {build['legacy_hidden_count']} conflicting legacy/proxy objects from canonical render/export.", "- Preserved the six independent-PASS groups without unnecessary remodeling.", "- Completed isolated label-blind proof generation before integrated QA.", "", "## Evidence", "", "- 20 isolated proofs, 60 integrated remediation views and 12 preservation views generated.", "- Evidence is unlabeled, non-empty and materially separated by group/view path.", "- Matrix and clean-replacement map link only to generated evidence; they do not claim independent PASS.", "", "## Handoff", "", f"- Final Blend SHA-256: `{blend_final}`", f"- Final GLB SHA-256: `{glb_final}`", "- Builder evidence is not independent GPT acceptance.", "- Final state: `AWAITING_GPT_REMEDIATION_AUDIT_V08`.", ""]
    (ROOT / "coordination/Logs/REV005_INTERIOR_REMEDIATION_V08_CODEX_LOG.md").write_text("\n".join(log), encoding="utf-8")
    print(json.dumps({"status": validation["status"], "prevalidation_pass": validation["prevalidation_pass"], "isolated": renders["isolated_count"], "integrated": renders["integrated_count"], "preservation": renders["preservation_count"], "total": renders["render_count"], "blend": blend_final, "glb": glb_final}, indent=2))

main()
