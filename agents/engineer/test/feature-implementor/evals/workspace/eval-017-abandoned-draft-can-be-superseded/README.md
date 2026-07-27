# eval-017-abandoned-draft-can-be-superseded

This fixture verifies that `feature-implementor` preserves the explicit
abandonment path for an unfinished active plan. The active plan is still
`Draft`, but the prompt contains a clear maintainer decision to abandon it, so
the skill should archive it as `Superseded` before preparing a linked
replacement plan.
