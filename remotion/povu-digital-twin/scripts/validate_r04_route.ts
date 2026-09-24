import fs from "node:fs";
import path from "node:path";
import * as THREE from "three";
import {R04_CALLOUTS, R04_DURATION_IN_FRAMES, R04_FOV, R04_FPS, R04_ROUTE_KEYFRAMES, getR04CameraPose} from "../src/data/m07-r04-long-form-route";

const root = path.resolve(process.cwd(), "..", "..");
const out = path.join(root, "output", "complete-tour-r04");
const catalogPath = path.join(root, "3d", "revisions", "REV004.2", "audit", "r04_target_catalog.json");
const catalog = JSON.parse(fs.readFileSync(catalogPath, "utf8")) as {items: Array<{name: string; type: string; world: number[]; bounds?: {center: number[]}}>};
fs.mkdirSync(out, {recursive: true});

const entries = catalog.items.map((item) => {
  const center = item.bounds?.center ?? item.world;
  return {
    name: item.name,
    upper: item.name.toUpperCase(),
    point: new THREE.Vector3(center[0], center[2], -center[1]),
  };
});

const resolve = (names: string[]) => {
  for (const query of names) {
    const normalized = query.toUpperCase().replace(/\*$/, "");
    const exact = entries.find((entry) => entry.upper === normalized);
    if (exact) return exact;
    const prefix = entries.find((entry) => entry.upper.startsWith(normalized));
    if (prefix) return prefix;
    const contains = entries.find((entry) => entry.upper.includes(normalized));
    if (contains) return contains;
  }
  return null;
};

const cameraAt = (frame: number) => {
  const pose = getR04CameraPose(frame);
  const camera = new THREE.PerspectiveCamera(R04_FOV, 16 / 9, 0.1, 2000);
  camera.position.copy(pose.position);
  camera.lookAt(pose.target);
  camera.updateProjectionMatrix();
  camera.updateMatrixWorld(true);
  return {camera, pose};
};

const directionFor = (frame: number) => {
  const {pose} = cameraAt(frame);
  return pose.target.clone().sub(pose.position).normalize();
};

let maxPositionDelta = 0;
let maxAngularDelta = 0;
let maxFovDelta = 0;
let maxPositionAcceleration = 0;
let maxAngularAcceleration = 0;
let maxPositionFrame = 0;
let maxAngularFrame = 0;
let maxPositionAccelerationFrame = 0;
let maxAngularAccelerationFrame = 0;
const samples: Array<{frame: number; position: THREE.Vector3; direction: THREE.Vector3}> = [];
let previousVelocity = 0;
let previousAngularVelocity = 0;
let previousPosition: THREE.Vector3 | null = null;
let previousDirection: THREE.Vector3 | null = null;

for (let frame = 0; frame < R04_DURATION_IN_FRAMES; frame++) {
  const {pose} = cameraAt(frame);
  const position = pose.position.clone();
  const direction = pose.target.clone().sub(pose.position).normalize();
  samples.push({frame, position, direction});
  if (previousPosition && previousDirection) {
    const positionDelta = position.distanceTo(previousPosition);
    const dot = THREE.MathUtils.clamp(direction.dot(previousDirection), -1, 1);
    const angularDelta = THREE.MathUtils.radToDeg(Math.acos(dot));
    const fovDelta = Math.abs(pose.fov - R04_FOV);
    if (positionDelta > maxPositionDelta) {maxPositionDelta = positionDelta; maxPositionFrame = frame;}
    if (angularDelta > maxAngularDelta) {maxAngularDelta = angularDelta; maxAngularFrame = frame;}
    if (fovDelta > maxFovDelta) maxFovDelta = fovDelta;
    const positionAcceleration = Math.abs(positionDelta - previousVelocity);
    const angularAcceleration = Math.abs(angularDelta - previousAngularVelocity);
    if (positionAcceleration > maxPositionAcceleration) {maxPositionAcceleration = positionAcceleration; maxPositionAccelerationFrame = frame;}
    if (angularAcceleration > maxAngularAcceleration) {maxAngularAcceleration = angularAcceleration; maxAngularAccelerationFrame = frame;}
    previousVelocity = positionDelta;
    previousAngularVelocity = angularDelta;
  }
  previousPosition = position;
  previousDirection = direction;
}

const discontinuities: Array<{frame: number; positionDelta: number; angularDelta: number}> = [];
for (let i = 1; i < samples.length; i++) {
  const positionDelta = samples[i].position.distanceTo(samples[i - 1].position);
  const angularDelta = THREE.MathUtils.radToDeg(Math.acos(THREE.MathUtils.clamp(samples[i].direction.dot(samples[i - 1].direction), -1, 1)));
  if (positionDelta > 10 || angularDelta > 12) discontinuities.push({frame: samples[i].frame, positionDelta, angularDelta});
}

