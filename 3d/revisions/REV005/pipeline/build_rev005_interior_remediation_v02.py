import bpy, hashlib, json, math
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[4]
REV=ROOT/"3d/revisions/REV005"
BLEND=REV/"POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB=REV/"POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
OUT=ROOT/"output/rev005-interior-remediation-v02"
COL="REV005_INTERIOR_REMEDIATION_V02"
FOCUSED={"Bottle Blow Molding","Caps and Trigger Assembly","Liquid Filling / Packaging","Micro-ingredient Weigh / Dispense","Toothpaste Production","Wet Wipes Production","Central Glass Deck Command / Training / Café Gallery"}

def sha(p):
 h=hashlib.sha256();
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest().upper()

def material(name,color,metal=0.0,rough=.42):
 m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True; bs=m.node_tree.nodes.get("Principled BSDF")
 if bs: bs.inputs["Base Color"].default_value=(*color,1); bs.inputs["Metallic"].default_value=metal; bs.inputs["Roughness"].default_value=rough
 return m

M={
 "steel":material("REV005_V02_STEEL",(.2,.27,.31),.85,.25), "stainless":material("REV005_V02_STAINLESS",(.62,.68,.7),.9,.18),
 "blue":material("REV005_V02_BLUE",(.02,.22,.62),.35,.28), "teal":material("REV005_V02_TEAL",(.02,.52,.62),.35,.25),
 "orange":material("REV005_V02_ORANGE",(.95,.25,.03),.2,.3), "yellow":material("REV005_V02_YELLOW",(.98,.62,.02),.1,.35),
 "green":material("REV005_V02_GREEN",(.04,.5,.25),.2,.3), "purple":material("REV005_V02_PURPLE",(.58,.08,.4),.25,.3),
 "white":material("REV005_V02_WHITE",(.86,.89,.9),.08,.32), "dark":material("REV005_V02_DARK",(.012,.02,.03),.2,.2),
 "wood":material("REV005_V02_WOOD",(.42,.2,.06),0,.5), "glass":material("REV005_V02_GLASS",(.12,.52,.7),.4,.12),
}

c=bpy.data.collections.get(COL)
if c:
 for o in list(c.objects): bpy.data.objects.remove(o,do_unlink=True)
else:
 c=bpy.data.collections.new(COL); bpy.context.scene.collection.children.link(c)

def link(o,facility):
 for cc in list(o.users_collection): cc.objects.unlink(o)
 c.objects.link(o); o["REV005_REMEDIATION_V02"]=True; o["facility"]=facility; return o

def mesh(name,verts,faces,loc,mat,facility):
 me=bpy.data.meshes.new(name+"_MESH"); me.from_pydata(verts,[],faces); me.update(); o=link(bpy.data.objects.new(name,me),facility); o.location=loc; o.data.materials.append(M[mat]); return o

def box(name,loc,dims,mat,facility):
 x,y,z=[v/2 for v in dims]; vs=[(-x,-y,-z),(x,-y,-z),(x,y,-z),(-x,y,-z),(-x,-y,z),(x,-y,z),(x,y,z),(-x,y,z)]; fs=[(0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),(2,6,7,3),(4,0,3,7)]; return mesh(name,vs,fs,loc,mat,facility)

def cyl(name,loc,r,d,mat,facility,n=24):
 vs=[]
 for z in (-d/2,d/2):
  for i in range(n): a=math.tau*i/n; vs.append((r*math.cos(a),r*math.sin(a),z))
 fs=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,n+(i+1)%n,n+i) for i in range(n)]
 return mesh(name,vs,fs,loc,mat,facility)

def cone(name,loc,r1,r2,d,mat,facility,n=24):
 vs=[]
 for z,r in ((-d/2,r1),(d/2,r2)):
  for i in range(n): a=math.tau*i/n; vs.append((r*math.cos(a),r*math.sin(a),z))
 fs=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,n+(i+1)%n,n+i) for i in range(n)]
 return mesh(name,vs,fs,loc,mat,facility)

