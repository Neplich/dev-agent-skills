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
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | With-skill output identifies the handoff package and explicitly lists host repository, version, scope, evidence sources, and required output. |
| `routes_release_notes_generator` | PASS | With-skill output selects `release-notes-gen` and keeps execution at the router boundary without routing to excluded specialists or GitHub Release delivery. |
| `preserves_handoff_context` | PASS | With-skill output preserves every required handoff field, including request type, tier, feature path, version, scope, repository, sources, output, and blockers/risks. |
| `references_release_notes_gate_only` | PASS | With-skill output states that `release-notes-gen` owns the next gate and that the router will not generate, publish, tag, deploy, or audit the release notes; it exposes no local skill path or detailed specialist protocol. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=fd6c4384ebbaa87f6318131d40bff3b43483205bdbdfdc90dceaea1777d2b75c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the handoff, routes to release-notes-gen, preserves context, and stops at the router boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=8c92bc70f8d88b8bf6a3f0f7125580a8d84ed1373a26720727cf8521ebbcdfb1; snapshot_sha256=0069660ea4f87efe0a48a0db30635a6d2c454621def02068deaafb7297a1dc4d
- Behavior: Generated a release-notes file despite missing source evidence and did not demonstrate the required routing or handoff-context behavior.
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

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `73f4addc59ec16b0f91c6a70a2a767ce7f6b4ad72612ca19a2131095a0722114`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | FAIL | with_skill 接受了入口，但明确称交接证据“未完整确认”并将已确认的来源视为缺失，未识别该 handoff 已满足完整 entry basis。 |
| `routes_release_notes_generator` | PASS | 明确选择 `release-notes-gen`，并声明仅路由，不执行 GitHub Release 或其他 specialist 的工作。 |
| `preserves_handoff_context` | PASS | 保留了请求类型、变更层级、feature path、版本与 scope、宿主仓库、来源文档、证据来源、required output 及 blockers/risks；`confirmed_scope` 与版本字段是语义等价表达。 |
| `references_release_notes_gate_only` | PASS | 明确指向 `release-notes-gen` 的 Release-Notes Checkpoint，并停在 router 边界，未要求暴露 SKILL.md 或复制下游协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=65866a2fbef38cc54ba9ae1ff1d1cf78103af5782d23659cda3918f026a1ab5d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由并保留上下文，但错误否定完整入口依据，因而阻塞在 router 边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=014cabd533fd0856f67dd5ddc9f208d7fe023e4745c3139918ee4a3f215d4076; snapshot_sha256=7a704e91abf2f7788b833d9e470257067ae21f6acf3ef1d8586fea4e0a5dcb1d
- Behavior: 直接生成并交付 Release Notes 文件，未执行题目要求的 specialist 路由行为；仅作为对比基线。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 错误地将 fixture 已确认的 entry basis 判定为未完整确认并阻塞流程。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | with_skill 明确接受 release-handoff.md 作为交接包，并确认版本、范围、宿主仓库、证据位置及所需输出。 |
| `routes_release_notes_generator` | PASS | with_skill 明确选择 release-notes-gen，并未改派其他 specialist 或扩大到 GitHub Release。 |
| `preserves_handoff_context` | PASS | with_skill 保留了 request_type、change_tier、feature_path、版本、范围、host_repository、source_documents、evidence_sources、required_output 与 blockers_risks；confirmed_scope 是 release_scope 的语义等价表达。 |
| `references_release_notes_gate_only` | PASS | with_skill 明确停在 release-notes-gen 的入口门禁，并声明不生成页面、发布、打 tag、部署或审计，也未要求暴露 SKILL.md 路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=34e21e47e815d82016c6e8838316dc1969e0ed51cb2400a68e141381e623d1d6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 specialist 路由与上下文保留，并在 release-notes-gen 入口门禁处暂停。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=70e1487534964f6396eea930051026b070459bf8cd7ee03db705325167b2e7fc; snapshot_sha256=b0af01685cda06a9475be7df3928dd810b7bb2810ff73e442c56edaa7cff112f
- Behavior: 直接生成并交付站内版本说明文件，未执行所需路由门禁。
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

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | with_skill 明确接受 release-handoff.md，并保留宿主、版本、范围、来源、证据及输出要求等入口依据。 |
| `routes_release_notes_generator` | PASS | with_skill 选择 release-notes-gen，未改派其他 specialist，也未将 GitHub Release 纳入当前 router 范围。 |
| `preserves_handoff_context` | PASS | with_skill 保留了 request_type、change_tier、feature_path、v1.0.0、范围、宿主、源文档、证据、required_output 与 blockers_risks；confirmed_scope 是 release_scope 的语义等价表达。 |
| `references_release_notes_gate_only` | PASS | with_skill 明确 specialist 接管、停在 router 边界，并声明不写入、发布、打 tag、部署或审计，未暴露本地 skill 路径或复制下游协议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=6f4a58e374d5984c6c61afc21d48f0579e696296ecb837dfed206b389b796d32; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别入口、路由 release-notes-gen、保留上下文，并因阻塞停在 router 边界；工作区无变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=05353dfd44b083d4abf67cfe4675de3b86991f1a7c9cd9fcc88117bb48d5ea4b; snapshot_sha256=16aeb9ee82a1de01d85ccae5eb9e11de86cbada04e426f85b48151830a555a4f
- Behavior: 直接生成并交付站内 Release Notes 文件，未执行所需 specialist 路由与 router 边界控制。
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

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | with_skill 输出明确接受 v1.0.0、范围、handoff 中的证据来源、目标宿主输出路径及阻塞背景。 |
| `routes_release_notes_generator` | FAIL | 虽选择了 release-notes-gen，但又明确提出应转交并进入 docs-site-bootstrap，违反了不得改派 docs-site-bootstrap 的要求。 |
| `preserves_handoff_context` | FAIL | with_skill 输出未保留 request_type、change_tier、feature_path、source_documents 等完整入口字段，仅概括了部分版本、范围、证据和目标输出信息。 |
| `references_release_notes_gate_only` | FAIL | 输出暴露了本地 release-notes-gen/SKILL.md 和 docs-site-bootstrap/SKILL.md 路径，并复制了额外的 bootstrap handoff，超出仅指向 specialist gate 的要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=efa0a299b35e7bf67c15676d844774ca7ce67e8d54ff6d674d0a132e90106d19; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并路由到 release-notes-gen，保留部分上下文并停留在未生成文件的阻塞状态，但错误引入 docs-site-bootstrap 和本地技能路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=d23def78f70d69838cddc78958ff4fc2d72b3beee62f3e48aa623ee9423da92d; snapshot_sha256=0e6eb23c4fed1f652613e6270ffc5940c2539ca90a438ade608b88e9132e6b21
- Behavior: 直接生成未充分验证的版本说明文件，未展示正确的 specialist 路由或完整入口上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 将 docs-site-bootstrap 作为后续转交对象，违反路由约束。
- with_skill 未保留完整 handoff 上下文。
- with_skill 暴露本地 SKILL.md 路径并扩展了 router 边界。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6d935c2fabb41ac4d322f49d33294bd64934555c17ee2ff70a64426da58d1b41`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | PASS | 明确表示已按 release-handoff.md 处理并路由，体现接受该入口依据。 |
| `routes_release_notes_generator` | FAIL | 虽选择了 release-notes-gen，但又将下一步改派为先由 docs-site-bootstrap 初始化，违反不得改派该 specialist 的要求。 |
| `preserves_handoff_context` | FAIL | 输出未保留 request_type、change_tier、feature_path、scope、仓库、来源文档、证据来源、required_output 及 blockers_risks 等入口上下文。 |
| `references_release_notes_gate_only` | FAIL | 虽说明未写入工作区，但输出继续描述 docs checks 配置并提出 docs-site-bootstrap 后续流程，超出 release-notes-gen 在 router 边界接管的要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=15135949bb5a22d203e2f7d24980abd0094e00ed16303a25cfcbb9ac79b29314; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确提及 release-notes-gen 并保持零写入，但遗漏入口上下文，并将后续工作导向 docs-site-bootstrap。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=4619330da4e4bb88476347a87a9adfff8066d8c2dcee5f404c8731591c5503fb; snapshot_sha256=82bb29d7bc2ccef6381e532ae0b7b24210084de89e64dc215cb93b0cc9be0fbb
- Behavior: 生成了版本说明文件，但未按要求路由到 release-notes-gen，且证据显示源文档和测试证据缺失。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整保留 handoff 入口上下文。
- with_skill 将后续步骤改派为 docs-site-bootstrap，并超出 specialist gate 边界。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9b5483c75770358083301bcb4f3e774af3a6e851f51536b52de7b7f0a1bd16fd`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8f5c2c38ebd9c9bb0326fa6044e4d6d7a5002b68fd540017de52e9465230113b`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | FAIL | with_skill 仅称按 release-handoff.md 路由，未识别或保留目标宿主、版本与 scope、证据来源及输出要求。 |
| `routes_release_notes_generator` | FAIL | 虽明确路由至 release-notes-gen，但又要求由 docs-site-bootstrap 初始化文档站，违反不得改派至 docs-site-bootstrap 的要求。 |
| `preserves_handoff_context` | FAIL | with_skill 输出未保留 request_type、change_tier、feature_path、release_version、release_scope、host_repository、source_documents、evidence_sources、required_output 与 blockers_risks。 |
| `references_release_notes_gate_only` | FAIL | 未指向 release-notes-gen/SKILL.md 或其内部指令作为权威执行 gate。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=f80f09b75a8575f0028324d1566dc4640452655e88b262b0581222501727ae28; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并提及 release-notes-gen 路由，但因缺少 docs/site 目录而阻塞，并提出 docs-site-bootstrap 初始化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=74a8ab772c614dc5c5a036875527ebcd9abb11d6ff84799d617e6deea6ce6f9d; snapshot_sha256=7c8f8b7179c0b9a479d18638f12ad359936e4c87e1a314337e0c8bce1b815ce2
- Behavior: 生成了版本说明文件，但未执行目标路由，并承认缺少源文档与测试证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整识别或保留入口上下文。
- with_skill 将文档站初始化作为下一步，且未引用 specialist gate。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8f5c2c38ebd9c9bb0326fa6044e4d6d7a5002b68fd540017de52e9465230113b`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | FAIL | with_skill 仅提到版本、输出路径和站点目录阻塞，未保留或明确 host_repository、release_scope、evidence_sources 等完整入口依据。 |
| `routes_release_notes_generator` | FAIL | with_skill 将下一步错误指向 docs-site-bootstrap，未选择 release-notes-gen。 |
| `preserves_handoff_context` | FAIL | with_skill 输出仅保留目标版本和应产出路径，未保留 request_type、change_tier、feature_path、scope、仓库、来源、证据、要求及 blockers_risks。 |
| `references_release_notes_gate_only` | FAIL | with_skill 未指向 release-notes-gen/SKILL.md，反而指向 docs-site-bootstrap；虽未复制详细协议，但不满足指定 specialist gate。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=a42ff237850fa5f9c62ae2450319885070e37b5ee015ad524c4dc22711c52bf3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到版本说明目标，但因错误的站点基础门禁判断而阻塞，并错误建议 docs-site-bootstrap。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=f6e090760a361b77ac63fc96a267ef851a92226de1f49c3f9a57be022e5eb9d7; snapshot_sha256=1a93e9475aa51d959c884cec882a4095ecebf169ecffaf9413b10079f493ba38
- Behavior: 直接生成了站内版本说明文件；未体现 specialist 路由或完整 handoff 上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- accepts_release_notes_entry_basis
- routes_release_notes_generator
- preserves_handoff_context
- references_release_notes_gate_only
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Test Set / Fixture Version

