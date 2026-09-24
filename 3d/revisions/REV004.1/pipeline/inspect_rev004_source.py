import json
import os
from pathlib import Path

import bpy
from mathutils import Vector


def props(obj):
    def safe(value):
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, (list, tuple)) or hasattr(value, '__iter__'):
            return [safe(item) for item in value]
        return str(value)
    return {str(key): safe(obj[key]) for key in obj.keys() if key != '_RNA_UI'}


def bounds(obj):
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box] if obj.type == 'MESH' else []
    if not points:
        return None
    return {'min': [round(min(point[i] for point in points), 4) for i in range(3)], 'max': [round(max(point[i] for point in points), 4) for i in range(3)]}


def record(obj, source_names):
    return {
        'name': obj.name,
        'type': obj.type,
        'parent': obj.parent.name if obj.parent else None,
        'collection_paths': [collection.name for collection in obj.users_collection],
        'location': [round(value, 4) for value in obj.matrix_world.translation],
        'dimensions': [round(value, 4) for value in obj.dimensions],
        'bounds': bounds(obj),
        'materials': [slot.material.name for slot in obj.material_slots if slot.material],
        'hide_viewport': obj.hide_viewport,
        'hide_render': obj.hide_render,
        'custom_properties': props(obj),
        'present_in_rev003_inventory': obj.name in source_names,
    }


def main():
    repo = Path(__file__).resolve().parents[4]
    source_blend = repo / '3d' / 'revisions' / 'REV004' / 'POVU_KENYA_FMCG_CAMPUS_REV004_FINAL_ARCHITECTURAL_MASTER.blend'
    rev003_inventory_path = repo / '3d' / 'revisions' / 'REV004' / 'audit' / 'REV003_full_inventory.json'
    output_path = repo / '3d' / 'revisions' / 'REV004.1' / 'audit' / 'REV004_source_semantic_audit.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    source_names = set(json.loads(rev003_inventory_path.read_text(encoding='utf-8')).get('object_names', []))
    bpy.ops.wm.open_mainfile(filepath=str(source_blend))
    selected = []
    for obj in sorted(bpy.data.objects, key=lambda item: item.name):
        upper = obj.name.upper()
        if any(token in upper for token in ('HOG', 'HAND', 'GROWTH', 'LIVING_WALL', 'VIP_LIVING', 'SMART_TOTEM')):
            selected.append(record(obj, source_names))
    result = {
        'source_blend': str(source_blend),
        'source_revision': 'REV004',
        'source_rev003_inventory': str(rev003_inventory_path),
        'object_count': len(bpy.data.objects),
        'mesh_object_count': sum(1 for obj in bpy.data.objects if obj.type == 'MESH'),
        'semantic_matches': selected,
        'root_candidates': [item['name'] for item in selected if item['type'] in {'EMPTY', 'ARMATURE'} or item['name'].upper() in {'HANDS_OF_GROWTH', 'HOG_ROOT'}],
        'rev003_name_matches': [item['name'] for item in selected if item['present_in_rev003_inventory']],
    }
    output_path.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output_path), 'semantic_match_count': len(selected), 'rev003_name_match_count': len(result['rev003_name_matches'])}, indent=2))


if __name__ == '__main__':
    main()
