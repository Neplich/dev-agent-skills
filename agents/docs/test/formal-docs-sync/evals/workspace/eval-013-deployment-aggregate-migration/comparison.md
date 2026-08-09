# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-013-deployment-aggregate-migration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-013-deployment-aggregate-migration`.
- Fixture SHA-256: `13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4`
- Prompt SHA-256: `ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `cb68cc7396b4ed1007a2bd5b5970baa015053110168fade98a969dbebc84c1b1`
- Eval definition SHA-256: `2adf472912fe37066628cc2da23affed241d146a6c7c80728c7df93b4f2fccc7`
- Metadata SHA-256: `24118b2c28e807c2d8787e545057d4e67c26fd6313bf8abe3b22a58982fbfa17`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `migrates_aggregate_path` | PASS | Locked delivery snapshot deletes docs/site/ops/deployment.md and adds deployment/index.md, environment-reference.md, and development, docker, and kubernetes-helm page trees. |
| `repairs_inbound_and_internal_links` | PASS | Locked files update both inbound links to deployment/index.md; the new root links resolve to all class pages and environment-reference.md, and no residual old aggregate links remain in the checked files. |
| `updates_change_map_without_data_loss` | PASS | Locked change-map content maps each deployment glob to root, shared environment, and class pages while preserving custom_owner_field, exclude, and the unrelated src/product mapping. |
| `updates_navigation_atomically` | PASS | With-skill evidence records npm run test:docs exit 0, git diff --check exit 0, no formal old-path remnants, and a coordinated snapshot containing navigation, moved pages, links, change-map updates, and consolidated facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=5077aba73143ee46ad58b2537d4287c8cc783ec52d5e442329da8c295c7d1e47; snapshot_sha256=b8fb2a9995e508f6e4d33f6242c40730a14a000f80bbbce82f83a0c1d13afc87
- Behavior: Completed the migration with the full page tree, repaired links, expanded change-map entries, preserved fields, and passing documentation tests.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ef6288663966feaaf953d5b243a6dc9ee464a3ae22e56d91ba3c5352bb37ed40; fixture_sha256=13971a8a2ce22367dc9a9017e6a9d07e4a46c704998bfe1f7035f4fbe3557cf4; output_sha256=d89c40f4b13f317991a77ee7fe6cfb2a0eaf54eb5e2c4b159b4a5bba10b340dc; snapshot_sha256=f671f7d7dc033436c1d9f37a04972c40a4df0ccef01fe720f7f0b0d0399a9dee
- Behavior: Deleted and split the aggregate page and repaired basic links, but mapped each category only to its class page and omitted root/shared pages from required_docs.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