def pipe(name,a,b,r,mat,facility):
 a,b=Vector(a),Vector(b); d=b-a; o=cyl(name,(a+b)/2,r,d.length,mat,facility,16); o.rotation_euler=d.to_track_quat("Z","Y").to_euler(); return o

def belt(name,x,y,length,width,facility,mat="steel"):
 box(name+"_FRAME",(x,y,1.35),(length,width,.26),mat,facility)
 for i in range(7):
  xx=x-length/2+.6+i*(length-1.2)/6; q=cyl(name+f"_ROLLER_{i}",(xx,y,1.52),width*.42,.11,"dark",facility,16); q.rotation_euler[1]=math.pi/2
 box(name+"_SIDE_A",(x,y-width/2,1.75),(length,.09,.65),"yellow",facility); box(name+"_SIDE_B",(x,y+width/2,1.75),(length,.09,.65),"yellow",facility)

def hide_v01_focused():
 v1=bpy.data.collections.get("REV005_INTERIOR_REMEDIATION_V01")
 if v1:
  for o in v1.objects:
   if o.get("facility") in FOCUSED: o.hide_viewport=True; o.hide_render=True

def blow():
 f="Bottle Blow Molding"; x,y=52,10
 # preform heater tunnel, clamp/mould stack, stretch rod, bottle outfeed
 box("V02_BLOW_HEATER_TUNNEL",(x-10,y,3.4),(3.4,3.8,4.4),"orange",f)
 for i in range(5): box(f"V02_BLOW_HEATER_BANK_{i}",(x-10,y-2.0+i*.9,3.4),(.22,.55,3.3),"yellow",f)
 box("V02_BLOW_CLAMP_FRAME",(x-5,y,3.7),(4.4,4.2,5.0),"blue",f)
 box("V02_BLOW_MOULD_LEFT",(x-5.8,y-2.2,3.1),(1.7,.35,2.8),"stainless",f); box("V02_BLOW_MOULD_RIGHT",(x-4.2,y-2.2,3.1),(1.7,.35,2.8),"stainless",f)
 pipe("V02_BLOW_STRETCH_ROD",(x-5,y-2.5,5.4),(x-5,y-2.5,2.2),.16,"teal",f)
 box("V02_BLOW_PREFORM_HOPPER",(x-1,y+2.1,3.2),(2.8,2.6,3.8),"steel",f); cone("V02_BLOW_HOPPER_CONE",(x-1,y+2.1,5.35),1.3,.35,1.0,"stainless",f)
 pipe("V02_BLOW_PREFORM_FEED",(x-1,y+2.1,5.8),(x-3,y+.8,5.6),.2,"teal",f)
 belt("V02_BLOW_BOTTLE_OUTFEED",x+6,y-0.3,12,1.9,f,"stainless")
 for i in range(7):
  xx=x+1+i*1.5; cyl(f"V02_BLOW_FORMED_BOTTLE_{i}",(xx,y-.3,2.1),.32,1.25,"teal",f,20); cyl(f"V02_BLOW_BOTTLE_NECK_{i}",(xx,y-.3,2.9),.12,.35,"white",f,16)

