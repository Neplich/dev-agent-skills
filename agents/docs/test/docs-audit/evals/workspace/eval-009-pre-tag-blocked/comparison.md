# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `7dbaa3390632c779b209a0992154e3a2f393b139ccab7a74c59a949526e90023`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | With_skill states that evidence must come from the resolved target_ref tree and treats staged, unstaged, and untracked changes as diagnostic only. |
| `blocks_every_in_scope_worktree_delta` | PASS | With_skill inventories staged routes, unstaged documentation and package.json, and the untracked audit draft, and concludes the inventory is blocked. |
| `performs_zero_audit_writes` | FAIL | Locked git evidence shows no writes, but with_skill explicitly says catalog-status may be marked verified despite the blocked branch. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | With_skill requires submitting or removing all scoped changes, confirming a clean workspace, resolving the updated target_ref, and rerunning the complete pre-tag audit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=1a9652fe6ea10240a1cbf1e06ba6ce6844c5a58463874b678ac8e1dd1c144f86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, uses target-tree evidence, inventories all scoped deltas, and specifies a full rerun, but incorrectly permits a page to be marked verified while blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=9a98646abd19e8822eac2bb109fa9664630cc939863e3139f7862aaa99b14900; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocks the audit and recommends committing changes and rerunning, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- A blocked branch must not mark any page verified; with_skill says catalog-status can be verified.
- Next: Do not mark any page verified while the audit is blocked; defer all page verdicts until the clean, updated target_ref is fully re-audited.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | with_skill 明确以 release-head 的目标 tree 为准，并将工作区未提交内容排除为诊断材料。 |
| `blocks_every_in_scope_worktree_delta` | PASS | with_skill 逐项识别了 routes.txt、catalog-items.md、package.json 和未跟踪审计草稿，并据此判定 blocked。 |
| `performs_zero_audit_writes` | PASS | with_skill 未判定 verified、未返回 ready_for_tag；锁定 git_evidence 显示 HEAD、分支、引用和提交均未变化。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | with_skill 要求提交或移出差异、更新 release-head、确认工作区和索引干净，并完整重跑 pre-tag audit。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=285676a37ff3c2b1561b23fc7aa2b4d0b885916cf0293eb3cb29fdfba174ec56; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定 blocked，排除工作区证据，并给出提交、更新引用、清理和完整重跑步骤。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=d31270dc3838db9cc9cb71d4e615bdc9d4fa081d70480ae2ffea27a8d79905b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞发布并识别目标 tree 与工作区差异，但重新检查建议较偏命令验证。
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
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | With-skill output resolves release-head to commit/tree, contrasts tree contents with workspace changes, and explicitly treats workspace content as diagnostic only, not pass evidence. |
| `blocks_every_in_scope_worktree_delta` | PASS | It identifies the staged routes file, unstaged affected page, modified package.json, and untracked audit draft, explains their scope, and concludes blocked. |
| `performs_zero_audit_writes` | PASS | The output does not claim verification or ready_for_tag, and locked git evidence shows unchanged HEAD/branch, no new commits, no ref changes, and empty delivery snapshot. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | It directs committing the confirmed implementation, affected pages, and version source, keeping workspace/index clean, using a new target commit, and rerunning the complete pre-tag audit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=90bc9288224821eab67f562d2b6ac0730288b7a44da74c55313a58784fffcfe7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly returns blocked, rejects all worktree/index/untracked deltas as audit evidence, records no mutation, and specifies a clean-commit/new-target/full-rerun path.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=14b0281c2804f42ad4f57e50a6210f536e638cc3412f2a6a695c400e51181be7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit and describes target-tree versus workspace evidence, but gives less explicit scope classification and rerun workflow detail.
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
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | with_skill 明确以 release-head 的 immutable commit/tree 为唯一通过依据，并将工作区/index/untracked 修改标为诊断材料。 |
| `blocks_every_in_scope_worktree_delta` | PASS | with_skill 识别了 staged routes.txt、unstaged catalog-items.md、modified package.json 和 untracked audit 草稿，并据此判定 blocked；change-map 命中的两个页面也要求重新核验。 |
| `performs_zero_audit_writes` | PASS | with_skill 明确 blocked、不得通过或返回 ready_for_tag；原始 git_evidence 显示 HEAD、branch、ref、reflog 和 result_diffs 均未变化。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | with_skill 要求提交所需实现、页面、版本来源和正式审计修改，使 release-head 指向新提交并确认工作树干净，再完整重跑 pre-tag 审计，不得局部续跑或补证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=3ad96dc9c12ef5fb1ee71e5cd92f87db3475722fd0009ebc33b812220ab04e44; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定 blocked，严格区分 target tree 与工作区证据，识别全部范围内差异，保持仓库不变，并要求清理、更新 target_ref 后完整重跑。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=9b2977aef7b86c5306ef510e7ebea1793a715c1c2128cae0c61941b716ae529c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定当前审计不能通过，并识别主要未提交/未跟踪修改及 target_ref 不包含这些事实；重新检查建议较完整。
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
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | with_skill requires facts from the immutable target_ref tree and treats all worktree/index evidence as diagnostic only. |
| `blocks_every_in_scope_worktree_delta` | PASS | with_skill identifies the staged implementation change, unstaged affected documentation and package version, and untracked audit draft, and concludes blocked. |
| `performs_zero_audit_writes` | PASS | with_skill returns blocked, forbids ready_for_tag and tag creation, and locked git evidence shows no branch, ref, commit, or worktree changes. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | with_skill requires committing the changes, updating release-head, confirming clean worktree/index, and rerunning the complete pre-tag audit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=34ada93f7c5d348ea2b09389a88a04f105d01bd083d97f059b9351aad97c4153; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, enforces immutable target-tree evidence, identifies all in-scope deltas, preserves state, and specifies a complete rerun.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=f50bd9550671b260f7b9584015661f051e1dcf720853336234bf6901a2652dca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly rejects approval and preserves repository state, but gives less complete scope classification and rerun requirements.
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
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e7c07749e1ccddc060263b8f3a4f43a48fd955320cdd49d95c38c2e2312093a6` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `e7c07749e1ccddc060263b8f3a4f43a48fd955320cdd49d95c38c2e2312093a6`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | with_skill explicitly requires passing evidence to come from the resolved target_ref tree and excludes workspace, index, and untracked files. |
| `blocks_every_in_scope_worktree_delta` | PASS | with_skill identifies all four porcelain states and treats the implementation, affected page, package version, and audit record as blocking scope differences. |
| `performs_zero_audit_writes` | PASS | with_skill concludes blocked, rejects ready_for_tag, and reports no audit writes or repository changes. |
| `requires_clean_commit_update_ref_and_rerun` | FAIL | with_skill requires committing the changes, updating release-head, and rerunning the full audit, but does not explicitly require confirming the scope worktree and index are clean before rerunning. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=e7c07749e1ccddc060263b8f3a4f43a48fd955320cdd49d95c38c2e2312093a6; output_sha256=0fa27ffb767bda3d1ffd71b3c541d2496b7bcf451aca70a11703ca66615d7674; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, identifies the relevant differences, preserves the no-write outcome, and gives a full rerun direction except for the explicit clean worktree/index confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=e7c07749e1ccddc060263b8f3a4f43a48fd955320cdd49d95c38c2e2312093a6; output_sha256=65f0a9a62cc382549d73dee2dbb1981a0d711cac3ee237b3b335e855b5084989; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit and distinguishes target-tree evidence from uncommitted workspace evidence; gives a rerun procedure but does not fully classify all scope requirements.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- requires_clean_commit_update_ref_and_rerun: the with_skill output omits an explicit instruction to confirm the scope worktree and index are clean before rerunning.
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

# Fresh Paired Validation: eval-009-pre-tag-blocked

## Evaluation target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`
- Validation time: `2026-08-03 22:40:00 +0800`（fresh re-baseline，issue #188）
- Fixture: 本轮工作区中的 `evals.json` prompt/assertions、`eval_metadata.json` 及其列出的 pristine fixture 文件
- Latest result: 本轮 #238 fresh 隔离重跑结论（2026-08-06），见上方 Overall result 与下方证据表
- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `PASS` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | PASS | 两条 lane 均指出 `release-head` 仍为 legacy dispatcher；`.eval/actual-diff.patch` 中的 table dispatcher 仅存在未提交差异，不能作为 target tree 证据。 |
| `blocks_every_in_scope_worktree_delta` | PASS | PASS | 两条 lane 均逐项识别 staged `src/catalog/routes.txt`、unstaged `docs/site/api/catalog-items.md`、untracked 审计草稿和 modified `package.json`，并判定阻塞。 |
| `performs_zero_audit_writes` | PASS | PASS | 两条 lane 均输出 `blocked`，明确不返回 `ready_for_tag`、不创建候选或修改主机文件；workspace 中也未发现候选/盖章产物。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | PASS | 两条 lane 均要求先提交或移出全部差异、更新 `target_ref`、确认范围干净，再从 pre-tag 流程第一步完整重跑，拒绝局部续跑。 |

