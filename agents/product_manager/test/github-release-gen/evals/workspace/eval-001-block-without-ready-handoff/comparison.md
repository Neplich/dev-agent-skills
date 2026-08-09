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
- Fixture SHA-256: `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900`
- Prompt SHA-256: `286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `00bb3d210a5b206a0ac9f62c0fe5d7e4f8787acdaa15b33827594f02c88b5a24`
- Eval definition SHA-256: `f104e1c59d5fad76689ae01a26b19666b3049ba013ffcdc08c70032e1a95c629`
- Metadata SHA-256: `9990f4cbb2adede98186059b8ed7e0088b4cd2cc6d822272edf43193f350dfdf`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_missing_handoff` | PASS | with_skill 明确说明 no-handoff 场景不能继续，标记 handoff 为 missing，并指出不可生成可提交或发布内容。 |
| `blocks_unconfirmed_handoff` | PASS | with_skill 明确识别 confirmation_status 为 unconfirmed、handoff 为 blocked，并说明 docs 测试通过及页面存在都不足以视为 ready。 |
| `returns_to_site_release_notes` | PASS | with_skill 对两个场景均指定退回 docs-agent:release-notes-gen，分别补齐确认或 handoff，未假设上游证据。 |
| `no_publishable_output_or_mutation` | PASS | with_skill 未输出完整可发布 Release 正文；明确禁止 draft、发布、docs/site 修改及 tag 操作。锁定 git evidence 显示无提交、分支、引用或工作区变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=76ba164ff2772de575027f5b436b3de2b4d3b613a0bd4c54b8138f0f176a0109; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞两个场景，识别 handoff 缺口与未确认状态，并返回站内 release-notes-gen 流程；无发布内容或仓库变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=58f7a027faeebe7c53095dd43dacaea68bd3de666b6d066c15e5c6f54c2992c7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线同样识别了两个阻塞条件并拒绝发布，但对正式站内流程和后续门禁链的说明较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
