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

Consume the shared frontmatter contract
(`agents/docs/skills/docs-agent/_internal/_shared/frontmatter-contract.md`)
for every created or updated manual page. When a section's pages need a
business-logic order that path slugs cannot express, `nav_order` may be written
per the contract's Optional Fields — but only after confirming the host's
delivered `docs/site/scripts/lib/sidebar.mjs` references `nav_order` in its
ordering logic. Delivered bootstrap assets are not upgraded automatically; on a
pre-upgrade host that ignores the field, do not write `nav_order` and report
in the batch summary that the host must rerun `docs-site-bootstrap` (or merge a
confirmed bootstrap upgrade) before the field can take effect.

## 2. Read the unique manual template and inspect the existing structure

Follow the host standards entry to the manual template under
`docs/site/standards/templates/`. Read its unique `docs-scaffold` block and
the existing `docs/site/manual/**` paths, frontmatter, indexes, and navigation
needed to place the confirmed scope.

Apply the `change_mode` from `../SKILL.md`. Under `extend`, keep an existing
path only when current code and interface evidence still support its ownership;
new functionality may add a leaf page or split a subdirectory. Under `rewrite`,
use existing pages only to identify facts, links, and migration needs; do not
inherit their tree as the target structure.

The host manual template is the only template source. This specialist must not
embed, reconstruct, or maintain a second copy of the template body. When the
host exposes `npm run new:doc`, prefer that deterministic scaffold entry for a
confirmed new page.

## 3. Inventory the confirmed scope and build the coverage matrix

Use only the environment confirmed by `../SKILL.md`. Inspect current code,
routes, role and permission evidence, and the actual interface to identify
roles, business scenarios, entry points, prerequisites, visible controls,
operation sequences, outcomes, and exception states. Base every candidate
operation on code and interface evidence; record gaps instead of filling them
with assumptions.

For `bounded`, inventory only the confirmed pages, roles, features, or flows and
their necessary parent navigation. Do not expand it into an unrelated user-side
or admin-side inventory.

For `full-manual`, inventory every confirmed user-visible route, menu action,
button, dialog, and supported role before writing any page. Existing manual
directories do not limit this inventory. For `full-site`, apply the same rule to
the already separated manual slice; non-manual surfaces stay with their owning
specialists.

Produce a coverage matrix with these fields:

- role;
- route or entry point;
- visible feature;
- independent user goal;
- operation and expected result;
- permission, prerequisite, or risk;
- target parent page;
- one owning leaf page;
- interface and code evidence; and
- screenshot requirement.

Map controls to user tasks before assigning pages. A button or dialog may be a
step inside a task and does not mechanically require its own page. Every
independent user task must map to exactly one owning leaf page, and every
candidate leaf page must map back to at least one evidenced task. Resolve
unowned or multiply owned tasks before any site write.

## 4. Present the page tree and implementation batches for confirmation

Before any manual page, screenshot asset, change-map, index, or navigation
write, present:

- the recorded `scope_mode` and `change_mode` with their evidence;
- the covered roles and business scenarios;
- the coverage matrix;
- the candidate parent-child page tree;
- each existing path to keep, add, split, replace, or remove, with its current-
  product evidence;
- each page's interface evidence and screenshot plan;
- the proposed change-map, index, and host-required navigation delta;
- explicit exclusions, unresolved discrepancies, and out-of-batch scope; and
- the ordered implementation batches and completion gate.

Create a separate leaf page when any condition holds: the task has an
independent entry or control; a user can complete it separately; it has an
independent expected result; it has distinct permission, prerequisite, risk,
or exception handling; it needs separate screenshot evidence; or it has a
different update cadence. Actions that must run together to reach one goal and
share the same entry and result may stay on one leaf page.

Wait for explicit maintainer confirmation. Unconfirmed scope receives zero
writes.

- For `bounded`, confirm and execute one finite batch. Any additional candidate
  requires a new confirmation.
- For `full-manual`, confirm the complete matrix, target tree, all ordered
  batches, and exclusions once. Execute one approved batch at a time, report
  its status, and continue through the remaining approved batches. Do not
  reinterpret a batch boundary as permission to shrink the complete scope or
  require a new scope confirmation. Pause only when scope, tree, side-effect
  boundary, or material evidence changes.

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

1. Explicitly set the browser window to the maintainer-confirmed desktop size.
   If no size was supplied, `1920×1080` may be used as the window target, not
   as an assumed content viewport.
2. Read the actual browser window width and height back from the running
   environment.
3. Separately read the actual page content viewport width and height from the
   running environment, using its layout-viewport reading or page values such
   as `window.innerWidth` and `window.innerHeight`.
4. 回读结果必须来自运行环境的实际读数，不得由设定值推断。Browser chrome may
   make the content viewport smaller than the window; that difference is not a
   failure by itself.
5. Confirm the content viewport renders the intended desktop layout. If either
   read-back is unavailable or the page enters an unintended mobile or other
   responsive layout, stop capture and record the blocker.
6. Preserve each captured image's natural aspect ratio. Do not resample it or
   force both width and height into `1920×1080`, 16:9, or another mismatched
   display box. Product-content cropping is allowed only when it does not
   distort the remaining pixels.

`窗口设定`, `窗口回读`, `内容视口回读`, and `截图自然尺寸` are separate report
fields; if any is missing, this step is incomplete. This contract prevents a
window target from being mistaken for the smaller Chrome content viewport and
also prevents a valid content screenshot from being stretched afterward.

### Screenshot hygiene

