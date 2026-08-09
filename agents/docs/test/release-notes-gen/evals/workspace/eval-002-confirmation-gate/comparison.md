# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-002-confirmation-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc` from `agents/docs/test/release-notes-gen/evals/workspace/eval-002-confirmation-gate`.
- Fixture SHA-256: `d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc`
- Prompt SHA-256: `7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `f52a12716f836504537cf75e93c1e10d802a32eb7ad0a9945e2057c1a94c3f7c`
- Eval definition SHA-256: `734d8912f6102b866e236fb845ac847f11fde3651b05c29ee143e730ba9a8ce3`
- Metadata SHA-256: `244623c4cb29666e66fbef86938647497dad20990909aac70827020a236484a7`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_derived_surfaces_unchanged` | PASS | with_skill 的 locked delivery_snapshot 提供了候选文件；git_evidence 显示仅有该文件未跟踪，index、metadata、导航及其他派生面均无 diff，且正文写明确认后才更新这些路径。 |
| `reports_unconfirmed_not_ready` | PASS | with_skill 输出明确给出 confirmation_status: unconfirmed 和 handoff: blocked，并说明等待明确确认，没有宣称 ready。 |
| `waits_for_explicit_confirmation` | PASS | with_skill 输出展示完整候选正文、逐项列出六份来源证据，正文记录确认后的 index/.meta/导航更新计划，并明确等待确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=45e65ce62e5c80eb37cbf36abbf67997863713765d4f44a020d5cce4568791f2; snapshot_sha256=ef77127d93e0346defb14e3dae1b65c9afe7c850f9db7f499d088135f5d0e1b3
- Behavior: 生成完整候选 Release Notes，保留派生面不变，并以 blocked/unconfirmed 状态等待确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7064d6e7dd15f0c86ca51cdae30720bfc492837e0e9ed31705f989006960c692; fixture_sha256=d8d3cd2bcfa848d5848a9287f747e035b721f3a64f1b4c03c2359e2a75f040bc; output_sha256=d7d7faef8e512034f2d15a43d4feecdef0bf7895e8f11f994285124f5007e2b3; snapshot_sha256=a20eec8402970f255dfb0587611575794d9c7126c21b6c04f112cec646f7b269
- Behavior: 生成候选页面并保持派生面不变，但交接状态和等待确认信息不完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 等待用户或维护者确认正文后，再更新 Release Notes 索引、metadata 和导航。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
