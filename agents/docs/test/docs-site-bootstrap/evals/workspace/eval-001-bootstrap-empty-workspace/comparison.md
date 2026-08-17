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
- target_skill_sha256: `2846695e854af26b77f56804bd16db1050e2bacd34407999d119ed4e4a881599`
- eval_definition_sha256: `0028d93b645e269e09fc6f6345ad073b0c2386395ad858bbd7693d057a9eca5f`
- metadata_sha256: `72695cba8eaf9810a85aa17ba3cc9622de1dd39f4d06db93fe0728a19509d73b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `373ba2965836f0cc6198ffb0151c12c61c34831fe45aaa5ef665fae7d893acbc`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c4382a755d40b4c37cbb5843089f99a5655b439fd2c6460df6c8b5adeb479967`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_complete_inventory` | PASS | Raw trace and manifest show 42 assets, 42 manifest entries, and byte mismatches: []; manifest covers every processed static asset. |
| `delivers_deterministic_scaffold_assets` | PASS | Snapshot contains package.json with a single new:doc command, scaffold-doc.mjs, its test, six templates each with one docs-scaffold block, and standards/index.md links to all six. |
| `validates_seven_frontmatter_fields` | PASS | All 19 Markdown pages in the snapshot contain the seven fields; doc_type values are within the allowed set and owners/related_code arrays are non-empty. The frontmatter checker is delivered, though test:docs could not run because fast-glob was unavailable. |
| `writes_only_docs_site` | PASS | Workspace status is only ?? docs/ and the delivery manifest contains only docs/site paths; no root configuration, source, or outside-docs/site files are shown as generated. |
| `requires_explicit_opt_in` | PASS | The user prompt explicitly confirms initialization in the current repository at docs/site/, and the trace records that confirmed host, fixed root, complete scaffold, and manifest were the write scope before generation. |
| `reports_manifest_readback` | PASS | The manifest was parsed and read back; trace reports 42/42 byte checks and a repeat classification of 42 skipped-identical, 0 created, 0 kept-as-is, with zero content changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=de699aabf45dbd24786ec9e07c25be10777d63769db3406bad89333f14c74b85; snapshot_sha256=bca774aac096fb9150e4d2f90f2f5b252b12b5d7c7b76e21033c1ecfd23bc3bd
- Behavior: Delivered the complete 42-file deterministic docs/site scaffold, manifest, validation tooling, and readback/idempotency evidence; runtime docs tests were blocked by a missing dependency.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8294223a6cc9320411b7f3ca9761133eeb49b555e990170abcfa40eeb8076bd8; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=47773e521aeba4c8d3b61da010f4b455e32437ea33c7703ae2fca34b6c81b1c1; snapshot_sha256=332f818b69be4a217aaa7ec2bb90c9df0fe097e434c0944e67695d339b6cdc8c
- Behavior: Fresh baseline produced only a small static landing site, added package.json and scripts outside docs/site, and did not provide the required 42-file scaffold, manifest, frontmatter system, or opt-in workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install dependencies and run test:docs when available.
- Next: After a confirmed commit, perform the pending deployment completeness check and choose integrated, independent, or deferred hosting.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
