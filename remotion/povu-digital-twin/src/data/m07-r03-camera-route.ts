import * as THREE from "three";

export type BlenderPoint = [number, number, number];
export type R03RouteKeyframe = {
  frame: number;
  positionBlender: BlenderPoint;
  targetBlender: BlenderPoint;
  section: string;
};

export type R03CameraPose = {
  position: THREE.Vector3;
  target: THREE.Vector3;
  fov: number;
};

/**
 * The approved poc-r02 camera philosophy: few meaningful controls, one
 * persistent camera, smooth target and position interpolation. The route is
 * adapted only where R03 must prove the REV004.1 East Stair relationship.
 */
export const R03_ROUTE_KEYFRAMES: R03RouteKeyframe[] = [
  {frame: 0, positionBlender: [205, -230, 155], targetBlender: [150, -170, 105], section: "campus overview"},
  {frame: 180, positionBlender: [145, -165, 92], targetBlender: [100, -120, 60], section: "campus overview"},
  {frame: 330, positionBlender: [76, -124, 38], targetBlender: [20, -80, 8], section: "arrival approach"},
  {frame: 540, positionBlender: [-58, -140, 14], targetBlender: [-50, -92, 4.5], section: "VIP entrance and water wall"},
  {frame: 750, positionBlender: [-135, -116, 27], targetBlender: [-108, -79, 5], section: "Hands of Growth"},
  {frame: 990, positionBlender: [-18, -110, 11], targetBlender: [5, -80, 4], section: "people and campus facilities"},
  // Rise above the campus mass before crossing to the east edge. The previous
  // low diagonal crossed roof volumes and produced blank wall/roof frames.
  {frame: 1080, positionBlender: [-18, -100, 20], targetBlender: [5, -75, 6], section: "people and campus facilities"},
  {frame: 1140, positionBlender: [0, -50, 42], targetBlender: [35, 0, 6], section: "Glass Deck approach"},
  {frame: 1200, positionBlender: [35, 45, 28], targetBlender: [55, 68, 6], section: "Glass Deck approach"},
  {frame: 1350, positionBlender: [28, 58, 25], targetBlender: [55, 68, 6], section: "East Stair relationship"},
  {frame: 1410, positionBlender: [35, 65, 14], targetBlender: [55, 68, 5], section: "East Stair relationship"},
  {frame: 1500, positionBlender: [45, 72, 8], targetBlender: [55, 68, 5], section: "East Stair relationship"},
  {frame: 1650, positionBlender: [-69, -1, 10], targetBlender: [-20, 12, 7], section: "smart manufacturing"},
  {frame: 1799, positionBlender: [-72, -5, 14], targetBlender: [-17, 12, 4.7], section: "smart manufacturing"},
];

export const R03_FPS = 30;
export const R03_DURATION_IN_FRAMES = 1800;
export const R03_FOV = 52;

export const blenderToThree = ([x, y, z]: BlenderPoint): [number, number, number] => [x, z, -y];

const smooth = (value: number) => value * value * (3 - 2 * value);

export const getR03CameraPose = (frame: number): R03CameraPose => {
  const clamped = Math.max(0, Math.min(R03_DURATION_IN_FRAMES - 1, frame));
  let left = R03_ROUTE_KEYFRAMES[0];
  let right = R03_ROUTE_KEYFRAMES[R03_ROUTE_KEYFRAMES.length - 1];
  for (let index = 0; index < R03_ROUTE_KEYFRAMES.length - 1; index++) {
    const candidateLeft = R03_ROUTE_KEYFRAMES[index];
    const candidateRight = R03_ROUTE_KEYFRAMES[index + 1];
    if (clamped >= candidateLeft.frame && clamped <= candidateRight.frame) {
      left = candidateLeft;
      right = candidateRight;
      break;
    }
  }
  const rawT = (clamped - left.frame) / Math.max(1, right.frame - left.frame);
  const t = smooth(Math.max(0, Math.min(1, rawT)));
  const positionBlender = new THREE.Vector3(...left.positionBlender).lerp(new THREE.Vector3(...right.positionBlender), t);
  const targetBlender = new THREE.Vector3(...left.targetBlender).lerp(new THREE.Vector3(...right.targetBlender), t);
  return {
    position: new THREE.Vector3(...blenderToThree([positionBlender.x, positionBlender.y, positionBlender.z])),
    target: new THREE.Vector3(...blenderToThree([targetBlender.x, targetBlender.y, targetBlender.z])),
    fov: R03_FOV,
  };
};
