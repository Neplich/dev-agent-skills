# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f225bc0cb8da89135ab8fda6545fb6caaf81067f282662f8137864aa5ba934b5`
- Skill overlay SHA-256: `6a4646ad3a1fa7bd703a7dd65466915e8af51609ca905370cd74275729cdaa61`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cbeae06859c5325069790802206e50a82b5b23d446c019f5364c7f597eb8f474`
- Metadata SHA-256: `2881f972587a02ea67b4b7ffba2b31eb69fa71b4cf60d23781d8d9d383996c5a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | 证据显示所有开放 milestone 均无 due_on，未发现有截止日期的 milestone；输出未捏造日期。 |
| `undated_semantic_inference` | FAIL | 输出正确指出无法按 semver 推断阶段并请求维护者确认，但仍将这些 milestone 放入“未排期”区段，违反了不得自动归入未排期的要求。 |
| `roadmap_artifacts` | FAIL | 输出包含进度条、issue 状态和 GitHub 链接，但明确因无截止日期而不生成 Mermaid Gantt，缺少必需工件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e6b544f8737d602714eb2f4ec5429155072f5e0ce8d0584779b0b21381596132; snapshot_sha256=f673eff5f537456013e5fafd947b7fef82b7d917b7e1b6bffa99729ad004a4d8
- Behavior: 基于 milestone、issue 和版本上下文整理了进度条、issue 状态及链接；识别无日期且非 semver 的 milestone 并请求确认，但将其置于未排期区段且省略 Mermaid Gantt。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=38031397ba38c47e007a6c2fe3ce04050d5b819938d3d82ff9576de10d0d651f; snapshot_sha256=3045c5dae12c123c781c79ea48b3d52accb7d146ee8b95db48385d98bdb093dc
- Behavior: 生成了主题化的规划路线图和官方链接，但未展示基于 milestone 的日期/语义分类证据，也未提供要求的结构化进度与 Gantt 工件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足无日期 milestone 不得自动归入未排期的约束。
- with_skill 缺少 Mermaid Gantt。
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

# Eval Result: roadmap-timeline

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — the exercised path correctly stopped on unavailable GitHub authentication.
- Coverage result: PARTIAL — 0/3 assertion scenarios could be exercised because no milestone/issue data was available.
Overall result: PASS (partial coverage)

### Assertion Results

- `phase_classification`: NOT EXERCISED — no milestone data was available.
- `undated_semantic_inference`: NOT EXERCISED — no undated milestones were available.
- `roadmap_artifacts`: NOT EXERCISED — no live-data roadmap could be generated.

### With-Skill / Baseline Comparison

The trace first checked for an existing roadmap, then `gh auth status` and `gh repo view` failed in the intentionally isolated HOME. The with-skill lane surfaced the authentication blocker and wrote no synthetic roadmap. The baseline wrote a roadmap, but it is comparison evidence only.

### Failures / Next Steps

- Re-run with a separately authorized GitHub fixture or authenticated isolated `gh` context; do not reuse historical live data.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-timeline/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-001-timeline`
- Prompt: 为 `flutter/flutter` 生成完整项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-001-timeline/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-001-timeline/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Historical result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

未覆盖场景：

- `phase_classification` 的 90 天以上 open dated milestone 分支未触发；live 数据只有逾期/30 天内与 31–90 天 milestone。
- `undated_semantic_inference` 的“无日期 milestone 可按 semver 匹配”分支未触发；6 个无日期 open milestone 都是非 semver 名称。无法匹配后列出并交用户确认的分支已触发。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | Q2/Q3 cutoff 按逾期或 30 天内归入当前冲刺，Q4 cutoff 按 31–90 天归入近期计划；没有捏造远期 milestone。 |
| `undated_semantic_inference` | PASS | 6 个非 semver、无日期 milestone 单列为“需维护者确认阶段”，没有自动归入“未排期”或虚构日期。 |
| `roadmap_artifacts` | PASS | 输出含 16 字符进度条、dated milestone Mermaid Gantt、issue checkbox 与 GitHub 链接。 |

## With Skill

- 严格用 `due_on` 分类有日期 milestone，并对无日期 milestone 进入语义推断路径。
- 对无法可靠匹配 semver 的 6 个 milestone 保留证据、逐项提出确认问题，没有使用固定“未排期”兜底。
- Backlog 截断为 20 条并保留总数；空 milestone、无 assignee、最近关闭 milestone 和未触发场景均显式说明。

## Fresh Without-Skill Baseline

- 同样正确处理了 dated milestone、进度、issue 链接和 Mermaid Gantt，基础路线图质量与 with-skill 接近。
- 但把 6 个无日期工程 milestone 直接归入“⚪ 未排期工程主题”，没有先按版本语义尝试匹配并把无法匹配项交用户确认，不满足新契约。
- Milestone 语义推断的区分度在本样本上主要来自“未匹配处理”：with-skill 遵守确认边界，baseline 使用了固定未排期兜底。由于 live 数据没有可匹配的无日期 semver milestone，本轮不能证明两者在成功语义匹配分支上的差异。

## Failures

- Behavior failure: none.
- Coverage gap: 90 天以上 dated milestone 与可匹配的无日期 semver milestone 均未出现。

## Next Steps

- 保留此 eval，后续 live 数据出现可匹配的无日期 semver milestone 时再观察成功推断分支。
- 不为补齐 coverage 人工制造 GitHub milestone 或日期。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
