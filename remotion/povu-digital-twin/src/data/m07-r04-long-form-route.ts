import * as THREE from "three";

export type BlenderPoint = [number, number, number];
export type R04RouteKeyframe = {
  frame: number;
  positionBlender: BlenderPoint;
  targetBlender: BlenderPoint;
  section: string;
};

export type R04CameraPose = {
  position: THREE.Vector3;
  target: THREE.Vector3;
  fov: number;
};

export type R04Callout = {
  id: string;
  from: number;
  to: number;
  text: string;
  secondary?: string;
  targetNames: string[];
  section: string;
};

export type R04OverviewLabel = {text: string; targetNames: string[]};

export const R04_FPS = 30;
export const R04_FOV = 52;
export const R04_DURATION_IN_FRAMES = 14100;

/**
 * One persistent camera, one global frame clock, and the approved R03
 * Blender-to-Three conversion/interpolation philosophy. Keyframes are route
 * waypoints, not per-label cuts; callouts ride on the continuous travel.
 */
export const R04_ROUTE_KEYFRAMES: R04RouteKeyframe[] = [
  {frame: 0, positionBlender: [205, -230, 155], targetBlender: [150, -170, 105], section: "complete campus overview"},
  {frame: 225, positionBlender: [188, -214, 144], targetBlender: [118, -145, 84], section: "complete campus overview"},
  {frame: 449, positionBlender: [150, -178, 112], targetBlender: [72, -104, 46], section: "complete campus overview"},
  {frame: 850, positionBlender: [40, -128, 34], targetBlender: [-42, -92, 5], section: "arrival and water wall"},
  {frame: 1200, positionBlender: [-82, -124, 16], targetBlender: [-58, -92, 5], section: "arrival and entrance"},
  {frame: 1500, positionBlender: [-124, -116, 23], targetBlender: [-102, -79, 5], section: "Hands of Growth approach"},
  {frame: 1800, positionBlender: [-116, -104, 15], targetBlender: [-102, -79, 5], section: "Hands of Growth reveal"},
  {frame: 2100, positionBlender: [-92, -106, 15], targetBlender: [-76, -77, 3], section: "POVU Plaza"},
  {frame: 2400, positionBlender: [-45, -116, 16], targetBlender: [-58, -80, 4], section: "Admin and headquarters"},
  {frame: 2700, positionBlender: [-42, -112, 16], targetBlender: [-76, -80, 4], section: "R&D and QC Innovation Centre"},
  {frame: 3000, positionBlender: [28, -108, 18], targetBlender: [30, -60, 5], section: "Training and Academy"},
  {frame: 3300, positionBlender: [-24, -115, 15], targetBlender: [5, -81, 4], section: "Restaurant and POVU Cafe"},
  {frame: 3600, positionBlender: [58, -122, 20], targetBlender: [16, -81, 5], section: "Wellness and recreation"},
  {frame: 3900, positionBlender: [-118, -116, 17], targetBlender: [-105, -73, 4], section: "Daycare and occupational health"},
  {frame: 4050, positionBlender: [-40, -120, 15], targetBlender: [-18, -102, 4], section: "Occupational health"},
  {frame: 4200, positionBlender: [-96, -108, 18], targetBlender: [-90, -92, 6], section: "Employee gardens and social spaces"},
  {frame: 4500, positionBlender: [-20, -120, 20], targetBlender: [-10, -89, 6], section: "solar canopy"},
  {frame: 4800, positionBlender: [20, 65, 20], targetBlender: [48, 88, 3], section: "low mounted solar field"},
  {frame: 5100, positionBlender: [100, 75, 22], targetBlender: [30, 96, 3], section: "ground solar field"},
  {frame: 5400, positionBlender: [0, -50, 42], targetBlender: [35, 0, 6], section: "Glass Deck approach"},
  {frame: 5700, positionBlender: [45, 72, 5], targetBlender: [55, 68, 5], section: "East Glass Deck access"},
  {frame: 6000, positionBlender: [15, 32, 13], targetBlender: [0, 17, 8], section: "Central Glass Deck access"},
  {frame: 6300, positionBlender: [-58, -36, 13], targetBlender: [-55, -17, 8], section: "West Glass Deck access"},
  {frame: 6600, positionBlender: [-69, -1, 10], targetBlender: [-20, 12, 7], section: "Glass Deck production oversight"},
  {frame: 6900, positionBlender: [-132, 95, 26], targetBlender: [-91, 100, 5], section: "raw materials transition"},
  {frame: 7200, positionBlender: [-117, 72, 18], targetBlender: [-91, 100, 5], section: "receiving and storage"},
  {frame: 7500, positionBlender: [-117, 72, 18], targetBlender: [-91, 100, 6], section: "raw materials warehouse"},
  {frame: 7800, positionBlender: [-67, 30, 14], targetBlender: [-45, 58, 4], section: "feeding"},
  {frame: 8100, positionBlender: [-73, -12, 16], targetBlender: [-55, 12, 6], section: "wet processing and mixing"},
  {frame: 8400, positionBlender: [34, -14, 13], targetBlender: [52, 10, 5], section: "bottle manufacturing"},
  {frame: 8700, positionBlender: [50, 7, 13], targetBlender: [68, 31, 5], section: "closures and trigger spray"},
  {frame: 9000, positionBlender: [-18, -29, 14], targetBlender: [0, -5, 5], section: "liquid filling"},
  {frame: 9300, positionBlender: [-8, -26, 13], targetBlender: [10, -2, 5], section: "liquid sachets"},
  {frame: 9600, positionBlender: [-76, 12, 13], targetBlender: [-58, 36, 5], section: "powder handling and packaging"},
  {frame: 9900, positionBlender: [-26, 15, 13], targetBlender: [-8, 39, 5], section: "toothpaste"},
  {frame: 10200, positionBlender: [-2, 12, 13], targetBlender: [16, 36, 5], section: "standard wet wipes"},
  {frame: 10500, positionBlender: [-2, 21, 13], targetBlender: [16, 45, 5], section: "medical and baby wipes"},
  {frame: 10800, positionBlender: [-2, 30, 13], targetBlender: [16, 54, 5], section: "flushable wipes"},
  {frame: 11100, positionBlender: [-34, 53, 20], targetBlender: [-12, 79, 8], section: "packaging materials warehouse"},
  {frame: 11400, positionBlender: [-34, 53, 20], targetBlender: [-12, 79, 6], section: "packaging supermarket"},
  {frame: 11700, positionBlender: [37, -26, 15], targetBlender: [55, -2, 5], section: "end of line"},
  {frame: 12000, positionBlender: [8, -41, 13], targetBlender: [30, -13, 5], section: "AMR logistics"},
  {frame: 12300, positionBlender: [58, -51, 21], targetBlender: [80, -25, 8], section: "finished goods warehouse"},
  {frame: 12600, positionBlender: [85, -75, 19], targetBlender: [109, -45, 6], section: "dispatch"},
  {frame: 12900, positionBlender: [66, 43, 22], targetBlender: [96, 75, 7], section: "utilities"},
  {frame: 13200, positionBlender: [80, 2, 20], targetBlender: [110, 34, 6], section: "water treatment"},
  {frame: 13500, positionBlender: [50, 42, 18], targetBlender: [76, 72, 7], section: "fire and HSE"},
  {frame: 13800, positionBlender: [205, -225, 136], targetBlender: [100, -100, 45], section: "final campus hero"},
  {frame: 14099, positionBlender: [198, -218, 132], targetBlender: [96, -96, 43], section: "final campus hero"},
];