const staticHolds: Array<{from: number; to: number; frames: number}> = [];
let holdStart = -1;
for (let frame = 451; frame < R04_DURATION_IN_FRAMES; frame++) {
  const delta = samples[frame].position.distanceTo(samples[frame - 1].position);
  const angular = THREE.MathUtils.radToDeg(Math.acos(THREE.MathUtils.clamp(samples[frame].direction.dot(samples[frame - 1].direction), -1, 1)));
  const negligible = delta < 0.0005 && angular < 0.0005;
  if (negligible && holdStart < 0) holdStart = frame - 1;
  if ((!negligible || frame === R04_DURATION_IN_FRAMES - 1) && holdStart >= 0) {
    const end = negligible && frame === R04_DURATION_IN_FRAMES - 1 ? frame : frame - 1;
    if (end - holdStart + 1 >= R04_FPS * 3) staticHolds.push({from: holdStart, to: end, frames: end - holdStart + 1});
    holdStart = -1;
  }
}

const calloutMap = R04_CALLOUTS.map((callout) => {
  const target = resolve(callout.targetNames);
  const checkpoints = [callout.from, Math.floor((callout.from + callout.to) / 2), callout.to].map((frame) => {
    if (!target) return {frame, insideFrustum: false};
    const {camera} = cameraAt(frame);
    const projected = target.point.clone().project(camera);
    return {frame, insideFrustum: projected.z > -1 && projected.z < 1 && Math.abs(projected.x) <= 1.04 && Math.abs(projected.y) <= 1.04, projected: {x: projected.x, y: projected.y, z: projected.z}};
  });
  return {id: callout.id, text: callout.text, targetQuery: callout.targetNames, resolvedTarget: target?.name ?? null, from: callout.from, to: callout.to, checkpoints};
});

const duplicateViews: Array<{first: string; second: string; positionDistance: number; angleDegrees: number}> = [];
const calloutSamples = R04_CALLOUTS.map((callout) => ({id: callout.id, ...cameraAt(Math.floor((callout.from + callout.to) / 2))}));
for (let i = 0; i < calloutSamples.length; i++) {
  for (let j = i + 1; j < calloutSamples.length; j++) {
    const a = calloutSamples[i];
    const b = calloutSamples[j];
    const positionDistance = a.pose.position.distanceTo(b.pose.position);
    const angleDegrees = THREE.MathUtils.radToDeg(Math.acos(THREE.MathUtils.clamp(a.pose.target.clone().sub(a.pose.position).normalize().dot(b.pose.target.clone().sub(b.pose.position).normalize()), -1, 1)));
    if (positionDistance < 1.5 && angleDegrees < 2) duplicateViews.push({first: a.id, second: b.id, positionDistance, angleDegrees});
  }
}

const continuity = {
  status: discontinuities.length === 0 && staticHolds.length === 0 && maxFovDelta === 0 ? "PASS" : "FAIL",
  fps: R04_FPS,
  durationFrames: R04_DURATION_IN_FRAMES,
  durationSeconds: R04_DURATION_IN_FRAMES / R04_FPS,
  fov: R04_FOV,
  persistentCamera: true,
  globalFrameClock: true,
  keyframeCount: R04_ROUTE_KEYFRAMES.length,
  maxPositionDelta, maxPositionFrame, maxAngularDelta, maxAngularFrame, maxFovDelta,
  discontinuities,
};
const acceleration = {maxPositionAcceleration, maxPositionAccelerationFrame, maxAngularAcceleration, maxAngularAccelerationFrame};
const visibility = {
  status: calloutMap.every((item) => item.resolvedTarget && item.checkpoints.some((checkpoint) => checkpoint.insideFrustum)) ? "PASS" : "FAIL",
  visualOcclusion: "REQUIRED_VISUAL_QA",
  callouts: calloutMap,
};
const duplicates = {status: duplicateViews.length === 0 ? "PASS" : "REVIEW", duplicates: duplicateViews};
const staticReport = {status: staticHolds.length === 0 ? "PASS" : "FAIL", openingExcludedThroughFrame: 450, holds: staticHolds};

fs.writeFileSync(path.join(out, "continuity-report.json"), JSON.stringify(continuity, null, 2));
fs.writeFileSync(path.join(out, "acceleration-report.json"), JSON.stringify(acceleration, null, 2));
fs.writeFileSync(path.join(out, "static-hold-report.json"), JSON.stringify(staticReport, null, 2));
fs.writeFileSync(path.join(out, "duplicate-view-report.json"), JSON.stringify(duplicates, null, 2));
fs.writeFileSync(path.join(out, "target-visibility-report.json"), JSON.stringify(visibility, null, 2));
fs.writeFileSync(path.join(out, "callout-target-map.json"), JSON.stringify(calloutMap, null, 2));
fs.writeFileSync(path.join(out, "complete-camera-route-report.json"), JSON.stringify({continuity, acceleration, staticHolds: staticReport, duplicates, visibility, route: R04_ROUTE_KEYFRAMES}, null, 2));
fs.writeFileSync(path.join(out, "callout-target-map.md"), calloutMap.map((item) => `- ${item.text}: ${item.resolvedTarget ?? "MISSING"} (${item.from}-${item.to})`).join("\n") + "\n");
console.log(JSON.stringify({continuity, staticHolds: staticHolds.length, duplicateViews: duplicateViews.length, visibility: visibility.status}, null, 2));
