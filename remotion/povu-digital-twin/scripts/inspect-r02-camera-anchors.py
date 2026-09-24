import bpy
import sys
from pathlib import Path
from mathutils import Vector

root = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
queries = [
    "ADMIN_HQ_ENTRANCE_SIGNAGE", "ADMIN_HQ_ENTRANCE_CANOPY", "ADMIN_HQ_ENTRANCE_DOOR_L",
    "R_D_QC_ENTRANCE_SIGNAGE", "R_D_QC_ENTRANCE_CANOPY", "GREEN_ROOF_Admin_RD_QC",
    "MULTIPURPOSE_STUDIO", "EXPERIENCE_LINK", "EXPERIENCE_ROOF",
    "CAFE_GLASS_FRONT", "CAFE_TERRACE", "RESTAURANT_ENTRANCE_SIGNAGE",
    "WELLNESS_PAVILION", "RECREATION_COURT", "WELLNESS_ENTRANCE_SIGNAGE",
    "Daycare", "DAYCARE_GARDEN", "DAYCARE_ENTRANCE_SIGNAGE", "CLINIC_ENTRY",
    "PRES_38_RESTAURANT_CAFE", "PRES_39_WELLNESS_RECREATION", "PRES_40_DAYCARE", "PRES_41_CLINIC",
    "PRES_42_EMPLOYEE_GARDENS", "PRES_HANDS_OF_GROWTH",
    "GLASS_DECK_EAST_STAIR", "GLASS_DECK_WEST_STAIR", "GLASS_DECK_CENTRAL_STAIR",
    "PRES_GLASS_DECK_EAST_ACCESS", "PRES_GLASS_DECK_CENTRAL_ACCESS", "PRES_GLASS_DECK_WEST_ACCESS",
]

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(root / "3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb"))

def world_center(obj):
    bpy.context.view_layer.update()
    points = []
    if obj.type == "MESH":
        points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    else:
        points = [obj.matrix_world.translation]
    if not points:
        return obj.matrix_world.translation
    center = sum(points, points[0].copy()) * (1.0 / (len(points) + 1)) if len(points) > 1 else points[0]
    return center

by_name = {obj.name.upper(): obj for obj in bpy.data.objects}
for query in queries:
    obj = by_name.get(query.upper())
    if obj is None:
        print(f"MISSING\t{query}")
        continue
    c = world_center(obj)
    print(f"FOUND\t{obj.name}\ttype={obj.type}\tworld={tuple(round(v,2) for v in c)}\tloc={tuple(round(v,2) for v in obj.location)}")
