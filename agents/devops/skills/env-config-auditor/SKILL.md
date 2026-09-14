---
name: env-config-auditor
description: "Compare environment variables and secret references across source, examples, deployment files, and CI to identify actionable configuration gaps."
---

# Environment Configuration Audit

Inspect the requested application or environment. Discover variable reads in
source, framework configuration, startup scripts, manifests, Compose/Helm files,
and CI. Compare those references with documented examples and available secret
names, keeping secret values protected.

## Check the configuration path

- Which values are required, optional, or have defaults in code?
- Which runtime or build phase consumes each value?
- Do local, staging, and production assets provide the intended names and types?
- Do examples describe realistic safe defaults and the source of protected values?
- Are database URLs, origins, callback addresses, ports, and service names
  consistent across dependent components?
- Does the application report a missing required value usefully at startup?

Check for committed credentials, sensitive logging, overly permissive defaults,
and environment-specific assumptions. Trace each finding to source and the
configuration location that needs attention. Existing documentation is a useful
index; verify material claims in code or deployed configuration.

Report variable name, consumer, required state, available source, gap, and
recommended action. Apply corrections included in the task and run relevant
configuration or startup checks. Label values and environments that could not
be inspected and explain the resulting verification limit.
