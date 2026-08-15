# Safety-Net Closeout and Auto-Continue

This is the cross-role public behavior shared by the seven dispatchers (the PM dispatcher plus the six downstream role routers). It
applies after the current role finishes its scoped task, selected specialist
workflow, or blocked handoff report.

- Use the existing Downstream Owner Map and the collaboration chain
  `PM -> Designer -> Engineer -> QA -> DevOps -> Security` to identify the
  most likely next owner. Insert `Docs` when formal documentation work is due:
  after feature implementation, recommend `formal-docs-sync`; before release,
  recommend `docs-audit`. Do not create a
  parallel owner map or new chain.
- At closeout, proactively tell the user what the recommended next step is,
  why that owner is next, and what artifact or action that owner should
  produce.
- Unless the user has already authorized automatic continuation, ask for user
  confirmation before continuing into the next role or skill. One role
  completion normally produces one next-step proposal.
- If the user authorizes auto-continue with wording such as "后面自动继续",
  "auto", or an equivalent instruction, continue through the collaboration
  chain without step-by-step confirmation until the chain ends, a blocker is
  reached, a required target is unavailable, or the user tells the agent to
  stop.
- Role boundaries and role-only gates take precedence over auto-continue.
  Auto-continue never authorizes the current role to execute another role's
  workflow, call that role's specialists, or bypass a hard stop. Across roles,
  auto-continue only automates the next-owner proposal and handoff; the next
  owner agent performs the actual work under its own gates. Roles with hard
  stopping points, such as Designer stopping at design deliverables and handing
  implementation to `engineer-agent`, may auto-continue only up to that handoff
  point.
- If a user directly invokes a downstream role, dispatcher, or specialist but
  the required upstream PM handoff packet, confirmed document chain, or
  specialist entry basis is missing, softly guide the request back through
  `pm-agent` to fill the prerequisite context. This is a safety-net guidance
  path, not a silent refusal and not permission to execute downstream work
  without the missing basis.

### Documentation Site Deployment Completeness

This is a conditional Docs -> PM -> DevOps closeout in the existing owner map,
not a parallel chain. Trigger it after a complete first `docs-site-bootstrap`
whose durable changes were committed with user confirmation, after every
completed re-bootstrap, after every completed existing-site content batch, and
when Release Notes, release audit, or another workflow materially changes a
documentation build target, navigation or assets, release scope, or runtime
entry.

Docs performs a read-only check against host code and configuration, not Ops
prose alone. Enumerate Public, Internal, and every host-specific documentation
build variant. For each variant verify:

- Dockerfile or build target, build context, static output, and runtime entry;
- immutable image version, required architectures, registry, CI/CD build and
  publish triggers, and post-publish verification;
- Compose ports, dependencies, health checks, networks, and resources;
- Kubernetes / Helm Deployment, Service, Ingress or Gateway, values, and health
  checks;
- Public domain and TLS, and Internal authentication, network restriction, or
  equivalent access control; and
- drift in build inputs, commands, paths, and CI triggers after bootstrap or
  content synchronization.

Use exactly one stable result and report its evidence paths, covered variants,
missing links, drift, and next owner:

- `integrated`: every discovered variant is covered end to end by image build,
  CI/CD, and the applicable Compose or Kubernetes / Helm startup and access
  chain.
- `partial`: only some variants or some links in that chain are covered.
- `not_integrated`: the host uses image delivery but the documentation site is
  absent from that chain.
- `not_applicable`: evidence confirms no image delivery for the site and a
  maintainer-confirmed alternative host or explicit out-of-scope decision
  remains valid.
- `unknown`: configuration, environment, or permission evidence is
  insufficient; never treat it as integrated.

Do not infer integration from prose, a reachable port, or a domain alone. For a
first complete bootstrap, show the result after the confirmed commit and ask
the user to choose full integration of every variant, confirmed independent
hosting (`not_applicable`), or deferral with an explicit blocker / follow-up.
For later checks, report unchanged `integrated` evidence without replaying
DevOps; ask again on `partial`, `not_integrated`, or drift; name missing evidence
on `unknown`; and revalidate a `not_applicable` decision, asking again if it no
longer holds.

When the user chooses integration, return to `pm-agent` for a repo-wide
`request_type: deployment` packet. Feature fields may be `N/A` with
`feature_path_evidence: []`; `source_documents` must preserve host configuration
and Docs check evidence. Route the confirmed work in dependency order:

`devops-agent:deployment-planner` -> `devops-agent:cicd-bootstrap` ->
`devops-agent:env-config-auditor` -> `docs-agent:formal-docs-sync`.

The final Docs step synchronizes only landed and verified operational facts.
This safety-net authorizes only read-only inspection, reporting, and a
next-owner proposal. It does not authorize Docs to edit deployment assets or
deploy, DevOps to edit formal documentation facts, or any role to commit, push,
publish images, or deploy without separate authorization.
