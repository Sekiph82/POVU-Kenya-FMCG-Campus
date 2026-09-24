import React from "react";
import { useLoader, useThree } from "@react-three/fiber";
import { Html } from "@react-three/drei";
import { ThreeCanvas } from "@remotion/three";
import {
  AbsoluteFill,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import * as THREE from "three";
import { applyRev004MaterialSystem } from "./MaterialSystem";
import { TOUR_CHAPTERS, type TourChapter, type TourShot } from "./data/complete-tour-production-manifest";

const GLB = staticFile("POVU_REV004_1_FINAL_MASTER.glb");
type Point = [number, number, number];

const blenderToThree = ([x, y, z]: Point): Point => [x, z, -y];
const clamp01 = (value: number) => Math.max(0, Math.min(1, value));
const smooth = (value: number) => value * value * (3 - 2 * value);
const chapterIndexFor = (chapterId: string) => Math.max(0, TOUR_CHAPTERS.findIndex((chapter) => chapter.id === chapterId));
const textFor = (shot: TourShot) => (shot.features.join(" ") + " " + shot.targets.join(" ")).toUpperCase();

const anchorForShot = (shot: TourShot): Point => {
  const text = textFor(shot);
  if (text.includes("SOLAR_CARPORT") || text.includes("CANOPY-MOUNTED PV")) return [40, -89, 4];
  if (text.includes("SOLAR_ARRAY") || text.includes("GROUND/FIELD PV") || text.includes("LOW-MOUNTED")) return [75, 104, 3];
  if (text.includes("INVERTER") || text.includes("SUPPORT CLUSTER")) return [40, 91, 4];
  if (text.includes("HANDS OF GROWTH")) return [-108, -79, 5];
  if (text.includes("WATER WALL") || text.includes("LIVING WALL") || text.includes("VIP") || text.includes("SMART TOTEM")) return [-58, -92, 5];
  if (text.includes("PLAZA") || text.includes("LANDSCAPE") || text.includes("WAYFINDING") || text.includes("ARRIVAL")) return [-76, -77, 3];
  if (text.includes("EMPLOYEE GARDEN") || text.includes("ORGANIC CANOPY") || text.includes("GARDEN POD")) return [-65, -55, 4];
  if (text.includes("DAYCARE")) return [-132, -105, 6];
  if (text.includes("OCCUPATIONAL") || text.includes("CLINIC")) return [-45, -120, 5];
  if (text.includes("WELLNESS") || text.includes("RECREATION")) return [92, -102, 7];
  if (text.includes("RESTAURANT") || text.includes("CAFÉ") || text.includes("CAFE")) return [-18, -110, 6];
  if (text.includes("ADMINISTRATION") || text.includes("HQ")) return [-58, -80, 6];
  if (text.includes("R&D") || text.includes("QC")) return [-76, -80, 6];
  if (text.includes("TRAINING") || text.includes("ACADEMY")) return [-90, -70, 5];
  if (text.includes("GLASS DECK") || text.includes("MES") || text.includes("STAIR") || text.includes("LIFT")) return [0, 20, 9];
  if (text.includes("RECEIVING") || text.includes("RAW MATERIAL WAREHOUSE")) return [-70, 45, 4];
  if (text.includes("CHEMICAL")) return [-58, 47, 4];
  if (text.includes("SUPERMARKET")) return [-42, 47, 4];
  if (text.includes("FEEDING")) return [-20, 25, 5];
  if (text.includes("WET PROCESSING") || text.includes("MIXING")) return [0, 20, 6];
  if (text.includes("CIP") || text.includes("HYPOCHLORITE") || text.includes("UTILITY")) return [80, 52, 5];
  if (text.includes("BOTTLE")) return [52, 10, 4];
  if (text.includes("CLOSURE") || text.includes("CAPS") || text.includes("TRIGGER")) return [60, 31, 4];
  if (text.includes("FILLING")) return [50, 10, 4];
  if (text.includes("SACHET")) return [45, 22, 4];
  if (text.includes("POWDER")) return [-29, 48, 4];
  if (text.includes("TOOTHPASTE")) return [-8, 39, 4];
  if (text.includes("WIPES")) return [40, 45, 4];
  if (text.includes("PACKAGING MATERIAL")) return [-55, 48, 4];
  if (text.includes("END-OF-LINE")) return [55, 45, 4];
  if (text.includes("AMR") || text.includes("AUTOMATION")) return [30, -13, 3];
  if (text.includes("FINISHED GOODS")) return [72, -40, 4];
  if (text.includes("DISPATCH") || text.includes("TRUCK")) return [90, -55, 4];
  if (text.includes("ETP") || text.includes("ENVIRONMENTAL")) return [110, 42, 5];
  if (text.includes("FIRE") || text.includes("EMERGENCY") || text.includes("HSE") || text.includes("PEDESTRIAN")) return [75, -45, 4];
  if (text.includes("SUSTAINABILITY") || text.includes("PORTFOLIO")) return [25, 25, 5];
  if (text.includes("CAMPUS") || text.includes("ALL-CAMPUS")) return [0, 0, 0];
  return [0, 20, 6];
};

const cameraOffsetFor = (chapterIndex: number, shot: TourShot): Point => {
  const text = textFor(shot);
  if (chapterIndex === 0 || text.includes("AERIAL") || text.includes("SOLAR")) return [-105, -125, 72];
  if (text.includes("DETAIL") || text.includes("MACHINE") || text.includes("TANK")) return [-15, -20, 7];
  if (chapterIndex >= 5 && chapterIndex <= 9) return [-30, -36, 12];
  return [-24, -30, 10];
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

const poseFor = (chapter: TourChapter, frame: number, fps: number) => {
  const active = shotAtFrame(chapter, frame, fps);
  const currentTarget = anchorForShot(active.shot);
  const previousTarget = active.index > 0 ? anchorForShot(chapter.shots[active.index - 1]) : currentTarget;
  const localProgress = active.duration <= 1 ? 1 : active.local / active.duration;
  const move = smooth(clamp01(interpolate(localProgress, [0, 0.58, 1], [0, 1, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})));
  const target: Point = [
    previousTarget[0] + (currentTarget[0] - previousTarget[0]) * move,
    previousTarget[1] + (currentTarget[1] - previousTarget[1]) * move,
    previousTarget[2] + (currentTarget[2] - previousTarget[2]) * move,
  ];
  const offset = cameraOffsetFor(chapterIndexFor(chapter.id), active.shot);
  const position: Point = [target[0] + offset[0], target[1] + offset[1], Math.max(4, target[2] + offset[2])];
  return {position: blenderToThree(position), target: blenderToThree(target), active};
};

const CameraRig: React.FC<{chapter: TourChapter}> = ({chapter}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const {camera} = useThree();
  const perspective = camera as THREE.PerspectiveCamera;
  const pose = poseFor(chapter, frame, fps);
  perspective.position.set(...pose.position);
  perspective.lookAt(...pose.target);
  const text = textFor(pose.active.shot);
  perspective.fov = text.includes("AERIAL") || text.includes("SOLAR") ? 52 : text.includes("DETAIL") ? 44 : 48;
  perspective.aspect = width / height;
  perspective.near = 0.1;
  perspective.far = 2000;
  perspective.updateProjectionMatrix();
  return null;
};

const CampusModel: React.FC<{chapter: TourChapter}> = ({chapter}) => {
  const gltf = useLoader(GLTFLoader, GLB);
  const model = React.useMemo(() => {
    const scene = applyRev004MaterialSystem(gltf.scene);
    scene.traverse((object) => {
      const upper = object.name.toUpperCase();
      if (upper.includes("LIVING_WALL") || upper === "VIP_LIVINGWALL") object.visible = true;
    });
    return scene;
  }, [gltf.scene]);
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
  }, [chapterIndex, model]);
  return <primitive object={model} />;
};

