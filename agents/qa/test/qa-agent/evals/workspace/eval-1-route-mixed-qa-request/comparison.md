# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `afcc089a4522fb7587710a20e21adb99a4567c8fc61ab08b5aa456f6ceac23cb`
- Skill overlay SHA-256: `4456feb4afcd3f05c1b5a634bd2e2f7f6addcac1102c5156f9d5ee00a8bd9c3a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2ad0a90eac7fca1f06d238ff5d3d06535381ddd810d8a9e8e9e423ce29483f2c`
- Metadata SHA-256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `f50f0253e5c8a7fde7a9d9b937a4655cb391c9fb5ee9621834e648c3bae66c36`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确选择 qa-agent:regression-suite，并以已实现变更、现有 QA/E2E 资料及 WebKit 间歇性超时说明其是当前最窄的 QA 回归责任方。 |
| `assertion_2` | PASS | 列出了 PRD/TRD/实现计划、变更说明、QA 测试资料、CI 日志、平台版本、凭据、QA URL、执行入口及 npm test -- login。 |
| `specialist_gate_pointer` | PASS | 声明 regression-suite 是后续验证执行责任方，并保留其检查 E2E memory、平台版本、凭据、执行入口及 PRD/TRD/确认文档等门禁；未自行执行验证。 |
| `assertion_4` | PASS | 定义了逐 TC 结果快照、按平台版本的回归汇总、原始失败复核、修复后行为、相邻路径、发布建议及状态/置信度等结构化产物。 |
| `assertion_5` | PASS | 只选择一个下游 specialist；将间歇性超时保留为回归风险，并要求确认复现后才转交 bug-analyzer，未直接认定为 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=b99701635892fc2f3d961994de577d6ddf9ef8b6b63d593ae5254c557d28d6d9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确路由至 regression-suite，传递所需上下文和门禁，结构化定义证据产物，并将当前状态标为 BLOCKED / needs more verification，等待用户确认继续。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=4d62c62d79532d1e480a2f2d3ef46f35801af385cbfdff81d495554db1e71ef1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出有条件验收建议和较完整的证据清单，但未明确路由至单一 specialist 或保留其权威门禁责任。
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

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b4717f001713de443fcd0ea5eb8f768ca2515b356c3836d41a4b8ecc7815aa8b`
- Skill overlay SHA-256: `7c905dbf8ce881f893226bf166e75e1e4e43ca380c29a9798b5a91b3efcfc299`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2ad0a90eac7fca1f06d238ff5d3d06535381ddd810d8a9e8e9e423ce29483f2c`
- Metadata SHA-256: `718fcc57ee1abd91d0d7551c46ebe8546481fa4f027452b86db232f30d15ab47`
- Executor SHA-256: `28de521676f44fb26d98a8943e30e638b7117fde8c52e2e6bdc9323fd9003961`
- Runtime SHA-256: `e054983e5b847c0b5102be505d299683dafcc043b1cc5f0db5fafb24d083ee5b`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 选择 regression-suite 作为主 QA 路径，并引用已实现变更、现有 TEST_SUITE/FLOW_INDEX 记忆和 CI WebKit 间歇失败，说明其用于已实现变更的验收回归及已知失败复核。 |
| `assertion_2` | FAIL | 列出了 PM/spec、实现变更、CI、平台版本、凭据/账号和执行入口，但错误称实际命令未提供；TRD 明确给出 `npm test -- login`，且输出未把该测试命令列为下游需读取或执行上下文。 |
| `specialist_gate_pointer` | PASS | 明确由 regression-suite 负责执行和写入 QA 结果，并要求其读取 E2E 记忆、平台版本、账号、测试入口及确认文档；未声称 router 自行执行 specialist 协议。 |
| `assertion_4` | PASS | 声明产出回归验证报告，并列出原失败复核、修复后行为、相邻登录路径、WebKit 间歇风险及发布建议等结构化内容。 |
| `assertion_5` | PASS | 仅选择 regression-suite 主路由；将 WebKit 超时保留为回归风险，并将 bug-analyzer 表述为需要时追加的后续路由，未确认其为产品缺陷。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=c7c249f4483b648a47162974aed0cef1bf6b72587da21ee58dc5e5b4cce04ff2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 regression-suite 并设置 specialist 门禁、输入上下文、证据报告和风险边界；但遗漏并错误否认了 fixture 中已有的 `npm test -- login` 测试命令。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=62a204eb4145bf968f199e4989b55b014722bcda100c86d5e24657a45696a887; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出有条件验收建议、重跑和证据清单，但未声明 specialist 主路由、下游读取责任或结构化路由产物。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2：未列出 fixture/TRD 已明确提供的 `npm test -- login` 测试命令，并错误称实际命令未提供。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bf605f953dcf46f19d2e331c4596d99cf4c0c84b7fc1582467970e0cc18f8ccd`
- Skill overlay SHA-256: `47f8d27a29d5dd33a6342a89bc1649d94b7a1e07378095c0146bd532fba34f55`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8760002335c8bb2569740b1d9606f6d16389f59c36b73454de4412fbf58d2bd7`
- Metadata SHA-256: `4be0f47d4261e8c4b656f6ffc80cff8a92794168034f2231da1ec209e3d5f4fd`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | 选择了 regression-suite，但没有说明其相较于 spec-based-tester、exploratory-tester、bug-analyzer 为什么更窄、更适合当前 evidence outcome。 |
| `assertion_2` | PASS | 列出了 PM/Engineer 文档、QA 记忆、实现变更、CI 风险、平台版本、QA URL 和测试执行入口，并明确指出其中缺失项。 |
| `specialist_gate_pointer` | FAIL | 指出 regression-suite 专员未安装及其检查项缺失，但没有明确声明该 specialist 是后续验证的执行责任方并保留该责任。 |
| `assertion_4` | PASS | 声明了 testcase 结果、快照、平台回归汇总、WebKit 重跑记录及验收结论等预期 artifact 结构。 |
| `assertion_5` | PASS | 只选择一个主 route；将 WebKit 问题作为已知风险并要求重跑确认，没有将其直接认定为 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=f4ceceeec403a33d9d5289207a80984929af71bf8cec6b5d3e243c46de8d1a52; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 regression-suite 并识别缺失的执行前置条件，提供回归证据产物和阻塞结论；但缺少与其他 route 的适配性比较及明确的 specialist 责任指针。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=67482e99e91fcac61320fff8ec5b2c53694f31d16e5670f9b7857b8f26f10895; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出谨慎的条件性验收建议和证据清单，但未选择规定的主 QA route，也未建立 specialist 路由门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未满足 assertion_1 的 route 比较与适配性理由要求。
- 未满足 specialist_gate_pointer 的 specialist 执行责任声明要求。
- Next: 补充 regression-suite 相较其他候选 route 更适合当前回归/evidence outcome 的明确理由。
- Next: 明确声明 regression-suite specialist 是后续验证的执行责任方，并保留其检查 E2E 记忆、平台版本、凭据、执行入口和确认文档的责任。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bf605f953dcf46f19d2e331c4596d99cf4c0c84b7fc1582467970e0cc18f8ccd`
- Skill overlay SHA-256: `47f8d27a29d5dd33a6342a89bc1649d94b7a1e07378095c0146bd532fba34f55`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8760002335c8bb2569740b1d9606f6d16389f59c36b73454de4412fbf58d2bd7`
- Metadata SHA-256: `4be0f47d4261e8c4b656f6ffc80cff8a92794168034f2231da1ec209e3d5f4fd`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | 选择了 spec-based-tester，但未明确说明其相较 exploratory-tester、bug-analyzer、regression-suite 更窄、更适合当前 evidence outcome 的理由。 |
| `assertion_2` | FAIL | 列出了 PM、TRD、实施计划、QA 套件和 CI 日志，但未明确列出下游需先读取的测试命令；环境说明也未作为前置读取项完整列出。 |
| `specialist_gate_pointer` | FAIL | 虽然声明路由给 spec-based-tester，但未声明该 specialist 是后续验证执行责任方，也未保留其检查 E2E 记忆、平台版本、凭据、执行入口和确认文档的责任。 |
| `assertion_4` | PASS | 明确给出结果文件、testcase snapshot、汇总报告及报告字段，并要求附 CI run、分片、版本、日志和截图/trace 等证据。 |
| `assertion_5` | PASS | 仅选择一个主 route；将间歇性 WebKit 失败作为阻断/风险证据，并指出只有稳定复现后才转 bug-analyzer，未直接认定 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=de8845790f9a8ea01c31f3f7afea97ac674f58ed7221e20e32a28a3bcebe7fd0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 spec-based-tester，保留间歇性 CI 问题的不确定性，并提供了较具体的验收产物和证据结构，但遗漏了明确的 route 对比理由及 specialist 门禁责任指针。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=ce9a6be329768eaf70522b8abe25af4422af725c65d9d1023f90307879182599; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未选择明确的 QA specialist route，但提出了定向复测、风险归因和验收证据要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 assertion_1、assertion_2 和 specialist_gate_pointer。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a20bd075e7e1649c2f9f1462392950229b31be9ed570a4e240d839bf872da003`
- Skill overlay SHA-256: `d4ab131d99e5579f17064924f9d9743db223506c52279c1e16497a0001a19110`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `df4278b098e7470d5c41718341478d7c82c0968178c0b46c4b2f1526aa5b9366`
- Metadata SHA-256: `4be0f47d4261e8c4b656f6ffc80cff8a92794168034f2231da1ec209e3d5f4fd`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | 选择了 spec-based-tester，但未说明其相较 exploratory-tester、bug-analyzer、regression-suite 为何更窄、更适合当前 evidence outcome。 |
| `assertion_2` | FAIL | 列出了所需补充证据，但没有明确列出下游 skill 需要先读取的 PM/spec、实现变更、CI 失败信息、环境说明和测试命令。 |
| `specialist_gate_pointer` | FAIL | 虽声明以 spec-based-tester 为主路由，但未指向 specialist 的权威 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 及 blocked-condition 门禁。 |
| `assertion_4` | PASS | 声明了 feature-update 汇总报告，并包含 passed/failed/blocked、风险、验收建议，以及逐项结果、trace/screenshot 和 CI 重跑记录等产物结构。 |
| `assertion_5` | PASS | 选择单一主路由，并将 WebKit 间歇性问题标为 suspected/needs more evidence，明确只有稳定复现后才转 bug-analyzer，未确认其为产品 bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=5cb559c67085a311f5ff5d7411c3303def5174c70c8f6615a451a0a664e7edc6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 spec-based-tester，正确保留 WebKit 问题为待证实风险并规划结构化验收证据，但缺少 route 对比、下游上下文读取清单和 specialist 权威门禁指针。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=a3dc3ea80b96eeef08ba7d7b51fbba3a46ede0aa5c64e372a65fc3548c826dfb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提出受控验收和补证据建议，但未选择规定的主 QA route，也未满足 specialist 门禁指针要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_1
- assertion_2
- specialist_gate_pointer
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fce4a3d76c9b69c96fdd86c3a44479dd8a12dd392536b124aa25210a7efca146`
- Skill overlay SHA-256: `02078f32eed1000178bae7f378d81856a077951dbb061b6ea461010744428cde`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `df4278b098e7470d5c41718341478d7c82c0968178c0b46c4b2f1526aa5b9366`
- Metadata SHA-256: `4be0f47d4261e8c4b656f6ffc80cff8a92794168034f2231da1ec209e3d5f4fd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill selects spec-based-tester as the main route, frames the work as feature-update scope acceptance, and contrasts it with full regression and immediate bug analysis. |
| `assertion_2` | FAIL | It names PRD/TRD/implementation plan and QA materials, plus platform/browser version, but does not explicitly require downstream reading of environment instructions and a concrete test command; the CI failure input is discussed rather than listed as required context to read. |
| `specialist_gate_pointer` | FAIL | It selects spec-based-tester and mentions platform version plus PRD/TRD/implementation plan, but does not point to authoritative E2E memory, credentials, execution entry, or blocked-condition gate applicability. |
| `assertion_4` | PASS | It specifies requirement matrices, feature paths, evidence references, per-TC result directories, a feature-update report, and risk/blocked-item treatment. |
| `assertion_5` | PASS | It uses spec-based-tester as the single main route, defers bug-analyzer to a stable reproduction, and explicitly says the intermittent symptom must not be marked a confirmed bug. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=46abced89ee013ee28226b77ce8e2935c16ca291baf14edc8ee16e1e9d70e04d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selects spec-based-tester, preserves the intermittent-failure risk distinction, and defines structured artifacts, but omits required downstream context details and the specialist authority gate pointer.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=6b7986914c4a65bdcb3f55a996fa36de4a267edc12cee141a31d96962479994c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a reasonable conditional-acceptance recommendation and evidence suggestions, but does not select a QA specialist route or satisfy the required routing and handoff structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2: missing explicit environment-instructions and concrete test-command context requirements.
- specialist_gate_pointer: missing authoritative E2E memory, credential, execution-entry, and blocked-condition gate pointers.
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

# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Natural user prompt:

> 用户说：这个登录重构已经按 docs/pm/login-refresh/PRD.md 实现了，但 CI 里有一个 intermittent 失败，同时 PM 想知道是否可以进入验收。请处理这个 QA 请求。

- Expected artifact: QA 路由决策，明确选择最窄的下游 QA skill、选择理由、需要读取的上下文和预期 evidence artifact

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-001-route-mixed-qa-request/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `483b12548bcebdb174340d9db79ae8cf525be3c084f49f4d2adec731730ab5bc`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 0 / FAIL 5 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>路由选择 | FAIL | candidate.md 与 transcript item_2 明确写成“主路由应为 spec-based-tester， 并联动 bug-analyzer”，没有只选择一个主 route，也没有说明该 route 为什么比其他 QA skill 更窄、更适合 evidence outcome。 | FAIL | candidate.md 没有选择 spec-based-tester、exploratory-tester、bug-analyzer 或 regression-suite 中的主 route，也没有比较适配性。 |
| `assertion_2`<br>上下文传递 | FAIL | candidate 只列出 PRD、TEST_SUITE 和 CI log；未列出实现变更、TRD/环境说明和测试命令。虽然 transcript item_3 实际读取了这些文件，但输出没有完整传递下游所需上下文。 | FAIL | candidate 没有完整列出 PM/spec、实现变更、CI 信息、环境说明和测试命令；transcript item_2 读取了相关文档，但 item_5 仅输出无 package.json，未形成完整下游上下文清单。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | candidate 没有声明选中的单一 specialist，也没有指出其权威 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 门禁适用；仅泛称“启用相应 QA specialist”。 | FAIL | baseline 没有路由 specialist，也没有任何 required specialist gate pointer。 |
| `assertion_4`<br>结构化产物 | FAIL | candidate 只列出三项后续结果（路径证据、失败复现/根因/回归、可验收结论），没有声明 requirement matrix、execution path、evidence references、risk notes 或 defect handoff notes 等结构化 artifact 结构。 | FAIL | candidate 仅给出 No-Go 和建议，没有声明结构化预期 artifact。 |
| `assertion_5`<br>边界控制 | FAIL | CI fixture 已触发该边界条件。candidate/transcript item_2 明确提出同时联动两个下游 skill；这违反“不能同时执行多个下游 skill”。虽未把 CI 直接写成 confirmed bug，但仍不足以抵消并行路由违规。 | PASS | baseline 没有同时执行或并联多个下游 skill，也没有把 intermittent CI 直接定性为 confirmed bug；其结论是先确认等待条件、重跑并补证据。 |

## With-Skill Behavior

with_skill 未满足路由器要求：同时列出 spec-based-tester 与 bug-analyzer，且缺少 specialist 权威门禁指针、完整上下文清单和结构化 artifact 说明。快照与 transcript 证实没有执行下游 specialist。

## Fresh Without-Skill Baseline

without_skill 未完成 QA 路由输出，但其边界结论未把 intermittent CI 直接定性为 confirmed bug。两条 lane 的最终快照文件树、文件内容及 fixture 哈希完全一致。

## Failures

- with_skill 的 assertion_1：选择了两个下游方向，且未说明单一主 route 相对其他 route 的窄适配理由。
- with_skill 的 assertion_2：未完整传递实现变更、环境说明和测试命令等下游上下文。
- 两条 lane 的 specialist_gate_pointer 均缺失权威门禁指针。
- 两条 lane 的 assertion_4 均未声明结构化 evidence artifact。
- with_skill 的 assertion_5：明确并联 spec-based-tester 与 bug-analyzer。

## Not Exercised

- 无。

## Next Steps

- 将主 route 明确限定为 spec-based-tester；把 CI intermittent 作为 risk note 或后续 handoff，不并行执行 bug-analyzer。
- 补充下游读取清单：PRD/spec、TRD、implementation changes、CI log、平台/环境说明和 npm test -- login；不得预设固定端口或浏览器。
- 加入 specialist 权威门禁指针，并声明 requirement matrix、execution path、evidence references、risk notes/defect handoff 等 artifact 结构。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
