# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-003-third-party`.
- Identity schema: `2`
- target_skill_sha256: `2d9aa34423715a24783169e774af3c68a95cbc320b5fc5af4b5753bd7785f2a0`
- eval_definition_sha256: `fde37322a972618cf8b85d5463c8e7a856c7547f8c15123669fd15297f556852`
- metadata_sha256: `2bb39446486b68c792ab91df36f237757842e6cc3f736b5a421d1cc25cf91455`
- fixture_sha256: `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2eea2d31331dfff7d98326573b856ca9f269bca068d5f182bf99e8b0d5d75219`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 的锁定报告逐项列出三类服务接收字段、个人数据类型、sendUserEvent 触发入口及处理目的，并有代码字段映射。 |
| `sharing_and_retention` | PASS | with_skill 报告识别了三家第三方及 US/未配置地域、730/2555 天和未配置保留期，区分了删除 API 配置与实际删除编排，并说明配置不等同于运行时证据。 |
| `user_rights` | PASS | with_skill 报告检查了同意/退出、访问、删除、导出/可携带和更正，明确指出未发现入口或第三方权利请求传播；同时区分 ExampleAnalytics 无删除 API 与 ExamplePay 有 API 但无调用。 |
| `compliance_gaps` | PASS | with_skill 报告给出了按风险和责任方组织的整改建议，覆盖同意控制、字段最小化、地域/跨境、保留删除、权利请求编排及运行证据验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=fd7498a8b00746f292901acec04c9ac2b914677a11e172207e0724bec1c9219e; snapshot_sha256=84bf85e6360eece4f445f5d3117990226fcaa108b7c274bb0d9b3a458395c84e
- Behavior: 完成并交付结构化隐私处理面报告，覆盖数据清单、共享与保留、用户权利、风险和整改建议；未修改代码或正式文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=7c39094e69da1657afc869a50a410d570e3a2c67fdca3eba258ea8b8a4646437; snapshot_sha256=c7d37fac447c089c01c44b745d0b03b20eb9d55826f09b7dbb83e82b4914919b
- Behavior: 同样交付了结构化第三方共享报告并覆盖主要结论，作为基线比较；其表现不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 PM 对高风险整改进行分类，再交应用工程和平台工程处理。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
