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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- metadata_sha256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- fixture_sha256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | PASS | with_skill 记录确认目标树中仅有可解析的 SVG，且明确指出第二步引用的 step-2-save-member.png 缺失。 |
| `checks_caption_step_correspondence` | PASS | with_skill 明确指出第一步要求打开访问设置，而图注写成“删除工作区确认框”，并以页面第24行和 SVG 内容为证。 |
| `checks_manual_navigation_reachability` | PASS | with_skill 依据 public 落地页、manual 根索引及生成侧边栏快照，明确指出 /manual/workspaces/manage-access 不在导航中。 |
| `checks_manual_redaction` | PASS | with_skill 明确指出正文第18行的 test.user@example.invalid 测试邮箱，以及 SVG 第5行的 token-demo-redact-me 测试令牌，均需脱敏。 |
| `blocks_manual_stamp` | PASS | with_skill 将审计结论标为 blocked，指出页面原始 last_verified_version 为 unverified，并明确未执行盖章、未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=2d2dd9615ef1689469607681b4d21c2a09c95230752217150c8c139357553a5f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整识别截图完整性、图注对应关系、导航不可达、脱敏问题及阻断盖章条件，并保留 unverified 状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=fd0740e2b82b7f0eb7c21c739ceb6b3ba231053d81bcddf71fa320ec58c48b51; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了缺失截图、导航缺失、图注不符和令牌风险，但未明确指出正文测试邮箱，也未完整覆盖导航三类证据和阻断状态要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
