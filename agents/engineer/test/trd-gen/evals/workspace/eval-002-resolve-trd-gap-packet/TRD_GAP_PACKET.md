# Capture Loop Technical Open Questions

The product requirements define asynchronous processing, idempotency, bounded
retry, dead-letter handling, and observable processing states. The following
engineering details are not yet decided:

1. Which component owns the HTTP capture entry, event publication, queue consumption, status persistence, and dead-letter handling?
2. Which fields belong in `capture.created`, and where is the client event ID converted into an organization-scoped idempotency key?
3. Which unit and integration cases cover duplicate delivery, transient failure, exhausted retries, and permanent errors, and which repository commands run those cases?
4. How do producers and consumers remain compatible during rolling deployment, and how are in-flight events handled during rollback?
5. Which errors are retryable, which are permanent, and where are duplicate side effects prevented?
6. Which correlation IDs, retry and dead-letter metrics, alerts, and organization-boundary checks are required?
