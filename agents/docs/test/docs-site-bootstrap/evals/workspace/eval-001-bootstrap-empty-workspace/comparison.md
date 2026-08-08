# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `373ba2965836f0cc6198ffb0151c12c61c34831fe45aaa5ef665fae7d893acbc`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | Manifest lists 42 assets; the snapshot contains those exact 42 files, with matching SHA-256 content and created statuses. |
| `delivers_deterministic_scaffold_assets` | PASS | package.json has one new:doc script; scaffold-doc.mjs and its test exist; six templates each contain exactly one docs-scaffold block and all are indexed. |
| `validates_seven_frontmatter_fields` | PASS | All 19 Markdown pages visibly contain the seven required frontmatter fields, valid doc_type values, non-empty owners/related_code arrays, and last_verified_version: unverified. |
| `writes_only_docs_site` | PASS | Every delivered snapshot path is under docs/site/, with no outside paths or repository configuration changes shown. |
| `requires_explicit_opt_in` | PASS | The prompt explicitly confirms the current repository, fixed docs/site root, and complete scaffold; the candidate reports that same host and root scope before reporting the write. |
| `reports_manifest_readback` | PASS | The candidate reports 42/42 manifest readback equality and 42 skipped-identical files on repeat; the manifest directly contains all paths and created statuses. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3fefd961b1b4acdc2e53b0fb4306d5f7803908f2422ebc51d3b2e9d5ff11a38a; snapshot_sha256=f50521887e92aa39c647e777bfeb66700911acfcfa7a230b19b389f788f822f0
- Behavior: Delivered the requested 42-asset formal documentation scaffold under docs/site, including manifest, templates, scripts, frontmatter pages, and repeat-run results.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=efb64f1206c3ac840f993effd66fbd457720bae8d556839db269510314256669; snapshot_sha256=2dd6f2f5375c211bea5c93c42c10e98c2b5b4c4798e437105790c9c3386a0494
- Behavior: Created a small Docusaurus starter site with 11 files, without the requested inventory, manifest, formal templates, or validation scaffold.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install the missing fast-glob dependency and rerun npm run test:docs.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | with_skill 的 manifest.files 含 42 个 docs/site 路径，全部对应 workspace_manifest；交付快照和输出均记录 42/42 逐字节校验。 |
| `delivers_deterministic_scaffold_assets` | PASS | package.json 含唯一 new:doc 命令；scaffold 脚本、测试文件、六个模板均存在。六个模板各有一个 docs-scaffold 区块，standards/index.md 索引了六者。 |
| `validates_seven_frontmatter_fields` | PASS | 所有交付 Markdown 页面均含七个 frontmatter 字段；页面 doc_type 使用允许值，owners 与 related_code 为非空数组，last_verified_version 均存在且可为 unverified。 |
| `writes_only_docs_site` | PASS | with_skill 的 git status 仅显示 docs/site/ 下新增文件；HEAD、分支、索引和工作树既有内容均未改变。 |
| `requires_explicit_opt_in` | NOT_EXERCISED | prompt 确实明确确认了当前仓库、docs/site/ 根和完整 scaffold，但锁定证据无法证明具体的 opt-in 读写门禁过程或无 opt-in 分支。 |
| `reports_manifest_readback` | PASS | 输出明确报告 manifest 已成功读回、42/42 校验通过，并说明模板与决策不变时重复执行为 zero-diff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5dbfcb97df214fd4b59d46f448cbdda47bc618be8df2ac46efbb06c26e3cc8cd; snapshot_sha256=762bd10c68863806694869bddc788c8599b52706912e253777086076352a5e77
- Behavior: 交付完整 42 项清单及 manifest、确定性脚手架、规范模板、页面 frontmatter 和 zero-diff 报告；依赖测试因 fast-glob 未安装未完成。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e4742da7d2efdb31b8fc6f4477edd17e06a229b0855d5b2a8f182ff60090d3b4; snapshot_sha256=2478dfc8f6cb1b0cade64eee058971a995de92ec33a88c2a6ebba889ca29778d
- Behavior: 仅交付基础 VitePress 文件，缺少 manifest、完整脚手架、规范模板和 frontmatter 体系；其重复执行描述不能替代目标要求。
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

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `94e37af2ad7f4b39032db420d30845826ffa4c408edb8ffe671f400ff7e83f83`
- Skill overlay SHA-256: `09f32081fb5da19c616e5c124981201ff10d8f1031a9890f0577b1364fa9c83c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | with_skill 清单列出 42 个 docs/site 文件，包含 bootstrap-manifest.json；manifest files 覆盖这些文件，且回读报告为 42/42 字节一致。 |
| `delivers_deterministic_scaffold_assets` | PASS | package.json 含唯一 new:doc 命令；scaffold-doc.mjs、测试文件及六个模板均存在。六个模板各含一个 docs-scaffold 区块，并由 standards/index.md 全部索引。 |
| `validates_seven_frontmatter_fields` | PASS | 快照中的正式 Markdown 页面均包含七个字段；doc_type 均为允许值，owners 与 related_code 为非空数组，last_verified_version 为 unverified。 |
| `writes_only_docs_site` | PASS | with_skill 的 git_status 仅显示 ?? docs/，清单中的生成路径全部位于 docs/site/，未显示根配置或其他路径变更。 |
| `requires_explicit_opt_in` | FAIL | 候选输出未说明写入获准是因为 prompt 明确确认了目标仓库、docs/site 根目录和完整 scaffold；仅报告了宿主仓库与生成根目录。 |
| `reports_manifest_readback` | NOT_EXERCISED | 候选报告了 manifest 回读和 42/42 一致，但重复执行仅表述为“预计 zero-diff”，没有实际重复运行的运行时证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=96e9991c55d6cf4a1988ed4ae76a710a48c7de81fa887da27d7b30f8c5a9dc4c; snapshot_sha256=be53d9b525308af5cde2254386cda00f462e44cf2b2a140dfbb8d2dbbf7d6fd1
- Behavior: 在 docs/site 下生成了完整 42 项 scaffold、manifest、模板、脚本和正式页面，并报告了字节一致性；未明确说明显式 opt-in 原因，幂等重复运行尚未实际验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=de7d3fb9a2202ba0783515d844996569bb257784b1985a6c712264744ac7ba49; snapshot_sha256=6a7d10cfd686d82ebc240f84f330aa675ebf545a13fdcccd4a88a049b7405ef3
- Behavior: 创建了基础 VitePress 站点，但写入了仓库根 package.json 和 scripts，未生成目标所需的 42 项清单、manifest、规范模板或校验体系。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未满足 requires_explicit_opt_in 的用户可见说明要求。
- Next: 补充明确的 opt-in 依据说明，并实际执行第二次初始化后回读 manifest，记录 42 个 skipped-identical 与 zero-diff 结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2f0004a415a9413ec4f04c88be670a46f49aae91bdfea7a5f5a1bd3994bc3a2`
- Skill overlay SHA-256: `e3264805b55d520c4492930be28050bfd749cd67b6530c8ad7ae5532a81dc597`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | With-skill evidence reports 42 byte-verified static scaffold files, and the manifest contains 42 corresponding docs/site paths. |
| `delivers_deterministic_scaffold_assets` | PASS | package.json has a single new:doc script; both requested scripts are present; six templates each contain one docs-scaffold block and standards/index.md links all six. |
| `validates_seven_frontmatter_fields` | PASS | All formal Markdown snapshots shown have the seven required fields, allowed doc_type values, non-empty owners and related_code arrays, and last_verified_version set to unverified. |
| `writes_only_docs_site` | PASS | All delivered files are under docs/site, and git evidence reports only an untracked docs/ tree with no outside changes. |
| `requires_explicit_opt_in` | FAIL | The prompt supplies explicit opt-in, but the with-skill output does not explain that this authorization was the reason writing was permitted. |
| `reports_manifest_readback` | NOT_EXERCISED | The output reports manifest creation and zero-diff repeated execution, but locked evidence cannot establish the hidden readback/parse order. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9783a050eee288d1901e721fe22e3273037611dacf9c4b9cfca7c3a7fe33c4a0; snapshot_sha256=92162d5ab6148a920c059ba6ac3a494740b2842bc17a25ed6a7afb4451e8c0bd
- Behavior: Created the required 42-file scaffold, manifest, deterministic tooling, templates, and frontmatter structure; reported a blocked test command and omitted the explicit opt-in rationale.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fd29c404c4a59bc71f3d8c8bb85d852c3c966ab263e2d0a45f0d01fb5d7d2c9a; snapshot_sha256=fc6baeedb47df910684a0bb0273cf348aa2f94423771c85ea7d7658c67eae291
- Behavior: Created a basic VitePress site without the required inventory, scaffold tooling, templates, or frontmatter contract.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required explanation that explicit prompt opt-in authorized the writes.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-001-bootstrap-empty-workspace`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | with_skill evidence reports 42/42 byte verification; manifest contains 42 created entries, all under docs/site/. |
| `delivers_deterministic_scaffold_assets` | PASS | Snapshot contains package.json with one new:doc script, both required scripts, six templates with exactly one docs-scaffold block each, and standards/index.md links all six. |
| `validates_seven_frontmatter_fields` | PASS | All 19 Markdown pages in the snapshot contain the seven required fields; owners and related_code are non-empty arrays, doc_type values are allowed, and last_verified_version is present. |
| `writes_only_docs_site` | PASS | All 42 manifest paths are within docs/site/; git evidence shows no tracked-file changes and only the docs directory untracked. |
| `requires_explicit_opt_in` | PASS | The prompt explicitly confirms the target repository, fixed docs/site root, and complete scaffold before the with_skill lane writes. |
| `reports_manifest_readback` | PASS | with_skill reports manifest parsing and path/status validation, plus repeat execution producing 42 skipped-identical files, zero conflicts, and zero content changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b94d3bc71ead18138be683dfdfb4ce717a4bb8b84236dc302dfe28186a27a095; snapshot_sha256=13b06c79556a034e84ca74d53414eac66892c7fad48ef238489f2cbc7275d24b
- Behavior: Created the complete 42-asset formal documentation scaffold under docs/site, validated manifest coverage and frontmatter, and reported deterministic zero-diff rerun behavior.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5face9b89423d7ac698448df35db8f8e53255cde6c5524d24fe775c1b9c7042a; snapshot_sha256=603023b347ba6e56192ea24250868340485c05ea2c579e7bf8b9a7903c705fb3
- Behavior: Created a small Docusaurus scaffold with 9 files, omitted the required 42-asset inventory and formal documentation scaffold, and reported repeat execution as unchanged.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-001-bootstrap-empty-workspace`
- Review context: issue #155 fresh paired eval

