# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264` from `agents/engineer/test/feature-implementor/evals/workspace/eval-001-implement-from-prd-trd`.
- Fixture SHA-256: `65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264`
- Prompt SHA-256: `9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bd840cbb6d300dba8607f0e2ffca8d1cce35f8afa38a03d78fa95279dfa455c6`
- Metadata SHA-256: `3f1598f1147e9d9fe4d3d8e602cb67a07409635701fd037d50b6d22e59d01fd0`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `writes_implementation_plan` | FAIL | with_skill 未输出或创建 IMPLEMENTATION_PLAN.md，也未提供文件变更清单；仅给出后续实施顺序。 |
| `requires_user_confirmation` | PASS | 明确表示正式实施安排提交后需等待用户明确批准，再开始编码。 |
| `does_not_implement_directly` | PASS | 未声称创建或修改代码、运行实现步骤或完成自检；明确表示当前不能进入编码。 |
| `maintains_plan_metadata` | NOT_EXERCISED | git_evidence 显示工作区无变更，实际未创建 IMPLEMENTATION_PLAN.md，因此无法检验其 frontmatter 元数据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636; fixture_sha256=65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264; output_sha256=6e078ce16d8e71715bbc2308c8edde34ca1da2608e7ab3b2bcc6757cbdadd720; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并强调了 UI 设计和 TRD 细节缺口，未创建计划文件，给出后续实施顺序并要求文档补齐及批准。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636; fixture_sha256=65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264; output_sha256=846830c4c8e38b28a2e3e4de333539308dc92d69ab908d8aaa40e7d2bafab93c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以只读梳理形式提供了实施安排、文件清单和确认问题，但未创建正式计划文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足本轮要求输出/创建可审查的 IMPLEMENTATION_PLAN.md 及文件变更清单。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264` from `agents/engineer/test/feature-implementor/evals/workspace/eval-001-implement-from-prd-trd`.
- Fixture SHA-256: `65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264`
- Prompt SHA-256: `9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `49964bfa40c4eb79d538198181fe371ea6dcc248c5f39dacb89d13915c52387e`
- Metadata SHA-256: `3f1598f1147e9d9fe4d3d8e602cb67a07409635701fd037d50b6d22e59d01fd0`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `writes_implementation_plan` | PASS | With-skill output identifies IMPLEMENTATION_PLAN.md, lists the three planned file changes, and states the implementation order. |
| `requires_user_confirmation` | PASS | With-skill output explicitly asks the user to confirm the plan before coding. |
| `does_not_implement_directly` | PASS | With-skill raw evidence shows only the implementation plan was added; no code files, implementation steps, or self-checks are claimed as completed. |
| `maintains_plan_metadata` | FAIL | The plan frontmatter contains version and last_updated, but the output does not explain the required initial-version rule or when substantive versus formatting updates change version metadata. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636; fixture_sha256=65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264; output_sha256=9e3aaf7b88d3bdc1f194641913a6d17474563937e92bcd78011932c794901664; snapshot_sha256=8c85e1d0aae5cbb3742b9a293d863c9ebd313a997638a42ff14739451834eac7
- Behavior: Created the implementation-plan document, listed scoped file changes and ordered steps, and gated coding on confirmation; metadata update-policy requirements were incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9724c537ded4c14b592d897088f388268956cff28e97f04ba4a128111c8f5636; fixture_sha256=65e03f7a1f44ddf6741e1196f7a8aa0bb58bff8733bbd1a64bd05da5fdd0d264; output_sha256=5322b8149ad2dae7ed88008e25ccf75857dc3de3dcf830618bc338a54f14cbd1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a detailed proposed implementation sequence and requested confirmation, but did not create the required implementation-plan document or provide its metadata policy.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not state the required version and last_updated maintenance rules for initial plans, substantive updates, and formatting or typo-only fixes.
- Next: Add the complete frontmatter maintenance policy to the implementation-plan output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-001-implement-from-prd-trd`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `f28befa0f58d85ac2ecb3e6c24e0090a145d4ddb6231b7848d726f4aa1c607e7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e8316f0aa4590c63e65f70612d76f8fbcd38a328f8061718a97190f173e80bf3`
- Metadata SHA-256: `a03f40843844b3baa3ce9f2eed494948253034bd0a93be1411356fd09a957890`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `writes_implementation_plan` | FAIL | with_skill 仅承诺收到文档后生成计划，并未实际生成实施计划、文件变更清单或实现顺序。 |
| `requires_user_confirmation` | PASS | 明确表示“你确认计划后再开始编码”。 |
| `does_not_implement_directly` | PASS | 未声称已创建或修改代码文件、运行实现步骤或完成自检。 |
| `maintains_plan_metadata` | FAIL | 未提及 IMPLEMENTATION_PLAN.md 的 frontmatter、version、last_updated 或版本更新规则。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f28befa0f58d85ac2ecb3e6c24e0090a145d4ddb6231b7848d726f4aa1c607e7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b00f9dbe1c5e995b84407e547532d5e4a58c8205cfa9cebbaaa954c8ce3377ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因工作区缺少文档而暂停，承诺后续生成计划并等待确认，但未实际提供计划内容或元数据要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f28befa0f58d85ac2ecb3e6c24e0090a145d4ddb6231b7848d726f4aa1c607e7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3cf826448d5b2b8a2a875e40f2eec4bb72d174e0f9610004ddc9f7f648d933cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了较完整的实施安排并要求负责人确认后编码，但未说明计划元数据规则。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足生成实施计划及文件变更清单、实现顺序的要求。
- with_skill 未满足实施计划元数据维护要求。
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

# Eval Result: eval-001-implement-from-prd-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`
- Test case: implement-from-prd-trd
- Workspace: `workspace/eval-001-implement-from-prd-trd`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 根据 docs/pm/notification-center/PRD.md 和 docs/engineer/notification-center/TRD.md 实现用户通知功能
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `writes_implementation_plan`: final.md 未包含实现计划、文件变更清单或实现顺序；workspace 中也不存在 IMPLEMENTATION_PLAN.md。
- FAIL `requires_user_confirmation`: 仅说明补齐文档后才能创建计划，未明确要求用户确认实施计划后再编码。
- PASS `does_not_implement_directly`: final.md 和 with_skill transcript 均未声称已创建/修改代码、运行实现步骤或完成自检。workspace 仅有既有指令文件，无代码变更。
- FAIL `maintains_plan_metadata`: 输出未说明 IMPLEMENTATION_PLAN.md frontmatter 的 version、last_updated 或版本维护规则。

