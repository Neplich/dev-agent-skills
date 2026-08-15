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
- Identity schema: `2`
- target_skill_sha256: `f325a3bc283b067240ee3d50726f680693f5cd996590e717b72af686853dbf3e`
- eval_definition_sha256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- metadata_sha256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `373ba2965836f0cc6198ffb0151c12c61c34831fe45aaa5ef665fae7d893acbc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8a54b9d8ab53e6a7ef3187af8e3063aff036e0d1740a4b832c4d3a33058de445`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | Locked trace reports readback of 42/42 assets with byte equality, and the manifest contains 42 matching paths, all marked created. |
| `delivers_deterministic_scaffold_assets` | PASS | Locked snapshot contains package.json with one new:doc script, both required scaffold files, six templates each with exactly one start/end docs-scaffold block, and standards/index.md links all six templates. |
| `validates_seven_frontmatter_fields` | PASS | Direct inspection of all 19 Markdown snapshot files found all seven fields, allowed doc_type values only, non-empty owners and related_code arrays, and last_verified_version set to unverified. |
| `writes_only_docs_site` | PASS | All 43 delivered snapshot files are under docs/site/, and locked git evidence shows only untracked docs/ content with no root or external modifications. |
| `requires_explicit_opt_in` | PASS | The prompt explicitly confirms the current repository, fixed docs/site root, and complete scaffold; the with_skill output explicitly records that opt-in before reporting writes. |
| `reports_manifest_readback` | PASS | Locked trace shows manifest JSON parsing, path/status validation, 42/42 byte readback, no conflicts, and a repeat classification with manifestUnchanged true and zero-diff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c7193c48e96072b41f1a09aff5042307f10256cb3a768a4ff24c9ef0cd6a3d43; snapshot_sha256=f836057223cddf83c406a99d35d284c9afbae342612132073d1423288e8d673c
- Behavior: Delivered the complete 42-asset formal documentation scaffold, manifest, frontmatter-compliant pages, deterministic templates, and readback/zero-diff evidence under docs/site/.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=90ff7d951d837568007090f488367743f82afd2c8efe646c79cf8d8cbabd0d47; snapshot_sha256=650a862275be16ace959dabe84710215a9278b8893300a1432df1826c4d9327e
- Behavior: Fresh baseline created a small Docusaurus scaffold without the required 42-asset inventory, manifest, formal frontmatter contract, or deterministic document scaffold.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
