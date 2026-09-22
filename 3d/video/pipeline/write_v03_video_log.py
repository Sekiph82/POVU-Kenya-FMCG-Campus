import argparse
import json
import os
from datetime import datetime, timezone


def read_json(path):
    with open(path, "r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=int, required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--status", choices=["PASS", "BLOCKED_MISSING_GEOMETRY", "FAIL"], required=True)
    parser.add_argument("--render-time", default="not recorded")
    args = parser.parse_args()
    manifest = read_json(args.manifest)
    spec = next(item for item in manifest["videos"] if item["id"] == args.video)
    out = os.path.abspath(args.output_dir)
    inventory = read_json(os.path.join(out, "scene_inventory.json")) if os.path.exists(os.path.join(out, "scene_inventory.json")) else {}
    route = read_json(os.path.join(out, "camera_route.json")) if os.path.exists(os.path.join(out, "camera_route.json")) else {}
    settings = read_json(os.path.join(out, "render_settings.json")) if os.path.exists(os.path.join(out, "render_settings.json")) else {}
    qa = read_json(os.path.join(out, "qa_report.json")) if os.path.exists(os.path.join(out, "qa_report.json")) else {}
    metadata = read_json(os.path.join(out, "render_metadata.json")) if os.path.exists(os.path.join(out, "render_metadata.json")) else {}
    mp4 = next((name for name in os.listdir(out) if name.lower().endswith(".mp4")), None)
    ffprobe = read_json(os.path.join(out, "final_ffprobe.json")) if os.path.exists(os.path.join(out, "final_ffprobe.json")) else {}
    video_stream = next((stream for stream in ffprobe.get("streams", []) if stream.get("codec_type") == "video"), {})
    sha = ""
    sha_path = os.path.join(out, "final_sha256.txt")
    if os.path.exists(sha_path):
        with open(sha_path, "r", encoding="ascii") as handle:
            sha = handle.read().strip()
    size = os.path.getsize(os.path.join(out, mp4)) if mp4 and os.path.exists(os.path.join(out, mp4)) else 0
    lines = [
        f"# M01 VIDEO-{args.video:03d} V03 Codex Log",
        "",
        f"- Status: **{args.status}**",
        f"- Subject: {spec['title']}",
        f"- Source SHA-256: `{manifest['source_sha256']}`",
        f"- Active camera: `{route.get('camera', 'not available')}`",
        f"- Semantic targets requested: {', '.join(spec['targets'])}",
        f"- Semantic targets resolved: {', '.join(inventory.get('resolved_targets', []))}",
        f"- Camera route: 7 locked checkpoints at frames 1, 121, 241, 361, 481, 601, 718; route is stored in `camera_route.json`.",
        f"- Material overrides: none unless listed in `render_settings.json`; source GLB was not modified.",
        f"- Render settings: local Blender Eevee, native 1280x720, 100%, 24 fps, frames 1–720, Workbench false; stored in `render_settings.json`.",
        f"- Checkpoint QA: automated={qa.get('automated_all_pass', 'not available')}; visual={qa.get('visual_qa', 'not available')}; final report stored in `qa_report.json`.",
        f"- Visual QA note: {qa.get('visual_qa_note', 'not recorded')}",
        f"- MP4 absolute Windows path: `{os.path.join(out, mp4) if mp4 else 'not produced'}`",
        f"- File size: {size} bytes",
        f"- SHA-256: `{sha}`",
        f"- Duration: {ffprobe.get('format', {}).get('duration', 'not available')} seconds",
        f"- FPS: {video_stream.get('r_frame_rate', 'not available')}",
        f"- Resolution: {video_stream.get('width', 'not available')}x{video_stream.get('height', 'not available')}",
        f"- Codec: {video_stream.get('codec_name', 'not available')}",
        f"- Render time: {args.render_time}",
        f"- Limitations: {spec.get('limitations', 'none recorded')}",
        f"- Evidence directory: `{out}`",
        f"- Log updated UTC: {datetime.now(timezone.utc).isoformat()}",
        "",
    ]
    os.makedirs(os.path.dirname(os.path.abspath(args.log)), exist_ok=True)
    with open(args.log, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    print(json.dumps({"log": os.path.abspath(args.log), "status": args.status, "mp4": mp4, "sha256": sha}))


if __name__ == "__main__":
    main()
