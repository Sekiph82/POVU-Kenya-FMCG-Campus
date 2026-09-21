# M01_VIDEO-001_V01_GPT_PROMPT

## Mission

Build a production-ready, GitHub-coordinated LOCAL Blender rendering pipeline for the POVU Kenya World-Class FMCG Campus and, if the pipeline is technically viable, render the complete 50-video factory-tour library without waiting for routine user approvals.

Repository:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus

All coordination must use this repository as the source of truth.

## Required coordination structure

Use these exact directories and naming conventions:

- `coordination/Prompts/` — GPT task specifications
- `coordination/Logs/` — Codex execution logs
- `coordination/Audits/` — GPT audits

This prompt is:
`coordination/Prompts/M01_VIDEO-001_V01_GPT_PROMPT.md`

Codex MUST create/update:
`coordination/Logs/M01_VIDEO-001_V01_CODEX_LOG.md`

GPT will later audit the completed Codex work in:
`coordination/Audits/M01_VIDEO-001_V01_GPT_AUDIT.md`

Do not create a parallel M33/C001 task system. The M01_VIDEO naming convention above is authoritative.

## Local source files

Use the user's LOCAL Windows files.

Clean POVU GLB source:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d-jutsu-POVU-Kenya-Integrated-Manufacturing-Camp-2026-09-20-22-10-57.glb`

PowerPoint masterplan:
`C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\POVU_Kenya_World_Class_FMCG_Campus_Masterplan_V2_HSE.pptx`

The GLB is the clean architectural source for the rendering pipeline. Before production, verify that the file exists and is a valid GLB. Do not silently substitute another model.

Copy the verified GLB into the repository as:
`3d/revisions/REV003/POVU_REV003_MASTER.glb`

Commit and push it if normal GitHub file-size limits permit.

The PowerPoint is a presentation/reference artifact. Preserve it. It may be inspected for tour structure, naming, HSE context, and later integration, but do not destructively modify it during this render task.

## Local Blender requirement

Rendering MUST use the user's LOCAL Windows Blender, not Higgsfield/cloud Blender and not GitHub Actions.

Inspect local Blender, Blender version, GPU/render capabilities, Blender MCP availability, ffmpeg/ffprobe availability, Git status, disk space, and source-file accessibility before production.

Prefer the configured Blender MCP connection when useful. Expected MCP setup may include:

`codex mcp add blender -- uvx mcp-for-blender`

Blender CLI and Blender Python are also permitted where they make batch production more reliable.

Existing legacy script to inspect:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/blender/render_video01.py

Reuse useful route/setup logic, but refactor it into a maintainable reusable pipeline. Do not blindly preserve obsolete assumptions.

## Master-scene safety

Never destructively overwrite the only architectural master.

Create a local working .blend from the clean GLB and preserve the source GLB unchanged.

Use ONE production video camera at a time. Do not reproduce the earlier 50-camera-in-one-scene design.

After each completed video, clean/reuse the temporary production camera before proceeding.

The pipeline must support restart/resume. A crash at Video 27 must not require re-rendering Videos 01–26.

## Production pipeline

Create a reusable pipeline under:
`3d/video/pipeline/`

It should include, as appropriate:
- Blender Python automation
- route/video manifest
- render configuration
- validation tooling
- resume/state tracking
- README
- output naming conventions
- QA frame/contact-sheet tooling
- ffprobe validation
- SHA-256 generation
- failure/retry handling

Design the pipeline for all 50 videos.

Target baseline per video:
- 16:9
- 30 seconds
- 24 fps
- 720 frames
- 1280x720
- H.264 MP4
- Eevee unless local testing establishes a clearly better reliable option
- smooth cinematic camera motion
- no cloud-worker timeout compromises

Before launching all 50 videos, run Video 01 as the end-to-end pilot.

If Video 01 passes technical AND visual QA, continue automatically through Videos 02–50 without asking for routine approval.

If a recoverable problem occurs, diagnose, fix, retry, log it, and continue.

Stop only for a genuine external blocker that requires user action.

## 50-video production manifest

01 POVU Campus Aerial
02 Main Entrance & POVU Plaza
03 People & Employee Campus
04 Administration & Headquarters
05 R&D + QC Innovation Centre
06 Training & POVU Academy
07 Restaurant + POVU Café
08 Wellness & Recreation
09 Daycare & Family Facilities
10 Occupational Health Centre
11 Production Building Overview
12 POVU Glass Deck
13 MES Production Control Room
14 Raw Material Receiving
15 Raw Material Warehouse
16 Chemical Storage & Unloading
17 Raw Material Supermarket
18 Liquid Ingredient Feeding
19 Liquid Mixing / Wet Processing
20 Hypochlorite Production
21 CIP & Hygiene Systems
22 Bottle Manufacturing
23 Caps & Closures Manufacturing
24 Trigger Spray Manufacturing
25 Liquid Bottle Filling
26 Liquid Sachet Packaging
27 Powder Handling
28 Powder Packaging
29 Toothpaste Manufacturing
30 Toothpaste Packaging
31 Standard Wet Wipes
32 Medical & Baby Wipes
33 Flushable Wipes
34 Packaging Material Warehouse
35 Packaging Material Supermarket
36 End-of-Line Automation
37 Finished Goods Flow
38 Finished Goods Warehouse
39 Dispatch & Truck Loading
40 AMR & Smart Internal Logistics
41 Forklift & Pedestrian Safety
42 Fire & Emergency Systems
43 Utilities Centre
44 ETP / Water Treatment
45 2.5 MW Solar Energy System
46 Heavy Maintenance & Workshop
47 Sustainability & Green Campus
48 Safety & Zero-Harm Campus
49 Employee Experience
50 POVU Smart Factory Grand Tour

## Common cinematic structure

Use this as the default grammar, adapting it to each subject:

- 0–5 s: establish context
- 5–12 s: approach the relevant building/zone
- 12–17 s: enter/reveal the operational area when appropriate
- 17–27 s: explore the core subject
- 27–30 s: hero/detail/transition composition

Do not force interior entry where the model does not contain a credible interior.

Do not invent machinery or architectural content that is absent merely to satisfy a shot list. Log model-content limitations.

## Video 01 pilot

Temporary camera:
`VID_01_POVU_Campus_Aerial`

Video 01 must provide a polished aerial establishing film of the full campus, progressively revealing campus organization, production, HQ and plaza, ending on a strong hero composition.

Existing `blender/render_video01.py` contains an earlier route and may be used as a starting point.

## Validation for EVERY video

A render is not complete merely because Blender exits successfully.

For every MP4 validate:
- file exists and is non-zero
- approximately 30 s
- 1280x720 unless a documented production-level exception is necessary
- expected fps
- H.264/playable/probeable
- no black render
- no catastrophic missing geometry/material state
- no obvious camera clipping
- representative beginning/middle/end frames visually inspected

Use ffprobe/ffmpeg where available.

Generate lightweight QA stills/contact sheets when useful.

Record:
- filename
- local output path
- byte size
- duration
- resolution
- fps
- codec
- SHA-256
- render elapsed time
- QA result
- retry/fix notes

## Output structure

Prefer:
`3d/video/VID_01_POVU_Campus_Aerial/`
through
`3d/video/VID_50_POVU_Smart_Factory_Grand_Tour/`

Each video folder should contain lightweight metadata/QA artifacts suitable for GitHub.

MP4 files may remain local if committing them would be inappropriate because of size. If not committed, log the exact Windows path and SHA-256. Do not introduce Git LFS without a clear need.

## Codex log

Codex MUST create and continuously maintain:

`coordination/Logs/M01_VIDEO-001_V01_CODEX_LOG.md`

The log must be useful for a later GPT audit and include:
- task/prompt identity
- start/end timestamps
- repository commit(s)
- local Blender version
- Blender MCP status
- source GLB verification
- source GLB repository copy status
- PowerPoint path verification
- pipeline files created/changed
- pilot Video 01 result
- per-video status table for 01–50
- render/validation/QA data
- retries and fixes
- blockers
- final completed count
- PASS / PARTIAL / BLOCKED status
- exact next action

Update the log during long production, not only at the end, and push meaningful checkpoints so progress survives interruption.

## Git discipline

Pull before work. Avoid overwriting unrelated user changes.

Commit/push meaningful checkpoints, including:
1. source/pipeline preparation
2. Video 01 pilot PASS
3. periodic production checkpoints
4. final 50-video state

Do not use GitHub Actions for Blender rendering.

## Autonomy

Do not ask the user to approve routine implementation choices, camera tuning, retries, render settings, validation, file organization, commits, or pushes.

After Video 01 passes, continue automatically through all remaining videos if technically feasible.

If a genuine user-only blocker occurs, write it clearly to the Codex log, push the log, and report BLOCKED.

## Completion criteria

Full PASS requires:
- local Blender used
- source master preserved
- verified REV003 GLB copied into repository
- reusable restartable pipeline committed
- Video 01 pilot passed
- Videos 01–50 rendered
- each video technically validated
- representative frames visually QA'd
- logs/metadata pushed
- final Codex log pushed

If only part of the library can be completed, report PARTIAL with exact completed video numbers and reason.

## Final response to the user

When the task stops or completes, keep the response concise.

Report:
- PASS / PARTIAL / BLOCKED
- videos completed, e.g. 50/50
- local output root
- latest relevant commit
- FULL GitHub URL of the Codex log

The required log URL is:

https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/coordination/Logs/M01_VIDEO-001_V01_CODEX_LOG.md

Do not shorten the URL.
