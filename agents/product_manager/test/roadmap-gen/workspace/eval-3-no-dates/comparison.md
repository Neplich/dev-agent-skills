# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f225bc0cb8da89135ab8fda6545fb6caaf81067f282662f8137864aa5ba934b5`
- Skill overlay SHA-256: `6a4646ad3a1fa7bd703a7dd65466915e8af51609ca905370cd74275729cdaa61`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0de988260cc4e373c5efec44f42b82c3d2d89a00786eedc87e778720aef52516`
- Metadata SHA-256: `739c0806056078dd90f0845c2ee57c51119138f3d8eec6b4cae5d7853161a3b4`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | FAIL | with_skill 输出按 Go1.27、Go1.28、Go1.29 和 Backlog 分组，基本体现近期/中期/远期分类，也列出 Backlog 与专项 milestone；但未明确将无法匹配的 milestone 交由用户确认。 |
| `no_fake_dates` | PASS | 明确说明开放 milestone 没有有效截止日期，因此不生成 Mermaid Gantt 图，也未提供虚构的起止日期。 |
| `release_blockers` | FAIL | 虽使用“发布阻塞项 / 高优先级关注”标题突出若干 issue，但没有证据表明这些 issue 是带有 release-blocker 标记的 issue，也未按该标签明确识别。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=351b527e08f894672fc56237d27b6664a2667fc2aa456450a4eafac67bcdc844; snapshot_sha256=ef955286c8de9125bb5699cc98fa037c18ad4720691c38d64948ac7b774b6e58
- Behavior: 生成了基于 GitHub milestone 快照的路线图，区分 Go1.27/1.28/1.29、Backlog 与维护工作，并避免无日期甘特图；但未完整满足用户确认流程和 release-blocker 标识要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=aa35c139439dad72d73be9c0961bdd975989a6ec8c2822540af0ab0303087397; snapshot_sha256=95299750998935184018cb9fb03bb2fdfb0a44cf9304eaa201c1f166c69e8a75
- Behavior: 生成了路线图文件，但内容是泛化的长期规划，未提供基于当前 milestone 的语义分类、日期约束或明确 release-blocker issue。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- semantic_classification 未明确将无法匹配的 milestone 交用户确认。
- release_blockers 未明确识别带 release-blocker 标记的 issue。
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

# Eval Result: roadmap-no-dates

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — the exercised path correctly stopped on unavailable GitHub authentication.
- Coverage result: PARTIAL — 0/3 assertion scenarios could be exercised because no milestone or issue data was available.
Overall result: PASS (partial coverage)

### Assertion Results

- `semantic_classification`: NOT EXERCISED — no undated milestone sample was available.
- `no_fake_dates`: NOT EXERCISED — no live-data roadmap was generated for format review.
- `release_blockers`: NOT EXERCISED — no issue labels were available.

### With-Skill / Baseline Comparison

The with-skill lane checked the existing-roadmap path, then stopped after `gh auth status` and `gh repo view` failed in the isolated HOME. It generated no fake dates or roadmap. The baseline produced a directional roadmap without GitHub milestone data.

### Failures / Next Steps

- Re-run after providing authenticated GitHub data to cover semantic inference and release-blocker behavior.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-no-dates/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-003-no-dates`
- Prompt: 为 `golang/go` 生成项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Historical result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | Patch milestones `Go1.25.13`/`Go1.26.6` 归入近期交付，当前 minor `Go1.27`、下一 minor `Go1.28` 和明显超出当前范围的 `Go1.29` 分层；非 semver milestones 单列交维护者确认。 |
| `no_fake_dates` | PASS | 文档明确不生成日期型 Mermaid Gantt，也没有为无日期版本 milestone 虚构截止日。 |
| `release_blockers` | PASS | Live 命中的 `release-blocker` issues 在对应 milestone 顶部以“🚨 发布阻塞项”突出，并保留 issue 链接。 |

## With Skill

- 用 semver 与当前开放版本关系推断 patch、当前/后续 minor 和远期版本，不依赖被移除的固定 Go 映射表。
- 无法仅靠 semver 匹配的 milestone 进入维护者确认清单；两个 2099 哨兵日期 milestone 也明确标注其非真实发布时间语义。
- 不生成无依据的 Gantt；release blockers、进度、assignee、closed milestones 和 backlog 均保留 live 证据。

## Fresh Without-Skill Baseline

- Baseline 也把维护版 `Go1.25.13`/`Go1.26.6`、当前 `Go1.27`、下一版本 `Go1.28`、远期 `Go1.29` 组织成 P0/P1/P2，并且没有虚构日期。
- 因此在本轮核心“milestone 语义推断”上，baseline 与 with-skill 基本持平，区分度不足；不能把通用模型已经具备的版本规划能力粉饰为 skill 独有收益。
- With-skill 的可见增益主要是更明确的 semver 推断理由、无法匹配项的用户确认边界，以及逐条突出 live `release-blocker`；baseline 对 blockers 多为目标性描述，没有同等完整地列出命中实体。

## Failures

- None.
- 内化度观察：语义推断本身没有形成强区分；本 eval 主要验证契约执行正确性，而不是证明 skill 相对 baseline 的显著优势。

## Next Steps

- 保留此 eval 作为无日期、语义推断和 release-blocker 的回归门禁。
- 后续评审继续关注 baseline 是否持续与 with-skill 持平；若长期无区分，应把它作为 skill 精简或 assertion 重构的决策证据。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