## Test Set / Fixture Version

- Fixture: pristine empty host from `workspace/eval-001-bootstrap-empty-workspace`
- Historical asset snapshot: 40-file `assets/docs/site/` inventory
- Current contract: 42 packaged assets and six templates
- Dependency fact under review: the VitePress declaration is pinned exactly to `1.6.4` in both `package.json` and the root and resolved entries of `package-lock.json`
- Actual validation date: `2026-07-22`
- Execution cleanup: isolated lane started without `docs/site/`

## Latest Result

**PASS (6/6 assertions)** — the historical fresh with-skill lane created the complete bounded scaffold for the then-current 40-asset, five-template contract, generated and read back a sorted 40-entry manifest, passed the applicable host checks and both site builds with VitePress 1.6.4, and demonstrated a zero-content-diff repeat classification.

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `creates_complete_inventory` | PASS | FAIL | with_skill 源资产 42 项全部逐字节匹配，manifest 含 42 条记录；without_skill 仅生成 6 个文件且无 manifest。 |
| `delivers_deterministic_scaffold_assets` | PASS | FAIL | with_skill `new:doc` 唯一存在，两个脚本齐全，六个模板各有一个完整区块并被 `standards/index.md` 索引；without_skill 均不存在。 |
| `validates_seven_frontmatter_fields` | PASS | FAIL | with_skill 的 19 个正式 Markdown 页面均有七字段，`doc_type` 均在允许集合内，数组非空且版本为 `unverified`；without_skill 页面无 frontmatter。 |
| `writes_only_docs_site` | PASS | PASS | 两条 lane 的实际生成文件均位于各自 workspace 的 `docs/site/` 下，未发现目标根外文件。 |
| `requires_explicit_opt_in` | PASS | PASS | 两条 lane 使用的 prompt 均明确确认当前仓库、固定 `docs/site/` 根及正式文档站初始化。 |
| `reports_manifest_readback` | FAIL | FAIL | with_skill manifest 可独立解析且路径/状态正确，但没有独立保留的重复运行快照或 diff 证据；without_skill 没有 manifest。 |

