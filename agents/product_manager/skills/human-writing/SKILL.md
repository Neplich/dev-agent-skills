---
name: human-writing
description: "Write or revise reader-facing documents in natural, purposeful Chinese while preserving the primary Skill’s facts, workflow, terminology, structure, formatting, and delivery contract. Use alongside document-generation Skills for manuals, product and technical docs, reports, release notes, READMEs, or other prose. Also applies to requests to rewrite, polish, humanize, or remove AI, machine, report, or agent tone. Do not use for code-, config-, schema-, or data-only output."
visibility: internal
---

# Human Writing

Write for the people who will use the document. Keep the primary Skill's facts
and delivery rules intact, then make the content read like a knowledgeable
person chose what to explain, in what order, and in what words.

This Skill is a composition capability. Load it in the same turn as the primary
document Skill. It is not an upstream producer, downstream consumer, or final
polishing stage.

## Entry

Use this Skill when the output contains substantial reader-facing prose,
including:

- user manuals, tutorials, help pages, and product documentation;
- PRDs, TRDs, ADRs, API documentation, runbooks, and operational guidance;
- QA reports, research or status reports, release notes, changelogs, and READMEs;
- a substantial rewrite of existing prose;
- a direct request to make writing natural, readable, less mechanical, less
  like AI, or less like an Agent's internal procedure.

Do not activate it only because a task happens to write a file. Code, config,
schemas, generated data, lockfiles, and source-only patches stay with their
owning Skill. Short labels and metadata need correctness before style.

Direct invocation does not replace a document owner. If the user asks for a
manual, TRD, spreadsheet, slide deck, or another governed artifact, load the
corresponding primary Skill as well.

## Resolve Rules in This Order

1. Follow the user's explicit facts, audience, tone, language, and delivery request.
2. Follow the primary Skill's evidence, workflow, safety, required structure,
   artifact path, formatting, and verification contract.
3. Apply this Skill to reader perspective, information order, paragraphs,
   sentences, and rhythm.

Never trade correctness for fluency. This Skill may move an explanation closer
to the step that needs it; it must not reorder a real operation. It may replace
an abstract phrase with a direct action; it must not rename a button, field,
command, or formal term.

## Infer the Writing Situation

Do not require the user to fill out a writing form. Infer, in order, from:

1. the current request and explicit constraints;
2. the primary Skill and its artifact contract;
3. the target file and the text being revised;
4. adjacent documents, repository terminology, and local style;
5. the minimum reasonable default for that document type.

Determine internally:

- who will read the document;
- what they are trying to understand, decide, or complete;
- what they already know at this point;
- which document type and tone fit that task;
- which facts and structures cannot change.

Ask one concise question only when different answers would materially change
the facts selected, the procedure, the audience, or the deliverable. Otherwise,
make the smallest reasonable assumption and continue.

## Protect the Source of Truth

Before drafting, identify the material that can support the document. Valid
material includes user-provided facts, verified repository or product evidence,
reliable sources, and content explicitly authorized as fictional or illustrative.

For factual documents:

- do not invent product behavior, examples, numbers, quotes, user experiences,
  interface states, failure modes, or outcomes;
- do not expand thin evidence by repeating the same idea in different words;
- distinguish a confirmed fact, a reasonable inference, and an unresolved gap;
- if required facts are missing, return to the primary Skill's research,
  evidence, or clarification workflow instead of filling space.

Preserve unless a higher-priority rule explicitly changes them:

- product, page, button, field, API, and domain names;
- operation order, prerequisites, permissions, warnings, failure conditions,
  recovery steps, and acceptance criteria;
- code, commands, configuration, paths, numbers, units, versions, and links;
- citations, source meaning, frontmatter, Markdown structure, tables, and
  required sections;
- artifact ownership, status, handoff fields, and verification evidence.

## Write from the Reader's Position

Choose content by asking whether the target reader needs it to understand,
decide, act, verify, or recover.

Do not leak authoring or Agent procedure into the document. Common leaks include
instructions about collecting evidence, masking screenshots, constructing a
handoff packet, checking that the Agent completed a step, or following an
internal generation gate. Keep such information only when the document's actual
reader is the operator or maintainer who must perform that work.

For example, a user manual may say:

> 选择左上角的菜单按钮即可展开 Wiki 索引。标题旁的数字是当前索引中的页面总数。

It should not tell the user to “查看标题旁的页面总数，确认索引已经加载”，unless that
check is a real recovery or troubleshooting step the user needs.

## Make Every Section Move

Organize around the reader's task, not the Agent's collection order.

- Open near the task, decision, change, or problem. Skip ceremonial background.
- Put a prerequisite immediately before the action that depends on it.
- Keep a result near the action that produces it.
- Explain a limitation where the reader is likely to encounter it.
- Let each paragraph add a fact, action, result, reason, distinction,
  constraint, example, or recovery path.
- Delete a paragraph that only restates the heading or previous paragraph.
- Stop when the reader has what they need. Do not add a summary or uplifted
  conclusion by habit.

Background, summaries, lists, tables, and callouts are valid when they reduce
reader effort. Do not force them into every document.

## Load Only the Needed References

- Read `references/document-patterns.md` for the target document type and its
  information order.
- Read `references/chinese-prose.md` when writing or substantially revising
  Chinese prose.
- After the draft exists, read `references/revision.md` for a silent final pass.

For a small local edit, load only the reference that addresses the problem. Do
not read every reference as a ritual.

## Create or Revise

When creating a document:

1. establish the reader's task and the primary Skill's immutable contract;
2. gather enough material for the requested scope;
3. select the document pattern;
4. draft in the order the reader needs information;
5. revise silently, then run the primary Skill's verification.

When revising an existing document:

1. preserve correct content, local terminology, working links, and valid voice;
2. identify the exact reader, organization, sentence, or repetition problem;
3. change only affected paragraphs and the transitions they require;
4. compare the result against the source for fact and format drift;
5. avoid whole-document synonym replacement or a new house style unless asked.

## Delivery

Deliver the artifact requested by the primary task. Do not append a writing
score, rule checklist, hidden outline, or explanation of how the prose was made.

In the final task report, mention material assumptions or unresolved evidence
only when the reader needs them to use or approve the document. Report factual
and verification limitations plainly; do not disguise them with smoother prose.
