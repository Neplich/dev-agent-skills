# Gen Skill Conventions

> Standard workflow, safety, and failure handling rules shared by all document
> generation skills under `gen/`. Each gen skill MUST follow these conventions
> unless explicitly overridden.

## Standard Workflow

Every gen skill follows this 6-step workflow:

1. **Collect context**: Read provided inputs plus any active feature docs. Scan
   `docs/pm/**/PRD.md` before choosing a target feature folder. If
   `docs/pm/{feature_path}/DECISIONS.md` exists, treat it as the source of
   truth for confirmed decisions, open questions, assumptions, and rejected
   options.

2. **Clarify one decision point at a time**: If the primary input is thin, ask
   the smallest question needed to unblock the current document. Do not bundle
   unrelated questions into one turn. Do not exceed 2 rounds of clarification.

3. **Load schema**: Reference the corresponding schema in
   `_internal/_shared/doc-schemas/`.
   Use the canonical filenames: `prd-schema.md`,
   `trd-schema.md`, `adr-schema.md`, `api-schema.md`, and
   `test-spec-schema.md`. Skip this step for utility skills
   (`mermaid-gen`, `weekly-report-gen`) that have no formal schema.

4. **Generate or update the target document**: Produce all required sections per
   the loaded schema. Follow
   `_internal/_shared/output-conventions.md`
   for naming, directory layout, and frontmatter format.

5. **Consolidate**: Rewrite any process notes, tentative correction phrasing, or
   chat-like fragments into stable document prose. The document body should
   state the current design directly.

6. **Self-check**: Validate the output against
   `_internal/_shared/quality-rules.md`
   scoring dimensions. Target overall score `>= 3.5` before presenting.

## Output Standards

- **Format**: Markdown with YAML frontmatter for formal docs, plain Markdown
  for utility skills
- **Directory layout**: Use the short-path feature directory convention from
  `output-conventions.md`
- **Memory sync**: When a generation step locks a new decision, ensure the
  corresponding `DECISIONS.md` is updated in the same feature folder
- **Feature path fields**: New formal feature-scoped documents include
  `feature_path`, `feature`, `parent_feature`, and `feature_level`
- **PRD child index**: New or updated PRDs include `child_features`, using
  `N/A` when the PRD has no direct child features
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
| L2a: Same-folder supporting-doc split | One document is too long, but all content belongs to one feature domain | Split into feature-scoped sibling docs in the same folder |
| L2b: Child `feature_path` split assessment | Any L2b signal below is met | Propose a child feature tree and wait for user confirmation; do not split automatically |
| L3: Incremental output | Extremely complex requirements | Use `design.md` or staged docs, then expand section by section |

### L1: Section Compression Rules

- Tables with more than 20 rows -> keep a summary table and move the full list
  to an appendix or sibling file
- Code or schema examples over 30 lines -> summarize inline and move the full
  example to an appendix
- Mermaid diagrams over 40 lines -> keep a simplified diagram inline and move
  the full version to an appendix

### L2a: Same-Folder Supporting-Document Split Rules

- Keep the files in the same feature folder
- Use fixed filenames for canonical docs, not versioned filenames
- Use sibling supporting docs only when the main doc would otherwise become
  unreadable
- Record supporting doc links in the main document frontmatter `related_docs`
  field

### L2b: Child Feature Path Split Assessment

Run a split assessment when any one of these signals is present:

1. The document has more than 500 total lines, including frontmatter.
2. The document contains at least 3 independent product or technical domains.
3. The PRD contains at least 15 user-story or requirement rows across its
   `US-*` and `FR-*` tables.
4. Section content has clear ownership boundaries that map to different child
   features, even when no numeric threshold is met.

A signal starts an assessment; it never authorizes an automatic split. The
assessment must present one proposal containing:

- a recommended child `feature_path` tree rooted at the current feature
- a section migration map from every source section to its proposed target
  document, including content that remains in the parent
- a downstream mirror impact list for `docs/engineer/`, `docs/design/`,
  `docs/qa/e2e/`, `docs/devops/`, and `docs/security/`, using `docs/pm/` as the
  feature-path source
- the evidence for each boundary and the expected effect on existing links,
  active work, archived plans, and QA history

Wait for explicit user confirmation before changing paths or documents. If the
user rejects the proposal, keep the current `feature_path` and continue with
L1 or L2a as appropriate.

When a proposal is confirmed:

- Treat the structural change as `change_tier: major`.
- Update `feature_path`, `parent_feature`, `feature_level`, `related_docs`, and
  the parent PRD's `child_features` index together.
- Use `git mv` for every directory move or file rename. For a pure split, use
  `git mv` for the file that carries the source document's main identity; create
  additional child documents normally.
- Before moving a PM directory, present the downstream mirror impact list and
  do not move it until the mirror handling decision is confirmed.
- Preserve the archive meaning of
  `docs/engineer/{feature_path}/implementation-plans/archive/`; do not promote
  archived plans back to active inputs during a move.
- Append QA `results/` history; never overwrite or rewrite historical results.
- Keep every source section traceable to a target document and record the
  migration in each affected document's changelog. No content may disappear
  silently.

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

- **Feature parent is unclear** -> blocked or ask the smallest clarifying
  question. Do not create a new top-level folder for a possible child feature.
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
4. **No directory drift**: Keep PM docs under `docs/pm/{feature_path}/`, where
   `feature_path` has one or more slash-separated slug segments. Do not invent
   alternate feature doc roots, and do not create a sibling top-level directory
   when an existing parent PRD clearly owns the child feature.
5. **No sensitive data**: Do not include real credentials, tokens, internal
   IPs, or PII in examples.

## Feature Path Gate

Run this gate before writing `PRD.md`, `DECISIONS.md`, or PM
`design.md`:

1. Scan `docs/pm/**/PRD.md`, supporting multi-level feature paths.
2. Read each PRD's `feature_path`, `feature`, `parent_feature`,
   `feature_level`, `child_features`, `title`, `related_issue`, and
   `related_docs` when present.
3. For old single-level PRDs without `feature_path`, infer
   `feature_path=<folder>`, `parent_feature=N/A`, and `feature_level=1`.
4. Decide whether the request is a level-1 feature or belongs under an existing
   parent PRD using explicit evidence: user statement, issue context, PRD title,
   DECISIONS content, or directory path.
5. Auto-create a child path only when evidence is clear. Otherwise stop with a
   blocked result or ask a concise clarification.
6. Reject empty paths, absolute paths, `..`, hidden segments, duplicate slashes,
   and non-lower-kebab path segments such as trailing hyphens or repeated
   hyphen separators.

Record the result in the next handoff as `feature_path_evidence`.