const WATER_VERTEX = "varying vec2 vUv; void main(){vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}";
const WATER_FRAGMENT = "uniform float uTime; uniform vec3 uColor; varying vec2 vUv; void main(){float flow=sin((vUv.y+uTime*0.42)*28.0+sin(vUv.x*16.0)*1.8);float streak=smoothstep(0.15,0.95,0.5+0.5*flow);float glint=pow(max(0.0,sin((vUv.x+uTime*0.05)*34.0+vUv.y*8.0)),12.0);vec3 c=mix(uColor*0.52,vec3(0.82,0.98,1.0),0.22*streak+0.22*glint);float alpha=0.58+0.18*streak+0.12*glint;gl_FragColor=vec4(c,alpha);}";

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

const WorldLabels: React.FC<{chapter: TourChapter}> = ({chapter}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const {camera} = useThree();
  const active = poseFor(chapter, frame, fps).active;
  const anchor = blenderToThree(anchorForShot(active.shot));
  const projected = new THREE.Vector3(...anchor).project(camera);
  const left = Math.max(180, Math.min(width - 180, (projected.x * 0.5 + 0.5) * width));
  const top = Math.max(100, Math.min(height - 150, (-projected.y * 0.5 + 0.5) * height));
  const visible = projected.z > -1 && projected.z < 1;
  const text = textFor(active.shot);
  const shouldLabel = active.shot.confidence !== "CAVEATED" && !text.includes("CAMPUS ESTABLISHMENT");
  if (!shouldLabel) return null;
  const label = active.shot.features[0] || active.shot.targets[0];
  return <Html fullscreen style={{pointerEvents: "none"}}><div className="tour-world-label" style={{left, top, opacity: visible ? 1 : 0}}><i />{label}<small>{active.shot.id} · WORLD-TRACKED</small></div></Html>;
};

