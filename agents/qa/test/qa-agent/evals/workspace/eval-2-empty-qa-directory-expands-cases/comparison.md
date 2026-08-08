# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d70112827b0542d867a7689306d190b9c9a901f0d16faf502ff69330466e810c`
- Skill overlay SHA-256: `3673b22dfa628fadf9c4bb5597b7b2a2e950ec87dc67f02d57318ceb09cf90cb`
- Judge schema SHA-256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill output recognizes no executable QA cases and does not fall back to the legacy directory. |
| `assertion_2` | FAIL | The output passes the target directory, environment, source files, and selected specialist downstream, but explicitly returns blocked at the qa-agent gate. |
| `specialist_gate_pointer` | PASS | It selects spec-based-tester as the execution owner and states qa-agent will not execute directly, while passing the relevant context. |
| `assertion_6` | PASS | It selects one narrow route, spec-based-tester, without running multiple QA skills or expanding into implementation repair. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=77f53f79057977d0fccd55e14bed9df0d24b4a74a27a5b94f18831882f3365fe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selected spec-based-tester and identified the supplied QA context, but stopped with a blocked result.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=b907d2da1749f2a1beaae0c0d15e2d9148539967424df0971f1382f5d354c9f0; snapshot_sha256=e0fb63a7f356855fac72d9a0a511899838f76d7bfa05db92939fa8dcfd422793
- Behavior: Created a five-case QA suite and flow index, but performed the work directly without specialist routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2 is contradicted by the explicit blocked-at-entry-gate outcome, despite the required downstream context and specialist selection.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d70112827b0542d867a7689306d190b9c9a901f0d16faf502ff69330466e810c`
- Skill overlay SHA-256: `3673b22dfa628fadf9c4bb5597b7b2a2e950ec87dc67f02d57318ceb09cf90cb`
- Judge schema SHA-256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确识别目标 QA 目录仅有 TEST_SUITE.md 和 FLOW_INDEX.md，且 cases/ 等无可执行用例；未回退到旧目录。 |
| `assertion_2` | FAIL | with_skill 虽声明已获授权并列出相关资料，但随后在入口门禁处直接阻塞并要求补充 PM handoff/安装 pm-agent，违反了不得直接返回 blocked 的要求。 |
| `specialist_gate_pointer` | PASS | with_skill 选择 spec-based-tester 作为后续责任方，并将 QA 资料、页面/表单实现及环境说明作为依据传递；未声称由 router 执行 specialist 协议。 |
| `assertion_6` | PASS | with_skill 选择了单一且最窄的 spec-based-tester 主 route，未执行多个 QA skill，也未扩展到实现修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=95a33a9cfaac362f7bddf75c651ffe4daf843af2bfdc920bb14f49ede4d255d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别空 QA 目录并选择 spec-based-tester，但因不必要的 PM 门禁错误阻塞后续路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=08c3ba9d6211c57f98f8d3a25e59961c673afa66a15fb861e6e95386a148e2fc; snapshot_sha256=7f66efe32d4521e6e490472629089ce154a421e971eca67269562012bd175533
- Behavior: 直接修改并新增 E2E 用例文件，未遵循路由和 specialist 门禁要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 在已获授权探索的情况下错误地将流程阻塞并要求 PM handoff/安装 pm-agent。
- Next: 移除不适用的 PM handoff 阻塞，继续将目标文件、环境说明和现有 QA 记忆交给 spec-based-tester。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ac14179f2aca4133a304fb2ec1e6f0613baa189aa0feceb7d5432c5a227afc79`
- Skill overlay SHA-256: `92c856407dda15bb2ec8dfea24b4313a280d4357969be16e1cbafe055eb08662`
- Judge schema SHA-256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确说明现有 QA 目录没有可执行用例、脚本或历史结果，且未回退到旧的单层目录。 |
| `assertion_2` | FAIL | 虽列出目标源码和 QA 文档，但未将 environment/qa-env.md 作为下游上下文传递，并直接称验证被入口门禁阻塞、要求补充资料。 |
| `specialist_gate_pointer` | FAIL | 声明 spec-based-tester 负责后续用例创建和执行，但未传递环境说明；该门禁指针要求未完整满足。 |
| `assertion_6` | PASS | 只选择 spec-based-tester 作为主 route，未执行多个 QA skill，也未扩展到实现修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=9e08c1fe75a1d100ef4ffbcc901c007e3529efa634dbd3876f8a91008ce346fe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别空覆盖目录并选择单一 specialist，但路由过早阻塞且下游上下文不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=4a0cf0e4b96ca43958b870075c26ef781bff7efbbf3870d25323dce830e0af04; snapshot_sha256=d1ae3715c0e0dee27b65bf96a088a0d2bc250fd46fea29467d8fc8bd2a63b52b
- Behavior: 实际创建了测试文档和用例，但属于比较上下文，不用于降低 with_skill 断言失败。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 路由在用户已授权探索的情况下直接返回入口阻塞并要求补充资料。
- with_skill 未把 environment/qa-env.md 明确交给 specialist。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ac14179f2aca4133a304fb2ec1e6f0613baa189aa0feceb7d5432c5a227afc79`
- Skill overlay SHA-256: `92c856407dda15bb2ec8dfea24b4313a280d4357969be16e1cbafe055eb08662`
- Judge schema SHA-256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 识别了目标 QA 目录存在，但仅有 TEST_SUITE.md、FLOW_INDEX.md，且没有可执行 TC 或脚本；未回退到旧目录。 |
| `assertion_2` | FAIL | 输出直接将任务判定为阻塞，并要求用户补充资料后再继续，未把目标项目文件、环境说明传递给下游 specialist，也未声明已适用的 specialist 执行门禁。 |
| `specialist_gate_pointer` | FAIL | 仅提到未来由 spec-based-tester 完成，但没有声明其为当前后续验证的权威执行责任方，也没有交付目标文件、环境说明和 E2E 记忆。 |
| `assertion_6` | PASS | 只指向 spec-based-tester 一个主 QA route，未执行多个 QA skill，也未扩展到实现修复。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=6e6d7e5e214943c8695a7b89a0784b2d1624bdb356b0f325ff14de669fae5d01; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别空 QA 覆盖目录并选择 spec-based-tester，但错误地阻塞任务，未完成授权后的下游路由和上下文传递。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=aa14b7018c6cf18b78b46ef75d61856f00b8aeab109dcef262d68277e415a7d7; snapshot_sha256=d7e757c4cbf9ae6fd1f189fa23c4f6134072a227490723df7f2843757762f85a
- Behavior: 创建了 QA 用例和报告，但其行为属于直接补充交付物，未体现所要求的路由门禁；仅作比较上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未在用户已授权探索的情况下完成路由上下文传递，反而直接返回 blocked 并要求补充资料。
- with_skill 未满足 specialist 权威门禁指针要求。
- Next: 在已授权前提下将目标项目文件、环境说明和现有 E2E 记忆交给 spec-based-tester，并声明其为后续验证的执行责任方。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ac14179f2aca4133a304fb2ec1e6f0613baa189aa0feceb7d5432c5a227afc79`
- Skill overlay SHA-256: `92c856407dda15bb2ec8dfea24b4313a280d4357969be16e1cbafe055eb08662`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill acknowledges the existing QA path but does not identify that TEST_SUITE.md, FLOW_INDEX.md, and cases/ contain no executable test cases, nor explicitly reject treating the directory as existing coverage or falling back to the old directory. |
| `assertion_2` | FAIL | with_skill incorrectly blocks on a missing PM handoff and requests additional confirmation/materials despite the prompt already confirming the feature update and authorizing exploration; it does not pass the provided project and environment context downstream. |
| `specialist_gate_pointer` | FAIL | with_skill says it cannot enter spec-based-tester and only describes what the specialist should do; it does not select the specialist as execution owner or hand it the target files, environment, and existing E2E memory. |
| `assertion_6` | FAIL | with_skill does not select a narrow primary route; it defers routing pending pm-agent work and returns that E2E creation/execution cannot proceed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=0d944297e925dcde7559a44896bda9fce380b847d1d0f6bd87c263aecdb56a42; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Returned a blocked/deferred routing response, citing missing PM handoff and failing to select or activate the required specialist route.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=5fc72dfdd755257bdca01af261d3072c8d086f86543700a493b3998c11fb4df2; snapshot_sha256=e01f3d95508e25007109a78ca31eb5e4c566dd5cda82823a5b7a07e5b2f2a01e
- Behavior: Created and modified the profile-form QA documents with six blocked cases, but did not demonstrate the required specialist routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane contradicted the authorized-exploration and specialist-routing requirements.
- The with_skill lane omitted the required empty-directory recognition and downstream context handoff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `afcc089a4522fb7587710a20e21adb99a4567c8fc61ab08b5aa456f6ceac23cb`
- Skill overlay SHA-256: `16c159ed291e76c7e6248dea0961cc074c51aa07aae71248dc9e8009292217a7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill says no cases were created, but does not explicitly identify the existing QA directory as empty/non-executable or distinguish it from a prior single-layer directory. |
| `assertion_2` | FAIL | It correctly names the project files, environment, and spec-based-tester, but incorrectly returns the workflow as blocked and asks for PM/Engineer handoff and credentials despite the user's prior authorization to explore. |
| `specialist_gate_pointer` | PASS | The output selects spec-based-tester as responsible for downstream E2E verification, states that it will read the complete materials and execute, and says the router will not execute tests directly. |
| `assertion_6` | PASS | It selects one narrow primary route, spec-based-tester, and explicitly keeps execution with that specialist without expanding into implementation or multiple QA skills. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=aff58b50d8b192d8baba7ed8b50424b36c2c9cf899f86bb84b23376020bb5b2c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selected a single spec-based specialist and preserved the router boundary, but incorrectly blocked on additional handoff materials and did not clearly identify the empty QA coverage directory.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=8dbeb67d80ae3c67cda75d8ed466c669982d0b812f23826830bfe639269ac264; snapshot_sha256=fffd8c61643e9e4f8d2a540a974755fe728d6fbdc1827d337f52be6f03ed88dc
- Behavior: Created and modified QA artifacts and reported a blocked run; it did not provide the required specialist routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill incorrectly re-requested PM/Engineer handoff and runtime/account materials instead of proceeding under the user's existing exploration authorization.
- with_skill did not clearly identify the existing profile-form QA directory as lacking executable cases.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bf605f953dcf46f19d2e331c4596d99cf4c0c84b7fc1582467970e0cc18f8ccd`
- Skill overlay SHA-256: `56ef2d43180dea784b914fa8976f7eea9cd5a503412b7838586b3195fe555016`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill identifies the existing profile-form QA directory, checks TEST_SUITE.md and FLOW_INDEX.md, and states that no active executable TC exists. This matches the fixture's empty-suite state. |
| `assertion_2` | FAIL | With_skill only reports blockers and lists files checked; it does not route the target files and environment as downstream context or declare an applicable specialist execution gate. The user had already authorized exploration. |
| `specialist_gate_pointer` | FAIL | With_skill does not identify a selected specialist as the verification owner or hand off the project files, environment notes, and existing E2E memory. |
| `assertion_6` | FAIL | With_skill selects no narrow primary route and returns blocked instead of assigning a single QA specialist route. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=659e4f1944d3502a0afee97313d8079ae939032b32dd566e4777ccb11528d5c8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognized that the fixture has no active executable cases, but incorrectly stopped at unrelated blockers and omitted the required specialist routing and handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=287994d270fbbc57889e58189016f6572e2eb924ad43e4b00bfb0a894378daea; snapshot_sha256=ad825740c159e3b02daf0ac49800b1b40aba00e0aa869b47c6b5d7463f2407bd
- Behavior: Created E2E documentation and correctly noted runtime blockage, but did not provide routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2
- specialist_gate_pointer
- assertion_6
- Next: Select one narrow QA specialist route and explicitly hand off the target files, environment notes, and existing E2E memory.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a20bd075e7e1649c2f9f1462392950229b31be9ed570a4e240d839bf872da003`
- Skill overlay SHA-256: `badb7717b586c61e5dc54d1f19f46df7c0dd13d0c9640c7f20d0dcbfe6068ee7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4e55e5728edf1af511c4153d6f4ebee13eca98f8056d3af30cfe3314c96bd08e`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill evidence states the existing suite/flow index had no reusable cases, scripts, prior results, or reports, and it worked within the requested profile-form path without reverting to the legacy single-layer directory. |
| `assertion_2` | FAIL | The with-skill output documents QA artifacts and blockers but does not route downstream context containing the target files and environment instructions, nor declare an applicable selected specialist gate. |
| `specialist_gate_pointer` | FAIL | The with-skill route/output does not name a selected specialist or point to the required authoritative E2E memory, platform, credential, execution, PRD/TRD/implementation-plan, and blocked-condition gates. |
| `assertion_6` | PASS | The with-skill changes remain narrowly scoped to profile-settings E2E coverage and blocked execution; they do not execute multiple QA skills or expand into implementation fixes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=6f81073d3df397d35dd7a3c7b66cb385bbd271e35c8cbb6ec7cd05da8ff1b87a; snapshot_sha256=7e1452b47de005ee3f89f57efc7896d27a6ce9b1727e35cae5e26f05fd9939be
- Behavior: Identified the empty QA area, added three focused cases and blocked results, but omitted the required specialist route and authoritative gate pointer.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=f0e5bc48f7b1b5ec5d1e0f9d3ae4450f6329948cc0dc62af3bcfe5876af2d897; snapshot_sha256=a569d2b18865b4b0c1730860ce85092646185c4b07a4b097f217844881c7e836
- Behavior: Created six profile-form cases and reports, correctly marked execution blocked, but provided no specialist-routing or gate-pointer behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required downstream context transfer and specialist authority declaration.
- The with_skill lane omits the required specialist gate pointer.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fce4a3d76c9b69c96fdd86c3a44479dd8a12dd392536b124aa25210a7efca146`
- Skill overlay SHA-256: `99289d48bcdf7ee91c35f76d50558d9c6f447a5da7e5945959c194da781dd666`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4e55e5728edf1af511c4153d6f4ebee13eca98f8056d3af30cfe3314c96bd08e`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill evidence states no reusable TC or execution harness existed before the update and identifies the existing feature-path files, then adds scoped cases under the same profile-form directory. |
| `assertion_2` | FAIL | The with-skill output directly concludes blocked and does not provide a routing handoff carrying the target files/environment context or declare an applicable specialist. |
| `specialist_gate_pointer` | FAIL | No selected specialist or authoritative E2E-memory/platform/credential/execution/documentation gate pointer appears in the with-skill output; it instead lists blocker details. |
| `assertion_6` | FAIL | The with-skill output reports completed QA artifact generation but does not select or state a narrow primary route. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=b6c5e4c586aa80fb1051ac2b8c6d959550a37d0625821675ede34532b4c86b2e; snapshot_sha256=778f33dfda3e5f8b770e6baea2815283827c8903a0f55a7f10b05d413d9b1113
- Behavior: Added four scoped cases, scripts, blocked results, and a report for the correct feature path, but returned a blocked QA outcome without the required routing and specialist gate pointer.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=d47573c8de9ac0765520cecf5a5fbb3727775d8dcba38f3e799e8bdf2b8a9adf; snapshot_sha256=fd96769af078914269102a29e8f5d8947bcce5a491e019f286e70e8d189872c0
- Behavior: Created broad E2E documentation and marked browser execution blocked; no routing or specialist handoff was shown.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omitted the required authorized exploration routing context and specialist declaration.
- The with_skill lane omitted the specialist authority gate pointer and did not state a narrow primary route.
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

# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Natural user prompt:

> 用户说：请对 profile-settings 做一次 E2E QA。docs/qa/e2e/account/profile-settings/profile-form/ 已存在，但 TEST_SUITE.md、FLOW_INDEX.md 和 cases/ 里没有测试用例。我确认这个功能有新更新，请主动查看项目文件并完成验证。

- Expected artifact: QA 路由决策与执行协议，明确空 E2E 功能树目录需要触发目标文件探索、更新 TEST_SUITE.md 和 FLOW_INDEX.md、创建独立 TC 与 script 文件，并要求后续验证基于这些用例执行

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-002-empty-qa-directory-expands-cases/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `4b523a57597194309a66e74261387466f919e128463a54f5f7cd87e452b26823`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 1 / FAIL 3 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>空目录识别 | PASS | transcript 的初始文件读取显示 TEST_SUITE.md 明确写着无 active TC，FLOW_INDEX.md 为空且目标目录仅含既有文档；最终快照仍在同一 profile-form 路径下新增用例，没有回退到旧的单层 profile-settings 目录。 | PASS | transcript 读取并确认同一目标目录为空；最终快照在目标 profile-form 路径新增 3 个用例，没有使用旧的单层 QA 目录。 |
| `assertion_2`<br>授权后传递探索范围 | FAIL | 用户已在 prompt.txt 中确认有新功能更新并授权探索，但 transcript item_2/item_5 进入了实现检查和资产执行，最终消息也只报告补齐 cases；没有路由输出把项目文件、environment/qa-env.md 和选定 specialist 作为下游上下文，也没有明确 specialist 接手。 | FAIL | candidate/transcript 直接执行测试资产补齐，没有输出授权后的 specialist 路由、项目文件/环境上下文传递或门禁适用声明。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | transcript 仅声明按 qa-agent 流程工作，未声明选中的 spec-based-tester 或 exploratory-tester，也未指出其 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 指针适用。 | FAIL | without_skill transcript 没有 specialist 选择或权威门禁指针，仅自行补齐 cases/scripts。 |
| `assertion_6`<br>路由边界 | FAIL | 未选择一个最窄主 route。transcript item_0/item_2 说按 qa-agent 流程检查，但后续直接执行静态检查、创建 4 个 case/script 和结果文件；这属于下游 QA 执行而非完成路由输出，且最终消息没有明确 specialist 接手。 | FAIL | 未声明主 route 或 specialist，直接执行 3 个 case、script 和静态验证；因此无证据表明完成了要求的窄路由。 |

## With-Skill Behavior

with_skill 正确识别了目标 QA 目录为空，并在最终快照中创建了 4 个 case、4 个 script 和结果文件；但未完成 qa-agent 所要求的路由输出，未选择具体 specialist，也未声明 specialist 权威门禁指针，且实际执行了下游 QA 资产补齐工作。

## Fresh Without-Skill Baseline

without_skill 同样识别并补齐了目标目录，最终快照中有 3 个 case 和 3 个 script；但同样缺少路由选择与 specialist 门禁指针，作为 baseline 仅供对照，不影响当前结果。

## Failures

- with_skill 的 assertion_2、specialist_gate_pointer、assertion_6 均为 FAIL；已触发的 with_skill assertion 存在 FAIL，因此 Behavior=FAIL、Overall=FAIL。
- 最终快照证实 with_skill 创建了声称的文件；没有出现“候选声称创建但快照不存在”的额外失败。
- 两条 lane 均将浏览器执行标为 blocked；这不是本组 assertions 的覆盖缺失，但不能替代要求的路由输出。

## Not Exercised

- 无。

## Next Steps

- 补充明确的 qa-agent 路由输出：选择最窄主 route，按本请求应为 spec-based-tester，并传递目标项目文件与 environment/qa-env.md。
- 只保留 specialist 权威门禁的指针式声明，不在 qa-agent 路由中展开 specialist 内部协议。
- 将测试资产创建和执行交由选定 specialist，qa-agent 仅负责路由、上下文传递和预期证据产物说明。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
