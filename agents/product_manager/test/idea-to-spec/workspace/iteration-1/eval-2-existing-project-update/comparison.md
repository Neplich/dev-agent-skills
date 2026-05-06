# Eval 2: existing-project-update

> This file is the durable eval result. Runtime output files are intentionally not committed.

## Prompt

当前系统已经有一版通知中心的 PRD/TRD，现在要把提醒策略从轮询改成事件驱动。请分析影响范围，更新设计思路，并告诉我应该改哪些文档。

## Output Presence Check

### With Skill

- PASS: `with_skill/outputs/transcript.md`
- PASS: `docs/pm/notification-center/DECISIONS.md`
- PASS: `docs/pm/notification-center/PRD.md`
- PASS: `docs/engineer/notification-center/TRD.md`

### Without Skill

- PASS: `without_skill/outputs/transcript.md`

## With Skill Assessment

**Observed behavior**

- Explicitly identifies the request as an `existing-project-update`
- Starts with delta summary and blast-radius analysis
- Names the affected PM and engineer documents before proposing changes
- Prefers coordinated iteration over regenerating a fresh design
- Resolves one key migration decision before updating the docs
- Reflects the chosen direction back into `DECISIONS.md`, `PRD.md`, and `TRD.md`

**Strengths**

- Correct update-lane framing
- Strong delta-oriented reasoning
- Good separation between "what changes" and "how to update docs"
- Uses document changes to preserve design continuity

**Weaknesses**

- The transcript is still summarized rather than captured as a turn-by-turn interaction
- The eval does not yet assert that the previous confirmed decision was explicitly retired or moved into decision history wording

## Without Skill Assessment

**Observed behavior**

- Jumps immediately to a replacement architecture recommendation
- Treats the request as a fresh redesign rather than an update to approved docs
- Suggests rewriting PRD/TRD without first analyzing blast radius
- Does not name or use the existing decision log as part of the update flow

**Weaknesses**

- Update semantics are lost
- No explicit impact analysis
- High risk of wiping out context from approved docs

## Conclusion

**Skill impact:** HIGH

The new `idea-to-spec` protocol behaves correctly for update scenarios. It does
not collapse the request into a greenfield redesign; instead, it uses delta,
impact, and iteration as the primary frame.

## What This Eval Says About The Current Design

This eval did not expose a major flaw in the current skill protocol.

It did reveal one potential future improvement for the eval itself:

- Add an assertion around decision-history handling, so updates that replace a
  previously confirmed choice must either revise or explicitly retire that old
  decision

## Recommendation

- Keep the current update-lane behavior
- Consider extending eval assertions to cover decision-history hygiene
