---
name: feature-implementor
description: "Implement and verify requested features or changes using repository conventions, focused edits, and tests appropriate to the affected behavior."
---

# Feature Implementation

Start from the user's requested behavior and the current implementation. Use
existing issues, specifications, designs, and tests as evidence where available.
Match the amount of planning and documentation to the size and uncertainty of
the task, then carry the authorized work through implementation and verification.

## Work through the change

1. Inspect the working tree and relevant code paths, callers, dependencies, and
   tests. Identify the expected result and compatibility requirements.
2. Choose a focused implementation. For a small change, explain the approach
   briefly and proceed. For substantial work, keep a useful plan with affected
   components, order, risks, and executable verification.
3. Implement using existing abstractions and conventions. Preserve unrelated
   work and maintain externally consumed behavior within the agreed scope.
4. Exercise the changed behavior and relevant failure paths. Run repository
   checks proportional to the change and investigate failures before delivery.
5. Review the diff against the requested result. Update documents that describe
   behavior changed by the implementation, then prepare the requested delivery.

Record material design choices when they will help future work. A durable plan
is useful for long tasks; store it with the project's existing planning records
and keep its completed state accurate. Routine progress can live in the task
and commit history.

For UI changes, inspect the actual rendered result and interaction states. For
migrations or external integrations, verify compatibility, failure recovery,
and the applicable rollout path. Report any verification that the environment
could not support, together with its impact on confidence.

## Focused references

- [Planning](./_internal/planner/INSTRUCTIONS.md)
- [Implementation](./_internal/implementor/INSTRUCTIONS.md)
- [Review](./_internal/reviewer/INSTRUCTIONS.md)
- [Coding practices](./_internal/_shared/coding-rules.md)
- [Completion evidence](./_internal/_shared/output-conventions.md)

Finish with the behavior changed, verification results, and material remaining
risks. Continue into tests, documentation, and delivery covered by the request.
