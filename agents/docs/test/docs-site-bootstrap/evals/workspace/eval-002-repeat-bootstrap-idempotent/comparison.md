# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `08c04fe57b81475dd890de6778e0567d043b2de7ae5ceb0392b2f8c748e60f69`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With-skill output reports zero new files, an empty git status, an empty git diff, and a clean work tree. |
| `reports_skipped_identical` | PASS | With-skill output reports all 42 assets as byte-identical and skipped, with 42 manifest records. |
| `preserves_existing_state` | PASS | With-skill output reports no created files or conflicts, clean Git state, and unchanged existing change-map/site assets. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=ccb22a1e11bfb4c2392115bea571adbf7bb00572b2ab69f33e1be4d061f31576; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Re-initialization is reported as idempotent: all 42 assets were skipped as identical, the manifest remained valid, and Git is clean.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=a65f10cb06c0f7a8c9639b6e892ab9344f3a1b62f6e7f2875c31885add21a672; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Baseline reports successful generation but leaves 38 untracked generated files, so its workspace is not zero-diff.
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
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `421f80bf3da30d58b5b544d4c2e96b4cfdc1446ea641a3ffc3d654e2472f3421`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | With-skill git evidence reports empty status, index diff, worktree diff, and unchanged HEAD; all 43 recorded hashes match the fixture, including the manifest. |
| `reports_skipped_identical` | PASS | The fixture manifest contains exactly 42 asset paths, all classified as skipped-identical; the with-skill output reports 42 byte-identical skipped assets and its recorded asset hashes match. |
| `preserves_existing_state` | PASS | With-skill evidence reports no Git or reference changes, and all recorded existing asset hashes match the read-only fixture. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=1b566b6ac69b6a7646a16b94e7ad752cc1cdd794b4eba2f856403d43bf7f2e61; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported and evidenced an idempotent rerun with 42 skipped-identical assets and a clean Git workspace.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=219004642334d3fd86d41d8b32fb56972f3d9199dafb7ce6c4e3f55baad9d7d1; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Reported no tracked-file diff but left 38 untracked generated files.
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
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `94e37af2ad7f4b39032db420d30845826ffa4c408edb8ffe671f400ff7e83f83`
- Skill overlay SHA-256: `09f32081fb5da19c616e5c124981201ff10d8f1031a9890f0577b1364fa9c83c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `b55dbc29e6b1365719d0847e8b8ceb11bcbcaa0b15d77aac44cd57ea26527a2b`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | with_skill reports zero-diff; locked git_status and git_diff are empty, and the manifest evidence matches the fixture's existing asset hashes. |
| `reports_skipped_identical` | PASS | with_skill reports all 42 static assets as skipped-identical and a 42-record manifest; fixture manifest independently contains 42 asset paths with that status. |
| `preserves_existing_state` | PASS | with_skill reports no conflicts or kept-as-is changes, clean Git state, and matching manifest/asset hashes; fixture includes the unchanged change-map, release metadata, pages, templates, configuration, and scripts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=3e1d7a4331ee80a633b25aa0821e819cb1df009e77c095f05cc392c0bf2580b3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported and evidenced an idempotent rerun: all 42 assets skipped-identical, manifest preserved, and Git remained clean.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=970626314f80eb97fc008436179e977f3b31875ef015d6a3dcce0205080e223e; output_sha256=1059b83f64eba41a5604b8b41ab5b47b4299535dee94c5fb26dc36c7d7e5ad7f; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Reported no tracked-file changes but created an untracked generated directory and did not establish the required 42-asset skipped-identical result.
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
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2f0004a415a9413ec4f04c88be670a46f49aae91bdfea7a5f5a1bd3994bc3a2`
- Skill overlay SHA-256: `e3264805b55d520c4492930be28050bfd749cd67b6530c8ad7ae5532a81dc597`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `67789de316a1ba3d112d33eabc20baa992cdfc352bddac2855c6bcc9a3f93650`
- Metadata SHA-256: `b55dbc29e6b1365719d0847e8b8ceb11bcbcaa0b15d77aac44cd57ea26527a2b`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | with_skill raw Git evidence shows unchanged HEAD/branch and empty status, index, worktree, and result diffs; all 43 recorded hashes match the fixture, including the unchanged manifest hash. |
| `reports_skipped_identical` | PASS | The with_skill output reports all 42 assets as skipped-identical with 0 missing, conflicts, or modifications; fixture manifest evidence contains exactly 42 records, all skipped-identical, and the candidate manifest hash matches. |
| `preserves_existing_state` | PASS | Raw evidence shows no Git or worktree changes, and every existing fixture asset hash—including metadata, pages, templates, configuration, scripts, and manifest—matches the candidate workspace. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=de845291fe31b3c3f68a99941044ca85a3df9455ff996ae9528cfa0e30a04911; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported and evidenced a 42-asset skipped-identical rerun with zero attributable Git/worktree changes and preserved manifest state.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=fcc19b16459c870ae88c109bb8b9342f99c5350916adc812250211d5ce6962e1; snapshot_sha256=1b323124e15340b551297f9dfa3a6372444f9d351e16047fe0f9bd65a9495fdc
- Behavior: Reported generated untracked output and did not establish the required 42-asset idempotent classification.
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
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `152b64c666428933a1e4cc6555b5ae40ea5c3e08c7fc1320bdd861942ed3733a`
- Skill overlay SHA-256: `256eb0ac5a55ca6fadf72afd9abf599973b2fa270458596afcc043a11cc688b6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d69da1ea23c3e19a3bb0fc90f80dd5c408b949a85124191f1000ce2477a1817f`
- Metadata SHA-256: `b55dbc29e6b1365719d0847e8b8ceb11bcbcaa0b15d77aac44cd57ea26527a2b`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | FAIL | with_skill reports zero-diff and raw Git evidence confirms unchanged HEAD, index, worktree, and no untracked files. However, neither the output nor raw evidence independently verifies that the pre-existing createdAt was preserved. |
| `reports_skipped_identical` | PASS | with_skill reports all 42 assets as skipped-identical; its workspace manifest contains 43 entries, consistent with 42 assets plus the manifest, and Git evidence shows no changes. |
| `preserves_existing_state` | PASS | Raw with_skill Git evidence shows unchanged commit, branch, index, worktree, and no untracked files. The manifest covers existing pages, templates, configuration, scripts, change-map, and release metadata. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=0b11a1f4731e7cab36b4c80f1187a6f0afd0aa04af18cfd6cce7975da0b725fa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported 42 skipped-identical assets, zero-diff, and clean Git state; createdAt preservation was not independently evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=264983134102ced305ff27d9a60ebf7a513bc64a8cc828e207e1541a5df9a7c4; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Generated 38 untracked .generated files and did not provide zero-diff or skipped-identical classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- createdAt preservation is asserted but not independently supported by the with_skill output or raw evidence.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-002-repeat-bootstrap-idempotent`.
- Fixture SHA-256: `81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba`
- Prompt SHA-256: `1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d69da1ea23c3e19a3bb0fc90f80dd5c408b949a85124191f1000ce2477a1817f`
- Metadata SHA-256: `b55dbc29e6b1365719d0847e8b8ceb11bcbcaa0b15d77aac44cd57ea26527a2b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `produces_zero_diff` | PASS | with_skill reports zero new files, zero unresolved conflicts, empty git status and git diff; the fixture manifest retains createdAt 2026-07-16T08:00:00+08:00. |
| `reports_skipped_identical` | PASS | with_skill reports 42 skipped-identical assets and a 42-record manifest. Raw fixture evidence contains 42 manifest file entries, all marked skipped-identical. |
| `preserves_existing_state` | PASS | with_skill reports no Git changes and zero kept-as-is conflicts; raw fixture evidence shows existing pages, templates, configuration, scripts, change-map, releases, and manifest assets. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=a70eafd0e42d11d5efd802490261615c2c4cc1ea8198fb8c723922d7b4c332fc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported an idempotent rerun: 42 skipped-identical assets, a 42-record manifest, zero Git changes, and zero-diff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1e8516931ef9c5300021c46d1671fb3fb195b5fe4d687cb8133fc778b15a0158; fixture_sha256=81fc070f4ad34328237a018c7882b4df392c1f8371f853eea4af158725fb66ba; output_sha256=4d4d958acde9d761caf2044d32ac40f7f6fc6b975a691d0de10e1264781cb425; snapshot_sha256=060c9f1e9bca54e39b34c9d582c0f4bb286da0cadf85ff1b87aaced36e86fce0
- Behavior: Reported no tracked modifications but introduced 38 untracked generated files under docs/site/.generated/ and did not establish the required 42-asset skipped-identical result.
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
- Eval: `eval-002-repeat-bootstrap-idempotent`
- Review context: cumulative API, Database, Product, Design, and Ops deployment layering fixture refresh from PR #164 and PR #166

