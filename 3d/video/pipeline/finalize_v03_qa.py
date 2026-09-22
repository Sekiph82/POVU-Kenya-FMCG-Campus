import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--status", choices=["PASS", "FAIL"], required=True)
    parser.add_argument("--note", default="")
    args = parser.parse_args()
    path = os.path.join(os.path.abspath(args.output_dir), "qa_report.json")
    with open(path, "r", encoding="utf-8") as handle:
        report = json.load(handle)
    report["visual_qa"] = args.status
    report["visual_qa_note"] = args.note
    report["all_pass"] = bool(report.get("automated_all_pass")) and args.status == "PASS"
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(json.dumps({"qa_report": path, "all_pass": report["all_pass"], "visual_qa": report["visual_qa"]}))


if __name__ == "__main__":
    main()
