# POVU SOLAR COVERAGE REPORT V02

## Frozen-source verification

- Source: 3d/revisions/REV004.1/POVU_REV004_1_FINAL_MASTER.glb
- SHA-256: BD3DF0AE5FDCE88F112547D8CCE84CA1B36682767510204771977103F3D5AB6A
- Confirmed unchanged on 2026-09-24.

## Confirmed modeled installations

1. **SOL-01 — SOLAR_ARRAY through SOLAR_ARRAY083**: 84 modeled panel surfaces, approximate bounds X 27–110, Y 94.5–121.5, Z 2.2–3.0. Associated SOLAR_INVERTER is near X 40, Y 91. Treat as a ground/field PV proxy.
2. **SOL-02 — SolarPanel through SolarPanel047**: 48 modeled panel surfaces, approximate bounds X 44–122, Y 86.8–109.2, Z 2.05–2.75. Treat as a separate low-mounted field; exact mounting relationship remains unconfirmed.
3. **SOL-03 — SOLAR_CARPORT_PANEL through SOLAR_CARPORT_PANEL010**: 11 modeled panel surfaces and 11 supports, approximate panel bounds X -14.5–94.5, Y -92–-86, Z 5.28–6.32. Show context, camera lowering and under-canopy ground/path relationship. Do not claim seating or charging.

## Support-only cluster investigation

SOLAR_POST through SOLAR_POST013 form 14 supports at X -45–39, Y -56–-50, with support bounds extending approximately Z 1.2–6.2. No matching panel surfaces or named canopy occur in the solar category. The only nearby non-solar semantic item in the same X/Y window is SHADE_TREE_TRUNK003 at approximately X 5, Y -58. No named seating, parking, charging or social-use object was found there. This cluster remains **UNPAIRED SOLAR-RELATED SUPPORT EVIDENCE**, not a fourth PV installation.

## Documentation reconciliation

HSE slide 14 documents a 2.5 MW ground-mounted solar intent and slide 15 allocates a solar field. Those documents support the narrative intent, but neither the 4,200-panel count nor exact capacity-to-mesh relationship is inferred from proxy surfaces. V02 therefore retains three modeled locations and uses 2.5 MW SOLAR PV only as a project-document label with no claim that 4,200 panels are individually modeled.

