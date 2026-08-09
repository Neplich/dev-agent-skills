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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
