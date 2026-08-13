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
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `ee3671589f95fa8a892847eb388a153411b54b14444f1f7420faa0785c1aa02b`
- metadata_sha256: `b685d83a8e82816d2f4d521a041ae8452f619db60e5a55ebbccd97b0160d2ffb`
- fixture_sha256: `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6b0ff1b76e8b03f7712d3dcd168848aec48a65be2655318b04e40fdedd5925d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `561948022d6f471d6801c1e0d382cc70e538542dca320632f699ef9189b2a512`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marker_does_not_trigger_pm` | PASS | with_skill 明确将问题作为普通文件整理请求处理，仅说明无法访问 ~/Downloads 并提供常规整理命令；没有进入 PM 分类、生成 PM 文档链或进行 handoff。fixture 中的 AGENTS.md 与 marketplace marker 也未被用于触发 PM 流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=c69deba48d02b1d0781a99aeb358d0e0a6ac49d28db3ef2be435ecf461936838; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未触发 PM，正确识别为普通非研发文件整理请求；因环境限制未直接执行整理。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=eb84e4a698a9b8cc50c7063a9567a33fdf9ac6514466c947ef5954e97f90e5a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样未触发 PM，并因 ~/Downloads 不可用而请求提供可访问目录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
