# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-002-session`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a` from `agents/security/test/authz-reviewer/evals/workspace/eval-002-session`.
- Fixture SHA-256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3e242b2dbb704cb1d29797b016c5227b3a75736fa3d4f0739192f0fdee71f01f`
- Skill overlay SHA-256: `3de2c418f3c14f33d91cbef534093000d696ba99512436f5551d86e45d872cc9`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- Metadata SHA-256: `f26166d912f73c7f118a1561bee3e62973123b274975fb4a17a869fba31f82a0`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | With-skill report identifies anonymous and authenticated-user roles, protected resources, session validity boundaries, and login, parsing, expiration, logout, and Cookie paths. |
| `access_control_findings` | PASS | With-skill report correctly identifies predictable/enumerable session IDs, missing 30-minute inactivity expiration, ineffective server-side logout revocation, and unverified secure-Cookie transport. |
| `evidence_and_impact` | PASS | Each finding includes file/line evidence, severity, and concrete impacts including session impersonation, prolonged unauthorized access, and credential leakage risk. |
| `remediation` | PASS | With-skill report provides actionable fixes and regression tests covering randomness, expiry boundaries, logout rejection, concurrency/idempotence, rotation, Cookie attributes, and endpoint integration. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=01c084989547b80982f0ce54a4b91ab6d850f9982d53a7eec0fd3813deda7b1f; snapshot_sha256=40d067eb7e4c23b263dce9d4780c9c971d127b739d7ce2296d4d8e21346bfc25
- Behavior: Produced a complete structured authorization review covering roles, resources, boundaries, lifecycle paths, findings, evidence, impacts, remediation, and regression validation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=7688f4f420598f77227b0f9d19059e22d74e70d614ad5accc2d2c7522b0d080b; snapshot_sha256=4785a5385c2ed8f39ec1db80a4ede322f10d674a9640156fabcfe8f714893638
- Behavior: Produced a substantively correct review with findings, evidence, impacts, remediation, and validation, but omitted an explicit role/resource/permission-boundary model in the shown output.
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
- Skill: `authz-reviewer`
- Eval: `eval-002-session`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a` from `agents/security/test/authz-reviewer/evals/workspace/eval-002-session`.
- Fixture SHA-256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0fb3bcf4b507247f482a2a4dba9d951bb407cd66a7a7b7801270374734e4b29d`
- Skill overlay SHA-256: `a5058c0e55b69c8360ce0ae93f04438f76cd73a75566cfde030e7cc6ed7b7266`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- Metadata SHA-256: `f26166d912f73c7f118a1561bee3e62973123b274975fb4a17a869fba31f82a0`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | The with_skill report identifies anonymous and authenticated-user roles, protected resources (user profiles/account settings), session creation/parsing/logout boundaries, and the login-to-session-to-protected-resource authorization path. |
| `access_control_findings` | PASS | It identifies predictable/enumerable session IDs, missing 30-minute inactivity expiry, and logout failing to revoke the server-side session, with precise source locations. |
| `evidence_and_impact` | PASS | Each finding includes code evidence, severity, affected resources, and concrete consequences including session impersonation, prolonged stolen-session use, and post-logout access. |
| `remediation` | PASS | The report provides executable fixes and regression checks for random IDs, expiry boundaries/activity refresh, server-side logout revocation, secure cookies, endpoint authorization, idempotency, and concurrency. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=4d984509a1b172e768c244acfe399a28596e7479214ae36004abb02bf2ff3ddb; snapshot_sha256=ec7b1c8b0dcf453fd2040ee02fe4da81cd42e7931ea7159148f89093635cc38d
- Behavior: Delivered a structured session security review with role/permission modeling, authorization flow, localized findings, impacts, remediation, regression tests, and explicit evidence gaps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=01f77a4a16c04540f32cd9235099d14039cb15bac73fc5112177369dc8342386; snapshot_sha256=5c2389a77e2ba1ffe617b722c7cd49edda9d00bfc1486b13600b4de73df6dbe9
- Behavior: Correctly found the three core session defects and gave evidence and basic remediation, but provided less structured authorization-path analysis and fewer detailed verification requirements.
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
- Skill: `authz-reviewer`
- Eval: `eval-002-session`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a` from `agents/security/test/authz-reviewer/evals/workspace/eval-002-session`.
- Fixture SHA-256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d2e4aec7daf8a1a3d4dd9129eb3c1a3dff6fda1cedda3583e17db51f3c77b01c`
- Skill overlay SHA-256: `93997287763bb5908bc9735f09115a4d8477c3badf934fbe6f43970bb3ecd156`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- Metadata SHA-256: `f26166d912f73c7f118a1561bee3e62973123b274975fb4a17a869fba31f82a0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | With-skill报告识别anonymous与authenticated-user角色、受保护资源、会话解析与退出权限边界，并明确指出登录、端点和中间件调用链缺失及无法验证。 |
| `access_control_findings` | PASS | 报告准确指出会话ID可预测、30分钟无活动过期缺失、退出不撤销服务端会话，并覆盖安全Cookie、登录轮换和受保护端点验证缺口。 |
| `evidence_and_impact` | PASS | 每个HIGH问题均提供了src/auth/session-store.js中的可定位行号证据，并说明枚举、会话劫持、长期有效和退出后继续访问等影响。 |
| `remediation` | PASS | 报告为随机高熵Token、过期判断与删除、服务端撤销、共享存储及安全Cookie集成提供可执行修复和回归验证建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=93581fe4b540317b82ce629ae3426f1ce1692c52df9708ad7303701539351c2c; snapshot_sha256=0dcaa6cbb4f3d4562261f361420955693d136e6b5ba4b20de3bd2e139f314765
- Behavior: 完整覆盖授权模型、会话缺陷、证据影响、修复验证和外围调用链缺口；与PRD及fixture代码一致。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=64a939ac89c90a9af94cedf0fd74d7d2cc9ebf0c7a9f6807ae39b4b53e558155; snapshot_sha256=74fb2a124b209a60c8fb08e053be0338a9294b9674d05eea1fddae91d95409a2
- Behavior: 识别了三个核心会话缺陷并提供了较完整的证据、影响、修复和验证建议，但未形成角色与权限矩阵。
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

