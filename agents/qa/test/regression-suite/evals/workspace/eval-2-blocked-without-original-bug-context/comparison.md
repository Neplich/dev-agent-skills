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
- Fixture SHA-256: `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5`
- Prompt SHA-256: `261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8289acf8e27bfd57efcbcc6d726b9bfaa4df0b2cb5c60400d61eca4c6f8c65d4`
- Skill overlay SHA-256: `a284e7eb3465da68b2d3792a2435d75549c3a3732ed503ef22754fbfde0a19d1`
- Judge schema SHA-256: `2f3ed1bac6bd41e43ecbd585f5beb95db8464a7cf767e9c9a3ef20fae4f56429`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出缺少缺陷记录、失败证据、修复上下文和测试环境，未执行泛化回归。 |
| `blocked` | PASS | with_skill 将原失败复核、修复行为、相邻风险、平台版本及 PRD/TRD 对齐标为 blocked/not executed 或明确说明因材料缺失无法完成。 |
| `assertion_3` | PASS | 输出包含所有要求的结构化字段。 |
| `assertion_4` | PASS | release_recommendation 为 needs more verification。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 目录或误作全量 E2E 结论，并列出了恢复验证所需证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=b5280e093b9c3cddccdfca013e94ebd51d08d2ba4014a39d6b96bff014d2ebe2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并阻止回归结论，提供结构化阻塞状态和补证清单。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=238c801175574f239fa123629263641549d1d67f24a70bfd9196ac175f349597; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并给出补充证据清单，但未提供要求的结构化回归字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充原始缺陷、失败证据、修复 PR/commit、构建版本、QA 环境和平台版本后再执行回归。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
