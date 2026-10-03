import json
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree


ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "output/rev005-facility-gated/F08_F15_combined"
STAGE = OUT / "REV005_F08_F15_STAGED.blend"
INDEX = OUT / "M08_47_EVIDENCE_INDEX.json"
REPORT = OUT / "M08_47_SOLID_CAMERA_VALIDATION.json"
RAYS = [Vector((0.811, 0.317, 0.491)).normalized(),
        Vector((-0.271, 0.913, 0.303)).normalized(),
        Vector((0.419, -0.503, 0.756)).normalized()]
EPS = 1e-5


def point_in_bounds(point, corners):
    xs = [v.x for v in corners]
    ys = [v.y for v in corners]
    zs = [v.z for v in corners]
    return (min(xs)-EPS <= point.x <= max(xs)+EPS and
            min(ys)-EPS <= point.y <= max(ys)+EPS and
            min(zs)-EPS <= point.z <= max(zs)+EPS)


def parity_inside(tree, point, direction):
    count = 0
    origin = point.copy()
    for _ in range(512):
        loc, normal, face, distance = tree.ray_cast(origin, direction, 100000.0)
        if loc is None:
            break
        count += 1
        origin = loc + direction * EPS
    else:
        raise RuntimeError("ray intersection limit reached")
    return count % 2 == 1


def main():
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    bpy.ops.wm.open_mainfile(filepath=str(STAGE))
    depsgraph = bpy.context.evaluated_depsgraph_get()
    facilities = {}
    errors = []
    for fid, record in index["facilities"].items():
        col = bpy.data.collections.get(record["collection"])
        if col is None:
            raise RuntimeError(f"missing target collection {fid}: {record['collection']}")
        solids, nonwatertight = [], []
        for obj in col.objects:
            if obj.type != "MESH":
                continue
            evaluated = obj.evaluated_get(depsgraph)
            mesh = evaluated.to_mesh()
            try:
                world = evaluated.matrix_world
                verts = [world @ v.co for v in mesh.vertices]
                faces = [list(p.vertices) for p in mesh.polygons if len(p.vertices) >= 3]
                corners = [world @ Vector(corner) for corner in obj.bound_box]
                bm = bmesh.new()
                bm.from_mesh(mesh)
                manifold = bool(bm.edges) and all(edge.is_manifold for edge in bm.edges)
                bm.free()
                if manifold and faces:
                    tree = BVHTree.FromPolygons(verts, faces, all_triangles=False, epsilon=0.0)
                    solids.append((obj.name, corners, tree))
                else:
                    nonwatertight.append((obj.name, corners))
            finally:
                evaluated.to_mesh_clear()
        view_results = []
        for view in record["views"]:
            point = Vector(view["camera_world"])
            inside, boundary = [], []
            for name, corners, tree in solids:
                if not point_in_bounds(point, corners):
                    continue
                near = tree.find_nearest(point, EPS)
                if near[0] is not None and near[3] <= EPS:
                    boundary.append(name)
                    continue
                tests = [parity_inside(tree, point, ray) for ray in RAYS]
                if sum(tests) >= 2:
                    inside.append(name)
            conservative = [name for name, corners in nonwatertight if point_in_bounds(point, corners)]
            result = {"role": view["role"], "camera_world": view["camera_world"],
                      "watertight_meshes_tested": len(solids),
                      "nonwatertight_meshes_aabb_containment_candidates": conservative,
                      "inside_solid_meshes": inside, "on_solid_mesh_boundary": boundary,
                      "camera_origin_clear": not (inside or boundary or conservative)}
            view_results.append(result)
            if not result["camera_origin_clear"]:
                errors.append({"facility": fid, **result})
        facilities[fid] = {"collection": record["collection"],
                            "watertight_meshes_built": len(solids),
                            "nonwatertight_meshes_conservatively_checked": len(nonwatertight),
                            "views": view_results}
    report = {"schema": "M08_47_SOLID_CAMERA_VALIDATION_V1",
              "method": "world-space BVH point-to-solid containment by parity of three non-axis-aligned ray casts; boundary proximity rejected; nonwatertight meshes use conservative per-object AABB containment",
              "epsilon": EPS, "camera_count": sum(len(v["views"]) for v in index["facilities"].values()),
              "result": "PASS" if not errors else "BLOCKED_CAMERA_ORIGIN_INTERSECTION",
              "errors": errors, "facilities": facilities}
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"result": report["result"], "camera_count": report["camera_count"],
                      "errors": errors, "report": str(REPORT)}, indent=2))


main()
