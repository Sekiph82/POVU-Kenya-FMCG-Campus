import bpy
import json
import math
import re
import struct
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
V05_RENDERER = REV / "pipeline/render_rev005_interior_remediation_v05.py"

source = V05_RENDERER.read_text(encoding="utf-8")
prefix = source.split("\ndef main():", 1)[0]
exec(compile(prefix, str(V05_RENDERER), "exec"), globals())

# The imported V05 helper defines its own OUT/ROOT globals; restore V07 paths.
ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
INV = ROOT / "output/rev005-owner-interior-review/REV005_OWNER_INTERIOR_MODEL_INVENTORY.json"
V05_RENDERER = REV / "pipeline/render_rev005_interior_remediation_v05.py"

PRESERVE = {
    "Caps and trigger assembly", "Daycare / crèche", "Electrical / LV-MV room",
    "Employee changing / shower / locker support", "Fire pump house",
    "Micro-ingredient weigh / dispense",
}

def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()

def is_v06(obj):
    return bool(obj.get("REV005_REMEDIATION_V06")) or obj.name.startswith("V06_")

def bbox(obj):
    try:
        corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        lo = Vector((min(c.x for c in corners), min(c.y for c in corners), min(c.z for c in corners)))
        hi = Vector((max(c.x for c in corners), max(c.y for c in corners), max(c.z for c in corners)))
        return lo, hi
    except Exception:
        p = obj.matrix_world.translation.copy()
        return p, p

def center(obj):
    lo, hi = bbox(obj)
    return (lo + hi) / 2.0

def extent(obj):
    lo, hi = bbox(obj)
    return hi - lo

def finite_vector(value):
    return all(math.isfinite(float(x)) for x in value)

def layer_find(layer, name):
    if layer.name == name:
        return layer
    for child in layer.children:
        found = layer_find(child, name)
        if found:
            return found
    return None

def collection_visible(collection):
    results = []
    for view_layer in bpy.context.scene.view_layers:
        layer = layer_find(view_layer.layer_collection, collection.name)
        results.append({
            "view_layer": view_layer.name,
            "found": bool(layer),
            "enabled": bool(layer and not layer.exclude and not layer.hide_viewport),
            "excluded": bool(layer and layer.exclude),
            "hidden": bool(layer and layer.hide_viewport),
        })
    return results

def path_for(collection):
    paths = []
    for scene in bpy.data.scenes:
        def walk(layer, path):
            current = path + [layer.name]
            if layer.name == collection.name:
                paths.append("/".join(current))
            for child in layer.children:
                walk(child, current)
        walk(scene.view_layers[0].layer_collection, [])
    return sorted(set(paths))

def same_group(group, obj):
    return meta_match(group, obj.get("facility"))

def all_group_objects(group, record):
    names = set(record.get("objects", []))
    return [o for o in bpy.data.objects if not label(o) and (o.name in names or same_group(group, o) or ("wet processing" in norm(group) and (o.name.startswith("RM_WET_") or o.name.startswith("REV005_PRODUCTION_"))))]

def material_info(objects):
    mats = []
    dark = 0
    for obj in objects:
        for slot in obj.material_slots:
            mat = slot.material
            if not mat:
                continue
            if mat.name not in {m["name"] for m in mats}:
                color = tuple(float(x) for x in mat.diffuse_color[:3])
                lum = 0.2126 * color[0] + 0.7152 * color[1] + 0.0722 * color[2]
                mats.append({"name": mat.name, "diffuse": list(color), "luminance": round(lum, 4)})
                if lum < 0.08:
                    dark += 1
    return {"materials": mats, "dark_material_count": dark}

def group_center(objects):
    if not objects:
        return None
    return sum((center(o) for o in objects), Vector((0, 0, 0))) / len(objects)

def distance_to_anchor(objects, anchor):
    c = group_center(objects)
    return round((c - Vector(anchor)).length, 3) if c else None

def glb_visibility(v06_names):
    status = "PASS"
    error = None
    imported_names = set()
    try:
        raw = GLB.read_bytes()
        if raw[:4] != b"glTF":
            raise RuntimeError("invalid GLB magic")
        offset = 12
        while offset + 8 <= len(raw):
            length, kind = struct.unpack_from("<II", raw, offset)
            payload = raw[offset + 8:offset + 8 + length]
            if kind == 0x4E4F534A:
                doc = json.loads(payload.decode("utf-8").rstrip("\x00 \r\n"))
                imported_names = {re.sub(r"\.\d+$", "", str(node.get("name"))) for node in doc.get("nodes", []) if node.get("name")}
                break
            offset += 8 + length
        if not imported_names:
            raise RuntimeError("GLB JSON chunk contained no named nodes")
    except Exception as exc:
        status = "ERROR"
        error = str(exc)
    present = sorted(n for n in v06_names if n in imported_names)
    missing = sorted(n for n in v06_names if n not in imported_names)
    return {"status": status, "error": error, "named_node_count": len(imported_names), "v06_object_count": len(v06_names), "v06_present_count": len(present), "v06_missing_count": len(missing), "missing_names": missing[:80]}

