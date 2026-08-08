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
