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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `b193497852920517172f09f5d68ba6d13d4646f7f71948ca300566e66c51cb59`
- Judge schema SHA-256: `373ba2965836f0cc6198ffb0151c12c61c34831fe45aaa5ef665fae7d893acbc`
- Eval definition SHA-256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- Metadata SHA-256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | With-skill raw evidence reports 42 asset files, `cmp` verification for all 42, and a manifest containing 42 `created` records under `docs/site/`. |
| `delivers_deterministic_scaffold_assets` | PASS | The delivery snapshot contains `package.json` with exactly one `new:doc` script, both required scaffold scripts, six template files with one scaffold block each, and `standards/index.md` links all six templates. |
| `validates_seven_frontmatter_fields` | PASS | All formal Markdown pages in the delivery snapshot contain the seven required fields with allowed values and non-empty arrays for `owners` and `related_code`; `last_verified_version` is `unverified`. |
| `writes_only_docs_site` | PASS | The locked workspace manifest and git status show generated files only under `docs/site/`; no root-level or outside-site generated file remains. |
| `requires_explicit_opt_in` | PASS | The with-skill trace explicitly records the confirmed current repository, fixed `docs/site/` root, and complete scaffold/manifest opt-in before writing. |
| `reports_manifest_readback` | PASS | Raw evidence parses the manifest, confirms 42 records with valid statuses, compares all 42 assets with zero conflicts, and reports `zero_diff=yes` on repeat verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=23c618c1d2d7bca50f175c29cb72b494b5cb5a3e604e35babc4b5b396fc6e705; snapshot_sha256=40598b1fb0713e774080d69bb7949777c3fd9e6856e60766deac03c4712a56cd
- Behavior: Completed the requested formal docs-site scaffold with manifest, validation assets, and repeat-run verification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8208757af0fda98f4a781fa685e53cb85bf7a2009c2f5a5dbd20ee4076c9f68e; snapshot_sha256=7848c62ad6db7e19b8ccd846d59f817b745961858b154ca6b5e169fc07cc1a41
- Behavior: Created only a minimal VitePress site and did not deliver the requested scaffold inventory, validation, or manifest.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
