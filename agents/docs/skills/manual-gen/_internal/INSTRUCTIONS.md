# Manual Gen — Internal Instructions

Authoritative execution contract for `manual-gen`. The entry gate and running
environment negotiation live in `../SKILL.md`; load this file only after both
have passed. Execute all eight steps in order.

## 1. Read the host standards entry and change map

Verify the confirmed host contains `docs/site/`, its standards entry, and
`docs/site/standards/change-map.yaml`. Read `docs/site/standards/index.md` or
the host's equivalent entry, then follow the linked standards needed for page
granularity, lifecycle, frontmatter, navigation, and checks.

If the foundation, standards entry, or change map is absent, stop with zero
site writes and return a bounded `docs-site-bootstrap` handoff. Do not create a
partial site or initialize missing foundations.

## 2. Read the unique manual template and existing structure

Follow the host standards entry to the manual template under
`docs/site/standards/templates/`. Read its unique `docs-scaffold` block and
the existing `docs/site/manual/**` paths, frontmatter, indexes, and navigation
needed to place the confirmed scope.

The host manual template is the only template source. This specialist must not
embed, reconstruct, or maintain a second copy of the template body. When the
host exposes `npm run new:doc`, prefer that deterministic scaffold entry for a
confirmed new page.

## 3. Map confirmed roles, scenarios, and flows in the running environment

Use only the environment confirmed by `../SKILL.md`. Within the maintainer-
confirmed boundary, inspect the actual interface to identify target roles,
business scenarios, entry points, prerequisites, user-visible controls,
operation sequences, visible outcomes, and exception states.

Base every candidate operation on an interface and flow that can be observed
in that environment. Do not expand the request into a full user-side and admin-
side inventory. Record evidence gaps instead of filling them with assumptions.

## 4. Present one bounded candidate batch and wait for confirmation

Before any manual page, screenshot asset, change-map, index, or navigation
write, present:

- the covered roles and business scenarios;
- the candidate parent-child page tree;
- each page's interface evidence and screenshot plan;
- the proposed change-map, index, and host-required navigation delta;
- explicit exclusions, unresolved discrepancies, and out-of-batch scope; and
- the remaining candidates after this batch.

Wait for explicit maintainer confirmation. Unconfirmed scope receives zero
writes. Execute only one confirmed batch at a time, report the remaining
candidates, and require new confirmation before another batch.

## 5. Set, read back, and validate the viewport before capture

### Execution entry

Use the repository's existing three-level priority:
`repo harness > Chrome plugin / browser connector > Playwright fallback`.
Its authoritative definition lives in `AGENTS.md` and the QA skills
`spec-based-tester`, `exploratory-tester`, and `regression-suite`; do not copy
their selection details or introduce a fourth contract. A host harness that
internally uses Playwright still counts as the repo harness. State why the
selected entry covers the current capture need. If no eligible entry can cover
it, stop as `blocked`.

### Viewport contract

For every screenshot batch:

1. Explicitly set the desktop viewport to `1920×1080` through the selected
   running environment.
2. Before taking any screenshot, read the actual viewport width and height
   back from that running environment.
3. 回读结果必须来自运行环境的实际读数，不得由设定值推断。
4. If the actual read-back is not exactly `1920×1080`, stop capture and record
   the mismatch. Do not produce screenshots until the viewport is corrected
   and read back again.

`视口设定` and `视口回读` are separate report fields; if either field is
missing, this step is incomplete. This constraint comes from an observed tool
failure: a browser tool's desktop preset resolved to `691×837` and triggered
the site's responsive mobile layout.

### Screenshot hygiene

Keep the same viewport, zoom, theme, and navigation state throughout one
manual. Capture product content only. Exclude browser tabs, address bar,
toolbars, window borders, loading states, open menus, translation popups,
promotional banners, marketing dialogs, and other temporary overlays.

Use test data by default. Hide tokens, keys, email addresses, personal
information, costs, and invocation logs. Do not copy environment-specific long
identifiers into the manual body. Creation, deletion, publication, permission
changes, and other state-changing actions may run only inside the confirmed
test scope.

## 6. Write manual pages, screenshots, and change-map entries

