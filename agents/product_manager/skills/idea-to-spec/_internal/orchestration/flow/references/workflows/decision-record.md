# Workflow: decision-record

Architecture decision workflow — create ADR, validate, assess impact.

## Steps

```yaml
name: decision-record
description: Hand off a technical decision for Engineer-owned ADR, then validate and assess impact
steps:
  - skill: engineer-agent:trd-gen
    input_from: context
    output_key: trd_and_adr
  - skill: adr-validator
    input_from: trd_and_adr
    gate: true
  - skill: change-impactor
    input_from: trd_and_adr
    output_key: impact_report
```
