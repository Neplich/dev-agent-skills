# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-006-site-less-degraded-gate`.
- Fixture SHA-256: `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20`
- Prompt SHA-256: `3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- Metadata SHA-256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | with_skill 场景 A 明确记录正式文档站、docs/site 与站内 Release Notes 能力链均不存在，并允许生成完整 Release 预览。 |
| `records_downgrade_basis` | PASS | with_skill 明确记录无正式文档站及能力链作为降级依据，并列出已确认的 changelog 与 version-bump 证据。 |
| `still_requires_maintainer_approval` | PASS | with_skill 明确为 preview-only、无维护者写入批准，禁止 draft/publish、tag 创建或移动，并要求每次写入前获得维护者显式且当前的批准。 |
| `blocks_without_confirmed_fact_source` | PASS | with_skill 场景 B 明确判定 blocked，指出 proposed bump、缺失 changelog 和确认事实源，且拒绝将 commit subjects 或未确认摘要作为发布事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=2f06e1bb96fcc95aa45a4bfce541b989cee9058c9c206c0bdaff80ac876d8165; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整呈现 site-less 降级依据、确认事实源、版本窗口和 Release 预览；保持无写入，并正确阻塞无确认事实源的场景 B。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=0c6615bbdb1b46f90d079285825e651152351272eca8f3c2c2234d37d5dcf90f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确处理两种场景：场景 A 生成预览并保持只读，场景 B 因无确认事实源阻塞；未显式展开宿主名称和部分运行时核验细节。
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
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-006-site-less-degraded-gate`.
- Fixture SHA-256: `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20`
- Prompt SHA-256: `3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `793cabc84dc1947c3d6386a1d060276eea2eb8b4e9de25fdd6c7b7a60fb82cb0`
- Skill overlay SHA-256: `ecc021af86f838c5c915ade1c1e1095fa203f789350af9aa701ad32bae876bb2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- Metadata SHA-256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | with_skill 明确记录无正式文档站、无站内 Release Notes 能力链，且因缺少 handoff 不阻塞；场景 A 生成了完整 Release 预览。 |
| `records_downgrade_basis` | PASS | with_skill 记录了文档站未初始化、docs/site 与能力链缺失，并列出已确认的 changelog 与无冲突的 version-bump 证据。 |
| `still_requires_maintainer_approval` | PASS | with_skill 明确仅保留预览，未创建或更新 Draft、发布 Release、创建或修改 Tag、修改文件；并说明写入前需要维护者显式且当前批准。 |
| `blocks_without_confirmed_fact_source` | PASS | with_skill 将场景 B 明确判为阻塞，并拒绝把 proposed 版本 bump、未确认摘要或 commit subjects 当作发布事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=ea90cd69e1485bc4680c0dab31fe003427124b1a64ec94459c23db2d8fd846d7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整记录降级依据、事实源和版本证据，生成场景 A 预览并阻塞场景 B，且保持无写入与维护者批准门禁。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=7d4426e518e60b2116123650c20b163fb909543990f7cd62ba7f50c354a709c3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确处理两种场景：场景 A 生成预览，场景 B 阻塞；但内容较简略。
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
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-006-site-less-degraded-gate`.
- Fixture SHA-256: `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20`
- Prompt SHA-256: `3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- Metadata SHA-256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | With-skill output confirms no formal documentation site, says the downgrade basis is valid, and provides a complete v1.4.0 Release preview without blocking on absent handoffs. |
| `records_downgrade_basis` | PASS | With-skill output records the site-less downgrade basis, identifies the confirmed changelog and version-bump evidence, and states the relevant handoff condition. |
| `still_requires_maintainer_approval` | PASS | With-skill output limits the result to preview, forbids tag/draft/publish writes, and states that every draft or publish write requires explicit current maintainer approval. |
| `blocks_without_confirmed_fact_source` | PASS | With-skill output marks Scenario B blocked, notes the proposed bump and absent confirmed source, and rejects commits or an unconfirmed summary as release facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=7bbee37bdf3ec3b2b06e42746ff9a2031cd09abd201d5601d4d6311cbb9d2364; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly handled both scenarios: complete preview with explicit write restrictions for the confirmed source, and blocking without a confirmed fact source.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=4133f83ba1d62ec23beb40304e822d2189e7c1ddf315dc3911121fd06ff2876c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete preview for the confirmed-source scenario and blocked the unconfirmed-source scenario; performed no writes.
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

# Eval Result: eval-006-site-less-degraded-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`
- Test case: `无文档站宿主降级双态审计门禁`
- Prompt:

> 请读取 `release-package.md`、`docs/changelog/changelog-v1.4.0.md`、`evidence/version-bump.md` 与 `scenarios/no-confirmed-fact-source.md`，处理其中两种 GitHub Release 场景。

- Expected output:

> 可信事实源场景因宿主无 docs/site 且无 release-notes-gen 站内 Release Notes 能力链，将 release-notes-gen / docs-audit 双态审计 handoff 门禁判为不适用并生成完整 preview，显式记录降级依据、已确认 changelog 与版本 bump 证据；预览交维护者批准且不执行任何写入。无可信版本事实源场景保持 blocked，不臆造版本事实。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `cf75cbbf67a65894298fe934a83d0c3f2f3701462abb01c13f26fe10b3f8ba45`（4 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1、item_3 读取技能及其 references），按场景生成预览或阻塞，且未产生写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1、item_3 读取技能及其 references），按场景生成预览或阻塞，且未产生写入。

## Without-Skill Baseline

without_skill 未加载目标 skill（skill_load_hits=0），但作为对照同样处理了两个场景；其标题为裸 v1.4.0 且预览结构较不完整。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | **PASS** | with_skill/candidate.md 场景 A 明确说明 docs/site、站内 Release Notes 能力链及 handoff 缺失，但仍生成了 v1.4.0 的完整标题、正文、compare 链接和预览决策；transcript item_4 记录当前模式为仅 Preview。 | without_skill 也生成预览，但标题仅为 v1.4.0，且正文较简略。 |
| `records_downgrade_basis` | **PASS** | candidate 明确记录文档站未初始化、docs/site/ 与站内 Release Notes 能力链缺失，并说明双态审计 handoff 的降级适用性；同时列出 docs/changelog/changelog-v1.4.0.md 和 evidence/version-bump.md。fixture-manifest.json 与快照确认这些证据文件存在且未被修改。 | without_skill 记录了无正式文档站及相关 handoff，并引用确认 changelog，但降级依据表述较简略。 |
| `still_requires_maintainer_approval` | **PASS** | candidate 顶部明确未执行任何 GitHub 写入、创建或移动 tag；场景 A 标注仅 Preview、无维护者写入批准，并明确 Draft/Publish 前须分别取得当前、明确的维护者批准。before-snapshot.json 与 after-snapshot.json 完全一致，transcript 无写入命令。 | without_skill 也明确未执行 Tag、Draft 或 Publish 写入，但未达到 with_skill 的详细审批与后续复核表述。 |
| `blocks_without_confirmed_fact_source` | **PASS** | candidate 场景 B 明确 blocked：版本化 changelog 不存在、version_bump_status 为 proposed、无维护者确认事实源，并声明 commit subjects 与未确认摘要不能作为 Release 事实；未生成可提交 Preview 或执行 Draft/Publish。 | without_skill 同样将场景 B 标记 blocked，并拒绝使用未确认材料。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `98.93s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `80.206s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `85.912s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
