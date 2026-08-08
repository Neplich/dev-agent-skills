# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c` from `agents/product_manager/test/github-reader/evals/workspace/eval-003-milestone-focused`.
- Fixture SHA-256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `cbc27cddf5543ee4c60ccd8f54bf10c1ec8b7799d5c9eb603008973679be6d9f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- Metadata SHA-256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `a6701d093076bc07d26c7e813151915b2b1a25f501428e58ba88c24bfe3d6c6e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出 Documentation refresh 进度最慢（50%），并指出 React 20 RC 已逾期。 |
| `assertion_2` | PASS | with_skill 为每个 milestone 提供了 open/closed 数量对应的完成率：28/40、16/20、5/10。 |
| `assertion_3` | PASS | with_skill 使用一致且可读的状态标识区分已逾期、顺利和无截止日期，并在结论中标明最慢项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=fe3239cf3e3c47f1fb4141760161b8f414f8d12efd11eeeb4107efd9cd76b623; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确提供快照时点、所有 milestone 的完成率、状态标签，以及最慢和逾期结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=343a7c1dcf381e2967b4f694a931218cfa2e8d0ee104c7acc9d0344987640845; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 已正确识别最慢和逾期 milestone，并提供完成率与数据时点，但未以表格或明确状态标签完整呈现所有状态。
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

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c` from `agents/product_manager/test/github-reader/evals/workspace/eval-003-milestone-focused`.
- Fixture SHA-256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `cbc27cddf5543ee4c60ccd8f54bf10c1ec8b7799d5c9eb603008973679be6d9f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- Metadata SHA-256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | with_skill 明确称 React 20 RC“最慢且已逾期”，但快照显示 Documentation refresh 完成率最低（5/10，50%）；React 20 RC 仅是逾期。 |
| `assertion_2` | FAIL | with_skill 给 Documentation refresh 标注“5/10（100%）”，与快照中的 5 closed、5 open（50% 完成）矛盾。 |
| `assertion_3` | FAIL | 状态标记将仍有 5 个 open issue 的 Documentation refresh 标为“完成”，且未准确区分实际最慢项，导致状态标签与原始证据不一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=1714e9280dcf097cf468679109d87c36c8420a0266495c1188107aff84529317; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供表格、数据时点和状态标记，但错误识别最慢 milestone，并将 Documentation refresh 的 50% 完成率写成 100% 且标为完成。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=4b4082384c2b5826180a11e04241fbad897e1d0ef226e06eca9ce13e733c8f21; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 React 20 RC 逾期，但错误地将其称为最慢；各项完成率与快照一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane 的最慢项判断错误。
- with_skill lane 的 Documentation refresh 完成率和状态错误。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c` from `agents/product_manager/test/github-reader/evals/workspace/eval-003-milestone-focused`.
- Fixture SHA-256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6e29f2b22f72bb9078ec886f3bf0d4599e102bac697619f52f799318f68df6c7`
- Skill overlay SHA-256: `08b4455eaa3f2baaf8b11c20e163fe95beeff153e05846e54d69f650a80acb16`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `03ca7dcd2d32073ad565b1b3c0ee72dd9b7d1e36194c962f2103c8ce3de68286`
- Metadata SHA-256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出 React 20 RC 已逾期，并指出 Documentation refresh 完成比例最慢。 |
| `assertion_2` | PASS | with_skill 为三个 milestone 均提供了具体完成比例：React 20 RC 70%、Documentation refresh 50%、Compiler follow-ups 80%。 |
| `assertion_3` | FAIL | with_skill 输出未使用 ✅、🟢、🟡、🔴 或 ⚪ 状态标识。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=9fd9e03c1c44b7235b737fb3382d6686357d64d7576aa4de818422a1b8eda46c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确识别逾期和最慢 milestone，覆盖全部 milestone 的完成率；未提供 emoji 状态标识。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=2bdef6f943ef8bcf7c805c2a911d353f9f6046920eb9b5321b7764fac71ee7ad; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确识别逾期和最慢 milestone，并提供完成率，但未使用要求的 emoji 状态标识。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_3 未满足：缺少指定 emoji 状态标识。
- Next: 为输出中的 milestone 添加 ✅、🟢、🟡、🔴 或 ⚪ 状态标识。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/github-reader/evals/workspace/eval-003-milestone-focused`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6eb8c3566bc8fc8a913d019e9e94735b16afef5c8f221d3b6f296749ac983217`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `254cc92cf58649aa2c5bb2447fe35aa135bdc944368afe7a7cc119c6e2735ba1`
- Skill overlay SHA-256: `86a7dea13dce1a60e9d0c4442e983c46d3a33318b7a112994f13359d56bd6e12`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5e2443beaea952c5c356e364bc1e6a90acf66dc1bc63bb3b9b5081c1e4c95035`
- Metadata SHA-256: `19102bf9e9cafdc1b97f6dab18d074a52dce71f0fd285b0ab6636008876611e3`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出 19.0.0 是当前进度最慢的 milestone，并说明无截止日期、无法确认逾期。 |
| `assertion_2` | PASS | with_skill 提供 19.0.0 的具体数据：6/11 个 issue 已关闭、5 个 open issue、完成度 54%。 |
| `assertion_3` | FAIL | with_skill 未使用 ✅、🟢、🟡、🔴 或 ⚪ 状态 emoji。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6eb8c3566bc8fc8a913d019e9e94735b16afef5c8f221d3b6f296749ac983217; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c1c30dd0a8431429260613d7296a17a068dac2ccd506e110c14035d893407456; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确指出 19.0.0 最慢且不可确认逾期，提供完成率和 issue 数量，但未提供要求的状态 emoji。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6eb8c3566bc8fc8a913d019e9e94735b16afef5c8f221d3b6f296749ac983217; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f645e1013686742d3527ba673de646ce805d2dbf9566777c4fd8255e85b14d23; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确指出 19.0.0 最慢，并提供 6/11、54% 等完成率数据；同样未使用状态 emoji。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_3 未满足：缺少指定的 emoji 状态标识。
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

# Eval Result: eval-003-milestone-focused

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`
- Test case: `milestone-focused`
- Prompt:

> 看一下 facebook/react 最近的 milestone，哪个进度最慢或者已经逾期了？

- Expected output:

> Milestone 状态报告，识别出进度最慢或逾期的 milestone，给出具体数据支撑

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- Overall result: FAIL
- With-skill summary: with_skill 实际加载了 github-reader（skill_load_hits=2），按顺序读取技能后尝试查询仓库和 milestone，但 GitHub CLI 未认证且网络请求失败，最终如实报告无法判断；输出未使用状态 emoji。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 github-reader（skill_load_hits=2），按顺序读取技能后尝试查询仓库和 milestone，但 GitHub CLI 未认证且网络请求失败，最终如实报告无法判断；输出未使用状态 emoji。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），通过网页搜索输出了 19.0.0、54%（6/11）等结论，并同样未使用状态 emoji。仅作对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `assertion_1` | **NOT EXERCISED** | with_skill transcript 中 gh repo view 与 milestones 查询因未登录失败，随后 curl 因无法解析 api.github.com 失败；candidate 明确写明“目前无法可靠判断”，因此实时 milestone 实体不可用，不能判定该断言。 | without_skill 明确指出 19.0.0 是进度最慢/停滞目标，但该对照行为不改变 with_skill 结论。 |
| `assertion_2` | **NOT EXERCISED** | 所需实时 milestone 数据不可用；with_skill candidate 没有提供 open/closed 数量或完成率，而是如实说明无法获取数据，因此该实时数据断言不能判 PASS 或 FAIL。 | without_skill 输出 54%（6/11）和 5 个 open issue。 |
| `assertion_3` | **FAIL** | with_skill candidate 只说明 CLI 未登录和无法判断，没有使用要求的 ✅、🟢、🟡、🔴、⚪ 任一状态 emoji；技能加载成功且不是基础设施缺口。 | without_skill candidate 同样没有使用要求的状态 emoji。 |

## Failures

- assertion_3 未满足：最终输出缺少要求的 emoji 状态标识。

## Not Exercised

- assertion_1：GitHub CLI 未认证、API 网络不可用，无法获得实时 milestone 集合。
- assertion_2：GitHub CLI 未认证、API 网络不可用，无法获得实时完成率数据。

## Next Steps

- 认证 GitHub CLI 或提供可用的实时 GitHub 数据后，重新评估 milestone 识别和完成率断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `62.459s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `57.834s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `76.421s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
