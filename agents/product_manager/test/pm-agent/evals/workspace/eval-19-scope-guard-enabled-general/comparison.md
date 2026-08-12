# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-019-scope-guard-enabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5` from `agents/product_manager/test/pm-agent/evals/workspace/eval-19-scope-guard-enabled-general`.
- Identity schema: `2`
- target_skill_sha256: `f9ea1bade234ebfd780e1e4773d4808a60f7baa61920e5859daea2b146c1ce93`
- eval_definition_sha256: `2e41aaf2a9f1898027fcb4bd2dc0d8b314b161c3848369aeb0ccc8e3d7c16e07`
- metadata_sha256: `f5c5f2a20d2b5185fc2f9a51b4985187997e135f3a377de786395157cfcdb827`
- fixture_sha256: `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `78fbc30f6ea00642b27e4bc9a167610aaa84574a08fb26567e68734e28c9ff68`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84ad07662e525000bb3bbf1da6aa3f2d49322c424326b70644431a72cdb52c55`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enabled_marker_detected` | PASS | with_skill 的 runner_captured_trace 显示检查了 AGENTS.md 与 .claude-plugin/marketplace.json，并检测到 dev-agent-skills 标记。 |
| `general_request_proceeds` | PASS | with_skill 输出说明已完成分类，判断为不匹配 PM 类别或下游角色，停留在 PM 范围内且未执行文件移动；未输出未启用拦截提示。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=00c8046e8053007b44141cfe74aa3c64a044664b5e9f4540facc19f718ce54b4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到启用标记并完成分类；将请求留在 PM 范围内，未移动文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=9fb4cf10e9301327d1f3469cb12757103622429039a4e0b523952d2aac8953df; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未检查启用标记，直接因无法访问隔离环境中的 Downloads 而停止。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
