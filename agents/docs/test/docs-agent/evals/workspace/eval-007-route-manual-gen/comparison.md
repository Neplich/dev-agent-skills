# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `91cbb2dfbc7f79ee3f298d858c1e3b0b986717f5b79fc8d2fb2d8be9f6762763`
- Judge schema SHA-256: `dfbcad96e39d7a0ba2503c7d345d86b54a6c9e1188ff1c09f99476b24380e820`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill 明确接受 manual-handoff.md 中的显式 Manual Generation Handoff，并保留入口字段。 |
| `routes_manual_gen` | PASS | with_skill 明确选择 selected_specialist: manual-gen，未改派其他 specialist。 |
| `preserves_manual_handoff_context` | PASS | with_skill 保留 request_type、change_tier、feature_path、host_repository、manual_scope（以 confirmed_scope 表达）、evidence_sources、required_output 与 blockers_risks。 |
| `references_manual_gate_only` | PASS | with_skill 指向 manual-gen authoritative Entry Gate，并明确路由边界：不采集截图、不生成正文、不写入站点文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=939dd18b83baa441759def73fa3c7dd6f61a8a6f186f5a8cfdb1e1e078d30ee8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别入口凭据，路由至 manual-gen，保留上下文并停在 specialist gate 边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=7a4c0fe3c14ba2bee699b05fc90b52bc83fcba24072d04c4bc519c0d5cc615ea; snapshot_sha256=10e8c8a895c274312d91e87ca89f644f3c6f2e3099f8f6385e33d5417421d464
- Behavior: 直接生成并声明完成手册，产生 docs/site/manual/ 下的文件，未执行所需的 manual-gen 路由边界。
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
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `91cbb2dfbc7f79ee3f298d858c1e3b0b986717f5b79fc8d2fb2d8be9f6762763`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | PASS | with_skill 明确接受 manual-handoff.md 交接包，并识别其手册范围、宿主仓库、运行界面证据和所需输出。 |
| `routes_manual_gen` | PASS | with_skill 明确选择 manual-gen，未改派其他 specialist。 |
| `preserves_manual_handoff_context` | PASS | with_skill 保留了 request_type、change_tier、feature_path、host_repository、manual_scope（以 confirmed_scope 表述）、evidence_sources、required_output 和 blockers_risks。 |
| `references_manual_gate_only` | PASS | with_skill 明确停在 manual-gen specialist 接管的路由边界，不生成或修改手册，也未要求暴露本地 SKILL.md 路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=5f50e73ab617a481e002b0a53708c5b98004e996ce1e3e63035fef9191a114f9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受交接包，路由至 manual-gen，并停在 specialist 接管边界，未进行手册生成或工作区修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=1886695e4f67a4c725a3f91b2c3ca56a7633ef208f7a457f3441009607de914c; snapshot_sha256=c8614e382a658eccbfcd08c298394ee6e41d3c983c39951f3de422aacfbba91d
- Behavior: 直接生成并交付手册及 SVG 示意图，未执行入口路由。
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
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `6214a7a342b55bde83bd1137337eab9c9044050e4bd53613b5541dbb41ce704b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | FAIL | 虽称接受 formal Docs 交接包并选择 manual-gen，但错误声称缺少 docs/site 基础设施及多项入口字段，未认可 fixture 已提供的完整入口凭据。 |
| `routes_manual_gen` | FAIL | 先选定 manual-gen，随后明确要求改派 docs-site-bootstrap，违反不得改派的要求。 |
| `preserves_manual_handoff_context` | FAIL | 未保留并呈现 request_type、change_tier、feature_path、host_repository、manual_scope、evidence_sources、required_output 与 blockers_risks，反而声称存在 fixture 未要求的缺失字段。 |
| `references_manual_gate_only` | FAIL | 虽提及 manual-gen specialist，但实际要求确认交由 docs-site-bootstrap 处理，未停在 manual-gen router 边界。未发生站点写入、截图采集或审计 handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=018422ab5983124489b1533020c0377ec5806e6aa5e0e9925cef6603ce8b73ac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并选定 manual-gen，但错误判定入口不完整并将后续处理改派 docs-site-bootstrap；未写入文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=d213a48d330e764d41e2c6368759a29d622f225c9a04e48c2d6956cf0b496568; snapshot_sha256=7b8956230334591da027c8e1f52e9944108886cec393da749f71b2184d52e68c
- Behavior: 直接生成并声明已完成手册及 SVG，产生 docs/site/manual/ 下未跟踪文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 错误否定 fixture 已提供的 manual-gen 入口凭据。
- with_skill 将请求改派至 docs-site-bootstrap，违反路由和 router 边界要求。
- with_skill 未保留所需的手册交接上下文字段。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `6214a7a342b55bde83bd1137337eab9c9044050e4bd53613b5541dbb41ce704b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `11398fbb2de74bd454f6e9c88338b5fcf6dffb0fd21436f1f6c99eaff5b1117d`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | FAIL | with_skill 仅笼统引用 manual-handoff.md，且错误声称仓库不存在 docs/site/；fixture 明确说明宿主仓库已有 docs/site/ 基础。 |
| `routes_manual_gen` | FAIL | 虽声明路由至 manual-gen，但随后明确要求改由 docs-site-bootstrap 初始化后再返回，构成错误改派。 |
| `preserves_manual_handoff_context` | NOT_EXERCISED | 锁定输出未展示各字段的保留过程或结构化上下文；该内部保留行为无法由原始证据证明。 |
| `references_manual_gate_only` | FAIL | 未明确停在 manual-gen specialist gate，反而提出 docs-site-bootstrap 后续改派；其 docs/site 缺失的阻塞理由也与 fixture 矛盾。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=a84476f5c1f4b53c0bc8b7a85f29e87b4b707ddb0c701f60f0cf3141342bf5b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 声明进入 manual-gen，但因错误识别仓库状态而阻塞，并提出改派 docs-site-bootstrap；未写入文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=9a1c5ceb7faf0974c7dbcc8fb81d5ff8fd810a5bc4b6074903fd5713e14a02e1; snapshot_sha256=fe781233cf50109238f273596eac263a0431554235ea584f261c6d9146fcaae5
- Behavior: 直接生成了手册及 SVG 文件，未遵循 manual-gen 路由边界并产生了工作区变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 错误声称 docs/site 不存在，违背手册入口凭据。
- with_skill 将后续处理改派给 docs-site-bootstrap，而不是仅停在 manual-gen specialist gate。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9b5483c75770358083301bcb4f3e774af3a6e851f51536b52de7b7f0a1bd16fd`
- Skill overlay SHA-256: `1d16022e6080ee5de6d68ef3f10a9fbc9514265e2e4db68a0fd837aa562987a7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5ef7a8c9ec39d7590c86a5a65b45bb35d1908a38c9e6c3552abfb5a25bde64ca`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | FAIL | with_skill says the handoff is routed to manual-gen, but incorrectly claims the repository lacks docs/site infrastructure; the fixture states the host repository has an existing docs/site foundation, so it does not accept the complete entry basis. |
| `routes_manual_gen` | FAIL | It initially routes to manual-gen, but then explicitly directs the next step to docs-site-bootstrap, violating the required routing. |
| `preserves_manual_handoff_context` | FAIL | The output omits request_type, change_tier, feature_path, manual_scope, and blockers_risks, and only partially mentions the host repository, evidence source, and required output. |
| `references_manual_gate_only` | FAIL | It points to docs-site-bootstrap as the next handoff instead of only identifying manual-gen/SKILL.md and its internal instructions as the execution gate. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=8e119032db6429a8e27f6a51e1fdeb178964ed9da011c383e9e2323a05a8f91c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly named manual-gen initially, but falsely treated existing docs/site infrastructure as missing and redirected to docs-site-bootstrap without preserving the handoff context.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=2723823c5961f4647e52c41a34aa2e6b4da695a001f382416e5542ce79867888; snapshot_sha256=3eb6955e6cb24eed8d92453e4226d0b0659e5bdc988dc6870d5aaf761901edc2
- Behavior: Generated manual files and diagrams without performing the required routing/handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill rejected a valid manual-gen entry because of a contradicted infrastructure blocker.
- with_skill redirected to docs-site-bootstrap.
- with_skill did not preserve all required handoff fields.
- with_skill did not reference only the manual specialist gate.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-007-route-manual-gen`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8` from `agents/docs/test/docs-agent/evals/workspace/eval-007-route-manual-gen`.
- Fixture SHA-256: `7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8`
- Prompt SHA-256: `a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `d1bf75634222a05713b3bf7d221f7c7af2d83563e0e044c3ba1f92db7ded641b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5ef7a8c9ec39d7590c86a5a65b45bb35d1908a38c9e6c3552abfb5a25bde64ca`
- Metadata SHA-256: `31c2720a1114e612336c51527d7aae20dddb1f4e46b566ffffe4788d27952b8e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_manual_entry_basis` | FAIL | with_skill 输出仅确认范围、运行环境和目标路径，未完整识别 handoff 中的 request_type、change_tier、feature_path、host_repository、evidence_sources、required_output 等入口凭据。 |
| `routes_manual_gen` | FAIL | with_skill 输出将 docs-site-bootstrap 作为下一步并称其 blocked，未保持直接分流到 manual-gen。 |
| `preserves_manual_handoff_context` | FAIL | with_skill 输出未保留完整的 request_type、change_tier、feature_path、host_repository、evidence_sources、required_output 与 blockers_risks 字段上下文。 |
| `references_manual_gate_only` | FAIL | with_skill 输出指向并要求先执行 docs-site-bootstrap，且提出截图计划与维护者确认，违反仅指向 manual-gen/SKILL.md 内部 gate 的要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=de2f4d86592c12c0e2d8f3487525213236840aea5f2407d4d0efc691a321aa63; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别部分手册范围后阻塞，改派 docs-site-bootstrap，并未保留完整 handoff 上下文。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a3cc737cbb46c53cc07ec65089d26bb1859146138c26d847279db190c633dcfa; fixture_sha256=7e690828debd990987ec359671232498f20061c2fa6e2bbd324f99b92a7c2fc8; output_sha256=d0a6c3a0c85dbf6dd54496efaa5e32948455f70a6cb251c6f7c18208c55d5ec3; snapshot_sha256=e9cd26ea79c9434384f2d8fef03002b3aa8c684a9c38f653d86021d7843fdf2a
- Behavior: 生成并声明写入 docs/site/manual/ 下的手册与 SVG，未执行入口路由判断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整接受并保留 manual-handoff 入口凭据。
- with_skill 将请求改派至 docs-site-bootstrap，而非仅路由至 manual-gen。
- with_skill 未遵守 manual specialist gate-only 约束。
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
- Eval: `eval-007-route-manual-gen`
- Target behavior: route a screenshot-evidenced illustrated manual request to `manual-gen` without executing its gate

