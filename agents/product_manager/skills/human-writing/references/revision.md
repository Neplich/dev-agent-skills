# Revision Pass

Read this after a draft exists. Revise silently; do not deliver this checklist.

## 1. Contract and Facts

Compare the draft with the request, primary Skill, sources, and original text.
Remove invented behavior, examples, numbers, quotes, experiences, interface
states, and outcomes. Restore exact terms, labels, commands, fields, paths,
versions, links, citations, operation order, permissions, warnings, recovery,
frontmatter, tables, code blocks, and required sections.

## 2. Reader Boundary

For each section, name the reader and their task. Remove content that only
explains how the Agent gathered or masked evidence, selected a Skill, passed a
gate, prepared a handoff, or checked its own generation. Keep it when the actual
reader is the maintainer or operator who performs that work.

Also remove maintenance history, compatibility shims kept for old readers, and
handoff narration that leaked into the body, unless the reader needs them.
Watch for role generalization ("everyone can"), scope generalization ("works in
all environments"), and idealized product claims that the evidence does not
support.

## 3. Progress

Mark each paragraph as fact, action, result, reason, distinction, constraint,
example, evidence, risk, or recovery. Merge or delete repeats. Remove ceremonial
introductions and conclusions. Move prerequisites, results, warnings, and
recovery beside the step they affect. Shorten the document when the evidence
cannot support the requested length.

## 4. Sentences

Check for delayed actors, nominalized actions, stacked conditions, vague
references, repeated sentence shapes, staged reversals, fake depth, and extra
explanation after the point is already clear. Judge meaning in context; do not
mechanically ban a word.

## 5. Structure and Restraint

Keep numbers for order, bullets for independent items, tables for repeated
fields, and prose for causality. Make headings describe content, not the author's
process. Check rendered Markdown after structural edits.

Preserve correct paragraphs and useful local voice. Do not add slang, fake
uncertainty, first-person claims, metaphors, jokes, deliberate roughness, FAQs,
summaries, or future outlook unless the reader needs them. Do not attach a
writing score or list of removed AI phrases.

## 6. Scope and Structure

Confirm the actual change scope matches the request. A passage request should
not have grown into a site rewrite; a site request should not have shrunk into
rewording a few sentences.

Check whether restraint hid a structural problem: if chapters are grouped by
code module or authoring order instead of reader tasks, say so rather than
polishing around it.

After any restructuring, verify the content invariants: pages, images, steps,
warnings, and recovery notes all survived, and no information was lost to
reclassification. Then confirm whether the primary Skill still needs to run
link, build, rendering, or independent review verification, and hand that back
instead of claiming it yourself.

Stop when the document is accurate, useful, coherent, and appropriately voiced.
