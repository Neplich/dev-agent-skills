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
- target_skill_sha256: `4e9403c0e6549024a79156a156c1294488d1a418598e88e3e9565298bc6bae6a`
- eval_definition_sha256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- metadata_sha256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- fixture_sha256: `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2f3ed1bac6bd41e43ecbd585f5beb95db8464a7cf767e9c9a3ef20fae4f56429`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确指出缺少原始缺陷/失败证据、修复上下文、测试环境等，并说明未执行测试、不能直接得出回归结论。 |
| `blocked` | PASS | with_skill 将原始失败复测、修复行为、相邻风险、平台版本及 PRD/TRD 对齐状态标记为 blocked 或 not executed。 |
| `assertion_3` | PASS | with_skill 包含原始失败复测、修复行为、相邻风险检查、发布建议和 evidence_confidence 字段。 |
| `assertion_4` | PASS | 发布建议为 needs more verification，未建议 release ready。 |
| `no_unknown_or_unscoped_release` | PASS | with_skill 未使用 unknown 目录或全量 E2E 结论，并列出了恢复验证所需的版本、环境、原始 bug、修复证据等。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=60324b1d5aafc14543837b70623814f10fd14c9fe9c2c9195bbe779bea80700d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别材料不足并阻断回归，提供结构化状态、证据置信度、发布边界和补充材料清单。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=1b6347fe6e6201c4eb8a4f97da6b862c86bd1ba85cad2c1d1b28a5c01b4e46f3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别材料不足并拒绝直接回归，但未提供 with_skill 中同等明确的结构化门禁与 PRD/TRD 对齐状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
