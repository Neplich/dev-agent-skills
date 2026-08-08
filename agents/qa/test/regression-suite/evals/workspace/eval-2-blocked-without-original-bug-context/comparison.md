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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `5963f60ead81ffc5fd7b8778d6215ec69825a76246473fc9777aee19c6576e9c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill 明确指出缺少缺陷记录、失败证据、变更记录、测试命令、构建标识和 QA 环境，并声明未执行测试。 |
| `blocked` | PASS | With_skill 将原始失败复核、修复行为验证、邻近回归检查标记为 blocked，将平台版本标记为缺失/未执行，并将 PRD、TRD 对齐标记为阻塞。 |
| `assertion_3` | PASS | With_skill 输出包含 original failure recheck、fixed behavior、adjacent regression checks、发布建议和 evidence_confidence。 |
| `assertion_4` | PASS | 发布建议为 blocked / needs more verification，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | With_skill 未使用 unknown 目录或给出全量 E2E 结论，并列出了所需的平台版本、QA 环境、原始缺陷和修复证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=4c9af0f81706fe6b37916866ad1a20bc4a792e99b2ced0dfc7e3a93583bac69c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确阻塞回归，结构化列出各验证门禁状态、证据置信度、发布边界及补充材料要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=f79923114a3875da63b778d864af36ba207fa7e6e267f26281117113df5132d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并列出缺失的缺陷、复现、修复、环境和验证证据，但未提供结构化门禁状态。
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
- Skill overlay SHA-256: `5963f60ead81ffc5fd7b8778d6215ec69825a76246473fc9777aee19c6576e9c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill output explicitly states the handoff lacks the original defect record, reproduction steps, failure evidence, and repair/test context, so regression cannot be performed. |
| `blocked` | PASS | With-skill output marks original failure recheck, fixed behavior verification, adjacent regression checks, and platform-version checking as blocked or not executed; PRD/TRD alignment is also marked blocked. |
| `assertion_3` | PASS | With-skill output includes original failure recheck, fixed behavior, adjacent regression checks, release recommendation, and evidence confidence. |
| `assertion_4` | PASS | Release recommendation is explicitly `needs more verification`, and the output says release cannot be recommended. |
| `no_unknown_or_unscoped_release` | PASS | With-skill output does not use an unknown directory or claim release-wide E2E coverage; it lists the required platform/version, environment, original defect, repair evidence, build, and validation materials. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=cec6baffc6790bc362ae808205ad122e109a115a40d46d5799f6cab396f1d1ba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks unsupported regression conclusions, provides the required structured statuses and confidence, and recommends further verification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=a73386f9a6adcaa2c153b818e2a40b628073e0686947516e24dc5ef9792698d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies insufficient evidence and lists missing materials, but does not provide the required structured regression-status fields.
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
- Target skill tree SHA-256: `f0c319a012387c7575d20d8895608b789ad01d7d5779f862d77b1253767b14fb`
- Skill overlay SHA-256: `b96ed92ce0423bb8527c13b8849f250fdaaadae3fbca0ab6a14820e55a642b24`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出缺少原始缺陷记录、失败截图/日志、修复内容或提交、测试环境及平台版本等证据，并未直接执行泛化回归。 |
| `blocked` | FAIL | with_skill 将原始失败复测、修复行为验证和相邻回归检查标为 blocked/not executed，但未明确将平台版本确认标为 blocked 或 not executed；PRD/TRD 仅表述为无法确认。 |
| `assertion_3` | FAIL | with_skill 包含三项回归状态和 evidence_confidence，但没有明确的 release recommendation 项或等价的结构化发布建议字段。 |
| `assertion_4` | PASS | with_skill 的结论明确为 BLOCKED，并说明不能判定 PASS 或 FAIL，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | with_skill 未使用 unknown 目录，也未将局部回归当作 release 全量 E2E 结论，并列出了所需的版本、环境、原始缺陷和修复证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=7c02aeaa4993fd94b401d6cfcf46033c350d9e7306ac7f016403722f73b665a3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别证据缺口，阻断回归并列出所需补充材料；但遗漏明确的平台版本状态和 release recommendation 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=ec1defc7a5c0522625b422dc5f98ae6cbbffd004c446597a2b23394f45e05adf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并列出补充项，但未提供结构化 blocked/not executed 状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未将平台版本确认明确标记为 blocked 或 not executed。
- with_skill 未包含明确的 release recommendation 结构化项。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `5b6d7cb9ff5171a983a8d8515599a4773ee6ffaa61ca2bb620f01078152d2f6a`
- Skill overlay SHA-256: `896f0e17d232feae7886d36d9b4a521d02c2ea0c4d33bfdb8e88073f3448a22f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出原始缺陷、失败复现证据、修复提交/构建信息、测试命令和 QA 环境均缺失，并判定材料不足以执行回归。 |
| `blocked` | PASS | with_skill 将整体状态标为 BLOCKED，并明确原始失败复测、固定行为验证、相邻回归和发布建议为 blocked/not executed；同时指出平台版本及 PRD/TRD 均缺失，未将其判为通过。 |
| `assertion_3` | FAIL | with_skill 涵盖了原始失败复测、固定行为、相邻回归和发布建议，但未提供明确的 evidence confidence/证据置信度输出项或等价结论。 |
| `assertion_4` | PASS | with_skill 明确表示不能推荐发布，整体结论为 BLOCKED，符合 blocked 或 needs more verification 边界。 |
| `no_unknown_or_unscoped_release` | PASS | with_skill 未使用 unknown 目录或作全量 E2E 结论，并列出了恢复验证所需的平台/版本、环境、原始 bug、修复及构建证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=4fb8ba347db282e866a9ffae6650426f6dccb915ff0d8a7ad92812615932ef11; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别证据缺失，阻断回归和发布建议，列出补齐材料及 PRD/TRD 对齐要求；缺少明确 evidence confidence 输出。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=e7618c051f6a054c721753e2f9b683d72478c171934bce556340ae1d6b8b911c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并列出缺失的缺陷、复现、修复、环境和测试证据，但未给出结构化的 blocked 门禁状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未包含明确的 evidence confidence/证据置信度结果，未满足 assertion_3。
- Next: 补充 evidence confidence 字段或明确的证据置信度结论。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `93e5fd0d6baa599b41823d84d9e76df4ae1d287d1ee0dc585a0fbe0d3c54e8d5`
- Skill overlay SHA-256: `9883d5bccab96c99ea3ecc04b59f35a7f6a047a4260200cdf425c896a87f0f3e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出缺少原始缺陷、复现/失败证据、修复上下文、测试环境等，并说明未执行复测。 |
| `blocked` | FAIL | 明确将原始失败复查、修复行为验证和相邻回归检查标为 blocked/not executed，但未明确将平台版本确认标为 blocked 或 not executed；PRD/TRD 仅称缺失。 |
| `assertion_3` | PASS | 语义上包含原始失败复查、修复行为验证、相邻回归检查、发布建议和低证据置信度。 |
| `assertion_4` | PASS | 发布建议明确为 blocked，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 目录或宣称全量 E2E；列出了缺陷、修复版本/提交、预期行为、环境和执行入口等补充材料。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=dd44279ecc427987b1b3621312c679d5378dbd76e878bf90df9a1aafa4b05c73; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻断回归结论并列出主要缺失证据，结构化覆盖大多数要求，但未明确标记平台版本确认状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=05968272771db0cb8dc360a4bedb54d9ad4b7c7cf2217f1b0cdc350415c57ba7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 能识别材料不足并列出补充信息，但未提供结构化 blocked 状态、证据置信度或 PRD/TRD 对齐信息。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出遗漏了平台版本确认必须为 blocked 或 not executed 的明确状态。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93e5fd0d6baa599b41823d84d9e76df4ae1d287d1ee0dc585a0fbe0d3c54e8d5`
- Skill overlay SHA-256: `e9706a0f5c60f10753664f62398d5e5d1b2198510bb7a2bd63d1c64e17ebc61f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出缺少原始缺陷、失败证据、修复信息、构建/环境和执行入口，结论为不能开始复测。 |
| `blocked` | FAIL | 虽将本次回归整体标为 BLOCKED，但未逐项标记 original failure recheck、fixed behavior、adjacent regression checks、平台版本确认和 PRD/TRD 对齐状态。 |
| `assertion_3` | FAIL | 未包含要求的 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence 结构化字段。 |
| `assertion_4` | FAIL | 写明回归整体 BLOCKED，但没有明确给出 release recommendation，亦未使用 needs more verification 或对应发布建议字段。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 目录或宣称全量 E2E；列出了需补充的版本、环境、原始缺陷、修复证据和回归范围。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=83bf137197583a51256b074f6190a9e665325a0d5c137c8f1bf21a0c8be23daf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻断复测并识别缺失材料，但未逐项呈现要求的回归状态、发布建议和证据置信度。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=ae167146b57a2879b03930fb22941a3e760874bb8d66e5531735ce180cd5603f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别证据不足并列出补充材料，但同样未提供要求的结构化回归状态字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未逐项标记各回归检查为 blocked/not executed。
- with_skill 缺失要求的结构化输出字段。
- with_skill 未明确提供 release recommendation。
- Next: 补充逐项回归状态、release recommendation 和 evidence confidence。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e0bb997f7c8683c58b155379f15e9833f91e4d2f51aece7bfcfa4974d6a1defb`
- Skill overlay SHA-256: `5380fc16efa2deba2f3d503697de616d07aef499ace1b8bbfa59e73c1e19fe13`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出缺少原始缺陷记录、失败证据、修复信息和测试环境。 |
| `blocked` | FAIL | 标记了原问题、修复行为和邻近风险为未执行/blocked，但未明确将平台版本确认及 PRD/TRD 对齐状态标记为 blocked 或 not executed。 |
| `assertion_3` | FAIL | 包含前三项回归状态和发布建议，但未提供 evidence confidence，且不是完整的结构化字段输出。 |
| `assertion_4` | PASS | 发布建议明确为 needs more verification，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 目录或全量 E2E 结论，并列出了平台/浏览器版本、环境、原始缺陷和修复证据等补充要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=b1bed0403b842b4f726f9889d906011178dbb82de51fdfbcb6abee4c74ba5a05; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确阻塞回归、未执行各项验证并给出补充材料清单；仍遗漏 evidence confidence 及平台版本/PRD/TRD 的明确阻塞状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=96f7582437d2f27e918274149676f54778e2980ccfa9dbed7bc27a883d96e73f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并列出缺失信息，但未提供要求的回归状态结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确标记平台版本确认和 PRD/TRD 对齐状态为 blocked 或 not executed。
- with_skill 未包含 evidence confidence 字段。
- Next: 补充平台版本确认和 PRD/TRD 对齐状态，并将其明确标记为 blocked 或 not executed。
- Next: 在结构化输出中增加 evidence confidence。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `850108c3e4722feb1b9e0417b1554f0fb5b41d47001505d7da16c6bcd9946093`
- Skill overlay SHA-256: `3af177f0dcd9723964fdbcbf144832d8c6b68b267a850af3da918d86fe27d617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出缺少原始缺陷记录、复现/失败证据、修复提交或变更说明，以及测试环境和版本信息。 |
| `blocked` | FAIL | 仅声明总体状态为 blocked，未分别将 original failure recheck、fixed behavior、adjacent regression checks、平台版本确认及 PRD/TRD 对齐标记为 blocked 或 not executed。 |
| `assertion_3` | FAIL | 未以输出字段或清晰分节完整包含 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence。 |
| `assertion_4` | FAIL | 虽表示不能得出可发布结论，但未明确给出 release recommendation 为 needs more verification 或 blocked。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 作为结论或将局部回归当作全量 E2E，并列出了版本、环境、原始 bug、修复证据及相关验证材料的补充要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=22f34b11dca71abdc089dde4c4f44863a85714fd099545e42de564bead900c8e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并总体标记 blocked，补充了 PRD/TRD/实施计划和邻近场景要求，但未完整输出各项结构化回归状态、发布建议和证据置信度。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=4599e365113a983c9087eac4921d42ed3c180bd5daf7d9360af32409d19d962d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并要求补充原始缺陷、修复、版本、环境、测试步骤和回归证据，但未提供结构化 blocked 状态或明确证据置信度。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未分别标记要求的回归维度为 blocked 或 not executed。
- with_skill 未完整提供要求的结构化输出字段。
- with_skill 未明确给出符合限定值的 release recommendation。
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

