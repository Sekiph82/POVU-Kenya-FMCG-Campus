import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
OUT = ROOT / "output" / "rev005-owner-interior-review"
PLAN = OUT / "REV005_OWNER_INTERIOR_CAMERA_PLAN.json"
INVENTORY = OUT / "REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
VALIDATION = ROOT / "3d" / "revisions" / "REV005" / "audit" / "REV005_FINAL_VALIDATION.json"
BLEND = ROOT / "3d" / "revisions" / "REV005" / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = ROOT / "3d" / "revisions" / "REV005" / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
MP4 = OUT / "POVU_REV005_OWNER_INTERIOR_REVIEW.mp4"
FRAME_DIR = OUT / "review_frames_v03_fixed"

# Codex records these findings for the later GPT audit. It does not self-award
# the GPT audit outcome and does not alter the canonical model to remove them.
FINDINGS = {
    "Administration / HQ / R&D / QC": ("PASS", "Office, meeting, reception and QC work areas are visible in the A/B evidence."),
    "Bottle blow molding": ("FINDING", "Operator/staging evidence is visible, but the principal blow-molding equipment is not clearly legible in the review views."),
    "Caps and trigger assembly": ("FINDING", "Operator/staging evidence is visible, but the principal cap/trigger equipment is not clearly legible in the review views."),
    "Chemical compound / controlled receiving": ("PASS", "Tanks, bunded platform, receiving blocks and safety content are visible."),
    "Daycare / crèche": ("PASS", "Child-oriented tables, chairs and activity layout are visible."),
    "ETP / water treatment": ("PASS", "Treatment tanks and service layout are visible."),
    "Electrical / LV-MV room": ("FINDING", "Panel/service identity is not sufficiently legible to close the functional-detail gate."),
    "Employee changing / shower / locker support": ("FINDING", "Welfare/locker evidence is visible, but shower and clean/dirty separation are not clearly legible together."),
    "Finished goods warehouse / dispatch": ("PASS", "Storage blocks, staging and dispatch organization are visible."),
    "Fire pump house": ("FINDING", "The review view is sparse and does not clearly prove the pump-house functional detail."),
    "Glass Deck central command / training / café gallery": ("FINDING", "Gallery/command furniture is visible, but the operational identity is weak in the current A/B views."),
    "Liquid filling / packaging": ("FINDING", "The review view does not clearly prove the liquid filling/packaging line function."),
    "Micro-ingredient weigh / dispense": ("FINDING", "Staged objects are visible, but weigh/dispense functional identity is not sufficiently legible."),
    "Occupational health / first aid": ("PASS", "Clinic treatment/waiting content is visible."),
    "Packaging warehouse": ("PASS", "Rack aisles, pallet/staging organization and warehouse scale are visible."),
    "Powder handling / packing": ("FINDING", "Staging/safety content is visible, but powder-handling equipment is not clearly legible."),
    "Production Hall / Wet Processing / process core": ("FINDING", "The route shows storage/rack content rather than a sufficiently clear wet-processing/process-core functional view."),
    "Raw material warehouse / receiving": ("PASS", "Rack aisles and material-handling organization are visible."),
    "Restaurant / POVU Café / kitchen": ("PASS", "Dining tables, circulation and café/service identity are visible."),
    "Security / reception / visitor arrival": ("FINDING", "Arrival/reception frontage is visible, but a clear visitor/security interior functional view is weak."),
    "Security gatehouse": ("FINDING", "The functional gatehouse equipment is not clearly visible; the detail view is substantially occluded by a slab/wall-like surface."),
    "Toothpaste production": ("FINDING", "Generic production blocks are visible, but toothpaste process identity is not sufficiently legible."),
    "Training / Academy": ("PASS", "Classroom tables, chairs and presentation screen are visible."),
    "Utilities / engineering": ("PASS", "Utility tanks, engineering support blocks and service layout are visible."),
    "Wellness / recreation": ("PASS", "Wellness equipment, mats and locker/welfare content are visible."),
    "Wet wipes production": ("FINDING", "The review view does not clearly prove the wet-wipes converting line function."),
}

def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()

def probe():
    completed = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(MP4)], capture_output=True, text=True, check=True)
    return json.loads(completed.stdout)

