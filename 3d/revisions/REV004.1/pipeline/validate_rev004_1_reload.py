import hashlib
import json
from pathlib import Path

import bpy


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main():
    repo = Path(__file__).resolve().parents[4]
    revision_dir = repo / '3d' / 'revisions' / 'REV004.1'
    glb = revision_dir / 'POVU_REV004_1_FINAL_MASTER.glb'
    output = revision_dir / 'audit' / 'REV004_1_GLTF_RELOAD_INVENTORY.json'
    bpy.ops.wm.read_factory_settings(use_empty=True)
    result = bpy.ops.import_scene.gltf(filepath=str(glb))
    if 'FINISHED' not in result:
        raise RuntimeError(f'GLB import failed: {result}')
    objects = list(bpy.data.objects)
    names = {obj.name for obj in objects}
    hog_roots = [obj.name for obj in objects if obj.name == 'HANDS_OF_GROWTH' and obj.type == 'EMPTY']
    flagship = [obj.name for obj in objects if obj.name == 'SMART_TOTEM_VIP_BODY']
    campus = [obj.name for obj in objects if obj.name.startswith('SMART_TOTEM_CAMPUS_') and obj.name.endswith('_BODY')]
    required = ['HANDS_OF_GROWTH', 'HOG_HAND_LEFT', 'HOG_HAND_RIGHT', 'HOG_TREE_TRUNK', 'HOG_TREE_CROWN', 'HOG_PLINTH', 'LABEL_ANCHOR_HANDS_OF_GROWTH', 'LIVING_WALL_EXTENDED_BACKING', 'VIP_ENTRANCE_DOOR_L', 'VIP_ENTRANCE_DOOR_R', 'WATER_WALL_STRUCTURE', 'GLASS_DECK_CENTRAL_LIFT', 'Production_Hall']
    missing = sorted(set(required) - names)
    report = {
        'status': 'PASS' if not missing and len(hog_roots) == 1 and len(flagship) == 1 and len(campus) == 4 else 'BLOCKED',
        'glb': str(glb),
        'glb_sha256': sha256(glb),
        'object_count': len(objects),
        'mesh_object_count': sum(1 for obj in objects if obj.type == 'MESH'),
        'material_count': len(bpy.data.materials),
        'camera_count': sum(1 for obj in objects if obj.type == 'CAMERA'),
        'hands_of_growth_roots': hog_roots,
        'hands_of_growth_root_count': len(hog_roots),
        'vip_flagship_smart_totems': flagship,
        'vip_flagship_smart_totem_count': len(flagship),
        'campus_smart_totems': campus,
        'campus_smart_totem_count': len(campus),
        'required_names_missing': missing,
    }
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
