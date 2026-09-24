# M03 — REV004 FINAL ARCHITECTURAL MASTER — V01 GPT PROMPT

## Mission
Create the final presentation-grade architectural Blender master for the POVU Kenya Integrated FMCG Campus before Remotion POC R02. Preserve REV003 unchanged and produce a new REV004 master. This is a structural/architectural/semantic finalization pass, not merely a render-material pass.

## Authoritative local project context
- Working project: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus`
- Git repository working tree (if available): `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus-repo`
- Current source GLB previously used for the successful Remotion POC: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d-jutsu-Untitled-3D-Jutsu-2026-09-21-07-44-56.glb`
- Presentation/masterplan reference: `C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\POVU_Kenya_World_Class_FMCG_Campus_Masterplan_V2_HSE.pptx`

Never overwrite REV003 or the successful R01 Remotion output.

## Governing design intent
The campus is a 7-hectare, people-first, automation-ready integrated FMCG campus. Preserve the masterplan logic: protected pedestrian movement; separate raw-material, packaging, finished-goods, truck and heavy-service flows; front-of-house people-first character; industrial logistics at rear/flanks. Preserve the Glass Deck concept: approximately 2,000 m², floor-to-ceiling acoustic glazing, direct production oversight, East stair, West stair, and Central stair + lift access.

This remains a concept/presentation digital twin, not a permit/construction set. Do not invent detailed engineering claims.

## Phase 0 — Audit before modification
1. Locate the actual Blender source/master used to create the current GLB. Do not rebuild the campus from scratch if the Blender master exists.
2. Save a protected backup/checkpoint before modification.
3. Audit scene graph, collections, object names, entrances, façades, Glass Deck access, Water Wall, Living Wall, Hands of Growth, Smart Totems, solar field, roofs/walls, loading/service openings, landscape destinations and major building signage.
4. Produce a machine-readable before/after inventory and record all objects added, removed, renamed or structurally changed.
5. Do not guess coordinates when existing geometry provides them.

# REQUIRED REV004 CHANGES

## 1. VIP Entrance — make it unmistakably a real entrance
The Living Wall + POVU Water Wall zone is the principal VIP entrance and must visually read as such.

Create/refine a presentation-grade entrance assembly including:
- wide automatic double glass entrance doors;
- graphite/dark architectural frames;
- restrained bronze/champagne architectural accent/portal;
- appropriate entrance canopy/portal if needed to establish hierarchy;
- threshold and pedestrian approach/paving;
- clear sightline to the doors;
- warm interior lobby/read-through where practical;
- appropriate POVU identity/signage without obscuring the door.

The Living Wall and Water Wall must frame the entrance, not hide it.

## 2. POVU Water Wall structural preparation
The existing POVU wall is intended to be an architectural waterfall/water wall.

Preserve/create separate semantic geometry wherever practical:
- `WATER_WALL_STRUCTURE`
- `WATER_WALL_WATER_SURFACE`
- `WATER_WALL_POVU_SIGNAGE`
- `WATER_WALL_BASIN`

Do not bake a fake waterfall animation into Blender if that would reduce GLB portability. The water surface must be separable so Remotion/Three.js can apply a deterministic animated falling-water shader in R02.

The basin/catchment and water path must make physical visual sense at concept level.

## 3. Other campus entrances
Audit every major occupied or operational building. Ensure entrances exist, are accessible, face sensible approach routes and are visually distinguishable from service/loading openings.

At minimum audit/refine as applicable:
- Admin/HQ;
- R&D/QC;
- Academy/training;
- restaurant/café;
- wellness;
- daycare;
- occupational health/first-aid;
- Production Hall staff access;
- Raw Material / Packaging warehouse staff access;
- Finished Goods / Dispatch staff access;
- Utilities/workshop/service areas.

Do not place decorative doors with no sensible access path.

## 4. Entrance hierarchy
The following must read as different functions:
- campus/security arrival;
- VIP entrance;
- employee/visitor pedestrian entrance;
- production/staff access;
- loading/service/maintenance access.

Do not let truck/service openings visually masquerade as pedestrian entrances.

## 5. Final architectural façades
Audit all campus buildings against the intended POVU architectural language. Remove generic unfinished white/grey-box appearance where it is a geometry/design problem.

Use coherent architecture appropriate to each zone:
- front-of-house: refined glazing, graphite/dark frames, controlled champagne/bronze accents, warm human-scale entrances, POVU identity;
- production/warehouse: disciplined industrial cladding language, readable bays/doors, controlled glazing, graphite/light-neutral surfaces and restrained POVU accents;
- utilities/service: robust functional architecture, still coherent with the campus.

Do not randomly decorate buildings. Maintain a consistent campus family.

Where only material/color correction is needed, preserve clean semantic material slots so Remotion can do the final material restoration rather than destructively baking everything.

## 6. Glass Deck final structural audit
Ensure the Glass Deck is physically legible as the signature mezzanine/operations layer, not just a glass strip.

