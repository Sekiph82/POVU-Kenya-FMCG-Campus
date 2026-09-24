import React from "react";
import {useLoader, useThree} from "@react-three/fiber";
import {ThreeCanvas} from "@remotion/three";
import {AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig, staticFile} from "remotion";
import {GLTFLoader} from "three/examples/jsm/loaders/GLTFLoader.js";
import * as THREE from "three";
import {blenderToThree, createProjectionCamera, getCameraPose} from "./CameraPath";
import {applyRev004MaterialSystem} from "./MaterialSystem";

const GLB = staticFile("POVU_REV004_FINAL_MASTER.glb");
const ease = (frame: number, start: number, end: number) => interpolate(frame, [start, end], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.bezier(0.16, 1, 0.3, 1)});

const WATER_VERTEX = `varying vec2 vUv; void main(){vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`;
const WATER_FRAGMENT = `uniform float uTime; uniform vec3 uColor; varying vec2 vUv; void main(){float flow=sin((vUv.y+uTime*0.42)*28.0+sin(vUv.x*16.0)*1.8); float streak=smoothstep(0.15,0.95,0.5+0.5*flow); float glint=pow(max(0.0,sin((vUv.x+uTime*0.05)*34.0+vUv.y*8.0)),12.0); vec3 c=mix(uColor*0.52,vec3(0.82,0.98,1.0),0.22*streak+0.22*glint); float alpha=0.58+0.18*streak+0.12*glint; gl_FragColor=vec4(c,alpha);}`;

const WaterWall = () => {
  const frame = useCurrentFrame();
  const uniforms = React.useMemo(() => ({uTime: {value: 0}, uColor: {value: new THREE.Color("#55c9d4")}}), []);
  uniforms.uTime.value = frame / 30;
  return <>
    <mesh position={[-42, 4.05, 91.15]}>
      <planeGeometry args={[11.8, 6.8, 32, 32]} />
      <shaderMaterial transparent depthWrite={false} side={THREE.DoubleSide} uniforms={uniforms} vertexShader={WATER_VERTEX} fragmentShader={WATER_FRAGMENT} />
    </mesh>
    <mesh position={[-42, 0.75, 93.8]} rotation={[-Math.PI / 2, 0, 0]}>
      <planeGeometry args={[13, 2.3]} />
      <meshPhysicalMaterial color="#3babb8" roughness={0.14} metalness={0.08} transparent opacity={0.76} />
    </mesh>
  </>;
};

const VIPRuntimeArchitecture = () => <>
  <mesh position={[-68, 6, 91.35]}><boxGeometry args={[6.2, 7.1, 0.28]} /><meshPhysicalMaterial color="#3f884d" roughness={0.88} /></mesh>
  <mesh position={[-58, 4.3, 91.55]}><boxGeometry args={[6.7, 6.2, 0.16]} /><meshPhysicalMaterial color="#64c7d0" roughness={0.08} transmission={0.72} transparent opacity={0.78} /></mesh>
  <mesh position={[-61.5, 4.3, 91.68]}><boxGeometry args={[0.22, 6.45, 0.24]} /><meshPhysicalMaterial color="#26313a" roughness={0.34} metalness={0.48} /></mesh>
  <mesh position={[-54.5, 4.3, 91.68]}><boxGeometry args={[0.22, 6.45, 0.24]} /><meshPhysicalMaterial color="#26313a" roughness={0.34} metalness={0.48} /></mesh>
  <mesh position={[-58, 7.62, 92.15]}><boxGeometry args={[7.1, 0.24, 2.6]} /><meshPhysicalMaterial color="#b98748" roughness={0.28} metalness={0.4} /></mesh>
</>;

