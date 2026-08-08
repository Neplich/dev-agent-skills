# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0b60a8fdef1023247fb430f4647e03f742c09fbfdb17e32a3a03dc6059ae9e02`
- Skill overlay SHA-256: `7093347dda9d009dc74c5bd9b37b3d0d8b980466e82f7a4efbacd767a0e9fa19`
- Judge schema SHA-256: `41bb096923702317d73162d8e61448819b14570f81b171d0e755ad4b6050a105`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | FAIL | 未说明内部 specialist 被直接调用时仍需执行 PM handoff entry gate。 |
| `requires_handoff_or_docs` | FAIL | 进入 PM 需求发现并要求确认功能方向，但未明确要求 PM handoff packet，也未提供等价的已确认 PRD/TRD 与 implementation scope。 |
| `blocks_implementation` | FAIL | 明确暂不进入设计、工程或 QA、不写代码，但未返回 `pm-agent` 分类，且未明确禁止创建 plan 或测试实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=05b7ba61b713987bb96cec97ba94863b2cb3d3c20560f10396fc06b49982d6bb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 进入 PM 需求发现并等待用户确认功能方向，未实施代码变更；但缺少 specialist gate、handoff packet/等价文档要求及 pm-agent 分类。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=94fe33aa427ca007c88d07861c858c52eda1cda8614fbdc4af4760577b9e01f9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别需求和技术设计缺失并请求补充信息，未实施代码变更；未体现 PM handoff gate 或 pm-agent 分类。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足三个断言要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `41bb096923702317d73162d8e61448819b14570f81b171d0e755ad4b6050a105`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | NOT_EXERCISED | 未发生可由锁定证据证明的 specialist 直接调用场景，无法检验其 PM handoff entry gate 行为。 |
| `requires_handoff_or_docs` | PASS | with_skill 明确将请求路由至 pm-agent:idea-to-spec，并要求产出 PRD、DECISIONS 及工程交接范围；同时标记 entry_basis 为 missing。 |
| `blocks_implementation` | PASS | with_skill 明确声明“暂不进行设计、实现或测试”，且 selected_owner 为 pm-agent。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a76cd3d5a1b056ded77a1079aaa112be3e75194bf993204d5b516afb4d579831; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别需求与文档缺失，路由至 pm-agent，并阻止设计、实现和测试，继续请求澄清用户问题。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a04508bfb98cccee069554a3a00ca36781e07d4580b6cc66f2c13bd97f2447cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅泛化地请求补充功能、平台和技术资料，未进行 pm-agent 分类或明确实现阻断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 确认账号中心功能要解决的最高优先级用户问题，并补充或确认 PM handoff packet、PRD/TRD 与 implementation scope。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `41bb096923702317d73162d8e61448819b14570f81b171d0e755ad4b6050a105`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | NOT_EXERCISED | The with_skill output does not establish that an internal specialist was directly invoked or explain that such invocation still runs the PM handoff entry gate. |
| `requires_handoff_or_docs` | FAIL | It says no PRD, technical design, or handoff evidence exists and pauses implementation, but does not require a PM handoff packet or equivalent confirmed PRD/TRD plus implementation scope. |
| `blocks_implementation` | FAIL | It blocks implementation, but does not explicitly block plan creation and returns `greenfield-discovery` rather than the required `pm-agent` classification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=0aa129cd3217c59a1338adff074a59766ed89bcecacc04d5b6edf99fdab203b6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Pauses implementation and requests feature clarification, but omits required PM handoff documentation and pm-agent classification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e4beaf2767afb3fc8d75687b081176dd7fa52e907ed9c87079274c7db7d8551b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline asks for feature, target, codebase, interfaces, and acceptance criteria without specialist-gate behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required PM handoff/docs requirement.
- The with_skill lane does not return the required `pm-agent` classification or explicitly block plan creation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | FAIL | with_skill 输出未说明内部 specialist 被直接调用时仍需执行 PM handoff entry gate。 |
| `requires_handoff_or_docs` | FAIL | with_skill 输出仅要求先确认核心问题并表示 PRD、DECISIONS 待补；未要求 PM handoff packet，也未提供已确认 PRD/TRD 与 implementation scope。 |
| `blocks_implementation` | FAIL | with_skill 输出阻止了技术设计和实现，但未返回 pm-agent 分类，且未明确阻止创建 plan、代码或测试实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=45e7a41f3db7d06948d99fc69077b8243b19a584ca25513e79b84e50c0733f9d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The lane performs greenfield discovery and pauses for user clarification, but omits the required specialist gate, handoff requirement, and pm-agent classification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4a7fe3993980ee1c5e7899a522d638d9ac552f63d4a36cf864488a3270c15a53; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline requests clarification and offers to prepare a requirements/design plan, without specialist-gate, handoff, or pm-agent behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All three with_skill assertions are contradicted or omitted by the locked output.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da17d4a3cc21b7b3406a5e9563eb0de52953132aff13ecd162bc201b422b9c60`
- Skill overlay SHA-256: `e406d715ee602cbed706c0ad23e94d5aceb1a2d88e22b51dc7fec5b6b0ff84ae`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | FAIL | with_skill 输出仅说明按 pm-agent → idea-to-spec 路由，未说明直接调用 specialist 仍须执行 PM handoff entry gate。 |
| `requires_handoff_or_docs` | FAIL | with_skill 输出要求确认账号中心方向，但未要求 PM handoff packet，或等价的已确认 PRD/TRD 与 implementation scope。 |
| `blocks_implementation` | FAIL | 输出明确暂不写代码，但未明确阻止创建 plan 或测试实现；虽提及 pm-agent 路由，也未完整满足该断言要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6a9f1373e3de69fce6de025a7785633d59c5e1682cc740e5563f213cda2fe025; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 进入 pm-agent → idea-to-spec 的 discovery 路由并暂不写代码，但遗漏 specialist gate、handoff/docs 要求及对 plan/测试实现的完整阻断。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b66ab17a9842a89ad290790ab0182db664788eba8a6ff4e7ab8665b2e4ec37ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别需求和技术设计缺失并请求补充信息；未创建或修改文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明 specialist 直接调用时仍执行 PM handoff entry gate。
- with_skill 未要求 PM handoff packet 或等价已确认 PRD/TRD 与 implementation scope。
- with_skill 未明确阻止创建 plan 和测试实现。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | NOT_EXERCISED | The locked output and raw evidence do not establish whether a directly invoked specialist would execute the PM handoff entry gate; no failure can be inferred from the omitted process narration. |
| `requires_handoff_or_docs` | FAIL | The with_skill output asks the user to choose an account-center scenario and says it will then refine scope, but it does not require a PM handoff packet or equivalent confirmed PRD/TRD plus implementation scope. |
| `blocks_implementation` | FAIL | The output does not perform implementation, planning, code, or test changes, but it does not return the required pm-agent classification; it instead names idea-to-spec and greenfield-discovery. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cec7112d401161be05de28ce39159d94553edbe95831de95f3c55839835dd8bb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: The skill-enabled lane recognizes the workspace lacks code and design artifacts, selects a greenfield discovery route, and asks for one core product direction, but does not visibly require the specified handoff/docs or return pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7d4b99508b0543713702f1ad9a421dcb1cbbc88c73470733a6b879a96ad566f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline asks for requirements, platform, existing interfaces/data/auth/UI design, and MVP scope; it performs no changes and provides no required specialist classification or handoff gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required PM handoff packet or equivalent confirmed PRD/TRD and implementation scope.
- The with_skill output omits the required pm-agent classification.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `780c8f93b8e6c45b2ccd3c9782ab0565304ee40820ab216a99298b8a0a82b7f1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | FAIL | with_skill 输出未说明内部 specialist 被直接调用时仍需执行 PM handoff entry gate。 |
| `requires_handoff_or_docs` | FAIL | 输出提到缺少 PRD/技术设计并要求补充信息，但未要求 PM handoff packet，亦未要求已确认的 PRD/TRD 与当前 implementation scope；没有把 IMPLEMENTATION_PLAN 作为前置条件。 |
| `blocks_implementation` | FAIL | 输出阻止了直接实现，但未明确阻止创建 plan、写代码或测试实现，也未返回 pm-agent 分类。仅标注了 request_type、PM 路径和 greenfield-discovery 泳道。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cddf6e4b7708d8fb1b10f3762c8a426837d4bcb7499373b6aaf81c2592073ac0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocks immediate implementation and requests product/technical clarification, but omits the required specialist gate, handoff-packet requirement, explicit action blocks, and pm-agent classification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c231082589afaa182727b3b1287f5a07d4ea72552b63a2d29c6a73d93b56b92e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline requests feature clarification and offers to produce requirements/design/planning; no implementation changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All three with_skill assertions are unsatisfied.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03b14b760268081b00dd698973c18041df83352f41685ff567d1a9c609892457`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `specialist_gate_runs` | FAIL | with_skill 输出未说明内部 specialist 被直接调用时仍需执行 PM handoff entry gate。 |
| `requires_handoff_or_docs` | FAIL | 输出仅要求补充方向和目标，并未要求 PM handoff packet 或等价的已确认 PRD/TRD 与当前 implementation scope；也未明确说明 IMPLEMENTATION_PLAN 不能作为前置条件。 |
| `blocks_implementation` | FAIL | 输出称暂时无法直接实现，但未明确阻止创建 plan、写代码或测试实现，也未返回 pm-agent 分类。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=89fdc3743d802184de224a4d80cf2098550c5d5a21d3c7ff130803aacddcc2c6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为空的新功能并请求澄清，但未满足三项强制断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=836e91f2358533e846fa633d0fc435d8de44890418321b0df75cdebbef9dc10b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3f9e84e72bde134132c56487d844626576df7e237626387f2408d4768a53c12b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别需求信息不足并请求补充，但未覆盖 specialist gate、PM handoff 或 pm-agent 分类要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未说明 specialist 入口 gate。
- with_skill 未要求 PM handoff packet 或等价确认文档。
- with_skill 未明确阻止所有实现动作且未返回 pm-agent 分类。
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

# Eval Result: eval-008-direct-specialist-bypass-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`
- Workspace: `eval-8-direct-specialist-bypass-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-008-direct-specialist-bypass-gate/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `specialist_gate_runs`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未说明 direct specialist invocation 仍执行 PM handoff entry gate；trace 也无 specialist gate 执行证据。without_skill 同样未提及。
- `requires_handoff_or_docs`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未要求 PM handoff packet，也未明确已确认 PRD/TRD 与 implementation scope 是进入实现的条件。without_skill 也未满足该门槛。
- `blocks_implementation`: with-skill **FAIL**; without-skill **FAIL** — with_skill 只阻止直接写代码，未明确阻止创建 plan 或测试实现，也返回了 idea-to-spec 而非 pm-agent。without_skill 还表示可整理实施计划。

## With-Skill Behavior

虽识别为 new_feature 并阻止立即写代码，但未完整执行 specialist gate 要求。status 显示正常完成且 added/removed/modified 均为空；trace 仅有读取操作。

## Fresh Without-Skill Baseline

仅要求补充需求，未满足断言要求；status 显示正常完成且零文件变化。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill specialist_gate_runs 未通过
- with_skill requires_handoff_or_docs 未通过
- with_skill blocks_implementation 未通过

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
