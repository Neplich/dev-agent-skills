# Workflow: new-feature

Full feature documentation pipeline from business case to test
specifications.

## Steps

```yaml
name: new-feature
description: Complete documentation pipeline for a new feature
steps:
  - skill: brd-gen
    input_from: context
    output_key: brd
  - skill: brd-validator
    input_from: brd
    gate: true
  - skill: prd-gen
    input_from: brd
    output_key: prd
  - skill: prd-validator
    input_from: prd
    gate: true
  - skill: trd-gen
    input_from: prd
    output_key: trd
  - skill: trd-validator
    input_from: trd
    gate: true
  - skill: tspecs-gen
    input_from: [prd, trd]
    output_key: test_specs
  - skill: tspecs-validator
    input_from: test_specs
    gate: true
  - skill: trace-check
    input_from: [brd, prd, trd, test_specs]
    output_key: trace_report
```

## Gate Behavior

When `gate: true` and a validator returns FAIL:
1. Pause execution
2. Show the validation report
3. Offer options: iterate with the matching `*-iteration` skill, skip, or abort
