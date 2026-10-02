import bpy,json
from mathutils import Vector
from pathlib import Path
for name in ['Production_Hall','PRODUCTION_ROOF','F08_NORTH_BACK_WALL','F08_ROOM_FINISHED_FLOOR','F08_SOUTH_GLAZING_PANEL_0']:
 o=bpy.data.objects.get(name)
 if not o:continue
 pts=[o.matrix_world@Vector(v) for v in o.bound_box];lo=[min(float(p[i]) for p in pts) for i in range(3)];hi=[max(float(p[i]) for p in pts) for i in range(3)];print('OBJECT_BOUNDS',name,lo,hi)
for xyz in [(52,2,6),(52,2,6.01),(52,2,6.2),(52,2,6.5),(40,2,6.5),(55,2,6.5),(52,18,6.5)]:
 hits=[]
 for o in bpy.data.objects:
  if o.type!='MESH':continue
  pts=[o.matrix_world@Vector(v) for v in o.bound_box];lo=[min(float(p[i]) for p in pts) for i in range(3)];hi=[max(float(p[i]) for p in pts) for i in range(3)]
  if all(lo[i]<=xyz[i]<=hi[i] for i in range(3)):hits.append(o.name)
 print('POINT_HITS',xyz,hits[:20], 'count',len(hits))
