# REV005 FACILITY F01 — CAPS & TRIGGER ASSEMBLY — LOCKED GPT AUDIT CRITERIA

**Executor:** Codex  
**Independent auditor:** GPT  
**Source class:** R — exact historical accepted-source restoration

Codex MUST NOT edit this file.

## Gate A — Git source provenance

Materialize without checkout/reset:

Commit:
`420038365847de763d64c8583a9e31ac5a6bd677`

Path:
`3d/revisions/REV005/POVU_KENYA_FMCG_CAMPUS_REV005_INTERIOR_COMPLETION_MASTER.blend`

Expected Git-materialized SHA-256:
`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

The historical local V05-final whole-Blend hash `B4F24C...` is provenance evidence only and is NOT the Git-source equality gate.

## Gate B — exact historical facility selection

Use the exact V05 selection semantics from:
`3d/revisions/REV005/pipeline/render_rev005_interior_remediation_v05.py`

Specifically:
- load the V05 owner-interior inventory referenced by that script;
- use its `objects_for(group, record)` logic;
- group string exactly: `Caps and trigger assembly`;
- exclude label/sign/text/callout/caption objects exactly as the historical renderer did.

Expected selected visible-object count:
**76**

Any other count => STOP before mutation.

## Gate C — byte-identical historical render reproduction

Before mutating the current canonical Blend, render the Git source in a separate Blender process using the exact historical V05 Workbench settings:

- engine: `BLENDER_WORKBENCH`
- resolution: 900×600, 100%
- PNG
- film transparent: false
- display light: STUDIO
- color type: MATERIAL
- shadows: true
- cavity: true
- cavity type: WORLD
- ridge factor: 1.8
- valley factor: 1.2
- background type: VIEWPORT
- background color: (0.08, 0.10, 0.12)
- camera lens: 52 mm
- sensor width: 36 mm

Historical cameras:
- A: location (60,18,13), target (52,31,3)
- B: location (54,24,8), target (52,31,3)
- C: location (46,26,8), target (52,31,3)

Expected PNG SHA-256:
- A: `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
- B: `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
- C: `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

All three must match byte-for-byte before current-model mutation.

## Gate D — exact restoration

After A/B/C source equivalence passes:
- append the exact selected 76-object facility set and required dependencies;
- preserve matrix_world, parents, data, materials, modifiers/constraints;
- remove/disable only the broken current Caps/Trigger representation;
- import no unrelated facility objects;
- do not globally unhide legacy proxies.

Transform tolerances:
- location <= 0.001 m/axis
- rotation <= 0.0001 rad/axis
- scale <= 0.0001/axis
- dimensions <= 0.001 m/axis

## Gate E — accepted visual identity

Restored result must show without labels:
- bowl/feed equipment;
- cap/trigger feed tracks;
- guarded assembly conveyor/cell;
- multiple work positions/fixtures;
- reject station.

## Gate F — V10/F01 review renders

Produce 1440×960 PNGs:

A:
- location (60,18,13)
- target (52,31,3)
- lens 52 mm

B:
- location (54,24,8)
- target (52,31,3)
- lens 52 mm

C:
- location (46,26,8)
- target (52,31,3)
- lens 52 mm

D integrated:
- same A camera with normal current-scene integration.

Any camera adjustment must be numerically logged and remain within prompt limits.

## Gate G — source/workflow protection

REV004 unchanged; no REV006; no second Desktop root; no `.hiveai`; no tour; no edits to TASKS or this criteria file.

## Gate H — stop

Stop at:
`AWAITING_GPT_FACILITY_AUDIT_F01`

Do not begin Facility 02.
