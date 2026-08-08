# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- Skill overlay SHA-256: `c7fd56e26e53c8ea32b598e8f4e06588e28aee376ed79eb9822ecf37e3099222`
- Judge schema SHA-256: `6731c51ff9f69981e5ade0a40fa5fb4f93b6c439e428212a1b46155c6fa123f1`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | NOT_EXERCISED | With_skill output only identifies the workspace and requests confirmation; no feature-catalog draft is produced yet. |
| `evidence_and_confidence` | NOT_EXERCISED | No candidate feature entries have been produced yet. |
| `business_capability_naming` | NOT_EXERCISED | No candidate feature entries have been produced yet. |
| `open_questions_present` | NOT_EXERCISED | No catalog analysis has been produced yet. |
| `confirmation_gate` | NOT_EXERCISED | The candidate requests workspace confirmation before proceeding; feature_path confirmation and handoff are therefore not yet exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=1919a3baa736681f811784c19273e37c3f2f43c7c1b51721df4d6b2ed289fa15; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Safely paused at the workspace-confirmation gate without creating files or claiming an unperformed catalog analysis.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=4a93b2b52e5b4c166d3678edabbed6d6166412c8e442e092908e74fa5f9553d8; snapshot_sha256=1ca0506bfcd12ecc19a5810077bedbf8c7bb742e656b2f0b02b41c7250117624
- Behavior: Produced a formal catalog at docs/feature-catalog.md without the required confirmation-gated draft workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the identified project root so the feature catalog can be drafted and evaluated.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- Skill overlay SHA-256: `c7fd56e26e53c8ea32b598e8f4e06588e28aee376ed79eb9822ecf37e3099222`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | NOT_EXERCISED | with_skill 先请求确认项目范围，尚未进入输出功能目录草案的步骤；其 git 状态显示未发生写入。 |
| `evidence_and_confidence` | NOT_EXERCISED | 尚未生成候选功能条目，因此无法评估证据分类和置信度。 |
| `business_capability_naming` | NOT_EXERCISED | 尚未生成候选功能目录。 |
| `open_questions_present` | NOT_EXERCISED | 尚未进入功能归属或边界分析步骤。 |
| `confirmation_gate` | NOT_EXERCISED | with_skill 已执行项目范围确认，但尚未生成包含 feature_path 的目录并收尾确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=cbba5bd183528e3c073845a697b640037b65baf2d2314fe8c44f8eacfa61ed30; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在梳理前先确认项目范围，未产生文件或其他 git 变更；后续目录流程尚待用户确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=efdf927183c352316f1f1c6070d2daaff8058fc0edb3143b2c36361d9e958e9c; snapshot_sha256=55cfd6622c133dfa78d4204a55f7e277982367b0e2e0446b5e7c444e1e1c69b8
- Behavior: 直接生成并写入了功能目录文件，内容较完整但未遵守草案/确认门禁要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 用户确认项目范围后，再生成待确认的功能目录草案并请求确认 feature_path。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e4cd9b0e262233f5d6a944962f6bf7c4c1323776752d0c1e41ea8bac4c33f829`
- Skill overlay SHA-256: `3f39f62240fb387c41fff7ebe0f42bb66e13cd2eda97d0b2c78636c06bb45d87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | With-skill 输出明确标记为“功能目录草案（待维护者确认）”；git_status、git_diff 和 delivery_snapshot 均显示未创建或修改正式文档。 |
| `evidence_and_confidence` | PASS | 每个候选功能均有 low 置信度，并按实际相关类别提供 routes/API、services、data_models、background_jobs、tests、docs 等证据；缺失类别也明确标注未发现。 |
| `business_capability_naming` | PASS | 功能按用户可理解的业务能力命名为客户登录与会话管理、订单创建与订单查询、订单状态通知，代码路径仅作为证据或关联路径出现。 |
| `open_questions_present` | PASS | 订单状态通知条目明确记录其是否应归入 order-management 子功能这一开放问题，并说明当前实现仅为任务骨架。 |
| `confirmation_gate` | PASS | 输出以请维护者确认各 feature_path 及订单状态通知归属收尾，并说明确认后才写入正式目录；未在确认前 handoff 给 prd-gen 或 trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=948f2d3e607522c2437a471f85e0baa36f7d1ab54a4e2530d4509d0718fe51a3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只输出待确认的功能目录草案，提供业务能力、分类证据、置信度和开放问题，并请求确认 feature_path；工作区保持未修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=9bfadd39a451e69fed0187f0d307f7e2a852736a88bab79941c216f65ae1776b; snapshot_sha256=b6b6f2c3e412698dc5380d6307d1ef454a6d30f363656cf4f34159e83d14b89e
- Behavior: 创建并修改了 README.md 和 docs/功能目录.md，直接交付正式功能文档，未遵守确认前草案门禁。
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
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e4cd9b0e262233f5d6a944962f6bf7c4c1323776752d0c1e41ea8bac4c33f829`
- Skill overlay SHA-256: `3f39f62240fb387c41fff7ebe0f42bb66e13cd2eda97d0b2c78636c06bb45d87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | with_skill 明确输出“待确认的功能目录草案”，并以确认后才写入 docs/pm/FEATURE_CATALOG.md 收尾；git_status 为空且没有 docs/pm 文档变更证据。 |
| `evidence_and_confidence` | PASS | 三个候选条目均有 low 置信度，并提供了与实际仓库类别对应的证据：路由/API、服务、数据模型、测试和后台任务；README 也被列为依据。 |
| `business_capability_naming` | PASS | 条目使用“客户登录与会话续期”“订单创建与查询”“订单状态通知”等业务能力名称；代码目录和路径仅作为关联证据出现。 |
| `open_questions_present` | FAIL | 输出要求确认功能及 feature_path，但没有为归属或边界不确定项明确记录 open questions 或 unresolved 标记；low 置信度不足以替代该要求。 |
| `confirmation_gate` | PASS | 输出以请维护者确认三个功能及路径收尾，并明确确认后才写入正式目录；没有提前交接给 prd-gen 或 trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=83b44f6b4ecec2d92eba9ca24a99486fc3880a595ebe8a826c5015847bd471a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只读输出待确认功能目录草案，使用业务能力命名、置信度和代码证据，并等待维护者确认；未明确记录 open questions/unresolved 边界问题。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=d04a7021968a07b7b4e102e4072dfce825c1ba40ac4f06c1763e760f3475e01b; snapshot_sha256=21b662f6abb6f3e86bf175f2ae788d0ef11f430cd1ef594ae402f6b814a6b9bb
- Behavior: 直接创建了未确认的正式功能目录文档，且未采用确认门禁；内容有功能和代码证据，但不是待确认草案。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确记录归属或边界不确定项的 open questions 或 unresolved 标记。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c7dc67ac03b6fbf2bf69bb7af239cc79636a61220df238e51a6c8f891a2b2bbf`
- Skill overlay SHA-256: `5fabe64a432e7077b010b055323ac846ade69c047e7f21a1ce71459e61d31a42`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | with_skill 明确标记为“功能目录草案（待确认）”，并以 git_status 为空、delivery_snapshot 为空证明未写入正式 docs/pm 文档。 |
| `evidence_and_confidence` | PASS | with_skill 对候选功能提供路由/API、服务、数据模型、后台任务、测试或 README 证据，并声明所有条目置信度为 low；这些类别均与 fixture 中实际存在的文件对应。 |
| `business_capability_naming` | PASS | 功能命名为客户认证、订单管理、下单、订单查询与状态跟踪、订单状态通知；代码路径仅作为证据或关联代码出现。 |
| `open_questions_present` | PASS | with_skill 对认证范围、查询与状态跟踪边界、通知任务真实性及实现状态列出待确认问题。 |
| `confirmation_gate` | PASS | 输出以请确认 feature_path/目录方案收尾，并明确确认后再写入正式 FEATURE_CATALOG.md，未提前 handoff 给 prd-gen 或 trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=5c59ce6b67b64cf190db4b0ccb781eabf0a936eeae3b03a6318e463f9f3777af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 输出待确认的业务能力功能目录草案，提供证据、低置信度和开放问题，且未产生工作区变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=f86abc40c9159b4fbd248e0d2c4958191f9eebe347521139e680f39665bdd4be; snapshot_sha256=9fcb875b83eb25d13fa3d4cea7bb14b61f6f6f57affcd8a20353aa0c4f9b9a2f
- Behavior: 输出了功能盘点并实际新增 docs/功能目录.md，未采用待确认草案门禁。
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
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `807b576a5130a49581d58f258e32f9a7f916850f2f335e3a48ede3a7886a942b`
- Skill overlay SHA-256: `96eaf3768827f13d232245de107b17f5e814bef969da3eb231f62d9287d9d070`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | with_skill 明确标记为“功能目录草案（待确认）”，git_status 和 git_diff 均为空，且输出说明尚无正式 docs/pm 文档。 |
| `evidence_and_confidence` | PASS | 三个候选条目均在总览表中标记 high 置信度，并提供与原始 fixture 相符的 API、路由、服务、数据模型、后台任务、测试或 README 文档证据。 |
| `business_capability_naming` | PASS | 候选名称为“客户身份认证与会话续期”“订单创建与查询”“订单状态变更通知”等业务能力名称；代码路径仅作为证据出现。 |
| `open_questions_present` | PASS | 每个候选条目均包含“待确认问题”，明确指出认证、状态变更、邮件发送、通知记录及重试等未确定或未实现边界。 |
| `confirmation_gate` | PASS | 输出结尾请求维护者确认三个 feature_path，并说明确认后才写入正式目录；未提前 handoff 给 prd-gen 或 trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=4d3eaf70234ac0964a6bd39c1fb4c0dd4ef89428de20110ed256aca210f59dc8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 产出待确认的业务能力功能目录草案，逐项提供证据、置信度和待确认问题，并以 feature_path 确认请求收尾；未产生文件变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=aca860cbc520da14670de2b6fa786b92b66ab0e8ab5a2e195c75c6feab58d851; snapshot_sha256=0538798cb2d752d059e4fc9214534c833817d714e75adb64cdcafc32e31cd466
- Behavior: 输出了未确认的正式目录文件 docs/功能目录.md，未采用待确认草案和 feature_path 确认门禁。
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

# Eval Result: eval-001-legacy-project-catalog

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; baseline and with-skill input manifests matched exactly.
- Isolation: baseline completed and its root was deleted before any with-skill root was created; the judge used a third independent root.
- Behavior result: PASS — 5/5 assertions passed.
- Coverage result: FULL — all 5 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `draft_before_formal_docs`: PASS — produced a visibly pending draft and wrote no formal catalog or PRD.
- `evidence_and_confidence`: PASS — used the actual route/API/service/model/job/test evidence and conservative confidence.
- `business_capability_naming`: PASS — grouped findings into user-facing authentication, order management, and status notification capabilities.
- `open_questions_present`: PASS — recorded unresolved ownership and boundary questions.
- `confirmation_gate`: PASS — stopped at maintainer confirmation before formal docs or handoff.

### With-Skill / Baseline Comparison

The with-skill lane produced an evidence-first, low-confidence draft without durable writes. The baseline wrote `docs/功能目录.md` before confirmation and lacked the same gate discipline.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-legacy-project-catalog/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`
- Workspace: `workspace/eval-001-legacy-project-catalog`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; Node.js commerce backend with no PM docs and shallow-scan evidence for authentication, orders, notifications, model, and tests.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `draft_before_formal_docs`: PASS — produces a visibly pending draft and writes no catalog or PRD.
- `evidence_and_confidence`: PASS — each candidate includes actual evidence categories, related paths, and conservative confidence.
- `business_capability_naming`: PASS — names authentication, order management, and order status notifications as business capabilities.
- `open_questions_present`: PASS — records ownership and boundary uncertainty instead of presenting guesses as facts.
- `confirmation_gate`: PASS — stops with one maintainer confirmation request before formal docs or handoff.

## With-Skill Behavior

The response used the documented lightweight scan because no Project Profile exists, grouped evidence by business capability, capped shallow-scan candidates at low confidence, and stopped before writing `docs/pm/FEATURE_CATALOG.md`. After confirmation, the spec handoff is directly to PRD/DECISIONS and later Engineer TRD; no BRD step remains.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the same broad modules but organized them more mechanically, used inconsistent confidence, and lacked the explicit maintainer confirmation gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected handoff-chain difference, not a regression: confirmed catalog entries now proceed directly to PRD/DECISIONS.

## Next Steps

- Keep this eval as coverage for legacy feature discovery and the BRD-free confirmation-to-spec handoff.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/` and are not committed.
