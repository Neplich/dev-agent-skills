# Workflow: decision-record

Architecture decision workflow — create ADR, validate, assess impact.

## Steps

```yaml
name: decision-record
description: Record and validate an architecture decision, then assess impact
steps:
  - skill: adr-gen
    input_from: context
    output_key: adr
  - skill: adr-validator
    input_from: adr
    gate: true
  - skill: change-impactor
    input_from: adr
    output_key: impact_report
```