const HandsOfGrowthRuntime = ({visible}: {visible: boolean}) => <group visible={visible} position={[0, 0, 12]}>
  <mesh position={[-108, 0.45, 79]}><boxGeometry args={[9.2, 0.9, 7.6]} /><meshPhysicalMaterial color="#303b42" roughness={0.58} metalness={0.32} /></mesh>
  <mesh position={[-110.9, 2.9, 79]}><cylinderGeometry args={[0.75, 0.85, 4, 18]} /><meshPhysicalMaterial color="#b98748" roughness={0.42} metalness={0.35} /></mesh>
  <mesh position={[-105.1, 2.9, 79]}><cylinderGeometry args={[0.75, 0.85, 4, 18]} /><meshPhysicalMaterial color="#b98748" roughness={0.42} metalness={0.35} /></mesh>
  <mesh position={[-110.25, 5.25, 79]} rotation={[0, 0, -0.16]}><boxGeometry args={[2.5, 3.3, 1.44]} /><meshPhysicalMaterial color="#b98748" roughness={0.42} metalness={0.35} /></mesh>
  <mesh position={[-105.75, 5.25, 79]} rotation={[0, 0, 0.16]}><boxGeometry args={[2.5, 3.3, 1.44]} /><meshPhysicalMaterial color="#b98748" roughness={0.42} metalness={0.35} /></mesh>
  <mesh position={[-108, 4.0, 79]}><cylinderGeometry args={[0.38, 0.48, 6.1, 14]} /><meshPhysicalMaterial color="#6b4328" roughness={0.82} /></mesh>
  <mesh position={[-108, 8.1, 79]} scale={[1.25, 1, 1.05]}><dodecahedronGeometry args={[2.3, 1]} /><meshPhysicalMaterial color="#3f884d" roughness={0.88} /></mesh>
  <mesh position={[-106, 7.8, 79]} scale={[0.9, 0.8, 0.9]}><dodecahedronGeometry args={[1.8, 1]} /><meshPhysicalMaterial color="#6a9a4d" roughness={0.88} /></mesh>
</group>;

const CameraRig = () => {
  const frame = useCurrentFrame();
  const {camera} = useThree();
  const perspective = camera as THREE.PerspectiveCamera;
  const {width, height} = useVideoConfig();
  const pose = getCameraPose(frame);
  perspective.position.set(...pose.position);
  perspective.lookAt(...pose.target);
  perspective.fov = frame >= 1080 ? 58 : 50;
  perspective.aspect = width / height;
  perspective.near = 0.1;
  perspective.far = 2000;
  perspective.updateProjectionMatrix();
  return null;
};

const CampusModel = () => {
  const gltf = useLoader(GLTFLoader, GLB);
  const model = React.useMemo(() => applyRev004MaterialSystem(gltf.scene), [gltf.scene]);
  const frame = useCurrentFrame();
  const interior = frame >= 1080;
  const hogHero = frame >= 540 && frame <= 780;
  React.useEffect(() => {
    const hall = model.getObjectByName("Production_Hall");
    if (hall) hall.visible = false;
    const roof = model.getObjectByName("PRODUCTION_ROOF");
    if (roof) roof.visible = !interior;
    ["PRODUCTION_WALL_NORTH", "PRODUCTION_WALL_SOUTH", "PRODUCTION_WALL_EAST", "PRODUCTION_WALL_WEST"].forEach((name) => {
      const object = model.getObjectByName(name);
      if (object) object.visible = !interior;
    });
    model.traverse((object) => {
      const upper = object.name.toUpperCase();
      if (upper.startsWith("TREE_CANOPY") || upper.startsWith("SHADE_TREE") || upper.startsWith("ICOSPHERE") || upper.startsWith("CANOPY_BRANCH") || upper.startsWith("CANOPY_RIB") || upper === "DAYCARE_SHADE" || upper === "POVU_CANOPY_LIGHT_RING") object.visible = !hogHero;
    });
  }, [hogHero, interior, model]);
  return <primitive object={model} />;
};

const R02World = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  return <ThreeCanvas width={width} height={height} camera={{position: [0, 0, 10], fov: 42, near: 0.1, far: 2000}} gl={{antialias: true, alpha: false}}>
    <color attach="background" args={["#aebdca"]} />
    <fog attach="fog" args={["#aebdca", 180, 520]} />
    <ambientLight intensity={0.72} color="#e9f2f3" />
    <directionalLight position={[100, -120, 180]} intensity={1.35} color="#fff3d7" castShadow />
    <directionalLight position={[-100, 80, 90]} intensity={0.55} color="#b8e5f1" />
    <CameraRig />
    <CampusModel />
    <VIPRuntimeArchitecture />
    <HandsOfGrowthRuntime visible={frame >= 540 && frame <= 780} />
    <WaterWall />
  </ThreeCanvas>;
};

