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
- target_skill_sha256: `dcee4cc39c2fa28ea4046f8b10ceca0528d9458efc81ffb2c28e21e284fe034f`
- eval_definition_sha256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- metadata_sha256: `c28ce2010bd179e2122284ba3710d5b5dd600f47e70a10f6ca7f48b43c5aac3a`
- fixture_sha256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5d95ff5039100f2131c72122b091ff4a172f65d45070290345e8a658862159d4`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill trace shows multiple skill/handoff scans before the command that reads `docs/site/api/runtime-health.md`; that command reads the change map first, so the required mapped-document-first order is contradicted. |
| `verifies_against_code` | PASS | The with_skill output explicitly distinguishes the document's 3-failure claim from `src/runtime/health.rules`'s 5-failure threshold and explains that the stale document would delay detection, escalation, and rollback. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output treats `last_verified_version: unverified` as low-trust navigation, uses the code value for the alert threshold, and refuses to invent rollback commands because no deployment or rollback evidence exists. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=350a44d322a8f9e88ce0f7cbed4c3fa88bce7639d35c91aceae0c61fc79c70af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verified the 3-versus-5 threshold discrepancy, described its operational impact, and treated unverified documentation as low trust, but blocked the runbook and read the mapped document too late.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=defc2603df307ceb96e283d7c81fb767936c6a65046cdd420ba2a077bc451819; snapshot_sha256=e249b7f8fdcccc2a1ee0dbf4d498ab29650bd4e844de112e31c6ef0ba315d93a
- Behavior: Created and delivered an updated health document with threshold correction and minimal incident/rollback guidance; comparison-only context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane violated the required mapped-document-first read order.
- Next: Read `docs/site/api/runtime-health.md` immediately after identifying the code target, then verify its claims against `src/runtime/health.rules` and available rollback evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
