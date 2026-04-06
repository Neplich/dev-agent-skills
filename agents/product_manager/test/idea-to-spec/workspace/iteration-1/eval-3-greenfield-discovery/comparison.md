# Eval 3: greenfield-discovery

## Prompt

我想做一个团队知识问答产品，现在只有一个模糊想法。你先不要直接写完整 PRD，先帮我把方向收敛。

## Output Presence Check

### With Skill

- PASS: `with_skill/outputs/transcript.md`

### Without Skill

- PASS: `without_skill/outputs/transcript.md`

## With Skill Assessment

**Observed behavior**

- Explicitly keeps the request in `greenfield-discovery`
- Starts with context framing rather than document generation
- Narrows the idea through two decision points: problem choice and first user
- Uses `2-3` options with trade-offs at each decision point
- Defers formal docs until more discovery decisions stabilize

**Strengths**

- Good discipline around not over-producing too early
- Strong use of controlled narrowing instead of broad brainstorming
- Clear distinction between stable outputs and unresolved questions

**Weaknesses**

- The transcript is framed as a summary of the discovery turn rather than verbatim interaction
- The eval currently does not assert whether the skill asked for explicit confirmation after each decision point

## Without Skill Assessment

**Observed behavior**

- Immediately shifts into PRD-like structure
- Expands scope too early into roles, features, and NFRs
- Does not establish a narrow MVP problem before broadening the product

**Weaknesses**

- Over-scopes too fast
- Weak discovery discipline
- High risk of writing polished but unstable documentation

## Conclusion

**Skill impact:** HIGH

The current `idea-to-spec` protocol behaves correctly in greenfield discovery
mode. It delays formal documentation and instead focuses on resolving a small
number of high-value product decisions first.

## What This Eval Revealed

This eval does not require a skill change right now. The main improvement area
is on the eval side:

- Add an assertion that checks explicit confirmation behavior between decision
  points, not just the presence of options and deferred documentation

## Recommendation

- Keep the current discovery-mode behavior
- Extend the eval metadata later to check explicit confirmation discipline
