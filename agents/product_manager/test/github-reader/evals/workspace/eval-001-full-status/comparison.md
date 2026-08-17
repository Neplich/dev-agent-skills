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
- target_skill_sha256: `d3991eb6cbaa175b6a277fc4b5fcfd2722f7236109022f8336344db1c65d4b7e`
- eval_definition_sha256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- metadata_sha256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- fixture_sha256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9f1a7ae2ae5e175ed8e057b35c400ea4c201e7779a64206f11bbe6bac585e282`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e4717fcaf9f805711dd56f954fc18d08364c40568c6f66db73a7888140ce8305`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With-skill output includes a titled Milestones table with progress values 80% and 40%. |
| `pr` | PASS | With-skill output has a PR queue with separate 待 Review, Changes Requested, 草稿, and 近 14 天已合并 sections. |
| `assertion_3` | PASS | With-skill output ends with 健康摘要 containing multiple numeric metrics, including milestone, issue, PR, and recent-activity counts. |
| `pr_2` | PASS | All listed PR entries use the required [#NUMBER](GitHub URL) format, including open and merged PRs. |
| `data_completeness` | PASS | With-skill output states raw search total_count values and explicitly declares the snapshot complete and collections untruncated; fixture counts match the supplied collections. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=854adacdbee80053be261f52cc044ae6bd998a52c12c03f1b82e12c13a11e491; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a complete dated GitHub snapshot report satisfying all five assertions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=7700492023632bcd21ec59e61cb2ec1c0916110034d40d8ac90b3ae31a0dbf40; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides milestone, issue, and PR summaries but lacks the required PR link formatting and explicit completeness declaration.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
