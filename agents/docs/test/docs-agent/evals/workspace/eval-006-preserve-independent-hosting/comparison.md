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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
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
| `preserves_not_applicable_evidence` | FAIL | FAIL：确认了静态 workflow、应用镜像不承载文档及 public/internal 变体，并提供了两个证据路径；但未明确报告 `not_applicable`，也未报告下一 owner（Web Platform）。 |
| `does_not_open_devops_handoff` | PASS | PASS：确认无需应用部署团队介入，且未生成 repo-wide deployment handoff；当前决策有效，因此失效时重新询问用户的条件未被触发。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=756d89c7323016ee29ab5ee091e6b363ca00eec9cf56de44e956784d00d81de3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对托管决策和静态发布 workflow，未修改配置或打开 DevOps handoff，但遗漏 assertion 要求的 not_applicable 与下一 owner。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=0385b3b05a180267d5d9c6d1017e331f765e8454b91089ca28474063b280ab92; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别静态托管、维护者签署和 Web Platform 责任，未修改配置或打开 DevOps handoff；同样未明确报告 not_applicable 与下一 owner。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整保留 not_applicable 结论及下一 owner。
- Next: 补充明确的 not_applicable 结论、证据路径、public/internal 覆盖变体和 Web Platform 下一 owner。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
