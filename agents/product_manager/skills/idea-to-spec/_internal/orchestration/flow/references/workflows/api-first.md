# Workflow: api-first

API-driven development that starts from interface definition.

## Steps

```yaml
name: api-first
description: Engineer-owned API documentation with TRD and test specs
steps:
  - skill: engineer-agent:trd-gen
    input_from: context
    output_key: trd_and_api_docs
  - skill: api-validator
    input_from: trd_and_api_docs
    gate: true
  - skill: trd-validator
    input_from: trd_and_api_docs
    gate: true
  - skill: tspecs-gen
    input_from: trd_and_api_docs
    output_key: test_specs
  - skill: tspecs-validator
    input_from: test_specs
    gate: true
```
