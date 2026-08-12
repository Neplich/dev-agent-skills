# Investigation Handoff

```yaml
request_type: bug_report
change_tier: standard
feature_path: session-management
feature: session-management
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: incident-summary.md
    reason: The reported failure occurs in the session refresh endpoint.
source_documents: [incident-summary.md]
scope_decision:
  summary: Investigate the intermittent session refresh failure without applying a fix.
  expectation_changed: false
  non_goals: [repair, test changes, delivery]
downstream_owner: Engineer
required_output: evidence_based_diagnosis_report
blockers_risks: [Approved PRD and TRD are not available.]
mode: diagnosis_only
allowed_mutations: none
```
