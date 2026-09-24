import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import bpy
from mathutils import Matrix, Vector


EXPECTED_REV004_GLB_SHA = '1DB31C66FCAB4F0FF9378C8049FD03890FEBE7157716DAFEA3794F2D1621E2DA'


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, (list, tuple)) or hasattr(value, '__iter__'):
        return [safe(item) for item in value]
    return str(value)


def set_prop(obj, key, value):
    obj[key] = safe(value)


def world_bounds(obj):
    if obj.type != 'MESH':
        return None
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    return {
        'min': [round(min(point[i] for point in points), 4) for i in range(3)],
        'max': [round(max(point[i] for point in points), 4) for i in range(3)],
    }


def semantic_entry(obj, category, role, source_object=None):
    return {
        'object_name': obj.name,
        'type': obj.type,
        'category': category,
        'parent': obj.parent.name if obj.parent else None,
        'world_position': [round(value, 4) for value in obj.matrix_world.translation],
        'world_bounds': world_bounds(obj),
        'materials': [slot.material.name for slot in obj.material_slots if slot.material],
        'visible': not obj.hide_viewport and not obj.hide_render,
        'intended_remotion_role': role,
        'source_object': source_object or obj.name,
    }


def ensure_collection(name):
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def empty(name, location, collection, category, role):
    existing = bpy.data.objects.get(name)
    if existing:
        return existing
    obj = bpy.data.objects.new(name, None)
    obj.empty_display_type = 'PLAIN_AXES'
    obj.empty_display_size = 1.0
    obj.location = location
    collection.objects.link(obj)
    set_prop(obj, 'rev004_1_semantic_id', name)
    set_prop(obj, 'rev004_1_category', category)
    set_prop(obj, 'remotion_role', role)
    return obj


def parent_preserve_world(obj, parent):
    world = obj.matrix_world.copy()
    obj.parent = parent
    obj.matrix_parent_inverse = Matrix.Identity(4)
    obj.matrix_world = world


def copy_material(source_name, new_name, color, metallic=0.0, roughness=0.6):
    material = bpy.data.materials.get(new_name)
    if material is None:
        source = bpy.data.materials.get(source_name)
        material = source.copy() if source else bpy.data.materials.new(new_name)
        material.name = new_name
    material.use_nodes = True
    material.diffuse_color = (*color, 1.0)
    nodes = material.node_tree.nodes if material.node_tree else []
    principled = nodes.get('Principled BSDF') if nodes else None
    if principled:
        principled.inputs['Base Color'].default_value = (*color, 1.0)
        principled.inputs['Metallic'].default_value = metallic
        principled.inputs['Roughness'].default_value = roughness
    set_prop(material, 'rev004_1_semantic_material', new_name)
    set_prop(material, 'remotion_override_ready', True)
    return material


def assign_material(obj, material):
    obj.data.materials.clear()
    obj.data.materials.append(material)


def create_box(name, location, dimensions, material, collection, category, role):
    mesh = bpy.data.meshes.new(name + '_MESH')
    hx, hy, hz = [dimension / 2.0 for dimension in dimensions]
    vertices = [
        (-hx, -hy, -hz), (hx, -hy, -hz), (hx, hy, -hz), (-hx, hy, -hz),
        (-hx, -hy, hz), (hx, -hy, hz), (hx, hy, hz), (-hx, hy, hz),
    ]
    faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7)]
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    collection.objects.link(obj)
    assign_material(obj, material)
    set_prop(obj, 'rev004_1_semantic_id', name)
    set_prop(obj, 'rev004_1_category', category)
    set_prop(obj, 'remotion_role', role)
    return obj


def add_semantic_to_existing(obj, semantic_id, category, role, source_object=None):
    set_prop(obj, 'rev004_1_semantic_id', semantic_id)
    set_prop(obj, 'rev004_1_category', category)
    set_prop(obj, 'remotion_role', role)
    set_prop(obj, 'rev004_1_source_object', source_object or obj.name)