Organize the manual through the host site's existing information architecture
at three semantic levels:

- platform level: platform positioning, intended audience, and role boundary;
- business level: business scenario, capability purpose, and module relation;
- operation level: reproducible task flow, numbered steps, and results.

Use the host's current nested navigation and headings; do not hard-code a new
site directory scheme. Each operation entry must satisfy all fields defined by
the authoritative manual template: applicable role, prerequisites, numbered
steps, visible interface description, screenshot and caption, expected result,
and notes or exception handling.

Place each screenshot beside the page that references it. Name it
`step-<number>-<lower-kebab-case>.png` and reference it through a `./` relative
path. This reuses the host `prepare-site.mjs` `referencedAssets()` mechanism;
do not create a new `public` subdirectory convention.

Every screenshot addition or replacement must also update its owning manual
page so the screenshot change enters the `docs-agent:docs-audit` affected
evidence set. Update the page's change-map entry when its mapping also needs to
change, but a change-map edit cannot replace the required page update.

For every created or updated manual page:

- set `doc_type: manual`;
- keep `related_code` non-empty and point it to the frontend route or component
  path that renders the documented interface, so the evidence boundary is
  locatable; and
- set `last_verified_version: unverified`; version stamping belongs to
  `docs-agent:docs-audit`.

Grow only the confirmed entries in
`docs/site/standards/change-map.yaml`. Preserve unrelated entries and unknown
fields, keep the page, its necessary indexes and navigation, its screenshot
assets, and its change-map closure in the same confirmed write scope, then read
all changed content back.

## 7. Run host docs checks and visual rendering acceptance

Read the authoritative commands from the host `docs/site/package.json`,
repository guidance, or CI. Run every required documentation check and record
the command, working directory, exit status, and result. Do not invent a
replacement check.

Render the manual through the host's existing documentation-site path and
visually inspect every changed page. Verify that screenshots are visible,
captions match their steps, page content is readable, and the page is reachable
through the expected navigation. Treat skipped assets, broken image references,
render failures, or unreachable navigation as blockers.

If required dependencies have no host-defined deterministic installation path,
or any required check or visual acceptance cannot be completed, stop and
report the missing evidence. Do not mark the manual complete.

## 8. Handoff to docs audit

After all confirmed writes, read-back checks, host checks, and visual
acceptance pass, hand the complete affected page, screenshot, mapping, index,
navigation, and evidence set to `docs-agent:docs-audit`. Keep every new or
updated page at `last_verified_version: unverified`; only `docs-audit` may
apply a verified version anchor.

If the environment, login state, feature availability, screenshot permission,
eligible execution entry, viewport read-back, host check, or rendering
acceptance is unavailable or fails, return `blocked`. Record the blocker,
owner, missing evidence, and next action. Never claim completion, invent an
interface, or substitute an unrelated example image.

## Boundaries

- Do not modify the five-type contract or eight-step flow of
  `formal-docs-sync`.
- Do not generate or edit Release Notes surfaces.
- Do not create or move tags, execute release operations, or initialize a
  documentation site.
- Do not add a screenshot-expiry mechanism, browser framework, startup script,
  or separate asset-publication convention.

## Report Shape

```markdown
## Manual generation result

- 确认范围：<角色、场景、页面树、排除项>
- 运行环境与来源：<域名或获明确同意的本地环境；确认来源>
- 执行入口：<repo harness | Chrome plugin / browser connector | Playwright fallback；覆盖理由>
- 视口设定：<明确的设定命令或操作及 1920×1080 目标>
- 视口回读：<从运行环境读取的实际宽度和高度>
- 采集截图清单：<页面、步骤、资产路径、图注，或 none>
- 变更页面：<路径或 none>
- change-map 增量：<条目及原子 required-doc closure，或 none>
- 宿主检查结果：<命令、cwd、退出状态、结果>
- 渲染验收结果：<目视检查页面及结果>
- 阻塞项：<事项、owner、缺失证据、下一步，或 none>
- 剩余候选：<批次外角色、场景或页面>
- handoff：<携带完整 affected evidence 的 docs-agent:docs-audit ready，或 blocked>
```
