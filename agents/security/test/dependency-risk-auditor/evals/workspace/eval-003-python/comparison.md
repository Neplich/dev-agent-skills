# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 报告直接识别 Python 生态及三个关键直接依赖：requests、urllib3、Jinja2，并覆盖 HTTP、TLS/连接和模板风险来源。 |
| `risk_classification` | PASS | 报告区分了高/中风险、条件性风险、ReDoS/XSS/凭据泄露/模板代码执行、维护线过期及供应链风险，并说明了严重度与触发条件。 |
| `evidence` | PASS | 报告引用了 requirements.txt 中三个精确固定版本，并提供多个 CVE/GHSA、NVD、PyPI 和上游公告链接作为证据。 |
| `upgrade_plan` | PASS | 报告给出统一升级目标、兼容性注意事项、回归验证重点及无法立即升级时的重定向、凭据清理、TLS、模板隔离和资源限制等临时缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=2d3d0ee3e2bd5c742592b13f697832a4f76881ad70ef2a2bae0a8e5c98065f1b; snapshot_sha256=f21f06af028ad00f4481d85d8a72c14c1b500b7684da2207903d1c89e2f868d9
- Behavior: 完成了结构化依赖安全审计，识别固定版本、分类风险、提供证据，并给出升级与临时缓解建议；交付了审计文件且未修改 requirements.txt。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=67ba5bcabf707d1795df6c5ab7891fdd41d6ec5f288f9d249ac50e0681695874; snapshot_sha256=cf23b7945262be95ce66636b1d6a0425ab31d16c13c69bd5d5e7075d1cb766bc
- Behavior: 同样交付了审计文件并覆盖主要依赖、风险、证据和升级建议，但内容较精简，风险分类和证据范围较窄。
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | with_skill 交付文件识别了 Python 依赖生态及 requests、urllib3、Jinja2 三个关键包，并覆盖 HTTP、TLS、模板、代理和重定向风险来源。 |
| `risk_classification` | PASS | with_skill 把漏洞按 Medium 分级，区分了固定版本过期与项目未 abandoned，并指出锁文件哈希、包来源/provenance 等供应链风险。 |
| `evidence` | PASS | with_skill 交付文件直接引用 requirements.txt:1-3 的固定版本、多个 CVE/OSV/GitHub advisory、修复版本和发布时间证据。 |
| `upgrade_plan` | PASS | with_skill 提供了 requests、urllib3、Jinja2 的升级目标、Python 兼容分支方案、重新生成锁文件和 CI 扫描建议，以及重定向、TLS、模板和代理的临时缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=ff6e3ad13c42064b465ecf19fbdb692eea9797de75c01bda864981e14a48f6f6; snapshot_sha256=8670cb57c13cc43d38b806ca1e25265e1a117ffab7e5240c1399d001c747879b
- Behavior: 完成并归档了结构化 Python 依赖安全审计，覆盖依赖盘点、风险分类、证据、升级计划及临时缓解，且未修改 requirements.txt。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=d530130b366fa88ccd483ea3390e807fa814c8fccfdbe45c595ab44056424931; snapshot_sha256=3e2ebccfa5d4de74c265e282af2c83a3f698d5026c644ba2ac3dcd75beeb43b5
- Behavior: 完成了依赖审计交付，覆盖三项关键依赖、漏洞证据和升级/缓解建议；未修改 requirements.txt。
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `b815bcadedc94647742113823ae910cacb0bd48d343e94eb3875bee2a6a39d68`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With_skill identifies Python dependencies requests, urllib3, and Jinja2, plus HTTP, TLS, template, proxy, redirect, and sandbox risk sources. |
| `risk_classification` | PASS | With_skill distinguishes high, medium, and usage-dependent risks and classifies vulnerability, support/freshness, compatibility, and supply-chain verification concerns. |
| `evidence` | PASS | With_skill cites exact requirements.txt versions and provides CVE/GHSA references, affected/fixed ranges, and advisory/NVD/PyPI links. |
| `upgrade_plan` | PASS | With_skill gives concrete upgrade targets, Python compatibility contingencies, temporary mitigations, testing requirements, and confirms requirements.txt was not modified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=cf05f6202ee8065c104062048f15f49f2a3defe2910352b23887a05b1d17adea; snapshot_sha256=31ef194c0d74e723463019d8352b1eee16b5f6be7548304e01960a0c4d43f7c7
- Behavior: Produced a structured, detailed audit covering all requested risk areas, evidence, severity, upgrade planning, mitigations, and handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=d5599e0d97e66c85af5caafd75073a8bda33b3fcf0044565569a81f7d5671457; snapshot_sha256=1afe945bba6dbe874d839f094f06d2810ee1b7a3326dd54484bc35c25b505989
- Behavior: Produced a strong audit with package/version evidence, vulnerabilities, upgrade targets, mitigations, and no requirements.txt mutation.
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `b815bcadedc94647742113823ae910cacb0bd48d343e94eb3875bee2a6a39d68`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With_skill identifies the Python ecosystem and all three key packages—requests, urllib3, and Jinja2—along with HTTP/TLS, redirect, template, and supply-chain risk sources. |
| `risk_classification` | PASS | With_skill distinguishes multiple CVE vulnerabilities, outdated/unsupported versions, and reproducibility/supply-chain risks, with HIGH/MEDIUM severity and contextual impact. |
| `evidence` | PASS | With_skill cites exact dependency versions from requirements.txt and provides specific CVE identifiers, affected ranges, remediation versions, and authoritative advisory links. |
| `upgrade_plan` | PASS | With_skill recommends coordinated upgrades to requests 2.34.2, urllib3 2.7.0, and Jinja2 3.1.6, plus compatibility testing and concrete interim mitigations. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=ccbbcfa7055360757cdf9a0553aac618d8b737e7feb25060b816d5e3ea6092b9; snapshot_sha256=85cd1d5c79b592f4ef54abd8815780fa8eb88ba7ab6e496f8b3a10ebe087627d
- Behavior: Produced a structured, detailed dependency security audit covering all requested packages, risks, evidence, upgrade targets, and interim mitigations without modifying requirements.txt.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=01204e2d5aa8231769836de2239575ad42e591d97c44c3821b294a6b65421575; snapshot_sha256=dcca324c423623654b5916fe961cd21a90f1aa6c1aaa979f70ec264bdd5ffd47
- Behavior: Produced a detailed security audit with version evidence, vulnerability classification, upgrade targets, and mitigations.
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2573dd217cef308cd88d80bd4db555dc7ac29ee2b87cd67e3ed8f4807140636`
- Skill overlay SHA-256: `ae39de43f00ac22182f0336b47936a0651b8b7cb847715311e719e485ae6d9ed`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | With-skill output identifies the three direct dependencies—Requests, urllib3, and Jinja2—and relates them to HTTP, TLS, redirect, proxy, compression, and template-rendering risk surfaces. |
| `risk_classification` | PASS | It distinguishes confirmed CVEs, outdated dependency lines, conditional usage risks such as SSTI, and assigns High/Medium severity with triggering conditions and impact. |
| `evidence` | PASS | It cites requirements.txt with exact versions (requests 2.19.1, urllib3 1.23, Jinja2 2.10.1), references the PRD and handoff, and provides CVE/advisory identifiers and links. |
| `upgrade_plan` | PASS | It provides concrete upgrade targets for all three packages, compatibility/testing guidance, and temporary mitigations for redirects, TLS verification, proxy credentials, templates, resource limits, and scanning. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=b9671876a506561b05bff453ad694ce52559afe698b79d6f5ae38417a019a1e8; snapshot_sha256=2f062bfbf6a5d160810dd5a68fdf3a8b8aafa20cc447cdaf3c97c7d81d3ff84b
- Behavior: Produced a structured, evidence-based audit covering all three dependencies, severity and conditionality, precise CVEs, upgrade targets, temporary controls, validation gates, and audit limitations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=281da6d055e7ae51f44caff9717fe527d9b7002cf05448fef4025841b0fea55a; snapshot_sha256=dc6eb2d381a7eb4bfb0c871ecc53a127414a2422411ca33db546b0d2bbfa7295
- Behavior: Produced a concise audit summary with exact dependency versions, several known risks, upgrade recommendations, citations, and a generated report path.
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

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9847519784146234ee8e6186ebd4f58b4e08cc25986e95e53a8cdbe8be3e0635`
- Skill overlay SHA-256: `b8089650410317e7cdca1594ef3aeb917b416730f8419e99172c09b88f6c8fc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | Identifies all three pinned dependencies and maps them to HTTP, TLS, and template risk surfaces. |
| `risk_classification` | PASS | Distinguishes vulnerabilities, maintenance risk, supply-chain observations, severity, and conditional exploitability. |
| `evidence` | PASS | Cites exact versions from requirements.txt and provides CVE, release-history, and limitation evidence. |
| `upgrade_plan` | PASS | Provides target versions, temporary mitigations, upgrade sequencing, regression tests, and release gates. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=681819f077024758640ff7c9832fbcaf971824a19cbb6c48fdea0145f9c17be8; snapshot_sha256=55c87f847faa464dc6809820a05d6c7b402bd3e6ff748ee000a5ae03257f4369
- Behavior: Provides a structured, evidence-grounded audit with classifications, remediation, validation, and release gates.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=6e6a6ab566635b436ad0cc9b4f339f58200e83194343f847058f0e25a36390a6; snapshot_sha256=a4f4201f83e05090830a661b6c7faaabd490746e485c99577ced83c87d61894c
- Behavior: Identifies dependencies, risks, upgrade targets, and mitigations, but is less comprehensive.
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

# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Review Python dependencies for security issues.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-003-python/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `6e2bb4aec3b87f9503c5fc46324b2258d9ef732b80318b6d5c0ebb7bb9b3f56c`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 报告明确识别 Python 生态，并列出 requests==2.19.1、urllib3==1.23、Jinja2==2.10.1 及其 HTTP、TLS、模板相关风险。 | PASS | 报告列出三项 Python 直接依赖及对应 HTTP、TLS、模板风险。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分漏洞、过期/不受支持版本和供应链/补丁滞后风险，并按 Critical、High、Medium 说明严重度及可利用条件。 | PASS | 报告区分已知漏洞、不受支持版本和模板风险，并给出 High/Medium 严重度与利用条件。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 requirements.txt 中的精确版本和行号，并提供多个 CVE/GHSA 及外部 advisory 链接作为证据。 | PASS | 报告引用 requirements.txt:1-3、精确版本及多个 CVE/GHSA advisory。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出协调升级到 requests 2.34.2、urllib3 2.7.0、Jinja2 3.1.6+ 的优先级、测试要求、CI 审计和升级延迟时的临时缓解措施。 | PASS | 报告给出替换全部 pin、协调升级、DevOps 临时控制和 lockfile/SBOM 后续计划。 |

## With-Skill Behavior

With-skill 明确读取 handoff、PRD 和 requirements.txt，创建了符合契约的 dependency-audit.md，包含三项依赖、版本证据、漏洞/过期分类、严重度、CVE、限制条件及升级和缓解建议。

## Fresh Without-Skill Baseline

Without-skill 也完成了依赖审计并创建报告，作为 baseline 各项断言均满足。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