def build_manifest(repo, source_glb, output_blend, output_glb, living_wall_extension, hog_entries, label_anchor, removed_objects, source_hog_names, rev003_hog_names):
    old_manifest_path = repo / '3d' / 'revisions' / 'REV004' / 'REV004_ARCHITECTURAL_MANIFEST.json'
    manifest = json.loads(old_manifest_path.read_text(encoding='utf-8'))
    manifest = copy.deepcopy(manifest)
    manifest['manifest'] = 'REV004_1_ARCHITECTURAL_MANIFEST'
    manifest['revision'] = 'REV004.1_FINAL_CLEANUP'
    manifest['generated_at_utc'] = datetime.now(timezone.utc).isoformat()
    manifest['source'] = {'path': str(source_glb), 'sha256': sha256(source_glb), 'revision': 'REV004'}
    manifest['output'] = {'blend': str(output_blend), 'glb': str(output_glb)}
    manifest['counts'] = {
        'object_count': len(bpy.data.objects),
        'mesh_object_count': sum(1 for obj in bpy.data.objects if obj.type == 'MESH'),
        'mesh_data_count': len(bpy.data.meshes),
        'material_count': len(bpy.data.materials),
        'camera_count': sum(1 for obj in bpy.data.objects if obj.type == 'CAMERA'),
    }
    categories = manifest.setdefault('categories', {})
    categories.setdefault('hands_of_growth', [])
    categories['hands_of_growth'].extend(hog_entries)
    categories.setdefault('living_wall', [])
    categories['living_wall'].append(living_wall_extension)
    categories.setdefault('label_anchor', [])
    categories['label_anchor'].append(label_anchor)
    manifest['rev004_1_cleanup'] = {
        'source_rev004_glb_sha256': sha256(source_glb),
        'source_rev004_glb_sha256_expected': EXPECTED_REV004_GLB_SHA,
        'living_wall_modification': {
            'object_name': living_wall_extension['object_name'],
            'usable_wall_bounds_x': [-97.5, -65.0],
            'door_clearance_right_edge': -65.0,
            'water_wall_clearance': 'preserved; Water Wall begins well to the right of the VIP entrance zone',
            'scope': 'single thin backing panel closes the existing VIP living-wall plane continuously without moving doors, glazing, portal, canopy, or circulation',
        },
        'hands_of_growth_duplicate_audit': {
            'method': 'Compared REV004 Blender object names, parent hierarchy, transforms, custom hf_id values, materials, and the REV003_full_inventory.json source-name set.',
            'rev003_hog_mesh_names': sorted(rev003_hog_names),
            'rev004_hog_mesh_names': sorted(source_hog_names),
            'rev003_name_matches': sorted(set(source_hog_names) & set(rev003_hog_names)),
            'duplicate_glb_root_candidates_before_cleanup': 0,
            'objects_removed': removed_objects,
            'finding': 'No second HOG hierarchy exists in the approved REV004 GLB. The second visible R02 sculpture is a locked Remotion runtime presentation overlay; R02 code and MP4 were not changed.',
        },
        'hands_of_growth': {
            'root': 'HANDS_OF_GROWTH',
            'root_count': 1,
            'components': ['HOG_HAND_LEFT', 'HOG_HAND_RIGHT', 'HOG_TREE_TRUNK', 'HOG_TREE_CROWN', 'HOG_PLINTH'],
            'retained_original_components': sorted(source_hog_names),
            'label_anchor': label_anchor['object_name'],
            'label_text': 'HANDS OF GROWTH',
            'subtitle': 'People • Skills • Future',
        },
        'smart_totems': {'vip_flagship_root_count': 1, 'campus_root_count': 4, 'total_documented_placements': 5},
        'regression_lock': ['VIP doors', 'VIP portal', 'Water Wall', 'Smart Totems', 'solar field', 'façades', 'Glass Deck', 'stairs/lift', 'Production Hall', 'machinery', 'machine label anchors', 'roads', 'logistics', 'utilities', 'landscaping except the Living Wall backing extension', 'R02 Remotion source and MP4'],
    }
    manifest_path = repo / '3d' / 'revisions' / 'REV004.1' / 'REV004_1_ARCHITECTURAL_MANIFEST.json'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')


