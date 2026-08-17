# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- metadata_sha256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- fixture_sha256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `13218ab4a7abff52fb220f782ffa27173bde4d7c9a5b1ae26ef3115112e26b3d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | With-skill preview includes all confirmed feature, compatibility, database, deployment, asset, upgrade, risk, and old-browser facts from the locked fixture without contradicting them. |
| `adds_verified_traceability_links` | PASS | It includes the intended v0.9.0...v1.0.0 compare link, PR #116 and #117 links, commit 8b6a1f2, and contributor links for Alice, Bob, and Carol. |
| `curates_instead_of_dumping` | PASS | The preview selects three representative maintenance links and does not paste the 18-commit maintenance feed. |
| `blocks_on_fact_conflict` | NOT_EXERCISED | The locked fixture contains no GitHub-versus-site fact conflict, so conflict blocking is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=d0443c22761e1de09fd03366ddb164158be56b2b599c8a5ca7debeb69c247984; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a fact-preserving, curated inline release preview with verified traceability links and correctly remains blocked from publishing before the target tag exists.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=cb8e2857c52bbfa9171e76d6b454a82abedad71443c937f7b9dfb8d1dd7d47fc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a concise preview preserving the main facts and representative links, but omits contributor links and the stronger release-gating context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Create the target v1.0.0 tag and complete the required post-tag audit before any publish/readback workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
