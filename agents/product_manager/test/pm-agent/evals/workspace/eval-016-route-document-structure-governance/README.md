# Eval 16: Route Document Structure Governance

A minimal PM/Engineer doc tree exists under `docs/`. The user asks for a
whole-tree structure audit (overlong docs, orphans, cross-role drift).

The regression target: pm-agent routes the request to
`idea-to-spec:structure-governance` as a read-only audit, instead of treating
it as a concrete split execution or handing it to a downstream role agent.