# Eval Result: eval-002-session

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-002-session`
- Test case: Session Management
- Workspace: `workspace/eval-002-session`
- Natural user prompt:

> Check the session management security, using the confirmed PRD and code as evidence.

- Expected artifact: Structured authorization review that identifies access-control risks, affected roles or resources, evidence, severity, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/authz-reviewer--eval-002-session/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `63b039d9c786dd32ac2a298722e0ce7cb53b7adcb57752d6375b08aac458cf6b`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `authorization_model`<br>识别角色、资源、权限边界和关键授权路径 | PASS | 最终快照中的 authz-review.md 含角色/权限矩阵、资源边界及 login→createSession→getSession→logout 授权路径。 | PASS | baseline 报告同样包含角色矩阵、资源边界和会话授权流程图。 |
| `access_control_findings`<br>指出越权、会话、JWT 或权限检查缺陷 | PASS | 报告明确指出可预测会话 ID、无 30 分钟空闲过期、退出不撤销服务端会话，并说明无法验证的 Cookie/轮换/受保护路由控制。 | PASS | baseline 报告明确指出相同的会话、过期和退出失效缺陷，并标注集成控制的证据缺口。 |
| `evidence_and_impact`<br>说明证据、影响范围和风险后果 | PASS | 每项主要发现均给出 session-store.js 定位证据、违反 PRD 的对应关系、会话劫持/账户接管或持续访问影响。 | PASS | baseline 报告提供了代码位置、PRD 对照及影响范围和风险后果。 |
| `remediation`<br>提供可执行的授权修复和回归验证建议 | PASS | 最终报告给出 CSPRNG token、服务端空闲过期、撤销/删除、Cookie 与集成补证建议，并列出具体回归验证场景。 | PASS | baseline 报告同样提供了可执行修复和回归测试建议。 |

## With-Skill Behavior

With-skill 明确识别角色、资源、会话信任边界和授权路径；报告包含可定位证据、影响、严重度、修复及回归建议。

## Fresh Without-Skill Baseline

Without-skill 也完成了合格的会话审查报告，作为 baseline 各项 assertions 均满足。

## Failures

- 无。

## Not Exercised

- fixture 未提供登录处理器、Cookie 设置/解析、受保护端点或会话中间件，因此登录轮换、安全 Cookie 属性、匿名拒绝和端点级授权覆盖只能标记为不可验证，未形成可直接核验的实现分支。

## Next Steps

- 如需 FULL coverage，应补充登录、Cookie、会话解析和受保护端点实现后复审。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
