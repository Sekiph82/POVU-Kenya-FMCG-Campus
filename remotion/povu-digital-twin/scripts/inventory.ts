import fs from 'node:fs/promises';
import path from 'node:path';
import {Box3, Vector3, Object3D} from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js';

type InventoryItem = {
  name: string;
  type: string;
  parent: string | null;
  visible: boolean;
  worldPosition: [number, number, number];
  worldBoundingBox: {min: [number, number, number]; max: [number, number, number]} | null;
  dimensions: [number, number, number] | null;
  material: string[];
  meshCount: number;
  cameraCount: number;
};

const root = path.resolve(import.meta.dirname, '..');
const glbPath = process.argv[2] ?? path.join(root, 'public', 'models', 'rev003.glb');
const outputPath = process.argv[3] ?? path.join(root, 'reports', 'scene-inventory.json');

const buffer = await fs.readFile(glbPath);
const loader = new GLTFLoader();
const arrayBuffer = buffer.buffer.slice(buffer.byteOffset, buffer.byteOffset + buffer.byteLength);

const gltf = await new Promise<any>((resolve, reject) => {
  loader.parse(arrayBuffer, path.dirname(glbPath) + path.sep, resolve, reject);
});

const scene = gltf.scene as Object3D;
scene.updateMatrixWorld(true);

const items: InventoryItem[] = [];
const materialNames = new Set<string>();
let nodeCount = 0;
let meshCount = 0;
let cameraCount = 0;

scene.traverse((object: any) => {
  nodeCount += 1;
  if (object.isMesh) meshCount += 1;
  if (object.isCamera) cameraCount += 1;

  const worldPosition = new Vector3();
  object.getWorldPosition(worldPosition);
  const box = object.isMesh ? new Box3().setFromObject(object, true) : null;
  const size = box ? box.getSize(new Vector3()) : null;
  const materials = object.isMesh
    ? (Array.isArray(object.material) ? object.material : [object.material])
        .filter(Boolean)
        .map((material: any) => {
          const label = material.name || material.type || 'unnamed';
          materialNames.add(label);
          return label;
        })
    : [];

  items.push({
    name: object.name || '(unnamed)',
    type: object.type,
    parent: object.parent?.name || null,
    visible: object.visible,
    worldPosition: [worldPosition.x, worldPosition.y, worldPosition.z],
    worldBoundingBox: box
      ? {min: [box.min.x, box.min.y, box.min.z], max: [box.max.x, box.max.y, box.max.z]}
      : null,
    dimensions: size ? [size.x, size.y, size.z] : null,
    material: materials,
    meshCount: object.isMesh ? 1 : 0,
    cameraCount: object.isCamera ? 1 : 0,
  });
});

const requestedPatterns = [
  'POVU Plaza', 'Hands of Growth', 'Water Wall', 'Living Wall', 'Glass Deck East',
  'Glass Deck West', 'Glass Deck', 'Production Hall', 'PRES_15_MIXING_HALL',
  'MIXING_PLATFORM', 'PROCESS_EPOXY_FLOOR', ...Array.from({length: 11}, (_, index) => `ProcessTank_${String(index + 1).padStart(2, '0')}`),
];

const normalized = (value: string) => value.toLowerCase().replace(/[\s_\-]+/g, '');
const matches = requestedPatterns.map((pattern) => ({
  pattern,
  matches: items.filter((item) => normalized(item.name).includes(normalized(pattern))),
}));

const report = {
  generatedAt: new Date().toISOString(),
  source: path.resolve(glbPath),
  counts: {nodes: nodeCount, meshes: meshCount, materials: materialNames.size, cameras: cameraCount},
  requestedPatterns: matches.map(({pattern, matches: found}) => ({
    pattern,
    count: found.length,
    names: found.map((item) => item.name),
  })),
  items,
};

await fs.mkdir(path.dirname(outputPath), {recursive: true});
await fs.writeFile(outputPath, JSON.stringify(report, null, 2));
console.log(JSON.stringify({outputPath, counts: report.counts, requestedPatterns: report.requestedPatterns}, null, 2));
