# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Identity schema: `2`
- target_skill_sha256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- eval_definition_sha256: `8e1f2a2b7cff1dcc676c7dcd6956883a0a24ee6d97754afcf56bc59fdaf06a61`
- metadata_sha256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- fixture_sha256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `609660421781976ec561327c947a31da6f7d421bc63e99d2f3f00692dcdf763a`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | 文件包含 `## [v0.120.2] - 2026-08-05`。 |
| `release_tag` | PASS | 版本 `v0.120.2` 与证据中的实际 release tag `v0.120.2` 匹配。 |
| `pr_conventional_commit` | PASS | PR 标题已去除 conventional commit 前缀；`client` scope 作为上下文保留。 |
| `breaking_change_breaking` | PASS | PR #302 条目带有 `⚠️ **BREAKING**` 前缀。 |
| `section` | PASS | 仅有内容的 `Changed` 和 `Fixed` section 出现在文件中。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=9411b28e307c82f3646b44f07761887623a6c065e74339e777fbfb1bb8b108f0; snapshot_sha256=81b742cd60b43f8962f9f527119057a2cd1cfef937315445d6ae8c68d6f192f2
- Behavior: 正确生成目标版本文件，纳入全部 3 个 PR，并满足版本、清洗、Breaking 和 section 要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=eca7ae9bf6fe74b78aeeb360b84be3d0358017e5e2bc5031414d0a85708101c0; snapshot_sha256=a56b8cf237114065d6f358fd6ef3c945f2a6003817cec99a9dfe9d6eb21b14f7
- Behavior: 生成了文件并纳入全部 PR，但版本标题缺少 v 前缀且 Breaking 标记不符合要求；仅作对比基线。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
