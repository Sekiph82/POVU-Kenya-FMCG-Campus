import React from "react";
import {useLoader, useThree} from "@react-three/fiber";
import {ThreeCanvas} from "@remotion/three";
import {AbsoluteFill, interpolate, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {GLTFLoader} from "three/examples/jsm/loaders/GLTFLoader.js";
import * as THREE from "three";
import {applyRev004MaterialSystem} from "./MaterialSystem";
import {R04_CALLOUTS, R04_OVERVIEW_LABELS, R04_PHASES, getR04CameraPose, type R04Callout} from "./data/m07-r04-long-form-route";

const GLB = staticFile("POVU_REV004_2_FINAL_MASTER.glb");

type RegistryEntry = {name: string; upper: string; point: THREE.Vector3};
type Registry = {entries: RegistryEntry[]};

const worldPointFor = (object: THREE.Object3D) => {
  const bounds = new THREE.Box3();
  object.traverse((child) => {
    if ((child as THREE.Mesh).isMesh) bounds.expandByObject(child);
  });
  return bounds.isEmpty() ? object.getWorldPosition(new THREE.Vector3()) : bounds.getCenter(new THREE.Vector3());
};

const buildRegistry = (model: THREE.Object3D): Registry => {
  model.updateMatrixWorld(true);
  const entries: RegistryEntry[] = [];
  model.traverse((object) => {
    if (object.name) entries.push({name: object.name, upper: object.name.toUpperCase(), point: worldPointFor(object)});
  });
  return {entries};
};

const resolveTarget = (names: string[], registry: Registry): RegistryEntry | null => {
  for (const query of names) {
    const normalized = query.toUpperCase().replace(/\*$/, "");
    const exact = registry.entries.find((entry) => entry.upper === normalized);
    if (exact) return exact;
    const prefix = registry.entries.find((entry) => entry.upper.startsWith(normalized));
    if (prefix) return prefix;
    const contains = registry.entries.find((entry) => entry.upper.includes(normalized));
    if (contains) return contains;
  }
  return null;
};

const project = (point: THREE.Vector3, camera: THREE.Camera, width: number, height: number) => {
  const projected = point.clone().project(camera);
  const x = (projected.x * 0.5 + 0.5) * width;
  const y = (-projected.y * 0.5 + 0.5) * height;
  return {
    left: Math.max(115, Math.min(width - 115, x)),
    top: Math.max(80, Math.min(height - 100, y)),
    visible: projected.z > -1 && projected.z < 1 && Math.abs(projected.x) <= 1.04 && Math.abs(projected.y) <= 1.04,
  };
};

const CameraRig: React.FC = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const {camera} = useThree();
  const perspective = camera as THREE.PerspectiveCamera;
  const pose = getR04CameraPose(frame);
  perspective.position.copy(pose.position);
  perspective.lookAt(pose.target);
  perspective.fov = pose.fov;
  perspective.aspect = width / height;
  perspective.near = 0.1;
  perspective.far = 2000;
  perspective.updateProjectionMatrix();
  return null;
};

const CampusModel: React.FC<{model: THREE.Object3D}> = ({model}) => {
  const frame = useCurrentFrame();
  const factoryInterior = frame >= 6600;
  React.useEffect(() => {
    const hall = model.getObjectByName("Production_Hall");
    if (hall) hall.visible = false;
    const shell = ["PRODUCTION_ROOF", "PRODUCTION_WALL_NORTH", "PRODUCTION_WALL_SOUTH", "PRODUCTION_WALL_EAST", "PRODUCTION_WALL_WEST"];
    shell.forEach((name) => {
      const object = model.getObjectByName(name);
      if (object) object.visible = !factoryInterior;
    });
    model.traverse((object) => {
      const upper = object.name.toUpperCase();
      if (upper.includes("LIVING_WALL")) object.visible = true;
      if (upper.startsWith("PRODUCTION_") && upper.includes("FLOOR")) object.visible = true;
    });
    model.updateMatrixWorld(true);
  }, [factoryInterior, model]);
  return <primitive object={model} />;
};

const WATER_VERTEX = "varying vec2 vUv; void main(){vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}";
const WATER_FRAGMENT = "uniform float uTime; uniform vec3 uColor; varying vec2 vUv; void main(){float flow=sin((vUv.y+uTime*0.42)*28.0+sin(vUv.x*16.0)*1.8);float streak=smoothstep(0.15,0.95,0.5+0.5*flow);float glint=pow(max(0.0,sin((vUv.x+uTime*0.05)*34.0+vUv.y*8.0)),12.0);vec3 c=mix(uColor*0.52,vec3(0.82,0.98,1.0),0.22*streak+0.22*glint);float alpha=0.58+0.18*streak+0.12*glint;gl_FragColor=vec4(c,alpha);} ";

const WaterWall: React.FC = () => {
  const frame = useCurrentFrame();
  const uniforms = React.useMemo(() => ({uTime: {value: 0}, uColor: {value: new THREE.Color("#55c9d4")}}), []);
  uniforms.uTime.value = frame / 30;
  const visible = frame >= 720 && frame <= 1260;
  return <group visible={visible}>
    <mesh position={[-42, 4.05, 91.15]}><planeGeometry args={[11.8, 6.8, 32, 32]} /><shaderMaterial transparent depthWrite={false} side={THREE.DoubleSide} uniforms={uniforms} vertexShader={WATER_VERTEX} fragmentShader={WATER_FRAGMENT} /></mesh>
    <mesh position={[-42, 0.75, 93.8]} rotation={[-Math.PI / 2, 0, 0]}><planeGeometry args={[13, 2.3]} /><meshPhysicalMaterial color="#3babb8" roughness={0.14} metalness={0.08} transparent opacity={0.76} /></mesh>
  </group>;
};

