---
name: flow
description: Execute named document workflows that chain multiple skills in sequence. Use when users say "run workflow", "execute flow", "new feature flow", "full document pipeline", "end-to-end docs", or need to orchestrate a sequence of gen/validate/iterate skills for a standard process like new feature development.
---

# Flow - Workflow Engine

Execute predefined or custom workflows that chain multiple skills together in a
logical sequence.

This is an internal secondary skill. Expect `idea-to-spec` to load it only
after the lane is already classified as an end-to-end workflow request.

## When to use

- Need to run a standard multi-step document pipeline (for example BRD -> PRD
  -> TRD -> Tests)
- Want to automate a repeatable process across multiple skills
- Setting up a complete documentation suite for a feature
- Prefer `idea-to-spec` first if the user's goals, scope, or constraints are
  still unclear
- **Orchestrates** other skills and checkpoints; does not generate documents
  directly

## Inputs

- **Required**:
  - `workflow`: Name of a predefined workflow or custom step list
  - `context`: Input context passed to the first skill in the chain
- **Optional**:
  - `skip_steps`: Steps to skip (for example skip BRD if it already exists)
  - `stop_after`: Stop after a specific step
  - `validate`: Run validators after each gen step (default: true)
  - `handoff_packet`: Stabilized context from `idea-to-spec` or another
    upstream skill, following
    `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`

## Shared Routing Contract

Before resolving validators, iteration paths, or checkpoint recommendations,
read `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

Use it to:

- interpret the `handoff_packet`
- pick the matching validator / iteration skill for each supported document type
- keep lifecycle and fallback behavior aligned with `idea-to-spec` and
  `iteration-coordinator`

## Predefined Workflows

Defined in `references/workflows/`:

### `new-feature`

Full feature documentation pipeline:
1. `brd-gen` -> BRD
2. `brd-validator` -> Validate BRD
3. `prd-gen` (input: BRD) -> PRD
4. `prd-validator` -> Validate PRD
5. `trd-gen` (input: PRD) -> TRD
6. `trd-validator` -> Validate TRD
7. `tspecs-gen` (input: PRD + TRD) -> TEST_SPEC
8. `tspecs-validator` -> Validate TEST_SPEC
9. `trace-check` (input: all docs) -> Traceability Report

### `quick-spec`

Lightweight spec generation (skips BRD):
1. `prd-gen` -> PRD
2. `prd-validator` -> Validate
3. `trd-gen` (input: PRD) -> TRD
4. `trd-validator` -> Validate

### `api-first`

API-driven development:
1. `api-gen` -> API Documentation
2. `api-validator` -> Validate
3. `trd-gen` (input: API docs) -> TRD
4. `trd-validator` -> Validate
5. `tspecs-gen` (input: API docs) -> TEST_SPEC
6. `tspecs-validator` -> Validate

### `decision-record`

Architecture decision:
1. `adr-gen` -> ADR
2. `adr-validator` -> Validate
3. `change-impactor` -> Impact Analysis

## Workflow

1. **Resolve workflow**: Load the predefined workflow from
   `references/workflows/` or parse the custom step list, then load
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` for
   lifecycle lookups.
2. **Initialize context**: Set up the shared context object that flows between
   steps. Prefer the `handoff_packet` if available so downstream skills reuse
   settled assumptions instead of re-asking basic questions.
3. **Execute steps sequentially**:
   - For each step, invoke the skill with accumulated context
   - Pass each step's output as input to the next step
   - If `validate: true` and a corresponding validator exists, run it after each
     gen step
   - If no validator exists for a step, explicitly note the gap and continue
   - If a validator returns FAIL, pause and offer the matching `*-iteration`
     skill from the shared lifecycle matrix before continuing
4. **Handle checkpoints**: After each step, briefly report status and ask if
   the user wants to review before proceeding.
5. **Final summary**: Report all generated documents, validation scores, and
   any outstanding issues.

## Output Contract

- **Format**: All individual skill outputs plus a workflow summary
- **Summary structure**:
  ```markdown
  ## Workflow Summary: <workflow-name>

  ### Steps Completed
  | Step | Skill | Output | Validation | Score |
  |------|-------|--------|------------|-------|

  ### Generated Documents
  - ...

  ### Outstanding Issues
  - ...

  ### Next Steps
  - ...
  ```

## Failure Handling

- Skill step fails -> report the error and ask whether to retry, skip, or abort
- Validator returns FAIL -> pause, suggest the matching iteration skill from
  the shared lifecycle matrix, continue on user approval
- Validator missing for a step -> note "no dedicated validator yet", suggest
  manual review or `trace-check` when appropriate
- Validator FAIL and no matching iteration skill exists for that custom step ->
  offer focused regeneration with the closest `*-gen` skill, then compare via
  `version-differ`
- Unknown workflow name -> list available workflows

## Safety Boundaries

- Always checkpoint between steps; never run the entire pipeline without user
  awareness
- Do not auto-iterate without user confirmation
- Each step must be clearly attributed to its source skill

## Examples

### Example 1: New feature workflow

**User**: Run the `new-feature` workflow for a "user notification system".

**Expected Output**:
1. Generated BRD (score: 4.1 PASS)
2. Generated PRD from BRD (score: 3.8 NEEDS_WORK - missing NFR metrics)
3. Pause: "PRD needs work. Run `prd-iteration` to fix, or continue?"
4. Continue based on the user's choice
