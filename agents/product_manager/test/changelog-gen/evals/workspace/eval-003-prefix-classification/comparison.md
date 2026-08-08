# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `cc05e28bb9aed099804431e1cee55bda0cec7614cc8c780d6f8ad4d50c137367`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Added entry was produced. |
| `fix_fixed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Fixed section was produced. |
| `chore_deps` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; dependency handling was not exercised. |
| `build_deps_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; dependency handling was not exercised. |
| `perf_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Changed section was produced. |
| `feat_added_breaking` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; breaking-change handling was not exercised. |
| `docs_release_workflow_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; release-workflow handling was not exercised. |
| `test_release_acceptance_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; release-acceptance handling was not exercised. |
| `ci_release_gate_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; CI release-gate handling was not exercised. |
| `docs_typo_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; docs filtering was not exercised. |
| `ci_cache_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; CI filtering was not exercised. |
| `remove_removed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Removed section was produced. |
| `security_security` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Security section was produced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=060c6a19e40c3ccd8dc27ae59ef3a4cf3e1384496e5d74fde7382b78e8a631ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly paused to request the required target changelog mode; content transformation was not yet exercised.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a1708dc2c3a196376850cc13ad0c6d6b8bd1405d55e2464c05b91a2225f1001b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete Keep a Changelog-style result covering the requested user-visible changes and exclusions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Select a target mode, then generate and evaluate the changelog content.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | With-skill output places Add OAuth2 login support (#101) under Added. |
| `fix_fixed` | PASS | With-skill output places token-expiry crash fix (#102) under Fixed. |
| `chore_deps` | PASS | With-skill output omits dependency-maintenance PR #103. |
| `build_deps_skipped` | PASS | With-skill output omits dependency-maintenance PR #114. |
| `perf_changed` | PASS | With-skill output places API caching improvement (#104) under Changed. |
| `feat_added_breaking` | PASS | With-skill output places the plugin configuration API redesign (#105) under Changed with an explicit BREAKING marker. |
| `docs_release_workflow_changed` | PASS | With-skill output places the release workflow changes (#106) under Changed. |
| `test_release_acceptance_changed` | PASS | With-skill output places release acceptance and evidence changes (#107) under Changed. |
| `ci_release_gate_changed` | PASS | With-skill output places required repository release checks (#108) under Changed. |
| `docs_typo_skipped` | PASS | With-skill output omits typo/copyediting PR #109. |
| `ci_cache_skipped` | PASS | With-skill output omits internal CI cache maintenance PR #110. |
| `remove_removed` | PASS | With-skill output places dropping Python 3.7 support (#112) under Removed. |
| `security_security` | PASS | With-skill output places the XSS vulnerability patch (#113) under Security. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fc221ad79b088a260e0f2d3ee55ec651b433b4e7aa386616d7894c902c4bef4e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced all required user-visible sections, classified every relevant PR correctly, marked the breaking API redesign clearly, and explicitly listed skipped internal-only items.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=7965b7bdb0d95568aec4244c2c63554836094a352a307ab0d49f9734bcd4f15d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a semantically complete changelog and skipped the three internal-only items.
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
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | with_skill places OAuth2 login under Added with the cleaned title “Add OAuth2 login support”. |
| `fix_fixed` | PASS | with_skill places the token-expiry crash fix under Fixed. |
| `chore_deps` | PASS | with_skill explicitly skips dependency upgrade #103. |
| `build_deps_skipped` | PASS | with_skill explicitly skips dependency upgrade #114. |
| `perf_changed` | PASS | with_skill places the API caching improvement under Changed. |
| `feat_added_breaking` | FAIL | with_skill clearly marks the plugin API redesign as BREAKING but places it under Added instead of Changed. |
| `docs_release_workflow_changed` | PASS | with_skill places the release workflow changes under Changed. |
| `test_release_acceptance_changed` | PASS | with_skill places the release acceptance and durable evidence changes under Changed. |
| `ci_release_gate_changed` | PASS | with_skill places the required repository checks before release under Changed. |
| `docs_typo_skipped` | PASS | with_skill explicitly skips README typo/copyediting change #109. |
| `ci_cache_skipped` | PASS | with_skill explicitly skips CI cache maintenance #110. |
| `remove_removed` | PASS | with_skill places dropping Python 3.7 support under Removed. |
| `security_security` | PASS | with_skill places the XSS vulnerability patch under Security. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=32d6fa043e6c8f14443850f221120cbdf22dd475d3c9ae9b96f12d410be383af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all exercised requirements except placing the clearly marked breaking API redesign under Added rather than Changed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=46b3d17de4b5dcc5c8adb893588b0607e16e8dacead04db86d4a8ad940d7040a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all listed changes, including the breaking API redesign under Changed, but uses less prominent breaking-change marking.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output places the breaking plugin configuration API redesign in Added, contradicting the requirement that it belong in Changed.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | With-skill output places OAuth2 login support in Added with the cleaned title “Add OAuth2 login support” (#101). |
| `fix_fixed` | PASS | With-skill output places the token-expiry crash fix in Fixed (#102). |
| `chore_deps` | PASS | With-skill output omits the dependency maintenance PR and explicitly says dependency version updates were skipped. |
| `build_deps_skipped` | PASS | With-skill output omits the Vite dependency bump; its skip note covers dependency version updates. |
| `perf_changed` | PASS | With-skill output places the caching/API response-time improvement in Changed (#104). |
| `feat_added_breaking` | FAIL | The breaking plugin configuration API redesign is placed in Added, but the assertion requires Changed with a clear BREAKING marker. |
| `docs_release_workflow_changed` | PASS | With-skill output places the release publishing workflow changes, including draft releases, changelog preflight, tag retargeting, and review rules, in Changed (#106). |
| `test_release_acceptance_changed` | PASS | With-skill output places release acceptance coverage and required publishing evidence changes in Changed (#107). |
| `ci_release_gate_changed` | PASS | With-skill output places required repository checks before release in Changed (#108). |
| `docs_typo_skipped` | PASS | With-skill output omits the README typo fix and says README spelling correction was skipped. |
| `ci_cache_skipped` | PASS | With-skill output omits the cache-only CI change and says internal cache maintenance was skipped. |
| `remove_removed` | PASS | With-skill output places dropping Python 3.7 support in Removed (#112). |
| `security_security` | PASS | With-skill output places the XSS vulnerability patch in Security (#113). |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f1e2468bc6cdc5f46fb12f4d4a71a27dd4843a52bc18ac20fb888bb7d0f236fb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all exercised requirements except the breaking API redesign, which is incorrectly placed in Added despite being marked BREAKING.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a7cd8d076819ce053d7644af9639b0ae61033dbc0b2bbc523c5f438cb04d8f94; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies all listed changes, including the breaking API redesign in Changed.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane misclassifies the breaking plugin configuration API redesign as Added instead of Changed.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `281e1b5c19a67eed1e87d8548e15e7ab23a90d7de9e0bd112a29df45200426a3`
- Skill overlay SHA-256: `f4e3f318f95aeaf018d947cb5144bbc03198d0d62d802018a4946522adbf8065`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a13934e813a2542c7822dc8e78db937ac0ee61dc52a8ddd247b8b0f1be1069a9`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | with_skill artifact lists “Add OAuth2 login support” under Added. |
| `fix_fixed` | PASS | with_skill artifact lists the token-expiry crash fix under Fixed. |
| `chore_deps` | PASS | The with_skill changelog contains no chore(deps) entry. |
| `build_deps_skipped` | PASS | The with_skill changelog contains no build(deps) entry. |
| `perf_changed` | PASS | with_skill artifact lists reduced API response time through caching under Changed. |
| `feat_added_breaking` | FAIL | The breaking plugin configuration API entry is under Changed, but the assertion requires Added with an ⚠️ BREAKING prefix. |
| `docs_release_workflow_changed` | PASS | with_skill artifact lists the release publishing workflow change under Changed. |
| `test_release_acceptance_changed` | PASS | with_skill artifact lists release acceptance coverage and durable evidence requirements under Changed. |
| `ci_release_gate_changed` | PASS | with_skill artifact lists required repository checks before release under Changed. |
| `docs_typo_skipped` | PASS | The with_skill changelog contains no typo/copyediting-only docs entry. |
| `ci_cache_skipped` | PASS | The with_skill changelog contains no cache-only CI entry. |
| `remove_removed` | PASS | with_skill artifact lists dropping Python 3.7 support under Removed. |
| `security_security` | PASS | with_skill artifact lists the XSS vulnerability patch under Security. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=414d2b4292b46241469441a4541a9738d23746965150e6246152d229c50ee3a5; snapshot_sha256=386d7591c16891d00eaee3786fafaf13f9eb4d18fb3c59a521e224a142872434
- Behavior: Created docs/changelog/changelog-unreleased.md with the requested sections, included all behaviorally relevant entries, skipped internal/formatting-only maintenance, but classified the breaking feature under Changed instead of Added.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2e900818a14a78ab2233cd758acdb55b5717bea165775606f1e0a5e4923c6b98; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete inline changelog and classified all listed changes correctly, including the breaking feature under Changed; made no workspace changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- feat_added_breaking failed because the with_skill output places the breaking feature in Changed rather than Added.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3dfcf246dc4057e8231ee4e2380b4525eeecf840a484daf60bd4e990283d5e5e`
- Skill overlay SHA-256: `5c214a0a2c2365016d6b3bafaa3e6cd9bb33067b007f4407a0b78fe50c4ba935`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a13934e813a2542c7822dc8e78db937ac0ee61dc52a8ddd247b8b0f1be1069a9`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | PASS | with_skill 输出将 #101 放入 Added，并清洗为“Add OAuth2 login support”。 |
| `fix_fixed` | PASS | with_skill 输出将 #102 放入 Fixed。 |
| `chore_deps` | PASS | with_skill 输出未列出 #103，且明确跳过依赖升级。 |
| `build_deps_skipped` | PASS | with_skill 输出未列出 #114，且明确跳过依赖升级。 |
| `perf_changed` | PASS | with_skill 输出将 #104 放入 Changed。 |
| `feat_added_breaking` | PASS | with_skill 输出将 #105 放入 Added，并以“⚠️ BREAKING”前缀标记。 |
| `docs_release_workflow_changed` | PASS | with_skill 输出将包含 draft releases、changelog preflight、tag retargeting 和 publishing review rules 的 #106 放入 Changed。 |
| `test_release_acceptance_changed` | PASS | with_skill 输出将发布验收覆盖率及发布证据要求变更的 #107 放入 Changed。 |
| `ci_release_gate_changed` | PASS | with_skill 输出将 required repository checks 的 #108 放入 Changed。 |
| `docs_typo_skipped` | PASS | with_skill 输出未列出 #109，并明确跳过 README 拼写修正。 |
| `ci_cache_skipped` | PASS | with_skill 输出未列出 #110，并明确跳过内部缓存维护。 |
| `remove_removed` | PASS | with_skill 输出将 #112 放入 Removed。 |
| `security_security` | PASS | with_skill 输出将 #113 放入 Security。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5237c20d2683883c996eb1df293f661940a25bbc22236142dd7bd332ff5420c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确整理 Added、Changed、Fixed、Removed、Security 章节，清洗标题并标记破坏性变更，同时跳过无意义内部维护项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cd52450af87a9cb43b9f603492d4d4130297fb14b1a50ca7f03a8a039eec758e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确整理所有用户可见变更、跳过内部维护项，并输出中文 Keep a Changelog；作为 fresh baseline 整体满足断言。
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

