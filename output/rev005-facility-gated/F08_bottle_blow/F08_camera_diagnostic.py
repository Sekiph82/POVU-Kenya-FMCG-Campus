import bpy
from mathutils import Vector
for name in ['Production_Hall','F08_WEST_WALL','F08_SOUTH_GLAZING_PANEL_0','F08_ROOM_FINISHED_FLOOR']:
 o=bpy.data.objects.get(name)
 if o:
  pts=[o.matrix_world@Vector(v) for v in o.bound_box]
  print(name,[round(min(p[i] for p in pts),3) for i in range(3)],[round(max(p[i] for p in pts),3) for i in range(3)])
for xyz in [(35,-3.5,6),(38,-3.5,6),(32,-3.5,6),(35,2.5,6),(38,2.5,6),(32,2.5,6)]:
 hits=[]
 for o in bpy.data.objects:
  if o.type!='MESH':continue
  pts=[o.matrix_world@Vector(v) for v in o.bound_box];lo=[min(p[i] for p in pts) for i in range(3)];hi=[max(p[i] for p in pts) for i in range(3)]
  if all(lo[i]<=xyz[i]<=hi[i] for i in range(3)):hits.append(o.name)
 print('CAM',xyz,'inside',hits[:10])