const TargetCallout: React.FC<{registry: Registry; callout: R04Callout; camera: THREE.Camera; width: number; height: number}> = ({registry, callout, camera, width, height}) => {
  const target = resolveTarget(callout.targetNames, registry);
  if (!target) return null;
  const screen = project(target.point, camera, width, height);
  return <div className="tour-world-label" style={{left: screen.left, top: screen.top, opacity: screen.visible ? 1 : 0}}><i />{callout.text}{callout.secondary && <small>{callout.secondary}</small>}</div>;
};

const OverviewLabels: React.FC<{registry: Registry; camera: THREE.Camera; width: number; height: number}> = ({registry, camera, width, height}) => {
  const frame = useCurrentFrame();
  if (frame > 450) return null;
  return <div className="r03-overview-labels">{R04_OVERVIEW_LABELS.map((label) => {
    const target = resolveTarget(label.targetNames, registry);
    if (!target) return null;
    const screen = project(target.point, camera, width, height);
    return <div key={label.text} className="r03-overview-label" style={{left: screen.left, top: screen.top, opacity: screen.visible ? 1 : 0}}>{label.text}</div>;
  })}</div>;
};

const FLOW_LABELS = ["RAW MATERIALS", "RECEIVING / STORAGE", "FEEDING", "WET PROCESSING / MIXING", "MANUFACTURING", "FILLING", "PACKAGING", "EOL", "PALLETIZING", "FINISHED GOODS", "DISPATCH"];

const flowIndex = (frame: number) => {
  if (frame < 6780 || frame > 12800) return -1;
  return Math.max(0, Math.min(FLOW_LABELS.length - 1, Math.floor((frame - 6780) / 550)));
};

const Overlay: React.FC<{registry: Registry; camera: THREE.Camera; width: number; height: number}> = ({registry, camera, width, height}) => {
  const frame = useCurrentFrame();
  const phase = R04_PHASES.find(([from, to]) => frame >= from && frame < to) || R04_PHASES[R04_PHASES.length - 1];
  const fade = interpolate(frame, [0, 24, 14040, 14099], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const callout = R04_CALLOUTS.find((item) => frame >= item.from && frame <= item.to);
  const flow = flowIndex(frame);
  return <div className="r03-overlay" style={{opacity: fade}}>
    <OverviewLabels registry={registry} camera={camera} width={width} height={height} />
    <div className="r03-route"><span>{phase[2]}</span><b> / </b>POVU KENYA FMCG CAMPUS</div>
    <div className="r03-title"><div className="r03-eyebrow">COMPLETE CAMPUS & FACTORY TOUR</div><div>{phase[2]}</div><small>One continuous journey through the campus</small></div>
    <div className="r03-signature">POVU KENYA / PEOPLE • SKILLS • FUTURE</div>
    {callout && <TargetCallout registry={registry} callout={callout} camera={camera} width={width} height={height} />}
    {flow >= 0 && <div className="r03-progress" style={{bottom: 52}}><span style={{width: `${((flow + 1) / FLOW_LABELS.length) * 100}%`}} /></div>}
    {flow >= 0 && <div className="tour-process-flow">{FLOW_LABELS.map((label, index) => <React.Fragment key={label}><span style={{color: index === flow ? "#70d5d8" : "#e8e2d2"}}>{label}</span>{index < FLOW_LABELS.length - 1 && <b>→</b>}</React.Fragment>)}</div>}
    <div className="r03-progress"><span style={{width: `${(frame / (14100 - 1)) * 100}%`}} /></div>
  </div>;
};

export const R04Video: React.FC = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const gltf = useLoader(GLTFLoader, GLB);
  const model = React.useMemo(() => applyRev004MaterialSystem(gltf.scene), [gltf.scene]);
  const registry = React.useMemo(() => buildRegistry(model), [model]);
  const projectionCamera = React.useMemo(() => {
    const pose = getR04CameraPose(frame);
    const camera = new THREE.PerspectiveCamera(pose.fov, width / height, 0.1, 2000);
    camera.position.copy(pose.position);
    camera.lookAt(pose.target);
    camera.updateProjectionMatrix();
    camera.updateMatrixWorld(true);
    return camera;
  }, [frame, height, width]);
  return <AbsoluteFill className="r03-root">
    <ThreeCanvas width={width} height={height} camera={{position: [0, 0, 10], fov: 52, near: 0.1, far: 2000}} gl={{antialias: true, alpha: false}}>
      <color attach="background" args={["#aebdca"]} />
      <fog attach="fog" args={["#aebdca", 180, 520]} />
      <ambientLight intensity={0.72} color="#e9f2f3" />
      <directionalLight position={[100, -120, 180]} intensity={1.35} color="#fff3d7" />
      <directionalLight position={[-100, 80, 90]} intensity={0.55} color="#b8e5f1" />
      <CameraRig />
      <CampusModel model={model} />
      <WaterWall />
    </ThreeCanvas>
    <Overlay registry={registry} camera={projectionCamera} width={width} height={height} />
  </AbsoluteFill>;
};
