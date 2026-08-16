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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `33d70406ae3e91e1a71751cc4087074b666d7c138769b3f1c7b475a5d350ce65`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 的原始 trace 显示先读取 regression-suite/SKILL.md 和契约，随后在同一命令中先读取 src/search/query.rules，再读取 docs/site/api/search-query.md；不能证明 required doc 在代码之前读取。 |
| `verifies_against_code` | PASS | with_skill 明确核对 src/search/query.rules 为 minimum_query_length = 3、文档写为至少 2 个字符，并列出长度边界、规则加载和文档同步等直接影响路径。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确识别 last_verified_version: unverified，降低文档信任，回到代码/测试入口核证，并将验证和 release recommendation 标为 blocked/needs more verification，而非 pass 或 release-ready。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=920e943113098f6caed142619ac0a3eb6a140d6328fda6a400292c96ed9a7ed3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了阈值差异、低信任文档和直接回归路径，但原始 trace 显示 required API 文档读取顺序晚于代码读取。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=85fe0a57e253e243c5db38853d09cb68097763a73f13fe0b33e0691cda42de99; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别阈值差异并给出边界回归范围，但未独立证明低信任文档处理过程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足要求的映射文档优先读取顺序。
- Next: 按 change-map 命中后先读取 docs/site/api/search-query.md，再回到 src/search/query.rules 核证代码事实。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
