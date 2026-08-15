# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56` from `agents/product_manager/test/github-reader/evals/workspace/eval-001-full-status`.
- Identity schema: `2`
- target_skill_sha256: `99ea82f9c285d0cd51090c481c0892adf1bdf20367a2866bf82eabffdc17f4c7`
- eval_definition_sha256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- metadata_sha256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- fixture_sha256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9f1a7ae2ae5e175ed8e057b35c400ea4c201e7779a64206f11bbe6bac585e282`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9770b603fd249fd7f80da3e56ab1a6acb6432c1ad6dff3ad5cfc0e089124eab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With_skill output includes a Milestones table with title, progress values 80% and 40%, dates, and status. |
| `pr` | PASS | With_skill output includes a PR 队列 section separating 待 Review and 近 14 天已合并 queues. |
| `assertion_3` | PASS | With_skill output ends with a numeric 健康摘要 covering milestone, overdue, merged PR, and closed issue counts. |
| `pr_2` | PASS | Open and merged PR entries use links in the required [#NUMBER](URL) format. |
| `data_completeness` | PASS | With_skill output states the capture time, cites raw search total_count values for the relevant collections, and reports the snapshot as complete; fixture evidence shows complete, non-truncated collections. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=99a3ecfbf9cc0c1d35f5ab3704eaab0d245cdcba5e98719a918326236f9f63e4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a complete dated GitHub status summary with milestone progress, issue totals, separated PR queues, links, and numeric health summary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=80e9dc80d1ac55764bed9fc5dfba4cf4a063db0e6a3aef3ebecfb268a74bd3bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a generally accurate dated summary but lacked the structured linked PR queue and explicit raw-count completeness framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
