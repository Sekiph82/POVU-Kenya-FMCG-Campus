import argparse
import hashlib
import json
import os
import sys

import bpy


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--report", required=True)
    return parser.parse_args(sys.argv[sys.argv.index("--") + 1:])


def socket_value(node, name, fallback=None):
    socket = node.inputs.get(name)
    if socket is None:
        return fallback
    value = socket.default_value
    try:
        return list(value)
    except TypeError:
        return value


def material_record(material):
    record = {
        "name": material.name,
        "use_nodes": bool(material.use_nodes),
        "base_color": list(material.diffuse_color),
        "metallic": None,
        "roughness": None,
        "alpha": float(material.diffuse_color[3]),
        "texture_presence": False,
        "texture_images": [],
    }
    if material.use_nodes and material.node_tree:
        for node in material.node_tree.nodes:
            if node.type == "BSDF_PRINCIPLED":
                record["base_color"] = socket_value(node, "Base Color", record["base_color"])
                record["metallic"] = socket_value(node, "Metallic")
                record["roughness"] = socket_value(node, "Roughness")
                record["alpha"] = socket_value(node, "Alpha", record["alpha"])
            if node.type == "TEX_IMAGE":
                record["texture_presence"] = True
                if node.image:
                    record["texture_images"].append(node.image.filepath)
    return record


def main():
    args = parse_args()
    source = os.path.abspath(args.source)
    with open(source, "rb") as handle:
        source_hash = hashlib.sha256(handle.read()).hexdigest()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=source)
    objects = list(bpy.context.scene.objects)
    tokens = (
        "HOG", "PROCESS", "TANK", "MIXING", "EPOXY", "GLASS", "DECK", "VIP", "PLAZA",
        "LIVING", "WATER", "CANOPY", "SIGN", "PRODUCTION", "LANDSCAPE", "TREE", "PALM",
    )
    relevant = []
    material_names = set()
    for obj in objects:
        if obj.type != "MESH" or not any(token in obj.name.upper() for token in tokens):
            continue
        slots = []
        for slot_index, slot in enumerate(obj.material_slots):
            material = slot.material
            if material is None:
                slots.append({"slot": slot_index, "material": None})
                continue
            material_names.add(material.name)
            slots.append({"slot": slot_index, "material": material.name, "audit": material_record(material)})
        relevant.append({"object": obj.name, "type": obj.type, "material_slots": slots})
    materials = {name: material_record(bpy.data.materials[name]) for name in sorted(material_names)}
    report = {
        "source_path": source,
        "source_sha256": source_hash,
        "object_count": len(objects),
        "relevant_object_count": len(relevant),
        "relevant_objects": relevant,
        "materials": materials,
        "material_count_audited": len(materials),
        "has_non_grey_material_data": any(
            any(channel > 0.05 and channel < 0.95 for channel in record["base_color"][:3])
            for record in materials.values()
        ),
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(json.dumps({
        "source_sha256": source_hash,
        "relevant_object_count": len(relevant),
        "material_count_audited": len(materials),
        "has_non_grey_material_data": report["has_non_grey_material_data"],
    }))


if __name__ == "__main__":
    main()
