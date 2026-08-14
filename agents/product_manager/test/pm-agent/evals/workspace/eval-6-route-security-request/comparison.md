# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-006-route-security-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-6-route-security-request`.
- Identity schema: `2`
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `b4ceb7c82713552e98022f642658a9fe01923ce2aef9cd904f9b3ce6b9d57837`
- metadata_sha256: `b68604b9408ecd1ae4f680e8b6bea0f1c221e273dc6389c6b8150eff4b36f0d2`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `356a8438fe026d0b1352a3ef7467cbb1d1fa3bb6c089f0c3e64b4d4c5d3741fc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_security` | PASS | with_skill 输出明确写出 `request_type: security`。 |
| `security_scope_first` | NOT_EXERCISED | with_skill 输出包含 risk_surface、assets、permissions、data_flow 和 remediation_expectations；但锁定证据无法证明这些内容是在其他审查动作之前记录的。 |
| `security_handoff` | NOT_EXERCISED | with_skill 输出选择 Security 并携带 scope 与 required_output，但 security-agent 未安装，实际后续 handoff 尚未发生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a25b0b66ade22bee6ea3f3b408b43ce95d9676a3a81a63686c44cbcd9d50ebff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成 security 分类并输出包含安全范围、阻断项和 Security 交接信息的结构化路由包；实际交接因缺少 security-agent 尚未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=36e2dc52efc02bd4a536346d8f3cd5d27459a1a97e6287cf5969afca708442f1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=817a7bef646d9a51098acf16f7e7d179c4b7a522306090bda56ca9b1f90be45a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别工作区为空并给出一般性安全检查建议，但未进行 security 分类或结构化 Security handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装或启用 security-agent 后完成 Security handoff。
- Next: 补充运行时证据以验证范围记录确实先于后续审查动作。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
