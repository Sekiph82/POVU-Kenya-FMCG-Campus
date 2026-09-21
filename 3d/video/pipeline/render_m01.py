import argparse
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

import bpy
from mathutils import Vector


def parse_args():
    raw = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description="POVU M01 local Blender video renderer")
    parser.add_argument("--source", required=True)
    parser.add_argument("--video-id", required=True, type=int)
    parser.add_argument("--title", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--qa-dir", required=True)
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--resolution-percentage", type=int, default=100)
    parser.add_argument("--engine", choices=["eevee", "workbench"], default="eevee")
    parser.add_argument("--merge-meshes", action="store_true")
    parser.add_argument("--frame-format", choices=["PNG", "JPEG"], default="JPEG")
    return parser.parse_args(raw)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.cameras, bpy.data.lights, bpy.data.materials):
        # Keep imported materials; only remove cameras/lights left by a prior run.
        if datablocks in (bpy.data.cameras, bpy.data.lights):
            for block in list(datablocks):
                datablocks.remove(block)


def import_source(source):
    ext = Path(source).suffix.lower()
    if ext == ".glb" or ext == ".gltf":
        bpy.ops.import_scene.gltf(filepath=str(source))
    elif ext == ".blend":
        bpy.ops.wm.open_mainfile(filepath=str(source))
    else:
        raise RuntimeError(f"Unsupported source format: {ext}")


def scene_bounds():
    points = []
    objects = []
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH":
            objects.append(obj)
            points.extend([obj.matrix_world @ Vector(corner) for corner in obj.bound_box])
    if not points:
        raise RuntimeError("Imported source contains no mesh geometry")
    lo = Vector((min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)))
    hi = Vector((max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)))
    return lo, hi, objects


def merge_meshes(objects):
    if len(objects) < 2:
        return
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.object.join()


def look_at(cam, target):
    cam.rotation_euler = (Vector(target) - cam.location).to_track_quat("-Z", "Y").to_euler()


def make_camera(video_id, lo, hi):
    center = (lo + hi) / 2.0
    size = hi - lo
    radius = max(size.x, size.y, size.z, 1.0)
    # Deterministic, subject-specific route variations keep one-camera-at-a-time
    # production while staying grounded in the actual imported campus bounds.
    angle = math.radians((video_id * 37) % 360)
    side = Vector((math.cos(angle), math.sin(angle), 0.0))
    forward = Vector((-math.sin(angle), math.cos(angle), 0.0))
    elevated = max(size.z * 0.75, radius * 0.42)
    near_elevated = max(size.z * 0.32, radius * 0.16)
    if video_id == 1:
        elevated = max(size.z * 1.05, radius * 0.65)
        near_elevated = max(size.z * 0.62, radius * 0.34)
    focus = center + Vector((0.0, 0.0, size.z * 0.18))
    camera_name = f"VID_{video_id:03d}_{Path(str(video_id)).stem}"
    data = bpy.data.cameras.new(f"VID_{video_id:03d}_DATA")
    cam = bpy.data.objects.new(camera_name, data)
    bpy.context.scene.collection.objects.link(cam)
    data.lens = 48 if video_id == 1 else 52
    data.sensor_width = 36
    # A deliberate reveal: wide context, lateral approach, low hero, then hold.
    route = [
        (0, center + side * radius * 1.55 + forward * radius * 1.10 + Vector((0, 0, elevated)), focus),
        (120, center + side * radius * 1.15 + forward * radius * 0.86 + Vector((0, 0, elevated * 0.82)), focus),
        (288, center + side * radius * 0.72 + forward * radius * 0.54 + Vector((0, 0, near_elevated * 1.30)), focus),
        (480, center + side * radius * 0.52 + forward * radius * 0.18 + Vector((0, 0, near_elevated)), center + Vector((0, 0, size.z * 0.20))),
        (719, center + side * radius * 0.42 - forward * radius * 0.10 + Vector((0, 0, near_elevated * 0.94)), center + Vector((0, 0, size.z * 0.24))),
    ]
    for frame, location, target in route:
        cam.location = location
        look_at(cam, target)
        cam.keyframe_insert(data_path="location", frame=frame)
        cam.keyframe_insert(data_path="rotation_euler", frame=frame)
    return cam, route


