# Eval Result: eval-001-analyze-nodejs-project

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-001-analyze-nodejs-project`
- Test case: analyze-nodejs-project
- Workspace: `workspace/eval-001-analyze-nodejs-project`
- Latest result: PASS (4/4 assertions) - fresh Codex paired validation completed on 2026-07-26
- Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: `ENGINEERING_CONTEXT.md`, Node/Express manifest, source/test samples, ESLint and Prettier configs
- Fresh run: isolated `with_skill` and newly generated `without_skill` copies under `tmp/eval-runs/issue-158-round1/engineer-a/`; no historical comparison or baseline was used
- Source branch: `test/issue-158-round1-thin-fixtures`

## Assertions

- PASS `assertion_1`: YAML profile identifies JavaScript, Node.js 22, Express 5.1.0 and npm 11.4.2.
- PASS `assertion_2`: profile lists `src/` and `test/`.
- PASS `assertion_3`: profile records `eslint.config.js` and `.prettierrc.json`.
- PASS `yaml`: Project Profile is emitted as YAML.

## With Skill Behavior

The candidate used the repo-level Engineer context and real project markers, sampled source and tests, and produced the full Project Profile schema without inventing feature scope.

## Without Skill Baseline

The fresh baseline identified the same stack, directories and lint/format tools, but returned prose and a table rather than YAML. Baseline result: 3/4 assertions.

## Failures

- With-skill: none.
- Baseline: `yaml` failed.

## Next Steps

Keep the fixture and assertions unchanged; regenerate both sides when project-profile behavior changes.

## Runtime Artifacts Policy

Runtime outputs remain under ignored `tmp/eval-runs/issue-158-round1/` and are not committed. The durable result is this comparison only.

## 2026-08-03 变更后回归（issue #188）

- 变更：删除 Step 3 技术栈 marker 表、Step 4 lint 工具表、Step 6 架构模式表（A 维实测确认磨平）。
- 验证：删除后 paired 回归（fresh 双侧，judge 独立判定）：with-skill 4/4 PASS、without-skill 4/4 PASS（原断言双侧零区分，skill 增量在入口门禁/证据边界/feature inventory 等非断言内容）。
- 验证：L3 A 维 with/without 实测确认磨平（judge 独立判定，证据 `tmp/eval-runs/issue-188-l3/`）；删除后以原 eval prompt + fixture 重跑 with-skill，fresh judge 逐条判定原断言全部 PASS（4/4 PASS），Behavior result **PASS**，**无回归**（证据 `tmp/eval-runs/issue-188-regress/`）。

