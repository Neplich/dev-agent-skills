# Coding Practices

- Read the affected code, callers, and tests before choosing a change.
- Reuse the project's naming, module boundaries, dependency patterns, and error
  handling. Keep edits focused on the requested result.
- Validate external inputs at the relevant boundary, use parameterized database
  access, and encode user-controlled output appropriately.
- Store credentials through the project's protected configuration mechanism.
- Handle failures where recovery or useful reporting is possible.
- Introduce abstractions when they simplify actual repeated responsibilities.
- Base expected behavior on user intent and reliable project evidence. Resolve
  material contradictions before committing to one interpretation.
- Verify changed behavior with meaningful tests and inspect the final diff.
