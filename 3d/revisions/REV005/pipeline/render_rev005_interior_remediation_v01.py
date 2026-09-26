import bpy, json, math, shutil
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[4]
BLEND=ROOT/"3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
OUT=ROOT/"output/rev005-interior-remediation-v01/qa"
REM="REV005_INTERIOR_REMEDIATION_V01"

TARGETS={
"01_bottle_blow_molding":("Bottle Blow Molding",(52,10,3),(34,-4,13),(38,0,10)),
"02_caps_trigger_assembly":("Caps and Trigger Assembly",(52,31,3),(34,17,13),(38,21,10)),
"03_electrical_lv_mv":("Electrical / LV-MV Room",(111,61,3),(99,52,10),(102,53,10)),
"04_employee_welfare":("Employee Changing / Shower / Locker Support",(31,-70,3),(18,-83,10),(17,-83,10)),
"05_fire_pump_house":("Fire Pump House",(76,72,3),(62,60,11),(69,62,8)),
"06_glass_deck_core":("Central Glass Deck Command / Training / Café Gallery",(70,24,11),(58,0,15),(60,8,16)),
"07_liquid_filling_packaging":("Liquid Filling / Packaging",(10,-2,3),(-15,-14,10),(-2,-14,11)),
"08_micro_weigh_dispense":("Micro-ingredient Weigh / Dispense",(-5,50,3),(-18,40,10),(-20,43,10)),
"09_powder_handling_packing":("Powder Handling / Packing",(-48,43,3),(-66,32,11),(-58,34,9)),
"10_wet_processing":("Production Hall / Wet Processing",(2,24,4),(-55,2,16),(-28,4,14)),
"11_security_reception":("Security / Reception / Visitor Arrival",(-58,-84,3),(-76,-96,10),(-75,-95,10)),
"12_security_gatehouse":("Security Gatehouse",(96,-106,3),(84,-114,9),(86,-115,10)),
"13_toothpaste_production":("Toothpaste Production",(-12,43,3),(-30,33,10),(-28,33,10)),
"14_wet_wipes_production":("Wet Wipes Production",(22,43,3),(4,33,10),(5,33,10)),
}

def mesh_box(name,loc,dims,material):
    x,y,z=[v/2 for v in dims]; vs=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]; fs=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]
    me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(vs,[],fs); me.update(); o=bpy.data.objects.new(name,me); bpy.context.scene.collection.objects.link(o); o.location=loc; o.data.materials.append(material); return o

def camera(name,loc,target):
    bpy.ops.object.camera_add(location=loc); c=bpy.context.object; c.name=name; c.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat("-Z","Y").to_euler(); c.data.lens=52; return c

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    rem=bpy.data.collections.get(REM)
    for o in bpy.data.objects: o.hide_render=True
    scene=bpy.context.scene; scene.render.engine="BLENDER_WORKBENCH"; scene.render.resolution_x=720; scene.render.resolution_y=480; scene.render.resolution_percentage=100; scene.render.image_settings.file_format="PNG"; scene.render.film_transparent=False
    scene.display.shading.light="STUDIO"; scene.display.shading.color_type="MATERIAL"; scene.display.shading.show_shadows=True; scene.display.shading.show_cavity=True; scene.display.shading.cavity_type="WORLD"; scene.display.shading.curvature_ridge_factor=1.8; scene.display.shading.curvature_valley_factor=1.2
    results=[]
    for key,(fac,center,wide,detail) in TARGETS.items():
        target=[o for o in rem.objects if o.get("facility")==fac] if rem else []
        for o in target: o.hide_render=False
        floor=mesh_box("QA_FLOOR_"+key,(center[0],center[1],1.20),(26 if key!="10_wet_processing" else 70,20 if key!="10_wet_processing" else 42,0.12),bpy.data.materials.get("REV005_RM_CLEAN_WHITE"))
        for label,loc,tgt in (("A_WIDE",wide,center),("B_FUNCTIONAL",detail,center)):
            cam=camera("QA_"+key+"_"+label,loc,tgt); scene.camera=cam; path=OUT/(key+"_"+label+".png"); scene.render.filepath=str(path); bpy.ops.render.render(write_still=True); results.append({"target":fac,"view":label,"path":str(path),"bytes":path.stat().st_size if path.exists() else 0,"status":"PASS" if path.exists() and path.stat().st_size>5000 else "FAIL"})
            bpy.data.objects.remove(cam,do_unlink=True)
        bpy.data.objects.remove(floor,do_unlink=True)
        for o in target: o.hide_render=True
    (OUT.parent/"RENDER_RESULTS.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
    print(json.dumps({"rendered":len(results),"pass":sum(r["status"]=="PASS" for r in results),"out":str(OUT)},indent=2))

main()
