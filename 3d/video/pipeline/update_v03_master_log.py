import argparse
import json
import os
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--log", required=True)
    args = parser.parse_args()
    with open(args.state, "r", encoding="utf-8") as handle:
        state = json.load(handle)
    with open(args.manifest, "r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    by_id = {entry["video"]: entry for entry in state["videos"]}
    counts = state.get("counts", {})
    lines = [
        "# POVU M01 — V03 Clean Master Production Log", "", "## Batch scope", "",
        "This run rebuilds the 48 canonical videos with IDs 001–011 and 013–050 using local Windows Blender. Approved canonical 012 and 019 remain untouched; Hands of Growth and Color/Materials Proof remain untouched validation films.", "",
        f"- Batch: `{state['batch']}`", f"- Source SHA-256: `{state['source_sha256']}`", "- Renderer: local Windows Blender Eevee only", "- Output root: `3d/video/V03_CLEAN_MASTER/`", f"- Target count: {state['target_count']}", f"- Counts: {json.dumps(counts, sort_keys=True)}", "- Approved existing: 012, 019", "", "## Quality contract", "",
        "Each rebuilt video requires actual REV003 semantic targets, a subject-specific camera route, native 1280x720 Eevee at 24 fps for frames 1–720, seven checkpoint renders, visual contact-sheet QA, final H.264, ffprobe, seven extracted final QA frames, SHA-256, an individual log, and GitHub publication. Source geometry and source GLB materials remain unchanged.", "", "## Video results", "", "| Video | Subject | Status |", "|---:|---|---|"
    ]
    for spec in sorted(manifest["videos"], key=lambda item: item["id"]):
        entry = by_id[spec["id"]]
        lines.append(f"| {spec['id']:03d} | {spec['title']} | {entry['status']} |")
    lines += ["", "## Restart rule", "", "On interruption, inspect `coordination/batch_state.json` and each V03 output directory. Resume at the first video that is not genuinely PASS or documented `BLOCKED_MISSING_GEOMETRY`. Do not rerender an already validated PASS output.", "", f"Updated UTC: {datetime.now(timezone.utc).isoformat()}", ""]
    with open(args.log, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines))
    print(json.dumps({"log": os.path.abspath(args.log), "counts": counts}))


if __name__ == "__main__":
    main()
