# POVU SOLAR COVERAGE REPORT V01

## Source and method

- Frozen source: `3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb`
- Required SHA-256 verified: `BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A`
- Supporting source: `3d/revisions/REV004.1/REV004_1_ARCHITECTURAL_MANIFEST.json`, REV004.1 reload inventory, M03/M04/M05 logs and the V03 clean-master manifest.
- Solar objects were grouped by contiguous semantic naming and world bounds. Individual repeated panel objects are not treated as separate presentation destinations.

## Solar location SOL-01 — SOLAR_ARRAY field

- Type: ground/field PV proxy.
- Semantic IDs: `SOLAR_ARRAY` through `SOLAR_ARRAY083`; associated `SOLAR_POST*`; `SOLAR_INVERTER`.
- Modeled panel surfaces: 84.
- Approximate extent: X `27.0–110.0`, Y `94.5–121.5`, Z `2.2–3.0` for the panel surfaces.
- Campus relationship: north/east campus sustainability field; inverter is modeled near X `40`, Y `91`.
- Beneath/around: open field context and campus edge; no named seating or rest area was identified under this installation.
- Functional relationship: renewable generation and utility interface.
- Recommended shots: high establishing view, slow descending oblique, row/detail hold, inverter return.
- Estimated screen time: 18 seconds in CH02, plus 18 seconds in the CH02 inverter shot and the CH11 synthesis.
- Evidence class: A for modeled semantic group; exact installed capacity remains a project-document question.

## Solar location SOL-02 — SolarPanel field

- Type: low-mounted panel field; exact mounting relationship is not explicitly documented in the available repository evidence.
- Semantic IDs: `SolarPanel` through `SolarPanel047`.
- Modeled panel surfaces: 48.
- Approximate extent: X `44.0–122.0`, Y `86.8–109.2`, Z `2.05–2.75`.
- Campus relationship: north/east campus, spatially near SOL-01 and the modeled inverter.
- Beneath/around: open campus/utility context; no named seating, charging infrastructure or social use was identified beneath the panels.
- Functional relationship: additional modeled PV field.
- Recommended shots: separate oblique from SOL-01, slow lateral pass, location overlay, inverter relationship.
- Estimated screen time: 18 seconds in CH02 plus synthesis coverage.
- Evidence class: B — clearly modeled, but not independently confirmed by a named external project document in the workspace.

## Solar location SOL-03 — SOLAR_CARPORT canopy

- Type: canopy-mounted PV / carport proxy.
- Semantic IDs: `SOLAR_CARPORT_PANEL` through `SOLAR_CARPORT_PANEL010`; `SOLAR_CARPORT_POST` through `SOLAR_CARPORT_POST010`.
- Modeled panel surfaces: 11.
- Modeled supports: 11.
- Approximate extent: X `-14.5–94.5`, Y `-92.0–-86.0`, Z `5.28–6.32` for panels; support posts extend from approximately Z `1.2` to `5.6`.
- Campus relationship: south campus edge / long canopy row.
- Beneath/around: ground-level under-canopy space and adjacent arrival/public-realm edge. No named seating/rest object was confirmed in the REV004.1 semantic manifest; M07 must show only what is visibly modeled.
- Functional relationship: renewable canopy and shade structure.
- Recommended shots: full row context, camera lowering to human height, under-canopy inspection, adjacent path/landscape relationship, return to sustainability context.
- Estimated screen time: 20 seconds in CH02 plus synthesis coverage.
- Evidence class: A for modeled canopy group; parking/social use is not asserted without additional documentation.

## Associated support cluster requiring clarification

`SOLAR_POST` through `SOLAR_POST013` form a 14-object support cluster approximately around X `-45–39`, Y `-56–-50`, with no matching panel surfaces in the REV004.1 solar category. It is not counted as a fourth PV installation. M07 should either show it as an unpaired support/solar-related element with a caveat or omit it from the solar narrative pending owner confirmation.

## Capacity and documentation boundary

The R02 overlay uses the documented-looking label `2.5 MW SOLAR PV`, and the V03 planning manifest names a `2.5 MW Solar Energy System`. The external budget/technical workbook was not present in the repository or available workspace during M06. The storyboard may use `2.5 MW SOLAR PV` only as a project-provided presentation label, not as a claim that 4,200 individual panels are modeled.

## Mandatory under-canopy coverage

SOL-03 receives the required sequence: context → canopy relationship → camera lowering → under-canopy space → visible ground/path/landscape function → return to wider sustainability context. Because no named seating object was found, the film must not claim shaded seating unless a future owner-supplied document or approved revision confirms it.

`TOTAL SOLAR LOCATIONS IDENTIFIED: 3`
