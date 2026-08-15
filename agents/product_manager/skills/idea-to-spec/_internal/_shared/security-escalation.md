# Security Conclusion Escalation to PM

This subsection is the authoritative cross-role rule for when a confirmed
Security conclusion returns to `pm-agent` for entry classification and issue
filing. The escalation is conditional: not every security review returns to
PM.

**Trigger conditions.** Escalate only when a confirmed Security conclusion — a
review finding, or a Security re-review confirming that a remediation has
landed — establishes that at least one of the following has changed:

- formal-documentation facts under `docs/site/`: documented current-state API,
  database, design, ops, or product behavior, for example authentication
  requirements, permission rules, data handling, or endpoint behavior
- externally visible behavior of the system
- operational or deployment facts, for example hardening steps, required
  environment configuration, or rollback behavior
- release readiness

**Non-trigger conditions.** Do not escalate when the security review finds no
issues, when findings and fixes stay internal without changing any of the
trigger categories above (formal-documentation facts, externally visible
behavior, operational or deployment facts, or release readiness), or when the
only outputs are Security-owned process reports under
`docs/security/{feature_path}/`. Those reports remain process documents owned
by Security.

**Escalation action.** Security returns the confirmed conclusion and evidence
to `pm-agent`, which classifies the entry and files the issue. The trigger is
Security's own conclusion; Security does not wait for a separate Engineer or
DevOps return handoff. Security must not hand evidence directly to `docs-agent`,
file the issue itself, or modify formal documentation (`docs/site/` or
documentation owned by other roles). Security-owned process reports under
`docs/security/{feature_path}/` remain required escalation evidence and are not
restricted by this prohibition.

**Evidence payload.** Include the Security report under
`docs/security/{feature_path}/` for feature-scoped work, or repo-wide audit
evidence for repo-wide scope. Also include the affected scope (`feature_path`
values or a repo-wide marker), affected formal document types across api /
database / design / ops / product, a short summary of which fact changed, and
the affected release version when release readiness is impacted. When the
conclusion confirms remediation for an existing tracking issue, the evidence
payload must include the original issue number or link.

**Downstream action.** `pm-agent` classifies the issue with request type
`bug_report`, `formal_docs`, `security`, or `deployment`; release-readiness
impacts map to `deployment`. After the user confirms the entry classification,
`pm-agent` uses `gh issue create` to create the tracking issue and owns its
lifecycle. Remediation is dispatched through the normal cross-role handoff
packet. After remediation lands, route the work back to Security for re-review.
When Security returns the re-review conclusion to PM, PM updates and
closes the original issue rather than creating a duplicate; only a conclusion
without an existing tracking issue creates a new issue. Any Docs work reaches a
documentation specialist only through a PM handoff packet and follows that
specialist's existing gates.