const ChapterTitle = () => {
  const frame = useCurrentFrame();
  const chapters = [
    {from: 0, to: 180, title: "POVU KENYA", sub: "WORLD-CLASS FMCG CAMPUS"},
    {from: 330, to: 540, title: "VIP ENTRANCE", sub: "Water • Green • Light"},
    {from: 540, to: 750, title: "HANDS OF GROWTH", sub: "People • Skills • Future"},
    {from: 900, to: 1200, title: "POVU GLASS DECK", sub: "Factory Experience"},
    {from: 1500, to: 1799, title: "POVU SMART MANUFACTURING", sub: "Designed for Flow • Safety • Automation"},
  ];
  const active = chapters.find((chapter) => frame >= chapter.from && frame <= chapter.to);
  if (!active) return null;
  const opacity = Math.min(ease(frame, active.from, active.from + 24), frame < active.to ? 1 : 1 - ease(frame, active.to, active.to + 24));
  return <div className="chapter-title" style={{opacity}}>
    <div className="eyebrow">POVU DIGITAL TWIN / R02</div>
    <div className="title">{active.title}</div>
    <div className="subtitle">{active.sub}</div>
  </div>;
};

const RouteIndicator = () => {
  const frame = useCurrentFrame();
  const labels = ["CAMPUS", "VIP", "LANDMARK", "GLASS DECK", "PRODUCTION"];
  const active = frame < 330 ? 0 : frame < 540 ? 1 : frame < 750 ? 2 : frame < 1200 ? 3 : 4;
  return <div className="route-indicator">{labels.map((label, index) => <span key={label} className={index === active ? "active" : ""}>{label}</span>)}</div>;
};

const TotemScreen = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [360, 390, 515, 545], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <div className="totem-screen" style={{opacity}}><span>POVU</span><strong>{frame < 450 ? "WELCOME TO POVU KENYA" : "WORLD-CLASS FMCG CAMPUS"}</strong></div>;
};

const SolarLabel = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [190, 215, 305, 330], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <div className="solar-label" style={{opacity}}>2.5 MW SOLAR PV<small>RENEWABLE CAMPUS ENERGY</small></div>;
};

const LabelOverlay = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const camera = React.useMemo(() => createProjectionCamera(width, height, frame), [frame, height, width]);
  const labels = frame >= 1370 && frame < 1510 ? [
    {text: "MIXING PLATFORM", point: [-8, 19, 7.8] as [number, number, number]},
    {text: "PROCESS TANK 03", point: [-17, 12, 8.4] as [number, number, number]},
  ] : frame >= 1510 ? [
    {text: "PROCESS TANK 03", point: [-17, 12, 8.4] as [number, number, number]},
    {text: "PROCESS TANK 07", point: [-55, 32, 8.4] as [number, number, number]},
    {text: "MIXING PLATFORM", point: [-8, 19, 7.8] as [number, number, number]},
  ] : [];
  return <>{labels.map((label) => {
    const projected = new THREE.Vector3(...blenderToThree(label.point)).project(camera);
    const rawLeft = (projected.x * 0.5 + 0.5) * width;
    const left = Math.max(180, Math.min(width - 180, rawLeft));
    const top = Math.max(90, Math.min(height - 130, (-projected.y * 0.5 + 0.5) * height));
    const visible = projected.z > -1 && projected.z < 1 && left > 40 && left < width - 40 && top > 50 && top < height - 60;
    return <div key={label.text} className="machine-label" style={{left, top, opacity: visible ? 1 : 0}}><i />{label.text}<small>WORLD-TRACKED ANCHOR</small></div>;
  })}</>;
};

const ProcessFlow = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [1330, 1370, 1550, 1600], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <div className="process-flow" style={{opacity}}>RAW MATERIAL <b>→</b> PROCESS <b>→</b> FILLING <b>→</b> PACKAGING <b>→</b> FINISHED GOODS</div>;
};

export const R02Video: React.FC = () => {
  const frame = useCurrentFrame();
  const fade = interpolate(frame, [0, 18, 1778, 1799], [1, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <AbsoluteFill className="r02-root" style={{opacity: fade}}><R02World /><div className="overlay"><ChapterTitle /><RouteIndicator /><SolarLabel /><TotemScreen /><ProcessFlow /><LabelOverlay /><div className="signature">POVU KENYA / DIGITAL TWIN R02</div></div></AbsoluteFill>;
};
