# Gen Skill Conventions

> Standard workflow, safety, and failure handling rules shared by all document
> generation skills under `gen/`. Each gen skill MUST follow these conventions
> unless explicitly overridden.

## Standard Workflow

Every gen skill follows this 6-step workflow:

1. **Collect context**: Read provided inputs plus any active feature docs. If
   `docs/pm/{feature-name}/DECISIONS.md` exists, treat it as the source of
   truth for confirmed decisions, open questions, assumptions, and rejected
   options.

2. **Clarify one decision point at a time**: If the primary input is thin, ask
   the smallest question needed to unblock the current document. Do not bundle
   unrelated questions into one turn. Do not exceed 2 rounds of clarification.

3. **Load schema**: Reference the corresponding schema in
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/`.
   Use the canonical filenames: `brd-schema.md`, `prd-schema.md`,
   `trd-schema.md`, `adr-schema.md`, `api-schema.md`, and
   `test-spec-schema.md`. Skip this step for utility skills
   (`mermaid-gen`, `weekly-report-gen`) that have no formal schema.

4. **Generate or update the target document**: Produce all required sections per
   the loaded schema. Follow
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/output-conventions.md`
   for naming, directory layout, and frontmatter format.

5. **Consolidate**: Rewrite any process notes, tentative correction phrasing, or
   chat-like fragments into stable document prose. The document body should
   state the current design directly.

6. **Self-check**: Validate the output against
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/quality-rules.md`
   scoring dimensions. Target overall score `>= 3.5` before presenting.

## Output Standards

- **Format**: Markdown with YAML frontmatter for formal docs, plain Markdown
  for utility skills
- **Directory layout**: Use the short-path feature directory convention from
  `output-conventions.md`
- **Memory sync**: When a generation step locks a new decision, ensure the
  corresponding `DECISIONS.md` is updated in the same feature folder
- **Line limit**: Keep output under 500 lines, including frontmatter
- **Section limit**: Keep each section under 80 lines; split or compress if
  exceeded
- **Section count**: When total sections exceed 10, consider splitting into
  multiple documents or using a working `design.md`

## Document Chunking Strategy

When a document risks exceeding the line limit, apply the appropriate chunking
level:

| Level | Trigger | Action |
| --- | --- | --- |
| L1: Section compression | Single section > 80 lines | Keep summary in place and move details to an appendix or sibling doc |
| L2: Multi-document split | Total > 500 lines OR `>= 3` independent domains | Split into feature-scoped sibling docs in the same folder |
| L3: Incremental output | Extremely complex requirements | Use `design.md` or staged docs, then expand section by section |

### L1: Section Compression Rules

- Tables with more than 20 rows -> keep a summary table and move the full list
  to an appendix or sibling file
- Code or schema examples over 30 lines -> summarize inline and move the full
  example to an appendix
- Mermaid diagrams over 40 lines -> keep a simplified diagram inline and move
  the full version to an appendix

### L2: Multi-Document Split Rules

- Keep the files in the same feature folder
- Use fixed filenames for canonical docs, not versioned filenames
- Use sibling supporting docs only when the main doc would otherwise become
  unreadable
- Record supporting doc links in the main document frontmatter `related_docs`
  field

### L3: Incremental Output Rules

1. Start with a working document where each major section has a short summary
2. Expand one section at a time after the user confirms the current direction
3. Consolidate the working draft before treating it as the final doc

Use these markers only when needed:

- `[PLACEHOLDER]` - section needs user input
- `[ASSUMED]` - reasonable default applied, needs confirmation
- `[ESTIMATE]` - rough figure, not verified
- `[DEFAULT]` - common default applied
- `[DERIVED]` - inferred from context
- `[INFERRED]` - inferred from limited information
- `[PROPOSED]` - suggested by the skill, awaiting approval
- `[RESEARCHED]` - based on domain knowledge, not verified data

## Failure Handling

- **Vague input after 2 rounds of questions** -> produce a partial document with
  explicit markers for incomplete sections and list the missing information
- **Cannot estimate a value** -> include the field with a note explaining what
  data points are still needed
- **Input too complex for one document** -> recommend splitting and establish
  the feature folder structure first
- **Missing optional context** -> use reasonable defaults, clearly marked with
  placeholder tags

## Safety Boundaries

1. **No fabrication**: Do not invent data, metrics, benchmarks, or research
   findings. Mark estimates and assumptions clearly.
2. **No external access by default**: Do not access external URLs or APIs
   unless the task explicitly requires it and the environment allows it.
3. **No silent memory drift**: If the generated document changes a previously
   confirmed decision, surface the conflict explicitly instead of silently
   overwriting it.
4. **No directory drift**: Keep PM docs under `docs/pm/{feature-name}/` and do
   not invent alternate feature doc roots.
5. **No sensitive data**: Do not include real credentials, tokens, internal
   IPs, or PII in examples.