## Test Set / Fixture Version

- Fixture version: `manual-routing-v0.1.0`
- Entry fixture: `manual-handoff.md`
- Validation status: #238 fresh 重跑已于 `2026-08-06` 完成

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_manual_entry_basis | PASS | PASS | with_skill 明确称“已完成入口校验”，并引用 handoff 中的范围、证据来源和预期产物；without_skill 明确称“已验证”，同样识别了范围、证据、目标和 `standard` 等入口信息。 |
| routes_manual_gen | PASS | FAIL | with_skill 明确选择 `docs-agent:manual-gen`；without_skill 仅写“manual specialist gate”，未明确选择 `manual-gen`。 |
| preserves_manual_handoff_context | FAIL | FAIL | with_skill 仅保留范围、证据和输出，遗漏 `request_type`、`change_tier`、`feature_path`、`host_repository`、`blockers_risks`；without_skill 也遗漏 `feature_path`、`host_repository`，且未完整保留原始阻塞风险字段。 |
| references_manual_gate_only | PASS | FAIL | with_skill 明确将截图、环境确认、候选步骤确认和写入交给“`manual-gen` 专项流程”，且声明当前未生成或修改文件；without_skill 未明确指向 `manual-gen` gate，仅泛称“manual specialist gate”，并额外自行判断 `docs/site/` 缺失为阻塞。 |

未满足断言（with/without 任一 FAIL）：`routes_manual_gen`、`preserves_manual_handoff_context`、`references_manual_gate_only`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Not observed. The future lane must stop after selecting and pointing to `manual-gen`.

## Fresh Without-Skill Baseline（#238）

- Source: 2026-08-06 #238 fresh isolated rerun using the same prompt and pristine fixture without loading `docs-agent`; an independent judge evaluated all four assertions.
- Behavior summary: Behavior `FAIL` / Coverage `FULL`; `accepts_manual_entry_basis` passed, while routing, handoff preservation, and specialist-gate references were incomplete.

## Failures

- #238 fresh 重跑中，with-skill 未完整保留 `request_type`、`change_tier`、`feature_path`、`host_repository` 与 `blockers_risks`，`preserves_manual_handoff_context` 判定为 `FAIL`。

## Next Steps

- 修复 router 的 handoff context 保留缺口后，使用相同 prompt 与 pristine fixture 重新执行 paired eval，并由独立 judge 复核四条断言。

## Runtime Artifact Policy

- Candidate outputs, transcripts, manifests, verdicts, timing, status, and diagnostics remain in isolated runtime scratch space and are not committed.
