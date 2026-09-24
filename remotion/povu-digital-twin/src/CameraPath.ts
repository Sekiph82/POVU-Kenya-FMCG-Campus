import * as THREE from "three";

export type CameraPose = { position: [number, number, number]; target: [number, number, number] };
export const blenderToThree = (point: [number, number, number]): [number, number, number] => [point[0], point[2], -point[1]];

type Key = { frame: number; position: THREE.Vector3; target: THREE.Vector3 };

const key = (frame: number, position: [number, number, number], target: [number, number, number]): Key => ({
  frame,
  position: new THREE.Vector3(...position),
  target: new THREE.Vector3(...target),
});

const KEYS: Key[] = [
  key(0, [205, -230, 155], [150, -170, 105]),
  key(180, [145, -165, 92], [100, -120, 60]),
  key(330, [76, -124, 38], [20, -80, 8]),
  key(540, [-58, -140, 14], [-50, -92, 4.5]),
  key(630, [-112, -126, 15], [-108, -79, 5]),
  key(750, [-135, -116, 27], [-108, -79, 5]),
  key(990, [-58, -44, 14], [-4, -7, 8]),
  key(1200, [-28, -2, 11], [-17, 12, 4.7]),
  key(1440, [-55, -1, 12], [-30, 12, 5]),
  key(1620, [-45, -8, 11], [-30, 12, 5]),
  key(1799, [-40, -15, 10], [-25, 12, 5]),
];

const smooth = (t: number) => t * t * (3 - 2 * t);

export const getCameraPose = (frame: number): CameraPose => {
  const clamped = Math.max(KEYS[0].frame, Math.min(KEYS[KEYS.length - 1].frame, frame));
  let left = KEYS[0];
  let right = KEYS[KEYS.length - 1];
  for (let index = 0; index < KEYS.length - 1; index++) {
    if (clamped >= KEYS[index].frame && clamped <= KEYS[index + 1].frame) {
      left = KEYS[index];
      right = KEYS[index + 1];
      break;
    }
  }
  const t = smooth((clamped - left.frame) / Math.max(1, right.frame - left.frame));
  const position = left.position.clone().lerp(right.position, t);
  const target = left.target.clone().lerp(right.target, t);
  return {position: blenderToThree([position.x, position.y, position.z]), target: blenderToThree([target.x, target.y, target.z])};
};

export const createProjectionCamera = (width: number, height: number, frame: number) => {
  const camera = new THREE.PerspectiveCamera(58, width / height, 0.1, 2000);
  const pose = getCameraPose(frame);
  camera.position.set(...pose.position);
  camera.lookAt(...pose.target);
  camera.updateProjectionMatrix();
  return camera;
};
