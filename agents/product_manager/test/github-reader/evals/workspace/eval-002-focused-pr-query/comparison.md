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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `b0004c5792dae6a7d4050cf6839b7073909210717e4fcd3dd4b28188da158276`
- Judge schema SHA-256: `ddb9410329ada83c41bd4e356f1396d4382d0277cddc70506d8c08ee4b2fa89f`
- Eval definition SHA-256: `f5bead0980a8f345220f5b383eac5991e933d1b98e28d8a0a232f76e705ff52b`
- Metadata SHA-256: `c5e584cdac5929bc66cbb7a8b1f6027ddae3cc40fe09b2afaf2c981fd146a7b2`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `pr` | PASS | 输出集中于开放 PR 表格及相关筛选说明，没有大量无关 issue 列表。 |
| `assertion_2` | PASS | 列出的每条 PR 都包含作者和等待天数。 |
| `assertion_3` | PASS | 列表按等待时间 29 天后 17 天递减排序，最旧 PR 在前。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=1bb4da1e3c48b5b4754b7f0c33b8b0751377c0be6846c2fa852e4d40e8c6132f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确读取导出数据，识别人工且非草稿的待 review PR，提供数据时点、作者、等待时间和排序。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468124d8eedb8d3a589e16901dfd4143cfa89af6e4b45d88eb587edfeea38b16; fixture_sha256=c47404a9f5ea07f17a4bfb2e97874d6684926d30ff0b484abac088755424ca88; output_sha256=100544687fb74368d431e6de87a9de7f9720281eec80754a713bc31f2106b9bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样聚焦 PR 并排序，但将机器人 PR 一并列入待 review 列表，未采用技能要求的人工 PR 分类。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
