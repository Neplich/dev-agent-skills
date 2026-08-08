# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出声称命中 change-map 后读取了 API 文档，但锁定原始证据无法证明读取顺序。 |
| `verifies_against_code` | PASS | 明确以 `src/session/config.txt` 的 30 分钟配置为依据，指出 API 文档的 60 分钟冲突，并将其作为需澄清的阻塞项，而非盲信文档。 |
| `treats_unverified_as_low_trust` | PASS | 明确指出 `last_verified_version: unverified`、将文档视为低可信，并依据配置文件作出 30 分钟判断；未在缺少运行时/测试证据时声称已验证真实行为。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=cea0e64278f28118305a8fe3376b8cad8e22a5b3ead9db14871661a1ba357a33; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了配置与文档的超时冲突，将未验证文档降为低可信，并停止于缺少实现/测试及规划文档的阶段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=528ea41312a82628025d7736c78e6255a7912e344b4993ea7693831c6d130ee5; snapshot_sha256=710fd6f9b773bd8e68cd27cdfdf00e2bfd5fea133f961dabad4c886605dcbb6c
- Behavior: 直接修改配置和文档以启用续期，但未展示先读取映射文档或基于代码核证的过程证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需判定映射文档读取顺序，应提供可证明该顺序的原始过程证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `664333a5486cf89713133cd2c13950492425453ded41d03d80fa464888580510`
- Skill overlay SHA-256: `e3882775ef1e3496d2f149c4016d8d04e22a586399acb4fdc6095b11e8f7c7bf`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 返回 PM/Engineer 确认 PRD、TRD 及 handoff packet，并明确当前门禁禁止仓库检查；锁定证据无法证明 change-map 读取顺序。 |
| `verifies_against_code` | NOT_EXERCISED | with_skill 明确表示需确认文档后才会核对 src/session/config.txt；该后续步骤尚未发生，不能据此判 FAIL。 |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | with_skill 尚未进入文档或代码核证阶段；锁定证据无法证明其如何处理 unverified 文档或验证关键判断。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=c6a67653b1309169743fd9fee3597dc7e1ee49b8bef6015ac1e64998db8e3668; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按门禁返回 PM/Engineer 进行需求确认，未修改仓库；代码核证及后续实施步骤尚未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=249475be924565018683141f82c5ce2ea6ebb7b06c7cf19dce9f7bc18fdfcb98; snapshot_sha256=f033746e63cf2fcd21a0130d42a9f5a51d94534346bc91c1a85efdbb4535791f
- Behavior: 完成了会话续期实现并交付文件；但其交付证据不证明所要求的文档读取顺序。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供所需 PM/Engineer 确认材料后，再核对 change-map、文档与 src/session/config.txt。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `34bb246c41505d261f20b6762e5f8c167260c9def318e938b2f40cd562a05376`
- Skill overlay SHA-256: `b58ba61aee19f19d841deeba69a31e4991e1e48601dbae26ffb264815cffa67d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出表明命中了 change-map 并读取了映射文档，但锁定证据无法证明实际读取顺序或未遍历全库。 |
| `verifies_against_code` | PASS | 明确以 src/session/config.txt 核实 30 分钟和续期禁用，并指出 API 文档错误写为 60 分钟；同时将超时与续期规则不一致列为影响，未盲信文档。 |
| `treats_unverified_as_low_trust` | PASS | 针对 unverified 文档回到代码核实关键现状，并将续期触发、延长时长、绝对上限及过期错误行为标记为未定义，要求先完成规格对齐后再实施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=ccfdc0476883eecdafe3851027d3a474293367ea4508d7385859824f09363f88; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只读核对映射、代码和文档，识别 30/60 分钟及续期规则差异，并因缺少规格文档而阻止计划和编码；无工作区修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=3925bd387d05904bed107c70e0cbb80083e0749ee842fe12d627bdb1d0771d83; snapshot_sha256=ce11c696e1ca41c0ef5089976370a140a896da4bced2d7132b0b38a70d0afafe
- Behavior: 直接修改配置和文档，修正 30/60 分钟差异并启用续期，但证据无法证明遵循映射文档优先或未验证文档低信任流程。
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

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出和锁定原始证据能证明映射文档、代码和结果存在，但不能证明读取顺序或未进行全库遍历。 |
| `verifies_against_code` | PASS | with_skill 输出明确核对了 src/session/config.txt 的 30 分钟配置，识别文档的 60 分钟错误，并据此更新文档和启用续期。 |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | 结果体现未盲信文档并以配置核证，但锁定证据不能证明对 unverified 元数据的具体信任处理过程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=263126995657e2b65cc69f76e7223279303fc71db60a277db3f20fa070c0a49c; snapshot_sha256=412df339352c504f00530a5702c26aebb765fc5e5c11a7deacde7fff6ebe8114
- Behavior: 正确核证当前超时、识别文档分歧，并完成续期配置和文档更新；读取顺序及最低信任处理过程无法由证据确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=c43c14d3b20f20940c66d5e71504625f482c0543e4f8cced4c686ca9cd221200; snapshot_sha256=52e3e3438ada9b6a49b744c06d88d5e77532f6ad089ebfe0502131e59463cbad
- Behavior: 同样核对出 30 分钟代码配置与 60 分钟文档分歧，并完成续期配置和文档更新；仅作比较基线。
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

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 输出与原始证据未证明先读取 change-map 命中的 docs/site/api/session.md，也未证明未进行全库文档遍历。 |
| `verifies_against_code` | PASS | with_skill 输出明确核对 src/session/config.txt 得出 30 分钟，并识别文档错误写为 60 分钟；交付快照显示文档改为引用该配置。 |
| `treats_unverified_as_low_trust` | FAIL | 虽然识别了文档与代码的冲突，但新增 renewal_window_minutes: 5 及其行为没有代码或测试证据支持，且仓库声明没有可运行测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=e8669836981a8e4b768a571ba64eda558e6e2b86779997cfe7aa21d36912be83; snapshot_sha256=37e90663c1c1051e61fad3d4fa3017c1a65ce2d4c0ae6b4724dac8767525a76c
- Behavior: 核对了代码中的 30 分钟超时并修正文档，但引入了未经代码或测试验证的 5 分钟续期窗口；读取映射文档的顺序未被证明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=588f6fad1b1877dd022afb3b1f1f7c40f86a50af1ed103450337bc1498ddad91; snapshot_sha256=ea337742104de433e29d2f54f5e9d584f1168f2aead1819fce34386844df7735
- Behavior: 识别了 30/60 分钟分歧并启用续期，但未提供读取顺序、change-map 使用或未验证文档信任处理的证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 引入未经验证的 renewal_window_minutes: 5，违反对 unverified 文档按最低信任处理并回代码或测试验证关键判断的要求。
- Next: 补充读取轨迹或等价证据以验证 change-map 命中文档的优先读取顺序。
- Next: 在代码或测试中验证续期窗口后再引入 5 分钟配置。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | With-skill output and raw evidence show the mapped document and config, but provide no access/order trace proving the change-map was used first or that full-document traversal was avoided. |
| `verifies_against_code` | FAIL | The 30-minute config value and 60-minute document discrepancy are reflected in the output and diff, but there is no plan or evidence that the discrepancy's impact was incorporated into a plan. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | The output resolves the 60-minute documentation discrepancy in favor of the 30-minute config and notes no test framework, but does not establish that unverified documentation was explicitly treated as lowest trust or that all scope judgments were verified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=e1f90c50ec385dd13119d5a5870340d5184e469277b163d5255b69dd575b89d7; snapshot_sha256=b1fbfc1f2d9143b1a8ccf4d98655cc1caec58885595501f78c84379c331a8897
- Behavior: Implemented renewal, reconciled the documentation to the 30-minute config, and reported consistency validation; process assertions are not fully evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=588f64a9e4d36b2c94eee5d94487bf33f9911c503ce75f3450a7c533f47f3c16; snapshot_sha256=0c4505e88fc23552662559dd8d2ca97f6f7d01e3dc764b584f56418a23d875d2
- Behavior: Implemented the same config and documentation changes, without evidence of mapped-document-first review or trust handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_against_code is not fully satisfied because the discrepancy was corrected but its impact was not shown as incorporated into a plan.なく
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

# Eval Result: eval-014-mapped-session-plan-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`
- Test case: mapped-session-plan-evidence
- Workspace: `workspace/eval-014-mapped-session-plan-evidence`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/session/` 增加会话续期，并先核对当前超时行为。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: Transcript item_4 reads change-map.yaml, then mapped docs/site/api/session.md and src/session/config.txt; no full site-document traversal is evidenced.
- PASS `verifies_against_code`: Transcript and final identify config.txt as 30 minutes with renewal disabled, contrast it with the document's 60 minutes, and retain the conflict as an implementation blocker. With-skill workspace hashes match input hashes.
- PASS `treats_unverified_as_low_trust`: Both mapping and API documents state last_verified_version: unverified; the agent relies on config/code evidence, reports the discrepancy, and does not implement based on the document alone.

## With Skill Behavior

按映射读取 API 文档并回读代码配置，识别 30/60 分钟冲突；因缺少 PM/TRD 链未实施或写入计划。workspace 未变更，hash 与输入一致。

## Without Skill Baseline

未使用映射消费协议，直接修改 config.txt 与 API 文档，启用 renewal 并统一为 30 分钟；output hash 反映两文件变更。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实（30 分钟、续期禁用）核证出文档 60 分钟声明的分歧，PRD/TRD 前置门禁正确触发暂停，未在预期未对齐时编写实施计划。

## With-Skill Behavior

- 命中映射文档后回代码核证会话行为，结构化区分代码事实与文档声明。
- 变更按 standard 分级，正确停在 PM → trd-gen → 实施计划的协作链前置，未越权编码。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样停在门禁前请求预期确认，行为合规但对文档分歧的证据组织与契约引用较弱。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
