# Implementing a Change

Inspect the affected code and its callers. Implement the smallest coherent
change using repository conventions and existing abstractions. Preserve
unrelated edits and public compatibility within the task's requirements.

Exercise the changed path early. Add tests that cover the behavior or defect,
then run relevant existing checks. Investigate failures using reproducible
commands and concrete evidence. Keep source, configuration, and affected usage
documentation consistent as the implementation develops.

Before delivery, review the complete diff, remove task-created temporary
artifacts, and summarize the outcome and verification.