未满足断言（with/without 任一 FAIL）：``creates_complete_inventory``、``delivers_deterministic_scaffold_assets``、``validates_seven_frontmatter_fields``、``reports_manifest_readback``



## Current Asset-Set Status

- The retained PASS above is the historical issue #155 result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after adding `standards/templates/manual-guide.md` and `manual/index.md`.
- The #238 paired rerun and independent judge validated the current inventory and scaffold surfaces. The current result remains `FAIL` only because `reports_manifest_readback` lacks an independently retained repeat-run snapshot or zero-diff evidence.

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `creates_complete_inventory`: PASS. All 40 packaged assets were copied byte-for-byte; manifest parsing returned 40 sorted `created` entries.
- `delivers_deterministic_scaffold_assets`: PASS. `package.json` has exactly one `new:doc`; the scaffold script and test exist; each of five templates has exactly one `docs-scaffold` block and all five are indexed.
- `validates_seven_frontmatter_fields`: PASS. `npm run test:docs` passed the shared frontmatter checker and all 74 Node tests.
- `writes_only_docs_site`: PASS. The generated scaffold and runtime manifest were confined to the isolated `docs/site/` root; evaluation evidence remained outside the generated host root under the issue scratch directory.
- `requires_explicit_opt_in`: PASS. Execution relied on the prompt's explicit host fixture, fixed `docs/site/` root, full scaffold, and manifest authorization; without that entry basis the skill gate stops before writes.
- `reports_manifest_readback`: PASS. The manifest parsed with 40 valid paths and dispositions, and a second full static-content checksum comparison was zero-diff with the original `createdAt` unchanged.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Source: fresh issue #155 with-skill lane under `tmp/eval-runs/issue-155/with_skill/eval-001`, using the current Docs README, target skill, internal inventory protocol, shared frontmatter contract, eval prompt, and pristine fixture.
- Copied 40/40 static assets exactly, created `.meta/bootstrap-manifest.json` with stable sorted paths, and read every generated static target back against its packaged source.
- Confirmed `vitepress: "1.6.4"` in `package.json`, the lockfile root dependency, and the resolved `node_modules/vitepress` record.
- Ran `npm ci`, `npm run test:docs`, `npm run build:public`, and `npm run build:internal`; all exited `0`, and both build logs identified VitePress 1.6.4.
- Reclassified the complete static inventory and compared checksums after host checks; scaffold content and manifest remained zero-diff. Generated `.generated/**` trees and `node_modules/**` were treated only as runtime evidence.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: a newly spawned independent issue #155 baseline worker using the same prompt and empty scratch fixture. It was explicitly prohibited from reading the target skill, Docs README, internal instructions, old comparisons, with-skill output, and packaged assets.
- Result: `BLOCKED`. The empty scratch exposed no scaffold source, complete inventory, manifest rules, or runner, so the worker correctly refused to guess and created no `docs/site/` output.
- No historical baseline was reused. The inability to generate the requested scaffold demonstrates the behavioral value of the skill and does not block the valid with-skill result.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures or blocked checks.
- The fresh without-skill lane was blocked by absent implementation sources and satisfied none of the artifact assertions.
- `npm ci` reported 3 audit advisories (2 moderate, 1 high); installation, 74/74 tests, and both required builds still passed, so this is recorded as non-blocking runtime evidence rather than an eval failure.

## Next Steps

- Retain the PASS only as the historical issue #155 result for the 40-asset, five-template contract.
- Re-run the current 42-asset, six-template contract with an independently retained repeat-run snapshot or zero-diff evidence before replacing the current `FAIL` result.

## Runtime Artifact Policy

- Runtime lanes, manifests, checksums, `node_modules`, generated site trees, and baseline reports remain under `tmp/eval-runs/issue-155/` and are not durable repository artifacts.
- Only this `comparison.md` is retained; no transcript, candidate, verdict, timing, diagnostics, dependency directory, or generated site output is submitted.
