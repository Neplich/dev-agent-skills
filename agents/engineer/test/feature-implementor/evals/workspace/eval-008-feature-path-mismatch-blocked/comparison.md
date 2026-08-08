# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-008-feature-path-mismatch-blocked`.
- Fixture SHA-256: `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d`
- Prompt SHA-256: `9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `66c4bea185008e1b43202328d058ecaa9e2ff572bdfe8be7d346a358d1c56597`
- Metadata SHA-256: `3365bfe92db70d4ff5499652a29702f93ac57621aa93b249c4712559af86079a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_trd_path_mismatch` | PASS | with_skill 明确列出 PRD feature_path 为 chat-interface/history-search、TRD feature_path 为 chat-interface，并指出未对齐。 |
| `checks_related_prd` | PASS | with_skill 明确检查并指出 TRD related_prd 指向不存在的 docs/pm/chat-interface/PRD.md，且因此无法安全实现。 |
| `blocks_implementation_plan` | PASS | with_skill 输出声明无法安全实现；git_status 和 git_diff 均为空，未创建实施计划或代码/测试修改。 |
| `hands_off_to_trd_gen` | PASS | with_skill 明确要求 engineer-agent 更新镜像 TRD，并说明 engineer-agent:trd-gen 完成 TRD。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=364cde90d3bb7fcba3da1dd9c08fd47ec63f75b0d6aef814b30c469dad2d92f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别路径及 related_prd 不一致，阻断实现并交回 engineer-agent:trd-gen，且保持工作区无修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=eb05d37ea6f3bd987338902c39b2bb3a7a1e67d493ba50bdd9f83628611e2964; snapshot_sha256=2e15a0f9ddb7f3872f75a00f54eae1aeb4b50f1158d45b54757570b9c61fd1c1
- Behavior: 错误地继续实现功能并修改了 TRD 与应用文件。
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
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-008-feature-path-mismatch-blocked`.
- Fixture SHA-256: `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d`
- Prompt SHA-256: `9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `66c4bea185008e1b43202328d058ecaa9e2ff572bdfe8be7d346a358d1c56597`
- Metadata SHA-256: `3365bfe92db70d4ff5499652a29702f93ac57621aa93b249c4712559af86079a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_trd_path_mismatch` | PASS | 明确指出 PRD 路径为 `chat-interface/history-search`、TRD 路径为 `chat-interface`，并说明二者不一致。 |
| `checks_related_prd` | PASS | 指出 TRD 的 `related_prd` 指向不存在的 `docs/pm/chat-interface/PRD.md`，并表示需先补齐 TRD，未继续规划。 |
| `blocks_implementation_plan` | PASS | with_skill 的 git_status 和 git_diff 均为空，输出明确说明未修改任何文件，未创建实施计划或代码/测试修改。 |
| `hands_off_to_trd_gen` | FAIL | 输出仅建议交给“Engineer”补齐子功能 TRD，没有明确交给 `engineer-agent:trd-gen`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=ce7bc9c215d7d5fc9a1fe5c228d36d15545cf054f6d1b95b7e94131e2ab09b63; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了路径和 related_prd 不一致，阻断实施并保持工作区干净，但未按要求明确交给 `engineer-agent:trd-gen`。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=7e7fdc120562d5e4e14b6ae4a50e7e126957cedeaacc8d97f96075797e96690c; snapshot_sha256=57e5a89f2dfaa95a6a74f4255c144a3a9f8270a9fbe756034e3c985b865cd34b
- Behavior: 未识别文档链阻断，直接实现功能并修改 TRD、创建代码文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确将下一步交给 `engineer-agent:trd-gen` 修正或重写镜像 TRD。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-008-feature-path-mismatch-blocked`.
- Fixture SHA-256: `fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d`
- Prompt SHA-256: `9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `66c4bea185008e1b43202328d058ecaa9e2ff572bdfe8be7d346a358d1c56597`
- Metadata SHA-256: `3365bfe92db70d4ff5499652a29702f93ac57621aa93b249c4712559af86079a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prd_trd_path_mismatch` | PASS | with_skill 明确列出 PRD `chat-interface/history-search`、TRD `chat-interface`，并说明二者对不上。 |
| `checks_related_prd` | PASS | with_skill 明确指出 TRD `related_prd` 指向不存在的 `docs/pm/chat-interface/PRD.md`，并要求先修正后继续。 |
| `blocks_implementation_plan` | PASS | with_skill 输出声明未修改任何文件；git_status、git_diff、delivery_snapshot 均为空，未创建实施计划、代码或测试。 |
| `hands_off_to_trd_gen` | FAIL | with_skill 要求补充并确认对应 TRD，但未明确交给 `engineer-agent:trd-gen` 修正或重写镜像 TRD。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=8349a14c55b41c97aa836f550b93fbe9501fd1b441134f5cbc3f1d8dc4701280; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别路径和 related_prd 冲突并阻断修改，但未按要求明确交回 `engineer-agent:trd-gen`。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ba9f5f01cabbae62ba3bf40c7c99d8dc7f337984c8ca4277c6f238b4df6793e; fixture_sha256=fa61fddb39b3b74bc77db4e82386f7b1f9cd3a070d4333160570607ea9172a8d; output_sha256=5a0970c229b88d378e7fff2c08d735ae455ed5cc8ce8444f47787cf193fa9962; snapshot_sha256=3329da9fa05bb112ce251c56f9ee9c8864b58f0c7377df370110637983d4b7cd
- Behavior: 直接按 PRD 路径实现并创建源码，未识别或处理 PRD/TRD 不一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确将下一步交给 `engineer-agent:trd-gen` 修正或重写镜像 TRD。
- Next: 明确交给 `engineer-agent:trd-gen` 修正或重写 `docs/engineer/chat-interface/history-search/TRD.md`。

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

# Eval Result: eval-008-feature-path-mismatch-blocked

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`
- Test case: feature-path-mismatch-blocked
- Workspace: `workspace/eval-008-feature-path-mismatch-blocked`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/chat-interface/history-search/PRD.md 和 docs/engineer/chat-interface/TRD.md 实现 Chat History Search。两份文档记录的功能路径不一致：PRD 是 chat-interface/history-search，TRD 是 chat-interface。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_prd_trd_path_mismatch`: 明确指出 PRD feature_path 为 `chat-interface/history-search`、TRD feature_path 为 `chat-interface`，且 transcript 实际读取并确认了两者。
- PASS `checks_related_prd`: 明确指出 TRD related_prd 指向 `docs/pm/chat-interface/PRD.md`，而非目标 PRD 路径。
- PASS `blocks_implementation_plan`: 明确表示未创建计划、未修改代码；transcript 无写入命令，目标 IMPLEMENTATION_PLAN.md 不存在，workspace 文档哈希与 fixture 一致。
- PASS `hands_off_to_trd_gen`: 明确要求交回 `engineer-agent:trd-gen`，生成与目标 PRD 对齐的 TRD。

## With Skill Behavior

with_skill 四项断言均满足，且 exit_code 为 0、JSONL transcript 有效、workspace 未发生实现性变更。

## Without Skill Baseline

without_skill 仅作对照：识别了路径冲突，但未明确检查 related_prd，也未交回 engineer-agent:trd-gen。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-008-feature-path-mismatch-blocked

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`
- Test case: feature-path-mismatch-blocked
- Workspace: `workspace/eval-008-feature-path-mismatch-blocked`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/chat-interface/history-search/PRD.md`, and `docs/engineer/chat-interface/TRD.md`.
- Fixture summary: the PRD declares `feature_path: chat-interface/history-search`; the TRD declares parent `feature_path: chat-interface` and `related_prd: docs/pm/chat-interface/PRD.md`.
- Expected output: detect PRD/TRD metadata and related PRD mismatch, block implementation planning, and hand back to `engineer-agent:trd-gen`.

## Assertions

- PASS `detects_prd_trd_path_mismatch`: the skill requires matching PRD/TRD `feature_path`, `parent_feature`, and `feature_level`.
- PASS `checks_related_prd`: output conventions and planner require TRD `related_prd` to point to `docs/pm/{feature_path}/PRD.md`.
- PASS `blocks_implementation_plan`: mismatched TRD blocks `docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md`, code, and tests.
- PASS `hands_off_to_trd_gen`: stale, incomplete, path-mismatched, or conflicting TRDs return to `engineer-agent:trd-gen`.

## With Skill Behavior

Fresh with-skill validation confirmed that Batch 3's direct specialist gate is not diluted by a parent TRD. The current skill should compare the nested PRD with the supplied parent TRD, explicitly report `chat-interface/history-search` versus `chat-interface`, detect that `related_prd` points to `docs/pm/chat-interface/PRD.md` instead of the nested PRD, and stop before writing any plan. The correct handoff is to `engineer-agent:trd-gen` to create or correct the mirrored nested TRD.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic response could accept the parent Chat Interface TRD as close enough and proceed with a plan, or mention mismatch without validating `related_prd`. It would not reliably enforce the mirrored feature path and related-PRD gates before planning.

## Failures

- None.

## Next Steps

- Keep this eval focused on blocking parent/child feature path mismatches before implementation planning.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