Preserve/refine:
- floor-to-ceiling glazing;
- clear visual oversight into production;
- usable deck/circulation geometry;
- East stair access;
- West stair access;
- Central stair + lift access;
- appropriate guard/edge conditions at concept level;
- semantic separation of glazing, frames, floors and major access elements.

Do not destroy existing machinery or production clearances.

## 7. Hands of Growth landmark
Preserve the landmark and improve its semantic organization.

Keep or create distinct semantic objects for:
- hands/palms/fingers/forearms;
- tree trunk;
- tree crown/leaves;
- plinth/base.

Tree trunk must be independently material-addressable as natural brown; crown/leaves independently addressable as natural green in Remotion.

Add a dedicated presentation camera named `PRES_HANDS_OF_GROWTH` (or a clearly equivalent stable name) with a strong hero composition suitable for later Remotion use. Do not rely only on a generic campus camera.

## 8. Landscape semantic cleanup
Ensure trees and key vegetation are separable enough for realistic runtime material restoration:
- trunk vs foliage where practical;
- lawn/grass vs paving;
- Living Wall as its own semantic object/material group;
- major garden/landscape destinations remain identifiable.

Do not replace the campus with dense high-poly vegetation that makes the GLB unusable.

## 9. Solar field semantic cleanup
Solar panels must not be a monolithic white object.

Separate/preserve where practical:
- `SOLAR_PANEL_SURFACE`
- `SOLAR_FRAME`
- support structure
- inverter/electrical objects if already represented.

The panel surface must be independently material-addressable so Remotion can give it realistic dark blue/blue-black photovoltaic glass; frame/support can remain dark/anodized metal.

## 10. Smart Totem redesign and placement — IMPORTANT
There are currently four Smart Totems around the VIP entrance. This is excessive and must be corrected.

### VIP rule
- Remove/reposition the four-totem cluster.
- Keep/create exactly ONE primary Smart Totem on the VIP approach/path.
- This VIP totem is the campus flagship wayfinding/digital-information totem and must be visibly larger than the secondary campus totems.
- Place it where an arriving VIP can naturally see/read it without blocking the entrance doors, Living Wall, Water Wall, Hands of Growth sightline, pedestrian path or accessibility route.
- It should feel intentional and premium, not like advertising clutter.

Suggested semantic name: `SMART_TOTEM_VIP_PRIMARY`.

### Campus secondary totems
Place a restrained number of smaller Smart Totems only at genuinely useful decision/arrival points. Do NOT put one on every corner.

Use the existing campus geometry and circulation to determine exact locations. Candidate functions include:
- principal employee/visitor arrival decision point;
- POVU Plaza / front-of-house orientation point if it does not duplicate the VIP primary;
- Glass Deck / Production visitor transition point;
- employee campus/social-zone decision point;
- one major industrial/logistics orientation point only if it is useful and safe.

Target approximately 4–6 secondary totems campus-wide, but do not force the count. Use fewer if some candidates are redundant. The governing rule is usefulness + visual restraint.

Suggested stable naming:
- `SMART_TOTEM_01_*`
- `SMART_TOTEM_02_*`
- etc.

Keep display/screen surfaces as separate semantic material/object groups so Remotion can animate their screens later.

## 11. Pedestrian spine and arrival legibility
Strengthen the protected pedestrian spine visually where needed using concept-level geometry such as:
- differentiated paving;
- crossings;
- curbs/bollards/guard separation where appropriate;
- clear links between arrival, VIP/front-of-house, employee destinations and occupied buildings.

Do not change the masterplan circulation logic.

## 12. Loading docks and service openings
Audit Raw Material Receiving, Packaging Warehouses, Production/service interfaces, FG Warehouse and Dispatch.

Make loading/service doors and docks legible where appropriate, while keeping pedestrian staff doors separate. Preserve one-way/segregated logistics logic.

## 13. Employee/social destinations
Audit the physical readability of employee garden, garden pods, Organic Canopy, café/restaurant, wellness/daycare/health and related front-of-house/social destinations. They should read as intentional places, not orphan props.

Do not redesign the campus plan unless a clear defect exists.

## 14. Building signage
Where appropriate, provide physical, restrained building/zone signage so the digital twin itself remains understandable without Remotion overlays.

Candidate labels include:
- POVU / VIP Entrance
- R&D + QC
- POVU Academy
- Production
- Raw Materials
- Finished Goods / Dispatch
- Utilities

Use the project’s existing naming where available. Do not fabricate departments not present in the project.

## 15. Roof/wall semantic separation for future Remotion reveal
For major production buildings, ensure roofs and major façade/wall groups are semantically separable from machinery/interiors wherever practical.

Goal: future Remotion scenes can fade/hide selected roof/wall sections to reveal the factory interior without hiding machinery.

Do not merge the entire factory into one semantic-less mesh.