本轮无 FAIL 断言。



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-20（fixture 身份文本变更前）：**PASS（4/4 assertions）**

## Run sources

- 2026-08-03（#188）fresh re-baseline：`with_skill` 与 `without_skill` 各自在隔离目录（`tmp/eval-runs/issue-188-docs/with_skill/` 与 `tmp/eval-runs/issue-188-docs/without_skill/`）的 pristine fixture 副本中独立执行，互不读取对方输出。
- `without_skill`: fresh baseline；仅读取本例 prompt、assertions、metadata 与 fixture，未读取或应用 docs-audit skill、Docs Agent README 或旧 `comparison.md`。
- `with_skill`: fresh candidate；完整读取 `docs-audit/SKILL.md`、`docs-audit/_internal/INSTRUCTIONS.md` 与 `agents/docs/README.md`，并在同 prompt/pristine fixture 下执行。
- fresh judge 读取冻结的双侧 candidate 与 assertions 判定（`tmp/eval-runs/issue-188-docs/judge/verdict.md`）；本轮没有复用历史 baseline、旧 comparison 内容或历史运行产物。

## Assertion review
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Without skill | With skill | Evidence and behavior |
| --- | --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | PASS | Baseline 能识别未提交 patch 不属于 `release-head`，不能作为通过证据。Skill §1 input gate 与 §4 step 2 进一步限定 passing evidence 必须是精确 target_ref tree 的 ordinary blob；工作区、index、untracked 和 later-branch bytes 仅可诊断。 |
| `blocks_every_in_scope_worktree_delta` | PASS | PASS | 两侧均逐项解析 porcelain：staged `src/catalog/routes.txt` 属事实证据，unstaged `catalog-items.md` 属 affected page，untracked candidate draft 属 authorized write path，modified `package.json` 属 required version inventory；每一项都独立阻塞。Skill 明确不需要调用方先把差异声明为 passing evidence。 |
| `performs_zero_audit_writes` | PASS | PASS | Baseline 在 dirty scope 下直接 blocked。Skill §4 step 2 和失败事务规则要求在建 candidate 前阻塞，不判页为 verified、不盖章、不建 candidate/anchor/discovery/handoff commit、不返回 `ready_for_tag`，并保持宿主 branch/worktree/index 原状。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | PASS | 两侧均要求维护者提交需保留的最终内容或移出全部 scope 内差异，再把 `target_ref` 更新到最终 commit、确认 scope/index 干净，并从输入解析开始完整重跑；Skill 明确不允许局部续跑或用补证修复本次尝试。 |

## Behavior summary
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

### With skill

在任何事实核对或审计写入前，完整列出四个独立 scope intersection，并将阶段判为 `blocked`。所有未提交内容仅作为诊断上下文；不会创建隔离事务或修改宿主状态。重跑条件覆盖全部差异处置、目标 ref 更新、scope 清洁确认和从头执行完整 pre-tag protocol。

### Without skill baseline

本例 prompt、release context 与 porcelain inventory 已清楚给出未提交证据和四类 scope 交集，因此 baseline 也能正确阻塞、保持零写入并要求完整重跑。Skill 的增益主要是把“任何 scope/authorized path/required inventory 差异都独立阻塞”和“只接受 target-tree ordinary blob”固化为不可绕过的协议。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With skill: 无 assertion failure。
- Without skill: 无 assertion failure。

## Next steps

- 无需修改 skill；保留本例验证 dirty scope 的 fail-closed 行为和完整重跑要求。

## Runtime artifact policy

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
