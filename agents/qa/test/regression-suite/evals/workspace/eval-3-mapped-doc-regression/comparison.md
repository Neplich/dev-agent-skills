# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Identity schema: `2`
- target_skill_sha256: `0d39fb3d56a0db02711ebbb062de0261e33393ff0e6f5f258b11c870a160c7e5`
- eval_definition_sha256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- metadata_sha256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- fixture_sha256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `33d70406ae3e91e1a71751cc4087074b666d7c138769b3f1c7b475a5d350ce65`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | runner_captured_trace 显示先读取 regression-suite/qa-agent 文档并遍历文件，再在同一命令中先读取 change-map.yaml、后读取 search-query.md；不满足 mapped doc 优先顺序。 |
| `verifies_against_code` | PASS | 候选明确核对 query.rules 为 minimum_query_length = 3、正式文档为 2，并记录差异及最短边界、规则消费路径等直接影响范围；同时将 2 字符行为表述为待确认的修复目标，而非已验证结论。 |
| `treats_unverified_as_low_trust` | PASS | 候选明确指出 last_verified_version: unverified，仅将文档作为低信任导航，扩大到代码、引用和测试/QA证据检查，并将当前回归与发布状态标为 blocked/needs more verification。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=c0b90dee1a43b3b4387cfafc7a62900525e166c434a111e947cf2789ea6c5772; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核证代码与文档阈值差异，并将未核证文档降为低信任；但映射文档读取顺序不符合断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=8b1cadb95ec2330e77b587fc9c9a1b578db7b4eb89ab1d46957c602c0c3ab947; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接核证代码为 3、文档为 2 并给出回归范围；作为 fresh baseline 未明确将 unverified 文档降为低信任。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未按要求优先读取映射指向的正式文档；锁定 trace 证明其先读取技能/契约并先读取 change-map，再读取 search-query.md。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
