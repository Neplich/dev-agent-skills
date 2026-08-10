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
- Fixture SHA-256: `0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56`
- Prompt SHA-256: `01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `b0004c5792dae6a7d4050cf6839b7073909210717e4fcd3dd4b28188da158276`
- Judge schema SHA-256: `9f1a7ae2ae5e175ed8e057b35c400ea4c201e7779a64206f11bbe6bac585e282`
- Eval definition SHA-256: `a688cc91089931e5821e56e4470a0bc8844e7a9c13d1b4c5bcc8d2e3929da0ce`
- Metadata SHA-256: `94b279ac62424134e6355f46df23e4185fa4034dd04349372cf9178ca3c8c29f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `milestone` | PASS | With-skill output contains a “Milestone 进度” section with a Markdown table and percentages 80% and 40%. |
| `pr` | PASS | With-skill output contains “PR 队列”, separating 待 Review, 需作者跟进/草稿, and 近 14 天已合并. |
| `assertion_3` | PASS | Output ends with a “摘要” section containing numeric health metrics for issues, PRs, milestones, merges, closures, and aged PRs. |
| `pr_2` | PASS | PR entries use links such as [#901](https://github.com/anthropics/anthropic-sdk-python/pull/901). |
| `data_completeness` | PASS | Output states raw search totals, fetched/total counts, snapshot completeness, incomplete_results status, and that collections were not truncated; these match the locked fixture. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=2647bd056ff34f52c2cbfb6aa9636225833c1cd1f4ee1945ab90f92cc5e520ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete, evidence-consistent GitHub status report with all requested sections, PR links, dated snapshot context, and completeness declarations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=01e34273d27e520aa4245ba28190974384941538e5ce7197f3456329c6301565; fixture_sha256=0519c739e4c8d28c0f994ae12773611385afed7d111bc3d263905cd5dd009c56; output_sha256=4abb9cac658fe9751162493d433d0eadde6b05b154e2ab47a843b73b6d32be6c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided milestone and PR information but omitted required GitHub link formatting, numeric health-summary section, and explicit completeness basis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
