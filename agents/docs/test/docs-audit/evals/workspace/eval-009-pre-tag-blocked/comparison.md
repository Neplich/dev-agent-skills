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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
- Judge schema SHA-256: `7dbaa3390632c779b209a0992154e3a2f393b139ccab7a74c59a949526e90023`
- Eval definition SHA-256: `d573477cbe6d660b40a0fd1ef0416d1d407e28ca525b29d8ef8303b282fe7f56`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | with_skill 明确将审计绑定到 immutable `release-head` commit/tree，并明确工作区、index、patch 和草稿不能替代 target tree 证据；同时指出目标 tree 仍是旧实现和旧版本。 |
| `blocks_every_in_scope_worktree_delta` | PASS | with_skill 逐项识别了 staged `src/catalog/routes.txt`、unstaged `docs/site/api/catalog-items.md` 与 `package.json`、untracked `docs/site/.meta/audit/audit-v1.2.0.md`，并据此判定阶段 `blocked`。 |
| `performs_zero_audit_writes` | PASS | with_skill 返回 `blocked`，明确不得返回 `ready_for_tag`；锁定 git evidence 显示 HEAD、分支、ref、提交和 reflog 均未变化，且无 result diffs 或新提交。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | with_skill 要求维护者保留并提交或移出全部差异、更新 `target_ref`、确认 index 和 worktree 干净，然后从输入解析开始完整重跑 pre-tag audit，并明确不能局部续跑或复用草稿/patch。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=3732a8f2cd12834ca8a56d7999f03706e8205a992547a5f31fec88002bd046b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定未提交 scope 差异导致 pre-tag audit blocked，区分诊断证据与精确 target tree 证据，并给出完整重跑条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=cf46b72dc6ee6df1371af133a1c7394b6ce63c5cab138d29d667b26ccaad3121; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样判定 blocked 并识别主要差异；作为 fresh baseline，其复查步骤较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
