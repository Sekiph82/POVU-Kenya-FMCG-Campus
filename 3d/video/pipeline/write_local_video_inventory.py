"""Write a durable inventory of the POVU M01 videos currently saved locally."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


VIDEOS = [
    ("001", "POVU Campus Aerial", "V03_CLEAN_MASTER/VID_001_POVU_Campus_Aerial/POVU_VID_001_POVU_Campus_Aerial_30s.mp4", "PASS"),
    ("002", "Main Entrance & POVU Plaza", "V03_CLEAN_MASTER/VID_002_Main_Entrance_POVU_Plaza/POVU_VID_002_Main_Entrance_POVU_Plaza_30s.mp4", "PASS"),
    ("003", "People & Employee Campus", "V03_CLEAN_MASTER/VID_003_People_Employee_Campus/POVU_VID_003_People_Employee_Campus_30s.mp4", "FAIL"),
    ("004", "Administration & Headquarters", "V03_CLEAN_MASTER/VID_004_Administration_Headquarters/POVU_VID_004_Administration_Headquarters_30s.mp4", "PASS"),
    ("006", "Training & POVU Academy", "V03_CLEAN_MASTER/VID_006_Training_POVU_Academy/POVU_VID_006_Training_POVU_Academy_30s.mp4", "PASS"),
    ("007", "Restaurant + POVU Cafe", "V03_CLEAN_MASTER/VID_007_Restaurant_POVU_Cafe/POVU_VID_007_Restaurant_POVU_Cafe_30s.mp4", "FAIL"),
    ("012", "POVU Glass Deck", "V03_CORRECTIVE/VIDEO_03_GLASS_DECK/POVU_VID_GLASS_DECK_V03_30s.mp4", "V03_APPROVED"),
    ("019", "Liquid Mixing / Wet Processing", "V03_CORRECTIVE/VIDEO_01_WET_PROCESSING/POVU_VID_019_V03_Wet_Processing_CLEAN_30s.mp4", "V03_APPROVED"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    entries = []
    for video_id, title, relative_path, status in VIDEOS:
        path = args.repo / "3d" / "video" / relative_path
        entry = {
            "video": video_id,
            "title": title,
            "status": status,
            "relative_path": path.relative_to(args.repo).as_posix(),
            "absolute_path": str(path),
            "exists": path.is_file(),
        }
        if path.is_file():
            entry["bytes"] = path.stat().st_size
            entry["sha256"] = sha256(path)
        entries.append(entry)

    payload = {
        "batch": "M01_REMAINING_48_V03_CLEAN_MASTER",
        "source_sha256": "839d70086df52604284c3cdce8599ac7738a1cdc916b56dacf50a6b3a5eebc07",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "production_paused_after": "007",
        "local_output_root": str(args.repo / "3d" / "video" / "V03_CLEAN_MASTER"),
        "note": "012 and 019 are preserved approved V03_CORRECTIVE outputs; failed 003 and 007 MP4s are retained as evidence; 005 has no MP4 because checkpoint QA failed before full render.",
        "videos": entries,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "all_exist": all(item["exists"] for item in entries)}))


if __name__ == "__main__":
    main()
