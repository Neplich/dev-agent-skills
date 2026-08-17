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
- target_skill_sha256: `f7992d17a0646109f134e112dee5a8d92a38fd3d8cf3007564f0979ffbd3929d`
- eval_definition_sha256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- metadata_sha256: `8e0e42373ca08b53a19ba642babbf44403e38e8a0315e0e26db92df6ea247617`
- fixture_sha256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `84f20ca3637061984a451201365104813c56f53ca0b37a9fb14c70d8de0d29b1`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `27a39b82b995acb5c798df074b3eb2e54e5b81ea6292feb84f2c09cf3d65fb1c`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 报告包含 failing scenario、错误消息、stack trace 缺失、screenshot 不可用、trace 不可用、console、network evidence 和 environment/build 上下文的逐项清单。 |
| `assertion_2` | PASS | 报告使用 `suspected / needs more evidence`，并分别记录 evidence status 与 confidence；未将证据强度和分类混为一谈。 |
| `assertion_3` | PASS | 报告给出 High severity 及阻断登录的 rationale，并单独给出 Medium confidence 及其证据边界。 |
| `assertion_4` | PASS | 报告作为本地 Markdown artifact 写入 `docs/qa/login-refresh/bug-valid-login-returns-500.md`，未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 现有证据仅支持一次失败记录，报告明确标记 repeatability 未建立，因此尚未达到确认的 E2E 复现场景条件。 |
| `assertion_6` | PASS | 报告包含 `Implementation and release impact`，并引用 `logs/test-failure.log` 与 `environment/build.md`。 |
| `non_e2e_report_path` | PASS | 无 E2E 用例树或版本化 E2E 执行要求；报告位于 `docs/qa/login-refresh/`，文件名不含日期且未使用 `docs/qa-reports/`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=e6aa407410331d3573dd24aada04d79c7a2b047275c11fbfc06d35c5e84f41d7; snapshot_sha256=a0ea3ebf08239c7e4553335729b35b0231c4613389413037a2f1b1083171d2d4
- Behavior: 产出结构化、持久化的缺陷报告，完整记录证据缺口、分类、严重度、置信度、影响和追踪引用。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=d73c6489c8c821ea14a888bd86ee74cca74d593bc88ecca282ecc94a258fb25f; snapshot_sha256=608ad22818efe842098d5119135651199544470edf462daa9de3c712e6ad6961
- Behavior: 产出工作区根目录下的 defect-report-login-500.md，包含基本复现、影响和调查建议，但未遵循 repo-native docs/qa 路径或结构化证据清单。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如后续获得第二次复现或可确定的 E2E 复现场景，再评估并创建对应的 E2E case 与 script artifacts。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
