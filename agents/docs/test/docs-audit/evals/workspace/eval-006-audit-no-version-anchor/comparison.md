# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Fixture SHA-256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- Metadata SHA-256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | with_skill 明确返回 `blocked`，并拒绝在缺少维护者确认的 `target_release_version` 时继续；未返回 `ready_for_tag` 或 `release_verified`。 |
| `allows_read_only_diagnostic` | PASS | with_skill 未执行写入或成功的 pre-tag audit，并明确说明当前条件下不能开始审计；锁定证据显示工作树、索引和提交均未变化。 |
| `does_not_persist_report_without_target` | PASS | with_skill 明确表示不能生成报告；`delivery_snapshot` 为空，且 git 状态、差异和未跟踪文件均为空。 |
| `does_not_write_version_stamp` | PASS | with_skill 未从 ref、分支或文件名推断版本，且锁定证据显示无工作树或索引修改；原始 fixture 中页面仍为 `last_verified_version: unverified`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=71a424ad51399f0901800e9c60b1110f08d522cb494663c1d8c170f8b7c80039; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞在缺少维护者确认的目标版本，并保持只读、无报告、无版本盖章状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=4a9caa6f51f9ba5c38fc7b9b38d238592075abdc06100c88ceeded23c157935e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了变更诊断，但未阻塞缺少目标发布版本的审计，也未报告写入版本元数据。
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

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Fixture SHA-256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- Metadata SHA-256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | with_skill 明确返回“blocked”，并说明缺少维护者确认的 target_release_version，未返回 ready_for_tag 或 release_verified。 |
| `allows_read_only_diagnostic` | FAIL | with_skill 明确表示尚未执行变更影响分析或页面核验，未基于 e1f2a3b..7c9e2af 描述 affected page 与事实诊断。 |
| `does_not_persist_report_without_target` | PASS | with_skill 明确说明未写入报告；delivery_snapshot 为空，git evidence 显示无新增提交、无工作树变更。 |
| `does_not_write_version_stamp` | PASS | fixture 页面仍为 last_verified_version: unverified；with_skill 说明未执行版本 stamping，且证据中无 .meta/releases.json 修改。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=0b4a26d6e92894f6d667f4fc1ee18f71ccbd06d5931bd1c0e9bd36d460959985; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确因缺少维护者确认的目标版本而阻塞，并避免写报告或版本印章，但未提供允许的只读 affected-page 诊断。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=88df094ff91e341a5ef9a4fd725a12fd61dbd4df7d8efb227246696eef34e96a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了范围和只读事实诊断，但将结果表述为未发现缺陷，未阻塞缺少目标版本的 pre-tag 审计。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未执行或提供基于确认范围的只读 affected-page 与事实诊断。
- Next: 在保持 blocked 状态、不写报告和不盖版本章的前提下，补充范围内 affected page 及事实变更诊断。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Fixture SHA-256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- Metadata SHA-256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | with_skill 明确指出 target_release_version 缺失，并将审计标记为 blocked。 |
| `allows_read_only_diagnostic` | PASS | with_skill 未声称 ready_for_tag 或 release_verified，仅报告已确认的 base_ref、target_ref 和缺失版本信息；git_evidence 显示无变更。 |
| `does_not_persist_report_without_target` | PASS | with_skill 明确未执行文档审计或写入报告；delivery_snapshot 和 declared_outputs 均为空，git_evidence 无新增或差异。 |
| `does_not_write_version_stamp` | PASS | 原始文档证据显示 last_verified_version: unverified；with_skill 未写入文件，且 git_evidence 显示工作树、索引和引用均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=5128cf6f73099a797871fcda63d792e5d22eff704194607f9a628d509d65ba5b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别缺少维护者确认的 target_release_version，并阻塞审计、避免写入报告或版本印章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=b09c8c81650c9b95f504638fd2fedc5e94255ebf867bc37277fd3056adef9ad4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了范围诊断和风险说明，但未因缺少 target_release_version 而明确阻塞。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_without_target_release_version` | PASS | FAIL | with_skill 的 `result.txt` 明确为“审计结果：blocked”，并指出缺少维护者确认的 `target_release_version`；without_skill 返回“结论：未发现需要更新文档的变更”，未将阶段结果标记为 `blocked`。 |
| `allows_read_only_diagnostic` | PASS | PASS | with_skill 未执行写入或成功审计，仅报告缺少 Git 元数据；without_skill 仅依据 `.eval/actual-diff.patch`、`change-map.yaml` 和代码文件做影响诊断，未声称 `ready_for_tag` 或 `release_verified`。 |
| `does_not_persist_report_without_target` | PASS | PASS | 两个工作区均不存在 `docs/site/.meta` 目录，也不存在 `audit-7c9e2af.md` 或其他版本化审计报告。 |
| `does_not_write_version_stamp` | PASS | PASS | 两个工作区的 `docs/site/api/catalog.md` 均保持 `last_verified_version: unverified`；均不存在 `.meta/releases.json`，也未写入版本号。 |

未满足断言（with/without 任一 FAIL）：``blocks_without_target_release_version``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | 明确因目标版本缺失且未确认而 `blocked`，未返回任一成功阶段状态。 |
| `allows_read_only_diagnostic` | PASS | 仍用已确认 base/target 描述 affected page，并确认纯重构下页面事实 `verified`，但不包装为成功审计。 |
| `does_not_persist_report_without_target` | PASS | workspace 零写入；不存在 `audit-7c9e2af.md` 或其他版本化报告，没有 SHA 回退命名。 |
| `does_not_write_version_stamp` | PASS | 页面保持 `last_verified_version: unverified`，未创建或修改 `.meta/releases.json`，未推测版本。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a75-30f2-72d0-bea2-6fd9fe5ff45d`，位于 `tmp/eval-runs/117/eval-006-audit-no-version-anchor/with_skill/`。
- 候选正确应用入口 gate 与只读诊断例外，完全修正旧模型的 SHA 报告回退语义。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a78-ed4d-77e1-a925-8cac1dcb9995`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 也保持零写入且拒绝推测版本，但没有 docs-audit 的入口、报告持久化禁止与阶段状态结构。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch` 仅作只读诊断，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；无目标版本 gate 或报告持久化规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
