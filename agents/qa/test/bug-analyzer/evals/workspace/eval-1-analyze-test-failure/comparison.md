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
- Identity schema: `2`
- target_skill_sha256: `09e738dc9988190b7f79b8aac551bd1674e0642fae4817109cb4551b9f01f0cd`
- eval_definition_sha256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- metadata_sha256: `8e0e42373ca08b53a19ba642babbf44403e38e8a0315e0e26db92df6ea247617`
- fixture_sha256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `84f20ca3637061984a451201365104813c56f53ca0b37a9fb14c70d8de0d29b1`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `147ea0edbf82c8ca9a07d9d6ff0b589da90d3fd96bbb89bae4f44faf26cc1243`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 报告逐项记录了 scenario、错误消息、stack trace、screenshot、trace、console、network 及 environment/build evidence，并标注缺失或部分可用状态。 |
| `assertion_2` | PASS | 报告使用了 `suspected / needs more evidence`，并分别记录 Evidence status 与 Confidence；单次失败不足以使用 confirmed 分类。 |
| `assertion_3` | PASS | 报告给出 High severity 及用户/发布阻断理由，并独立给出 Medium confidence 及证据不足说明。 |
| `assertion_4` | PASS | 已交付本地 Markdown artifact `docs/qa/login-refresh/bug-login-api-500.md`，未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 当前证据仅支持单次观察，未确认可复现的 E2E 场景；仓库也没有 E2E 用例树或版本化执行要求。 |
| `assertion_6` | PASS | 报告包含 Implementation impact、Release impact，并引用 `logs/test-failure.log` 与 `environment/build.md`。 |
| `non_e2e_report_path` | PASS | 报告路径为 `docs/qa/login-refresh/bug-login-api-500.md`，位于 `docs/qa/{feature_path}/` 下，文件名不含日期且未使用 `docs/qa-reports/`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=8a0daca43fcc71e8354d4ca2c290edc6700fc5ff2993123aa4e60f3eeca5c62e; snapshot_sha256=8e041df6a9a9472268e6302fe592e4cb814875e994dd42afd325711b4dd73861
- Behavior: 交付了持久化缺陷报告，完整区分证据状态、严重度、置信度和影响，并保留证据引用；未虚构根因或可复现性。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=027b3e338d538ad322db8bc3342e82a64b9c055b4b4cc539deeab56b4a1dc862; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅在最终消息中提供未持久化的缺陷报告，覆盖基本现象和建议，但未交付本地 Markdown artifact，也未按结构化证据状态/置信度完整整理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充重复执行结果、服务端堆栈、脱敏请求/响应及目标发布环境验证后，再判断是否升级为 confirmed 分类并建立 E2E 回归覆盖。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
