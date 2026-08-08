# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With_skill explicitly covers staging and production for Public DNS/TLS and Internal authentication/network controls, marking unavailable evidence as unknown where appropriate. |
| `audits_runtime_environment_differences` | PASS | With_skill covers ports, probes, Service/Ingress/Gateway evidence, secret/config references, and staging-versus-production differences, distinguishing known facts from unknown values. |
| `does_not_overclaim_missing_evidence` | PASS | With_skill records missing permissions/runtime/config evidence as unknown, avoids treating documented domains as verified integration, and limits formal-docs-sync to later landed and verified facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=1843cfa8447fd8425aa65acb4388c3c8642ac6112ab376f88c02091030bce7a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a complete read-only audit covering all requested access and runtime dimensions, with explicit unknowns and verification boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=30167cace5de71fff3476d876e54408bfadd21624c37ff7322c26228d2beb628; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a useful baseline audit with partial coverage, but less explicit runtime and evidence-boundary detail.
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

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | 报告逐项覆盖 staging/production 的 Public 与 Internal 入口，并分别记录 DNS、TLS、认证或网络限制及缺失项。 |
| `audits_runtime_environment_differences` | PASS | 报告矩阵和环境变量覆盖部分核对了端口/values、探针、Service/Ingress/Gateway、Secret/ConfigMap/CI/CD 引用及 staging-production 差异，缺失内容均标为 unknown。 |
| `does_not_overclaim_missing_evidence` | PASS | 报告明确将声明性文字与独立运行时验证区分，缺失权限、策略和运行时输出均记录为 unknown，未将域名或配置存在误称为集成或就绪证明。formal-docs-sync 的后续交接未被本次证据触发。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=03471c9d12594d4069ccee9ded8bf64533fe2172a88b0c2393fe9e434b9c49d4; snapshot_sha256=3713d7e68235292a325ab715453d695625a5cbce7d277840bed741c4c47008d6
- Behavior: 完成只读审计并交付 deploy/ENV_AUDIT.md；覆盖四个环境/入口及配置证据缺口。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=96b84aa6560c9049b483faf7a93a06f41ea1a25b9f2b70a33c3751aff403a92b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供未写入文件的审计摘要，覆盖主要入口和部分未知项，但没有交付审计文件。
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

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `10734badb795d9dd2c7f522212860a120a71a582b6fdcf439619f31f19b4904f`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | The with_skill audit covers all four variants. It explicitly records staging Public DNS/TLS and production Public's documented domain with TLS unknown; staging Internal network restriction/authentication; and production Internal with authentication policy unknown. This satisfies the requested Public DNS/TLS and Internal access-control audit across staging/production. |
| `audits_runtime_environment_differences` | PASS | The delivered audit matrix and configuration-coverage tables address ports, probes/health checks, Service, Ingress/Gateway, Secret/Config references, and staging-versus-production differences, marking unavailable details as unknown. |
| `does_not_overclaim_missing_evidence` | PASS | The with_skill evidence consistently distinguishes confirmed statements from unknown runtime, permission, and configuration evidence. It states that a documented domain or existing Service does not prove endpoint health or access-control completeness, and makes no unsupported deployment-readiness claim. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=3b63fba877fb7f6fe67dc804267e58c70b5a122b4297276792467b1f4f923a4f; snapshot_sha256=7927398aeb8e9b6dfd5b3371dca8231a57bc74fb7c438d460283cce69092b485
- Behavior: Produced a read-only environment audit covering all requested entry points and configuration surfaces, with missing evidence explicitly marked unknown.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=f866af3ed882773fac54a605b0b4a3e510672461acab3364eea75d6e24a70d17; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a cautious prose-only baseline audit with broad unknown handling but no delivered audit file.
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

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | with_skill 的交付报告覆盖 staging/production 的 Public/Internal 四个变体，并分别记录 DNS/TLS、认证及网络限制；缺失项明确标为 unknown。 |
| `audits_runtime_environment_differences` | PASS | 报告矩阵逐项覆盖端口、探针、Service/Ingress/Gateway、secret/config 引用及环境差异，并将未提供的精确值标为 unknown。 |
| `does_not_overclaim_missing_evidence` | FAIL | 报告正确将 DNS 解析、证书、探针、认证策略和运行时权限等缺失证据标为 unknown，并说明域名文档不足以证明运行状态；但未将已落地验证事实交由 formal-docs-sync，反而建议下一步运行 deployment-planner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=29b0ab8e9589df053d8ff5163522e5da34e4e689d42e5304f0a19cdeaedb8f08; snapshot_sha256=cefba4cc7ebbe9ee1eef9522af3003ec5b3f68b2e539f4bdf68cd920e48a509d
- Behavior: 交付了覆盖四个环境/入口变体的审计报告，详细标记证据边界与 unknown，但遗漏 formal-docs-sync 交接要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=39ff687a8657d3441a795ea1d94521b85f881c6032d1031e2f29a62f320be822; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了基础只读审计并谨慎标记缺失证据，但未交付审计文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足将落地验证事实交 formal-docs-sync 的要求。
- Next: 补充 formal-docs-sync 交接边界，并仅交付已由运行时或文档证据验证的事实。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | with_skill 逐一覆盖 Staging/Production 的 Public 与 Internal；Public 列出 DNS/TLS，Internal 列出认证/网络限制及 unknown 状态。 |
| `audits_runtime_environment_differences` | PASS | with_skill 表格逐环境覆盖端口、Probe、Service、Ingress/Gateway、Secret/Config 引用，并记录 staging/production 的端口和值存在差异但具体值未知。 |
| `does_not_overclaim_missing_evidence` | PASS | with_skill 对无法检查的证书、探针、认证策略、配置引用等明确标为 unknown，并明确文档声明不能证明完整部署就绪性或集成事实；未将可达性或域名当作集成证明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=05e4b3fff00db219be2c8ff6db171117b525f4ae51e86526373be77f0b9fc3a7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以只读方式逐环境、逐字段审计入口状态，明确区分文档声明与未知运行时证据，且报告未发生写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=6b4a044708d6bac082bacdb29be42b145db161544dde7779f9971044c570cc5e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 覆盖了主要入口和缺失证据，但运行时字段与 Secret/Config 引用的逐项覆盖较不完整。
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

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With_skill 分别覆盖了 staging/production 的 Public 与 Internal，并对 DNS、TLS、认证和网络限制列出已有证据或 unknown。 |
| `audits_runtime_environment_differences` | FAIL | With_skill 覆盖端口、探针、Service/Ingress、配置/Secret 引用及 staging/production 差异，但未明确核对或记录 Gateway values。 |
| `does_not_overclaim_missing_evidence` | PASS | With_skill 明确仅有 fixture 文档、没有独立运行时配置证据，并将无法验证的 DNS/TLS、探针、认证、网络、端口和引用记录为未知，未把文档声明推断为运行时事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=7c350d25c06076f923be90f2b845d7d82ef9d0b1362ec5917d3ef3b9fdd3ae1d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读审计，覆盖四个入口并谨慎区分文档声明与独立运行时证据，但遗漏 Gateway values。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=bd40cdcb9dbeba3f5e11fbdc5d5d854d3e8eb1869eba445f98ff723b47c0bc21; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 覆盖主要入口和部分未知项，但将 fixture 中的配置声明表述为已配置，证据边界较弱。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未覆盖 assertion audits_runtime_environment_differences 要求中的 Gateway values。
- Next: 补充 staging/production 各入口的 Gateway values 证据或明确记录其为 unknown。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `672542b4c547ee15b5007c81b95d14b5fa65c727675122bbb5a233f553fe8ae7`
- Skill overlay SHA-256: `de10ec2dd3547ee5b7a57196d7f9e6584e3ffbd9e717a8e1c8e3b5506cd96520`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With-skill output covers Public and Internal for both staging and production, identifying DNS/TLS, authentication, network restriction, and unknown states where evidence is missing. |
| `audits_runtime_environment_differences` | FAIL | It covers ports/values, probes, Service, and Ingress, but does not address Gateway values or secret/config references. |
| `does_not_overclaim_missing_evidence` | FAIL | It correctly records unknowns and avoids inferring that missing authentication evidence means authentication is absent, but does not state that reachable endpoints or documented domains cannot prove integration, nor route landed validation facts to formal-docs-sync. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=d8c08b89e26552a7b719bff5f003c00bf742169538ba8f62c654b3f95f0da293; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a structured four-entry audit, distinguishes document claims from runtime evidence, and records missing evidence as unknown; it omits several explicitly required audit and handoff constraints.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=c87ff95f61a8cb78742c6155ac60495483a42ca9500299e7da5e112990fa1c60; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Broadly audits the four entry points and records unknowns, but similarly omits Gateway/secret-config checks and the endpoint/integration and formal-docs-sync constraints.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits Gateway values and secret/config references.
- The with_skill output omits the rule that reachable endpoints or documented domains do not prove integration and the formal-docs-sync handoff constraint.
- Next: Add explicit checks or unknowns for Gateway values and secret/config references.
- Next: State that endpoint/domain reachability is not integration proof and route only landed validation facts to formal-docs-sync.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218` from `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`.
- Fixture SHA-256: `2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218`
- Prompt SHA-256: `d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e8fed3827f899b24fa32a7e47350d1b61d93c36648369ee6fefd2624963c060`
- Metadata SHA-256: `3f77718e244c5e457dcf111e54d39609c8dbea3f2bea11e11380c41c91504669`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `audits_public_and_internal_access` | PASS | With-skill output covers Staging/Production Public and Internal, addressing DNS/TLS for Public and authentication/network controls for Internal while marking unverifiable details unknown. |
| `audits_runtime_environment_differences` | FAIL | It covers ports, probes, Service/Ingress, values, and staging/production differences, but does not address Gateway values or secret/config references. |
| `does_not_overclaim_missing_evidence` | FAIL | It correctly marks missing runtime evidence unknown and avoids treating a documented domain as proof, but does not state that verified facts should be handed to formal-docs-sync. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=f8996466543df3d61c8bba9898f30925419d8d03cbef4bb0001a8decd6cba68b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Systematically covers all four entry categories, distinguishes document claims from runtime evidence, and identifies unknowns; it still omits Gateway, secret/config references, and the required formal-docs-sync handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d0a4d782a855fc779a0b6ac4bae5494cbfe62706b00fe098bafa54a0f2523712; fixture_sha256=2af9780db4417e1c98550fa0f1ac701b6027949cee7ad798872f862a34631218; output_sha256=ed8724f3c94dcf934f57fcd8b6fd5b9ff5242f49f0ad9ad02ea55afe5551f2ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides broad read-only coverage and cautious evidence qualification, but omits the explicit formal-docs-sync handoff and also lacks Gateway and secret/config-reference coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not cover Gateway values or secret/config references.
- The with-skill output does not specify handing only landing/verification facts to formal-docs-sync.
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

# Eval Result: eval-004-docs-entry-access-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-004-docs-entry-access-audit`
- Test case: `docs-entry-access-audit`
- Workspace: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/evals/workspace/eval-004-docs-entry-access-audit/eval_metadata.json`
- Expected output: 逐环境报告 DNS/TLS、认证或网络限制、端口、探针、Ingress/Gateway、配置引用与未知项。
- Fixture: `evidence.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `audits_public_and_internal_access` | PASS | PASS | with_skill 逐行列出 Staging/Production 的 Public/Internal；Public 覆盖 DNS/TLS，Internal 覆盖认证与网络限制，并对缺失项标记 unknown。 |
| `audits_runtime_environment_differences` | PASS | FAIL | with_skill 覆盖探针、Service/Ingress、端口和值、staging/production 差异，并明确四个入口缺少 secret/config 引用证据；without_skill 未实际核对或明确记录 secret/config 引用。 |
| `does_not_overclaim_missing_evidence` | PASS | PASS | 两条 lane 均将不可检查的生产 TLS、探针、认证等标为 unknown，且明确域名或 Service 不足以证明安全/集成；with_skill 未声称已完成 formal-docs-sync。 |

## With-Skill Behavior

- with_skill 的三项断言均有实际、可评估证据，故行为 PASS、Coverage FULL，按 binding_result_model durable Overall 为 PASS。without_skill 作为对照在 secret/config 引用核对上缺失，判 baseline FAIL，但不影响 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