export const R04_OVERVIEW_LABELS: R04OverviewLabel[] = [
  {text: "ADMIN / HQ", targetNames: ["ADMIN_HQ_ENTRANCE_CANOPY"]},
  {text: "R&D / QC INNOVATION CENTRE", targetNames: ["R_D_QC_ENTRANCE_CANOPY"]},
  {text: "RESTAURANT / POVU CAFÉ", targetNames: ["RESTAURANT_ENTRANCE_CANOPY"]},
  {text: "WELLNESS / RECREATION", targetNames: ["WELLNESS_ENTRANCE_CANOPY"]},
  {text: "DAYCARE", targetNames: ["DAYCARE_ENTRANCE_CANOPY"]},
  {text: "SMART MANUFACTURING", targetNames: ["PRODUCTION_FLOOR"]},
  {text: "SOLAR FIELD", targetNames: ["SOLAR_ARRAY"]},
];

export const R04_CALLOUTS: R04Callout[] = [
  {id: "arrival-living-wall", from: 780, to: 1050, text: "LIVING WALL", secondary: "POVU arrival landscape", targetNames: ["LIVING_WALL_PANEL", "VIP_LivingWall"], section: "arrival and entrance"},
  {id: "arrival-water-wall", from: 900, to: 1180, text: "WATER WALL", secondary: "moving water / basin / entrance", targetNames: ["WATERWALL_FRAME", "WATER_WALL_STRUCTURE"], section: "arrival and water wall"},
  {id: "arrival-identity", from: 1040, to: 1260, text: "POVU ENTRANCE", secondary: "arrival doors and visitor space", targetNames: ["VIP_ENTRANCE_DOOR_L", "VIP_ENTRANCE_LOBBY_FLOOR"], section: "arrival and entrance"},
  {id: "flagship-totem", from: 1120, to: 1380, text: "SMART TOTEM", secondary: "flagship visitor wayfinding", targetNames: ["SMART_TOTEM_VIP_BODY", "SMART_TOTEM_VIP_SCREEN"], section: "arrival and entrance"},
  {id: "hands-of-growth", from: 1600, to: 2020, text: "HANDS OF GROWTH", secondary: "People • Skills • Future", targetNames: ["HOG_PALM_L", "HOG_PALM_R", "HANDS_OF_GROWTH"], section: "Hands of Growth reveal"},
  {id: "plaza", from: 1990, to: 2250, text: "POVU PLAZA", secondary: "public realm and social space", targetNames: ["POVU_PLAZA", "NAV_TARGET_POVU_PLAZA"], section: "POVU Plaza"},
  {id: "admin", from: 2280, to: 2520, text: "ADMIN / HQ", targetNames: ["ADMIN_HQ_ENTRANCE_SIGNAGE", "ADMIN_HQ_ENTRANCE_CANOPY"], section: "Admin and headquarters"},
  {id: "rd-qc", from: 2580, to: 2820, text: "R&D / QC INNOVATION CENTRE", targetNames: ["R_D_QC_ENTRANCE_SIGNAGE", "R_D_QC_ENTRANCE_CANOPY"], section: "R&D and QC Innovation Centre"},
  {id: "academy", from: 2880, to: 3120, text: "TRAINING / ACADEMY", targetNames: ["MULTIPURPOSE_STUDIO", "EXPERIENCE_LINK", "EXPERIENCE_ROOF"], section: "Training and Academy"},
  {id: "cafe", from: 3180, to: 3420, text: "RESTAURANT / POVU CAFÉ", targetNames: ["RESTAURANT_ENTRANCE_SIGNAGE", "CAFE_GLASS_FRONT", "CAFE_TERRACE"], section: "Restaurant and POVU Cafe"},
  {id: "wellness", from: 3480, to: 3720, text: "WELLNESS / RECREATION", targetNames: ["WELLNESS_ENTRANCE_SIGNAGE", "WELLNESS_PAVILION", "RECREATION_COURT"], section: "Wellness and recreation"},
  {id: "daycare", from: 3780, to: 3980, text: "DAYCARE", targetNames: ["DAYCARE_ENTRANCE_SIGNAGE", "DAYCARE_GARDEN"], section: "Daycare and occupational health"},
  {id: "clinic", from: 3900, to: 4140, text: "OCCUPATIONAL HEALTH", targetNames: ["CLINIC_ENTRY", "CLINIC_CANOPY"], section: "Daycare and occupational health"},
  {id: "gardens", from: 4080, to: 4350, text: "EMPLOYEE GARDENS", secondary: "garden pods and social spaces", targetNames: ["EMPLOYEE_REFLECTION_POND", "GARDEN_BENCH", "PRES_42_EMPLOYEE_GARDENS"], section: "Employee gardens and social spaces"},
  {id: "solar-canopy", from: 4380, to: 4680, text: "SOLAR CANOPY", secondary: "canopy panels / supports / arrival use", targetNames: ["SOLAR_CARPORT_PANEL", "SOLAR_CARPORT_POST"], section: "solar canopy"},
  {id: "solar-low", from: 4680, to: 4980, text: "LOW-MOUNTED SOLAR", secondary: "panel field / mounting", targetNames: ["SolarPanel", "SolarPanel001"], section: "low mounted solar field"},
  {id: "solar-field", from: 4980, to: 5280, text: "SOLAR FIELD", secondary: "ground array / inverter support", targetNames: ["SOLAR_ARRAY", "SOLAR_INVERTER"], section: "ground solar field"},
  {id: "east-stair", from: 5550, to: 5820, text: "EAST GLASS DECK ACCESS", secondary: "physical stair approach", targetNames: ["GLASS_DECK_EAST_STAIR", "GLASS_DECK_EAST_STAIR_STEP_06"], section: "East Glass Deck access"},
  {id: "central-stair", from: 5850, to: 6120, text: "CENTRAL STAIR / LIFT", secondary: "Glass Deck access", targetNames: ["GLASS_DECK_CENTRAL_STAIR", "GLASS_DECK_CENTRAL_LIFT"], section: "Central Glass Deck access"},
  {id: "west-stair", from: 6150, to: 6420, text: "WEST GLASS DECK ACCESS", secondary: "physical stair approach", targetNames: ["GLASS_DECK_WEST_STAIR", "GLASS_DECK_WEST_STAIR_STEP_06"], section: "West Glass Deck access"},
  {id: "production-oversight", from: 6450, to: 6780, text: "PRODUCTION OVERSIGHT", secondary: "Glass Deck experience", targetNames: ["GLASS_DECK_LINK_FLOOR", "MES_GLASS", "MES_ROOM"], section: "Glass Deck production oversight"},
  {id: "raw-materials", from: 6840, to: 7140, text: "RAW MATERIALS", secondary: "receiving and storage", targetNames: ["RM_DOCK", "RM_Truck_Yard", "RM_Warehouse"], section: "receiving and storage"},
  {id: "receiving", from: 7080, to: 7380, text: "RECEIVING / STORAGE", targetNames: ["RM_DOCK", "RM_LEVELER", "RM_LOAD"], section: "receiving and storage"},
  {id: "feeding", from: 7680, to: 7980, text: "FEEDING", secondary: "material supermarket / manifolds", targetNames: ["RM_SUPERMARKET", "RM_MANIFOLD", "RM_FEED_HEADER"], section: "feeding"},
  {id: "wet-processing", from: 7980, to: 8280, text: "WET PROCESSING / MIXING", secondary: "tank hall / pipework / platforms", targetNames: ["ProcessTank_01", "MIXING_PLATFORM", "PROCESS_EPOXY_FLOOR"], section: "wet processing and mixing"},
  {id: "manufacturing", from: 8280, to: 8580, text: "MANUFACTURING", secondary: "bottle production", targetNames: ["Bottle_BlowMolding", "EMPTY_BOTTLE_CONVEYOR", "HOPPER_DRYER"], section: "bottle manufacturing"},
  {id: "closures", from: 8580, to: 8880, text: "CLOSURES / TRIGGER SPRAY", targetNames: ["Caps_Triggers", "CAP_ASSEMBLY", "TRIGGER_ASSEMBLY"], section: "closures and trigger spray"},
  {id: "filling", from: 8880, to: 9180, text: "FILLING", secondary: "liquid filling / conveyors", targetNames: ["FILLER_MONOBLOCK_01", "FILLER_CAROUSEL_01", "FILLED_CONVEYOR_01"], section: "liquid filling"},
  {id: "sachets", from: 9180, to: 9480, text: "SACHET PACKAGING", targetNames: ["Liquid_Packing", "LIQUID_FFS_01", "FILLED_CONVEYOR_02"], section: "liquid sachets"},
  {id: "powder", from: 9480, to: 9780, text: "POWDER", secondary: "handling and packaging", targetNames: ["POWDER_BAG_DUMP_00", "POWDER_HOPPER_00", "Powder_Packaging"], section: "powder handling and packaging"},
  {id: "toothpaste", from: 9780, to: 10080, text: "TOOTHPASTE", secondary: "mixing / filling / packing", targetNames: ["TOOTHPASTE_HOMOGENIZER", "TUBE_FILLER", "TOOTHPASTE_FFS"], section: "toothpaste"},
  {id: "wipes-standard", from: 10080, to: 10380, text: "WET WIPES", secondary: "standard line", targetNames: ["WIPES_UNWIND_STANDARD", "WIPES_PACK_STANDARD", "WIPES_OUT_STANDARD"], section: "standard wet wipes"},
  {id: "wipes-medbaby", from: 10380, to: 10680, text: "WET WIPES", secondary: "medical and baby line", targetNames: ["WIPES_UNWIND_MEDBABY", "WIPES_PACK_MEDBABY", "WIPES_OUT_MEDBABY"], section: "medical and baby wipes"},
  {id: "wipes-flushable", from: 10680, to: 10980, text: "WET WIPES", secondary: "flushable line", targetNames: ["WIPES_UNWIND_FLUSHABLE", "WIPES_PACK_FLUSHABLE", "WIPES_OUT_FLUSHABLE"], section: "flushable wipes"},
  {id: "packaging", from: 10980, to: 11280, text: "PACKAGING MATERIALS", secondary: "warehouse and supermarket", targetNames: ["Packaging_Warehouse", "PK_RACK_FRAME", "PK_SUPERMARKET"], section: "packaging materials warehouse"},
  {id: "eol", from: 11280, to: 11610, text: "END OF LINE", secondary: "palletizing / conveyors", targetNames: ["ROBOT_PALLETIZER", "ROBOT_ARM", "POWDER_END_CONVEYOR"], section: "end of line"},
  {id: "amr", from: 11820, to: 12120, text: "AMR / AGV LOGISTICS", secondary: "smart internal movement", targetNames: ["AMR_SPINE", "AMR_CROSS", "AMR_00"], section: "AMR logistics"},
  {id: "finished-goods", from: 12120, to: 12480, text: "FINISHED GOODS", secondary: "warehouse movement", targetNames: ["FG_Warehouse", "FG_STAGE_PALLET_00", "FG_RACK_FRAME"], section: "finished goods warehouse"},
  {id: "dispatch", from: 12480, to: 12780, text: "DISPATCH", secondary: "outbound flow", targetNames: ["FG_DOCK", "FG_LEVELER", "FG_Truck_Yard"], section: "dispatch"},
  {id: "utilities", from: 12780, to: 13080, text: "UTILITIES", secondary: "service infrastructure", targetNames: ["Utility_House", "UTILITY_PIPE_BRIDGE", "AIR_RECEIVER"], section: "utilities"},
  {id: "etp", from: 13080, to: 13380, text: "WATER TREATMENT", secondary: "ETP systems", targetNames: ["ETP", "ETP_CONTROL", "ETP_MBBR"], section: "water treatment"},
  {id: "fire-hse", from: 13380, to: 13680, text: "FIRE / HSE", secondary: "safe movement and emergency systems", targetNames: ["FIRE_PUMP_HOUSE", "FIRE_WATER_TANK", "FIRE_ROUTE_MARK"], section: "fire and HSE"},
];

