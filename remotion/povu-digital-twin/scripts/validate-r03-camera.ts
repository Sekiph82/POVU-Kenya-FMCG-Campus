import * as THREE from "three";
import {getR03CameraPose, R03_DURATION_IN_FRAMES, R03_FPS, R03_FOV, R03_ROUTE_KEYFRAMES} from "../src/data/m07-r03-camera-route";

const forwardAt = (frame: number) => {
  const camera = new THREE.PerspectiveCamera(R03_FOV, 16 / 9, 0.1, 2000);
  const pose = getR03CameraPose(frame);
  camera.position.copy(pose.position);
  camera.lookAt(pose.target);
  const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion).normalize();
  return {position: pose.position, forward, fov: pose.fov};
};

const angleDeg = (a: THREE.Vector3, b: THREE.Vector3) => THREE.MathUtils.radToDeg(Math.acos(Math.max(-1, Math.min(1, a.dot(b)))));
const frames = Array.from({length: R03_DURATION_IN_FRAMES}, (_, frame) => forwardAt(frame));
let maxPositionDelta = 0;
let maxPositionFrame = 0;
let maxAngularDelta = 0;
let maxAngularFrame = 0;
let maxFovDelta = 0;
let maxFovFrame = 0;
let maxAcceleration = 0;
let maxAccelerationFrame = 0;
let maxAngularAcceleration = 0;
let maxAngularAccelerationFrame = 0;
const velocity: number[] = [0];
const angularVelocity: number[] = [0];
const fovDeltas: number[] = [0];

for (let frame = 1; frame < frames.length; frame++) {
  const positionDelta = frames[frame].position.distanceTo(frames[frame - 1].position);
  const angularDelta = angleDeg(frames[frame].forward, frames[frame - 1].forward);
  const fovDelta = Math.abs(frames[frame].fov - frames[frame - 1].fov);
  velocity.push(positionDelta);
  angularVelocity.push(angularDelta);
  fovDeltas.push(fovDelta);
  if (positionDelta > maxPositionDelta) { maxPositionDelta = positionDelta; maxPositionFrame = frame; }
  if (angularDelta > maxAngularDelta) { maxAngularDelta = angularDelta; maxAngularFrame = frame; }
  if (fovDelta > maxFovDelta) { maxFovDelta = fovDelta; maxFovFrame = frame; }
}
for (let frame = 2; frame < frames.length; frame++) {
  const acceleration = Math.abs(velocity[frame] - velocity[frame - 1]);
  const angularAcceleration = Math.abs(angularVelocity[frame] - angularVelocity[frame - 1]);
  if (acceleration > maxAcceleration) { maxAcceleration = acceleration; maxAccelerationFrame = frame; }
  if (angularAcceleration > maxAngularAcceleration) { maxAngularAcceleration = angularAcceleration; maxAngularAccelerationFrame = frame; }
}

const discontinuities = [
  ...frames.map((_, frame) => ({frame, kind: "position", value: velocity[frame]})).filter((item) => item.value > 3),
  ...frames.map((_, frame) => ({frame, kind: "orientation", value: angularVelocity[frame]})).filter((item) => item.value > 5),
  ...frames.map((_, frame) => ({frame, kind: "fov", value: fovDeltas[frame]})).filter((item) => item.value > 0.01),
];

const report = {
  status: discontinuities.length === 0 ? "PASS" : "FAIL",
  composition: {fps: R03_FPS, durationInFrames: R03_DURATION_IN_FRAMES, durationSeconds: R03_DURATION_IN_FRAMES / R03_FPS, fov: R03_FOV},
  cameraSystem: {persistentCamera: true, hardCuts: 0, controlPointCount: R03_ROUTE_KEYFRAMES.length, interpolation: "smoothstep position and target interpolation"},
  maxFrameToFramePositionDelta: {value: maxPositionDelta, frame: maxPositionFrame},
  maxFrameToFrameAngularDeltaDegrees: {value: maxAngularDelta, frame: maxAngularFrame},
  maxFrameToFrameFovDelta: {value: maxFovDelta, frame: maxFovFrame},
  maxPositionAccelerationDelta: {value: maxAcceleration, frame: maxAccelerationFrame},
  maxAngularAccelerationDelta: {value: maxAngularAcceleration, frame: maxAngularAccelerationFrame},
  discontinuities,
  keyframes: R03_ROUTE_KEYFRAMES,
};
console.log(JSON.stringify(report, null, 2));

