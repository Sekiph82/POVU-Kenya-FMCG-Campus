import hashlib
import json
import struct
import subprocess
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
REV = ROOT / "3d" / "revisions" / "REV005"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
SOURCE = ROOT / "3d" / "revisions" / "REV004.2" / "POVU_REV004_2_FINAL_MASTER.glb"
REV004 = ROOT / "3d" / "revisions" / "REV004" / "POVU_REV004_FINAL_MASTER.glb"
MANIFEST = REV / "REV005_ARCHITECTURAL_MANIFEST.json"
QA = REV / "audit" / "REV005_VISUAL_QA_REPORT.json"
OUT = REV / "audit" / "REV005_FINAL_VALIDATION.json"

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def glb_json(path):
    data = path.read_bytes()
    if data[:4] != b"glTF":
        raise RuntimeError("not a GLB")
    offset = 12
    while offset < len(data):
        length, kind = struct.unpack_from("<II", data, offset)
        payload = data[offset + 8:offset + 8 + length]
        if kind == 0x4E4F534A:
            return json.loads(payload.decode("utf-8"))
        offset += 8 + length
    raise RuntimeError("JSON chunk missing")

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    qa = json.loads(QA.read_text(encoding="utf-8")) if QA.exists() else {"status": "MISSING", "results": []}
    gltf = glb_json(GLB)
    names = [node.get("name", "") for node in gltf.get("nodes", [])]
    interior_nodes = sum(1 for node in gltf.get("nodes", []) if (node.get("extras") or {}).get("rev005_facility"))
    upper = [n.upper() for n in names]
    retired = sorted(n for n, u in zip(names, upper) if "EAST_ACCESS" in u or "WEST_ACCESS" in u or u.startswith("GLASS_DECK_EAST") or u.startswith("GLASS_DECK_WEST") or n in {"GlassDeck_East", "GlassDeck_West"})
    removed_trees = [n for n in ("TREE_CANOPY", "TREE_CANOPY001", "TREE_CANOPY002", "TREE_CANOPY003", "TREE_CANOPY004", "TREE_CANOPY005", "TREE_TRUNK", "TREE_TRUNK001") if n not in names]
    living_removed = [n for n in ("LIVING_WALL_PANEL", "LIVING_WALL_FOLIAGE", "LIVING_WALL_FOLIAGE001", "LIVING_WALL_FOLIAGE002", "LIVING_WALL_EXTENDED_BACKING") if n not in names]
    qa_pass = qa.get("status") == "PASS" and len(qa.get("results", [])) == 15 and all(x.get("status") == "PASS" for x in qa.get("results", []))
    rev004_status = subprocess.run(["git", "status", "--short", "--", "3d/revisions/REV004"], cwd=ROOT, capture_output=True, text=True, check=False).stdout.splitlines()
    rev004_tracked_modified = [line for line in rev004_status if not line.startswith("??")]
    checks = {
        "rev005_blend_exists": BLEND.exists(),
        "rev005_glb_exists": GLB.exists(),
        "glb_has_nodes": len(names) > 2000,
        "interior_collection_extras_present": any((node.get("extras") or {}).get("rev005_facility") for node in gltf.get("nodes", [])),
        "east_west_access_absent": not retired,
        "two_owner_tree_assemblies_absent": len(removed_trees) == 8,
        "living_wall_left_extension_absent": len(living_removed) == 5,
        "living_wall_retained_section_present": "LIVING_WALL_PANEL001" in names and "VIP_LivingWall" in names,
        "hands_of_growth_present": "HANDS_OF_GROWTH" in names and "LABEL_ANCHOR_HANDS_OF_GROWTH" in names,
        "qa_15_of_15_pass": qa_pass,
        "tour_video_not_created": not list(REV.glob("*.mp4")),
        "rev004_tracked_files_unmodified": not rev004_tracked_modified,
        "rev004_reference_exists": REV004.exists(),
        "source_revision_exists": SOURCE.exists(),
    }
    result = {
        "status": "PASS" if all(checks.values()) else "BLOCKED",
        "checks": checks,
        "failed_checks": [k for k, v in checks.items() if not v],
        "revision": "REV005",
        "source_revision": "REV004.2",
        "blend": str(BLEND),
        "blend_sha256": sha(BLEND),
        "glb": str(GLB),
        "glb_sha256": sha(GLB),
        "source_glb_sha256": sha(SOURCE) if SOURCE.exists() else None,
        "rev004_glb_sha256": sha(REV004) if REV004.exists() else None,
        "glb_node_count": len(names),
        "glb_mesh_count": len(gltf.get("meshes", [])),
        "glb_material_count": len(gltf.get("materials", [])),
        "rev005_interior_node_count": interior_nodes,
        "retired_east_west_names_found": retired,
        "removed_tree_names_absent": removed_trees,
        "living_wall_removed_names_absent": living_removed,
        "qa_report": str(QA),
        "manifest": str(MANIFEST),
        "rev004_git_status_lines": rev004_status,
    }
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    manifest["output_glb_sha256"] = result["glb_sha256"]
    manifest["blend_sha256"] = result["blend_sha256"]
    manifest.setdefault("counts", {})["glb_nodes"] = result["glb_node_count"]
    manifest.setdefault("counts", {})["glb_meshes"] = result["glb_mesh_count"]
    manifest.setdefault("counts", {})["glb_materials"] = result["glb_material_count"]
    manifest.setdefault("counts", {})["rev005_interior_nodes"] = result["rev005_interior_node_count"]
    manifest["visual_qa_report"] = str(QA)
    manifest["visual_qa_status"] = qa.get("status")
    manifest["final_validation"] = str(OUT)
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
