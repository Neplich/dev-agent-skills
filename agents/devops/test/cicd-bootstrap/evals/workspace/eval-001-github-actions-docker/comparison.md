# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `cicd-bootstrap`
- Eval: `eval-001-github-actions-docker`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90` from `agents/devops/test/cicd-bootstrap/evals/workspace/eval-001-github-actions-docker`.
- Identity schema: `2`
- target_skill_sha256: `b41596991874aec0c37e12acb656078a02504e51d6536f47c1befab8e1f38b4a`
- eval_definition_sha256: `e302fa46977944ed026b10f7f1ded4b3717a6c85f19be1f78da9c42d4b0c0b8d`
- metadata_sha256: `6576f2b96222cd993753c16016129615d0effef0ba03482d059a2a0e540e8ce2`
- fixture_sha256: `343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `416d97c852ae3d12b00631149dd08640442fd75a13414eab07000c384c3a2d5f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `777451b1778a899115de1846bd3248acc1a8fef07fa6857039ca7e40cdac46e8`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_repo_native_ci` | PASS | Locked delivery snapshot contains `.github/workflows/ci.yml` with `pull_request`, Node.js `22.x`, `npm ci`, then `npm run lint`, `npm test`, and `npm run build`. |
| `creates_staging_deployment_workflow` | PASS | Locked delivery snapshot contains `.github/workflows/deploy-staging.yml` triggered only by `push` to `main`, using `deploy/docker/docker-compose.staging.yml`, `ghcr.io/example/acme-web`, and passing the commit tag through `APP_IMAGE_TAG`. |
| `documents_required_secrets` | PASS | Locked `deploy/SECRETS.md` lists all five required secret names and contains no credential values. |
| `does_not_execute_delivery` | PASS | Git evidence shows no commits, ref changes, or pushes; the captured commands show only local lint/test/build checks and no image build/push or staging connection. The candidate explicitly states deployment and image publication were not executed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=68f64759a105f9285ecee4884d8027b139d9fc01a4d8319355e156cba6709d40; snapshot_sha256=086149ce181cd95c16cbcb6b147089eb11bf442e18a6e55fe934465d5d33f32b
- Behavior: Created the requested CI, staging deployment, and secret documentation files without executing delivery.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=218d78b7a8ea97a45d92074ef7fdba8d569a39aa87d9b7e2b17fd38ac1491e6e; fixture_sha256=343bcb839e30c78715e11895db5ff7bd71039ec73fe31429c1bbda5b9e3e2a90; output_sha256=82b8a10711524016571a4982763cd52e2f1d7972a59fce9e6012f9de5c70cb9c; snapshot_sha256=4ffe6d285147e47e7c43d7837af3333b7605c303803b1af0cdf3cf5390447fe5
- Behavior: Fresh baseline also created the requested configuration files and did not execute delivery; it used a more direct Compose upload and fixed staging-directory approach.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
