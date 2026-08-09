# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | 报告的“Deterministic impact”明确说明必需页面未在 base-to-target diff 中更新，因此进入事实审查时标记为 `suspect`。 |
| `confirms_outdated_claim_stale` | PASS | 报告以目标代码 blob 为证据，确认 `locale` 必填非空并存在 `400 {"code": "invalid_locale"}`，随后将文档结论定为 `stale`。 |
| `blocks_stale_release` | PASS | 报告结果为 `blocked`，列出 stale 页面证据及更新文档后重新审计等具体待办，并明确未执行 tag 操作且未返回 `ready_for_tag`。 |
| `does_not_stamp_stale_set` | PASS | 报告明确写出“No page was stamped”，且目标树没有 `.meta/releases.json`；文档的 `last_verified_version` 保持为 `v1.0.0`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=f548f1e435668a919e740752f08347fe8e91d96eae537e2284575c40aaa83861; snapshot_sha256=b510e4dcdd8ee892520bac506cf355a2ce699b54aa4bcbfddb54bea690de79df
- Behavior: 完成正式文档审计，识别 suspect、经事实核验确认 stale，并以 blocked 结果阻止版本盖章和发布操作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=cd07cf3d7db5e15199afce0f99febb20947a1a5e6d3915894fb5c31ac15f5735; snapshot_sha256=c327e63cd185bf04976939bce8907b505f7cbd832509ebd95570461c80f3156e
- Behavior: 生成了审计报告并指出文档遗漏 locale、invalid_locale 和旧验证版本，但未展示确定性 suspect 到事实层 stale 的审计链路，也未明确 blocked、未盖章和具体发布阻塞控制。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