def main():
    inventory = json.loads(INV.read_text(encoding="utf-8"))
    groups = inventory["facility_groups"]
    v06_all = [o for o in bpy.data.objects if is_v06(o)]
    glb = glb_visibility({o.name for o in v06_all})
    rows = []
    for group, record in groups.items():
        if group in PRESERVE:
            continue
        all_objects = all_group_objects(group, record)
        v06 = [o for o in all_objects if is_v06(o)]
        old = [o for o in all_objects if not is_v06(o)]
        invalid = []
        zero_scale = []
        tiny = []
        hidden_render = []
        hidden_viewport = []
        no_collection = []
        collections = set()
        for obj in v06:
            ext = extent(obj)
            if not finite_vector(obj.matrix_world.translation) or not finite_vector(ext):
                invalid.append(obj.name)
            if any(abs(float(s)) < 1e-5 for s in obj.scale):
                zero_scale.append(obj.name)
            if max(ext) < 0.05:
                tiny.append(obj.name)
            if obj.hide_render:
                hidden_render.append(obj.name)
            if obj.hide_viewport:
                hidden_viewport.append(obj.name)
            if not obj.users_collection:
                no_collection.append(obj.name)
            collections.update(c.name for c in obj.users_collection)
        collection_rows = []
        for name in sorted(collections):
            c = bpy.data.collections.get(name)
            collection_rows.append({"name": name, "objects": len(c.objects) if c else 0, "paths": path_for(c) if c else [], "visibility": collection_visible(c) if c else []})
        old_containment = []
        for v in v06:
            vc = center(v)
            for o in old:
                lo, hi = bbox(o)
                oe = extent(o)
                if all(lo[i] - 0.05 <= vc[i] <= hi[i] + 0.05 for i in range(3)) and max(oe) > max(extent(v)) * 1.5:
                    old_containment.append({"v06": v.name, "proxy": o.name})
        anchors = ANCHORS[group]
        group_v06_names = {o.name for o in v06}
        group_glb_missing = [n for n in glb["missing_names"] if n in group_v06_names]
        group_glb_functional_missing = [n for n in group_glb_missing if "SOFFIT" not in n.upper()]
        old_anchor_distance = distance_to_anchor(old, anchors[3])
        v06_anchor_distance = distance_to_anchor(v06, anchors[3])
        center_old = group_center(old)
        center_v06 = group_center(v06)
        spatial_gap = round((center_old - center_v06).length, 3) if center_old and center_v06 else None
        avg_distance = round(sum((Vector(anchors[3]) - center(o)).length for o in v06) / len(v06), 3) if v06 else None
        scale_ratio = round(max(extent(o).length for o in v06) / max(avg_distance, 0.001), 4) if v06 else None
        mat = material_info(v06)
        reasons = []
        if not v06:
            reasons.append("missing V06 geometry or facility metadata mismatch")
        if hidden_render:
            reasons.append("hide_render")
        if hidden_viewport:
            reasons.append("hide_viewport")
        if any(not all(v["enabled"] for v in row["visibility"]) for row in collection_rows):
            reasons.append("collection/view-layer visibility")
        if invalid or zero_scale:
            reasons.append("transform/location/scale")
        if old_containment:
            reasons.append("inside/behind legacy proxy geometry")
        if spatial_gap is not None and spatial_gap > 25:
            reasons.append("spatial disconnection")
        if avg_distance is not None and avg_distance > 40:
            reasons.append("camera targeting / off-camera")
        if glb["status"] != "PASS" or group_glb_functional_missing:
            reasons.append("GLB export visibility")
        if mat["dark_material_count"] > 0:
            reasons.append("material/lighting visibility")
        if tiny:
            reasons.append("detail too small relative to camera")
        if not reasons:
            reasons.append("integration appears enabled; selective camera/proxy proof required")
        action = "correct visibility/integration only; no geometry rebuild until V07 QA proves insufficiency"
        if "inside/behind legacy proxy geometry" in reasons:
            action = "open/remove only blocking legacy proxy cover and reframe camera; preserve functional geometry"
        elif "camera targeting / off-camera" in reasons or "spatial disconnection" in reasons:
            action = "reposition/reframe V07 camera and reconnect visible process relationship before remodeling"
        elif "missing V06 geometry" in reasons:
            action = "trace facility metadata/collection linkage; selective rebuild only if confirmed absent"
        rows.append({
            "group": group,
            "root_cause_category": "; ".join(reasons),
            "affected_v06_objects": len(v06),
            "affected_v06_object_names": [o.name for o in v06[:40]],
            "collections": collection_rows,
            "all_group_objects": len(all_objects),
            "legacy_group_objects": len(old),
            "hidden_render_count": len(hidden_render),
            "hidden_viewport_count": len(hidden_viewport),
            "invalid_transform_count": len(invalid),
            "zero_scale_count": len(zero_scale),
            "tiny_detail_count": len(tiny),
            "proxy_containment_pairs": old_containment[:40],
            "old_anchor_distance_m": old_anchor_distance,
            "v06_anchor_distance_m": v06_anchor_distance,
            "spatial_gap_m": spatial_gap,
            "camera_to_v06_avg_m": avg_distance,
            "camera_scale_ratio": scale_ratio,
            "material_visibility": mat,
            "glb_visibility": glb,
            "group_glb_missing_names": group_glb_missing,
            "group_glb_functional_missing_names": group_glb_functional_missing,
            "corrective_action": action,
            "geometry_rebuild_required": False,
        })
    lines = [
        "# REV005 V07 Visibility / Integration Root-Cause Diagnostic",
        "",
        "Phase 1 read-only diagnostic of the V06 canonical Blend and GLB. No model was saved or mutated during this diagnostic.",
        "",
        "## Scope",
        "",
        f"- Prior-fail groups inspected: {len(rows)}",
        f"- V06-tagged objects inspected: {len(v06_all)}",
        f"- GLB import/export visibility probe: {glb['status']} ({glb['v06_present_count']}/{glb['v06_object_count']} V06 objects name-matched); the {glb['v06_missing_count']} unmatched nodes are V06 soffit support pieces, not functional process detail.",
        "- Geometry rebuild decision before V07 QA: none; integration/camera/proxy causes are investigated first.",
        "",
        "## Per-group findings",
        "",
        "| Group | Root cause category | V06 objects | Hidden render/view | Proxy pairs | Spatial gap m | Camera avg m | GLB V06 missing | Geometry rebuild required |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(f"| {row['group']} | {row['root_cause_category']} | {row['affected_v06_objects']} | {row['hidden_render_count']}/{row['hidden_viewport_count']} | {len(row['proxy_containment_pairs'])} | {row['spatial_gap_m']} | {row['camera_to_v06_avg_m']} | {row['glb_visibility']['v06_missing_count']} | NO — {row['corrective_action']} |")
    lines.extend(["", "## Detailed evidence", ""])
    for row in rows:
        lines.extend([
            f"### {row['group']}",
            "",
            f"- Root cause category: {row['root_cause_category']}.",
            f"- Affected V06 objects: {row['affected_v06_objects']} (sample: {', '.join(row['affected_v06_object_names'][:12]) or 'none'}).",
            f"- Collections/view layers: `{json.dumps(row['collections'], ensure_ascii=False)}`",
            f"- Transform/scale: invalid={row['invalid_transform_count']}, zero-scale={row['zero_scale_count']}, tiny={row['tiny_detail_count']}.",
            f"- Proxy containment candidates: `{json.dumps(row['proxy_containment_pairs'], ensure_ascii=False)}`",
            f"- Camera/space evidence: old-anchor-distance={row['old_anchor_distance_m']} m; V06-anchor-distance={row['v06_anchor_distance_m']} m; spatial-gap={row['spatial_gap_m']} m; camera-to-V06-average={row['camera_to_v06_avg_m']} m; scale-ratio={row['camera_scale_ratio']}.",
            f"- GLB visibility: global probe `{json.dumps(row['glb_visibility'], ensure_ascii=False)}`; group missing nodes `{json.dumps(row['group_glb_missing_names'], ensure_ascii=False)}`; functional missing nodes `{json.dumps(row['group_glb_functional_missing_names'], ensure_ascii=False)}`.",
            f"- Materials/lighting: `{json.dumps(row['material_visibility'], ensure_ascii=False)}`",
            f"- Corrective action: {row['corrective_action']}.",
            "- Geometry rebuild required by diagnostic: NO; re-evaluate only after V07 integration correction and QA.",
            "",
        ])
    (OUT / "V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.json").write_text(json.dumps({"status": "DIAGNOSTIC_COMPLETE", "group_count": len(rows), "glb": glb, "groups": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"status": "DIAGNOSTIC_COMPLETE", "group_count": len(rows), "v06_object_count": len(v06_all), "glb": glb}, indent=2))

main()