# Eval Result: eval-002-blocked-without-original-bug-context

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`
- Test case: blocked-without-original-bug-context
- Workspace: `workspace/eval-2-blocked-without-original-bug-context`
- Natural user prompt:

> 复测上周修过的支付按钮问题，但仓库里找不到原始 bug 报告、失败证据、修复 PR 或可用测试环境。请给出回归验证结论。

- Expected artifact: blocked 回归验证报告，说明缺失上下文、无法复核 original failure、不能给 release ready 结论，并列出恢复验证所需证据

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-002-blocked-without-original-bug-context/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `fcb18ed7faddb7313fd51c13f012a7fe051e13a2f764566630a63d003a998d9a`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 1 / FAIL 4 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>原始证据缺失 | PASS | candidate.md 明确写出缺少 bug 报告、失败证据、修复 PR、变更说明、测试命令和测试环境；transcript 中仅执行了读取/探索命令，最终快照也只有 notes/missing-context.md，因此没有直接执行泛化回归的证据。 | PASS | candidate.md 明确列出缺少原始 Bug 报告、失败证据、修复 PR、测试命令和测试环境；transcript 仅有只读探索命令，快照无测试产物。 |
| `blocked`<br>blocked 状态 | FAIL | 原始失败、修复验证和邻近回归被描述为无法复现/未执行，且 PRD/TRD 对齐不可用；但没有明确标记 platform version confirmation 为 blocked 或 not executed，也未完整逐项给出 fixed behavior、adjacent regression checks 和对齐状态。 | FAIL | 虽然说明无法复测并列出缺失证据，但没有逐项标记 fixed behavior、adjacent regression checks、平台版本确认及 PRD/TRD 对齐为 blocked/not executed；transcript 也只有失败的 git 检查和文件读取。 |
| `assertion_3`<br>结构化输出 | FAIL | candidate.md 使用了语义近似的“原始失败/修复验证/邻近回归/发布建议”，但缺少必需的 evidence confidence 字段，且未完整按 original failure recheck、fixed behavior、adjacent regression checks 等结构化字段输出。 | FAIL | candidate.md 未包含完整的 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence 五项结构化输出。 |
| `assertion_4`<br>发布边界 | FAIL | “暂缓放行”语义上表示不放行，但断言规定 release recommendation 必须是 needs more verification 或 blocked；输出没有使用规定取值。 | FAIL | candidate.md 没有 release recommendation 字段，也没有明确给出 needs more verification 或 blocked 作为发布建议。 |
| `no_unknown_or_unscoped_release`<br>不得用 unknown 或误判发版范围 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 也无写入证据；但恢复清单虽包含原始 bug、失败证据、修复 PR、测试环境和执行入口，未明确列出缺失的测试平台版本，因此未满足“版本、环境、原始 bug 和修复证据”完整清单要求。 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 无写入证据；但候选未明确列出测试平台版本，恢复验证所需证据清单不完整。 |

## With-Skill Behavior

with_skill 正确识别上下文缺失并阻塞回归，但未完整满足结构化字段、平台版本状态和规定的 release recommendation 取值要求。最终快照仅有 notes/missing-context.md，且 transcript 仅显示读取命令，无写入或测试执行证据。

## Fresh Without-Skill Baseline

without_skill 同样识别了缺失上下文，但缺少更多必需的结构化状态与发布建议字段；仅作为 baseline 对照，不影响当前结果。两条 lane 的最终快照树、文件内容、SHA-256 和大小均一致，符合 fixture-manifest。

## Failures

- with_skill 的 blocked 断言未明确覆盖 platform version confirmation，且未逐项完整标记所有要求的检查状态。
- with_skill 缺少 evidence confidence，结构化输出字段不完整。
- with_skill 使用“暂缓放行”而非规定的 needs more verification 或 blocked。
- 两条 lane 均未在恢复验证清单中明确列出平台版本。

## Not Exercised

- 无。

## Next Steps

- 补充逐项结构化状态：original failure recheck、fixed behavior、adjacent regression checks、platform version confirmation、PRD/TRD alignment，均标为 blocked 或 not executed。
- 增加 evidence confidence 及简短依据。
- 将 release recommendation 明确写为 blocked 或 needs more verification，并列出平台版本、测试环境、原始 bug/失败证据、修复 PR/提交及预期行为。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
