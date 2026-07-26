# Capture Service Context

The current service receives Capture events over HTTP and publishes background work to a queue. The Engineer TRD must define component boundaries, event flow, idempotency, retry behavior, validation, observability, rollout and rollback without implementing code.
