# REV005 Interior Remediation V07 Report

## Final state

`AWAITING_GPT_REMEDIATION_AUDIT_V07`

This is a Codex implementation handoff. Independent GPT visual acceptance remains pending; no final PASS is claimed.

## Root-cause diagnostic

- Required Phase 1 diagnostic completed for all 20 prior-failing groups before V07 correction.
- V06 detail was present and enabled in the `REV005_INTERIOR_REMEDIATION_V06` collection; no disabled view layer, zero-scale, or missing-facility-metadata failure was found.
- The primary integration cause was legacy V03/V04/V05 machine housings/panels and foreground proxy covers remaining in the QA keep set and occluding V06 functional detail.
- 35 obsolete machine proxies were hidden from the canonical render/export path; 3 architectural/foreground covers remain QA-only exclusions so floor/back enclosure cues are not deleted.
- The GLB probe matched 1910/1950 V06 object names; the 40 unmatched nodes are soffit support pieces, not functional process detail.
- Detailed per-group transforms, collection/view-layer visibility, hide flags, proxy pairs, camera distance, scale, materials and GLB evidence are recorded in `V07_VISIBILITY_INTEGRATION_DIAGNOSTIC.md`.

## QA readiness

- 26/26 groups represented.
- 6 preserved PASS groups re-rendered with 2 views each = 12 renders.
- 20 diagnostic/remediation groups rendered with A_CONTEXT/B_FUNCTIONAL/C_SEQUENCE = 60 renders.
- Total: 72/72 non-empty unlabeled human/process-scale PNG renders.
- Three contact sheets generated.
- Before/after matrix links V06 references to V07 corrected views.

## Provenance

- V07 baseline Blend: `393B2CEE1523D5CEDFB28E53D081C57C78223021355B12EC6617C223CD2B96DD`
- V07 baseline GLB: `8C669893EEF13D0EC01103E5532C361FDEE5FB85AC2D11FE21D8A8F4D2B16089`
- V07 final Blend: `BF61CAFCD0EA20E5FE371D491913A51D866AE058F58242FDC30B94AB454ACBD8`
- V07 final GLB: `105C83237E5903B1957E206A17E278B7B60214BE38E78F65AB65937294338BE7`
- Baseline values were captured and committed before V07 model mutation; they were not overwritten.

## Protection gates

- REV004 unchanged by hash; no `.hiveai`; no REV006; no tour/owner-review video; TASKS.md and locked V07 criteria were not edited by V07 execution.

## Stop gate

`AWAITING_GPT_REMEDIATION_AUDIT_V07`
