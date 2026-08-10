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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `9482baaf8c9e8ed2c6d5d65dd72ca668fb6cc639dacfe10c14d42e2f2d0f4c53`
- Eval definition SHA-256: `97a23b71b146f4c0d34488da4fd45ddfa63b73d91d16deb5d2e03fbe4f5d01f6`
- Metadata SHA-256: `253b7cd58ea1d83c5776d9de8bd0332f1de43ff8d162b4ae1c25de74c0394acf`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `positioning` | PASS | With_skill output separately describes Linear and Jira positioning, target users, and core selling points in the positioning comparison and competitor profiles. |
| `messaging_gap` | PASS | With_skill output identifies multiple messaging gaps and content opportunities, including context continuity, cross-functional collaboration, simplicity versus governance, project health, and AI collaboration quality. |
| `evidence_boundary` | PASS | With_skill output explicitly labels the company context as unavailable, frames the recommended entry point as a hypothesis, and marks several judgments as requiring customer validation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=492069627ede798bb4c6974dc87de7fded774a8dc09f89e227a7ca734c804214; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a comprehensive, structured Linear-versus-Jira brief covering all requested areas with explicit hypothesis and validation boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=adf7889b0d876e991ee47320ba8f46f60cd10315ed2d153b1c81fce9f52aed9b; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fda0bff7f4205dc63e02e41246bd691d5022ce77e23f097405f342888e8cb038; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Delivered a shorter brief that covered the core comparison and messaging gaps, with less explicit evidence-boundary framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
