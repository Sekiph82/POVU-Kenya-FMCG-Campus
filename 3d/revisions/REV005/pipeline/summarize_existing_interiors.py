import json
import os
from pathlib import Path

ROOT = Path(r"C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo")
AUDIT = ROOT / "3d" / "revisions" / "REV005" / "audit" / "REV005_INTERIOR_AUDIT.json"
OUT = ROOT / "3d" / "revisions" / "REV005" / "audit" / "REV005_EXISTING_INTERIOR_SUMMARY.md"

data = json.loads(AUDIT.read_text(encoding="utf-8"))
items = data["program_term_inventory"]
by_name = {x["name"]: x for x in items}

buildings = [
    "VIP_Entrance_Pavilion", "Admin_RD_QC", "Daycare", "Clinic", "Restaurant_Wellness", "WELLNESS_PAVILION",
    "Production_Hall", "RM_Warehouse", "Packaging_Warehouse", "FG_Warehouse", "Chemical_Compound", "Utility_House",
    "ETP", "Fire_Water_Tank", "Bottle_BlowMolding", "Caps_Triggers", "WetWipes", "Toothpaste", "Powder_Packaging",
    "Liquid_Packing", "WEIGH_DISPENSE_ROOM", "GlassDeck_East", "GlassDeck_West"
]

def inside(obj, shell):
    b = obj.get("bounds")
    s = shell.get("bounds")
    if not b or not s:
        return False
    c = b["center"]
    lo, hi = s["min"], s["max"]
    return lo[0] - 0.25 <= c[0] <= hi[0] + 0.25 and lo[1] - 0.25 <= c[1] <= hi[1] + 0.25 and lo[2] - 0.25 <= c[2] <= hi[2] + 0.25

lines = ["# REV005 Existing Interior Summary", "", f"Source: `{data['source_blend']}`", "", "This is a source audit only. No REV004 file was modified.", ""]
for name in buildings:
    shell = by_name.get(name)
    if not shell:
        lines += [f"## {name}", "MISSING FROM TERM INVENTORY", ""]
        continue
    contained = [x for x in items if x["name"] != name and inside(x, shell)]
    meshes = [x["name"] for x in contained if x["type"] == "MESH"]
    lines += [f"## {name}", f"Shell bounds: `{shell['bounds']['size']}` at `{shell['bounds']['center']}`", f"Contained named program objects: {len(contained)} (meshes {len(meshes)})"]
    if meshes:
        lines.append("- " + "\n- ".join(sorted(meshes)[:120]))
    else:
        lines.append("- No named interior/support objects were found within the shell bounds.")
    lines.append("")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(OUT)