const TourOverlay: React.FC<{chapter: TourChapter}> = ({chapter}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const active = poseFor(chapter, frame, fps).active;
  const chapterIndex = chapterIndexFor(chapter.id);
  const title = chapter.title.replace(/^CH\d+\s+—\s+/i, "");
  const fade = interpolate(frame, [0, 18, Math.max(18, chapter.durationSec * fps - 30), chapter.durationSec * fps], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const text = textFor(active.shot);
  const showSolar = text.includes("SOLAR") || text.includes("SUSTAINABILITY");
  const caveat = active.shot.confidence === "CAVEATED";
  const showFlow = chapterIndex >= 6 && chapterIndex <= 8;
  return <div className="tour-overlay" style={{opacity: fade}}>
    <div className="tour-route"><span className="active">{title}</span><span> / </span><span>POVU KENYA DIGITAL TWIN</span></div>
    <div className="tour-chapter-title"><div className="tour-eyebrow">M07 COMPLETE FACTORY TOUR · {chapter.id}</div><div>{title}</div><small>{active.shot.features.slice(0, 2).join(" · ")}</small></div>
    <div className="tour-shot-meta">{active.shot.id}<br /><span>{active.shot.coverageIds.join(" · ")}</span></div>
    {showSolar && <div className="tour-callout solar-callout">2.5 MW SOLAR PV<small>PROJECT DOCUMENT LANGUAGE · 3 MODELED INSTALLATIONS</small></div>}
    {caveat && <div className="tour-caveat">{active.shot.overlay || "DOCUMENTED NOT MODELED"}<small>REV004.1 EVIDENCE BOUNDARY</small></div>}
    {showFlow && <div className="tour-process-flow">RAW MATERIALS <b>→</b> PROCESSING <b>→</b> FILLING <b>→</b> PACKAGING <b>→</b> DISPATCH</div>}
    <div className="tour-signature">POVU KENYA / COMPLETE CAMPUS &amp; FACTORY TOUR</div>
  </div>;
};

export const CompleteTourChapter: React.FC<{chapterId: string}> = ({chapterId}) => {
  const chapter = TOUR_CHAPTERS.find((item) => item.id === chapterId) || TOUR_CHAPTERS[0];
  const {width, height, fps} = useVideoConfig();
  const frame = useCurrentFrame();
  const text = textFor(poseFor(chapter, frame, fps).active.shot);
  const water = chapter.id === "CH03" && (text.includes("WATER") || text.includes("VIP") || text.includes("LIVING"));
  return <AbsoluteFill className="tour-root">
    <ThreeCanvas width={width} height={height} camera={{position: [0, 0, 10], fov: 48, near: 0.1, far: 2000}} gl={{antialias: true, alpha: false}}>
      <color attach="background" args={["#aebdca"]} />
      <fog attach="fog" args={["#aebdca", 180, 520]} />
      <ambientLight intensity={0.72} color="#e9f2f3" />
      <directionalLight position={[100, -120, 180]} intensity={1.35} color="#fff3d7" />
      <directionalLight position={[-100, 80, 90]} intensity={0.55} color="#b8e5f1" />
      <CameraRig chapter={chapter} />
      <CampusModel chapter={chapter} />
      <WaterWall visible={water} />
      <WorldLabels chapter={chapter} />
    </ThreeCanvas>
    <TourOverlay chapter={chapter} />
  </AbsoluteFill>;
};
