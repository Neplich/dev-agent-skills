---
name: manual-gen
description: "Create or update illustrated user manuals from screenshots and verified navigation in a running interface. Use after docs-agent confirms the documentation site and runtime access."
visibility: internal
---

# Manual Gen

## Reader-Facing Writing Composition

For substantial reader-facing prose, co-load `human-writing` even on direct
invocation; use the same context, not a later pass. This Skill retains evidence,
facts, required structure, paths, gates, and verification. Skip code-, config-, schema-,
lockfile-, and data-only output.

## Entry Gate

Require a PM handoff packet or an equivalent confirmed document chain that
defines the host repository, confirmed manual scope, evidence sources, and
required output. The PM packet definition lives in
the plugin-local generated `../docs-agent/_internal/_generated/shared-contracts/handoff-contract.md`.
Direct invocation does not waive this gate.

Verify that the host already contains the `docs/site/` foundation and its
standards entry. If the entry basis is incomplete, stop before writing and
return product ambiguity to `pm-agent` or technical-impact gaps to the owning
engineering role. If the site foundation or standards entry is missing, return
a `docs-site-bootstrap` handoff with zero site writes; this specialist must not
initialize the site.

## Scope and Directory Classification

Before inventory or writing, record two independent decisions:

- `scope_mode: bounded` for explicitly named pages, roles, features, or flows;
- `scope_mode: full-manual` for the complete user-visible product manual; or
- `scope_mode: full-site` only when a PM plan has already separated the manual
  slice from other formal-documentation surfaces. Otherwise return the whole-
  site request to `pm-agent` for decomposition.

Requests to complete a manual, cover the whole product, or audit all current
user-visible functionality select `full-manual`. Do not narrow that scope to
the existing manual directories or to one implementation batch.

Separately record `change_mode`:

- `extend` when the maintainer asks to add, complete, or update documentation
  without explicitly replacing it. Preserve existing paths only where current
  code and interface evidence still support them; add leaf pages or split
  subdirectories when new independent tasks require it.
- `rewrite` when the maintainer explicitly asks to discard old content,
  rewrite, rebuild, or derive the information architecture anew from the
  current product. Treat the existing tree as comparison evidence, not the
  target skeleton.

Full scope does not imply `rewrite`, and bounded scope does not imply `extend`.
If the supplied evidence already makes both decisions clear, record them
without asking again. Return a materially ambiguous scope decision to
`pm-agent`; do not use the old directory tree to decide scope by default.

## Running Environment Negotiation

Follow this conditional protocol before loading the execution instructions:

1. If the entry credential or handoff already provides a domain-accessible
   environment, use that confirmed URL directly and record its source without
   asking again. Only when domain evidence is missing must the first question
   be: 「是否有可通过域名访问的截图环境」. Do not combine this question
   with local startup as a two-option prompt.
2. If a domain-accessible environment is available, use that confirmed
   environment. Do not ask about local startup.
3. Enter the local-startup branch only when either no domain-accessible
   environment is available or the user explicitly asks to switch to a local
   environment. Then ask whether the user explicitly agrees to local startup.
4. Do not execute any startup command until that explicit agreement is
   received. If agreement is absent, remain at zero startup commands.
5. If neither the domain path nor an explicitly approved local path is
   available, report the missing environment evidence and return `blocked`.

## Authoritative Execution Pointer

After the entry gate passes and the running environment is confirmed, load
`_internal/INSTRUCTIONS.md` and follow its ordered host-site execution,
evidence, screenshot, validation, boundary, and report contracts.
