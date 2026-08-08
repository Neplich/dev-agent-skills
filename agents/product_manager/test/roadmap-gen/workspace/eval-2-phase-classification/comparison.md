# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-002-phase-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/roadmap-gen/workspace/eval-2-phase-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `48debf99d24171b22711e67aef8b03da211bba4f7a7e84e6508da207d1b88bd2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f225bc0cb8da89135ab8fda6545fb6caaf81067f282662f8137864aa5ba934b5`
- Skill overlay SHA-256: `6a4646ad3a1fa7bd703a7dd65466915e8af51609ca905370cd74275729cdaa61`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8b592fbdf152900e0b07011285ddc364c0b4f368d766cac12b9d185cb4699397`
- Metadata SHA-256: `75f949fe92a4ccbdc39fe76ef54be3d44d89ef12368477ca1a620be162db45a3`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | with_skill 将开放 milestones 分入当前冲刺、近期计划、远期规划和未排期，并设置已完成区域说明已关闭 milestones。 |
| `large_backlog` | PASS | with_skill 对大型 backlog 使用数量摘要、代表性条目和截断说明，保持可读性。 |
| `issue_details` | PASS | with_skill 按类型分组 issue，并保留链接；当前冲刺保留 assignee，Backlog 示例保留标签。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=48debf99d24171b22711e67aef8b03da211bba4f7a7e84e6508da207d1b88bd2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ae9beb9597ef8e921829506946adecc5ff315a35d2227557e22c60b67aed644f; snapshot_sha256=5d72d8da6a41d91da7d26051317563e4e9d7a997ddbfa07652d0106277e2a340
- Behavior: 生成基于 VS Code GitHub milestones/issues 的路线图，满足三项断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=48debf99d24171b22711e67aef8b03da211bba4f7a7e84e6508da207d1b88bd2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=39977d071d433f7819fe64a22ca386863225d87cadc7273555d4925eea946e58; snapshot_sha256=d9cf38defc8e88d621c82c84ff85988a1837d102da3ffed0699f8a26fdd75681
- Behavior: 生成泛化的 12 个月规划，未呈现基于 milestone/issue 的目标细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: roadmap-phase-classification

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-002-phase-classification`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — the exercised path correctly stopped on unavailable GitHub authentication.
- Coverage result: PARTIAL — 0/3 assertion scenarios could be exercised because no milestone, backlog, or issue data was available.
Overall result: PASS (partial coverage)

### Assertion Results

- `open_closed`: NOT EXERCISED — no milestone data was available.
- `large_backlog`: NOT EXERCISED — no backlog sample was available.
- `issue_details`: NOT EXERCISED — no issue, label, assignee, or URL data was available.

### With-Skill / Baseline Comparison

The with-skill lane checked the empty workspace, then stopped after `gh repo view` failed in the isolated HOME. It did not invent repository state. The baseline wrote a generic roadmap without actual milestone/issue evidence.

### Failures / Next Steps

- Re-run with an authorized GitHub data source to exercise the three live-data assertions.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-002-phase-classification/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-002-phase-classification`
- Prompt: 为 `microsoft/vscode` 生成项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-002-phase-classification/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-002-phase-classification/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Historical result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | Open milestones 按截止日期进入当前冲刺/近期计划，最近 5 个 closed milestones 进入“已完成”。 |
| `large_backlog` | PASS | Live 查询到 9,986 个未关联 milestone 的 open issue，仅列 20 条并汇总其余 9,966 条。 |
| `issue_details` | PASS | 1.132.0 issue 按 Agent/Chat、修复、API/功能、工程/发布分组，保留 checkbox、assignee 与链接。 |

## With Skill

- 完整区分 open/closed milestone，并在同一文档保留进度、日期阶段和已完成区域。
- 对超大 backlog 执行明确的 20 条截断，保留总数而不展开 9,986 条。
- Issue 分组使用仓库标签与主题语义，保留 assignee 和 GitHub 链接；空 milestone 仍显示并注明无 issue。

## Fresh Without-Skill Baseline

- 生成了简洁的版本阶段路线图，能保留部分 issue 链接、assignee 和主题分组。
- 没有呈现最近 closed milestone 的“已完成”区域，也没有查询并压缩 9,986 条未关联 milestone 的 backlog；因此在 `open_closed` 与 `large_backlog` 上弱于 with-skill。
- Baseline 更接近优先级规划摘要，with-skill 更完整地执行了 eval 的 GitHub 同步契约。

## Failures

- None.
- `release-blocker` 场景未命中，但它不属于本 eval 的 assertions，不影响 Coverage result。

## Next Steps

- 保留此 eval，持续验证 open/closed 分类、超大 backlog 压缩和 issue 细节保留。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