## 16. Fire/life-safety presentation cues
Preserve and improve visibility of already-designed fire/emergency features where they exist, such as emergency exits, hydrant/fire-water features and muster/assembly cues.

Do NOT invent detailed code-compliance geometry or claim permit-level compliance. This is concept visualization.

# MATERIAL/SEMANTIC PREPARATION FOR REMOTION R02
Do not spend the revision turning every runtime material into a baked final render material. The critical requirement is clean object/material separation and stable naming.

Prepare the GLB so R02 can reliably assign:
- foliage = natural green;
- tree trunks = natural brown;
- Living Wall = rich natural green;
- solar panel surfaces = realistic dark blue/blue-black PV glass;
- solar frames = dark/anodized metal;
- architectural glass = transparent physical glass;
- Water Wall water surface = animated water shader target;
- stainless machinery = stainless/metallic;
- graphite façades = graphite/dark neutral;
- bronze/champagne architectural accents = controlled metallic accent;
- paving/roads/epoxy floors = realistic contextual materials.

# CAMERAS / SEMANTIC TARGETS
Do not delete useful existing cameras.

Add stable cameras/targets only where they improve future Remotion authoring, including at minimum:
- `PRES_HANDS_OF_GROWTH`
- a clear VIP entrance hero camera/target
- a Water Wall/VIP entrance camera/target if not already available
- Glass Deck visitor approach/interior target(s) where useful.

Camera creation must not replace semantic scene targeting; object names remain authoritative.

# QUALITY / VALIDATION
Before export, validate:
1. No major entrance is missing or floating.
2. VIP entrance clearly reads as an entrance.
3. Exactly one large primary Smart Totem is on the VIP approach.
4. Secondary Smart Totems are smaller, sparse and only at useful campus decision points.
5. Water Wall components are semantically separable.
6. Hands of Growth tree trunk/crown are independently material-addressable.
7. Solar surface/frame are independently material-addressable.
8. Glass Deck access hierarchy is represented.
9. Building façades form one coherent POVU architectural family.
10. Pedestrian and truck/service access are not visually confused.
11. Production machinery and previous validated interior layout are not damaged.
12. Existing successful POC source/output is untouched.
13. No severe mesh intersections, floating doors, blocked access, broken normals or accidental hidden major objects.
14. Scene remains exportable to GLB and usable in Three.js/Remotion.

Render presentation QA stills from at least:
- campus aerial;
- VIP approach showing the single primary Smart Totem;
- VIP entrance straight/three-quarter view;
- Water Wall + Living Wall + doors;
- Hands of Growth hero;
- representative front-of-house façade;
- representative production façade/loading interface;
- Glass Deck exterior/interior access;
- solar field;
- employee/social zone.

Review the pixels, not merely successful render exit codes. Repair visible structural failures before final export.

# OUTPUTS
Create a new final Blender master, preserving the previous revision.

Preferred naming:
- `POVU_REV004_FINAL_ARCHITECTURAL_MASTER.blend`
- `POVU_REV004_FINAL_MASTER.glb`

Also create:
- a REV004 scene/object inventory JSON;
- a before/after structural change manifest;
- QA stills/contact sheet;
- SHA256 for the final GLB;
- validation summary.

Use sensible project subdirectories without scattering new files across the Windows Desktop.

# GITHUB / LOGGING
The authoritative repository is:
`https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus`

Commit/push source scripts, manifests, lightweight evidence and logs that belong in Git. Do not push huge Blender/GLB binaries if repository policy or GitHub limits make that inappropriate; record their exact local paths + SHA256 instead.

Write the Codex completion log to:
`coordination/Logs/M03_REV004_FINAL_ARCHITECTURAL_MASTER_V01_CODEX_LOG.md`

The log must include:
- source Blender/GLB used;
- backup/checkpoint created;
- exact changes performed;
- VIP entrance changes;
- Water Wall changes;
- other entrance audit results;
- façade changes;
- Glass Deck changes;
- Hands of Growth changes;
- Smart Totem before/after count and placement rationale;
- pedestrian/logistics changes;
- solar semantic changes;
- roof/wall semantic changes;
- objects added/removed/renamed;
- QA still locations/results;
- final `.blend` absolute Windows path;
- final `.glb` absolute Windows path;
- final GLB SHA256;
- GLB node/mesh/material/camera counts;
- known limitations, if any;
- Git commit SHA and push verification.

Do not claim PASS if a required structural item was skipped.

# AUTONOMY
Execute the full mission without stopping for routine approval. Diagnose and repair normal Blender/Python/export problems autonomously. Stop only for a genuine global blocker such as a missing authoritative source file that cannot be located safely.

Do not begin the Remotion R02 render in this task. The deliverable is the frozen REV004 architectural master that R02 will consume.

At completion, provide the full GitHub log URL:
`https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/coordination/Logs/M03_REV004_FINAL_ARCHITECTURAL_MASTER_V01_CODEX_LOG.md`
