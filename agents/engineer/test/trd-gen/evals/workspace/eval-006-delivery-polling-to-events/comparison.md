# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74` from `agents/engineer/test/trd-gen/evals/workspace/eval-006-delivery-polling-to-events`.
- Fixture SHA-256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ec0b30178f28a00245f34e8794f34ea3d889794c5e097f45505840818ce3d657`
- Metadata SHA-256: `c58e464b2f51cbecc05208e0f4320ff2bade980227072a25840336ba048c489e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | PASS | with_skill 的 git diff 与交付快照显示仅更新 docs/engineer/delivery-pipeline/TRD.md，版本由 1.1.0 更新为 2.0.0；未见其他文档或任务路由变更。 |
| `body_consolidation` | PASS | TRD 正文改为直接描述 delivery.created 事件驱动、异步消费者、重试队列和 dead-letter；旧轮询方案未作为已废弃方案保留，仅在非目标中说明不实现轮询扫描器。 |
| `removal_recorded_in_changelog` | PASS | frontmatter 新增 changelog，明确记录将定时轮询替换为事件驱动投递；版本同步更新为 2.0.0。 |
| `no_implementation_plan_or_code` | PASS | git diff、workspace_manifest 与 git_status 均显示只有 TRD.md 被修改；未创建 IMPLEMENTATION_PLAN.md，未修改代码或补测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=462ef9c6f312aabce38d6990bdd801b580726dd0f753d1873a6a61f565e8436f; snapshot_sha256=2b75bc480bc4069bd62712059fb88266ee37200a2e7b5648c96e5efc8969e7fb
- Behavior: 完整更新现有 TRD，加入事件驱动设计、changelog 与版本升级，且未发生实现代码或额外文档变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=bb5c6ca5399e8c030a681850bb00d46f1f54eaa239b4eef74d42e5082d3fa6c3; snapshot_sha256=e7acaeaae473e78768c503120c1e62491ec580b3a286bb81bc52cf4a2a90a7b7
- Behavior: 更新了 TRD 为事件驱动方案并移除旧轮询内容，但未记录 frontmatter changelog。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74` from `agents/engineer/test/trd-gen/evals/workspace/eval-006-delivery-polling-to-events`.
- Fixture SHA-256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a696884cd8ec31e2137cab6da5326eb0f6fb0d49089fe5e32218dce4da5cdfee`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ec0b30178f28a00245f34e8794f34ea3d889794c5e097f45505840818ce3d657`
- Metadata SHA-256: `c58e464b2f51cbecc05208e0f4320ff2bade980227072a25840336ba048c489e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | FAIL | 仅修改了目标 TRD，但正文新增“移交 feature-implementor 编写实现计划”，属于把任务路由给别人。 |
| `body_consolidation` | PASS | 正文以事件驱动方案为主，轮询仅在非目标和变更记录中提及，未保留旧轮询方案作为正文架构。 |
| `removal_recorded_in_changelog` | FAIL | 版本已更新为 1.2.0，但变更记录放在正文的“变更记录”章节，而非 frontmatter changelog；frontmatter 未新增 changelog。 |
| `no_implementation_plan_or_code` | PASS | git evidence 显示仅修改 TRD.md，没有新增 IMPLEMENTATION_PLAN.md、代码文件或测试文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=46e159d9058b1de8376f86c951c433ab46c4e00acf41fca9e9cef9e625f35b71; snapshot_sha256=19eb7691b8c7262018b96533ca75cbdc1ce08eaf4d3a0fc84ed8b905a05c5048
- Behavior: 更新内容更完整并加入正文变更记录，但仍将 changelog 放在正文、未放入 frontmatter，并包含移交给 feature-implementor 的路由内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=893bef299a3a19d50cf0984bb1b1b325cd50707cadf96048291768080339a373; snapshot_sha256=2b69294f10dc8d6c57216466f226031a92bde71f223469559b4fafd977c9fa04
- Behavior: 更新了事件驱动 TRD 并移除了轮询描述，但未记录 changelog。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- updates_existing_trd：正文包含将后续工作移交给 feature-implementor 的内容。
- removal_recorded_in_changelog：删除留痕未写入 frontmatter changelog。
- Next: 移除任务移交/路由内容，并将轮询删除记录加入 frontmatter changelog。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74` from `agents/engineer/test/trd-gen/evals/workspace/eval-006-delivery-polling-to-events`.
- Fixture SHA-256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ec0b30178f28a00245f34e8794f34ea3d889794c5e097f45505840818ce3d657`
- Metadata SHA-256: `c58e464b2f51cbecc05208e0f4320ff2bade980227072a25840336ba048c489e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | FAIL | 仅修改了目标 TRD，但正文第 8 节写明将移交给 feature-implementor 编写实现计划，违反不得把任务路由给别人的要求。 |
| `body_consolidation` | PASS | 正文已改为事件驱动方案，旧轮询描述已从正文移除；旧方案仅在 frontmatter changelog 中留痕。 |
| `removal_recorded_in_changelog` | PASS | frontmatter 新增 changelog，记录轮询方案删除及 1.2.0 版本更新。 |
| `no_implementation_plan_or_code` | PASS | 证据显示仅修改 TRD.md，未创建 IMPLEMENTATION_PLAN.md、修改代码或补测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=d1c810ac9a1fb6b3e3bbad543fcdac39b80b369d0433392ce1fa75599cd40f65; snapshot_sha256=b6a37f324805f128a73bfd997abf1e48f23e6a5df0d607e1c185ef319c757a8b
- Behavior: 更新了 TRD，补充事件驱动设计与 changelog，但正文包含移交给 feature-implementor 编写实现计划的路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=55885933de5348311609eee5afe6b4bcc0203c52f3c6d5af2bf3ad576448b741; snapshot_sha256=0b16383286786094bb5deedfa3fa9c0ba95e0e9ef07f01ac89077cf678e4bc51
- Behavior: 更新了 TRD 为事件驱动方案，但未增加 changelog。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出在 TRD 正文中将后续工作移交给 feature-implementor，违反 updates_existing_trd 的不得路由要求。
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

# Eval Result: eval-006-delivery-polling-to-events

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`
- Test case: delivery-polling-to-events
- Workspace: `workspace/eval-006-delivery-polling-to-events`
- Latest result: PASS - 2026-08-06 final-harness fresh paired validation completed（frontmatter changelog 口径）；with_skill 4/4 assertions passed，without_skill 3/4。
- Behavior result: PASS — with_skill 实际触达路径满足全部 4 条断言（正文、版本与 changelog 事实一致）。
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: delivery-pipeline PRD v1.2.0（事件驱动已确认）与 TRD v1.1.0（定时轮询旧方案：60 秒扫描、`poller.ts` / `batch.ts`）
- Expected output: 更新 docs/engineer/delivery-pipeline/TRD.md：正文直接描述事件驱动方案，轮询旧方案从正文移除并留痕，不进入实现计划或代码。
- Fresh run: `2026-08-06`（issue #233 新增 eval，最终 harness 重跑，codex exec `gpt-5.6-luna` + `model_reasoning_effort=medium`；两 lane 独立 workspace，均含剥离 test 的 agents/ 依赖镜像（可见上下文一致），with lane 额外在 `.agents/skills` 暴露入口 skill；HOME + CODEX_HOME 隔离（auth 从活跃 CODEX_HOME 复制）；README / eval_metadata.json / comparison.md 已物理排除；independent judge 对照 4 条断言判定）
- Runtime directory: `tmp/eval-runs/fix-233/trd-gen-eval-006-delivery-polling-to-events/`（不入 git）