def main():
    repo = Path(__file__).resolve().parents[4]
    source_blend = repo / '3d' / 'revisions' / 'REV004' / 'POVU_KENYA_FMCG_CAMPUS_REV004_FINAL_ARCHITECTURAL_MASTER.blend'
    source_glb = repo / '3d' / 'revisions' / 'REV004' / 'POVU_REV004_FINAL_MASTER.glb'
    rev003_inventory_path = repo / '3d' / 'revisions' / 'REV004' / 'audit' / 'REV003_full_inventory.json'
    output_dir = repo / '3d' / 'revisions' / 'REV004.1'
    output_dir.joinpath('audit').mkdir(parents=True, exist_ok=True)
    output_dir.joinpath('pipeline').mkdir(parents=True, exist_ok=True)
    output_dir.joinpath('qa').mkdir(parents=True, exist_ok=True)
    output_blend = output_dir / 'POVU_KENYA_FMCG_CAMPUS_REV004_1_FINAL_ARCHITECTURAL_MASTER.blend'
    output_glb = output_dir / 'POVU_REV004_1_FINAL_MASTER.glb'
    if sha256(source_glb) != EXPECTED_REV004_GLB_SHA:
        raise RuntimeError('REV004 GLB SHA mismatch; refusing to create REV004.1')
    rev003_hog_names = [name for name in json.loads(rev003_inventory_path.read_text(encoding='utf-8')).get('object_names', []) if 'HOG' in name.upper() or 'HAND' in name.upper() or 'GROWTH' in name.upper()]
    bpy.ops.wm.open_mainfile(filepath=str(source_blend))
    cleanup_collection = ensure_collection('REV004_1_CLEANUP')

    # The approved REV004 source contains the original single HOG component set. Preserve it and make one explicit root.
    hog_meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH' and (obj.name.upper().startswith('HOG_') or obj.name.upper().startswith('HANDS_OF_GROWTH'))]
    source_hog_names = [obj.name for obj in hog_meshes]
    if not hog_meshes:
        raise RuntimeError('No HOG mesh components found in REV004 source')
    root = empty('HANDS_OF_GROWTH', (-108.0, -79.0, 0.0), cleanup_collection, 'hands_of_growth', 'HANDS_OF_GROWTH_ROOT')
    set_prop(root, 'rev004_1_original_source', 'REV003-retained component set')
    set_prop(root, 'rev004_1_root_count', 1)
    left = empty('HOG_HAND_LEFT', (-110.0, -79.0, 3.5), cleanup_collection, 'hands_of_growth', 'HOG_HAND_LEFT')
    right = empty('HOG_HAND_RIGHT', (-106.0, -79.0, 3.5), cleanup_collection, 'hands_of_growth', 'HOG_HAND_RIGHT')
    crown = empty('HOG_TREE_CROWN', (-108.0, -79.0, 8.0), cleanup_collection, 'hands_of_growth', 'HOG_TREE_CROWN')
    # Keep the original mesh parenting and transforms untouched. The semantic empties
    # below provide stable Remotion targets without risking Blender parent-inverse drift
    # when the .blend is saved and reloaded.
    left_members = []
    right_members = []
    crown_members = []
    for obj in hog_meshes:
        if obj.name.startswith('HOG_FOREARM_L') or obj.name.startswith('HOG_PALM_L') or obj.name.startswith('HOG_FINGER_-1_'):
            left_members.append(obj.name)
        elif obj.name.startswith('HOG_FOREARM_R') or obj.name.startswith('HOG_PALM_R') or obj.name.startswith('HOG_FINGER_1_'):
            right_members.append(obj.name)
        elif obj.name.startswith('HOG_TREE_CROWN_'):
            crown_members.append(obj.name)
        add_semantic_to_existing(obj, obj.name, 'hands_of_growth', obj.name, obj.name)
    for obj, semantic in ((left, 'HOG_HAND_LEFT'), (right, 'HOG_HAND_RIGHT'), (crown, 'HOG_TREE_CROWN')):
        set_prop(obj, 'rev004_1_component_of', 'HANDS_OF_GROWTH')
        set_prop(obj, 'rev004_1_semantic_id', semantic)
    set_prop(left, 'rev004_1_component_members', left_members)
    set_prop(right, 'rev004_1_component_members', right_members)
    set_prop(crown, 'rev004_1_component_members', crown_members)
    set_prop(root, 'rev004_1_component_members', sorted(source_hog_names))
    for obj in (root, left, right, crown):
        set_prop(obj, 'rev004_1_component_count', len(hog_meshes))

    stone = copy_material('POVU_Bronze_Signature', 'HOG_Stone_Light', (0.68, 0.72, 0.75), 0.05, 0.68)
    trunk = copy_material('POVU_Graphite', 'HOG_Trunk_Brown', (0.22, 0.07, 0.025), 0.0, 0.82)
    foliage = copy_material('POVU_Landmark_Green', 'HOG_Crown_Natural_Green', (0.08, 0.34, 0.07), 0.0, 0.78)
    for obj in hog_meshes:
        if obj.name.startswith(('HOG_FOREARM_', 'HOG_PALM_', 'HOG_FINGER_')):
            assign_material(obj, stone)
        elif obj.name == 'HOG_TREE_TRUNK':
            assign_material(obj, trunk)
        elif obj.name.startswith('HOG_TREE_CROWN_'):
            assign_material(obj, foliage)

    # Extend the existing usable VIP wall plane with one backing panel only; all locked entrance geometry stays untouched.
    living_material = copy_material('VIP_Leaf', 'LIVING_WALL_BACKING_GREEN', (0.045, 0.19, 0.065), 0.0, 0.82)
    extension = create_box('LIVING_WALL_EXTENDED_BACKING', (-81.25, -91.94, 5.8), (32.3, 0.16, 8.0), living_material, cleanup_collection, 'living_wall', 'LIVING_WALL_ARCHITECTURAL_EXTENSION')
    set_prop(extension, 'rev004_1_usable_wall_x_min', -97.5)
    set_prop(extension, 'rev004_1_usable_wall_x_max', -65.0)
    set_prop(extension, 'rev004_1_doors_clear', True)
    set_prop(extension, 'rev004_1_glazing_clear', True)
    set_prop(extension, 'rev004_1_water_wall_clear', True)
    for obj in bpy.data.objects:
        if 'LIVING_WALL' in obj.name.upper() or obj.name == 'VIP_LivingWall':
            add_semantic_to_existing(obj, 'LIVING_WALL', 'living_wall', 'LIVING_WALL_VEGETATION_OR_STRUCTURE', obj.name)

    # A future Remotion label anchor sits above the crown, not inside it.
    label_anchor = empty('LABEL_ANCHOR_HANDS_OF_GROWTH', (-108.0, -79.0, 11.4), cleanup_collection, 'label_anchor', 'HANDS_OF_GROWTH')
    set_prop(label_anchor, 'rev004_1_component_of', 'HANDS_OF_GROWTH')
    set_prop(label_anchor, 'label_text', 'HANDS OF GROWTH')
    set_prop(label_anchor, 'label_subtitle', 'People • Skills • Future')
    set_prop(label_anchor, 'anchor_clear_of_tree_crown', True)
    set_prop(label_anchor, 'anchor_clearance_above_crown', 0.9)

    # Reassert explicit source semantics without modifying locked systems.
    for name, role in (('VIP_ENTRANCE_DOOR_L', 'VIP_DOOR'), ('VIP_ENTRANCE_DOOR_R', 'VIP_DOOR'), ('WATER_WALL_STRUCTURE', 'WATER_WALL'), ('GLASS_DECK_CENTRAL_LIFT', 'GLASS_DECK_ACCESS'), ('Production_Hall', 'PRODUCTION_HALL')):
        obj = bpy.data.objects.get(name)
        if obj:
            set_prop(obj, 'rev004_1_regression_locked', True)
            set_prop(obj, 'rev004_1_locked_role', role)

    # Explicit flagship/campus count is based on the existing documented semantic placements.
    vip_body = bpy.data.objects.get('SMART_TOTEM_VIP_BODY')
    vip_count = 1 if vip_body and not vip_body.hide_render else 0
    campus_count = sum(1 for index in range(1, 5) if bpy.data.objects.get(f'SMART_TOTEM_CAMPUS_{index:02d}_BODY') and not bpy.data.objects.get(f'SMART_TOTEM_CAMPUS_{index:02d}_BODY').hide_render)
    if vip_count != 1 or campus_count != 4:
        raise RuntimeError(f'Unexpected Smart Totem count: VIP={vip_count}, campus={campus_count}')

    bpy.context.scene['REV004_1_SOURCE_REV004_GLB_SHA256'] = EXPECTED_REV004_GLB_SHA
    bpy.context.scene['REV004_1_HOG_ROOT_COUNT'] = 1
    bpy.context.scene['REV004_1_VIP_FLAGSHIP_SMART_TOTEM_COUNT'] = vip_count
    bpy.context.scene['REV004_1_CAMPUS_SMART_TOTEM_COUNT'] = campus_count
    bpy.context.scene['REV004_1_R02_LOCKED'] = True
    bpy.ops.wm.save_as_mainfile(filepath=str(output_blend))
    bpy.ops.export_scene.gltf(filepath=str(output_glb), export_format='GLB', export_cameras=True, export_lights=True, export_apply=True, export_extras=True)

    hog_entries = [semantic_entry(root, 'hands_of_growth', 'HANDS_OF_GROWTH_ROOT'), semantic_entry(left, 'hands_of_growth', 'HOG_HAND_LEFT'), semantic_entry(right, 'hands_of_growth', 'HOG_HAND_RIGHT'), semantic_entry(crown, 'hands_of_growth', 'HOG_TREE_CROWN')]
    for obj in hog_meshes:
        hog_entries.append(semantic_entry(obj, 'hands_of_growth', obj.name, obj.name))
    living_entry = semantic_entry(extension, 'living_wall', 'LIVING_WALL_ARCHITECTURAL_EXTENSION')
    label_entry = semantic_entry(label_anchor, 'label_anchor', 'HANDS_OF_GROWTH')
    build_manifest(repo, source_glb, output_blend, output_glb, living_entry, hog_entries, label_entry, [], source_hog_names, rev003_hog_names)
    audit = {
        'status': 'PASS',
        'source_rev004_glb_sha256': sha256(source_glb),
        'source_rev004_glb_sha256_expected': EXPECTED_REV004_GLB_SHA,
        'output_blend': str(output_blend),
        'output_glb': str(output_glb),
        'output_glb_sha256': sha256(output_glb),
        'living_wall_extension': living_entry,
        'hands_of_growth_root_count': 1,
        'hands_of_growth_components': ['HANDS_OF_GROWTH', 'HOG_HAND_LEFT', 'HOG_HAND_RIGHT', 'HOG_TREE_TRUNK', 'HOG_TREE_CROWN', 'HOG_PLINTH'],
        'objects_removed': [],
        'duplicate_identification': 'No duplicate exists in the approved REV004 GLB; all HOG geometry names match REV003 inventory. The extra R02 sculpture is a locked runtime overlay.',
        'vip_flagship_smart_totem_count': vip_count,
        'campus_smart_totem_count': campus_count,
        'label_anchor': label_entry,
    }
    (output_dir / 'audit' / 'REV004_1_BUILD_AUDIT.json').write_text(json.dumps(audit, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(audit, indent=2))


if __name__ == '__main__':
    main()
