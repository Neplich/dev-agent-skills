# Document Patterns

Use the smallest matching pattern. It guides information order and never
replaces the primary Skill's required structure.

## User Manual and Tutorial

Write for a user completing a real task. Lead with the goal and prerequisite,
then give the shortest real navigation path, each action, its visible result,
and nearby recovery. Number only true sequences. Preserve exact page, button,
menu, tab, and field names.

Screenshots support the step they illustrate. Screenshot collection, masking,
naming, and Agent validation belong to the authoring workflow, not the user's
instructions. Keep a success check only when it helps users recognize completion
or recover from failure. Avoid a separate “Expected result” section when the
result is immediate and can sit beside the action.

## Product Documentation

Explain the task or problem, suitable users, prerequisite, concrete behavior,
limits, permissions, compatibility, and side effects. Show what changes in the
user's work. Do not replace behavior with abstract values or unsupported promotion.

## PRD

Keep the chain visible:

```text
problem -> user -> scope -> requirement -> acceptance -> risk or open question
```

Requirements state observable behavior or decisions. Keep non-goals near scope.
Use tables for traceability; surrounding prose should add context rather than
repeat every cell. Leave implementation choices to the TRD.

## TRD and ADR

Present source requirements and constraints, architecture, components, data flow,
interfaces, decisions, failure handling, security, compatibility, migration,
rollback, and exact verification. Keep technical terms. Readability comes from
putting decisions before consequences and answering concrete engineering questions.

An ADR records one durable decision: context, decision, important alternatives,
and consequences. It does not preserve the whole discussion history.

## API Documentation

Give the purpose and endpoint, authentication, request fields and constraints, a
runnable minimal example, response fields, errors, limits, retry or idempotency,
and compatibility. Keep field names exact. Examples must match verified behavior
and schemas.

## Runbook and Operational Guidance

Write for an operator under time pressure. State when to use the procedure,
impact, permissions, prerequisites, exact actions, success signals, stop
conditions, rollback, and escalation. Keep commands copyable. Put warnings where
the risky choice occurs, not in distant background.

## QA or Audit Report

Start with pass, fail, blocked, ready, or not ready. Follow with scope, evidence,
findings, impact, confidence, uncovered areas, and the smallest responsible next
step. Separate observation from inference. Logs support a conclusion; they do
not replace it.

## Release Notes and Changelog

User-facing notes emphasize workflow changes, upgrade actions, compatibility,
fixed visible problems, and known limits. Developer changelogs can emphasize
APIs, schemas, dependencies, migrations, and operations. Keep exact versions and
breaking-change language. Exclude prompts, eval counts, review rounds, and raw
commit dumps unless the target reader needs them.

## README

Help a new reader reach first use: what the project is, supported scope, shortest
setup path, minimal example, then deeper configuration, architecture, contribution,
and documentation links. Keep maintainer governance out of the opening unless it
affects ordinary use.

## Status, Research, and Decision Briefs

Put the decision-relevant conclusion first, then evidence, uncertainty, trade-offs,
and recommended action. Preserve source dates. Do not present inference as fact.
Use a table for repeated comparisons and prose for causality or judgment.
