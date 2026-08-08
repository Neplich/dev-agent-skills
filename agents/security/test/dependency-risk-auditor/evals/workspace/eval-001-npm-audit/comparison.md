# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-001-npm-audit`.
- Fixture SHA-256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `b815bcadedc94647742113823ae910cacb0bd48d343e94eb3875bee2a6a39d68`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- Metadata SHA-256: `aee94fbc4f1b4c53f14bd2d88b010307b382e89dd9cc2398f8a45f7d41146704`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | with_skill identifies the Node.js/npm production dependency ecosystem and names both fixed direct dependencies: lodash@4.17.15 and minimist@0.0.8, including lockfile and transitive-dependency risk sources. |
| `risk_classification` | PASS | with_skill distinguishes prototype pollution, ReDoS, version-governance, and supply-chain/reproducibility risks, with Critical/High/Medium severity and P0/P1 priorities. |
| `evidence` | PASS | with_skill cites package names and exact versions from package.json, references CVE/GHSA advisories, explains the affected API/input conditions, and records the missing-lockfile/ENOLOCK limitation. |
| `upgrade_plan` | PASS | with_skill gives concrete targets (lodash 4.18.1 and minimist 1.2.8), lockfile/npm ci/audit/SBOM actions, regression checks, and actionable temporary mitigations; it does not modify dependencies. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=31373fde8f906a0b7db2c1ac3cafea4a8e52303dac9d0ecf8c55539b0eb0017e; snapshot_sha256=8eb958f872a9a0a64bf2ffac5b742ddf12c44b1dbc74fcc0747eaf294e62fe9f
- Behavior: Produced a structured, user-visible audit with package inventory, classified risks, cited evidence, upgrade targets, mitigations, and release-gate actions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=a0067e743b2f550571d00029168caf92a40e60e2db7229c7aa1264fb1e725812; snapshot_sha256=94e2e61ca65dd0a9b58d6f628c3cbdb577eef801969a18f2c2c899c7d43a8858
- Behavior: Produced a detailed dependency audit covering both packages, vulnerabilities, evidence, and remediation.
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-001-npm-audit`.
- Fixture SHA-256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2573dd217cef308cd88d80bd4db555dc7ac29ee2b87cd67e3ed8f4807140636`
- Skill overlay SHA-256: `ae39de43f00ac22182f0336b47936a0651b8b7cb847715311e719e485ae6d9ed`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- Metadata SHA-256: `aee94fbc4f1b4c53f14bd2d88b010307b382e89dd9cc2398f8a45f7d41146704`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With-skill output identifies the Node.js production dependency ecosystem, both fixed direct dependencies (lodash@4.17.15 and minimist@0.0.8), the relevant object-path/argument surfaces, and missing-lockfile supply-chain risk. |
| `risk_classification` | PASS | It distinguishes prototype pollution, template code injection, ReDoS, maintenance risk, and lockfile/ reproducibility risk, with Critical/High/Moderate severity and release-blocking priorities. |
| `evidence` | PASS | It cites package names and exact versions from package.json, names specific CVEs and advisories, provides severity scores, and records the ENOLOCK result and missing lockfile. |
| `upgrade_plan` | PASS | It recommends upgrading or removing minimist, upgrading lodash, generating a package-lock.json and using npm ci, plus concrete short-term input validation, allowlisting, isolation, timeout, and regression-test mitigations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=88a53996186290f9479409f3785a66643563df205b1d1779121d8dcf31779e00; snapshot_sha256=08ea3904097ab6f855f89787a6bcdd6e8b0f0e1a01d1a1345c17b91f4e4a2bbe
- Behavior: Produced a structured, feature-aligned audit with package inventory, severity classification, cited evidence, explicit uncertainty boundaries, upgrade sequencing, and mitigations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=131412e10760a9a656243cdf8df784faeba5ba283528819e916b16309d98c2ef; snapshot_sha256=4eba7ad660ba1092e6a74556abe8c8d95f68e3c8a667a6aed285f46f933a428a
- Behavior: Produced a detailed dependency audit covering both packages, vulnerabilities, evidence, priorities, lockfile risk, and remediation.
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-001-npm-audit`.
- Fixture SHA-256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9847519784146234ee8e6186ebd4f58b4e08cc25986e95e53a8cdbe8be3e0635`
- Skill overlay SHA-256: `b8089650410317e7cdca1594ef3aeb917b416730f8419e99172c09b88f6c8fc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- Metadata SHA-256: `aee94fbc4f1b4c53f14bd2d88b010307b382e89dd9cc2398f8a45f7d41146704`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With-skill output identifies the Node.js ecosystem, both production dependencies (`lodash@4.17.15` and `minimist@0.0.8`), their usage/exposure areas, and missing-lockfile supply-chain risk. |
| `risk_classification` | PASS | With-skill output distinguishes multiple CVEs, classifies them as Critical/High/Medium, and separately identifies lockfile/reproducibility and maintenance risks. |
| `evidence` | PASS | With-skill report cites concrete package versions, CVE identifiers, CVSS scores, affected-version ranges, fixture documents, and NVD/GitHub/npm references. |
| `upgrade_plan` | PASS | With-skill output provides upgrade targets for both dependencies, lockfile/npm ci and CI scanning actions, regression testing, input restrictions, and runtime mitigations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=733133beee49307c7982695f24a4c844cc45798a100610bedc32be10b3a9db1b; snapshot_sha256=1c8c55c6991dec5be4131a1b4b6fde38cadff02b2e3ddf6fdbf82722ba9d9331
- Behavior: Produced a structured, evidence-backed audit covering dependency inventory, vulnerability classification, supply-chain limitations, upgrade sequencing, testing, and mitigations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=0c81a00d91fb0c235cf114a8ace7c6c9db11abfe857c28c3c2ca397875eb445f; snapshot_sha256=91d6b21b93a550526105662d2bc8d4671772bf4d8496419a7680def4feee56e8
- Behavior: Produced a detailed dependency audit covering both packages, CVEs, evidence, severity, mitigations, and upgrade recommendations.
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

# Eval Result: eval-001-npm-audit

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`
- Test case: NPM Dependency Audit
- Workspace: `workspace/eval-001-npm-audit`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Audit the dependencies for security vulnerabilities.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-001-npm-audit/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `b6edbf42dbd9af42590304ec15b34e704e0eb43cb86c0ab81d6d6d9f3e023c6f`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 最终产物明确识别 Node.js 生态及 package.json 中的 lodash@4.17.15、minimist@0.0.8，并说明直接依赖、传递依赖和风险来源。 | PASS | Baseline 报告同样列出 Node.js 生产依赖、两个固定版本及锁文件缺失导致的传递依赖风险。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分 Critical/High/Medium 漏洞、过期或安全陈旧包，以及缺失锁文件、完整性和生命周期脚本等供应链/可复现性风险，并给出严重度。 | PASS | Baseline 报告分别分类漏洞、过期版本和供应链验证缺口，并标注严重度。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 package.json、PM_HANDOFF.md、PRD.md、具体包版本、CVE 编号、受影响范围及 npm audit ENOLOCK 结果。 | PASS | Baseline 报告引用依赖文件、固定版本、多个 CVE/GHSA、受影响范围和无锁文件证据。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出 minimist 升级到 1.2.8+、lodash 升级到 4.17.23+、生成并提交锁文件、复跑 npm audit、测试及临时输入校验/隔离缓解措施。 | PASS | Baseline 报告给出升级目标、锁文件、测试、CI/SBOM 和短期缓解建议。 |

## With-Skill Behavior

已在最终工作区创建结构化审计报告，覆盖 Node.js 依赖清单、漏洞严重度、证据、供应链缺口及升级/缓解建议。

## Fresh Without-Skill Baseline

Baseline 也创建了满足要求的审计报告，四项 assertion 均通过。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
