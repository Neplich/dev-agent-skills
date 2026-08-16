# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5` from `agents/qa/test/regression-suite/evals/workspace/eval-2-blocked-without-original-bug-context`.
- Identity schema: `2`
- target_skill_sha256: `5f00953469c57cd0a924598017d2502b6a836948c3bfa067998cf3e91f7335a1`
- eval_definition_sha256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- metadata_sha256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- fixture_sha256: `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2f3ed1bac6bd41e43ecbd585f5beb95db8464a7cf767e9c9a3ef20fae4f56429`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `07500a40de121399595841537e6aef1df4c976254ab123954a243d97bad454fb`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出缺少原始缺陷记录、失败证据、修复上下文、测试环境等，并未执行泛化回归。 |
| `blocked` | PASS | with_skill 将原始失败复测和修复行为标为 blocked，将相邻回归标为 not executed，将平台版本标为 blocked；同时说明 PRD/TRD 等对齐材料缺失，需补齐后才能回归。 |
| `assertion_3` | PASS | 输出包含原始失败复测、修复行为验证、相邻回归、发布建议和证据可信度五项结果。 |
| `assertion_4` | PASS | 发布建议明确为 needs more verification，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | 未产生未知目录或发布文件；明确列出恢复验证所需的版本、环境、原始 bug、修复证据及相关测试材料。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=7b51cdb46b65326af64abbb301f86f4f073559080e76c877c42ebf070a0371a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整识别证据缺口并阻止无依据的回归或发布结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=bff4262c8f6e9502fa15be7e772e97b29ba3f4d1b919769771dc307852c1f019; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别主要证据缺口并建议阻塞发布，但未提供同等细致的状态拆分和 PRD/TRD 对齐缺口。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充原始 bug、失败证据、修复提交或构建、测试环境与平台版本、验证命令及 PRD/TRD 对齐材料。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
