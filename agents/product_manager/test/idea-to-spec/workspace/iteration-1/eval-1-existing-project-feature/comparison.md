# Eval 1: existing-project-feature-design

## Prompt

我们在一个已有的 Web 应用里，要新增应用标签系统。请先看项目上下文，再和我一起把方案收敛下来，最终沉淀成 PM 设计文档。

## Output Presence Check

### With Skill

- PASS: `with_skill/outputs/transcript.md`
- PASS: `docs/pm/app-tags/DECISIONS.md`
- PASS: `docs/pm/app-tags/design.md OR docs/pm/app-tags/PRD.md`

### Without Skill

- PASS: `without_skill/outputs/transcript.md`

## With Skill Assessment

**Observed behavior**

- Starts with explicit project context and lane selection
- Frames the request as an `existing-project-feature`
- Uses decision-point progression instead of one-shot solution dumping
- Presents explicit options with trade-offs on the tag data model
- Writes confirmed decisions into `docs/pm/app-tags/DECISIONS.md`
- Uses `docs/pm/app-tags/design.md` as an intermediate PM artifact

**Strengths**

- Strong adherence to the new design protocol
- Good separation between confirmed decisions and open questions
- Uses documentation as durable memory instead of relying only on transcript
- Produces a realistic incremental artifact rather than forcing a full PRD too early

**Weaknesses**

- The transcript is still a condensed summary, not a full turn-by-turn capture
- Section 3 is stable enough for a working draft, but not yet expanded into a full PRD

## Without Skill Assessment

**Observed behavior**

- Jumps straight to a recommended implementation approach
- Does not begin with project context or lane framing
- Does not compare multiple options before recommending one
- Does not structure the output into confirmed sections
- Does not create durable PM docs or a decision log

**Weaknesses**

- Too solution-first
- No stable decision memory
- High risk of hidden assumptions and drift across long conversations

## Conclusion

**Skill impact:** HIGH

The new `idea-to-spec` protocol materially improves design quality for existing
project feature planning. The skill now behaves more like a design facilitator
than a one-shot advisor.

## What Needed Updating

The primary issue discovered in this eval was in the eval definition, not in the
skill:

- The original eval required `docs/pm/app-tags/PRD.md`
- The current protocol correctly allows `docs/pm/app-tags/design.md` as an
  intermediate PM artifact before the design is fully promoted to `PRD.md`

The eval was updated to accept either:

- `docs/pm/app-tags/design.md`
- `docs/pm/app-tags/PRD.md`

## Recommendation

- Keep the current `idea-to-spec` protocol direction
- Retain the updated eval rule that allows phased PM artifacts
- In future eval runs, consider storing a fuller turn-by-turn transcript to make
  behavior assertions easier to review
