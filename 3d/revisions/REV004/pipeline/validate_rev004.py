"""Validate REV004 artifacts, GLB reload evidence, and visual QA evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


EXPECTED_SOURCE_SHA = "839D70086DF52604284C3CDCE8599AC7738A1CDC916B56DACF50A6B3A5EEBC07"
REQUIRED_FINAL_NAMES = [
    "VIP_ENTRANCE_DOOR_L",
    "VIP_ENTRANCE_DOOR_R",
    "WATER_WALL_STRUCTURE",
    "WATER_WALL_WATER_SURFACE",
    "WATER_WALL_BASIN",
    "WATER_WALL_TOP_FEED",
    "WATER_WALL_POVU_SIGNAGE",
    "SMART_TOTEM_VIP_BODY",
    "SMART_TOTEM_VIP_SCREEN",
    "SMART_TOTEM_CAMPUS_01_BODY",
    "SMART_TOTEM_CAMPUS_02_BODY",
    "SMART_TOTEM_CAMPUS_03_BODY",
    "SMART_TOTEM_CAMPUS_04_BODY",
    "GLASS_DECK_EAST_STAIR_STEP_01",
    "GLASS_DECK_WEST_STAIR_STEP_12",
    "GLASS_DECK_CENTRAL_STAIR_STEP_12",
    "GLASS_DECK_CENTRAL_LIFT",
    "PRODUCTION_ROOF",
    "PRODUCTION_FLOOR",
    "PRODUCTION_WALL_NORTH",
    "PRODUCTION_WALL_SOUTH",
    "PRODUCTION_WALL_EAST",
    "PRODUCTION_WALL_WEST",
    "HOG_TREE_TRUNK",
    "HOG_TREE_CROWN_0",
    "SOLAR_ARRAY",
    "ProcessTank_01",
    "PRES_HANDS_OF_GROWTH",
    "PRES_VIP_ENTRANCE",
    "PRES_GLASS_DECK_EAST_ACCESS",
]
REQUIRED_SOURCE_NAMES = ["Production_Hall", "VIP_LivingWall", "GlassDeck_East", "SolarPanel", "ProcessTank_01"]
REQUIRED_QA_CAMERAS = [
    "PRES_VIP_ENTRANCE",
    "PRES_HANDS_OF_GROWTH",
    "PRES_GLASS_DECK_EAST_ACCESS",
    "PRES_GLASS_DECK_WEST_ACCESS",
    "PRES_GLASS_DECK_CENTRAL_ACCESS",
    "PRES_01_CAMPUS_HERO",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    rev = repo / "3d" / "revisions" / "REV004"
    source = repo / "3d" / "revisions" / "REV003" / "POVU_REV003_MASTER.glb"
    final_blend = rev / "POVU_KENYA_FMCG_CAMPUS_REV004_FINAL_ARCHITECTURAL_MASTER.blend"
    final_glb = rev / "POVU_REV004_FINAL_MASTER.glb"
    manifest_path = rev / "REV004_ARCHITECTURAL_MANIFEST.json"
    source_inventory_path = rev / "audit" / "REV003_full_inventory.json"
    reload_inventory_path = rev / "audit" / "REV004_GLTF_RELOAD_INVENTORY.json"
    visual_report_path = rev / "qa" / "REV004_visual_qa_report.json"

    manifest = load(manifest_path)
    source_inventory = load(source_inventory_path)
    reload_inventory = load(reload_inventory_path)
    visual_report = load(visual_report_path)
    source_names = set(source_inventory["object_names"])
    final_names = set(reload_inventory["object_names"])
    required_missing = sorted(set(REQUIRED_FINAL_NAMES) - final_names)
    source_missing = sorted(set(REQUIRED_SOURCE_NAMES) - source_names)
    qa_status = {item["camera"]: item["status"] for item in visual_report["rendered"]}
    qa_missing = sorted(name for name in REQUIRED_QA_CAMERAS if qa_status.get(name) != "PASS")
    totem_table = manifest.get("smart_totem_placement_table", [])

    checks = {
        "source_exists": source.exists(),
        "source_sha256_matches_expected": source.exists() and sha256(source) == EXPECTED_SOURCE_SHA,
        "source_inventory_matches_expected": source_inventory.get("source_sha256", "").upper() == EXPECTED_SOURCE_SHA,
        "final_blend_exists": final_blend.exists(),
        "final_glb_exists": final_glb.exists(),
        "final_glb_reload_inventory_matches_export": reload_inventory.get("source_sha256", "").upper() == sha256(final_glb),
        "required_source_names_present": not source_missing,
        "required_final_names_present_after_reload": not required_missing,
        "five_totem_placements_documented": len(totem_table) == 5,
        "visual_qa_cameras_rendered": not qa_missing,
        "remotion_not_started": not (repo / "remotion" / "renders").exists(),
    }
    result = {
        "status": "PASS" if all(checks.values()) else "BLOCKED",
        "checks": checks,
        "failed_checks": [name for name, passed in checks.items() if not passed],
        "source_sha256": sha256(source) if source.exists() else None,
        "final_glb_sha256": sha256(final_glb) if final_glb.exists() else None,
        "source_inventory_counts": {key: source_inventory.get(key) for key in ("object_count", "mesh_object_count", "material_count", "camera_count")},
        "final_reload_counts": {key: reload_inventory.get(key) for key in ("object_count", "mesh_object_count", "material_count", "camera_count")},
        "final_missing_names": required_missing,
        "source_missing_names": source_missing,
        "visual_qa_missing_or_failed": qa_missing,
        "totem_placement_count": len(totem_table),
        "manifest_revision": manifest.get("revision"),
        "blender_version": manifest.get("blender_version"),
        "artifacts": {
            "blend": str(final_blend),
            "glb": str(final_glb),
            "manifest": str(manifest_path),
            "visual_qa_report": str(visual_report_path),
        },
    }
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
