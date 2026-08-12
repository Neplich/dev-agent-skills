# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Identity schema: `2`
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- metadata_sha256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- fixture_sha256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | with_skill 的锁定输出说明第二步 PNG 不存在，但未输出确认第一步 SVG 可作为图像解析；raw trace 虽有 `svg-parse-ok`，未弥补输出遗漏。 |
| `checks_caption_step_correspondence` | PASS | 输出明确指出第一步“删除工作区确认框”图注与“访问设置”步骤及 SVG 内容不一致。 |
| `checks_manual_navigation_reachability` | FAIL | 输出仅指出导航快照确认页面不可达，未明确依据 public 落地页、manual 根索引和生成后快照均不含目标页面。 |
| `checks_manual_redaction` | FAIL | 输出识别了 SVG 中的 `token-demo-redact-me`，但未识别正文中的测试邮箱 `test.user@example.invalid`，也未完整提供两者的脱敏结论。 |
| `blocks_manual_stamp` | PASS | 输出将审计判为 `blocked`（pre-tag），记录页面 `last_verified_version: unverified`，且未返回 `ready_for_tag`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=7d999fe7f3465884bafdfc59f610dd684d1ca4916ff46e782d56e024e1ed7d15; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了主要事实缺陷并正确阻止盖章，但最终输出遗漏了 SVG 可解析性、完整导航来源和测试邮箱脱敏结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=8b75e81302de8fb315a0e567a4b3bee6a3d143b557b4891f8f719393338ddb66; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线识别了缺失 PNG、导航缺失、图注不匹配和 token 风险，但同样未完整覆盖逐步解析与邮箱脱敏要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- checks_step_screenshot_files 未输出第一步 SVG 可解析性的确认。
- checks_manual_navigation_reachability 未完整列出要求的三个导航证据来源。
- checks_manual_redaction 漏报正文测试邮箱及其脱敏要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
