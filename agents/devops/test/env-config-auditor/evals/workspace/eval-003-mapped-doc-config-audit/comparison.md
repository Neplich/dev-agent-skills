# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Locked evidence contains the intended change-map and required document, but cannot prove the actual read order. |
| `verifies_against_code` | PASS | The delivered report records the document's optional declaration, `required.env`'s `API_TOKEN = required` fact, and the resulting configuration-missing/runtime-enforcement risk without treating the document as authoritative. |
| `treats_unverified_as_low_trust` | PASS | The delivered report explicitly identifies `last_verified_version: unverified` and keeps runtime conclusions unconfirmed absent executable code or tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=bd6eb0c053e7935fcc7f8732a3e7e516199e17de63abdf80fce4a0799acdb52a; snapshot_sha256=f630fdf8ae8cd278990c820b4532b5f09839ed2c4ff59f7476c993cf7bd84f0a
- Behavior: Created a detailed audit report that correctly distinguishes documentation, configuration declaration, and unverified runtime evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=ca7e09d0ee689c3376ad933af1343a391254efd5ac6462ddf89de7ad3111831b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the required-vs-optional drift, but provided only prose and did not create a report artifact.
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
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出确认命中映射并读取 runtime-config.md，但锁定证据无法证明其读取顺序或未遍历无关目录。 |
| `verifies_against_code` | FAIL | 候选输出明确表示尚未执行代码/测试核验，因此未回读 required.env，也未发现代码标记 API_TOKEN 为 required 或记录配置缺失风险。原始 fixture 确实显示该代码规则。 |
| `treats_unverified_as_low_trust` | PASS | 候选输出识别了 last_verified_version: unverified，并将文档视为低信任，且表示关键结论需要代码或测试核证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=bd87557eefcd33618d5d1bd2dcb3635b23787bbb8884a4718cd62dd75e46ff5c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 读取了映射文档并识别其未核证状态，但因自设入口门禁暂停，未核对代码规则。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=20c2381c91e80865e56d5c759c1bd843e131cfc42ceaacf9dfff052cbc7c9647; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接核对映射、正式文档和 required.env，正确识别文档称可选而代码要求必填，并指出文档过时及核验状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成对 src/config/required.env 的代码核验，未给出 API_TOKEN 必填及配置缺失风险结论。
- Next: 回读 src/config/required.env，确认 API_TOKEN=require​​d，并记录文档冲突与配置缺失风险。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `11f5a69db2a4c2ab81d782a866d9a88090a8560b5e61462d8af4e66c4376601f`
- Skill overlay SHA-256: `ce7aff0f7795c878221dac5c9435b88a48e75e2799c5f15832edbd27f5f6796f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定证据能证明读取了 change-map 和 runtime-config.md，但无法证明读取顺序或未遍历无关目录。 |
| `verifies_against_code` | PASS | deploy/ENV_AUDIT.md 直接记录代码中的 API_TOKEN = required、文档称 optional 的冲突，并指出缺少运行时加载器/校验器导致的风险。 |
| `treats_unverified_as_low_trust` | PASS | 报告明确识别文档及 change-map 的 last_verified_version: unverified，并将文档作为导航证据、以代码事实为准。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=311ffc8e21a499acaef1f0652c4795e3c8f0e594ded14369047ade1996713142; snapshot_sha256=628827eae6e2392fa4955568e7baf8044b0d81194068d497a911168e373a490b
- Behavior: 交付了完整审计报告，核对映射文档、代码规则和文档可信度，并保留运行时强制执行未知的边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=3ab6c95c76319bf7dd3c9d1827e98037b331684b7771184fe07e2f0205eff383; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出 API_TOKEN 必填与文档可选的冲突，并建议修正文档；未明确处理 unverified 信任级别。
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
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 读取顺序和是否先命中 change-map 属于隐藏过程，锁定原始证据无法证明。 |
| `verifies_against_code` | FAIL | with_skill 正确记录了代码要求 API_TOKEN 必填及文档称其可选的冲突，但未明确记录 API_TOKEN 缺失会带来的配置风险。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别 last_verified_version: unverified，并以 required.env 的代码规则作为 API_TOKEN 必填结论依据，而非单独采信文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=24ec36c59510849178e1985e9eee439220782c776bf998f7c59b19d47387c4ad; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码与文档冲突及 unverified 状态，但以未提供交接包为由暂停正式审计，且未明确说明配置缺失风险。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=4da3f04dcf6d36bc719306ec296cbe16733328bad0f242c3b609c88eaad34bcc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出 API_TOKEN 必填结论，记录文档冲突，并声称查阅了变更映射。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未记录 API_TOKEN 缺失的配置风险，未完整满足代码核对断言。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a23a5206e5734d346e9cc05988abcd19e92dc09bd52f243173dd300d409a14ca`
- Skill overlay SHA-256: `cf962faf729c051cb7dfd2e1a6a7c8c9a1b7f9b67501cbf18f492cb32a84adc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 最终输出列出了映射文档及正式配置文档，但锁定的原始证据无法证明读取顺序。 |
| `verifies_against_code` | PASS | 明确指出 required.env 将 API_TOKEN 声明为 required，并指出 runtime-config.md 错误声明为 optional，且以当前配置规则判定 API_TOKEN 必填。 |
| `treats_unverified_as_low_trust` | FAIL | 输出将代码规则作为结论依据并说明运行时强制行为未知，但未识别或提及文档元数据 last_verified_version: unverified。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=fe2ff9814180cb60a654e8cd80c07a6a3a0d369b01e164bbf785a20bc52c800c; snapshot_sha256=26c0422e538b08e7f419482503c82aa8aa3064fea2e39228971fb8245f0d75f3
- Behavior: 正确判定 API_TOKEN 必填并记录文档冲突及运行时强制行为未知，但遗漏未核验元数据；另生成了 ENV_AUDIT.md。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=d45354b3a1906f38bf2270100e96e34707d151f59c5462d463c6be78b4a9bdfb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别代码与文档冲突，并提及文档未核验状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 last_verified_version: unverified，未满足按最低信任处理配置文档的明确要求。
- Next: 在审计结论中明确记录相关文档的 last_verified_version 为 unverified，并说明不能仅凭该文档确认配置覆盖完整性。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `672542b4c547ee15b5007c81b95d14b5fa65c727675122bbb5a233f553fe8ae7`
- Skill overlay SHA-256: `de10ec2dd3547ee5b7a57196d7f9e6584e3ffbd9e717a8e1c8e3b5506cd96520`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output identifies the change map and the mapped runtime-config document, with no irrelevant documentation cited. |
| `verifies_against_code` | PASS | It cites required.env showing API_TOKEN = required, contrasts this with the document's optional claim, and treats the code rule as authoritative. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version as unverified and limits the conclusion, noting that actual startup rejection cannot be proven without loader or runtime validation evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=2588871add4deba5a32cfe8b7ef4d56451325e73588826ca5ec08b634fd5b923; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly prioritizes mapped documentation, verifies against required.env, and appropriately treats unverified documentation and runtime enforcement as limited evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=a1f8d1f017d263e8387b03c3ddd3e1c9758a5bf005b8b70c8476968af41e8004; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the code/document conflict but asserts missing API_TOKEN should be rejected without runtime enforcement evidence.
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
- Eval: `eval-003-mapped-doc-config-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5` from `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`.
- Fixture SHA-256: `d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5`
- Prompt SHA-256: `b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `745b306831066bee2a7ff3a7b48abf881c1196cfdb1e28206ff9239f069e955c`
- Metadata SHA-256: `c5eaf2656d7227ecd689bf4922af4f6c541bc3cb4d63375292c5b605d7e8380c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 输出引用了 change-map 和 runtime-config.md，但未提供可验证的读取顺序或目录遍历证据。 |
| `verifies_against_code` | PASS | 明确指出 runtime-config.md 声称 API_TOKEN optional，而 src/config/required.env 标记为 required，并记录了文档与代码不一致及无法证明运行时强制校验的风险。 |
| `treats_unverified_as_low_trust` | PASS | 识别 last_verified_version: unverified，并以代码配置定义作为 API_TOKEN 必填结论依据，没有仅凭文档判定覆盖完整。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=ebabed1d0f513f44960c753cf927acd375e2a938d434c8a91e7379f3920a30d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对映射文档、代码规则和 unverified 元数据，并区分配置定义层要求与运行时强制校验事实。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b79f24622b9644bbd1fa788251bd901e2da05ea7b38df10e90eb31488aa20956; fixture_sha256=d8b594c02acd54c63c782827a944b663d600d50c48ab45d0916be040dcdd3bf5; output_sha256=0c9912ae2a3917d8f33adabcf470bdc675fa33117ac45ddcfd491c9583ebedf1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 API_TOKEN 为代码层面的必填项及文档冲突，但未明确说明无法证明运行时强制校验。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供工具调用或读取轨迹以验证映射文档优先读取及目录遍历范围。

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

# Eval Result: eval-003-mapped-doc-config-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-003-mapped-doc-config-audit`
- Test case: `mapped-doc-config-audit`
- Workspace: `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: FAIL
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: FAIL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/evals/workspace/eval-003-mapped-doc-config-audit/eval_metadata.json`
- Expected output: 区分映射文档声明和代码配置事实的环境审计结论。
- Fixture: `src/config/required.env`, `docs/site/standards/change-map.yaml`, `docs/site/api/runtime-config.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | FAIL | with_skill 的读取命令顺序为 change-map、契约/skill-map、src/config/required.env、runtime-config.md；映射文档并未先于代码读取。without_skill 先读取 required.env，随后才读取文档。 |
| `verifies_against_code` | PASS | PASS | 两条 lane 均读取 required.env，确认 API_TOKEN = required，并识别文档中的 optional 冲突；with_skill 还明确记录了配置缺失风险。 |
| `treats_unverified_as_low_trust` | PASS | FAIL | with_skill 明确识别 last_verified_version: unverified，并以代码事实作为关键结论依据。without_skill 虽读取了该字段，但最终结论未识别或说明其最低信任影响。 |

## With-Skill Behavior

- with_skill 已核对文档与代码并正确判定 API_TOKEN 为必填，也正确处理 unverified；但未满足“先读取映射文档再回读代码”的严格读取顺序，因此 durable Overall 为 FAIL。Coverage 为 FULL。without_skill 作为对照同样未满足首读文档顺序，且未在结论中处理 unverified。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill failures: `reads_mapped_docs_first`。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 按上表 with_skill failure 的共同根因建立后续修复项；本轮只记录结果，不修改 skill、eval 定义或 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
