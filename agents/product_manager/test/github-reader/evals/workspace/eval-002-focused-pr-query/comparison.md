# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-002-focused-pr-query`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88` from `agents/product_manager/test/github-reader/evals/workspace/eval-002-focused-pr-query`.
- Fixture SHA-256: `c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88`
- Prompt SHA-256: `468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `68da0ba1f028f581794447a220a41c2a7932596fc89598d52df4a3ae7cae05a7`
- Judge schema SHA-256: `ddb9410329ada83c41bd4e356f1396d4382d0277cddc70506d8c08ee4b2fa89f`
- Eval definition SHA-256: `f5bead0980a8f345220f5b383eac5991e933d1b98e28d8a0a232f76e705ff52b`
- Metadata SHA-256: `c5e584cdac5929bc66cbb7a8b1f6027ddae3cc40fe09b2afaf2c981fd146a7b2`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `pr` | PASS | with_skill 输出仅包含 PR 表格及相关查询说明，没有 issue 列表。 |
| `assertion_2` | PASS | 表格中的每条 PR 都包含作者和明确的等待时间（1201、1202）。 |
| `assertion_3` | PASS | PR 按等待时间从 29 天到 17 天递减排列，且明确说明等待时间计算时点。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=0135054ef9f36c2d2b18b957c998da99e966e4e2143e9ded17636323876ffd76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 聚焦列出 2 个等待 review 的 PR，包含作者、标签、等待时间和数据时点，并按等待时间从长到短排序。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=992a7e88b4ac28e48cbc505df5aea6c3066cf257c2f1e48b0abb19f4707ea4ed; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 列出 2 个 PR，包含等待时间、作者和数据时点；按等待时间排序，但未列出 PR #1202，改列出 PR #1205。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
