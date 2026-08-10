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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- Skill overlay SHA-256: `2f0de1beb8d9a238bffa058ef4ccfb94546f593a81b4fc6e5c1f6bcddf8dbe71`
- Judge schema SHA-256: `80b618e955757ddc076d881c72f5f8be648700b5dd3e7c6b222dd59ecfccd495`
- Eval definition SHA-256: `266baf4d19e4ef318c97a6eab3bf8e029fbe8357edfa824c6d453c40e91b2d33`
- Metadata SHA-256: `12fc2cb8802eb1dba2db5f0429fdb4322d489582597f6f44ee10596dc46d8d26`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_write_docs_site` | PASS | with_skill 输出明确说明未执行站点修改，并表示不能代替 Docs owner 修改站点或运行检查。 |
| `does_not_mutate_tags` | PASS | with_skill 输出明确说明不能创建 tag，并将创建 v1.0.0 的下一步交给 release-owner；git_evidence 显示 refs 未变化。 |
| `avoids_gh_release_create_without_tag` | PASS | with_skill 输出识别 tag 缺失时禁止 gh release create，并仅保留完整 inline preview；raw trace 未显示该命令执行。 |
| `reports_zero_mutation_boundary` | PASS | with_skill 输出明确说明未执行站点修改、tag 创建或 GitHub draft 创建，并报告 actual_tag 为 absent、draft_command 未执行；git_evidence 显示 HEAD 和 refs 均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=5c65567c915f3affb667f91db806d101dd612f6b62d18ac5b86bc5a5546c6c90; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只读检查并保留完整 inline preview，拒绝站点、tag 和 GitHub Release 写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=96b11d9293a9fee02576c477ae6ba77e8baa57a2dff031fc1bdf413b8c1f2d28; snapshot_sha256=e8d3c1d2609ab3a0c794b7052148ea7820ef9312eb4f545490c21abe63c93c99
- Behavior: 修改 docs/site、创建提交和 tag；未创建 GitHub draft。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