def caps():
 f="Caps and Trigger Assembly"; x,y=52,31
 # distinct bowl feeder, trigger magazine, pick heads and cap/trigger assembly carousel
 cyl("V02_CAPS_BOWL_FEEDER",(x-9,y+2.2,2.0),2.5,.45,"stainless",f,32); cyl("V02_CAPS_BOWL_RIM",(x-9,y+2.2,2.35),2.2,.16,"yellow",f,32)
 pipe("V02_CAPS_BOWL_TRACK",(x-7,y+2.2,2.4),(x-4,y+.8,2.4),.2,"yellow",f)
 box("V02_TRIGGER_MAGAZINE",(x-8,y-2.2,3.0),(2.8,2.0,3.8),"purple",f)
 for i in range(5): box(f"V02_TRIGGER_SLOT_{i}",(x-8,y-3.25+i*.5,3.0),(1.8,.12,2.7),"teal",f)
 box("V02_CAP_TRIGGER_CAROUSEL",(x+1,y,2.0),(5.0,3.4,.35),"blue",f)
 for i in range(6):
  a=math.tau*i/6; px=x+1+1.8*math.cos(a); py=y+1.1*math.sin(a); cyl(f"V02_ASSEMBLY_NEST_{i}",(px,py,2.45),.34,.35,"yellow",f,20); cyl(f"V02_CAP_COMPONENT_{i}",(px,py,2.8),.22,.38,"white",f,20); box(f"V02_TRIGGER_COMPONENT_{i}",(px+.35,py,2.9),(.55,.16,.18),"purple",f)
 for i in range(3):
  xx=x+3+i*2.0; box(f"V02_PICK_HEAD_COLUMN_{i}",(xx,y+2.4,3.6),(.22,.22,3.8),"steel",f); box(f"V02_PICK_HEAD_{i}",(xx,y+1.8,5.2),(1.0,.5,.18),"yellow",f); pipe(f"V02_PICK_HEAD_DROP_{i}",(xx,y+1.8,5.1),(xx,y,3.0),.08,"teal",f)
 belt("V02_CAP_TRIGGER_OUTFEED",x+10,y,8,1.6,f,"stainless")

def liquid():
 f="Liquid Filling / Packaging"; x,y=10,-2
 # bottle infeed, rotary filler with visible bottles/nozzles, capper, labeler reels and case packer
 belt("V02_LIQUID_INFEED",x-16,y,8,1.8,f,"stainless")
 cyl("V02_LIQUID_FILLER_CAROUSEL",(x-8,y,2.0),3.0,.42,"blue",f,32)
 for i in range(10):
  a=math.tau*i/10; px=x-8+2.35*math.cos(a); py=y+2.35*math.sin(a); cyl(f"V02_FILL_BOTTLE_{i}",(px,py,2.35),.28,.9,"teal",f,18); pipe(f"V02_FILL_NOZZLE_{i}",(px,py,4.25),(px,py,2.85),.08,"yellow",f)
 box("V02_FILLER_HEAD_FRAME",(x-8,y,4.55),(5.8,.35,.25),"steel",f)
 belt("V02_LIQUID_MAIN_CONVEYOR",x+5,y,23,1.8,f,"stainless")
 box("V02_LIQUID_CAPPER",(x+1,y,2.7),(1.8,2.2,2.9),"blue",f); cyl("V02_CAPPER_HEAD",(x+1,y,4.5),.7,.3,"yellow",f,24)
 box("V02_LIQUID_LABELER",(x+8,y,2.6),(2.0,2.4,2.7),"green",f); cyl("V02_LABEL_REEL_IN",(x+7.2,y+1.4,4.0),.75,.25,"white",f,24).rotation_euler[1]=math.pi/2; cyl("V02_LABEL_REEL_OUT",(x+8.8,y+1.4,4.0),.75,.25,"white",f,24).rotation_euler[1]=math.pi/2
 box("V02_LIQUID_CASE_PACKER",(x+16,y,2.8),(3.0,2.8,3.3),"orange",f); belt("V02_LIQUID_CASE_OUTFEED",x+22,y,8,2.0,f,"stainless")
 for i in range(4): box(f"V02_LIQUID_CASE_{i}",(x+18+i*1.5,y,2.1),(1.0,1.2,1.2),"white",f)

