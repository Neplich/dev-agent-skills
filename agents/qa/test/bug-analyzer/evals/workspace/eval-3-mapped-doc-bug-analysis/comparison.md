# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Identity schema: `2`
- target_skill_sha256: `f7992d17a0646109f134e112dee5a8d92a38fd3d8cf3007564f0979ffbd3929d`
- eval_definition_sha256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- metadata_sha256: `98bdccb4e3241d7facbaf94d94c2edbbe1adcec302e237e84c10d586748147c6`
- fixture_sha256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `27a39b82b995acb5c798df074b3eb2e54e5b81ea6292feb84f2c09cf3d65fb1c`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the change-map was read first in the targeted evidence command, followed immediately by the mapped notification document; no unrelated site-document contents were traversed. |
| `verifies_against_code` | PASS | The locked delivery snapshot directly records `max_retry_attempts = 2`, the document statement of up to 3 retries, their numeric inconsistency, and the unresolved counting semantics; it classifies the defect as suspected rather than confirmed. |
| `treats_unverified_as_low_trust` | PASS | The locked artifact identifies `last_verified_version: unverified` as low-trust evidence and bases the conclusion and medium-low confidence on directly observed source values plus missing runtime/test evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=05c2aca7faa7801466c539ea5dafc54c06b4080d2fde76c8c79aef9cad69e5ce; snapshot_sha256=68fadce15e86e1c1eafbf43a3fee6d8cbcc8524b329acc9784967ef71b9d3118
- Behavior: Produced the required evidence-based diagnosis artifact, verified the mapped documentation against the rule file, and kept the defect classification appropriately unconfirmed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=9da5894c7ee93c50bc9ea87962376063119fea4bc5a7ae2e073dddffe492fe39; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a correct prose comparison analysis but delivered no durable artifact; used only as baseline context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