## Assertions

- PASS `updates_existing_trd`: 两条 lane 均更新目标 `docs/engineer/delivery-pipeline/TRD.md`，未新建 feature 文档或转交任务。
- PASS `body_consolidation`: 两份正文均改写为事件驱动方案；60 秒扫描、`poller.ts`、`batch.ts` 旧方案细节已移除，仅保留「不再使用轮询」的当前约束，无「已废弃」等状态标注。
- PASS `removal_recorded_in_changelog`（with）/ FAIL（without）: with_skill 在 frontmatter 新增 `changelog` 结构（version/date/summary）记录删除并同步版本 `1.1.0 -> 1.2.0`（对应 trd-gen SKILL.md「无 changelog 结构则新增到 frontmatter」指令）；without_skill 仅更新版本号，无 changelog 留痕。该断言在 frontmatter 口径下具备判别力。
- PASS `no_implementation_plan_or_code`: 两条 lane 均未生成 `IMPLEMENTATION_PLAN.md`、修改代码或补测试。

## With Skill

第三轮重跑（frontmatter 口径 + SKILL.md「无 changelog 结构则新增到 frontmatter」指令）：更新后的 TRD 与已确认 PRD 对齐，`delivery.created` 事件驱动方案、状态机、重试队列与 dead-letter；正文直接改写；**frontmatter 新增 `changelog` 结构**（version/date/summary）记录删除并同步版本 `1.1.0 -> 1.2.0`；未进入实现。

## Without Skill

同一 prompt 与 fixture 下新建 baseline（codex `gpt-5.6-luna`，workspace 无 skill 文档）。baseline 同样完成事件驱动改写与版本 bump，但**未新增 changelog 留痕**（仅版本号与 last_updated 更新）。baseline 回复提及 `pm-agent` / `trd-gen` 名称——该仓库为公开仓库，模型先验知识中存在 skill 体系名称，非 lane 泄漏。

## Conclusion

**Skill impact:** MEDIUM

frontmatter 口径下 `removal_recorded_in_changelog` 断言具备判别力（with PASS / without FAIL）：skill 加载后按「无 changelog 结构则新增到 frontmatter」指令补留痕，baseline 遗漏。事件驱动改写与正文收束仍属模型基线能力（两条 lane 均满足），但删除留痕纪律是 skill 带来的可观测差异。该 eval 保留为正文收束与删除留痕的回归覆盖。

## Runtime Artifact(s) Policy

- with/without lane 产物、workspace 更新后的 TRD、judge verdict 均在 `tmp/eval-runs/fix-233/` 下，不入 git。
