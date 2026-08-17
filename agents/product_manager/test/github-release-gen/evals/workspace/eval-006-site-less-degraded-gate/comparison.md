# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-006-site-less-degraded-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-006-site-less-degraded-gate`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `ee0644452d121d4667c014aaf941ed770c3978ba415b0f3ee7cfc601dc801335`
- metadata_sha256: `d64e10da3608725d47dc87efed91ed453ddbf43cfa5350e92eb1e539cf16b5a4`
- fixture_sha256: `411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b8169d6d4489fefe59aefe4458af6c4e8108513691e18f7c250f5d7f5c9b7ba5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `proceeds_without_handoff_when_site_absent` | PASS | with_skill 明确确认 docs/site 与 release-notes-gen 能力链不存在，且在已确认 changelog 场景生成了完整 GitHub Release 标题与正文预览。 |
| `records_downgrade_basis` | PASS | with_skill 明确记录正式文档站未初始化、docs/site 与 Release Notes 能力链不存在、handoff 门禁不适用，并列出 release-package.md、已确认 changelog 与 version-bump evidence。 |
| `still_requires_maintainer_approval` | PASS | with_skill 明确仅提供 inline preview，禁止 draft、GitHub 写入和 tag 操作；git evidence 显示无变更，并要求后续 draft/publish 写入前获得明确、当前的维护者批准。 |
| `blocks_without_confirmed_fact_source` | PASS | with_skill 将第二场景标记为 blocked，指出 version bump 为 proposed、无版本化 changelog及维护者确认事实源，并拒绝将候选版本、commit subjects或未确认摘要作为发布事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=ed5d51a14d0c9ea500cfa7674a902e250d9347327f268a044325864aa8ca5c15; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分 site-less 且有确认事实源的可预览场景与无确认事实源的阻塞场景；仅生成预览且保留维护者批准门禁。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3543da7f86f46fe1ddba91b579642c6082b99cf4ee707ac9b96a7d9fcb3ea3e7; fixture_sha256=411862fab7a80dddacd42426a98282018153d50c9458b43edec6c0056c4dce20; output_sha256=a0d9dcd018c3a7b269b9a7a08b44e4106081f196f2c3b8f80e25611c625d5429; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: fresh baseline 同样生成了场景 A 预览并阻塞场景 B，但未显式记录完整的门禁降级依据与结构化适用性状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