export const R04_PHASES = [
  [0, 450, "COMPLETE CAMPUS OVERVIEW"],
  [450, 1380, "ARRIVAL / POVU ENTRANCE"],
  [1380, 2250, "HANDS OF GROWTH / PEOPLE CAMPUS"],
  [2250, 4380, "PEOPLE + CAMPUS FACILITIES"],
  [4380, 5280, "SUSTAINABILITY SYSTEMS"],
  [5280, 6780, "GLASS DECK / PRODUCTION OVERSIGHT"],
  [6780, 8280, "RAW MATERIALS / WET PROCESSING"],
  [8280, 10980, "MANUFACTURING"],
  [10980, 12780, "PACKAGING / LOGISTICS / DISPATCH"],
  [12780, 13680, "UTILITIES / WATER / HSE"],
  [13680, 14100, "POVU KENYA FMCG CAMPUS"],
] as const;

export const blenderToThree = ([x, y, z]: BlenderPoint): [number, number, number] => [x, z, -y];

const smooth = (value: number) => value * value * (3 - 2 * value);

export const getR04CameraPose = (frame: number): R04CameraPose => {
  const clamped = Math.max(0, Math.min(R04_DURATION_IN_FRAMES - 1, frame));
  let left = R04_ROUTE_KEYFRAMES[0];
  let right = R04_ROUTE_KEYFRAMES[R04_ROUTE_KEYFRAMES.length - 1];
  for (let index = 0; index < R04_ROUTE_KEYFRAMES.length - 1; index++) {
    const candidateLeft = R04_ROUTE_KEYFRAMES[index];
    const candidateRight = R04_ROUTE_KEYFRAMES[index + 1];
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
    fov: R04_FOV,
  };
};