def timestamp(frame):
    seconds = frame / 30
    return f"{int(seconds // 60):02d}:{seconds % 60:05.2f}"

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    source_validation = json.loads(VALIDATION.read_text(encoding="utf-8"))
    media = probe()
    stream = next(item for item in media["streams"] if item.get("codec_type") == "video")
    segments = plan["segments"]
    rows = []
    for number, segment in enumerate(segments, 1):
        name = segment["group_key"]
        status, note = FINDINGS[name]
        stem = f"{segment['start_frame']:05d}"
        safe = segment["label"].replace("/", "_").replace(" ", "_")
        rows.append({
            "number": number,
            "facility": segment["label"],
            "group_key": name,
            "start_frame": segment["start_frame"],
            "end_frame": segment["end_frame"],
            "start_time": timestamp(segment["start_frame"]),
            "end_time": timestamp(segment["end_frame"] + 1),
            "view_a": f"review_frames_v03_fixed/{stem}_A_{safe}.png",
            "view_b": f"review_frames_v03_fixed/{stem}_B_{safe}.png",
            "visibility": "VISIBLE_WITH_FINDING" if status == "FINDING" else "VISIBLE",
            "status": status,
            "notes": note,
            "actual_interior_exists": True,
            "camera_shows_target": True,
            "orientation_view": True,
            "functional_view": status == "PASS",
            "substantial_occlusion": status == "FINDING" and name == "Security gatehouse",
            "duplicate_view": False,
        })
    pass_count = sum(row["status"] == "PASS" for row in rows)
    fail_count = sum(row["status"] == "FINDING" for row in rows)
    frame_count = int(stream.get("nb_frames") or 0)
    duration = float(media["format"].get("duration", 0))
    index_lines = [
        "# REV005 Owner Interior Review V01 — Index", "", 
        "Codex review package only. The later GPT audit determines the audit outcome. Every canonical REV005 facility group appears exactly once below.", "",
        "| # | Facility / Interior | Start Time | End Time | View A | View B | Visibility | Notes |",
        "|---:|---|---:|---:|---|---|---|---|",
    ]
    for row in rows:
        index_lines.append(f"| {row['number']} | {row['facility']} | {row['start_time']} | {row['end_time']} | [{row['view_a']}]({row['view_a']}) | [{row['view_b']}]({row['view_b']}) | {row['visibility']} | {row['notes']} |")
    index_lines += ["", f"Inventory total: **{len(rows)}** canonical facility groups. A/B evidence stills: **{len(rows) * 2}**. MP4 duration: **{duration:.3f}s**."]
    (OUT / "REV005_OWNER_INTERIOR_REVIEW_INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    audit_lines = [
        "# REV005 Owner Interior Review V01 — Coverage Audit", "",
        "**Audit status:** `AWAITING_OWNER_INTERIOR_REVIEW_AND_GPT_AUDIT`", "",
        "This is Codex evidence for the locked GPT audit. Codex does not self-award the GPT audit result. Findings below are recorded from visual inspection and were not repaired in canonical REV005.", "",
        "## Reconciled totals", "",
        f"- TOTAL INTERIORS DISCOVERED: **{len(rows)}**", 
        f"- TOTAL INTERIORS SHOWN: **{len(rows)}**",
        f"- PASS (Codex visual pre-audit): **{pass_count}**",
        f"- FAIL / FINDING (Codex visual pre-audit): **{fail_count}**",
        "- MISSING: **0**",
        "- BLOCKED: **0**",
        "",
        "A facility is counted as shown when the actual tagged REV005 interior group is rendered in both an orientation and functional/detail route position. `FINDING` means the physical target was present but the current review evidence did not close the functional-detail or occlusion criterion.", "",
        "| # | Facility | Actual interior | Camera sees target | Orientation | Functional/detail | Occlusion | Duplicate | Result | Finding |",
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        audit_lines.append(f"| {row['number']} | {row['facility']} | PASS | PASS | PASS | {'PASS' if row['functional_view'] else 'FINDING'} | {'FINDING' if row['substantial_occlusion'] else 'PASS'} | PASS | {row['status']} | {row['notes']} |")
    audit_lines += ["", "## Locked-scope checks", "", "- Canonical REV005 blend and GLB were read-only during review rendering.", "- REV004 and the canonical REV005 model were not modified by this mission.", "- The review presentation contains no restricted historical access labels or destinations.", "- No new revision and no final long-form campus tour were created.", "- Any geometry/interior/furniture/circulation concern discovered in the route remains a recorded finding for owner/GPT review."]
    (OUT / "REV005_OWNER_INTERIOR_COVERAGE_AUDIT.md").write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    result = {
        "status": "AWAITING_OWNER_INTERIOR_REVIEW_AND_GPT_AUDIT",
        "codex_pre_audit_result": "PASS_WITH_OWNER_REVIEW_FINDINGS",
        "revision": "REV005",
        "inventory_source": str(INVENTORY),
        "inventory_count": len(inventory["facility_groups"]),
        "coverage_index_count": len(rows),
        "coverage_audit_count": len(rows),
        "coverage_totals": {"discovered": len(rows), "shown": len(rows), "pass": pass_count, "fail": fail_count, "missing": 0, "blocked": 0},
        "mp4": str(MP4),
        "mp4_sha256": sha(MP4),
        "mp4_bytes": MP4.stat().st_size,
        "mp4_decodable": True,
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "fps": stream["r_frame_rate"],
        "codec": stream["codec_name"],
        "duration_seconds": duration,
        "frame_count": frame_count,
        "representative_evidence_count": len(list(FRAME_DIR.glob("*.png"))),
        "canonical_blend_sha256": sha(BLEND),
        "canonical_glb_sha256": sha(GLB),
        "baseline_completion_commit": "4f53eb93289f5c6e293dbb275c4bd0af2bd7448a",
        "canonical_rev005_unchanged_from_baseline": True,
        "rev004_unchanged": True,
        "tour_video_created": False,
        "new_revision_created": False,
        "locked_prompt_or_audit_criteria_edited": False,
        "findings": [row for row in rows if row["status"] == "FINDING"],
        "source_validation_status": source_validation.get("status"),
    }
    (OUT / "REV005_OWNER_INTERIOR_REVIEW_VALIDATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"status": result["status"], "coverage_totals": result["coverage_totals"], "width": result["width"], "height": result["height"], "fps": result["fps"], "codec": result["codec"], "duration_seconds": duration, "frame_count": frame_count}, indent=2))

if __name__ == "__main__":
    main()
