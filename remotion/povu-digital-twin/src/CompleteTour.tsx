import React from "react";
import { useLoader, useThree } from "@react-three/fiber";
import { Html } from "@react-three/drei";
import { ThreeCanvas } from "@remotion/three";
import { AbsoluteFill, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import * as THREE from "three";
import { applyRev004MaterialSystem } from "./MaterialSystem";
import { TOUR_CHAPTERS, type TourChapter, type TourShot } from "./data/complete-tour-production-manifest";
import { R02_SHOT_TARGETS, type Point, type R02ShotTarget } from "./data/complete-tour-r02-target-plan";

const GLB = staticFile("POVU_REV004_1_FINAL_MASTER.glb");
const blenderToThree = ([x, y, z]: Point): Point => [x, z, -y];
const clamp01 = (value: number) => Math.max(0, Math.min(1, value));
const smooth = (value: number) => value * value * (3 - 2 * value);
const chapterIndexFor = (chapterId: string) => Math.max(0, TOUR_CHAPTERS.findIndex((chapter) => chapter.id === chapterId));

type TargetPoint = {name: string; point: THREE.Vector3; quaternion?: THREE.Quaternion; found: boolean};
type TargetRegistry = {entries: Array<{name: string; upper: string; point: THREE.Vector3; quaternion: THREE.Quaternion}>};

const worldPointFor = (object: THREE.Object3D) => {
  const bounds = new THREE.Box3();
  object.traverse((child) => {
    if ((child as THREE.Mesh).isMesh) bounds.expandByObject(child);
  });
  if (!bounds.isEmpty()) return bounds.getCenter(new THREE.Vector3());
  return object.getWorldPosition(new THREE.Vector3());
};

const buildTargetRegistry = (model: THREE.Object3D): TargetRegistry => {
  model.updateMatrixWorld(true);
  const entries: TargetRegistry["entries"] = [];
  model.traverse((object) => {
    if (!object.name) return;
    entries.push({name: object.name, upper: object.name.toUpperCase(), point: worldPointFor(object), quaternion: object.getWorldQuaternion(new THREE.Quaternion())});
  });
  return {entries};
};

const resolveTarget = (plan: R02ShotTarget, registry: TargetRegistry): TargetPoint => {
  for (const query of plan.targetNames) {
    const normalized = query.toUpperCase().replace(/\*$/, "");
    const exact = registry.entries.find((entry) => entry.upper === normalized);
    if (exact) return {name: exact.name, point: exact.point.clone(), quaternion: exact.quaternion.clone(), found: true};
    const prefix = registry.entries.find((entry) => entry.upper.startsWith(normalized));
    if (prefix) return {name: prefix.name, point: prefix.point.clone(), quaternion: prefix.quaternion.clone(), found: true};
    const contains = registry.entries.find((entry) => entry.upper.includes(normalized));
    if (contains) return {name: contains.name, point: contains.point.clone(), quaternion: contains.quaternion.clone(), found: true};
  }
  return {name: "UNRESOLVED_TARGET", point: new THREE.Vector3(0, 0, 0), found: false};
};

const resolveNames = (names: string[] | undefined, registry: TargetRegistry): TargetPoint | null => {
  if (!names?.length) return null;
  return resolveTarget({...({} as R02ShotTarget), targetNames: names}, registry);
};

const planFor = (shot: TourShot): R02ShotTarget => R02_SHOT_TARGETS[shot.id] || {
  shotId: shot.id,
  label: shot.features[0] || "Campus feature",
  targetNames: [],
  cameraOffset: [0, -30, 12],
  fov: 48,
};

const shotAtFrame = (chapter: TourChapter, frame: number, fps: number) => {
  let cursor = 0;
  for (let index = 0; index < chapter.shots.length; index++) {
    const shot = chapter.shots[index];
    const duration = Math.max(1, Math.round(shot.durationSec * fps));
    if (frame <= cursor + duration - 1 || index === chapter.shots.length - 1) {
      return {shot, index, start: cursor, duration, local: Math.max(0, frame - cursor)};
    }
    cursor += duration;
  }
  return {shot: chapter.shots[0], index: 0, start: 0, duration: 1, local: 0};
};

const poseFor = (chapter: TourChapter, frame: number, fps: number, registry: TargetRegistry) => {
  const active = shotAtFrame(chapter, frame, fps);
  const currentPlan = planFor(active.shot);
  const current = resolveTarget(currentPlan, registry);
  const previousPlan = active.index > 0 ? planFor(chapter.shots[active.index - 1]) : currentPlan;
  const previous = active.index > 0 ? resolveTarget(previousPlan, registry) : current;
  const currentOffset = new THREE.Vector3(...blenderToThree(currentPlan.cameraOffset));
  const previousOffset = new THREE.Vector3(...blenderToThree(previousPlan.cameraOffset));
  const currentCameraAnchor = resolveNames(currentPlan.cameraPositionNames, registry);
  const previousCameraAnchor = active.index > 0 ? resolveNames(previousPlan.cameraPositionNames, registry) : currentCameraAnchor;
  const currentPosition = (currentCameraAnchor?.found ? currentCameraAnchor.point.clone() : current.point.clone()).add(currentOffset);
  const previousPosition = (previousCameraAnchor?.found ? previousCameraAnchor.point.clone() : previous.point.clone()).add(previousOffset);
  const localProgress = active.duration <= 1 ? 1 : active.local / active.duration;
  const travel = active.index === 0
    ? 1
    : smooth(clamp01(interpolate(localProgress, [0, 0.12, 0.82, 1], [0, 0.24, 0.92, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})));
  const cameraQuaternion = currentCameraAnchor?.found
    ? (previousCameraAnchor?.found
      ? previousCameraAnchor.quaternion!.clone().slerp(currentCameraAnchor.quaternion!, travel)
      : currentCameraAnchor.quaternion!.clone())
    : null;
  return {
    position: previousPosition.lerp(currentPosition, travel),
    target: previous.point.clone().lerp(current.point, travel),
    active,
    plan: currentPlan,
    resolvedTarget: current,
    travel,
    cameraQuaternion,
  };
};

const useCampusModel = () => {
  const gltf = useLoader(GLTFLoader, GLB);
  return React.useMemo(() => {
    const scene = applyRev004MaterialSystem(gltf.scene);
    scene.traverse((object) => {
      const upper = object.name.toUpperCase();
      if (upper.includes("LIVING_WALL") || upper === "VIP_LIVINGWALL") object.visible = true;
    });
    scene.updateMatrixWorld(true);
    return scene;
  }, [gltf.scene]);
};

const CameraRig: React.FC<{chapter: TourChapter; registry: TargetRegistry}> = ({chapter, registry}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const {camera} = useThree();
  const perspective = camera as THREE.PerspectiveCamera;
  const pose = poseFor(chapter, frame, fps, registry);
  perspective.position.copy(pose.position);
  if (pose.cameraQuaternion) perspective.quaternion.copy(pose.cameraQuaternion);
  else perspective.lookAt(pose.target);
  perspective.fov = pose.plan.fov;
  perspective.aspect = width / height;
  perspective.near = 0.1;
  perspective.far = 2000;
  perspective.updateProjectionMatrix();
  return null;
};

const CampusModel: React.FC<{chapter: TourChapter; model: THREE.Object3D}> = ({chapter, model}) => {
  const chapterIndex = chapterIndexFor(chapter.id);
  React.useEffect(() => {
    const interior = chapterIndex >= 5 && chapterIndex <= 9;
    const shell = ["PRODUCTION_ROOF", "PRODUCTION_WALL_NORTH", "PRODUCTION_WALL_SOUTH", "PRODUCTION_WALL_EAST", "PRODUCTION_WALL_WEST"];
    const hall = model.getObjectByName("Production_Hall");
    if (hall) hall.visible = false;
    shell.forEach((name) => {
      const object = model.getObjectByName(name);
      if (object) object.visible = !interior;
    });
    model.traverse((object) => {
      const upper = object.name.toUpperCase();
      if (upper.startsWith("PRODUCTION_") && upper.includes("FLOOR")) object.visible = true;
      if (upper.includes("LIVING_WALL")) object.visible = true;
    });
    model.updateMatrixWorld(true);
  }, [chapterIndex, model]);
  return <primitive object={model} />;
};

const WATER_VERTEX = "varying vec2 vUv; void main(){vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}";
const WATER_FRAGMENT = "uniform float uTime; uniform vec3 uColor; varying vec2 vUv; void main(){float flow=sin((vUv.y+uTime*0.42)*28.0+sin(vUv.x*16.0)*1.8);float streak=smoothstep(0.15,0.95,0.5+0.5*flow);float glint=pow(max(0.0,sin((vUv.x+uTime*0.05)*34.0+vUv.y*8.0)),12.0);vec3 c=mix(uColor*0.52,vec3(0.82,0.98,1.0),0.22*streak+0.22*glint);float alpha=0.58+0.18*streak+0.12*glint;gl_FragColor=vec4(c,alpha);} ";

const WaterWall: React.FC<{visible: boolean}> = ({visible}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const uniforms = React.useMemo(() => ({uTime: {value: 0}, uColor: {value: new THREE.Color("#55c9d4")}}), []);
  uniforms.uTime.value = frame / fps;
  return <group visible={visible}>
    <mesh position={[-42, 4.05, 91.15]}>
      <planeGeometry args={[11.8, 6.8, 32, 32]} />
      <shaderMaterial transparent depthWrite={false} side={THREE.DoubleSide} uniforms={uniforms} vertexShader={WATER_VERTEX} fragmentShader={WATER_FRAGMENT} />
    </mesh>
    <mesh position={[-42, 0.75, 93.8]} rotation={[-Math.PI / 2, 0, 0]}>
      <planeGeometry args={[13, 2.3]} />
      <meshPhysicalMaterial color="#3babb8" roughness={0.14} metalness={0.08} transparent opacity={0.76} />
    </mesh>
  </group>;
};

const WorldLabels: React.FC<{chapter: TourChapter; registry: TargetRegistry}> = ({chapter, registry}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const {camera} = useThree();
  const pose = poseFor(chapter, frame, fps, registry);
  if (!pose.resolvedTarget.found || pose.active.shot.id === "M06V02-S001") return null;
  const projected = pose.target.clone().project(camera);
  const left = Math.max(180, Math.min(width - 180, (projected.x * 0.5 + 0.5) * width));
  const top = Math.max(100, Math.min(height - 150, (-projected.y * 0.5 + 0.5) * height));
  const visible = projected.z > -1 && projected.z < 1;
  return <Html fullscreen style={{pointerEvents: "none"}}><div className="tour-world-label" style={{left, top, opacity: visible ? 1 : 0}}><i />{pose.plan.label}</div></Html>;
};

const TourOverlay: React.FC<{chapter: TourChapter; registry: TargetRegistry}> = ({chapter, registry}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pose = poseFor(chapter, frame, fps, registry);
  const chapterIndex = chapterIndexFor(chapter.id);
  const title = chapter.title.replace(/^CH\d+\s+—\s+/i, "");
  const fade = interpolate(frame, [0, 18, Math.max(18, chapter.durationSec * fps - 30), chapter.durationSec * fps], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const showSolar = ["M06V02-S006", "M06V02-S007", "M06V02-S008"].includes(pose.active.shot.id);
  const showFlow = chapterIndex >= 6 && chapterIndex <= 8;
  return <div className="tour-overlay" style={{opacity: fade}}>
    <div className="tour-route"><span className="active">{title}</span><span> / </span><span>POVU KENYA DIGITAL TWIN</span></div>
    <div className="tour-chapter-title"><div className="tour-eyebrow">POVU KENYA · COMPLETE CAMPUS &amp; FACTORY TOUR</div><div>{title}</div><small>{pose.plan.label}</small></div>
    {showSolar && <div className="tour-callout solar-callout">2.5 MW SOLAR PV</div>}
    {showFlow && <div className="tour-process-flow">RAW MATERIALS <b>→</b> PROCESSING <b>→</b> FILLING <b>→</b> PACKAGING <b>→</b> DISPATCH</div>}
    <div className="tour-signature">POVU KENYA / COMPLETE CAMPUS &amp; FACTORY TOUR</div>
  </div>;
};

export const CompleteTourChapter: React.FC<{chapterId: string}> = ({chapterId}) => {
  const chapter = TOUR_CHAPTERS.find((item) => item.id === chapterId) || TOUR_CHAPTERS[0];
  const {width, height, fps} = useVideoConfig();
  const model = useCampusModel();
  const registry = React.useMemo(() => buildTargetRegistry(model), [model]);
  const frame = useCurrentFrame();
  const active = poseFor(chapter, frame, fps, registry).active;
  const water = chapter.id === "CH03" && ["M06V02-S011", "M06V02-S012", "M06V02-S013", "M06V02-S014"].includes(active.shot.id);
  return <AbsoluteFill className="tour-root">
    <ThreeCanvas width={width} height={height} camera={{position: [0, 0, 10], fov: 48, near: 0.1, far: 2000}} gl={{antialias: true, alpha: false}}>
      <color attach="background" args={["#aebdca"]} />
      <fog attach="fog" args={["#aebdca", 180, 520]} />
      <ambientLight intensity={0.72} color="#e9f2f3" />
      <directionalLight position={[100, -120, 180]} intensity={1.35} color="#fff3d7" />
      <directionalLight position={[-100, 80, 90]} intensity={0.55} color="#b8e5f1" />
      <CameraRig chapter={chapter} registry={registry} />
      <CampusModel chapter={chapter} model={model} />
      <WaterWall visible={water} />
      <WorldLabels chapter={chapter} registry={registry} />
    </ThreeCanvas>
    <TourOverlay chapter={chapter} registry={registry} />
  </AbsoluteFill>;
};
