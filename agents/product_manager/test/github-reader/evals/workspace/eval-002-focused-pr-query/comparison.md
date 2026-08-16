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
- target_skill_sha256: `99ea82f9c285d0cd51090c481c0892adf1bdf20367a2866bf82eabffdc17f4c7`
- eval_definition_sha256: `f5bead0980a8f345220f5b383eac5991e933d1b98e28d8a0a232f76e705ff52b`
- metadata_sha256: `c5e584cdac5929bc66cbb7a8b1f6027ddae3cc40fe09b2afaf2c981fd146a7b2`
- fixture_sha256: `c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `ddb9410329ada83c41bd4e356f1396d4382d0277cddc70506d8c08ee4b2fa89f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9770b603fd249fd7f80da3e56ab1a6acb6432c1ad6dff3ad5cfc0e089124eab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `pr` | PASS | 输出仅列出 PR，没有 issue 列表或其他大量无关内容。 |
| `assertion_2` | PASS | 列出的每条 PR 都包含作者和等待天数（29 天、17 天）。 |
| `assertion_3` | PASS | 列表按等待天数从长到短排列：#1201（29 天）在 #1202（17 天）之前。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=57c531f81999f901617849f64f48ad3591a56ed89fd60de094f552564e5c7e8b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 聚焦 PR，标注数据时点、作者和等待天数，并按等待时间降序排列。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=d46c31a358eef4acaa84a187e3b33c577ef25e52c0308503f425b73426a9a4b6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样聚焦 PR 并排序，但列出的是 REVIEW_REQUIRED PR，未纳入 reviewDecision 为 null 的 #1202。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
