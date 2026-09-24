import * as THREE from "three";

const green = ["#2f6f46", "#4f8a45", "#6a9a4d", "#2d5a3b"];
const hash = (value: string) => value.split("").reduce((total, char) => (total * 31 + char.charCodeAt(0)) >>> 0, 7);

const physical = (color: string, options: Partial<THREE.MeshPhysicalMaterialParameters> = {}) =>
  new THREE.MeshPhysicalMaterial({color, roughness: 0.62, metalness: 0, ...options});

const categoryFor = (name: string, sourceMaterials = "") => {
  const upper = `${name} ${sourceMaterials}`.toUpperCase();
  if (name.toUpperCase().includes("SITE_7HA") || name.toUpperCase().includes("GROUND")) return "paving";
  if (upper.includes("WATER") || upper.includes("WATERFALL") || upper.includes("CURTAIN")) return "water_wall";
  if (upper.includes("LIVING_WALL") || upper.includes("FOLIAGE")) return "living_wall";
  if (upper.includes("HOG_TREE") || upper.includes("HANDS_OF_GROWTH")) return "hands_of_growth";
  if (upper.startsWith("SOLAR") || upper.includes("SOLARPANEL") || upper.includes("PV_")) return "solar";
  if (upper.includes("GLASS") || upper.includes("WINDOW") || upper.includes("DOOR")) return "glass";
  if (upper.includes("PROCESS") || upper.includes("PROC_") || upper.includes("STAINLESS") || upper.includes("EPOXY") || upper.includes("TANK") || upper.includes("MIXING") || upper.includes("MOLDER") || upper.includes("WIPES")) return "machine";
  if (upper.includes("ROOF") || upper.includes("WALL_") || upper.includes("HALL") || upper.includes("ENTRANCE") || upper.includes("ARCH_") || upper.includes("CONCRETE") || upper.includes("STONE") || upper.includes("BRONZE") || upper.includes("GRAPHITE") || upper.includes("WARM")) return "architecture";
  if (upper.includes("ROAD") || upper.includes("PAV") || upper.includes("CURB") || upper.includes("PATH")) return "paving";
  if (upper.includes("TREE") || upper.includes("SHRUB") || upper.includes("GRASS") || upper.includes("VEGETATION") || upper.includes("PLANT") || upper.includes("LANDSCAPE") || upper.includes("LEAF") || upper.includes("LIVINGGREEN")) return "landscape";
  if (upper.includes("TOTEM")) return "smart_totem";
  return "source";
};

const assign = (object: THREE.Object3D, material: THREE.Material) => {
  const mesh = object as THREE.Mesh;
  if (!mesh.isMesh) return;
  mesh.material = material;
  mesh.castShadow = true;
  mesh.receiveShadow = true;
};

export const applyRev004MaterialSystem = (input: THREE.Object3D) => {
  const scene = input.clone(true);
  scene.traverse((object) => {
    const name = object.name || "unnamed";
    const upper = name.toUpperCase();
    const sourceMaterials = object instanceof THREE.Mesh
      ? (Array.isArray(object.material) ? object.material : [object.material]).map((material) => material?.name || "").join(" ")
      : "";
    const category = categoryFor(name, sourceMaterials);
    if (name === "Production_Hall") object.visible = false;
    if (upper.startsWith("LIVING_WALL") || upper === "VIP_LIVINGWALL") object.visible = false;

    if (category === "water_wall") {
      assign(object, physical("#86d7de", {roughness: 0.12, metalness: 0.05, transparent: true, opacity: 0.62}));
    } else if (category === "living_wall" || upper.includes("FOLIAGE")) {
      assign(object, physical(green[hash(name) % green.length], {roughness: 0.88}));
    } else if (category === "hands_of_growth") {
      const isTrunk = upper.includes("TRUNK") || upper.includes("FOREARM") || upper.includes("PALM");
      assign(object, physical(isTrunk ? "#6b4328" : green[hash(name) % green.length], {roughness: 0.82}));
    } else if (category === "solar") {
      assign(object, physical("#10263b", {roughness: 0.2, metalness: 0.72, clearcoat: 0.35, clearcoatRoughness: 0.18}));
    } else if (category === "glass") {
      assign(object, physical("#7fc6d3", {roughness: 0.08, metalness: 0, transmission: 0.78, thickness: 0.08, transparent: true, opacity: 0.72}));
    } else if (category === "machine") {
      const stainless = upper.includes("TANK") || upper.includes("STAINLESS") || upper.includes("PROCESS");
      assign(object, physical(stainless ? "#9ca8ae" : "#46535d", {roughness: stainless ? 0.28 : 0.4, metalness: stainless ? 0.76 : 0.4}));
    } else if (category === "architecture") {
      const accent = upper.includes("CHAMPAGNE") || upper.includes("BRONZE") || upper.includes("ACCENT") || upper.includes("SIGNAGE");
      const graphite = upper.includes("FRAME") || upper.includes("GRAPHITE") || upper.includes("CANOPY");
      assign(object, physical(accent ? "#b98748" : graphite ? "#26313a" : "#b9c0bc", {roughness: accent ? 0.28 : 0.66, metalness: accent || graphite ? 0.42 : 0.08}));
    } else if (category === "paving") {
      assign(object, physical(upper.includes("ROAD") ? "#303940" : "#a8aaa2", {roughness: 0.92}));
    } else if (category === "landscape") {
      const isTrunk = upper.includes("TRUNK") || upper.includes("STEM");
      assign(object, physical(isTrunk ? "#765039" : green[hash(name) % green.length], {roughness: 0.9}));
    } else if (category === "smart_totem") {
      const screen = upper.includes("SCREEN");
      assign(object, physical(screen ? "#0d7180" : "#202c35", {roughness: screen ? 0.18 : 0.42, metalness: screen ? 0.3 : 0.62, emissive: screen ? "#0b6673" : "#000000", emissiveIntensity: screen ? 0.4 : 0}));
    }
  });
  return scene;
};
