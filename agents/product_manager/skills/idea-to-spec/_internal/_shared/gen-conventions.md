# Gen Skill Conventions

> Standard workflow, safety, and failure handling rules shared by all document generation skills under `gen/`.
> Each gen skill MUST follow these conventions unless explicitly overridden.

## Standard Workflow

Every gen skill follows this 5-step workflow:

1. **Collect context**: Read provided inputs. If the primary input is thin, ask up to 5 clarifying questions (fewer for simpler document types). Do not ask more than 2 rounds of questions.

2. **Load schema**: Reference the corresponding schema in
`skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/`. Use the canonical filenames:
   `brd-schema.md`, `prd-schema.md`, `trd-schema.md`, `adr-schema.md`,
   `api-schema.md`, and `test-spec-schema.md`. Skip this step for utility
   skills (mermaid-gen, weekly-report-gen) that have no formal schema.

3. **Generate document**: Produce all required sections per the loaded schema. Follow `skills/product-dev/idea-to-spec/_internal/_shared/output-conventions.md` for versioning, naming, and frontmatter format.

4. **Self-check**: Validate the generated output against `skills/product-dev/idea-to-spec/_internal/_shared/quality-rules.md` scoring dimensions (Completeness, Consistency, Clarity, Testability). Target overall score ≥ 3.5 before presenting.

5. **Present**: Output the document with YAML frontmatter metadata (type, version `1.0.0`, status `Draft`, date, changelog). For utility skills without formal document structure, skip frontmatter.

## Output Standards

- **Format**: Markdown with YAML frontmatter (formal docs) or plain Markdown (utility skills)
- **File naming**: `<type-lowercase>-<name>-v<version>.md` per output-conventions.md
- **Line limit**: Keep output under 500 lines (including frontmatter); move detailed content to appendix
- **Section limit**: Keep each section under 80 lines; split into sub-sections or move to appendix if exceeded
- **Section count**: When total sections > 10, consider splitting into multiple documents

### Document Chunking Strategy

When a document risks exceeding the line limit, apply the appropriate chunking level:

| Level | Trigger | Action |
|-------|---------|--------|
| L1: Section compression | Single section > 80 lines | Keep summary in-place + move details to Appendix with anchor links |
| L2: Multi-document split | Total > 500 lines OR ≥ 3 independent functional domains | Split into main doc + sub-docs; main doc contains index table |
| L3: Incremental output | Extremely complex requirements (e.g., full-platform PRD) | Output skeleton first, then expand module by module on request |

#### L1 — Section Compression Rules

Apply when a single section exceeds 80 lines:

- **Tables > 20 rows** → Keep top 5 rows + "Full list in Appendix §X"
- **Code/schema examples > 30 lines** → Summary + "See Appendix §X for full example"
- **Mermaid diagrams > 40 lines** → Simplified diagram inline + full diagram in Appendix

#### L2 — Multi-Document Split Rules

Apply when total output exceeds 500 lines or the subject covers ≥ 3 independent domains:

- **Main document** contains: metadata, executive summary, sub-document index table, global constraints (NFRs, risks, timeline)
- **Sub-documents** split by: functional domain / user story group / service boundary
- **Naming**: `<type>-<project>-<module>-v<ver>.md` (e.g., `prd-checkout-payment-v1.0.0.md`)
- **Main document frontmatter** MUST include a `parts:` field listing all sub-documents:
  ```yaml
  parts:
    - prd-checkout-payment-v1.0.0.md
    - prd-checkout-shipping-v1.0.0.md
    - prd-checkout-inventory-v1.0.0.md
  ```
- Each sub-document frontmatter MUST include `parent:` referencing the main document filename

#### L3 — Incremental Output Rules

Apply when requirements are too complex for a single generation pass:

1. **Step 1**: Output a skeleton document — each section contains only 2-3 line summary, marked with `[EXPAND]`
2. **Step 2**: Present the skeleton and ask the user which modules to expand
3. **Step 3**: Generate detailed content for selected modules one at a time

- **Placeholders**: When information is unavailable, use these markers:
  - `[PLACEHOLDER]` — section needs user input
  - `[ASSUMED]` — reasonable default applied, needs confirmation
  - `[ESTIMATE]` — rough figure, not verified
  - `[DEFAULT]` — industry standard default applied
  - `[DERIVED]` — inferred from context
  - `[INFERRED]` — inferred from limited information
  - `[PROPOSED]` — suggested by skill, awaiting approval
  - `[RESEARCHED]` — based on domain knowledge, not verified data

## Failure Handling

All gen skills handle failures gracefully:

- **Vague input after 2 rounds of questions** → Produce a partial document with `[PLACEHOLDER]` markers for incomplete sections. List what information is still needed.
- **Cannot estimate a value** → Include the field with a note explaining what data points are needed.
- **Input too complex for single document** → Recommend splitting and provide skeleton for each part.
- **Missing optional context** → Use reasonable defaults, clearly marked with appropriate placeholder tags.

## Safety Boundaries

All gen skills observe these rules:

1. **No fabrication** — Do not invent data, metrics, benchmarks, or research findings. Mark estimates and assumptions with appropriate placeholder tags.
2. **No external access** — Do not access external URLs or APIs.
3. **No file modification** — Do not modify existing files unless the user explicitly instructs.
4. **No command execution** — Do not run commands unless the skill's workflow specifically requires it (e.g., weekly-report-gen reading git log).
5. **No sensitive data** — Do not include real credentials, tokens, internal IPs, or PII in examples.
