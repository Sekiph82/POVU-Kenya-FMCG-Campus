import bpy, json, math
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[4]
BLEND=ROOT/"3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT=ROOT/"output/rev005-interior-remediation-v02/qa"
V2="REV005_INTERIOR_REMEDIATION_V02"
FOCUSED={
"01_blow_molding":("Bottle Blow Molding",(52,10,3),(34,-4,13),(40,-2,8),(36,0,14),(28,20,20)),
"02_caps_triggers":("Caps and Trigger Assembly",(52,31,3),(34,17,13),(38,24,9),(36,20,14),(28,40,20)),
"03_liquid_filling":("Liquid Filling / Packaging",(10,-2,3),(-15,-14,10),(-2,-14,9),(28,-12,13),(-20,12,18)),
"04_micro_weigh":("Micro-ingredient Weigh / Dispense",(-5,50,3),(-18,40,10),(-12,45,9),(-20,40,12),(-25,60,17)),
"05_toothpaste":("Toothpaste Production",(-12,43,3),(-30,33,10),(-22,36,9),(-25,35,12),(-30,55,18)),
"06_wet_wipes":("Wet Wipes Production",(22,43,3),(4,33,10),(14,36,9),(5,35,12),(0,55,18)),
"07_glass_deck":("Central Glass Deck Command / Training / Café Gallery",(70,24,11),(58,0,15),(60,10,15),(58,0,16),(55,48,18)),
}
PROCESS_TARGETS={"07_glass_deck":(70,5,11)}
REG={
"regression_01_restaurant_cafe":("Restaurant / POVU Café / kitchen",(5,-69,2.5),(-25,-98,15),(24,-92,9),["REV005_RESTAURANT","REV005_CAFE","REV005_KITCHEN","REV005_DINING"]),
"regression_02_daycare":("Daycare / crèche",(-105,-64,2.5),(-128,-45,12),(-102,-45,8),["REV005_DAYCARE"]),
}

def box_mesh(name,loc,dims,mat):
 x,y,z=[v/2 for v in dims]; vs=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]; fs=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]; me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(vs,[],fs); me.update(); o=bpy.data.objects.new(name,me); bpy.context.scene.collection.objects.link(o); o.location=loc; o.data.materials.append(mat); return o

def cam(name,loc,target):
 bpy.ops.object.camera_add(location=loc); o=bpy.context.object; o.name=name; o.data.lens=42; o.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat("-Z","Y").to_euler(); return o

def main():
 OUT.mkdir(parents=True,exist_ok=True); v2=bpy.data.collections.get(V2); scene=bpy.context.scene
 for o in bpy.data.objects: o.hide_render=True
 scene.render.engine="BLENDER_WORKBENCH"; scene.render.resolution_x=760; scene.render.resolution_y=500; scene.render.resolution_percentage=100; scene.render.image_settings.file_format="PNG"; scene.render.film_transparent=False; scene.display.shading.light="STUDIO"; scene.display.shading.color_type="MATERIAL"; scene.display.shading.show_shadows=True; scene.display.shading.show_cavity=True; scene.display.shading.cavity_type="WORLD"; scene.display.shading.curvature_ridge_factor=1.8; scene.display.shading.curvature_valley_factor=1.2
 neutral=bpy.data.materials.get("REV005_V02_WHITE") or bpy.data.materials.new("V02_QA_FLOOR")
 results=[]
 for key,(fac,center,wide,detail,process,floor_center) in FOCUSED.items():
  objs=[o for o in v2.objects if o.get("facility")==fac] if v2 else []
  for o in objs: o.hide_render=False
  floor=box_mesh("V02_QA_FLOOR_"+key,(center[0],center[1],1.18),(26 if key!="07_glass_deck" else 9,20 if key!="07_glass_deck" else 46,.12),neutral)
  for label,loc,tgt in (("A_WIDE",wide,center),("B_FUNCTIONAL",detail,center),("C_PROCESS",process,PROCESS_TARGETS.get(key,center))):
   cc=cam("V02_QA_"+key+"_"+label,loc,tgt); scene.camera=cc; p=OUT/(key+"_"+label+".png"); scene.render.filepath=str(p); bpy.ops.render.render(write_still=True); results.append({"kind":"focused","target":fac,"view":label,"path":str(p),"bytes":p.stat().st_size if p.exists() else 0,"status":"PASS" if p.exists() and p.stat().st_size>5000 else "FAIL"}); bpy.data.objects.remove(cc,do_unlink=True)
  bpy.data.objects.remove(floor,do_unlink=True)
  for o in objs: o.hide_render=True
 for key,(fac,center,wide,detail,prefixes) in REG.items():
  objs=[]
  for o in bpy.data.objects:
   if (o.get("facility")==fac or any(o.name.startswith(p) for p in prefixes)) and not any(k in o.name for k in ["KITCHEN_PARTITION","NAP_PARTITION"]): objs.append(o)
  for o in objs: o.hide_render=False
  floor=box_mesh("V02_QA_FLOOR_"+key,(center[0],center[1],1.18),(30,24,.12),neutral)
  for label,loc,tgt in (("A_WIDE",wide,center),("B_FUNCTIONAL",detail,center)):
   cc=cam("V02_QA_"+key+"_"+label,loc,tgt); scene.camera=cc; p=OUT/(key+"_"+label+".png"); scene.render.filepath=str(p); bpy.ops.render.render(write_still=True); results.append({"kind":"regression","target":fac,"view":label,"path":str(p),"bytes":p.stat().st_size if p.exists() else 0,"status":"PASS" if p.exists() and p.stat().st_size>5000 else "FAIL"}); bpy.data.objects.remove(cc,do_unlink=True)
  bpy.data.objects.remove(floor,do_unlink=True)
  for o in objs: o.hide_render=True
 (OUT.parent/"RENDER_RESULTS.json").write_text(json.dumps(results,indent=2),encoding="utf-8"); print(json.dumps({"renders":len(results),"passes":sum(r["status"]=="PASS" for r in results),"focused":sum(r["kind"]=="focused" for r in results),"regression":sum(r["kind"]=="regression" for r in results)},indent=2))
main()