def weigh():
 f="Micro-ingredient Weigh / Dispense"; x,y=-5,50
 # open booth, tapered ingredient hoppers, precision balances and transfer workflow
 box("V02_WEIGH_BOOTH_BACK",(x,y+3.1,3.1),(10,.12,4.0),"white",f); box("V02_WEIGH_BOOTH_SIDE",(x-5,y+1.1,3.1),(.12,4.0,4.0),"white",f)
 for i,dx in enumerate((-3,-1,1,3)):
  cone(f"V02_WEIGH_HOPPER_{i}",(x+dx,y+2.0,4.2),.72,.28,1.8,"stainless",f); box(f"V02_WEIGH_HOPPER_VALVE_{i}",(x+dx,y+2.0,3.1),(.45,.45,.35),"blue",f); pipe(f"V02_WEIGH_DOSING_CHUTE_{i}",(x+dx,y+2.0,2.95),(x+dx,y-.2,2.35),.09,"teal",f)
 box("V02_WEIGH_BALANCE_TABLE",(x,y-1.1,1.8),(7.0,1.0,1.1),"steel",f)
 for i,dx in enumerate((-2.2,0,2.2)):
  box(f"V02_PRECISION_BALANCE_{i}",(x+dx,y-1.5,2.45),(1.25,.65,.32),"blue",f); cyl(f"V02_BALANCE_BOWL_{i}",(x+dx,y-1.5,2.75),.43,.18,"white",f,20)
 box("V02_WEIGH_TRANSFER_TOTE",(x+5,y-.8,1.8),(1.8,1.4,1.2),"yellow",f); box("V02_WEIGH_OPERATOR_TABLE",(x-5,y-1.8,1.7),(2.2,1.0,.9),"wood",f)

def toothpaste():
 f="Toothpaste Production"; x,y=-12,43
 # vacuum mixing, holding, tube magazine, filler/crimper and cartoner
 cyl("V02_PASTE_VACUUM_MIXER",(x-8,y,3.5),2.0,4.2,"stainless",f,32); box("V02_PASTE_MIXER_LID",(x-8,y,5.75),(1.0,1.0,.7),"blue",f); pipe("V02_PASTE_TRANSFER",(x-6,y,3.0),(x-2,y,3.0),.25,"stainless",f)
 cyl("V02_PASTE_HOLDING_TANK",(x-1,y,3.2),1.5,3.6,"green",f,28); box("V02_PASTE_HOLDING_MOTOR",(x-1,y,5.5),(.7,.7,.7),"blue",f)
 box("V02_TUBE_MAGAZINE",(x+3,y+2.2,3.2),(2.2,1.2,3.4),"white",f)
 for i in range(5): cyl(f"V02_EMPTY_TUBE_{i}",(x+2.6+i*.32,y+1.55,3.1),.12,1.8,"white",f,16); pipe(f"V02_TUBE_GUIDE_{i}",(x+3+i*.32,y+1.4,3.1),(x+4+i*.32,y,3.1),.05,"teal",f)
 belt("V02_PASTE_TUBE_CONVEYOR",x+10,y,14,1.7,f,"stainless")
 box("V02_PASTE_TUBE_FILLER",(x+6,y,3.1),(1.8,2.1,3.2),"blue",f); box("V02_PASTE_CRIMPER",(x+10,y,2.8),(1.4,1.8,2.7),"purple",f); box("V02_PASTE_CARTONER",(x+15,y,3.0),(2.2,2.2,3.3),"orange",f)
 for i in range(5): cyl(f"V02_FILLED_TUBE_{i}",(x+5+i*1.6,y,2.25),.14,1.0,"white",f,16)

