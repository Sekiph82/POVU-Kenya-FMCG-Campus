# REV005 FACILITY F01 — CAPS & TRIGGER — INDEPENDENT GPT AUDIT

## Outcome

`REMEDIATION_REQUIRED_D_INTEGRATED_ONLY`

The F01 historical-model restoration itself passes. Only the integrated-context evidence camera fails.

## Evidence audited

Execution commit:
`6384c03c943f06eef43550e4eb57b6ffede0435d`

Owner-uploaded integrated image:
`F01_D_INTEGRATED_CONTEXT.png`
- resolution: 1440×960
- recorded SHA-256: `52F71B8D493E5017E190707522B8645EEE1A71FAA5306F3B3BAF01C433DE092B`

## PASS — historical reconstruction

- initial source hash correct
- composition correct: 7 base + 21 V01 + 47 V02 + 0 V03 + 0 V04 + 1 V05 anchor = 76
- selected/restored object count = 76
- transform/dimension/parent parity exact
- source/destination facility-only A/B/C visual parity matches the accepted V05 facility
- bowl/feed equipment, feed track, assembly fixtures/cell and outfeed/reject relationship are visible in the accepted restored model

## PASS — scope protection

The F01 execution commit changes only:
- canonical REV005 Blend/GLB
- F01-specific evidence/log artifacts

No evidence of unrelated facility modeling mutation, REV004 change, REV006, .hiveai or tour/video work.

## Finding — PNG metadata

Raw PNG container hashes differ from the archived V05 PNGs because of ancillary metadata, while the reported visual/IDAT pixel streams match. This is a metadata-only finding and requires no model remediation.

## FAIL — D_INTEGRATED_CONTEXT

Direct visual inspection of the uploaded 1440×960 D image fails the integrated-context gate.

Observed failure:
- the Caps & Trigger facility is completely absent from view;
- nearly the entire frame is occupied by a large dark architectural/envelope surface;
- diagonal structural/frame elements cross the image;
- there is no usable evidence of F01 in its current campus context;
- the camera is therefore effectively behind/inside/against an occluding building envelope or is aimed through a blocking surface.

This is **not** a facility-model failure.

## Required remediation

Do not change the 76 restored F01 objects.

Do not change their:
- geometry
- world transforms
- dimensions
- materials
- visibility state
- parent relationships

Do not alter any other facility.

Only regenerate D_INTEGRATED_CONTEXT using a validated, unobstructed integrated camera.

Execution prompt:
`coordination/Prompts/REV005_FACILITY_F01_D_INTEGRATED_CONTEXT_REMEDIATION_GPT_PROMPT.md`

## Final unlock rule

F01 receives final PASS only when the corrected integrated-context image:
- clearly shows the restored F01 facility;
- shows enough current surrounding scene/architecture to prove integration;
- has no destructive overlap with unrelated geometry;
- is not blocked by wall/roof/envelope surfaces;
- does not use global legacy-object unhide;
- is independently inspected by GPT.

Current state:
`REMEDIATION_REQUIRED_D_INTEGRATED_ONLY`

Do not begin F02.
