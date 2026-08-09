# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-003-docs-image-release-rules`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-003-docs-image-release-rules`.
- Fixture SHA-256: `3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf`
- Prompt SHA-256: `d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `86f7228d11d9f7ad3ec145d83be1c28f8a4bb93afea61016f55ed2860069bc68`
- Skill overlay SHA-256: `d87d7023cb1778acf3685e0e616785cca86656081ff2fa7f0e1ff03553b77b80`
- Judge schema SHA-256: `8eaf2480ee518c77bc5e1ae8a7f25c0acfc010e7317cc45d7143e8591e25551c`
- Eval definition SHA-256: `90a9cf04ee14bffff8a2eaca0298de327ed551cee77903fd69a219a57495281e`
- Metadata SHA-256: `3fa9951d25624dea3daa1a46647a39c6e45e551d897c4684f13850f3c7afbfd4`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_host_image_policy` | PASS | with_skill 明确说明 Public 与 Internal 均使用不可变 vX.Y.Z/git-<shortsha> 标签、指定 registry、版本标签触发生产发布及 amd64/arm64 架构，符合 fixture 中的宿主约定。 |
| `verifies_each_published_variant` | NOT_EXERCISED | with_skill 正确要求两个镜像单元分别进行构建/发布验证并检查发布后的 digest/manifest；但锁定证据显示没有 CI/CD 实现或实际发布结果，因此无法行使对具体验证的核验。 |
| `keeps_delivery_authority_separate` | PASS | with_skill 明确指出 release manager 尚未批准 push/publication，且工作流定义不能授权这些动作；未发生文件、Git 或发布变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=b4d0b90fec33f0f2b53e923c6bf825ee760abd933c446f8c29829fc0131f5217; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确读取并应用发布约定，覆盖 Public 与 Internal、双架构、不可变标签、registry、tag trigger、digest/manifest 验证及授权边界；因无拟议 CI/CD 实现，未声称完成实际实现审查。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d3c1631bc39b4cdb5a62c7ac02b9b6359957e5c2debaf73a2659a08294722209; fixture_sha256=3676f277a876b41e1703c92d57107677efc45689334ecbdddc74bf8f7e7cb8bf; output_sha256=60ea10bac4e957d0ee6532244e3fc3002904ca38533b75e269ff2db159adff2a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别了现有发布约定和授权边界，但也只能进行规则级审查；作为新鲜基线，未提供实现级证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供拟议 CI/CD 配置或 diff，以核验每个镜像单元的实际 build/publish validation。
- Next: 提供发布后的 manifest/digest 运行时证据，以完成逐变体验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
