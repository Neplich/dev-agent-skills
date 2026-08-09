# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `84f20ca3637061984a451201365104813c56f53ca0b37a9fb14c70d8de0d29b1`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 报告直接记录了失败场景、500 错误、缺失的堆栈/截图/trace、console、network、环境与构建上下文，并列出各项证据状态。 |
| `assertion_2` | PASS | 报告使用了 suspected / needs more evidence，并分别记录 Evidence status 与 Confidence；根据单次失败且缺少服务端证据，分类选择合理。 |
| `assertion_3` | PASS | 报告给出 High severity 及登录主链路阻断的 rationale，并独立给出 Low confidence 及其证据依据。 |
| `assertion_4` | PASS | 报告持久化为本地 Markdown artifact：docs/qa/login-refresh/bug-valid-login-returns-500.md，未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 当前证据仅支持一次失败，报告明确无法声称可重复触发；因此确认的 E2E 回归覆盖条件未被满足。 |
| `assertion_6` | PASS | 报告包含 User / System Impact、Implementation / Release Impact，以及指向日志和构建文件的 Evidence References。 |
| `non_e2e_report_path` | PASS | 报告路径为 docs/qa/login-refresh/bug-valid-login-returns-500.md，位于 docs/qa/{feature_path}/ 下、文件名不含日期，且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=e6f29d61b5cf825a8b543844613bb9019fbf8ba5ea2420b22b6ff5b7f1ec5017; snapshot_sha256=5638f1df22bf505abae3369d8428fe4fd9df535f7fe1634d83b9b378157dfebe
- Behavior: 创建了结构完整的本地缺陷报告，谨慎将单次 500 归为 suspected / needs more evidence，并分离证据状态、严重度和置信度。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=88ec1c259f97530bf7f51a95b7c822a6968eb2ed18e1989a83a7b6395a6c46ba; snapshot_sha256=da15e8b12d6fe33e48d12141ad3317e1fa0a8f56cee11fa04d3b959677c65136
- Behavior: 创建了本地缺陷报告并覆盖基础复现和日志内容，但使用了 docs/defect-report-* 路径，未采用要求的分类结构，且未单独盘点完整证据缺口。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充重复复现及服务端堆栈后，再判断是否需要创建 E2E 回归用例与脚本。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
