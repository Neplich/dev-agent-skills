# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013` from `agents/product_manager/test/pm-agent/evals/workspace/eval-015-route-docs-site-deployment-gap`.
- Fixture SHA-256: `16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013`
- Prompt SHA-256: `f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4`
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `6e906e23fd0805526cda111a5e2e74eb02ce2f72534b3e384e90b10a34160090`
- Judge schema SHA-256: `69f2798cad12b0dd0ca3c224e3cfd6cf611a315695684db1b07a23452b52a60e`
- Eval definition SHA-256: `6e2d29edefa67ed434a00461a929405f7c4bccd693a99ad48559b546fe6fab29`
- Metadata SHA-256: `e7a743e88e4c53094e4afe2903a87ebcc467ace2dc58c61ccb0a0dcf64ebf2fd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unknown_evidence` | PASS | with_skill 明确保留静态证据边界，指出未执行 CI、镜像发布或部署验证，并将交接标为阻塞；没有宣称 integrated 或 ready handoff。 |
| `builds_repo_wide_deployment_packet` | PASS | with_skill 输出 request_type: deployment，所有 feature fields 为 N/A，feature_path_evidence 为空，并列出真实 source_documents 与 blockers_risks。 |
| `routes_devops_ordered_chain` | NOT_EXERCISED | with_skill 正确提出下一步交给 DevOps，随后由 Docs 同步；但 devops-agent 不可用，后续具体阶段的运行时证据不存在。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=d56efe9fe0297d78228f659df6ac25799c762f6e32563ce06d87010506eedcbb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确核对 CI 仅构建 public、Helm 仅启用 public，并生成受边界约束的 deployment 交接建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f6c9996daf9a7bdf78228fb674eccb457f386d1e74abf9925ac4646e4da1c9d4; fixture_sha256=16e3b6cbbbae6769ac6b5ead7bae34214b3dd90e3e6c4d5fad97cfd7d3784013; output_sha256=58e558e71c3ed255df1dbd041d69c8dd0c7047cc48ad366392e60d1faa00d2e1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 CI 证据缺口，但因未读取可用 fixture 中的 CI 配置而停留在 unknown。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 启用或安装 devops-agent 后，继续执行 DevOps 规划、CI/CD 引导和环境配置审计；取得验证证据后再进行 Docs 正式同步。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
