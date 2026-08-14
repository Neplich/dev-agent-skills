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
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `ee3671589f95fa8a892847eb388a153411b54b14444f1f7420faa0785c1aa02b`
- metadata_sha256: `b685d83a8e82816d2f4d521a041ae8452f619db60e5a55ebbccd97b0160d2ffb`
- fixture_sha256: `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6b0ff1b76e8b03f7712d3dcd168848aec48a65be2655318b04e40fdedd5925d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6ef9504e39a31fcbe8fbf27603399dd657878f1891b55f001c87ffcd613b4b43`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marker_does_not_trigger_pm` | PASS | with_skill 的锁定输出仅说明 ~/Downloads 不存在并请求提供可访问目录；runner_captured_trace 仅显示检查目录的命令及普通整理说明，未出现 PM 分类、PM 文档链或 handoff，也没有交付文件或 git 变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=08f7cae87bd3e8232162bed76bdfc3b07152cd2dad8ca2f549514c41b18254dc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在检测到 ~/Downloads 不可访问后停止并请求用户提供目录；未被 marker 触发进入 PM 流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=e207a5b5711050e1b337ab28f232de1c50f78500f7d2a04ff0a679575df7c55d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样因 ~/Downloads 不存在而停止；未进入 PM 流程，作为新鲜基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
