---
name: skill-eval-runner
description: Create, run, inspect, and diagnose this repository's Skill evals and eval contracts. Use for eval definitions, paired runs, result analysis, or eval infrastructure triage; not for unit tests or product QA.
---

# Skill Eval Runner

Operate the repository's skill-eval lifecycle without reimplementing its validation,
isolation, judging, persistence, or cleanup logic. Treat this skill as the operator
workflow, `scripts/check_eval_contract.py` as the definition contract, and
`scripts/run_skill_eval.py` plus `scripts/eval_runtime.py` as the executable contract.

Read [references/eval-authoring.md](references/eval-authoring.md) before creating,
changing, or reviewing an eval definition, metadata file, or candidate-visible fixture.
Read [references/eval-runbook.md](references/eval-runbook.md) before launching model
evals or diagnosing a non-passing result. For a static contract-only request, the
commands in this file are sufficient.

## Classify the Request

- Treat “检查 eval 定义、comparison 或 CI” as static verification. Do not launch
  `codex exec`.
- Treat “新增、修改或评审 eval” as authoring. Validate scenario truthfulness, prompt
  naturalness, assertion semantics, metadata, and candidate-visible materials before
  considering a model run.
- Treat “运行、重跑、批量跑 eval” as model execution. Require explicit user
  authorization because it consumes model time and rewrites durable results.
- Treat “分析 FAIL/BLOCKED/PARTIAL” as diagnosis. Inspect current evidence before
  proposing changes; do not rerun first.
- Exclude `manual-gen`; it is the repository's only manual-only skill.

## Establish the Target

Resolve targets from `agents/{agent}/test/{skill}/evals/evals.json`. Prefer the
narrowest selector that satisfies the request:

```bash
# One eval
uv run scripts/run_skill_eval.py \
  --agent docs --skill docs-audit --eval eval-001-audit-mismatch --jobs 1

# One skill
uv run scripts/run_skill_eval.py --agent docs --skill docs-audit --jobs 10

# One role
uv run scripts/run_skill_eval.py --agent docs --jobs 10

# Exact targets across roles; repeat --select
uv run scripts/run_skill_eval.py --jobs 10 \
  --select docs/docs-audit/eval-001-audit-mismatch \
  --select qa/bug-analyzer/eval-001-analyze-test-failure

# All regular evals
uv run scripts/run_skill_eval.py --jobs 10
```

Use `--metadata <path>` only for one exact metadata file. Do not combine it with
filters or `--select`. Use `uv run scripts/run_skill_eval.py --help` rather than
guessing a flag.

## Run Static Gates First

Run these checks before any model eval:

```bash
uv run scripts/check_repository_contract.py
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/check_doc_contract.py
```

Run independent static checks concurrently when the orchestration environment supports
it. This does not relax the single-runner-process rule for model evals.

Stop and repair a static contract failure before spending model calls. Do not convert a
static failure into `BLOCKED` by manually editing `comparison.md`.

One expected pre-run state is not a static failure: for a brand-new eval whose workspace
has no `comparison.md` yet, `check_eval_contract.py` reports `missing durable
comparison.md` until the first model run persists it. Proceed with the first run when
this is the only contract failure for that eval; after the run, every static gate must
pass.

## Preserve the Execution Boundary

- Launch one `run_skill_eval.py` process. Let its `--jobs` pool provide concurrency.
  Never shell-parallelize multiple runner processes against the same checkout.
- Use at most `--jobs 10`. Parallelism is across eval targets only.
- Preserve each target's serial order: fresh `without_skill`, destroy it; fresh
  `with_skill`, destroy it; then create the read-only fresh judge.
- Keep the candidate prompt and canonical fixture identical across both lanes. The
  only variable is whether the target skill and its declared dependencies are loaded.
- Keep `gpt-5.6-luna` with `model_reasoning_effort="medium"` for both candidates and
  the judge. If unavailable, report `BLOCKED`; do not substitute a model.
- Do not edit eval inputs while a batch is running. The runner locks inputs and rejects
  source drift, but concurrent edits waste completed model work.
- Do not reuse an older baseline, a candidate self-assessment, or a transcript as the
  verdict.

## Converge With Minimum Model Work

- For pre-fix diagnosis, use an existing durable `FAIL` as evidence when its target,
  input identity, assertion, and failure mode still match the defect. Inspect it first;
  do not mechanically rerun it twice. This does not make old evidence a post-fix verdict.
- After the final candidate fix, run the exact target once. Add a second exact run only
  when the new result conflicts with relevant durable history, changes across runs, or
  otherwise shows model/judge variance.
- Defer the affected-target regression until the final edit is ready, then run it once
  with one runner process and up to `--jobs 10`. Do not rerun the full affected set after
  each intermediate edit.
- In that final regression, retain every completed `PASS`, `PASS (partial coverage)`,
  and `FAIL` as the valid fresh verdict. Retry only `BLOCKED`, timeout, or incomplete
  targets; do not rerun completed targets merely because the batch exited nonzero.
- Retry a timing-sensitive target alone with `--jobs 1`. When the default timeout is the
  proven blocker, one bounded `--timeout` increase is allowed for that target without
  rerunning the batch.
- Record unrelated fresh `FAIL` results separately. They do not block the current defect
  from closing when its target passes and freshness/static contracts are satisfied.

## Interpret and Persist Results

- Accept `PASS`, `PASS (partial coverage)`, or `FAIL` only from the fresh independent
  judge after both lane outputs and raw evidence are locked.
- Treat preflight, candidate, dependency, schema, or judge completion failures as
  `BLOCKED`. Do not fabricate a durable result to make the contract green.
- Let the runner transactionally update the target `comparison.md` and migration
  inventory. Do not hand-copy results between evals.
- Keep only the latest result in `comparison.md`; use Git history for superseded runs.
- Expect any non-passing target to make the batch command exit nonzero. Classify each
  target from its printed `Overall result` and blockers instead of treating the whole
  process as one undifferentiated failure.
- Confirm the runner removes `tmp/eval-runs/` and all candidate, snapshot, judge,
  transcript, timing, and diagnostic artifacts on every exit path.

Summarize durable results with:

```bash
uv run scripts/summarize_eval_results.py
```

## Diagnose Before Changing Anything

- If preflight or model execution is `BLOCKED`, diagnose infrastructure or isolation;
  do not score the skill.
- If the prompt, scenario, fixture, or assertions leak protocol details or contradict
  available materials, fix the eval definition or fixture.
- If the eval is valid and with-skill behavior violates the skill contract, record a
  skill defect. Do not weaken assertions to turn it green.
- If both lanes pass, check for fixture leakage, behavior already supplied by a shipped
  template, or baseline capability. Treat zero differentiation as lifecycle evidence,
  not a reason to forge a difference.
- If behavior passes with partial coverage, list unexercised assertions and decide
  whether another realistic eval is needed. Do not relabel it as a behavior failure.
- Create or update GitHub issues only when the user authorizes external writes. Keep
  eval defects, skill defects, and runner/infrastructure defects as separate issues.

## Verify the Final State

After a model run or eval-related edit, run:

```bash
uv run scripts/check_eval_contract.py
uv run scripts/check_eval_artifacts.py
uv run scripts/summarize_eval_results.py
git status --short
git diff --check
```

Run the independent static checks in parallel where supported, then inspect their
individual exit codes. Keep Git status and diff inspection after they complete.

Report the exact selected targets, worker count, result counts, blockers, files changed,
and whether runtime artifacts remain. Never claim that required CI ran model evals;
`.github/workflows/ci.yml` runs deterministic contracts and tests, while model evals are
manual through `.github/workflows/evals.yml`.
