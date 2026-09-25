import bpy
from mathutils import Vector

target = Vector((-102.0, -89.0, 5.0))
for obj in sorted(bpy.data.objects, key=lambda o: o.name.lower()):
    if obj.type != "MESH":
        continue
    if not any(t in obj.name.upper() for t in ("TREE", "ICOSPHERE", "CANOPY")):
        continue
    d = obj.matrix_world.translation - target
    if abs(d.x) <= 35 and abs(d.y) <= 35:
        print(obj.name, [round(float(v), 2) for v in obj.matrix_world.translation], "distance", round(float(d.length), 2))
