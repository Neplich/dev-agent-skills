# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-002-abandoned`.
- Fixture SHA-256: `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f`
- Prompt SHA-256: `89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9847519784146234ee8e6186ebd4f58b4e08cc25986e95e53a8cdbe8be3e0635`
- Skill overlay SHA-256: `b8089650410317e7cdca1594ef3aeb917b416730f8419e99172c09b88f6c8fc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `88dd9b929d53963534f872d5c6b43117be6b35cb41fa6b99bd7d05175018ade8`
- Metadata SHA-256: `6e01d4daa6b468e7c7a0ddfd1d17ad1116a727bf8d6709ea8ad0e5baec7fce48`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With-skill output identifies request@2.88.2 and node-uuid@1.4.8, their deprecated/unmaintained ecosystems, network and UUID assets, and associated maintenance and compatibility risks. |
| `risk_classification` | PASS | It distinguishes deprecation/maintenance risk from unconfirmed direct vulnerabilities, assigns high priority to request and medium priority to node-uuid, and explains the relevant exposure and limitations. |
| `evidence` | PASS | It cites package names and exact versions from package.json, npm and upstream maintenance evidence, Node.js documentation, and explicitly notes the absence of lockfiles and source code. |
| `upgrade_plan` | PASS | It recommends fetch or undici for request, crypto.randomUUID or uuid for node-uuid, provides migration validation areas and priorities, and preserves the requirement not to modify dependencies. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=e5ccbe3b8aa5dff278a9d65ed96ebfaa1b64ead3a39fe7c49c6c0fa6bf5505f0; snapshot_sha256=96e21e7f37175059a6fb3a0ec5c4ed7d47ddd8709434247ac59e50cbd671bc17
- Behavior: Produced a complete, scoped dependency risk audit with stronger explicit distinctions between confirmed and unconfirmed risks, audit limitations, priorities, migration validation, and platform mitigations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=8a90167a1f444d8737afd437327e66d2c3868e5703cc989d1800fdff2d2496c7; snapshot_sha256=7b452011080938ffcd23c4c7e057a8a0164d0d9e751c5a8a69c86229fce8127e
- Behavior: Produced a complete dependency audit with package/version evidence, risk discussion, replacement guidance, and interim controls.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-002-abandoned

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`
- Test case: Abandoned Packages
- Workspace: `workspace/eval-002-abandoned`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Check for abandoned or outdated dependencies.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-002-abandoned/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `78690f73cc6febd2097ea7892857fa979d64f69bbf14c879133bbbd07d659103`。
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
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 最终快照中的 docs/security/dependency-inventory/dependency-audit.md 明确识别 package.json 中的 2 个生产依赖：request@2.88.2 与 node-uuid@1.4.8，并说明无 lockfile。 | PASS | AUDIT.md 明确盘点同样的两个直接生产依赖及缺失 lockfile。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分并分级了废弃/维护风险、供应链与传递依赖限制，并明确“Confirmed vulnerabilities: 0”及无法确认 exploitability；request 为 High，node-uuid 为 Medium。 | PASS | AUDIT.md 区分 abandoned/deprecated、public security report、direct vulnerability 未确立及 transitive 风险未评估，并给出 P0/P1 优先级。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 package.json 中的具体包名和版本，并提供 npm/GitHub 维护状态证据；transitive 结论有 ENOLOCK 和无 runtime/tree 的明确依据。 | PASS | AUDIT.md 引用 package.json:6/7、具体版本、npm 页面及上游 SSRF 报告。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出按 P0/P1/P2 排序的替换计划：request 迁移至 fetch/undici，node-uuid 迁移至 crypto.randomUUID()/uuid，并包含测试、SSRF 控制、lockfile 和发布门禁建议。 | PASS | AUDIT.md 给出 request 和 node-uuid 的替换、隔离、测试及 lockfile/audit 后续计划。 |

## With-Skill Behavior

with-skill 正确读取 handoff/PRD，盘点 2 个直接依赖，创建了符合要求的 dependency-audit.md；明确记录 npm audit 的 ENOLOCK 限制，并分类废弃、供应链/传递依赖风险及严重度。

## Fresh Without-Skill Baseline

without-skill 也创建了 AUDIT.md，覆盖同一依赖盘点、风险证据与替换建议；作为 baseline，各 assertion 均满足。

## Failures

- 无。

## Not Exercised

- 没有 lockfile 或 node_modules，因此具体传递依赖、树深度和可验证 CVE 修复版本路径未被客观触发；报告已诚实标注 ENOLOCK 限制。
- 未触发需要实际确认具体漏洞的分支；当前 fixture 的主要触发条件是废弃/过时依赖。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
