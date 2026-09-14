---
name: incident-playbook-writer
description: "Write operational runbooks for diagnosing and recovering from actual application, dependency, and deployment failures."
---

# Incident Playbooks

Identify the service, environment, runtime, monitoring, and recovery mechanisms
from project code and operational assets. Select incident scenarios relevant
to the user request and the system's actual dependencies.

Useful scenarios include failed deployment, application unavailability,
database connectivity or saturation, queue backlog, storage exhaustion, and
resource pressure. Cover the scenarios supported by the system under review.

For each runbook, describe the symptoms, impact, initial checks, diagnostic
commands, decision points, recovery actions, and success signals. Include
rollback or escalation when recovery depends on another system or owner.
Commands identify the intended context, namespace, service, or container.

Keep diagnostic steps before mutations. Clearly identify actions that change
traffic, credentials, data, or availability and the conditions for using them.
Use the project's protected secret mechanism and sanitized output examples.
Verify commands against the current manifests and tooling; distinguish a
statically checked procedure from one exercised in a test environment.

Save the runbook where operators already look for deployment guidance. A
short, executable procedure with concrete recovery signals is usually the
most useful artifact.
