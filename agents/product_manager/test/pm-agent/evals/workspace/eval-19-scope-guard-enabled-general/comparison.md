# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-019-scope-guard-enabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5` from `agents/product_manager/test/pm-agent/evals/workspace/eval-19-scope-guard-enabled-general`.
- Identity schema: `2`
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `ee3671589f95fa8a892847eb388a153411b54b14444f1f7420faa0785c1aa02b`
- metadata_sha256: `b685d83a8e82816d2f4d521a041ae8452f619db60e5a55ebbccd97b0160d2ffb`
- fixture_sha256: `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6b0ff1b76e8b03f7712d3dcd168848aec48a65be2655318b04e40fdedd5925d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8b076cb82c470b131f01d4ac1cd0d36cbfb1e690ece346a8313d30b76a409813`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marker_does_not_trigger_pm` | PASS | With_skill output and trace show the request was treated as an ordinary file-organization task; it reported the unavailable isolated ~/Downloads and requested mounting/uploading files. No PM classification, PM documents, or handoff was produced, and git evidence shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=4f6d771affe828fe4ad47ab1e892677ae5709598a17c1a66a3b7145cb906627b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized the isolated environment lacked ~/Downloads and requested the files or mount needed to continue; did not enter PM workflow.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=ceb5e22ac9d44d06ee9995c8f00f93b1ebecac11cc93e91670faf3b689acf826; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also recognized the missing ~/Downloads; additionally supplied a local shell procedure for organizing image and document files.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
