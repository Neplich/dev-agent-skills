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
- target_skill_sha256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- eval_definition_sha256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- metadata_sha256: `d30677e1d058f7ced7ac6b80a07136e834c175a519dc8964e75c167556348374`
- fixture_sha256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the mapped health document was read after mapping resolution, with no traversal of unrelated site documents. |
| `verifies_against_code` | PASS | The delivered incident response file states the document says 3, verifies src/runtime/health.rules as 5, and explains the two-failure timing and escalation impact. |
| `treats_unverified_as_low_trust` | PASS | The delivered file identifies last_verified_version: unverified as low trust and bases the threshold on src/runtime/health.rules, while noting missing deployment evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=5ba63e6ec63835be342e1d2cb9d54aab17316f38c7259c25a23c5a48352b117f; snapshot_sha256=d9eea1489c17f372a1bd7343e0b4caa59339d2e85560ed79b497fb89a703bbdf
- Behavior: Created evidence-backed incident response guidance, verified the threshold against code, and bounded unsupported rollback claims.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=f89f0211d54e7e72a6ef80e935b8717b6837275489b4028214193e5e225c5e24; snapshot_sha256=d5222ff6169b45c8b26859a73e43e2970ed5997330dbb04bd75b9329d326dfda
- Behavior: Updated the mapped health document with the code threshold and generic response/rollback steps, without explicitly addressing the document's unverified trust level or threshold impact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
