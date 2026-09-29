# F01 SOURCE PROVENANCE CORRECTION

## Finding

The first F01 attempt correctly stopped at:

`BLOCKED_F01_SOURCE_MANIFEST_MISMATCH`

The block was caused by an incorrect assumption in the GPT-authored F01 prompt, not by a Codex execution error.

## Root cause

The V05 report/log records the **local post-build** canonical Blend SHA-256 as:

`B4F24C77EDDCCC273B6D283AAE08C49AABE0063241C17039E1C39CF4BA5D89E6`

However, the V05 evidence commit:

`420038365847de763d64c8583a9e31ac5a6bd677`

did not commit that post-build Blend binary. Git history for the canonical REV005 Blend skips the V05 evidence commit.

The Blend materialized from the mandated V05 evidence commit has SHA-256:

`1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`

This does **not** invalidate Caps & Trigger as a restoration source because V05 explicitly classified Caps & Trigger as `EVIDENCE_ONLY_REMEDIATION`: V05 did not rebuild that facility. It only reframed the existing geometry.

## Correct source-equivalence test

For F01, whole-Blend hash equality to the local V05-final hash is no longer required.

The Git-restorable source from commit 420038... is authoritative only if ALL of the following pass:

1. Git-materialized source Blend SHA-256 is exactly:
   `1CAB3DC959B1FA8ED8729D33AD36C5C8EF6C89E80CEC41F4CCEFEDA58FCF747D`
2. The historical V05 object-selection logic for Caps & Trigger returns exactly **76** visible objects.
3. Re-rendering that source with the exact V05 Workbench settings and historical cameras reproduces the archived V05 evidence byte-for-byte:
   - A_WIDE SHA-256: `0BA58F03F7E4674DB5BE21DEE95D426AAD7693E1AE23AA69EF98B37FB7750363`
   - B_FUNCTIONAL SHA-256: `B963D85D658969501A6220DFB002DB592ECC56917AB96581E9B49F7F52065374`
   - C_PROCESS_OR_DETAIL SHA-256: `229F5EC480314012EAB019739BBDE277E55954C698ADC4EA45C420B00680E27A`

If these three source-equality gates pass, the selected 76-object facility set is proven to be the exact accepted visual source, regardless of the different whole-file Blend hash.

If any gate fails, Codex must stop before mutation.
