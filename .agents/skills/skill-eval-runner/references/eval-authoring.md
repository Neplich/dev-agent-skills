# Eval Authoring Contract

## Scope and Purpose

Create a regular eval for every marketplace skill except `docs/manual-gen`, the only
manual-only exception. Do not infer new exceptions. Require maintainer approval and a
checker update before adding another manual-only skill.

Use skill evals to test skill-specific usability: activation, protocol execution,
context use, evidence handling, blocking discipline, handoff boundaries, and expected
role output. Do not score generic writing quality or require one exact phrasing when
several equivalent answers are valid.

## Definition and Metadata

Use schema version `1.0` under
`agents/{agent}/test/{skill}/evals/evals.json`. Treat
`scripts/check_eval_contract.py` as the exact field and path authority rather than
copying its schema into prose.

For each eval:

- use a unique `eval-NNN-short-slug` ID and a real `workspace/...` directory;
- provide non-empty name, description, prompt, expected output, scenario, and semantic
  assertion objects;
- define scenario persona, situation, trigger, goal, materials, constraints, and
  success criteria from facts that exist in the user request or candidate workspace;
- keep assertion IDs lower snake case and assertion text outcome-oriented;
- keep the prompt only in `evals.json`, never duplicated in metadata;
- declare all explicit cross-skill dependencies and all six runtime-isolation surfaces;
- use output declarations only for deterministic candidate outputs; baseline outputs
  are diagnostic and never a passing gate;
- omit `validation_method` and runtime diagnostic artifact paths from committed
  metadata.

Run `uv run scripts/check_eval_contract.py` after every authoring change.

## Scenario and Prompt Integrity

Write the prompt as a request a real user would make outside this test repository.
Describe the problem and desired outcome, not the test protocol.

Reject prompt text that names or explains internal skills, agents, gates, steps,
`feature_path`, `change_tier`, assertions, expected output, runner modes, model choice,
or judging. Express required authorization naturally, such as “范围已经确认，可以直接
处理”, instead of declaring an internal gate passed.

Apply this leakage test to every sentence:

> If deleting the sentence leaves the real user goal complete but prevents an agent
> unfamiliar with the skill from guessing a scoring item, delete it.

Do not derive the scenario backward from the skill rules. Verify that every claimed
material, Git ref, dependency, runtime, and authorization actually exists in both
candidate lanes before loading the target skill.

## Assertions

Derive assertions from the documented skill obligations and observable user outcome.
Use semantic evidence rather than exact strings when localization, formatting, or
equivalent wording may vary.

Do not copy assertions into prompts, required-output lists, handoff blockers, README
instructions, evidence summaries, or fixture comments. Keep authorization, safety, and
workflow assertions testable through natural facts and actual candidate behavior.

## Candidate-Visible Fixture

Include only host-native facts that both candidate lanes should see. Remove
`eval_metadata.json`, `evals.json`, old comparisons, assertions, expected output, judge
instructions, transcripts, diagnostics, mode labels, and answer-bearing scripts or
summaries from the materialized fixture.

Use `required_output` in a handoff only for the user's desired deliverable shape. Use
`blockers_risks` only for objective risks. Do not place skill rules or scoring
prohibitions in either field.

Treat templates, standards, source code, configurations, raw diffs, logs, and
maintainer-approved scope as legitimate host material. Reject synthetic `.rules`,
`evidence.md`, README text, comments, fake object IDs, or renamed setup scripts created
only to reveal an answer. Confirm that referenced files and Git topology are executable,
not merely described in prose.

## Persistence and Review

Commit the eval definition, metadata, host fixture, and latest durable `comparison.md`.
Never commit lane workspaces, outputs, snapshots, judge packages, verdicts, transcripts,
timing, diagnostics, or run-status files.

After changing a skill, internal instruction, assertion dependency, or behavioral
fixture, identify the affected evals and ask whether to run them. Launch model evals
only after explicit authorization. If a fresh run occurs, let the shared runner update
the latest comparison; never handcraft a PASS or reuse an earlier baseline.

If both lanes satisfy an assertion, check for prompt or fixture leakage, behavior
shipped inside a template, or baseline model capability. Record the cause instead of
weakening the assertion or fabricating differentiation.