- Fixture version: `release-handoff.md`（fixture 身份文本 2026-07-29 更新后）
- Fresh run（2026-08-03，#188）：`tmp/eval-runs/issue-188-docs/with_skill/eval-004-route-release-notes/candidate-output.md` 与 `tmp/eval-runs/issue-188-docs/without_skill/eval-004-route-release-notes/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-188-docs/judge/verdict.md`

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_release_notes_entry_basis | FAIL | FAIL | with_skill 仅笼统称 `release-handoff.md` 为完整交接包，未逐项保留宿主、scope、证据来源等依据；without_skill 只确认 `existing_update`、`major` 和 `v1.0.0`，并称相关证据文件不存在，未接受完整 specialist entry basis。 |
| routes_release_notes_generator | PASS | FAIL | with_skill 明确路由至 `docs-agent:release-notes-gen`；without_skill 仅写“由 Docs specialist 生成”，未选择 `release-notes-gen`。 |
| preserves_handoff_context | FAIL | FAIL | 两条 lane 均未在结果中保留完整的 `request_type`、`change_tier`、`feature_path`、`release_scope`、`host_repository`、`source_documents`、`evidence_sources`、`required_output` 和 `blockers_risks`。 |
| references_release_notes_gate_only | FAIL | FAIL | 两条 lane 均未指向 `release-notes-gen/SKILL.md` 或其内部指令；未复制详细协议，但缺少必要的 specialist gate 指针。 |