def configure_render(output, resolution_percentage, engine_name):
    scene = bpy.context.scene
    scene.frame_start = 0
    scene.frame_end = 719
    scene.render.fps = 24
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 720
    scene.render.resolution_percentage = resolution_percentage
    if engine_name == "workbench":
        scene.render.engine = "BLENDER_WORKBENCH"
        scene.display.shading.light = "STUDIO"
        scene.display.shading.color_type = "MATERIAL"
        scene.display.shading.show_shadows = True
        scene.display.shading.show_cavity = True
    else:
        try:
            scene.render.engine = "BLENDER_EEVEE_NEXT"
        except Exception:
            scene.render.engine = "BLENDER_EEVEE"
    # Blender 5.2 on this machine exposes the movie enum but rejects assigning
    # it in headless mode. Render lossless PNG frames locally, then encode with
    # the installed local ffmpeg executable in the orchestration step.
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = str(output.parent / f"{output.stem}_frames" / "frame_")
    scene.render.film_transparent = False
    scene.world.color = (0.025, 0.04, 0.06)
    # A modest sun gives the imported GLB readable form without changing source data.
    light_data = bpy.data.lights.new("M01_Sun", type="SUN")
    light_data.energy = 2.2
    sun = bpy.data.objects.new("M01_Sun", light_data)
    bpy.context.scene.collection.objects.link(sun)
    sun.rotation_euler = (math.radians(28), math.radians(-18), math.radians(25))


def bounds_payload(lo, hi, objects):
    return {
        "object_count": len(objects),
        "bounds_min": [round(v, 4) for v in lo],
        "bounds_max": [round(v, 4) for v in hi],
        "dimensions": [round(v, 4) for v in (hi - lo)],
        "sample_objects": [obj.name for obj in objects[:30]],
    }


def main():
    args = parse_args()
    source = Path(args.source).resolve()
    output = Path(args.output).resolve()
    qa_dir = Path(args.qa_dir).resolve()
    qa_dir.mkdir(parents=True, exist_ok=True)
    if not source.exists():
        raise FileNotFoundError(source)
    clear_scene()
    import_source(source)
    lo, hi, objects = scene_bounds()
    payload = bounds_payload(lo, hi, objects)
    payload.update({"source": str(source), "video_id": args.video_id, "title": args.title})
    if args.inspect:
        print(json.dumps(payload, indent=2))
        return
    if args.merge_meshes:
        merge_meshes(objects)
    cam, route = make_camera(args.video_id, lo, hi)
    scene = bpy.context.scene
    scene.camera = cam
    configure_render(output, args.resolution_percentage, args.engine)
    scene["POVU_M01_VIDEO_ID"] = args.video_id
    scene["POVU_M01_TITLE"] = args.title
    scene["POVU_M01_SOURCE_SHA256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    blend_path = output.with_suffix(".blend")
    frame_dir = output.parent / f"{output.stem}_frames"
    frame_dir.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    if args.preview:
        scene.render.image_settings.file_format = "PNG"
        for frame, label in ((0, "begin"), (360, "middle"), (719, "end")):
            scene.frame_set(frame)
            scene.render.filepath = str(qa_dir / f"{label}.png")
            bpy.ops.render.render(write_still=True)
        payload.update({"preview": True, "preview_frames": [0, 360, 719], "resolution_percentage": args.resolution_percentage, "engine": args.engine, "blender_version": bpy.app.version_string})
        (output.with_suffix(".preview.json")).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"POVU_M01_PREVIEW_DONE video={args.video_id:03d}")
        return
    scene.render.image_settings.file_format = args.frame_format
    scene.render.filepath = str(frame_dir / "frame_")
    start = time.time()
    print(f"POVU_M01_RENDER_START video={args.video_id:03d} output={output}")
    bpy.ops.render.render(animation=True)
    elapsed = time.time() - start
    payload.update({
        "output": str(output),
        "blend_archive": str(blend_path),
        "frame_dir": str(frame_dir),
        "frame_format": args.frame_format,
        "render_engine": scene.render.engine,
        "engine_requested": args.engine,
        "resolution": [scene.render.resolution_x, scene.render.resolution_y],
        "resolution_percentage": scene.render.resolution_percentage,
        "fps": scene.render.fps,
        "frame_start": scene.frame_start,
        "frame_end": scene.frame_end,
        "duration_seconds_expected": (scene.frame_end - scene.frame_start + 1) / scene.render.fps,
        "elapsed_seconds": round(elapsed, 3),
        "route": [[f, [round(x, 3) for x in loc], [round(x, 3) for x in tgt]] for f, loc, tgt in route],
        "blender_version": bpy.app.version_string,
    })
    (output.with_suffix(".render.json")).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"POVU_M01_RENDER_DONE video={args.video_id:03d} elapsed={elapsed:.1f}s")


if __name__ == "__main__":
    main()
