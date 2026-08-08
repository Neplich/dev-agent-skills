# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `f6ca8293d29d78d2f2b85bd613e1f25b3aa93a647c64e21ca6731d5a228a1284`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill 正确识别 editorial.patch 仅为正文措辞变化，并保留其不影响现有部署结论的状态。 |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill 正确识别 internal-entry.patch 修改 internal 构建输出目录和 Docker COPY 路径，并要求重新进行部署完整性审查；但锁定证据无法证明是否复用了 skill-map 共享检查或避免复制清单。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=86199450813edfd305850baa10a0b4d7b2e4b608b272075731925c275397ae24; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分纯正文变化与发布面变化，并阻止在缺少主机仓库和确认信息时完成版本说明交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=8f9f196f9f02e624204209cc18afcab66ba42caffbe09ee10aa408c1dad821dc; snapshot_sha256=713fe3832b81918f3ee4ef3502c1588b5d24f8611e15c9c881967438462b655f
- Behavior: 将 internal-entry.patch 误判为不影响部署结论，未触发共享部署完整性复查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充主机仓库、发布范围、证据来源和维护者确认后完成版本说明收尾。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | NOT_EXERCISED | with_skill 仅暂停并请求补充确认，未完成对 editorial.patch 的语义判断或部署检查。 |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill 仅暂停并请求补充确认，未完成对 internal-entry.patch 的共享状态复用或检查。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=bcda0e9919eeb46af07674568da35ad043cff6822cdb7965d319840501f5b392; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因声称缺少发布入口凭据而暂停，要求补充确认；未产生交付文件或仓库变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=9ab62b53769c3214751351dd50f75cdf76e1f42ac40356c605684ed9d9741eb0; snapshot_sha256=99552617a66eaccf71eec00db068dc4bc664bf61303a06f7874c3f1cb76162b0
- Behavior: 读取并比较两份 patch，创建 closeout.md；正确区分正文变化与构建产物路径、导航及 Dockerfile 变化，且未修改部署配置。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供候选输出所请求的等价发布确认后，继续比较两份 patch 并完成版本说明收尾。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill 明确判断 editorial.patch 仅改变文案，不使现有文档部署结论失效，符合纯正文变化保留既有状态。 |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill 正确识别 internal-entry.patch 涉及构建输出路径和 Docker 复制路径变化，并要求重新核验；但锁定证据无法证明是否复用了 skill-map 共享检查或未复制清单。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=e82c5db9ffe36c2dabc5c4c7c0597374f512ea22c8b4d25be73e5a7acf2af223; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判断 editorial.patch 不影响部署结论，识别 internal-entry.patch 需要重新核验，并因缺少版本说明基础设施而阻止写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=717ad4c33f5dbf8f13295d1ad5fd9b4d2f99ab906867e0f525ebf404adb47d60; snapshot_sha256=bb2812ed2fcbbd83f0f328eb3d9122ce391dd456b83ffd08923b365454bdaac4
- Behavior: 完成并写入版本说明；正确区分文案变化与构建产物路径变化，但未提供共享检查过程证据。
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
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | NOT_EXERCISED | with_skill correctly identifies editorial.patch as documentation-only and says the existing deployment conclusion remains valid, but the locked evidence cannot prove the hidden check/recheck behavior. |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill identifies the coordinated output-path change and explicitly says a fresh build evidence check is required, but the snapshot lacks the runtime documentation build inputs and no such check was run. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=0840d1bb87037e58787c2fc8ff58b5a2267b17484dbade6399fad585da302fc6; snapshot_sha256=24d8dee3804e96749c32fbf2011393ea645cc9ec6ad9606848a1f22e9462b56c
- Behavior: Accurately distinguished editorial versus material changes, captured the navigation impact, preserved the no-config-mutation constraint, and transparently marked runtime verification blocked by missing snapshot inputs.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=078c7696c04cecf916c43f24a47b8f1da155d0c38f1390471e34d050f9b3478f; snapshot_sha256=c44f260ecbfa3fcd8dbd16df762e986a1cbc6ccc077f74364a572ba9105fafdf
- Behavior: Correctly classified the editorial change and path synchronization, but omitted the internal navigation change and did not identify the need for fresh build evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Run the shared documentation build/deployment evidence check in the host repository, then confirm the release-notes handoff with maintainer metadata and index evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `299c765e24bed3d47cd5f1165cb4e7dae973e90fb9c91e1e5e35950ac2fddd9f`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill identifies editorial.patch as wording-only and says it does not affect deployment configuration or conclusion, preserving the existing deployment state. |
| `rechecks_material_release_surface` | FAIL | with_skill correctly identifies the changed internal output path and requires rebuild/validation, but does not establish reuse of skill-map shared state/checks or explicitly avoid duplicating a checklist. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=6475ddbdd1fa01a46226501676e0d4cdb91a986b6e1e35995ebd428191aaf967; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Made no changes, accurately classified the two patches, identified the internal path impact, and appropriately kept completion blocked; however, it did not demonstrate the required skill-map shared-check reuse.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=83a267f61e981ef7797e15930355588ad06ffd48ad7afe12cb17c320e3bca1f2; snapshot_sha256=28e148a5ee290faad421e9aedba462b7ab92cdd6de2bbcf8f2d8c9781369c695
- Behavior: Created an unrequested README, concluded editorial is safe and internal-entry needs revalidation, and noted incomplete patch hunks.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required skill-map shared-state/shared-check reuse for the material release-surface change.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | With_skill correctly identifies editorial.patch as a wording-only change with no impact on build, deployment artifacts, or routes, so the existing deployment conclusion remains valid. |
| `rechecks_material_release_surface` | PASS | With_skill correctly identifies internal-entry.patch as changing the internal output directory and Dockerfile copy path, requiring revalidation of the internal build/container chain; it does not introduce a separate checklist. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=4625e5f92e5571bd6647d1526b3ccdb87ea9e3299c04bd686a4d67fd8af289e5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the patch impacts and appropriately declined unsafe version-note completion because the documentation host structure was absent and the patches were corrupt.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=dee79b9a68003b286a2e9031df6e760ae8c6262aa9000d934af202da6ce9c32b; snapshot_sha256=c00960013e1ff6240e05a6af420c08a5f9d68ef56aa347528e579d03b5a39525
- Behavior: Correctly classified both patches, but claimed version-note completion by creating an unsupported release-note file.
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

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口，已按 #238 于 2026-08-06 fresh 隔离重跑）
- Eval: `eval-004-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `skips_content_only_recheck` | PASS | PASS | with_skill 明确写出“Content-only…不触发部署级复核”；without_skill 写出“纯文案/错字变更：不影响运行时，无需部署”。 |
| `rechecks_material_release_surface` | FAIL | FAIL | 两条 lane 都识别出新增 Internal 导航会改变生成输出和启动路径；但 with_skill 仅说“需重新验证”，没有产出共享状态/检查复用证据；without_skill 仅分类为需要部署，也没有证明复用共享检查。两者均未复制新清单。 |

未满足断言（with/without 任一 FAIL）：``rechecks_material_release_surface``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- content-only 保留状态；runtime change 复用唯一共享协议且不复制 checklist。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- PARTIAL (1/2)；识别触发差异，但未声明共享状态/协议复用。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺共享协议复用语义。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
