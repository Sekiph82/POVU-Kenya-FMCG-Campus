export type Point = [number, number, number];

export type R02ShotTarget = {
  shotId: string;
  label: string;
  targetNames: string[];
  cameraPositionNames?: string[];
  cameraOffset: Point;
  fov: number;
};

/**
 * R02 is deliberately object-driven. The first resolvable name is a real
 * node in the frozen REV004.1 GLB; camera and label use the same node.
 */
export const R02_SHOT_TARGETS: Record<string, R02ShotTarget> = {
  "M06V02-S001": {shotId:"M06V02-S001", label:"Campus overview", targetNames:["NAV_TARGET_CAMPUS_AERIAL","PRES_01_CAMPUS_HERO"], cameraOffset:[-105,-125,72], fov:52},
  "M06V02-S002": {shotId:"M06V02-S002", label:"Production hall", targetNames:["PRES_06_PRODUCTION_FACADE","Production_Hall","PRODUCTION_ROOF"], cameraOffset:[78,-86,38], fov:48},
  "M06V02-S003": {shotId:"M06V02-S003", label:"Landscape and public realm", targetNames:["NAV_TARGET_ORGANIC_CANOPY","CANOPY_BRANCH_01","TREE_TRUNK_01"], cameraOffset:[-58,-62,30], fov:50},
  "M06V02-S004": {shotId:"M06V02-S004", label:"Smart wayfinding", targetNames:["SMART_TOTEM_CAMPUS_01_BODY","SMART_TOTEM_VIP_BODY"], cameraOffset:[-28,-42,16], fov:48},
  "M06V02-S005": {shotId:"M06V02-S005", label:"Arrival threshold", targetNames:["NAV_TARGET_MAIN_ARRIVAL","SMART_TOTEM_CAMPUS_01_BODY"], cameraOffset:[0,-34,13], fov:50},
  "M06V02-S006": {shotId:"M06V02-S006", label:"Ground solar field", targetNames:["SOLAR_ARRAY","SolarPanel"], cameraOffset:[45,-58,28], fov:50},
  "M06V02-S007": {shotId:"M06V02-S007", label:"Solar canopy", targetNames:["SOLAR_CARPORT_PANEL","SOLAR_CARPORT_POST"], cameraOffset:[36,-44,16], fov:48},
  "M06V02-S008": {shotId:"M06V02-S008", label:"Solar support equipment", targetNames:["SOLAR_INVERTER","SOLAR_POST"], cameraOffset:[28,-28,12], fov:46},
  "M06V02-S009": {shotId:"M06V02-S009", label:"Pedestrian-first arrival", targetNames:["NAV_TARGET_MAIN_ARRIVAL","AMR_SPINE"], cameraOffset:[0,-38,12], fov:50},
  "M06V02-S010": {shotId:"M06V02-S010", label:"POVU smart totem", targetNames:["SMART_TOTEM_VIP_BODY","SMART_TOTEM_VIP_SCREEN"], cameraOffset:[-28,-38,14], fov:46},
  "M06V02-S011": {shotId:"M06V02-S011", label:"Living wall", targetNames:["LIVING_WALL_PANEL","LIVING_WALL_PANEL001","VIP_LivingWall"], cameraOffset:[24,-34,12], fov:46},
  "M06V02-S012": {shotId:"M06V02-S012", label:"POVU water wall", targetNames:["POVU_WATER_WALL_7M","POVU_WATER_WALL_FRAME","POVU_WATER_WALL_BASIN"], cameraOffset:[28,-36,10], fov:44},
  "M06V02-S013": {shotId:"M06V02-S013", label:"VIP entrance", targetNames:["VIP_ENTRANCE_CANOPY","VIP_ENTRANCE_DOOR_L","VIP_ENTRANCE_LOBBY_FLOOR"], cameraOffset:[0,-36,10], fov:46},
  "M06V02-S014": {shotId:"M06V02-S014", label:"POVU VIP arrival", targetNames:["POVU_VIP_SIGN","VIP_ENTRANCE_SIGNAGE","POVU_WATER_WALL_7M"], cameraOffset:[-30,-38,16], fov:48},
  "M06V02-S015": {shotId:"M06V02-S015", label:"Hands of Growth", targetNames:["NAV_TARGET_HANDS_OF_GROWTH","HOG_HAND_LEFT","HOG_HAND_RIGHT","HANDS_OF_GROWTH"], cameraOffset:[-30,-40,24], fov:44},
  "M06V02-S016": {shotId:"M06V02-S016", label:"POVU plaza", targetNames:["NAV_TARGET_POVU_PLAZA","BENCH_PLANTER_01","SMART_TOTEM_CAMPUS_01_BODY"], cameraOffset:[28,-38,18], fov:50},
  "M06V02-S017": {shotId:"M06V02-S017", label:"Organic canopy", targetNames:["NAV_TARGET_ORGANIC_CANOPY","CANOPY_BRANCH_01"], cameraOffset:[-34,-32,20], fov:48},
  "M06V02-S018": {shotId:"M06V02-S018", label:"Garden pods", targetNames:["GARDENPOD_TABLE","GARDENPOD_DECK_00","GardenPod_Canopy"], cameraOffset:[24,-30,14], fov:48},
  "M06V02-S019": {shotId:"M06V02-S019", label:"Employee garden", targetNames:["EMPLOYEE_REFLECTION_POND","GARDEN_BENCH","TREE_CANOPY021"], cameraOffset:[32,-34,20], fov:48},
  "M06V02-S020": {shotId:"M06V02-S020", label:"Administration and HQ", targetNames:["ADMIN_HQ_ENTRANCE_SIGNAGE","ADMIN_HQ_ENTRANCE_CANOPY","ADMIN_HQ_ENTRANCE_DOOR_L"], cameraPositionNames:["PRES_14_HQ_EXPERIENCE"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S021": {shotId:"M06V02-S021", label:"R&D and QC centre", targetNames:["R_D_QC_ENTRANCE_SIGNAGE","R_D_QC_ENTRANCE_CANOPY","GREEN_ROOF_Admin_RD_QC"], cameraPositionNames:["PRES_14_HQ_EXPERIENCE"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S022": {shotId:"M06V02-S022", label:"POVU Academy", targetNames:["MULTIPURPOSE_STUDIO","EXPERIENCE_LINK","EXPERIENCE_ROOF"], cameraOffset:[45,-45,18], fov:44},
  "M06V02-S023": {shotId:"M06V02-S023", label:"Restaurant and café", targetNames:["CAFE_GLASS_FRONT","CAFE_TERRACE","RESTAURANT_ENTRANCE_SIGNAGE"], cameraPositionNames:["PRES_38_RESTAURANT_CAFE"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S024": {shotId:"M06V02-S024", label:"Wellness and recreation", targetNames:["WELLNESS_PAVILION","RECREATION_COURT","WELLNESS_ENTRANCE_SIGNAGE"], cameraPositionNames:["PRES_39_WELLNESS_RECREATION"], cameraOffset:[0,0,0], fov:46},
  "M06V02-S025": {shotId:"M06V02-S025", label:"Daycare and clinic", targetNames:["DAYCARE_ENTRANCE_SIGNAGE","DAYCARE_GARDEN","Daycare","CLINIC_ENTRY"], cameraPositionNames:["PRES_40_DAYCARE"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S027": {shotId:"M06V02-S027", label:"East Glass Deck stair", targetNames:["GLASS_DECK_EAST_STAIR_STEP_06","GLASS_DECK_EAST_STAIR"], cameraPositionNames:["PRES_GLASS_DECK_EAST_ACCESS"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S028": {shotId:"M06V02-S028", label:"West Glass Deck stair", targetNames:["GLASS_DECK_WEST_STAIR_STEP_06","GLASS_DECK_WEST_STAIR"], cameraOffset:[-80,-80,50], fov:44},
  "M06V02-S029": {shotId:"M06V02-S029", label:"Central Glass Deck stair", targetNames:["GLASS_DECK_CENTRAL_STAIR_STEP_06","GLASS_DECK_CENTRAL_STAIR"], cameraPositionNames:["PRES_GLASS_DECK_CENTRAL_ACCESS"], cameraOffset:[0,0,0], fov:44},
  "M06V02-S030": {shotId:"M06V02-S030", label:"Glass Deck link", targetNames:["GLASS_DECK_LINK","GLASS_DECK_LINK_FLOOR","NAV_TARGET_GLASS_DECK_INTERIOR"], cameraOffset:[-26,-28,14], fov:46},
  "M06V02-S031": {shotId:"M06V02-S031", label:"MES control room", targetNames:["MES_ROOM","MES_CONSOLE","MES_SCREEN"], cameraOffset:[-26,22,12], fov:44},
  "M06V02-S032": {shotId:"M06V02-S032", label:"Production hall", targetNames:["PRODUCTION_FLOOR","Production_Hall","PRES_08_PROCESS_HALL"], cameraOffset:[92,-60,30], fov:48},
  "M06V02-S033": {shotId:"M06V02-S033", label:"Raw material receiving", targetNames:["PRES_09_RM_LOGISTICS","RM_DOCK","RM_Truck_Yard"], cameraOffset:[-26,-28,13], fov:46},
  "M06V02-S034": {shotId:"M06V02-S034", label:"Chemical storage", targetNames:["Chemical_Compound","IBC_TANK","RM_PUMP_00"], cameraOffset:[-22,-26,12], fov:46},
  "M06V02-S035": {shotId:"M06V02-S035", label:"Raw material supermarket", targetNames:["RM_SUPERMARKET","RM_SUPER_BIN","RM_MANIFOLD"], cameraOffset:[-22,-26,12], fov:44},
  "M06V02-S036": {shotId:"M06V02-S036", label:"Wet processing and mixing", targetNames:["ProcessTank_01","MIXING_PLATFORM","LABEL_ANCHOR_PROCESS_TANK_01"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S037": {shotId:"M06V02-S037", label:"Utilities and process services", targetNames:["Utility_House","UTILITY_PIPE_BRIDGE","AIR_RECEIVER"], cameraOffset:[-30,-32,16], fov:46},
  "M06V02-S038": {shotId:"M06V02-S038", label:"Downstream process flow", targetNames:["FILLER_MONOBLOCK_01","EMPTY_BOTTLE_CONVEYOR","FILLED_CONVEYOR_01"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S039": {shotId:"M06V02-S039", label:"Bottle manufacturing", targetNames:["Bottle_BlowMolding","EMPTY_BOTTLE_CONVEYOR","HOPPER_DRYER"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S040": {shotId:"M06V02-S040", label:"Closure and trigger manufacturing", targetNames:["Caps_Triggers","CAP_ASSEMBLY","CAPPER_01"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S041": {shotId:"M06V02-S041", label:"Liquid filling", targetNames:["FILLER_MONOBLOCK_01","FILLER_CAROUSEL_01","DRUM_FILLER"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S042": {shotId:"M06V02-S042", label:"Liquid sachets", targetNames:["LIQUID_FFS_01","Liquid_Packing","FILLED_CONVEYOR_02"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S043": {shotId:"M06V02-S043", label:"Powder handling and packaging", targetNames:["POWDER_BAG_DUMP_00","POWDER_HOPPER_00","Powder_Packaging"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S044": {shotId:"M06V02-S044", label:"Toothpaste manufacture", targetNames:["Toothpaste","TOOTHPASTE_HOMOGENIZER","TUBE_FILLER"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S045": {shotId:"M06V02-S045", label:"Standard wet wipes", targetNames:["WIPES_UNWIND_STANDARD","WIPES_PACK_STANDARD","WIPES_OUT_STANDARD"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S046": {shotId:"M06V02-S046", label:"Medical and baby wipes", targetNames:["WIPES_UNWIND_MEDBABY","WIPES_PACK_MEDBABY","WIPES_OUT_MEDBABY"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S047": {shotId:"M06V02-S047", label:"Flushable wipes", targetNames:["WIPES_UNWIND_FLUSHABLE","WIPES_PACK_FLUSHABLE","WIPES_OUT_FLUSHABLE"], cameraOffset:[-18,-24,10], fov:44},
  "M06V02-S048": {shotId:"M06V02-S048", label:"Packaging materials warehouse", targetNames:["Packaging_Warehouse","PK_RACK_FRAME","PK_SUPERMARKET"], cameraOffset:[-22,-26,12], fov:44},
  "M06V02-S049": {shotId:"M06V02-S049", label:"End-of-line automation", targetNames:["ROBOT_PALLETIZER","ROBOT_ARM","POWDER_END_CONVEYOR"], cameraOffset:[-18,-24,11], fov:44},
  "M06V02-S050": {shotId:"M06V02-S050", label:"AMR logistics", targetNames:["AMR_SPINE","AMR_CROSS","AMR_00"], cameraOffset:[-22,-28,12], fov:44},
  "M06V02-S051": {shotId:"M06V02-S051", label:"Finished goods flow", targetNames:["FG_STAGE_PALLET_00","FG_LOAD","AMR_SPINE"], cameraOffset:[-22,-26,12], fov:44},
  "M06V02-S052": {shotId:"M06V02-S052", label:"Finished goods warehouse", targetNames:["FG_Warehouse","FG_RACK_FRAME","FG_PALLET_00"], cameraOffset:[-22,-26,12], fov:44},
  "M06V02-S053": {shotId:"M06V02-S053", label:"Dispatch and outbound", targetNames:["FG_DOCK","FG_LEVELER","FG_Truck_Yard"], cameraOffset:[-24,-30,14], fov:46},
  "M06V02-S054": {shotId:"M06V02-S054", label:"Utilities centre", targetNames:["Utility_House","UTILITY_PIPE_BRIDGE","AIR_RECEIVER"], cameraOffset:[-30,-32,16], fov:46},
  "M06V02-S055": {shotId:"M06V02-S055", label:"Water treatment", targetNames:["ETP","ETP_CONTROL","ETP_MBBR"], cameraOffset:[-30,-32,16], fov:46},
  "M06V02-S056": {shotId:"M06V02-S056", label:"Service infrastructure", targetNames:["UTILITY_PROCESS_FLOOR","Utility_House","WORKSHOP_BENCH"], cameraOffset:[-26,-30,14], fov:46},
  "M06V02-S057": {shotId:"M06V02-S057", label:"Fire and pedestrian safety", targetNames:["FIRE_HYDRANT_00","MUSTER_POINT_00","FIRE_ROUTE_MARK"], cameraOffset:[-26,-30,14], fov:46},
  "M06V02-S058": {shotId:"M06V02-S058", label:"Sustainability systems", targetNames:["SOLAR_ARRAY","SOLAR_CARPORT_PANEL","ETP"], cameraOffset:[-90,-110,58], fov:52},
  "M06V02-S059": {shotId:"M06V02-S059", label:"FMCG capability campus", targetNames:["Production_Hall","PRODUCTION_FLOOR","PRES_01_CAMPUS_HERO"], cameraOffset:[-92,-112,60], fov:52},
  "M06V02-S060": {shotId:"M06V02-S060", label:"People and public realm", targetNames:["HANDS_OF_GROWTH","NAV_TARGET_POVU_PLAZA","EMPLOYEE_REFLECTION_POND"], cameraOffset:[-86,-112,52], fov:52},
  "M06V02-S061": {shotId:"M06V02-S061", label:"Complete campus", targetNames:["NAV_TARGET_CAMPUS_AERIAL","PRES_01_CAMPUS_HERO"], cameraOffset:[-105,-125,72], fov:52},
  "M06V02-S062": {shotId:"M06V02-S062", label:"POVU Kenya FMCG Campus", targetNames:["POVU_VIP_SIGN","POVU_PRODUCTION_SIGN","PRES_01_CAMPUS_HERO"], cameraOffset:[-72,-98,42], fov:50},
};

export const FORBIDDEN_RENDER_TERMS = [
  "PRODUCTION MASSING",
  "LANDSCAPE FRAMEWORK",
  "UNCERTAIN CALLOUT",
  "DOCUMENTED NOT MODELED",
  "EVIDENCE BOUNDARY",
  "WORLD-TRACKED",
];
