# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `38b6af0374fcc8ce56a2a453684404f29e895eaad6d86b973c652b7dd34579f8`
- metadata_sha256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- fixture_sha256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | with_skill 明确列出版本、scope、宿主仓库、来源证据和 required_output，并判断入口基础完整。 |
| `routes_release_notes_generator` | PASS | with_skill 明确路由至 `release-notes-gen`，并声明路由器不执行页面写入、发布、打 tag 或审计。 |
| `preserves_handoff_context` | PASS | with_skill 保留并传递 handoff 的版本、scope、feature path、宿主、来源证据、输出要求和 blockers；语义等价地使用了字段摘要。 |
| `references_release_notes_gate_only` | PASS | with_skill 指向 `release-notes-gen` 承接后续正文生成和验证，并明确路由器不执行下游写入或审计流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=845d9ccc977325ad1c33cfed893f84369a0258f73f7f5c3877a488dcbf723744; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别完整 Release Notes 入口基础，路由至 release-notes-gen，保留上下文并遵守路由边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=49253717b05b70ac5dba4b5189f7021aded6d59023c3de2ef4e8ced6bd39ca89; snapshot_sha256=385dff775fc2a4e117a2383bdda867061125fff470f6b8273d06cc1b11708c9d
- Behavior: 直接生成并交付了站内版本说明文件，未展示路由器边界或 specialist handoff 行为。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
