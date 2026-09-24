"""Resolve every R02 camera target against the frozen REV004.1 GLB."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import bpy


def parse_plan(plan_path: Path) -> dict[str, dict]:
    text = plan_path.read_text(encoding="utf-8")
    pattern = re.compile(r'"(?P<id>M06V02-S\d+)"\s*:\s*\{shotId:"(?P<shot>M06V02-S\d+)"\s*,\s*label:"(?P<label>[^"]+)"\s*,\s*targetNames:\[(?P<targets>.*?)\]', re.S)
    plans = {}
    for match in pattern.finditer(text):
        targets = re.findall(r'"([^"]+)"', match.group("targets"))
        plans[match.group("id")] = {"label": match.group("label"), "targets": targets}
    return plans


def resolve(targets: list[str], names: list[str]) -> str | None:
    upper_names = [(name, name.upper()) for name in names]
    for query in targets:
        normalized = query.upper().rstrip("*")
        for name, upper in upper_names:
            if upper == normalized:
                return name
        for name, upper in upper_names:
            if upper.startswith(normalized):
                return name
        for name, upper in upper_names:
            if normalized in upper:
                return name
    return None


def main() -> int:
    if "--" not in sys.argv:
        raise SystemExit("expected -- <repo-root>")
    root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
    glb_path = root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(glb_path))
    plans = parse_plan(root / "remotion/povu-digital-twin/src/data/complete-tour-r02-target-plan.ts")
    names = [obj.name for obj in bpy.data.objects if obj.name]
    results = []
    for shot_id in sorted(plans):
        plan = plans[shot_id]
        resolved = resolve(plan["targets"], names)
        results.append({"shotId": shot_id, "label": plan["label"], "resolved": resolved, "targets": plan["targets"]})
    missing = [item for item in results if item["resolved"] is None]
    output = {"sourceObjectCount": len(names), "planCount": len(plans), "missing": missing, "results": results}
    print(json.dumps(output, indent=2))
    return 1 if missing or len(plans) != 61 else 0


if __name__ == "__main__":
    raise SystemExit(main())
