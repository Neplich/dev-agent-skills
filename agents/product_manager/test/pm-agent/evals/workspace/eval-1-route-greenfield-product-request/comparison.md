# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da17d4a3cc21b7b3406a5e9563eb0de52953132aff13ecd162bc201b422b9c60`
- Skill overlay SHA-256: `e406d715ee602cbed706c0ad23e94d5aceb1a2d88e22b51dc7fec5b6b0ff84ae`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4e776e14ac2c8d3f3aa33718b92238355ee2d15eab3267a50cdada6bb3d4a1de`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | With-skill output identifies the current lane as greenfield discovery and keeps responsibility in product discovery, semantically equivalent to an idea-to-spec route. |
| `pm_first_guardrail` | PASS | It explicitly recognizes an empty workspace, no selected tech stack or existing product documents, and states that product scope should be confirmed before MVP convergence; no code or engineering execution occurs. |
| `context_to_collect` | PASS | It asks the highest-value first discovery question about the primary usage scenario and invites the user to describe the typical user and context. |
| `expected_pm_artifacts` | NOT_EXERCISED | The workflow is still waiting for the user's answer to the first discovery question, so no PM artifact or handoff is yet required. |
| `handoff_boundary` | NOT_EXERCISED | No handoff occurs in the with-skill output; it remains in discovery pending user input. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7b1cfd686f8bb896fb22e665ada9cc95ca26997aa6cb7b42a6ade37c79bf61dc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The output correctly keeps the empty-directory request in a PM-first greenfield discovery lane, asks a focused first product question, and waits for user input.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=62dc71a12bba7c84c65cdb77d916c0097a858106fcabdd90f82ca035370eb8e0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The baseline stays non-mutating but prematurely proposes a broad MVP specification and several product defaults before resolving the primary user and problem.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Continue the discovery interaction after the user answers, then evaluate PM artifacts and handoff boundary.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da17d4a3cc21b7b3406a5e9563eb0de52953132aff13ecd162bc201b422b9c60`
- Skill overlay SHA-256: `e406d715ee602cbed706c0ad23e94d5aceb1a2d88e22b51dc7fec5b6b0ff84ae`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `faee85a9ae3bd921ee8761d30678e08d5487ca74d086f45ad7e7b47811da7807`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | 将请求保持在空目录的 greenfield-discovery PM 路径，未转入工程实现；语义上等价于产品定义 route。 |
| `pm_first_guardrail` | PASS | 明确识别工作区为空、技术栈未定且 PM 文档不存在，并在范围确认前未写代码或启动工程执行。 |
| `context_to_collect` | PASS | 首轮围绕目标用户和核心场景提出了具体选择题，并允许用户补充目标用户与核心场景。 |
| `expected_pm_artifacts` | FAIL | 未说明当前先进行交互式产品发现，也未说明需求稳定后将产出 PRD/决策记录等 PM 文档及由后续工程阶段负责 TRD/实现。 |
| `handoff_boundary` | FAIL | 未说明需求稳定后才 handoff 给 designer-agent 或 engineer-agent。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5835de55bbece98eb216d829e56a05225651aa6b19d855ba11e7a0e54cdc9b0d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持空目录的 PM-first 产品发现路径，识别 greenfield-discovery 状态并提出高信息量的目标用户/场景问题，但遗漏了 PM 产物和后续 handoff 边界说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=05f19bd1f7881080fa595a242ecb930686c9ba0444a26f799046190a225def29; snapshot_sha256=c1bee362a288b881016f7dc9d3c31ee241ecc40a4c915f1aefef4306f866be60
- Behavior: 生成了 PROJECT_BRIEF.md 并给出较完整的产品假设和待确认事项，但未体现明确的 PM route 或交接边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明需求稳定后的 PM 产物与工程阶段边界。
- with_skill 未说明需求稳定后向 designer-agent 或 engineer-agent 交接。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `37388793264fc16c6901433dfb398542e681204e884a09d39569839783d291d8`
- Skill overlay SHA-256: `98289e4d5e90701d1a7cf8c6a3c2845a0e946fc28f557914acb9f7861bf21322`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `28de521676f44fb26d98a8943e30e638b7117fde8c52e2e6bdc9323fd9003961`
- Runtime SHA-256: `e054983e5b847c0b5102be505d299683dafcc043b1cc5f0db5fafb24d083ee5b`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | with_skill selects `greenfield-discovery` and never selects or explains `idea-to-spec`. |
| `pm_first_guardrail` | FAIL | It notes an empty workspace and no code, but does not identify the missing skip-PM override or classify future direct engineering requests as `pm-agent`. |
| `context_to_collect` | FAIL | It asks about target users and problem, but omits core flow, scope boundaries, acceptance criteria, and key unresolved questions. |
| `expected_pm_artifacts` | FAIL | It explicitly says it will not create a PRD yet and does not declare PRD/DECISIONS outputs or the `engineer-agent:trd-gen` TRD boundary. |
| `handoff_boundary` | NOT_EXERCISED | No handoff occurs; the interactive discovery question must be answered before a later handoff step can occur. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=04e85142bd2a5a4682dfca5ff7a276fc1cbcf5e98fc459725230205758e97ade; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly avoids coding and begins interactive discovery, but uses the wrong route and omits required PM guardrails, context, and artifact declarations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f0dc32ff065b2f822e087cf071e5ab1b2fa91de47bcb1494174bbf94bf7b6cee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Proposes an MVP and product directions but does not follow the required PM route or guardrails.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill fails route_to_idea_to_spec, pm_first_guardrail, context_to_collect, and expected_pm_artifacts.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | with_skill 输出未选择或提及 `idea-to-spec`，也未说明其产品发现、范围收敛和 spec 创建职责。 |
| `pm_first_guardrail` | FAIL | with_skill 输出虽识别为空目录并处于 discovery 阶段，但未提及无 skip-PM override，也未将后续工程请求分类为 `pm-agent`。 |
| `context_to_collect` | FAIL | 输出询问首要用户、问题和三类常见问题，但未说明需收集核心流程、范围边界、验收标准及关键未决问题。 |
| `expected_pm_artifacts` | FAIL | 输出未声明 PRD、DECISIONS 等 PM 文档，也未说明 TRD 应由 `engineer-agent:trd-gen` 负责。 |
| `handoff_boundary` | NOT_EXERCISED | 当前输出停留在等待用户确认目标用户和场景的交互步骤；尚未到需求稳定后的 handoff 步骤，无法判定后续交接边界。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2d712d6fd90a28eff6364aff626bc0fe68168f537ef09d13a643e6e0913c2a1c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为空目录并停留在产品发现阶段，通过选项询问用户与核心场景；但未呈现要求的路由、PM guardrail、完整上下文收集项或 PM 产物边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=80734442529e933d376f323a032a240aff21d542b7decbb3dcfb71ad88400a90; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接提出较完整的 MVP、页面结构和产品决策，但未体现指定的 idea-to-spec / PM-first 路由与产物边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 route_to_idea_to_spec、pm_first_guardrail、context_to_collect 和 expected_pm_artifacts。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | With_skill names `pm-agent → idea-to-spec`, but does not explain that this route handles product discovery, scope convergence, and spec creation. |
| `pm_first_guardrail` | FAIL | With_skill identifies an empty directory and uses `pm-agent`, but does not state the absence of a skip-PM override or the required classification for direct engineering requests. |
| `context_to_collect` | FAIL | With_skill asks only about the intended usage scenario; it does not state that goals, core flow, scope boundaries, acceptance criteria, and open questions must be collected. |
| `expected_pm_artifacts` | FAIL | With_skill does not declare PRD/DECISIONS as expected PM artifacts or identify `engineer-agent:trd-gen` as the post-confirmation TRD owner, nor exclude code, tests, and deployment configuration. |
| `handoff_boundary` | FAIL | With_skill does not state that handoff to `designer-agent` or `engineer-agent` occurs only after requirements stabilize. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b2f4c433242474b1807269fd923a0394a569184ddea6220b3623ae37e37fbc46; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selected `pm-agent → idea-to-spec` and paused for a product-scenario decision, but omitted the required PM guardrail, context checklist, artifacts, TRD ownership, and handoff boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=16f0c39b0908deb1a422e8266867748f57d9fd528821190901d2bb4083d4740e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline proposed an MVP, technical stack, implementation sequence, and decisions without selecting or describing the required PM route.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All five with_skill assertions omit required user-visible content, despite the route being named.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `780c8f93b8e6c45b2ccd3c9782ab0565304ee40820ab216a99298b8a0a82b7f1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | with_skill 输出选择了 `greenfield-discovery`，没有选择或说明 `idea-to-spec`。 |
| `pm_first_guardrail` | FAIL | with_skill 输出未识别空目录中的 skip-PM override，也未说明直跳工程执行请求应返回 `pm-agent` 正常分类。 |
| `context_to_collect` | FAIL | with_skill 输出仅询问助手服务对象，未说明需要收集用户目标、核心流程、范围边界、验收标准和关键未决问题。 |
| `expected_pm_artifacts` | FAIL | with_skill 输出未声明 PRD、DECISIONS 等 PM 文档，也未说明由 `engineer-agent:trd-gen` 负责 TRD，且未区分代码、测试或部署配置。 |
| `handoff_boundary` | FAIL | with_skill 输出未说明需求稳定后才 handoff 给 `designer-agent` 或 `engineer-agent`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=0f76e4806d9686fe24006431fac1e3f3db4a033ffd75ff92d5d215b1416f494a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 进入 `greenfield-discovery`，暂不写代码和锁定技术栈，并询问目标用户；未覆盖 judge assertions 要求的 route、PM guardrail、产物和 handoff 约束。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7c2c004cd65728c6d24c9fc76ec339411ddfa177d9e25452455195a956722e91; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出了 MVP 范围、产品结构和待确认问题，明确暂不写代码；未体现指定 PM route 或 agent 边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足任何一项指定 assertion。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | with_skill 输出未选择或提及 `idea-to-spec`，也未说明其产品发现、范围收敛和 spec 创建职责。 |
| `pm_first_guardrail` | FAIL | with_skill 输出未识别无 skip-PM override，也未提及 `pm-agent` 分类或禁止直跳工程执行。 |
| `context_to_collect` | FAIL | with_skill 输出未说明需要收集用户目标、核心流程、范围边界、验收标准和关键未决问题。 |
| `expected_pm_artifacts` | FAIL | with_skill 输出未声明 PRD、DECISIONS 或其他 PM 文档产物，也未说明由 `engineer-agent:trd-gen` 负责 TRD。 |
| `handoff_boundary` | FAIL | with_skill 输出未说明需求稳定后再交接给 `designer-agent` 或 `engineer-agent`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=79b5c20d1670b837f55c74829538a9b598686950658f5a31c15b4ea8de473230; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别空目录并给出三个产品方向，推荐通用 AI 聊天助手；未包含要求的 route、PM guardrail、上下文收集、产物或 handoff 信息。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6eaffe63a493e78443a8d8f3405c938d418dcdd711e419953485e824248842ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接提出 MVP 功能、排除项和技术方向，并询问三个产品问题；未提及任何技能 route 或 PM 交接边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足全部五项断言。
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

# Eval Result: eval-001-route-greenfield-product-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`
- Workspace: `eval-1-route-greenfield-product-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-001-route-greenfield-product-request/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 5/5 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `route_to_idea_to_spec`: with-skill **FAIL**; without-skill **FAIL** — with_skill 最终回复未明确选择 `idea-to-spec` 或说明其职责；without_skill 同样未路由。
- `pm_first_guardrail`: with-skill **FAIL**; without-skill **FAIL** — with_skill 说明停留 PM 发现阶段但未明确无 skip-PM override 或返回 `pm-agent` 分类；without_skill 也未作该分类。
- `context_to_collect`: with-skill **PASS**; without-skill **FAIL** — with_skill 覆盖产品概念/目标、核心流程、MVP 与非目标、验收标准及待确认问题；without_skill 有部分问题清单，但缺少明确验收标准和完整核心流程。
- `expected_pm_artifacts`: with-skill **FAIL**; without-skill **FAIL** — with_skill 提到 PRD，但未声明 DECISIONS，也未说明 TRD 由 `engineer-agent:trd-gen` 负责；without_skill 未声明这些 PM 产物或 TRD 边界。
- `handoff_boundary`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确只有 PRD 稳定后才进入设计或工程阶段，满足稳定需求后的设计/工程交接边界；without_skill 未明确稳定需求后的 agent handoff。

## With-Skill Behavior

最终回复完成了 PM 需求发现、范围收敛、流程、验收和待决策整理，且未写代码；但缺少明确的 `idea-to-spec` 路由、pm-agent guardrail 分类，以及 DECISIONS/TRD 与 `engineer-agent:trd-gen` 的产物边界。status 显示无新增、删除或修改，trace 仅读取 pm-agent skill 和目录，没有外部 mutation。

## Fresh Without-Skill Baseline

回复停留在需求讨论且无文件写入，但未给出要求的 PM 路由、guardrail、PM 产物/TRD 边界，也未完整覆盖下游上下文与正式 handoff。status 显示无文件变化；trace 无工具调用。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未明确选择 `idea-to-spec` 主 route。
- with_skill 未明确说明空目录无 skip-PM override 并返回 `pm-agent` 正常分类。
- with_skill 未声明 DECISIONS 及 `engineer-agent:trd-gen` 负责 TRD。
- without_skill 未满足指定 PM 路由、guardrail、产物边界和完整下游上下文要求。

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
