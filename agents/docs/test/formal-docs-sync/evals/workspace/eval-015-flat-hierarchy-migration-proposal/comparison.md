# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-015-flat-hierarchy-migration-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-015-flat-hierarchy-migration-proposal`.
- Fixture SHA-256: `687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac`
- Prompt SHA-256: `02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `162b3544cbde876f526df1805303ea3ab78e34b2ebde819bbdbfe83bc8251b8c`
- Eval definition SHA-256: `de76a086939d1591df845f72fbdb70d76c350be98629e84e5fc28aead6c5474b`
- Metadata SHA-256: `1745a4b411c4974d9b158bc811fac50658345383bc93cab2e1df286dcb1629d0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_flat_hierarchy_drift` | FAIL | with_skill 仅指出 research-conversations.md 的漂移，未点名 graph-search.md 与其同属缺失的“知识发现与应用”域节点。 |
| `proposes_migration_before_write` | FAIL | with_skill 提供了会话消息目标子树和部分 change-map/导航说明，但未完整给出所有旧路径映射、三项决策选项及明确等待确认的同批迁移提案。 |
| `does_not_deepen_flat_layout` | PASS | git_evidence 显示无变更；候选输出明确写明未修改 site files，且未宣称执行写入后检查。 |
| `reports_out_of_batch_drift_read_only` | FAIL | with_skill 未列出知识建设与维护、平台治理与运行两组批次外 drift 的具体页面清单及建议目标节点，仅笼统排除其他 API。 |
| `loads_only_api_contract` | FAIL | 候选输出未显式列出已加载的 API 类型模块与 host API 模板；虽然给出层级漂移说明并排除其他文档类型，但不足以满足显式加载模块报告。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=462e3cb55aa4551c3ed966e949b49ad3ff131ec31ac481e65e551562d7b2f835; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了部分层级漂移并保持工作区零写入，但迁移提案、批次外 drift 报告和加载模块报告不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=02d5619a5b35a2cb54dbb7f3f19b3f4325fef0a1206d2f3f66f83a6cc1613ad3; fixture_sha256=687c8c162f66866c443380eff16dcacb1132beefea8bacd8446882557f88aaac; output_sha256=d8afa4c355ad38fafb7c51f0469c3dd8d3d1fc7ffba8e7cf0ddba727104b9564; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出扁平路径下新增叶子页和根导航链接，未识别层级漂移，也未提出迁移或批次外只读报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_flat_hierarchy_drift
- proposes_migration_before_write
- reports_out_of_batch_drift_read_only
- loads_only_api_contract
- Next: 补齐 research-conversations.md 与 graph-search.md 到同一缺失域节点的 drift 证据和结论。
- Next: 在写入前提供完整迁移树、旧新路径映射、入链/递归导航与 change-map delta，并给出三项决策选项后等待确认。
- Next: 列出两组批次外 drift 的具体页面、目标节点及明确的范围外声明。
- Next: 显式报告仅加载的 API 类型模块、host API 模板和 Hierarchy drift 结论。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
