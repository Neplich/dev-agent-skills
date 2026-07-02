# eval-013-implementation-plan-archive-allows-next-plan

This fixture verifies that once the prior plan on a `feature_path` has been
closed out and archived, `feature-implementor` allows creating a new active
`IMPLEMENTATION_PLAN.md`. The new plan must record `previous_plan_archive`
pointing to the archived plan, and the active entry stays fixed.
