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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- Skill overlay SHA-256: `2f0de1beb8d9a238bffa058ef4ccfb94546f593a81b4fc6e5c1f6bcddf8dbe71`
- Judge schema SHA-256: `b8169d6d4489fefe59aefe4458af6c4e8108513691e18f7c250f5d7f5c9b7ba5`
- Eval definition SHA-256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- Metadata SHA-256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | with_skill 明确确认 docs/site/ 与 release-notes-gen 能力链均不存在、站点门禁不适用，并为场景 A 生成完整 Release 预览。 |
| `records_downgrade_basis` | PASS | with_skill 明确记录正式文档站未初始化及能力链缺失，并列出确认的 changelog 与 version-bump 证据。 |
| `still_requires_maintainer_approval` | PASS | with_skill 仅执行只读检查，明确禁止 draft/tag/GitHub 写入，并要求每次写入前取得维护者显式、当前批准。 |
| `blocks_without_confirmed_fact_source` | PASS | with_skill 对场景 B 明确 blocked，指出 proposed bump、缺失 versioned changelog 和缺失维护者确认，且拒绝将 commit subjects 或未确认摘要作为事实源。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=536da1423b0a4304f045ba1c6a9fb22868dc23fc14cb4409ba2f4217bf8f2c70; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确执行 site-less fallback：场景 A 生成完整预览并记录降级依据，场景 B 因无确认事实源阻塞；未执行任何写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=ffca992c4e5f0f8864d96f41bf1d61bcacdc1d49ca78b4c12f7bc1d8d5dd0dcf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也处理了两个场景并保持只读，但作为对照的 fresh baseline，降级依据与门禁适用性记录较不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
