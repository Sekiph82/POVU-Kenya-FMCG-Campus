# REV005 F06-X03 Dual-View Evidence Closure (M08.40)

## Scope and canonical state

Executed F06-X03 evidence closure only. No F07 work was started. The canonical Blend was not saved or modified; no geometry, visibility, quarantine, neighbor facility, or GLB export was changed.

- Blend SHA-256: `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B` (locked expected: `4C2C7E4439CEE37874042C802FB8439729623982AA6E84ADCBE1E6661173AA5B`)
- GLB SHA-256: `948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133` (locked expected: `948777A20528E4F3FB86D8DA72981049F063E67F36315C6349C6B736E4DAF133`)
- F06 accepted collection: `REV005_FG_F06_MICRO_WEIGH_ACCEPTED_V05_REPLAY`; 43 objects; contribution split BASE 7 / V01 12 / V02 23 / V03 0 / V04 0 / V05 1.
- All seven X01 quarantine objects and saved hidden flags remain intact.

## View D — process / transfer overview

Rendered from the approved X02 Candidate 01 seed: camera `(8,43,6)`, target `(-4,50,2.8)`, 20 mm lens, 36 mm sensor. Visual review confirms the enclosure, four-hopper row, outlets/valves, dosing lines, balance stations/table, transfer tote, and a coherent process path in current facility context.

- Full: `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_CONTEXT.png` (1440x960; SHA-256 `EC36EE45EA35DF6D3EDDA386F2BDBB9CE64691FBD1A05856F52BE0F499A70C99`)
- Preview: `output/rev005-facility-gated/F06_micro_weigh/X03/D_PROCESS_INTEGRATED_CONTEXT_PREVIEW_900x600.png` (900x600; SHA-256 `A7DE7657F6B9C422BCBFF0CAE0FAC59073933EFB15D00F23262D106F25668178`)

## View E — operator / service / access

Rendered 30 focused 900x600 candidates (within the 12–30 limit), across the prescribed service-side camera positions and 20/24/28/32/35/40 mm lenses. Candidate E01 selected: camera `(-14,44,4.5)`, target `(-6,48,2.2)`, 20 mm lens, 36 mm sensor. Candidate camera is outside geometry (nearest surface 0.62 m). Visual review confirms the operator station body and panel, V02 operator table, open access/service floor, visible PPE station and staging, and shared balance/hopper/transfer context. LOS check to the PPE station, staging objects, and transfer tote passes.

- Full: `output/rev005-facility-gated/F06_micro_weigh/X03/E_OPERATOR_ACCESS_CONTEXT.png` (1440x960; SHA-256 `CD630890014D8C3E4D0CC37BC4E12B41AC31D7251A56C2B05AEF649D932F38EC`)
- Preview: `output/rev005-facility-gated/F06_micro_weigh/X03/E_OPERATOR_ACCESS_CONTEXT_PREVIEW_900x600.png` (900x600; SHA-256 `74C037B1603D19DC1B0E1C36ACFF13164E00512E6A6385E6EE5844929F7B6081`)
- Candidate manifest: `output/rev005-facility-gated/F06_micro_weigh/X03/F06_X03_OPERATOR_ACCESS_CANDIDATES.json` (30 candidates; E01 selected).

## Pair coverage and regression

The pair uses one locked canonical Blend and its saved visibility state. D covers process/transfer; E covers operator/service/access. No QA-only hiding, geometry mutation, neighbor mutation, or quarantine expansion was used. The exact seven X01 quarantine objects remain locked. F01–F05 protection is preserved by canonical Blend byte identity. The 43-signature prior regression check remains valid against this byte-identical canonical state.

Evidence: `F06_X03_DUAL_VIEW_VALIDATION.json`, `F06_X03_COMBINED_VISUAL_COVERAGE.json`, `F06_X03_REGRESSION.json`, and `F06_X03_VALIDATION.json`.

## Stop marker

`AWAITING_GPT_FACILITY_AUDIT_F06_X03`
