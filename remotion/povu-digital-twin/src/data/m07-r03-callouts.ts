export type R03Callout = {
  from: number;
  to: number;
  text: string;
  targetNames: string[];
};

export const R03_CALLOUTS: R03Callout[] = [
  {from: 300, to: 540, text: "POVU ENTRANCE / WATER WALL", targetNames: ["VIP_ENTRANCE_SIGNAGE", "POVU_WATER_WALL_7M", "VIP_ENTRANCE_CANOPY"]},
  {from: 560, to: 820, text: "HANDS OF GROWTH", targetNames: ["NAV_TARGET_HANDS_OF_GROWTH", "HANDS_OF_GROWTH", "HOG_HAND_LEFT"]},
  {from: 850, to: 1040, text: "RESTAURANT / POVU CAFE", targetNames: ["RESTAURANT_ENTRANCE_SIGNAGE", "CAFE_GLASS_FRONT", "CAFE_TERRACE"]},
  {from: 1230, to: 1515, text: "EAST STAIR / GLASS DECK", targetNames: ["GLASS_DECK_EAST_STAIR_STEP_06", "GLASS_DECK_EAST_STAIR"]},
  {from: 1530, to: 1799, text: "POVU SMART MANUFACTURING", targetNames: ["MIXING_PLATFORM", "ProcessTank_01", "PRODUCTION_FLOOR"]},
];

export const R03_OVERVIEW_LABELS = [
  {text: "R&D / QC", targetNames: ["R_D_QC_ENTRANCE_SIGNAGE", "R_D_QC_ENTRANCE_CANOPY"]},
  {text: "RESTAURANT / CAFE", targetNames: ["RESTAURANT_ENTRANCE_SIGNAGE", "CAFE_GLASS_FRONT"]},
  {text: "WELLNESS / RECREATION", targetNames: ["WELLNESS_ENTRANCE_SIGNAGE", "WELLNESS_PAVILION"]},
  {text: "POVU FACTORY", targetNames: ["PRODUCTION_PERSONNEL_ENTRANCE_SIGNAGE", "PRODUCTION_FLOOR"]},
];

