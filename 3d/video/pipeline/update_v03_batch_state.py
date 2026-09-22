import argparse
import json
import os
from datetime import datetime, timezone


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--video", type=int)
    parser.add_argument("--status", choices=["PENDING", "QA", "RENDERING", "VALIDATING", "PASS", "FAIL", "BLOCKED"])
    parser.add_argument("--note", default="")
    parser.add_argument("--render-time", default="")
    args = parser.parse_args()
    state_path = os.path.abspath(args.state)
    if os.path.exists(state_path):
        with open(state_path, "r", encoding="utf-8") as handle:
            state = json.load(handle)
    else:
        with open(args.manifest, "r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        entries = []
        for spec in sorted(manifest["videos"], key=lambda item: item["id"]):
            entries.append({"video": spec["id"], "title": spec["title"], "status": "PENDING", "updated_at_utc": now(), "note": ""})
        state = {"batch": "M01_REMAINING_48_V03_CLEAN_MASTER", "source_sha256": manifest["source_sha256"], "target_count": len(entries), "approved_existing": {"012": "V03_APPROVED", "019": "V03_APPROVED"}, "videos": entries, "updated_at_utc": now()}
    if args.video is not None:
        matches = [entry for entry in state["videos"] if entry["video"] == args.video]
        if not matches:
            raise SystemExit(f"Video {args.video} is not in batch state")
        entry = matches[0]
        entry["status"] = args.status
        entry["updated_at_utc"] = now()
        if args.note:
            entry["note"] = args.note
        if args.render_time:
            entry["render_time"] = args.render_time
    state["updated_at_utc"] = now()
    counts = {}
    for entry in state["videos"]:
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    state["counts"] = counts
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    with open(state_path, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)
    print(json.dumps({"state": state_path, "counts": counts}))


if __name__ == "__main__":
    main()
