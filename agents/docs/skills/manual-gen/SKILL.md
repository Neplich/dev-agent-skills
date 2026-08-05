---
name: manual-gen
description: "Internal documentation specialist—not a direct entry point. Invoked by docs-agent after the documentation-site gate passes to generate or update illustrated user operation manuals from screenshots of a real running interface."
visibility: internal
---

# Manual Gen

## Entry Gate

Require a PM handoff packet or an equivalent confirmed document chain that
defines the host repository, bounded manual scope, evidence sources, and
required output. The PM packet definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Direct invocation does not waive this gate.

Verify that the host already contains the `docs/site/` foundation and its
standards entry. If the entry basis is incomplete, stop before writing and
return product ambiguity to `pm-agent` or technical-impact gaps to the owning
engineering role. If the site foundation or standards entry is missing, return
a `docs-site-bootstrap` handoff with zero site writes; this specialist must not
initialize the site.

## Running Environment Negotiation

Follow this conditional protocol before loading the execution instructions:

1. The first question must be: 「是否有可通过域名访问的截图环境」. Do not
   combine this question with local startup as a two-option prompt.
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
