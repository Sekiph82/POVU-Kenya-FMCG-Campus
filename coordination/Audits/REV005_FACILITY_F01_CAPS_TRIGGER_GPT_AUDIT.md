# REV005 FACILITY F01 — CAPS & TRIGGER — INDEPENDENT GPT AUDIT

## Current outcome

`BLOCKED_EVIDENCE_ONLY`

This is **not a modeling remediation failure**. The exact historical facility restoration has passed all directly inspectable source/model/parity gates. One integrated-context image remains unavailable to GPT for direct visual inspection because the GitHub Contents connector does not return binary content for the >1 MB PNG.

## Evidence audited

Commit:
`6384c03c943f06eef43550e4eb57b6ffede0435d`

### Historical reconstruction
PASS.
- initial source hash: `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
- composition: 7 base + 21 V01 + 47 V02 + 0 V03 + 0 V04 + 1 V05 anchor = 76
- no unexpected Caps/Trigger objects

### Replay checkpoint hashes
The serialized Blend checkpoint hashes differ from the historical local hashes after V01–V05. This was explicitly a diagnostic-only criterion. The exact facility reconstruction is instead proven by the hard visual/object gates below.

### Source visual equivalence
PASS with a non-model metadata finding.

The archived V05 A/B/C evidence has been independently inspected and the replay facility pixel stream is reported equal. The committed normalized source evidence files have the archived SHA-256 values.

Finding:
- raw replay PNG container hashes differ because of ancillary PNG metadata;
- decoded/IDAT visual pixel parity is reported true;
- this does not indicate a geometry/render-content mismatch, but the original criterion phrase "byte-for-byte" was stricter than the achieved raw PNG-container equality.

No model remediation is requested for this metadata-only finding.

### Destination restoration
PASS.
- selected/restored facility object count: 76
- composition and destination manifest reconcile
- transform/dimension/parent parity reported exact
- source facility geometry is restored in historical world coordinates

### Destination facility-only visual parity
PASS.

The three 900×600 destination parity PNGs were directly opened by GPT and visually inspected. They reproduce the accepted V05 Caps & Trigger evidence:
- bowl/feed equipment visible;
- feed track visible;
- carousel/assembly fixtures visible;
- guarded conveyor/cell elements visible;
- multiple work positions visible;
- reject/outfeed relationship present.

The committed normalized destination parity files also carry the same archived V05 SHA-256 values:
- A: `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
- B: `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
- C: `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

### Scope protection
PASS based on commit diff and validation evidence.

The execution commit changes:
- canonical REV005 Blend;
- canonical REV005 GLB;
- F01-specific evidence/log files.

It does not edit root TASKS, locked criteria, REV004, another facility's source file, or create REV006/.hiveai/tour artifacts.

### Final A/B/C
The 1440×960 files exist but exceed the connector's direct-content threshold. Their camera/source geometry is already proven by the directly inspectable 900×600 exact destination parity views.

### D_INTEGRATED_CONTEXT
**PENDING DIRECT VISUAL INSPECTION.**

Required file:
`output/rev005-facility-gated/F01_caps_trigger/F01_D_INTEGRATED_CONTEXT.png`

Recorded:
- resolution: 1440×960
- SHA-256: `52F71B8D493E5017E190707522B8645EEE1A71FAA5306F3B3BAF01C433DE092B`
- size: 1,324,474 bytes

The connector cannot provide this >1 MB PNG to GPT as viewable image content. It must be uploaded directly to the chat, or an evidence-only <=900×600 preview of this same integrated view must be produced without model mutation.

## Unlock rule

F01 receives final `PASS` and F02 unlocks only after direct inspection confirms that D_INTEGRATED_CONTEXT:
- shows the restored Caps/Trigger facility in its correct current-campus location;
- has no destructive overlap/occlusion from unrelated current geometry;
- does not reveal a global legacy-proxy unhide regression;
- remains visually coherent in the current REV005 scene.

Until then:
`BLOCKED_EVIDENCE_ONLY`

Do not begin F02.
