# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-002-phase-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192` from `agents/product_manager/test/roadmap-gen/workspace/eval-2-phase-classification`.
- Fixture SHA-256: `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192`
- Prompt SHA-256: `129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a12253d9a3d1d231837468fc266a18cbef8c731ab282a55d4d464a493ca02f11`
- Skill overlay SHA-256: `c50d53c79d2138148c86c2ddaa4ea3403b46c5d6a9d3d67baf48a5203cd6d0b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9bebcff97f69229af9d2fc6b841c4826a4650eeb5ee2c6254e8400fa19d31afa`
- Metadata SHA-256: `ae0af75c7768cc5a422a172a7778c85838314f028847e67a9b64a099fa24dc99`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | with_skill 输出将 August/September 2026 open milestones 放入当前/近期规划，并将 July 2026 closed milestone 单独放入“已完成”区域，同时标注 open/closed 聚合计数。 |
| `large_backlog` | PASS | with_skill 输出说明 backlog 共 128 条、仅抓取 6 条明细，并明确其余 122 条未列出，以摘要/截断方式保持可读。 |
| `issue_details` | FAIL | with_skill 输出按领域/类型分组了已列出的 milestone issue，并保留 assignee 与链接；但 backlog 表格仅保留标签和链接，没有保留 fixture 中 3301、3302、3303 的 assignee 信息。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=53e03584247f819df7b32a6375baad9b071bf4f809205a196a929c564dc701e3; snapshot_sha256=c7c5653979cb88c96934e64f4917fd7540b6028f77bcc67cd456701a7187bcd2
- Behavior: 生成了带数据时点的路线图，正确区分 milestone 状态并压缩 backlog；但 backlog issue 明细遗漏 assignee。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=d4b62a56c0b1026614e46f8d136bae4d1509912ad255a99b78ea0122cbb8ffdd; snapshot_sha256=c051746d92dd36dc980dd15ab6c4344b392a58469c601e0d11e2c4d40d7bcfd9
- Behavior: 生成了路线图，区分 open/closed milestone，压缩 backlog，并为 6 条 issue 保留分组、assignee 和链接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的 issue_details 断言未满足：backlog issue 明细未保留 assignee。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-002-phase-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192` from `agents/product_manager/test/roadmap-gen/workspace/eval-2-phase-classification`.
- Fixture SHA-256: `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192`
- Prompt SHA-256: `129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2b8eaa887e0089b78c69e8bf72f0824676518d33b5c372709e901a79190cd61b`
- Skill overlay SHA-256: `61c47c3293a0a8c5746d4b748abf3c5e11689bfbf0a0493a9b3beca73cbb7663`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9bebcff97f69229af9d2fc6b841c4826a4650eeb5ee2c6254e8400fa19d31afa`
- Metadata SHA-256: `ae0af75c7768cc5a422a172a7778c85838314f028847e67a9b64a099fa24dc99`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | with_skill 输出将 August/September open milestones 放入当前与近期计划，并将 July closed milestone 放入“已完成”区域。 |
| `large_backlog` | PASS | with_skill 输出明确说明 backlog 总量 128、仅抓取 6 条，并以 3 条明细加“另有 125 条未列出”进行压缩。 |
| `issue_details` | FAIL | with_skill 输出按标签/类型分组并保留链接；但 backlog 表未保留 assignee 字段，导致 3301、3302、3303 的负责人信息缺失。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=b3a6cff73fe5522b1fcc5ed69280fbdb2fbc5c9befb44806d2f6cf666c11bf64; snapshot_sha256=4bab2d527d2ea5dd2718b6f560d871210f5d231a818c0ffb602439a207efe4e8
- Behavior: 清晰区分 open/closed milestone，压缩了大 backlog，并按标签/类型展示 issue；里程碑 issue 有负责人，但 backlog issue 未保留 assignee。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=021cec1909e8c166cd302f0cd9c1cc093feb36cbde14cdf4b0b6730b2dee2b53; snapshot_sha256=63af8b1a8f65e3bfcfa5799ab589e4a8e8823b1e20c0884c32afb94ee82a768d
- Behavior: 区分了开放与已关闭里程碑，压缩并说明了大 backlog，也为列出的 issue 保留了标签、负责人和链接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- issue_details 未完整满足：backlog issue 缺少 assignee 信息。
- Next: 在 backlog 表中增加 assignee 列，并填入 dev-c、未分配、dev-d。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