# Eval Result: eval-003-prefix-classification

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`
- Test case: `prefix-classification`
- Prompt:

> 以下是一批 PR 标题和正文，帮我把它们分类到 Keep a Changelog 的各个章节（Added/Changed/Fixed/Deprecated/Removed/Security），并按格式输出，跳过不需要出现在 changelog 的条目。注意：docs/test/ci 不能只按前缀跳过，需要根据正文判断是否影响用户可见能力、skill 行为、eval 契约、release workflow、installation 或协作边界。
>
> - feat(auth): add OAuth2 login support (#101)
>   Body: Adds a new OAuth2 login flow for users.
> - fix: resolve crash when token expires (#102)
>   Body: Fixes a user-visible crash.
> - chore(deps): bump requests from 2.28 to 2.31 (#103)
>   Body: Dependency maintenance only.
> - build(deps): bump vite from 5.0.0 to 5.0.1 (#114)
>   Body: Dependency maintenance only.
> - perf: reduce API response time by caching (#104)
>   Body: Improves response time.
> - feat!: redesign plugin configuration API (#105)
>   Body: BREAKING CHANGE: plugin configuration fields changed.
> - docs: update release notes generator publishing workflow (#106)
>   Body: Adds GitHub draft release, changelog preflight, tag retargeting, and publishing review rules used by release owners.
> - test: tighten changelog-gen eval contract (#107)
>   Body: Updates eval assertions and durable comparison requirements so docs/test/ci PRs are judged by semantic impact.
> - ci: require repository and eval contract checks before release (#108)
>   Body: Changes required release gates for this skill marketplace.
> - docs: fix typo in README heading (#109)
>   Body: Copyediting only; no behavior or workflow change.
> - ci: tune cache restore key (#110)
>   Body: Internal cache maintenance only; no release gate change.
> - fix(ui): correct button alignment on mobile (#111)
>   Body: Fixes visible UI layout.
> - remove: drop Python 3.7 support (#112)
>   Body: Removes unsupported runtime.
> - security: patch XSS vulnerability in template renderer (#113)
>   Body: Fixes a security vulnerability.

- Expected output:

> Added: feat items. Changed: perf items plus docs/test/ci items with semantic impact. Fixed: fix items. Removed: remove items. Security: security items. 跳过 chore(deps)、build(deps)、formatting-only docs 和 cache-only ci。Breaking change (#105) 带 ⚠️ BREAKING 前缀。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 加载了 changelog-gen（status.json skill_load_hits=2；transcript 先读取 SKILL.md），输出完整且正确分类所有条目，并准确跳过三类维护项；fixture-manifest 未被写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 加载了 changelog-gen（status.json skill_load_hits=2；transcript 先读取 SKILL.md），输出完整且正确分类所有条目，并准确跳过三类维护项；fixture-manifest 未被写入。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），作为对照其输出遗漏了若干标题清洗/格式细节，但不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | **PASS** | with_skill candidate.md 将 #101 放入 Added，并输出“**auth:** Add OAuth2 login support”。 | without_skill 也将 #101 放入 Added，但使用中文标题。 |
| `fix_fixed` | **PASS** | with_skill candidate.md 将 #102 放入 Fixed，输出“Resolve crash when token expires”。 | without_skill 也将 #102 放入 Fixed。 |
| `chore_deps` | **PASS** | with_skill 明确写入“已跳过：依赖维护（#103、#114）”，且正文无 #103 条目。 | without_skill 未输出 #103。 |
| `build_deps_skipped` | **PASS** | with_skill 明确写入“已跳过：依赖维护（#103、#114）”，且正文无 #114 条目。 | without_skill 未输出 #114。 |
| `perf_changed` | **PASS** | with_skill 将 #104 放入 Changed，输出“Reduce API response time by caching”。 | without_skill 也将 #104 放入 Changed。 |
| `feat_added_breaking` | **PASS** | with_skill 将 #105 放入 Added，并以“⚠️ **BREAKING:**”前缀标记。 | without_skill 将 #105 错放入 Changed，且未使用要求的 BREAKING 前缀。 |
| `docs_release_workflow_changed` | **PASS** | with_skill 将 #106 放入 Changed；其 SKILL.md 明确要求依据 release workflow、changelog preflight 等正文语义纳入。 | without_skill 也将 #106 放入 Changed。 |
| `test_eval_contract_changed` | **PASS** | with_skill 将 #107 放入 Changed；transcript 中加载的 SKILL.md 明确覆盖 eval contract/durable comparison 语义。 | without_skill 也将 #107 放入 Changed。 |
| `ci_release_gate_changed` | **PASS** | with_skill 将 #108 放入 Changed；其 SKILL.md 明确要求 release gates、required checks 等语义纳入。 | without_skill 也将 #108 放入 Changed。 |
| `docs_typo_skipped` | **PASS** | with_skill 明确写入“README 拼写修正（#109）”已跳过，且无 #109 条目。 | without_skill 未输出 #109。 |
| `ci_cache_skipped` | **PASS** | with_skill 明确写入“CI 缓存维护（#110）”已跳过，且无 #110 条目。 | without_skill 未输出 #110。 |
| `remove_removed` | **PASS** | with_skill 将 #112 放入 Removed，输出“Drop Python 3.7 support”。 | without_skill 也将 #112 放入 Removed。 |
| `security_security` | **PASS** | with_skill 将 #113 放入 Security，输出“Patch XSS vulnerability in template renderer”。 | without_skill 也将 #113 放入 Security。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `30.96s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `23.374s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `79.221s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
