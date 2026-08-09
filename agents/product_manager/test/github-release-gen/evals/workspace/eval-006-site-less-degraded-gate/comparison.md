# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-006-site-less-degraded-gate`.
- Fixture SHA-256: `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20`
- Prompt SHA-256: `3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `b8169d6d4489fefe59aefe4458af6c4e8108513691e18f7c250f5d7f5c9b7ba5`
- Eval definition SHA-256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- Metadata SHA-256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | With_skill confirms no docs/site or site Release Notes capability chain and produces a complete inline GitHub Release preview. |
| `records_downgrade_basis` | PASS | With_skill explicitly records the formal site and both handoff chains as absent/not applicable, and cites the confirmed changelog plus version-bump evidence. |
| `still_requires_maintainer_approval` | PASS | With_skill limits action to preview, reports no GitHub writes, forbids draft creation, and requires explicit current maintainer approval before writes. |
| `blocks_without_confirmed_fact_source` | PASS | With_skill marks the second scenario blocked because the bump is proposed and no maintainer-confirmed fact source exists; it rejects commit subjects and the unconfirmed summary as facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=b9b2d97df1cb4fcd13923455b7c1bcc57db8bec85916df34d347575626460c3b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly handles both site-less scenarios: downgrades the missing handoffs, previews only from confirmed evidence, preserves maintainer approval gates, and blocks the unconfirmed scenario.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=7f60394eac76765a39f9aaf153242e91f81d747f6dce2b964cec08340df3eeae; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also reaches the key outcomes, but gives a less complete preview and does not explicitly document the full site-less downgrade basis or detailed approval-gate state.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
