# TRD Gap Packet

```yaml
finder: feature-implementor
classification: trd_gap
feature_path: capture-loop
source_documents:
  - docs/pm/capture-loop/PRD.md
target_document: docs/engineer/capture-loop/TRD.md
target_state: missing
boundary: finder reports gaps; trd-gen owns the Engineer document
```

## Named Gaps

1. Affected components: HTTP capture entry, `src/capture/processor.ts`, queue retry policy and dead-letter path.
2. Data flow and integration: define `capture.created` fields, idempotency key propagation, enqueue/consume boundaries and status persistence.
3. Validation: define unit and integration coverage plus the concrete command `npm test -- capture-loop`.
4. Release and rollback: define compatibility during rolling deployment, safe disablement of consumers and treatment of in-flight events.
5. Error handling: distinguish retryable from permanent errors and prevent duplicate side effects.
6. Observability and security: define correlation ID, retry/dead-letter metrics, alerting and organization boundary validation.

Any unresolved technical decision must be recorded as an open question with owner and unblock condition. Until the TRD is complete and confirmed, `feature-implementor`, `debugger`, `IMPLEMENTATION_PLAN.md` and QA E2E updates remain blocked.
