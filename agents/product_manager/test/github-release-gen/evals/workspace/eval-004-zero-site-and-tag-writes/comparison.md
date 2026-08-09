# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-004-zero-site-and-tag-writes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-004-zero-site-and-tag-writes`.
- Fixture SHA-256: `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626`
- Prompt SHA-256: `1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `80b618e955757ddc076d881c72f5f8be648700b5dd3e7c6b222dd59ecfccd495`
- Eval definition SHA-256: `266baf4d19e4ef318c97a6eab3bf8e029fbe8357edfa824c6d453c40e91b2d33`
- Metadata SHA-256: `12fc2cb8802eb1dba2db5f0429fdb4322d489582597f6f44ee10596dc46d8d26`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_write_docs_site` | PASS | with_skill 明确说明未修改站内版本说明、版本索引，未运行 test:docs，并将站点证据补齐交由上游 agents。 |
| `does_not_mutate_tags` | PASS | with_skill 明确说明未创建 v1.0.0 tag，并将实际创建交给 release owner。 |
| `avoids_gh_release_create_without_tag` | FAIL | with_skill 明确禁止在 tag 缺失时执行 gh release create，且证据显示无远端 tag、无既有 draft；但未提供完整 release preview。 |
| `reports_zero_mutation_boundary` | PASS | with_skill 明确报告站内版本说明、版本索引、tag 和 GitHub Release draft 均未写入；git evidence 也显示无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=3d7c00d6c0138533d018afb5e3973b5fc3dfe2e264d8a9fc0d0827bceddc08c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 拒绝所有站点、tag 和 GitHub Release 写入，并报告零变更边界；但缺少完整 preview。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=f35016d943fa978f23e21af2c3e8db5f2fd90239add7ddd5e034b2f909124bc2; snapshot_sha256=6ca063d554b4b2d19925ea5394ea7702d95b28d11a977ac85a4ddf5672cc9452
- Behavior: 修改 docs/site、提交变更并创建本地 tag，未创建远端 draft。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未保留完整的 GitHub Release draft preview。
- Next: 在不执行写入的前提下补充完整 GitHub Release draft preview。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
