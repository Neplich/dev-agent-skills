# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `9482baaf8c9e8ed2c6d5d65dd72ca668fb6cc639dacfe10c14d42e2f2d0f4c53`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | With-skill output separately covers Linear and Jira positioning, target users, and core selling points in sections 2–4 and the comparison matrix. |
| `messaging_gap` | PASS | With-skill output identifies five explicit messaging gaps plus concrete content opportunities in sections 6–7. |
| `evidence_boundary` | PASS | With-skill output explicitly distinguishes category-level opportunity analysis, judgment-based weaknesses, public facts, and items requiring price verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4a08efe07d313da50417d9ae8b7dc4b8c402ce46b94b60ff18392de7f6c67297; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a structured Linear-versus-Jira competitive brief covering positioning, users, selling points, messaging gaps, content opportunities, and evidence qualifications.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9e067866ab87b79bc38902e6c76e95cf800dcfd8ede63c7bb27b48f5dd946b47; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also delivered a complete competitive brief with positioning, users, selling points, and messaging gaps, but used less explicit evidence-boundary qualification.
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

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | 分别说明了 Linear 与 Jira 的定位、主要/典型用户、核心承诺和关键卖点。 |
| `messaging_gap` | PASS | 识别并展开了多个 messaging gap，包括跨职能协作、执行者与管理者兼顾、项目上下文、外部协作和低维护成本。 |
| `evidence_boundary` | PASS | 明确说明我方产品定位未提供，相关切入机会需结合能力收敛；对用户反馈和痛点也标注了来源或建议进一步访谈验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=498223423d1f4dcac8e46c9d2889f04b56192804dfaf9956521dbdb0c64da824; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了更系统的 Linear/Jira 竞品 brief，覆盖定位、用户、卖点、差异、多个 messaging gap，并包含来源、假设说明和验证建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=80877a9c3d0ff9a960d74a08e9b66201e1a9ac5f73fd10984ca56f42981882f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了定位、目标用户、卖点及 messaging gap 分析，并对部分推断标注了验证边界。
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

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | with_skill 输出分别覆盖 Linear 和 Jira 的定位、主要/典型用户、核心价值与关键卖点，并提供对比矩阵和竞品画像。 |
| `messaging_gap` | PASS | with_skill 明确识别跨职能协作、决策上下文、易用性与治理、AI 共识辅助、项目叙事等 messaging/content gaps，并给出具体切入表达与行动建议。 |
| `evidence_boundary` | PASS | with_skill 明确说明未提供自家产品定位，并将“我们”的分析标为策略假设；竞品事实以归因和来源链接呈现，未将自家产品未知信息伪装成确定事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5add1fc00b3a0d32d5d1c54d40b9b345b05055bab5f8a3c2bd06383f55257d96; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整覆盖定位、目标用户、卖点和 messaging gap，并明确区分自家产品假设与带来源的竞品信息。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a761b88e188c3f3ae3fc20ac69af5343eff2aef7c864dbd39100f016db0f29ac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 内容覆盖三项主题，但未明确标注“我们”的产品定位是假设，证据边界相对较弱。
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

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | 分别覆盖了 Linear 和 Jira 的定位、目标用户、购买者/组织阶段及核心卖点。 |
| `messaging_gap` | PASS | 明确提出多个可切入的 messaging gap，包括易用性与治理平衡、跨职能协作、决策可见性、AI 差异化和渐进式迁移。 |
| `evidence_boundary` | FAIL | 部分关于 2026 年产品能力、第三方评论和竞品弱点的具体断言以确定语气呈现，引用仅为不可核验的内部 citation 标记，未充分标注为假设或待验证信息。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8d266118653f31f5e5c1bda57940baa9f1328f894f8a55d261eb116cc412eb8f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 结构化且深入覆盖竞品定位、用户、卖点和多个 messaging gap，但证据边界处理不足，包含不可核验引用和未充分限定的事实断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3f5c39ac78859b59b7e3b18139a6eb023d35eca6289c1e61978a304d1ff107f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 内容完整覆盖定位、用户、卖点和 messaging gap，并提供可访问的公开链接，结尾也明确建议通过用户访谈验证假设。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出对部分无法从锁定原始证据确认的当前产品能力、第三方评论和竞品弱点作确定性陈述。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f050f17a1dbf3e48425b707abdd9557be859b400a83ed4439f082d737e9f50e7`
- Skill overlay SHA-256: `f7c1d1bd37dbecccce69473aa024a7dbd7ecb928c80497054513ac2ccbdb41d1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | With-skill output separately states Linear and Jira positioning, target users, and core selling points in the comparison and dedicated sections. |
| `messaging_gap` | PASS | With-skill output identifies multiple concrete gaps, including outcome focus, cross-functional collaboration, lower maintenance, decision context, and the simplicity/governance balance. |
| `evidence_boundary` | PASS | With-skill output explicitly notes that the messaging gaps are provisional because the user's product positioning was not provided, and conditions recommendations on actual product capabilities. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ced4f4aba53c9958a49e88d5b73981b46cacd34bd7e5eb857dd045b2e17ef5bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides comprehensive positioning, target-user, selling-point, messaging-gap, and assumption-boundary coverage.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b14570c5122c4190e54ea8e13d88f07597365dacc46f413b45eb434b039e7f85; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides strong positioning and messaging-gap analysis, but gives less explicit qualification of assumptions.
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

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9bcbaea9ed44a65b8b7c8fe2503291ec2b4f93690b7975aa2c81cb08e3724567`
- Skill overlay SHA-256: `e16b71c2700d685342e052804fd5eb5278935b75eddc6e749594182c8bc24969`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | With_skill 明确分别说明 Linear 与 Jira 的核心定位、首要用户、核心购买者、使用场景、产品哲学和关键卖点。 |
| `messaging_gap` | PASS | With_skill 单独列出 5 个 messaging gap，并为每项提供可切入的 messaging，例如从追踪工作到推动结果、跨职能协作和简单体验与企业治理之间的中间地带。 |
| `evidence_boundary` | PASS | With_skill 明确说明未提供“我们”的产品背景并声明分析假设；对薄弱点标注为“基于产品叙事和公开功能结构的判断”，并指出需避免将推断当作绝对能力缺陷。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=320428a532ca6374a39ad2981cef9e3752c787e2e811a7a3c4fea4c7a70c599e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 系统覆盖定位、目标用户、卖点和多个 messaging gap，并明确区分公开信息、假设与基于叙事的判断。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=57664f7642719ed550403c109e16a22511718d9b134dba54420a7d3035f09103; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 内容完整覆盖竞品定位、用户、卖点和 messaging gap，但证据边界标注相对较少。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-001-positioning-gap-brief

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Isolation: the fresh baseline completed before any with-skill root was created; the judge ran in a third independent root.
- Behavior result: PASS — 3/3 defined assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `positioning`: PASS — covered Linear and Jira positioning, target users, and core selling points.
- `messaging_gap`: PASS — identified concrete unclaimed messaging and content opportunities.
- `evidence_boundary`: PASS — cited sources, qualified weak evidence, and marked product-context-dependent conclusions for validation.

### With-Skill / Baseline Comparison

The with-skill lane produced a complete positioning brief using fresh web research. The baseline also produced a useful brief and passed the broad assertions, so this eval continues to show low behavioral differentiation.

### Failures / Next Steps

- No with-skill assertion failures or coverage gaps.
- The broad assertions remain a lifecycle signal: baseline already covers most of this behavior.

### Runtime Artifact Policy

- Fresh web traces, candidate output, manifests, and verdict remain under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-positioning-gap-brief/` and are not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`
- Test case: positioning-gap-brief
- Workspace: `workspace/eval-001-positioning-gap-brief`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Historical result: PASS

## Review Context

- Date: 2026-08-03（issue #188 A 维删除后 paired 回归）
- 变更：Analysis Frameworks 节已删除（L3 A 维实测确认磨平），新增 Battlecard Mode 条件模式
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-regress/judge/verdict-paired.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: live 联网研究（Linear 与 Jira 官方公开页面），无静态 fixture
- With-skill evidence: `tmp/eval-runs/issue-188-regress/with_skill/competitive-brief-eval-001/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-188-regress/without_skill/competitive-brief-eval-001/candidate-output.md`

## Assertions

- PASS `positioning`：分别说明 Linear 与 Jira 的定位、目标用户和核心卖点；without-skill 同 PASS
- PASS `messaging_gap`：识别线性/强治理之间的 messaging gap 并提出可切入机会；without-skill 同 PASS
- PASS `evidence_boundary`：区分官方事实与策略推断，无法确认信息标记为假设；without-skill 同 PASS

## With Skill Behavior

- 删除 Analysis Frameworks 后仍产出完整 brief：定位、卖点、messaging gap、机会/威胁/行动项，并保留证据边界；Battlecard Mode 在 pm-agent `battlecard` 信号路由时直接产出单页 battlecard（不输出完整 brief）。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt，未读 skill）；3/3 assertions PASS。
- 原断言双侧零区分（baseline 已内化定位/gap/证据边界分析）；skill 增量在扩展内容（近期动态、机会、威胁、行动项）与 Battlecard Mode，删除后无行为回归。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 零区分度观察：原 3 条断言被 baseline 全部白捡，与 #188 删除决策一致（已删内容正是 baseline 内化的框架知识）；剩余增量不在本 eval 断言范围。

## Historical Results

- 2026-07-26（删除前）：PASS（3/3 assertions，fresh same-agent judge；双侧均满足，with-skill 对事实/推断边界更系统）。该轮基于删除前 skill 内容，仅作历史记录。

## Next Steps

- 删除后后续修改 competitive-brief 时重新运行本 eval。
- 原断言已无区分度；后续评估可考虑把断言钉在 skill 特有增量（Battlecard Mode 产物、扩展结构）上。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-regress/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
