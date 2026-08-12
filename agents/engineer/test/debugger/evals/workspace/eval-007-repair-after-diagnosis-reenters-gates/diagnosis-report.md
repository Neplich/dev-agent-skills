# Read-only Diagnosis Report

- Mode: diagnosis only
- Mutation boundary: none
- Expected behavior alignment: unaligned; no approved PRD or TRD was available
- Observed fact: the session refresh log reports `SessionStoreError: missing session table`
- Observed fact: `src/session-store.ts` queries the `sessions` table
- Assessment: the table may be missing or unavailable; confidence medium
- Unknown: whether the approved design requires this table and how it should be provisioned
- No repair plan or modification was authorized
