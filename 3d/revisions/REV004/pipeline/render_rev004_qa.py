"""Render low-resolution architectural QA stills from the REV004 blend."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import bpy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--blend", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    args = parser.parse_args(argv)
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.open_mainfile(filepath=os.path.abspath(args.blend))
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 640
    scene.render.resolution_y = 360
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.studio_light = "paint.sl"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = "BOTH"

    cameras = [
        "PRES_VIP_ENTRANCE",
        "PRES_HANDS_OF_GROWTH",
        "PRES_GLASS_DECK_EAST_ACCESS",
        "PRES_GLASS_DECK_WEST_ACCESS",
        "PRES_GLASS_DECK_CENTRAL_ACCESS",
        "PRES_01_CAMPUS_HERO",
    ]
    rendered = []
    for name in cameras:
        camera = bpy.data.objects.get(name)
        if not camera or camera.type != "CAMERA":
            rendered.append({"camera": name, "status": "MISSING"})
            continue
        scene.camera = camera
        output = output_dir / f"{name}.png"
        scene.render.filepath = str(output)
        bpy.ops.render.render(write_still=True)
        rendered.append({"camera": name, "status": "PASS", "path": str(output), "bytes": output.stat().st_size})
    with open(args.report, "w", encoding="utf-8") as stream:
        json.dump({"blend": os.path.abspath(args.blend), "rendered": rendered}, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"rendered": len([item for item in rendered if item["status"] == "PASS"]), "report": args.report}))


if __name__ == "__main__":
    main()
