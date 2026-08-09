# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-001-full-status`.
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `68da0ba1f028f581794447a220a41c2a7932596fc89598d52df4a3ae7cae05a7`
- Judge schema SHA-256: `9f1a7ae2ae5e175ed8e057b35c400ea4c201e7779a64206f11bbe6bac585e282`
- Eval definition SHA-256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- Metadata SHA-256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With_skill 输出包含“Milestone 进度”表格，列出 v0.80/v0.81 及 80%、40% 进度。 |
| `pr` | PASS | With_skill 输出包含“PR 队列”，并分别列出待 Review、Changes Requested、草稿及近 14 天已合并 PR。 |
| `assertion_3` | PASS | With_skill 输出末尾包含“健康摘要”，列出 open issue、open PR、milestone、合并 PR、关闭 issue 等数字。 |
| `pr_2` | PASS | With_skill 的 PR 条目使用了如 [#901](https://github.com/anthropics/anthropic-sdk-python/pull/901) 的格式，其他 PR 条目同样如此。 |
| `data_completeness` | PASS | With_skill 明确声明快照集合完整，并给出 GitHub total_count 与获取数（如 open issues 4/4、open PR 3/3）；原始快照中各查询 incomplete_results=false 且 milestones_complete=true，无需标注截断。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=bd7a4393c0bc109869393870005cf699ceef06e65d76fae29fd4d2c87c21792c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整整理数据时点、Milestone、open issues、PR 队列、已合并 PR 和健康摘要，并声明数据完整性。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=45fd54bbb048b1f492da7b9d333b18bb061f8fea2c5088dfc3660dfc4886b171; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了 Milestone、issue 和 PR 基础统计及数据时点，但未形成明确的已合并分类、末尾健康摘要或完整性声明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
