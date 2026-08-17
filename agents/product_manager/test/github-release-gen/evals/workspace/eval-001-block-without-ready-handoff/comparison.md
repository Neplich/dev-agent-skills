# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-001-block-without-ready-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-001-block-without-ready-handoff`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `f104e1c59d5fad76689ae01a26b19666b3049ba013ffcdc08c70032e1a95c629`
- metadata_sha256: `9990f4cbb2adede98186059b8ed7e0088b4cd2cc6d822272edf43193f350dfdf`
- fixture_sha256: `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `00bb3d210a5b206a0ac9f62c0fe5d7e4f8787acdaa15b33827594f02c88b5a24`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_missing_handoff` | PASS | With_skill 明确将 no-handoff 场景标为阻塞，指出 handoff 为 missing，并说明不能生成可提交预览或草稿；同时要求返回 release-notes-gen。 |
| `blocks_unconfirmed_handoff` | PASS | With_skill 明确记录 confirmation_status: unconfirmed，并指出 docs check 通过不能替代 handoff；页面为 draft 且未获确认，因此仍阻塞。 |
| `returns_to_site_release_notes` | PASS | With_skill 对两个场景均指定返回 docs-agent:release-notes-gen，之后再等待 docs-audit；未自行补齐或假设上游证据。 |
| `no_publishable_output_or_mutation` | PASS | 未输出完整可发布 Release 正文；delivery_snapshot、declared_outputs、git diff/status 为空，git head、分支和引用均未变化，并明确禁止 draft、发布和 tag 操作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=76690008262ea7eb1a37ce7feea60473d5424eeb59bb20f8d8e15dc96cbf08f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 两个场景均正确阻塞，区分缺失 handoff 与未确认页面，并返回 docs-agent:release-notes-gen；无发布内容或仓库 mutation。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=70e93c53f5bd05cf29a39af78b8f8b0e818d0c0b431da42529ab4512df0fa4c5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样判断两个场景不能继续并识别主要门禁，但作为 fresh baseline 仅较简要地说明缺失 handoff 与未确认状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