## Test Set / Fixture Version

- Fixture: `2026-07-ops` (cumulative from `issue-122-assets-v2-c5r`)
- Scope: 9 materialized targets; all omitted targets are explicitly assumed present and byte-identical to the current 40-file inventory
- Dependency fact under review: the representative `package.json` VitePress declaration is pinned exactly to `1.6.4`
- Asset refresh under review: materialized `standards/templates/api-template.md`, `standards/templates/database.md`, and `standards/templates/ops-runbook.md` match the current packaged assets; Product, Design, and Ops deployment layering in `standards/doc-granularity.md` plus `ops/index.md` remain covered by the explicit omitted-target assumption
- Actual validation date: `2026-07-22`

## Latest Result

**PASS（3/3 assertions）— 历史结论（适用旧 fixture），已被上方 fixture-stale BLOCKED 取代**

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— fixture stale 导致成功断言未执行
- Overall result: BLOCKED

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `produces_zero_diff` | PASS | PASS | 两条 lane 的工作区文件哈希均稳定，manifest 的 `createdAt` 保持为 `2026-07-16T08:00:00+08:00`；未发现重写后的文件内容。 |
| `reports_skipped_identical` | NOT_EXERCISED | NOT_EXERCISED | 已提交 fixture 与源资产哈希不一致，skill 正确报告冲突；在 fixture 修复前无法执行 byte-identical / `skipped-identical` 成功断言。 |
| `preserves_existing_state` | PASS | PASS | `standards/change-map.yaml` 与 `.meta/releases.json` 均存在，内容分别保持源资产哈希 `014f624…`、`c906ead…`；manifest 的既有 `createdAt` 也未被重置。阻塞时未写入宿主状态。 |