## With Skill Behavior

with_skill 正确识别工作区缺少 PRD/TRD，并未直接写代码；但未按 expected_output 生成计划内容、文件清单、顺序、确认门禁或计划元数据说明。output.sha256 与 workspace 文件逐项校验通过。

## Without Skill Baseline

without_skill 同样发现工作区为空并停止；仅作对照，不影响 with_skill 判定。其 input/output hash 文件为空，workspace 无 .git。

## Failures / Findings

- writes_implementation_plan
- requires_user_confirmation
- maintains_plan_metadata
- Root cause: 实际 fixture workspace 不含用户指定的 PRD/TRD，with_skill 因门禁阻塞而只输出缺失文档提示；该输出未满足 eval.json 明确要求的计划与确认协议。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-implement-from-prd-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`
- Test case: implement-from-prd-trd
- Workspace: `workspace/eval-001-implement-from-prd-trd`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: metadata-only case whose prompt supplies the confirmed `notification-center` PRD/TRD paths and whose expected output defines the planning behavior.
- Fixture version: current HEAD `a452319`.
- Fresh run time: `2026-08-03 11:58:13 +0800`.
- Runtime directory: `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/feature-implementor/eval-001-implement-from-prd-trd/`.
- Expected output: produce or update `docs/engineer/notification-center/IMPLEMENTATION_PLAN.md` with the file change list, implementation order, metadata rules, and user-confirmation gate; do not code directly.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 4 assertions were exercised and passed. Removing BRD from the planner input list did not weaken PRD/TRD alignment, durable plan metadata, or the pre-code confirmation gate.

## Assertion Results

- PASS `writes_implementation_plan`: identifies `docs/engineer/notification-center/IMPLEMENTATION_PLAN.md` and requires a source-traceable file list, ordered implementation steps, tests, and verification before implementation.
- PASS `requires_user_confirmation`: stops after presenting the exact plan and requires explicit user confirmation before loading the implementation phase.
- PASS `does_not_implement_directly`: does not claim code changes, implementation execution, tests, or self-review have occurred.
- PASS `maintains_plan_metadata`: requires an initial `version`, `last_updated`, feature-path linkage, and synchronized version/date updates for substantive plan changes while allowing typo-only edits not to bump the version.

## With-Skill Behavior

The fresh with-skill run applies the planner phase only, carries the prompt-declared same-path PRD/TRD through the fixture's metadata-only convention, and states the full alignment checks required in a real host workspace. It produces the durable plan path, the required file-list and dependency-order behavior, verification and delegation fields, and the frontmatter maintenance contract, then waits for confirmation without coding. The planner now consumes PRD plus `DECISIONS.md` or equivalent product decisions and TRD; no removed BRD prerequisite remains.

## Fresh Without-Skill Baseline

The without-skill baseline was newly generated in this run from the same prompt and fixture without applying `feature-implementor`, the Engineer README, with-skill output, historical comparison, or any prior baseline. It suggests reading the specs and planning before implementation, but does not require the durable plan path, exact metadata/version rules, or a hard confirmation boundary. Baseline assertion result: 1/4.

## Failures

- None.

## Next Steps

- Keep this eval focused on the PRD/TRD-to-plan gate, plan metadata maintenance, and no-direct-code boundary after BRD removal.

## Runtime Artifact Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/feature-implementor/eval-001-implement-from-prd-trd/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are ignored scratch evidence and must not be committed.
- This `comparison.md` is the only durable result for this case.
