# M01_VIDEO-004_V01_GPT_PROMPT

## Video
004 — Administration & Headquarters

## Parent orchestration
Master prompt:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/coordination/Prompts/M01_VIDEO_MASTER_V01_GPT_PROMPT.md

Read the master prompt first. Its source, local-Blender, safety, pipeline, validation, Git, autonomy, and restart rules apply to this video.

## Required Codex log
Create and maintain exactly:
coordination/Logs/M01_VIDEO-004_V01_CODEX_LOG.md

GitHub URL:
https://github.com/Sekiph82/POVU-Kenya-FMCG-Campus/blob/main/coordination/Logs/M01_VIDEO-004_V01_CODEX_LOG.md

## Required later GPT audit
Codex must NOT author the audit. GPT will later create:
coordination/Audits/M01_VIDEO-004_V01_GPT_AUDIT.md

## Deliverable
Render one production MP4 for **Administration & Headquarters** using the reusable local Blender pipeline.

Filename prefix:
POVU_VID_004_Administration_Headquarters

Temporary production camera:
VID_004_Administration_Headquarters

## Cinematic intent
Create a clear, polished factory-tour film centered specifically on **Administration & Headquarters**.

Default 30-second grammar:
- 0–5 s: establish context
- 5–12 s: approach/reveal the relevant zone
- 12–17 s: enter or transition closer when credible
- 17–27 s: explore the core subject
- 27–30 s: strong hero/detail/transition composition

Adapt the route to actual scene geometry. Do not invent absent architecture or machinery. Avoid clipping, abrupt rotation, excessive speed, unreadable framing, or a generic orbit when a deliberate reveal is possible.

## Acceptance criteria
PASS only if:
- LOCAL Windows Blender rendered the video
- source master was not destructively overwritten
- output is approximately 30 s, 16:9, target 1280x720, 24 fps, H.264 unless a documented production-level exception is necessary
- file is probeable/playable and non-zero
- representative beginning/middle/end frames were visually inspected
- no black/catastrophic render or obvious camera clipping
- filename/path/size/duration/resolution/fps/codec/SHA-256/render time are logged
- retries/fixes are logged
- individual Codex log is committed and pushed

At completion, Codex must continue to the next numbered video automatically when running under the master prompt.