未触发断言：`reports_skipped_identical`。

Fixture 阻塞说明：已提交 fixture 的源资产（feature-design.md / product-handbook.md）与工作区哈希不一致，skill 如实报告冲突（未伪报 skipped-identical）属正确行为；需更新 fixture 后重跑。



## Current Asset-Set Status

- The retained PASS above is the historical result for the former 40-asset, five-template inventory.
- The current packaged asset set contains 42 assets and six templates after
  adding `standards/templates/manual-guide.md` and `manual/index.md`.
- The #238 paired rerun and independent judge exercised the current contract, but detected that the committed fixture no longer matches the packaged source assets. The current result therefore remains `BLOCKED` until the fixture is refreshed and rerun.

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `produces_zero_diff`: PASS. All nine materialized targets compared byte-identical to packaged assets; before/after SHA-256 sets and manifest hash `0bb02c44054da996a17a489f0453ced2c03cde6b9bf757d4a035ac5f3e90017b` matched, and `createdAt` remained `2026-07-16T08:00:00+08:00`.
- `reports_skipped_identical`: PASS. The nine representative paths remain persisted as `skipped-identical` in the existing manifest; refreshed `api-template.md`, `database.md`, and `ops-runbook.md` respectively match current assets at SHA-256 `d5186c628d6b9967f9343b22ac60e7b2a275ee70085523c133859cf696153231`, `da5fecfea765dce8cac4e0289d0371d34eca5bf6038589d024da8ae8946ff424`, and `038a8578d48f5d40bd4db74de96e1013524dba94e25f26f763285bd943ab88e4`.
- `preserves_existing_state`: PASS. `standards/change-map.yaml`, `.meta/releases.json`, standards pages, templates, package metadata, manifest, and all other fixture content remained unchanged.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Source: fresh PR #164 review round 7 and PR #166 validation lanes under `tmp/eval-runs/pr164-review7-s4MWVn/with_skill` and `tmp/eval-runs/issue-161-review/eval-002/with_skill`, each executed by a new `codex exec` validation subagent using the current target skill, required internal inventory rules, the eval prompt, and a copied minimal fixture.
- Applied the 40-file inventory and persistent manifest rules while honoring the fixture's explicit omitted-target byte-equivalence assumption.
- Exact comparisons for all nine materialized targets returned equal; manifest read-back preserved all nine `skipped-identical` dispositions and the original timestamp.
- The refreshed materialized `api-template.md`, `database.md`, and `ops-runbook.md` matched their current packaged assets exactly. Product, Design, and Ops deployment layering in `standards/doc-granularity.md` plus `ops/index.md` are not materialized targets and remain within the fixture's explicit omitted-target byte-equivalence assumption.
- The representative package declares VitePress exactly as `1.6.4` and remained byte-identical to the current packaged asset.
- The fixture intentionally omits scripts, the lockfile, and most of the complete site, so host tests and builds are not applicable. Validation used exact asset comparisons, manifest parsing, and before/after content hashes; no complete-host checks are claimed.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh baseline lanes under `tmp/eval-runs/pr164-review7-s4MWVn/without_skill` and `tmp/eval-runs/issue-161-review/eval-002/without_skill`, each regenerated by its corresponding new `codex exec` validation subagent with the identical prompt and copied fixture; target skill, Docs README, internal instructions, packaged assets, old comparison, and with-skill output were prohibited in these lanes.
- Result: `PARTIAL / NO-OP`. It confirmed the nine materialized files, existing manifest shape and dispositions, fixed `createdAt`, and an unchanged before/after hash set, but could not perform a real asset-aware bootstrap without the target protocol or asset bytes.
- No historical baseline was reused. It could observe the fixture's existing `skipped-identical` declarations but could not independently prove host-to-asset byte equality; the with-skill lane supplied the authoritative inventory and asset-mapping evidence needed for the complete PASS.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures or blocked checks.
- Host docs tests and builds are not applicable to this deliberately minimized fixture because the scripts, lockfile, and full site are not materialized.
- The baseline's missing runner and inventory source limit it to `PARTIAL`; this does not affect the complete with-skill byte and manifest evidence.

## Next Steps

- Refresh the stale materialized fixture from the current 42-asset, six-template
  inventory, then run a new paired validation and independent judge before restoring a PASS result.

## Runtime Artifact Policy

- Runtime copies, checksums, lane reports, and subagent verdicts remain under `tmp/eval-runs/pr164-review7-s4MWVn/` and `tmp/eval-runs/issue-161-review/eval-002/` and are not submitted.
- Only this durable comparison is retained; no runtime output, dependency directory, generated site, transcript, candidate, verdict, timing, or diagnostics are committed.
