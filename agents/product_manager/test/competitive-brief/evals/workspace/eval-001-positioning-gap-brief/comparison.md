# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-001-positioning-gap-brief`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-001-positioning-gap-brief`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `9482baaf8c9e8ed2c6d5d65dd72ca668fb6cc639dacfe10c14d42e2f2d0f4c53`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | With-skill output separately covers Linear and Jira positioning, target users, and core selling points in sections 2–4 and the comparison matrix. |
| `messaging_gap` | PASS | With-skill output identifies five explicit messaging gaps plus concrete content opportunities in sections 6–7. |
| `evidence_boundary` | PASS | With-skill output explicitly distinguishes category-level opportunity analysis, judgment-based weaknesses, public facts, and items requiring price verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4a08efe07d313da50417d9ae8b7dc4b8c402ce46b94b60ff18392de7f6c67297; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a structured Linear-versus-Jira competitive brief covering positioning, users, selling points, messaging gaps, content opportunities, and evidence qualifications.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9e067866ab87b79bc38902e6c76e95cf800dcfd8ede63c7bb27b48f5dd946b47; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also delivered a complete competitive brief with positioning, users, selling points, and messaging gaps, but used less explicit evidence-boundary qualification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