Keep the same window, content viewport, zoom, theme, and navigation state
throughout one batch. Capture product content only. Exclude browser tabs, address bar,
toolbars, window borders, loading states, translation popups, promotional
banners, marketing dialogs, and other overlays unrelated to the documented
task.

A menu or dialog that is itself part of the confirmed operation is product
evidence, not an overlay to remove: when a step opens an export, share, or
similar control, capture that expanded menu or dialog as the step's visible
interface. Exclude only overlays that no confirmed step depends on.

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

Use the host's navigation mechanism and headings; do not hard-code a new site
directory scheme. Apply the confirmed `change_mode`: `extend` keeps supported
paths and makes only the confirmed additions or splits; `rewrite` implements
the confirmed current-product tree and its migration/link delta.

Group and index pages describe scope, supported roles, relationships, and
navigation only. They must not substitute for reproducible operation pages or
duplicate their detailed steps. Each leaf operation page must satisfy all
fields defined by the authoritative manual template: applicable role,
prerequisites, numbered steps, visible interface description, screenshot and
caption, expected result, and notes or exception handling. A leaf page that
ends at a capability overview is incomplete.

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

Run a page-level content check after writing: every leaf page must contain
prerequisites, numbered steps, visible interface evidence, expected results,
and exception handling. Reject capability-overview-only leaves. Verify that
parent indexes describe scope, relations, and navigation without duplicating or
replacing the operation pages.

Then reconcile the coverage matrix in both directions:

- every evidenced independent task has exactly one owning leaf page;
- every operation leaf maps back to evidenced matrix entries;
- every confirmed visible route, menu action, button, dialog, and role is
  covered by a leaf task, recorded as a step within one, explicitly excluded,
  or blocked with named missing evidence; and
- every page is reachable through the expected navigation.

For `full-manual`, a reviewer other than the author must independently compare
the current code, routes, running interface, matrix, and delivered tree and
report no unexplained omissions. Build, link, and rendering success cannot
replace this coverage review. The manual remains incomplete until all approved
batches and this review pass.

When the affected host has public and internal variants, inspect each affected
landing/index surface and changed content surface. Verify that header, sidebar,
content width, and screenshot rendering follow the host's intended variant
styles without cross-page inconsistency or image distortion.

If required dependencies have no host-defined deterministic installation path,
or any required check or visual acceptance cannot be completed, stop and
report the missing evidence. Do not mark the manual complete.

## 8. Handoff to docs audit

After all confirmed writes, read-back checks, host checks, matrix reconciliation,
independent review when required, and visual acceptance pass, hand the complete
affected page, screenshot, mapping, index, navigation, and evidence set to
`docs-agent:docs-audit`. For `full-manual`, this means all approved batches, not
the first completed batch. Enter pre-tag audit
only when a maintainer has explicitly confirmed `target_release_version`;
include that value and its confirmation source in the handoff. Otherwise keep
every new or updated page at `last_verified_version: unverified`, return a
blocked handoff that explicitly waits for confirmed release context, and never
infer a version from refs, branch names, or other context. A manual generation
report is not a stamp or release authorization. Only `docs-audit` may apply a
verified version anchor.

If the environment, login state, feature availability, screenshot permission,
eligible execution entry, viewport read-back, host check, matrix reconciliation,
required independent review, or rendering acceptance is unavailable or fails,
return `blocked`. Record the blocker, owner, missing evidence, and next action.
Never claim completion, invent an interface, or substitute an unrelated example
image.

## Boundaries

- Do not modify the five-type contract or eight-step flow of
  `formal-docs-sync`.
- Do not generate or edit Release Notes surfaces.
- Do not create or move tags, execute release operations, or initialize a
  documentation site.
- Do not add a screenshot-expiry mechanism, browser framework, startup script,
  or separate asset-publication convention.
- Do not let a bounded request expand into a complete manual, or let batch
  boundaries reduce a confirmed complete-manual scope.

## Report Shape

```markdown
## Manual generation result

- scope_mode / change_mode：<bounded | full-manual | full-site manual slice> / <extend | rewrite>；<判定依据>
- 确认范围：<角色、场景、页面树、批次、排除项>
- 覆盖矩阵：<完整矩阵或其经确认的持久位置；任务与叶子页归属>
- 运行环境与来源：<域名或获明确同意的本地环境；确认来源>
- 执行入口：<repo harness | Chrome plugin / browser connector | Playwright fallback；覆盖理由>
- 窗口设定：<明确的设定命令或操作及目标窗口尺寸>
- 窗口回读：<从运行环境读取的实际窗口宽度和高度>
- 内容视口回读：<从运行环境读取的实际内容视口宽度和高度>
- 截图自然尺寸：<每张截图的原始宽度、高度和宽高比校验>
- 采集截图清单：<页面、步骤、资产路径、图注，或 none>
- 变更页面：<路径或 none>
- change-map 增量：<条目及原子 required-doc closure，或 none>
- 宿主检查结果：<命令、cwd、退出状态、结果>
- 单页完整性：<叶子页字段、索引页职责和导航可达检查>
- 覆盖校验：<矩阵双向映射、可见控件/角色审计、独立复核结果>
- 渲染验收结果：<各受影响站点变体的首页/索引/内容页目视结果>
- 阻塞项：<事项、owner、缺失证据、下一步，或 none>
- 批次状态：<每个已确认批次的状态；bounded 的范围外候选>
- handoff：<docs-audit ready，或等待维护者确认 target_release_version 的 blocked；ready 时包含该值与确认来源>
```
