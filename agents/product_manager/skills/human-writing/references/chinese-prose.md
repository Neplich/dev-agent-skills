# Natural Chinese Prose

Apply these rules to Chinese prose. They describe useful writing actions, not a
universal list of forbidden words or punctuation.

## Put Meaning Before Style

Identify what each sentence contributes: a fact, action, result, reason,
warning, distinction, or recovery path. Delete sentences that contribute none.
If the meaning is uncertain, return to the evidence instead of polishing it.

Natural does not mean casual. A manual can be plain, a PRD explicit, a TRD
technical, and a runbook terse. Match the reader and task.

## Show the Actor and Action

Let readers know who does what before adding long conditions or background.

Prefer:

> 管理员启用单点登录后，新成员可以使用公司账号登录。

Avoid:

> 在完成对于单点登录能力的启用之后，可以实现新成员通过公司账号进行登录。

Use direct verbs: “创建页面” instead of “进行页面的创建”, “更新配置” instead
of “完成配置的更新”. Keep nouns that are real domain terms, such as 身份验证,
访问控制, and 事务隔离.

## Let Paragraphs Advance

Each paragraph should complete one local job. A new paragraph must add new
material rather than rename the previous conclusion. Put prerequisites before
the dependent action, results beside the action, and limits where readers meet
them. Vary length according to content, not to simulate personality.

## Remove Report and Agent Tone

State the reader's reality instead of the author's process.

| Process-centred wording | Better action |
| --- | --- |
| 本节将对相关能力进行介绍 | State what the capability does |
| 通过上述步骤即可实现 | State the actual result |
| 需要注意的是 | Put the warning directly |
| 对操作结果进行确认 | Name the success signal only when needed |
| 截图中应遮盖账号信息 | Keep in authoring guidance, not the user manual |

Do not begin sections with “本节介绍” or “本文将” when the heading already does
that work.

## Avoid Manufactured Insight

State judgments and evidence directly. Do not invent a reader misconception and
overturn it, announce a “deeper level” without new evidence, or use phrases such
as “真正的问题” and “值得注意” as substitutes for reasoning. Real comparisons
between alternatives, states, and failure modes remain valid.

## Do Not Perform Humanness

Do not add slang, memes, fake first-person experience, invented scenes, deliberate
typos, synonym churn, or decorative metaphors. Human-feeling prose comes from a
clear position, supported material, useful selection, and natural order.

Repeat exact product and technical terms. Keep code, commands, fields, identifiers,
menu labels, and quoted UI text unchanged.

## Use Format Deliberately

Colons, semicolons, dashes, parentheses, lists, and tables are available when
they reduce reader effort. Use lists for scanable independent items, numbers for
real sequences, tables for repeated fields, and prose for causality or judgment.
If every paragraph has the same shape, revise the structure rather than swapping
punctuation.

End with the last useful result, risk, recovery step, decision, or next action.
Do not append a summary, product praise, or broad significance by habit.
