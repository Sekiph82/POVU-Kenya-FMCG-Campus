# CODEX TASK M33-C001 — Local Blender Video Pipeline + Video 01

## Mission
Build and execute the first production-ready local Blender render workflow for the POVU Kenya FMCG Campus. All coordination, task state, scripts, logs, and result references must live in this GitHub repository:

https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus

Do not wait for user approval between normal technical steps. Diagnose, fix, retry, validate, commit, push, and continue until the acceptance criteria below are met or a genuine external blocker requires user action.

## Source of truth
Repository:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus

Active Higgsfield/3D Jutsu project reference:
https://higgsfield.ai/3d-jutsu/24191841-ac4e-4ec3-85ef-f6695638fff3

Current architectural master milestone:
REV003, landmark package completed.

Existing revision manifest:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/3d/revisions/REV003/REVISION.md

3D QA area:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/tree/main/3d/qa

Video area:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/tree/main/3d/video

## Local execution requirement
Use the user's LOCAL Windows Blender, not a cloud render worker.

First inspect available local tools and MCP configuration. Prefer the configured Blender MCP connection if available. The expected setup may include:

codex mcp add blender -- uvx mcp-for-blender

If Blender MCP is not currently usable, diagnose the local configuration and make safe/reversible fixes where possible. You may use the local terminal, repository scripts, Blender Python, and Blender CLI as appropriate.

Do not silently replace local rendering with Higgsfield/cloud rendering.

## Git workflow
1. Clone/open/pull the repository.
2. Work from current `main` unless repository state clearly requires a dedicated branch.
3. Before modifying anything, inspect README and relevant files under `3d/`.
4. Keep all reusable Blender automation scripts in the repository.
5. Commit meaningful checkpoints.
6. Push all task files/logs/results to GitHub.
7. The final response to the user MUST include the full GitHub URL of the final task log. Do not shorten URLs.

## Safety / master-scene rule
Do not destructively modify the only architectural master.

Use a working copy for rendering.

The workflow must remain recoverable:
- architectural source/master remains intact;
- one video camera is created/used at a time;
- do not create 50 animated cameras in one scene;
- after a video is finished, remove/reuse the temporary video camera before moving to the next video;
- preserve revision/result metadata.

## Task 1 — Locate the clean master
Locate the newest usable local POVU master file.

Preferred order:
1. a REV003 .blend backup if present;
2. a clean .blend corresponding to the imported Rev3 scene;
3. the clean GLB exported from the Rev3 master;
4. if none exists locally, report the exact missing source in the GitHub log instead of inventing a substitute.

Known Rev3 reference metadata:
- project revision: 3
- object count after landmark package: 2027
- GLB reference size: 7,269,192 bytes
- BLEND reference size: 25,835,619 bytes
- QA image reference: POVU_Clean_Master_Landmarks_QA.png, 960x540

The scene should include the completed landmark package:
- Hands of Growth
- approximately 7 m POVU Water Wall
- signature organic canopy refinement
- Smart Totem polish

## Task 2 — Create reusable local render pipeline
Create a reusable pipeline under a sensible path such as:

3d/video/pipeline/

At minimum include:
- Blender Python script(s) for camera creation/animation/render setup;
- configuration or manifest for video routes;
- README with exact local execution procedure;
- render output convention;
- validation/logging.

The pipeline should be designed for all 50 POVU videos later, but execute only Video 01 in this task.

Target production defaults:
- 16:9
- H.264 MP4
- 30 seconds
- 24 fps
- 720 frames
- Eevee unless the local machine proves another choice is clearly preferable
- 1280x720 initial production target
- sensible quality settings that can finish reliably on the local machine

Do not sacrifice the 30-second duration merely to work around the old Higgsfield 300-second limit. Local Blender has no such project requirement.

## Task 3 — Video 01
Produce:

VID_01 — POVU Campus Aerial

Purpose:
A polished establishing aerial of the full POVU Kenya FMCG campus.

Narrative:
- 0–5 s: broad campus aerial establishing shot
- 5–12 s: controlled approach toward the main campus
- 12–20 s: reveal production/HQ/plaza relationship
- 20–27 s: move closer while retaining campus legibility
- 27–30 s: strong hero composition suitable for transition to the next film

Camera behavior:
- smooth, cinematic, no abrupt rotation;
- no clipping through geometry;
- no excessive speed;
- preserve architectural verticals as much as practical;
- campus must remain readable;
- avoid a generic orbit if a more deliberate reveal works better.

Temporary camera naming:
VID_01_POVU_Campus_Aerial

## Task 4 — Render validation
Do not treat “Blender finished” as sufficient validation.

Validate at minimum:
- MP4 exists;
- duration is approximately 30 s;
- 1280x720;
- expected fps;
- file is non-zero and playable/probeable;
- inspect representative frames near beginning, middle, and end;
- no black render;
- no obvious camera clipping;
- no obvious catastrophic missing geometry/material state.

If ffprobe/ffmpeg is available, use it for technical validation.

Generate small QA stills/contact sheet if useful and store them in the repository if file size is reasonable.

## Output convention
Prefer:

3d/video/VID_01_POVU_Campus_Aerial/
    VIDEO_LOG.md
    render metadata / QA files

For the MP4 itself:
- commit it to GitHub only if repository/file-size constraints make that sensible;
- otherwise keep the local rendered MP4 in a clearly documented local output folder and record its exact Windows path, filename, byte size, duration, resolution, fps, SHA-256, and why it was not committed;
- do not use Git LFS unless the repository is already configured for it or there is a clear reason to introduce it.

Expected filename:
POVU_VID_01_Campus_Aerial_30s.mp4

## Required GitHub log
Create:

3d/video/VID_01_POVU_Campus_Aerial/VIDEO_LOG.md

It must contain:
- task ID M33-C001;
- date/time;
- machine/Blender version;
- source master used and source path;
- Git commit/source revision;
- Blender MCP status;
- render engine;
- resolution/fps/frame range/duration;
- camera route summary;
- render start/end/elapsed time;
- output path;
- output file size;
- SHA-256;
- technical validation results;
- visual QA notes for sampled frames;
- warnings/fixes/retries;
- final PASS/FAIL/BLOCKED state;
- exact next action.

## Acceptance criteria
PASS only when:
1. local Blender was used;
2. clean POVU master was used without destructive overwrite;
3. reusable video pipeline exists in GitHub;
4. Video 01 was actually rendered;
5. MP4 technical validation passes;
6. representative frames were visually inspected;
7. VIDEO_LOG.md is committed and pushed;
8. the GitHub log URL is available.

If rendering cannot proceed because the clean master file is absent locally, mark BLOCKED and make the blocker extremely specific. Do not fabricate completion.

## Autonomy
Do not ask the user for approval for routine implementation choices, retries, render settings tuning, folder creation, script fixes, or Git commits.

Only stop for user action if a genuinely external prerequisite is missing, for example:
- Blender itself is not installed;
- Blender MCP requires a manual UI action that cannot be performed;
- no clean master file exists locally and cannot be obtained through available repository/project resources;
- authentication prevents GitHub push.

## Final response to user
Keep it short. State PASS/FAIL/BLOCKED, summarize what was completed, and provide the FULL GitHub URL to:

https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/3d/video/VID_01_POVU_Campus_Aerial/VIDEO_LOG.md

Do not provide a shortened GitHub link.
