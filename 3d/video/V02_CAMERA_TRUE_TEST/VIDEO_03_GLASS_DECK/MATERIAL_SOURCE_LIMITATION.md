# VIDEO-03 Glass Deck — MATERIAL_SOURCE_LIMITATION

Status: `FAIL` / final MP4 withheld

The corrected REV003 source contains the actual Glass Deck geometry and the camera route enters the deck and finishes toward production. Manual Eevee checkpoint QA fails the readability gate because the source deck materials are not physically transparent in the supplied GLB:

- `GlassDeck_East`, `GlassDeck_West`, `GLASS_DECK_LINK`, and related deck objects reference `Glass`, `REF_Glass`, and `PEO_Glass`.
- The audited Principled materials have `Transmission Weight: 0`, with neutral grey base color and non-transparent surface behavior.
- Checkpoints 3, 4, and 7 are therefore grey/opaque/noise views rather than a readable through-glass production view.

This is reported as `MATERIAL_SOURCE_LIMITATION` per the mission. No materials or geometry were fabricated or silently recolored, and no final MP4 was encoded for Video 3.
