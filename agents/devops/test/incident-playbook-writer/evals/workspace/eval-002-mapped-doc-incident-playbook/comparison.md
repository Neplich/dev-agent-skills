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
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `5d95ff5039100f2131c72122b091ff4a172f65d45070290345e8a658862159d4`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | runner_captured_trace shows the mapped health document and code were inspected without traversing unrelated site documents. |
| `verifies_against_code` | PASS | The with_skill output explicitly contrasts the document's 3-failure claim with the code's 5-failure threshold and explains the effect on alerting, escalation, and rollback timing. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly treats last_verified_version: unverified as low trust, relies on the code for the threshold, and refuses to invent rollback commands without deployment evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=f620455c9a8154e61451ea16fe901f6dd74023c42fbd35ca28c46e7f68362e71; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performed evidence discovery and threshold verification, then blocked runbook generation pending operational context.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=d31dfa6feb000c7bbf99c4963dbae61851a4a1229cf3ec47f4e036d43a6b2792; snapshot_sha256=12185e216614fd50c621cf9e43a2de9f54828f81f5593af3b3de65fdb457548d
- Behavior: Updated the mapped health document with the code threshold and generic response/rollback guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the confirmed PM/DevOps handoff packet and select the required playbook(s).
- Next: Provide deployment and rollback evidence so the operational steps can be completed.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
