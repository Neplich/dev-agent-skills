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
- Identity schema: `2`
- target_skill_sha256: `d3991eb6cbaa175b6a277fc4b5fcfd2722f7236109022f8336344db1c65d4b7e`
- eval_definition_sha256: `f5bead0980a8f345220f5b383eac5991e933d1b98e28d8a0a232f76e705ff52b`
- metadata_sha256: `c5e584cdac5929bc66cbb7a8b1f6027ddae3cc40fe09b2afaf2c981fd146a7b2`
- fixture_sha256: `c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `ddb9410329ada83c41bd4e356f1396d4382d0277cddc70506d8c08ee4b2fa89f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e4717fcaf9f805711dd56f954fc18d08364c40568c6f66db73a7888140ce8305`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `pr` | PASS | with_skill 输出仅包含 PR 信息，没有 issue 列表或其他大量无关内容。 |
| `assertion_2` | PASS | with_skill 表格中的每条 PR 都包含作者和等待时间：#1201 为 29 天 1 小时 15 分，#1202 为 17 天 1 小时 15 分。 |
| `assertion_3` | PASS | with_skill 明确说明按等待时间从长到短，且 29 天的 #1201 排在 17 天的 #1202 之前。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=1a47aea0487e1c69d49f8acf44eaa2bea0ed4f03894987ac69d0a8819ac9bb9f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 聚焦列出等待 review 的人工 PR，包含数据时点、作者和等待时间，并按等待时长降序排列。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=6a032c7d67ffd9d67f0e36f620e27169dd9a0f80da79a9d5f4da522739132bef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样聚焦 PR、提供作者和等待时间并排序，但额外列出了 bot PR，作为基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
