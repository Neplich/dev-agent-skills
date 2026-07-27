# eval-012-implementation-plan-archive-preflight

This fixture verifies that `feature-implementor` runs the pre-plan archive scan
before creating a next `IMPLEMENTATION_PLAN.md` on a `feature_path` that already
has an unarchived active plan. The skill must block a direct overwrite and ask
the user to archive the completed plan before creating a new plan, or archive
it as `Superseded` with a reason before creating a new plan.
