"""Resolve the R03 callout and overview targets against the frozen REV004.1 GLB."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import bpy


CALLOUTS = [
    ("POVU ENTRANCE / WATER WALL", ["VIP_ENTRANCE_SIGNAGE", "POVU_WATER_WALL_7M", "VIP_ENTRANCE_CANOPY"]),
    ("HANDS OF GROWTH", ["NAV_TARGET_HANDS_OF_GROWTH", "HANDS_OF_GROWTH", "HOG_HAND_LEFT"]),
    ("RESTAURANT / POVU CAFE", ["RESTAURANT_ENTRANCE_SIGNAGE", "CAFE_GLASS_FRONT", "CAFE_TERRACE"]),
    ("EAST STAIR / GLASS DECK", ["GLASS_DECK_EAST_STAIR_STEP_06", "GLASS_DECK_EAST_STAIR"]),
    ("POVU SMART MANUFACTURING", ["MIXING_PLATFORM", "ProcessTank_01", "PRODUCTION_FLOOR"]),
]

OVERVIEW = [
    ("R&D / QC", ["R_D_QC_ENTRANCE_SIGNAGE", "R_D_QC_ENTRANCE_CANOPY"]),
    ("RESTAURANT / CAFE", ["RESTAURANT_ENTRANCE_SIGNAGE", "CAFE_GLASS_FRONT"]),
    ("WELLNESS / RECREATION", ["WELLNESS_PAVILION", "RECREATION_COURT"]),
    ("POVU FACTORY", ["PRODUCTION_FLOOR", "Production_Hall"]),
]


def resolve(query: str, names: list[str]) -> str | None:
    normalized = query.upper().rstrip("*")
    for name in names:
        upper = name.upper()
        if upper == normalized:
            return name
    for name in names:
        if name.upper().startswith(normalized):
            return name
    for name in names:
        if normalized in name.upper():
            return name
    return None


def main() -> int:
    if "--" not in sys.argv:
        raise SystemExit("expected -- <repo-root>")
    root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
    glb_path = root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(glb_path))
    names = [obj.name for obj in bpy.data.objects if obj.name]

    def audit(items: list[tuple[str, list[str]]]) -> list[dict]:
        results = []
        for label, queries in items:
            resolved = next((resolve(query, names) for query in queries if resolve(query, names)), None)
            results.append({"label": label, "queries": queries, "resolved": resolved})
        return results

    callouts = audit(CALLOUTS)
    overview = audit(OVERVIEW)
    missing = [item for item in callouts + overview if item["resolved"] is None]
    output = {
        "status": "PASS" if not missing else "FAIL",
        "source": str(glb_path),
        "sourceObjectCount": len(names),
        "callouts": callouts,
        "overviewLabels": overview,
        "missing": missing,
    }
    print(json.dumps(output, indent=2))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
