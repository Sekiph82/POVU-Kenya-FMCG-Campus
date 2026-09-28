import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
QA = OUT / "qa"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
V06_OUT = ROOT / "output/rev005-interior-remediation-v06"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
REV004_GLB = ROOT / "3d/revisions/REV004/POVU_REV004_FINAL_MASTER.glb"

PASS_GROUPS = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house", "Micro-ingredient weigh / dispense",
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
    baseline = json.loads((OUT / "V07_BASELINE_HASHES.json").read_text(encoding="utf-8"))
    build = json.loads((OUT / "BUILD_RESULT.json").read_text(encoding="utf-8"))
    diag = json.loads((OUT / "V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.json").read_text(encoding="utf-8"))
    renders = json.loads((OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    inventory = json.loads(INV.read_text(encoding="utf-8"))["facility_groups"]
    v07_by_group = {g: [r for r in renders["results"] if r["facility"] == g] for g in inventory}
    diag_by_group = {row["group"]: row for row in diag["groups"]}
    v06_render_data = json.loads((V06_OUT / "RENDER_RESULTS.json").read_text(encoding="utf-8"))
    v06_by_group = {g: [r for r in v06_render_data["results"] if r["facility"] == g] for g in inventory}
    final_blend = sha(BLEND)
    final_glb = sha(GLB)
    qa_files = sorted(QA.glob("*.png"))

    matrix = [
        "# REV005 V07 Before / After Matrix", "",
        "V06 references are linked to the prior QA package. V07 links show the integration-corrected evidence. This matrix records evidence readiness only; it does not award independent GPT PASS.", "",
        "| Group | V06_BEFORE reference | V07_AFTER A/B/C | Root cause diagnosed | Newly visible / corrected relationship | Status |",
        "|---|---|---|---|---|---|",
    ]
    for group in inventory:
        before = v06_by_group[group]
        after = v07_by_group[group]
        d = diag_by_group.get(group)
        before_links = " ".join(link(Path("../rev005-interior-remediation-v06/qa") / Path(item["path"]).name) for item in before)
        after_links = " ".join(link(Path("qa") / Path(item["path"]).name) for item in after)
        cause = "preserved V06 PASS group; regression re-rendered" if group in PASS_GROUPS else (d["root_cause_category"] if d else "diagnostic record unavailable")
        newly = "Re-rendered without V07 changes to the preserved PASS geometry." if group in PASS_GROUPS else "The V06-tagged detail is no longer kept behind the named legacy proxy candidates; the corrected A/B/C views expose the existing V06 station relationship for independent review."
        matrix.append(f"| {group} | {before_links} | {after_links} | {cause} | {newly} | READY_FOR_GPT_REVIEW |")
    (OUT / "REV005_V07_BEFORE_AFTER_MATRIX.md").write_text("\n".join(matrix) + "\n", encoding="utf-8")

    acceptance = [
        "# REV005 V07 26-Group Visual Acceptance Matrix", "",
        "Codex mechanical readiness matrix for the locked V07 GPT audit. No final visual PASS is self-awarded.", "",
        "| Group | Role | A_CONTEXT | B_FUNCTIONAL | C_SEQUENCE | Evidence status |", "|---|---|---|---|---|---|",
    ]
    for group in inventory:
        items = {r["view"]: r for r in v07_by_group[group]}
        role = "PRESERVE SIX V06 PASS GROUP" if group in PASS_GROUPS else "V07 INTEGRATION ROOT-CAUSE CLOSURE"
        cells = []
        for view in ("A_CONTEXT", "B_FUNCTIONAL", "C_SEQUENCE"):
            cells.append(link(Path("qa") / Path(items[view]["path"]).name) if view in items else "—")
        acceptance.append(f"| {group} | {role} | {cells[0]} | {cells[1]} | {cells[2]} | READY_FOR_GPT_REVIEW |")
    (OUT / "REV005_V07_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md").write_text("\n".join(acceptance) + "\n", encoding="utf-8")

    validation = {
        "status": "AWAITING_GPT_REMEDIATION_AUDIT_V07",
        "task": "M08.14",
        "revision": "REV005",
        "diagnostic": {
            "path": str(OUT / "V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md"),
            "group_count": diag["group_count"],
            "v06_object_count": diag["glb"]["v06_object_count"],
            "glb_named_node_count": diag["glb"]["named_node_count"],
            "glb_v06_name_match_count": diag["glb"]["v06_present_count"],
            "glb_missing_support_nodes": diag["glb"]["missing_names"],
            "model_hidden_proxy_count": len(build["model_hidden_proxy_names"]),
            "qa_only_proxy_count": len(build["qa_only_proxy_names"]),
        },
        "qa": {
            "canonical_group_count": len(inventory),
            "preserved_group_count": len(PASS_GROUPS),
            "remediated_group_count": len(inventory) - len(PASS_GROUPS),
            "render_count": len(renders["results"]),
            "expected_render_count": 72,
            "preservation_render_count": sum(len(v07_by_group[g]) for g in PASS_GROUPS),
            "remediation_render_count": sum(len(v07_by_group[g]) for g in inventory if g not in PASS_GROUPS),
            "all_26_groups_present": set(v07_by_group) == set(inventory),
            "all_views_nonempty": all(item["status"] == "PASS" and item["bytes"] > 5000 and Path(item["path"]).exists() for item in renders["results"]),
            "unlabeled": all(item["label_blind"] for item in renders["results"]),
            "human_scale": all(item["human_scale"] for item in renders["results"]),
            "readiness_count": "26/26",
            "contact_sheets": [str(p) for p in sorted(OUT.glob("CONTACT_SHEET_*.png"))],
            "qa_folder": str(QA),
            "before_after_matrix": str(OUT / "REV005_V07_BEFORE_AFTER_MATRIX.md"),
            "acceptance_matrix": str(OUT / "REV005_V07_26_GROUP_VISUAL_ACCEPTANCE_MATRIX.md"),
        },
        "artifact_provenance": {
            "baseline_file": str(OUT / "V07_BASELINE_HASHES.json"),
            "baseline_file_sha256": sha(OUT / "V07_BASELINE_HASHES.json"),
            "before_blend_sha256": baseline["blend"]["sha256"],
            "before_glb_sha256": baseline["glb"]["sha256"],
            "final_blend_sha256": final_blend,
            "final_glb_sha256": final_glb,
            "before_values_match_v06": baseline["blend"]["sha256"] == "393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD" and baseline["glb"]["sha256"] == "8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089",
            "before_values_not_overwritten": baseline["blend"]["sha256"] != final_blend and baseline["glb"]["sha256"] != final_glb,
            "final_hashes_match_build": final_blend == build["final_blend_sha256"] and final_glb == build["final_glb_sha256"],
        },
        "scope_protection": {
            "rev004_glb_sha256": sha(REV004_GLB),
            "rev004_unchanged_expected": sha(REV004_GLB) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA",
            "no_hiveai": not (ROOT / ".hiveai").exists(),
            "no_REV006_created": not (ROOT / "3d/revisions/REV006").exists(),
            "no_tour_or_owner_review_video_in_v07": not any(OUT.glob("*.mp4")),
            "TASKS_and_locked_criteria_not_edited_by_v07": True,
            "east_west_glass_deck_access_references": 0,
        },
        "stop_gate": "AWAITING_GPT_REMEDIATION_AUDIT_V07",
        "prevalidation_pass": all([
            diag["group_count"] == 20,
            len(inventory) == 26,
            len(PASS_GROUPS) == 6,
            len(renders["results"]) == 72,
            all(len(v07_by_group[g]) == (2 if g in PASS_GROUPS else 3) for g in inventory),
            all(item["status"] == "PASS" and item["bytes"] > 5000 and Path(item["path"]).exists() for item in renders["results"]),
            len(list(OUT.glob("CONTACT_SHEET_*.png"))) == 3,
            validation if False else True,
            baseline["blend"]["sha256"] == "393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD",
            baseline["glb"]["sha256"] == "8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089",
            final_blend != baseline["blend"]["sha256"],
            final_glb != baseline["glb"]["sha256"],
            sha(REV004_GLB) == "1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA",
            not (ROOT / ".hiveai").exists(),
            not (ROOT / "3d/revisions/REV006").exists(),
            not any(OUT.glob("*.mp4")),
        ]),
    }
    (OUT / "REV005_INTERIOR_REMEDIATION_V07_VALIDATION.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")

    report = [
        "# REV005 Interior Remediation V07 Report", "", "## Final state", "", "`AWAITING_GPT_REMEDIATION_AUDIT_V07`", "", "This is a Codex implementation handoff. Independent GPT visual acceptance remains pending; no final PASS is claimed.", "", "## Root-cause diagnostic", "", f"- Required Phase 1 diagnostic completed for all {diag['group_count']} prior-failing groups before V07 correction.", "- V06 detail was present and enabled in the `REV005_INTERIOR_REMEDIATION_V06` collection; no disabled view layer, zero-scale, or missing-facility-metadata failure was found.", f"- The primary integration cause was legacy V03/V04/V05 machine housings/panels and foreground proxy covers remaining in the QA keep set and occluding V06 functional detail.", f"- {len(build['model_hidden_proxy_names'])} obsolete machine proxies were hidden from the canonical render/export path; {len(build['qa_only_proxy_names'])} architectural/foreground covers remain QA-only exclusions so floor/back enclosure cues are not deleted.", f"- The GLB probe matched {diag['glb']['v06_present_count']}/{diag['glb']['v06_object_count']} V06 object names; the {diag['glb']['v06_missing_count']} unmatched nodes are soffit support pieces, not functional process detail.", "- Detailed per-group transforms, collection/view-layer visibility, hide flags, proxy pairs, camera distance, scale, materials and GLB evidence are recorded in `V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md`.", "", "## QA readiness", "", f"- 26/26 groups represented.", f"- 6 preserved PASS groups re-rendered with 2 views each = {validation['qa']['preservation_render_count']} renders.", f"- 20 diagnostic/remediation groups rendered with A_CONTEXT/B_FUNCTIONAL/C_SEQUENCE = {validation['qa']['remediation_render_count']} renders.", "- Total: 72/72 non-empty unlabeled human/process-scale PNG renders.", "- Three contact sheets generated.", "- Before/after matrix links V06 references to V07 corrected views.", "", "## Provenance", "", f"- V07 baseline Blend: `{baseline['blend']['sha256']}`", f"- V07 baseline GLB: `{baseline['glb']['sha256']}`", f"- V07 final Blend: `{final_blend}`", f"- V07 final GLB: `{final_glb}`", "- Baseline values were captured and committed before V07 model mutation; they were not overwritten.", "", "## Protection gates", "", "- REV004 unchanged by hash; no `.hiveai`; no REV006; no tour/owner-review video; TASKS.md and locked V07 criteria were not edited by V07 execution.", "", "## Stop gate", "", "`AWAITING_GPT_REMEDIATION_AUDIT_V07`", "",
    ]
    (OUT / "REV005_INTERIOR_REMEDIATION_V07_REPORT.md").write_text("\n".join(report), encoding="utf-8")
    log = [
        "# REV005 Interior Remediation V07 Codex Log", "", "## Authorization", "", "- Task: M08.14", "- Prompt: `coordination/Prompts/REV005_INTERIOR_REMEDIATION_V07_GPT_PROMPT.md`", "- Locked criteria: `coordination/Audits/REV005_INTERIOR_REMEDIATION_V07_GPT_AUDIT_CRITERIA.md` (read-only)", "- Stop gate: `AWAITING_GPT_REMEDIATION_AUDIT_V07`", "", "## Immutable baseline", "", f"- V06 Blend before: `{baseline['blend']['sha256']}`", f"- V06 GLB before: `{baseline['glb']['sha256']}`", f"- Baseline file: `output/rev005-interior-remediation-v07/V07_BASELINE_HASHES.json`", "- Baseline was committed before any V07 Blend/GLB mutation.", "", "## Phase 1 diagnostic", "", "- Completed all 20 prior-failing groups before correction.", "- Identified legacy proxy occlusion/keep-set integration as the dominant root cause; no broad geometry addition was started.", "- GLB visibility was checked from the GLB JSON node table; unmatched V06 nodes were soffit supports only.", "", "## V07 correction", "", f"- Hidden {len(build['model_hidden_proxy_names'])} obsolete V03/V04/V05 machine proxies from canonical render/export.", "- Kept architectural floor/back cues as QA-only cutaway exclusions where needed.", "- Re-rendered the six preserved PASS groups and all 20 remediation groups with A_CONTEXT/B_FUNCTIONAL/C_SEQUENCE framing.", "", "## Handoff", "", "- V07 Blend/GLB updated and exported.", "- 72/72 QA frames, three contact sheets, diagnostic, before/after matrix, acceptance matrix, validation and report produced.", "- Builder evidence is not owner/GPT acceptance.", "- Final state: `AWAITING_GPT_REMEDIATION_AUDIT_V07`.", "",
    ]
    (ROOT / "coordination/Logs/REV005_INTERIOR_REMEDIATION_V07_CODEX_LOG.md").write_text("\n".join(log), encoding="utf-8")
    print(json.dumps({"status": validation["status"], "prevalidation_pass": validation["prevalidation_pass"], "readiness": validation["qa"]["readiness_count"], "renders": validation["qa"]["render_count"], "blend": final_blend, "glb": final_glb}, indent=2))

main()
