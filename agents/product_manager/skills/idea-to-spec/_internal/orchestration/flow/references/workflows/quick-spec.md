# Workflow: quick-spec

Lightweight spec generation — skips BRD, produces PRD + Engineer TRD handoff.

## Steps

```yaml
name: quick-spec
description: Fast PRD generation with Engineer TRD handoff without BRD
steps:
  - skill: prd-gen
    input_from: context
    output_key: prd
  - skill: prd-validator
    input_from: prd
    gate: true
  - skill: engineer-agent:trd-gen
    input_from: prd
    output_key: trd
  - skill: trd-validator
    input_from: trd
    gate: true
```