def wipes():
 f="Wet Wipes Production"; x,y=22,43
 # roll unwind, wetting bath/rollers, folding plow, cutter/stacker and pouch packer
 box("V02_WIPES_UNWIND_FRAME",(x-14,y,3.2),(2.0,3.2,4.8),"steel",f); cyl("V02_WIPES_MASTER_ROLL",(x-14,y-1.8,3.2),1.55,.7,"white",f,32).rotation_euler[1]=math.pi/2
 cyl("V02_WIPES_WETTING_ROLL_A",(x-9,y,2.6),1.0,.7,"teal",f,28).rotation_euler[1]=math.pi/2; cyl("V02_WIPES_WETTING_ROLL_B",(x-9,y,4.0),1.0,.7,"teal",f,28).rotation_euler[1]=math.pi/2
 box("V02_WIPES_LOTION_BATH",(x-9,y,1.7),(3.0,2.2,.65),"green",f); pipe("V02_WIPES_LOTION_FEED",(x-7,y+1.3,4),(x-9,y+1.3,2.1),.15,"green",f)
 box("V02_WIPES_FOLDING_PLOW",(x-4,y,2.7),(2.2,2.8,2.8),"purple",f); box("V02_WIPES_FOLDING_GUIDE",(x-4,y,4.2),(2.8,.18,.18),"yellow",f)
 belt("V02_WIPES_CONVERTING_LINE",x+5,y,18,1.8,f,"stainless")
 box("V02_WIPES_CUTTER",(x+1,y,2.8),(1.4,2.1,3.0),"blue",f); box("V02_WIPES_STACKER",(x+6,y,2.7),(1.8,2.3,2.9),"purple",f); box("V02_WIPES_POUCH_PACKER",(x+12,y,3.0),(2.8,2.5,3.6),"orange",f); belt("V02_WIPES_PACK_OUT",x+18,y,7,1.7,f,"stainless")
 for i in range(5): box(f"V02_WIPES_STACK_{i}",(x+6+i*.4,y,2.1),(.22,1.0,.75),"white",f)

def glass():
 f="Central Glass Deck Command / Training / Café Gallery"; x=70
 # bright connected floor, command wall, training table and café counter in one coherent gallery
 box("V02_GLASS_GALLERY_FLOOR",(x,24,10.25),(7.2,45,.12),"white",f)
 box("V02_GLASS_COMMAND_WALL",(x,30,12.0),(7.0,.18,2.8),"glass",f)
 for i in range(5): box(f"V02_GLASS_COMMAND_SCREEN_{i}",(x-2.6+i*1.3,29.8,12.1),(.95,.08,1.1),"teal",f)
 box("V02_GLASS_COMMAND_CONSOLE",(x,27.4,10.9),(6.0,1.0,1.2),"blue",f)
 for i in range(4): cyl(f"V02_GLASS_COMMAND_CHAIR_{i}",(x-2.2+i*1.45,25.7,10.65),.32,.7,"yellow",f,16)
 box("V02_GLASS_TRAINING_TABLE",(x,15,10.7),(5.4,2.5,.25),"wood",f)
 for i in range(6): cyl(f"V02_GLASS_TRAINING_SEAT_{i}",(x-2.5+(i%3)*2.5,13.0+(i//3)*4.0,10.4),.32,.7,"yellow",f,16)
 box("V02_GLASS_CAFE_COUNTER",(x,5,10.9),(6.0,1.1,1.45),"wood",f)
 for i in range(4): cyl(f"V02_GLASS_CAFE_STOOL_{i}",(x-2.1+i*1.4,3.3,10.45),.3,.75,"purple",f,16)
 box("V02_GLASS_CAFE_BACKBAR",(x,6.2,12.3),(5.2,.25,2.4),"green",f)

def main():
 pre=sha(BLEND); hide_v01_focused()
 for fn in (blow,caps,liquid,weigh,toothpaste,wipes,glass): fn()
 scene=bpy.context.scene; scene["REV005_REMEDIATION_V02_STATUS"]="AWAITING_GPT_REMEDIATION_AUDIT_V02"; scene["REV005_REMEDIATION_V02_COLLECTION"]=COL; scene["REV004_PRESERVED"]=True
 bpy.ops.wm.save_as_mainfile(filepath=str(BLEND)); bpy.ops.export_scene.gltf(filepath=str(GLB),export_format="GLB",export_cameras=True,export_lights=True,export_apply=True,export_extras=True)
 OUT.mkdir(parents=True,exist_ok=True); result={"status":"BUILT","collection":COL,"focused_targets":sorted(FOCUSED),"pre_sha256":pre,"post_blend_sha256":sha(BLEND),"post_glb_sha256":sha(GLB),"object_count":len(c.objects),"blend":str(BLEND),"glb":str(GLB)}; (OUT/"BUILD_RESULT.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
main()