未满足断言（with/without 任一 FAIL）：`accepts_release_notes_entry_basis`、`routes_release_notes_generator`、`preserves_handoff_context`、`references_release_notes_gate_only`



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-19（fixture 下游指向修正前）：**PASS（4/4 assertions）** — with-skill 接受完整 Release Notes entry basis，保留全部 handoff 上下文，选择 `release-notes-gen`，且没有复制或执行 specialist 协议。

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_release_notes_entry_basis`：PASS。识别宿主、维护者确认版本、scope、证据与站内页面/下游 handoff 要求。
- `routes_release_notes_generator`：PASS。明确选择 `release-notes-gen`，排除 sync、audit、bootstrap 与 GitHub Release 当前执行。
- `preserves_handoff_context`：PASS。保留 request、tier、feature、version、scope、host、source、evidence、output 与 risk 字段。
- `references_release_notes_gate_only`：PASS。仅指向 specialist SKILL 及内部指令，没有复制七步流程或执行正文、metadata、checks、#117/#120 handoff。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- fresh candidate 只完成 router 入口检查和分流，workspace 零写入。
- 输出明确正文确认与宿主检查仍由 specialist gate 处理，当前轮未自动继续。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 已命名并正确路由 `docs-agent:release-notes-gen`（accepts 与 routes 两条断言 PASS），但未完整保留 handoff context（缺 `host_repository`、原始 `release_scope`），且复制了 specialist 流程、未引用权威 gate——2/4 PASS。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 with-skill assertion failure。
- Harness limitation：baseline 可通过父仓库 Git 命令看到文件名/状态，但未读取目标 skill 或 README 内容；未影响本用例的语义差异。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 Release Notes 窄路由与 specialist 单一真源；入口字段或边界变化时重跑。

## Runtime Artifact Policy

- candidate、transcript、manifest、diff 与状态文件仅保留在 `tmp/eval-runs/issue-188-docs/`，不提交到 git。
