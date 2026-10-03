import bpy,json
from mathutils import Vector
for n in ('Production_Hall','PRODUCTION_ROOF'):
 o=bpy.data.objects.get(n)
 if not o: print('MISSING',n);continue
 pts=[o.matrix_world@Vector(c) for c in o.bound_box]
 print('OBJECT',n,'TYPE',o.type,'BOUNDS',[[round(min(p[i] for p in pts),4),round(max(p[i] for p in pts),4)] for i in range(3)],'loc',tuple(o.location),'dims',tuple(o.dimensions))
