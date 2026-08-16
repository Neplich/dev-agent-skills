# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`.
- Identity schema: `2`
- target_skill_sha256: `50cae2b4bb9c10d0d200f08d68ca4dd9d27b329f1a2b94cb2b8cb7333b3815ce`
- eval_definition_sha256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- metadata_sha256: `c28ce2010bd179e2122284ba3710d5b5dd600f47e70a10f6ca7f48b43c5aac3a`
- fixture_sha256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `f3eab55f60df9bb2b74211b8616c657af594a2e8a1c83328a335347ab9dd3bf1`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill stopped at its PM/DevOps handoff gate before inspecting repository documents; read-order execution was not reached. |
| `verifies_against_code` | NOT_EXERCISED | with_skill did not inspect src/runtime/health.rules or produce threshold guidance because the required handoff context was absent. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | with_skill did not reach operational guidance generation, so handling of the unverified document could not be exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=f3e2c8a6f1249005a510933f97cb04ee1a8a935c16409c64a874b43e2aa6bd7e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the specialist entry gate and requested the required handoff context; no repository mutation occurred.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=6cba89a4d0faab106e930c9fd2c42e6ab9754e263f9ec5ab6aecbe08e0063b12; snapshot_sha256=a19e52e9415a4bdaf4bde9822d98b92c8123411d4426e3eeee062e0efca7a1c8
- Behavior: Read the mapped documentation and code, identified the 3-versus-5 threshold mismatch, and delivered an updated health document with response and rollback guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the confirmed PM/DevOps handoff packet, then perform the repository verification and documentation update.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
