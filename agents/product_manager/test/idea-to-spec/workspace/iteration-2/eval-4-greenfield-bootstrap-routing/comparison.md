# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7638558b96730ed626879bcffd4a606d3ed390013a41acf29ade725d210e3f4e`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- Metadata SHA-256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | With_skill 输出未说明工作区为空、技术栈待定或已有文档为空；仅直接进入 MVP 定位选择。 |
| `pm_first_lane` | PASS | 输出先确认 MVP 核心定位并建议收敛为多轮对话加会话管理，语义上体现了新项目的 PM 需求发现路径。 |
| `pm_first` | PASS | 未执行任何脚手架或工程初始化命令，而是先进行产品定位和 MVP 范围收敛。 |
| `assertion_4` | NOT_EXERCISED | 这是交互式流程；候选输出正在等待用户确认 MVP 定位，尚未到达推荐 PRD/DECISIONS 等文档化下一步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fb50c3394f9a772be0ac0086c8fd11e26899de1147b549ac6038602f3dd105f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 先进行 MVP 核心定位澄清，未初始化项目或创建文件，但未说明空工作区检测结果。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c0abf5633ba538c66d18a143fe16c9265579e677c07feb2b429e60e5ca24b5f1; snapshot_sha256=7d7c31b448f78faa33b029c7a7d99571bd5102df79f5f40c552209cda52f8f3f
- Behavior: 直接声称已完成并产出 PRD.md，未先说明空工作区检测结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足先说明空工作区、技术栈待定和已有文档为空的要求。
- Next: 用户确认 MVP 定位后，再生成 PRD 骨架并记录待决策项。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a2e446c3d8d5f02d34cd5e3954e55500a6eaf296bcb868f9d3dbe27d39c64b91`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- Metadata SHA-256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill 输出未先明确说明目录为空、技术栈待定及已有文档为空；这些信息仅出现在后续 DECISIONS.md 原始证据中。 |
| `pm_first_lane` | PASS | 明确表示已进行需求梳理、产出 PRD 骨架且未初始化项目，等价表明处于 PM-first 的新项目需求收敛阶段。 |
| `pm_first` | PASS | 未执行脚手架或工程初始化；交付物是 docs/pm/ai-chat-assistant 下的 PRD.md 与 DECISIONS.md。 |
| `assertion_4` | FAIL | 虽已交付 PRD.md 和 DECISIONS.md，但“下一步”仅建议确认产品决策，未明确推荐 project-init、PRD 骨架、DECISIONS 记录或等价的文档化下一步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bfa3702571b55568a055f454be594df926f68d960399d1d59e04f51c4fe5a250; snapshot_sha256=359998dc026d33ae3a3cc33fa5ceec080133bdb2d4435e08f883e18fa5eb94b3
- Behavior: 交付了结构化 PM 路径下的 PRD.md 与 DECISIONS.md，未初始化项目；但缺少开头的空目录状态说明，且下一步建议未明确指向文档化动作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=97a03db04e49feda962bca95b1b1a7a83d5461b3ddb3dc4fd629cd66eedb152c; snapshot_sha256=441cebc423e865c629e4d03b3c6363a89368136fc7a23250cac9f68b8b2ccd66
- Behavior: 交付了根目录 PRD.md，未初始化项目，但未明确说明空工作区、技术栈待定或 PM-first 路径。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 assertion_1。
- with_skill 未满足 assertion_4。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- Metadata SHA-256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill 输出未先说明目录为空、技术栈待定和已有文档为空；仅说明已完成需求梳理、未初始化项目。 |
| `pm_first_lane` | FAIL | 未明确使用 greenfield-discovery、greenfield-bootstrap 或等价表达。 |
| `pm_first` | PASS | 未执行脚手架初始化；已产出 docs/pm/ai-chat-assistant/PRD.md 和 DECISIONS.md。 |
| `assertion_4` | FAIL | 下一步建议是确认首要用户，而非明确推荐 PRD 骨架、DECISIONS 记录或其他文档化下一步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6980692ec140d2f7f38189182bc420e8f22e67c6c82c06bbae3835bf45087acd; snapshot_sha256=09f4cf0c3136218547fcd3a2f37f6599afe124ad4556da91a687fa50906e41ac
- Behavior: 产出 docs/pm 下的 PRD.md 与 DECISIONS.md，保持需求梳理和文档优先；但未明确说明空目录状态、greenfield 路径或文档化下一步建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c60b04723a8769d551ac0cf5248ce0358cdf2469cfda623d704de8d0dda36ca3; snapshot_sha256=37ae5bf0677942679ce43f564ee169389a0187d287a47b10318818570f749a7c
- Behavior: 直接交付根目录 PRD.md，未初始化项目；未体现空工作区检测或 PM-first 路径标识。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 assertion_1、pm_first_lane 和 assertion_4。
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

# Eval Result: eval-004-greenfield-bootstrap-routing

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; stale `PRD.md` was removed in both lanes before hashing, and the manifests matched exactly.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `assertion_1`: PASS — started from an empty-workspace context summary.
- `pm_first_lane`: PASS — explicitly selected `greenfield-discovery`.
- `pm_first`: PASS — ran no scaffolding or implementation command.
- `assertion_4`: PASS — advanced PM requirement shaping toward a PRD skeleton and decision record.

### With-Skill / Baseline Comparison

The with-skill response remained PM-first and asked one product-positioning question. The baseline created a `PRD.md` immediately; it did not scaffold code but skipped the explicit lane decision.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-004-greenfield-bootstrap-routing/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`
- Workspace: `workspace/iteration-2/eval-4-greenfield-bootstrap-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; empty-workspace AI assistant request with stale root `PRD.md` excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-004-greenfield-bootstrap-routing/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `assertion_1`: PASS — reports an empty workspace, undetermined stack, and no current docs after cleanup.
- `pm_first_lane`: PASS — selects PM-first `greenfield-bootstrap`.
- `pm_first`: PASS — explicitly avoids engineering scaffold commands.
- `assertion_4`: PASS — routes to `project-init`, PRD skeleton, and DECISIONS after one product decision.

## With-Skill Behavior

The response did not reuse stale root output or start implementation. It kept the feature path provisional, used a single product-positioning decision, and described the durable bootstrap as PRD/DECISIONS only. Removing BRD therefore produces the intended simplified document chain.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It respected the no-code request but drafted a broad PRD skeleton immediately and expanded multiple unresolved topics at once.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected artifact-chain difference, not a regression: bootstrap no longer includes any BRD step.

## Next Steps

- Keep this eval as coverage for empty-workspace PM-first routing and the PRD/DECISIONS bootstrap contract.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-004-greenfield-bootstrap-routing/` and are not committed.
