# M01_VIDEO_MASTER_V01_GPT_PROMPT

## Purpose
This is the master orchestration prompt for the complete 50-video POVU Kenya FMCG Campus local-Blender production.

Repository:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus

## Authoritative coordination model
There are exactly:
- 1 master GPT prompt
- 50 individual GPT video prompts
- 50 individual Codex logs
- 50 individual GPT audits

Directories:
- coordination/Prompts/
- coordination/Logs/
- coordination/Audits/

Per-video naming:
- Prompt: M01_VIDEO-NNN_V01_GPT_PROMPT.md
- Log: M01_VIDEO-NNN_V01_CODEX_LOG.md
- Audit: M01_VIDEO-NNN_V01_GPT_AUDIT.md

NNN runs from 001 through 050.

## Local sources
GLB:
C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\3d-jutsu-POVU-Kenya-Integrated-Manufacturing-Camp-2026-09-20-22-10-57.glb

PowerPoint:
C:\Users\sekip\Desktop\POVU-Kenya-FMCG-Campus\POVU_Kenya_World_Class_FMCG_Campus_Masterplan_V2_HSE.pptx

Rendering must use LOCAL Windows Blender. Do not use Higgsfield/cloud Blender or GitHub Actions for production rendering.

## Master execution rule
Read this master prompt, then execute individual video prompts strictly in numerical order from VIDEO-001 through VIDEO-050.

For each video:
1. Read its complete GPT prompt from coordination/Prompts/.
2. Use/reuse the common local Blender pipeline.
3. Render that video.
4. Perform technical validation and representative-frame visual QA.
5. Create/update its exact individual Codex log in coordination/Logs/.
6. Commit and push the pipeline/result metadata/log.
7. Continue automatically to the next video without asking for routine approval.

Do not combine the 50 Codex logs into one log.

Do not create all 50 animated cameras in one Blender scene. Use one production camera at a time and clean/reuse it.

The workflow must be restartable. Before rendering a video, inspect its individual log and existing output. Skip only if the existing result is demonstrably PASS and matches the current source/pipeline.

## Common production baseline
- 16:9
- 30 seconds
- 24 fps
- 720 frames
- 1280x720
- H.264 MP4
- local Eevee by default
- smooth cinematic motion
- source architectural master preserved
- ffprobe/ffmpeg validation when available
- beginning/middle/end frame visual QA
- SHA-256 and render metadata logged

## Source control
Copy the verified local clean GLB into:
3d/revisions/REV003/POVU_REV003_MASTER.glb
if not already present, then commit/push it if normal GitHub limits permit.

Build/reuse the common automation under:
3d/video/pipeline/

Inspect the existing legacy helper:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/blender/render_video01.py

## Autonomy
Do not wait for user approval for normal implementation, camera tuning, render settings, retries, QA, validation, commits, pushes, or moving to the next video.

If one video has a recoverable problem, fix/retry it. If a video cannot be completed because of a video-specific limitation, mark that individual log BLOCKED/PARTIAL with exact evidence and continue to the next video when safe.

Stop the whole master run only for a genuine global blocker such as unavailable Blender, inaccessible source master, unrecoverable repository authentication, insufficient disk space that requires user intervention, or another condition preventing subsequent videos.

## Completion
Full master PASS means all 50 individual videos have PASS logs.

GPT audits are NOT to be authored by Codex. Codex creates the 50 logs. GPT subsequently reviews each log/result and writes the 50 audit files.

At the end, Codex must report:
- overall PASS / PARTIAL / BLOCKED
- completed count out of 50
- failed/blocked video numbers
- latest commit
- full GitHub URLs for all relevant logs, at minimum the last completed log and any blocked logs
- full repository URL

Do not shorten GitHub URLs.
