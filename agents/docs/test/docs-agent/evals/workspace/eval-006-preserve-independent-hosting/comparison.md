# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-006-preserve-independent-hosting`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f` from `agents/docs/test/docs-agent/evals/workspace/eval-006-preserve-independent-hosting`.
- Fixture SHA-256: `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f`
- Prompt SHA-256: `75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `787b3941ec90b819758a9894561fa37e2c0eff7eedddb4c4a4d863809f28587f`
- Eval definition SHA-256: `8a4360282a35d2ba7a52bbb24d703648e9f263e7fbfc9516063ba62f62b92b92`
- Metadata SHA-256: `62050136e2c1de0d65367ed4b1b1b706bb2211c3759fb54a832b8fd66233328b`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_not_applicable_evidence` | FAIL | with_skill 保留了决策记录和 workflow 的证据路径，并列出 public/internal 变体及 Web Platform，但未明确报告 not_applicable 状态，也未清晰给出下一 owner 的结构化结论。 |
| `does_not_open_devops_handoff` | PASS | with_skill 的锁定输出和 trace 均未生成 repo-wide deployment handoff；其 Routing decision 是 formal-docs-sync 文档路由，不是 DevOps 部署交接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=f93c636fdcb3fe38f486ef4d0d61108e83f8a9df04d2600b7a6237fd39bf6ff4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确确认无需应用部署团队介入，保留了主要托管证据并避免 DevOps handoff，但缺少明确的 not_applicable 状态和完整下一 owner 表达。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=0a27ea9a34efda69cf47d2eb6ece34c7551820ee61061722a8ec1bbca2c3b8ec; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样确认无需应用部署团队介入并避免 DevOps handoff，但仅提供普通结论和证据，没有结构化路由结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整保留并报告 not_applicable、证据路径、覆盖变体和下一 owner。
- Next: 明确报告 not_applicable 状态，并结构化列出证据路径、public/internal 覆盖变体和下一 owner。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
