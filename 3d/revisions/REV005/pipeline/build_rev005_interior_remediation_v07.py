import bpy
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REV = ROOT / "3d/revisions/REV005"
OUT = ROOT / "output/rev005-interior-remediation-v07"
BLEND = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend"
GLB = REV / "POVU_REV005_INTERIOR_COMPLETION_MASTER.glb"
BASELINE = OUT / "V07_BASELINE_HASHES.json"

MODEL_HIDE_PROXY_NAMES = {
    "V04_ADMIN_QC_LAB_BENCH", "V05_ADMIN_QC_BENCH",
    "V03_BLOW_OVEN_HOUSING", "V05_BLOW_OVEN_HOUSING", "V05_BLOW_MOULD_CLAMP_HOUSING",
    "V05_CHEM_TANK0_VESSEL", "V05_CHEM_TANK1_VESSEL", "V05_CHEM_TANK2_VESSEL",
    "V04_ETP_TANK_02", "V05_ETP_HEADER0", "V05_ETP_HEADER1",
    "V03_LIQUID_FILLER_HOUSING", "V03_LIQUID_MAIN_LINE_FRAME", "V05_LIQUID_FILLER_HOUSING", "V05_LIQUID_CASE_PACK_HOUSING",
    "V05_CLINIC_PRIVACY_PANEL",
    "V05_POWDER_DOSER_HOUSING",
    "V03_RESTAURANT_CAFE_BAR", "V05_CAFE_SERVICE_COUNTER", "V05_KITCHEN_PARTITION_PANEL",
    "V05_SECURITY_WAIT_PANEL",
    "V03_PASTE_CARTONER", "V03_PASTE_CASE_OUTFEED", "V03_PASTE_FILLER_GUARD", "V03_PASTE_TUBE_LINE_FRAME", "V04_PASTE_BLEND_JACKET", "V04_PASTE_RIGHT", "V05_PASTE_VACUUM_MIX_VESSEL",
    "V04_UTIL_RIGHT", "V05_UTIL_BOILER_VESSEL",
    "V03_WIPES_CONVERTING_LINE_FRAME", "V03_WIPES_UNWIND_FRAME", "V03_WIPES_WETTING_BATH", "V05_WIPES_FOLD_FRAME", "V05_WIPES_DISCHARGE",
}

QA_ONLY_PROXY_NAMES = {
    "V05_FG_BACK", "V05_GLASS_LEFT", "V05_GATEHOUSE_BACK",
}

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()

def main():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    before_blend = sha(BLEND)
    before_glb = sha(GLB)
    if before_blend != baseline["blend"]["sha256"] or before_glb != baseline["glb"]["sha256"]:
        raise RuntimeError("V07 baseline mismatch; refusing to mutate REV005")

    hidden = []
    missing = []
    for name in sorted(MODEL_HIDE_PROXY_NAMES):
        obj = bpy.data.objects.get(name)
        if not obj:
            missing.append(name)
            continue
        obj.hide_render = True
        obj.hide_viewport = True
        obj["REV005_V07_OBSOLETE_PROXY_HIDDEN"] = True
        obj["REV005_V07_ROOT_CAUSE"] = "legacy proxy occluded V06 functional detail"
        hidden.append(name)

    scene = bpy.context.scene
    scene["REV005_REMEDIATION_V07_STATUS"] = "AWAITING_GPT_REMEDIATION_AUDIT_V07"
    scene["REV005_REMEDIATION_V07_METHOD"] = "visibility_integration_root_cause_closure"
    scene["REV005_V06_BASELINE_BLEND_SHA256"] = before_blend
    scene["REV005_V06_BASELINE_GLB_SHA256"] = before_glb
    scene["REV005_V07_MODEL_HIDDEN_PROXY_COUNT"] = len(hidden)
    scene["REV005_V07_QA_ONLY_PROXY_NAMES"] = sorted(QA_ONLY_PROXY_NAMES)

    # Save to a fresh temporary file and replace the canonical Blend, preserving
    # the existing owner .blend1 backup rather than asking Blender to version it.
    temp_blend = REV / "POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER_V07.tmp.blend"
    if temp_blend.exists():
        temp_blend.unlink()
    bpy.ops.wm.save_as_mainfile(filepath=str(temp_blend), check_existing=False)
    os.replace(temp_blend, BLEND)
    export_kwargs = dict(
        filepath=str(GLB), export_format="GLB", export_cameras=True,
        export_lights=True, export_apply=True, export_extras=True,
        use_selection=False,
    )
    try:
        bpy.ops.export_scene.gltf(**export_kwargs, use_visible=True)
        export_visibility = "use_visible=True"
    except TypeError:
        bpy.ops.export_scene.gltf(**export_kwargs)
        export_visibility = "operator_fallback_without_use_visible"
    result = {
        "status": "V07_INTEGRATION_CORRECTION_COMPLETE",
        "task": "M08.14",
        "baseline_file": str(BASELINE),
        "before_blend_sha256": before_blend,
        "before_glb_sha256": before_glb,
        "model_hidden_proxy_names": hidden,
        "missing_declared_proxy_names": missing,
        "qa_only_proxy_names": sorted(QA_ONLY_PROXY_NAMES),
        "export_visibility": export_visibility,
        "final_blend_sha256": sha(BLEND),
        "final_glb_sha256": sha(GLB),
    }
    (OUT / "BUILD_RESULT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

main()
