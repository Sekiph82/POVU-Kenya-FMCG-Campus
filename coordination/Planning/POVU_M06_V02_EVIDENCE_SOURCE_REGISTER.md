# POVU M06 V02 — Evidence Source Register

## Scope

This register corrects the V01 external-document availability record and binds the V02 coverage package to the frozen REV004.1 source. The source GLB was not edited.

- Frozen model: 3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb
- Required SHA-256: BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A
- Verified on 2026-09-24: actual hash equals required hash.
- Search locations: C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\, C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\, and POVU/PRESENTATIONS directories directly under C:\Users\sekip\Desktop\.
- Current output copies were used. Backup copies were found but were not used as V02 authority.

## Authoritative local sources

| Source | Local path | SHA-256 | Relevant sections | V02 use |
|---|---|---|---|---|
| HSE masterplan V2 | C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\POVU_Kenya_World_Class_FMCG_Campus_Masterplan_V2_HSE.pptx | 069699FBDBC8C1401C38872F0C45729D04D1E9640F809061DE685A1FCC9A38AF | Slides 2, 4–6, 9–12, 14–16, 19–24 | Site flows, HSE/life safety, fire/emergency, chemical segregation, heavy-service corridor, solar intent |
| POVU Brand Kenya Strategy | C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\03_POVU_Brand_Kenya_Strategy.pptx | 80AC98BC51DBDD52DF75C1D37EAF9D18DAEFFBF0D2711068C58D1E0F1AB0745C | Slides 1–3, 5–10, 13, 16, 19, 25 | 91-SKU total, six-category portfolio, formats, consumer/channel context |
| KCC Presidential Deck | C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\01_POVU_KCC_Presidential_Deck.pptx | 96D2231A62B093350D7D087BE1ED64969CDF66FB52B94E2466A6D1BB1EACA3C6 | Slides 6, 8–14 | Four portfolio roll-up, 81 equipment line items, process/equipment intent, capacity formats |
| Kenya Market Research | C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\04_Kenya_Market_Research.pptx | E87C1618B91415AC5B936425FE09D9E43429BDF71CD614F5997F20054BCD81B6 | Slides 1–2, 5–13, 16, 18, 20–25 | Market narrative context only; not used to claim modeled geometry |
| Extended-line 91-SKU workbook | C:\Users\sekip\Desktop\PRESENTATIONS\OUTPUTS\BUDGETING PROCESS - KENYA CHEMICAL COMPANY EXTENDED LINE 91 SKU.xlsx | F764E52BCF20D5C4559322E54ECF55A607C3F7BEDD89DA0A2D7E456AE8D0CB71 | Product/cost sheet 14(3.4) serials 1–91; forecast sheets 15(3.4) and 17(2.5); BEP cross-check 6(6.4) | Product-family, format and 91-line closure; not proof that each SKU is separately modeled |

## Model and prior pipeline sources

- 3d/revisions/REV004.1/REV004_1_ARCHITECTURAL_MANIFEST.json
- 3d/revisions/REV004.1/audit/REV004_1_GLTF_RELOAD_INVENTORY.json
- coordination/Planning/POVU_REV004_1_M06_INVENTORY_AUDIT.json
- 3d/video/pipeline/v03_clean_master_manifest.json
- V01 matrix/storyboard and M03–M05 logs under coordination/Planning/ and coordination/Logs/.

These sources establish actual semantic names and bounds. Generic visible massing is not promoted to named equipment.

## Evidence-use decisions

1. HSE documents establish design intent and safety logic; REV004.1 establishes what may be shown. The film must not present concept-level HSE text as certified detailed engineering.
2. The 91-SKU sources close the portfolio narrative at family/format level. They do not convert a modeled proxy into a one-to-one SKU representation.
3. Security/gatehouse, dedicated workshop, dedicated CIP skid and dedicated PP+FRP hypochlorite vessel remain documented-not-modeled or uncertain in the frozen GLB. V02 uses truthful caveat cards.
4. Solar remains three confirmed modeled locations. The SOLAR_POST* support-only cluster is not counted as a fourth installation.

