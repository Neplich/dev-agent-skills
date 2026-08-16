# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-006-preserve-independent-hosting`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f` from `agents/docs/test/docs-agent/evals/workspace/eval-006-preserve-independent-hosting`.
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `8a4360282a35d2ba7a52bbb24d703648e9f263e7fbfc9516063ba62f62b92b92`
- metadata_sha256: `62050136e2c1de0d65367ed4b1b1b706bb2211c3759fb54a832b8fd66233328b`
- fixture_sha256: `f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `787b3941ec90b819758a9894561fa37e2c0eff7eedddb4c4a4d863809f28587f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_not_applicable_evidence` | PASS | With-skill 输出确认文档不进入应用镜像、Compose 或 Helm，并由 `.github/workflows/publish-docs-static.yml` 以 public/internal 两个变体发布；fixture 中的决策记录确认维护者复核并签署现有方案且无需配置变更，输出给出证据路径并指定 Web Platform 为后续 owner。 |
| `does_not_open_devops_handoff` | PASS | With-skill 输出明确当前不需要应用部署团队介入，未启动下游 specialist，并仅在文档重新纳入应用部署链路时才考虑应用部署团队；git evidence 显示无提交、分支或工作树变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=ebb22a1b7ab1d6e2928e8a1c4ce67b394e68634551b9d754ec6a42e02246a92d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保留了替代静态托管的决策、证据路径、public/internal 覆盖变体和 Web Platform owner，并避免当前应用部署路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=75b11cec554fb9cabf92f38559abd7d5bd8c24a6e4b7927952fa49a44fb00e8c; fixture_sha256=f6c421284ed0143d28fff161f0f4c1cd48b067505beae1d38677d871a066543f; output_sha256=602532c7e3fe7d1303a8188306fd71f56e16e38ee0f6dfe0075c97d0e43edff1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样得出无需应用部署团队介入的结论，并保留主要托管证据；作为对照，其额外强调了快照缺少 workflow 运行依赖。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
