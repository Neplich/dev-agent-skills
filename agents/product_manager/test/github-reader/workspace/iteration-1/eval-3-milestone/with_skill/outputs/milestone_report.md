## 项目状态：facebook/react — 2026-03-20

### Milestones

| Milestone | 进度 | 截止日期 | 状态 |
|-----------|------|---------|------|
| [19.0.0](https://github.com/facebook/react/milestone/40) | 6/11 (54.5%) | 无 | ⚪ 无截止日期 |

> 状态图例：✅ 完成 / 🟢 顺利 / 🟡 进行中 / 🔴 逾期 / ⚪ 无截止日期

**注**：facebook/react 目前仅有 1 个 open milestone（19.0.0），其余历史 milestone 均已关闭。19.0.0 没有设置截止日期，因此按定义不构成"逾期"，但该 milestone 进度停滞迹象明显（见下方分析）。

---

### Milestone 19.0.0 — 详细分析

**完成率：54.5%**（6 个 issue 已关闭，5 个仍 open）

**剩余 Open Issues（全部无 assignee）：**

| Issue | 标题 | 最后更新 | 搁置时长 |
|-------|------|----------|---------|
| [#11972](https://github.com/facebook/react/issues/11972) | Consider removing mouseenter/mouseleave polyfill | 2025-08-26 | ~7 个月 |
| [#11667](https://github.com/facebook/react/issues/11667) | RFC: Drop isAttributeNameSafe() check | 2023-04-21 | ~3 年 |
| [#11799](https://github.com/facebook/react/issues/11799) | Consider removing XML compatibility from SSR or hiding it behind an option | 2020-08-25 | ~5.5 年 |
| [#10143](https://github.com/facebook/react/issues/10143) | Remove unstable_renderIntoContainer | 2020-01-08 | ~6 年 |
| [#11896](https://github.com/facebook/react/issues/11896) | Stop syncing value attribute for controlled inputs | 2018-10-04 | ~7.5 年 |

**结论：19.0.0 是进度最慢的（也是唯一的）open milestone。**

- 无截止日期，所以技术上不算"逾期"
- 但 5 个剩余 issue 平均搁置时长超过 **4 年**，其中最老的 #11896 已搁置 **7.5 年**
- 所有剩余 issue 均**无 assignee**，没有人认领推进
- 这些 issue 多为 breaking changes / cleanups，属于刻意延后的技术债，可能需要 React 团队重新评估是否仍计划在 19.x 完成

---

### Open Issues（仓库整体）

- 总 open issues：**1185 个**
- 100 条样本中：无 assignee 约 **194/200（~97%）**
- 近 14 天关闭：**24 个**（多为 spam 或重复 issue）

---

### PR 队列

**待 Review（非草稿，50 条样本统计）：**
- 总计约 **46 个** open non-draft PR（其中 1 个为 CHANGES_REQUESTED：[#36095](https://github.com/facebook/react/pull/36095)、[#35989](https://github.com/facebook/react/pull/35989)）

**草稿（3 个）：**
- [#36058](https://github.com/facebook/react/pull/36058) [eprh] Bump hermes-parser — @hassankhan
- [#35998](https://github.com/facebook/react/pull/35998) [flow] Upgrade flow-bin to 0.302.0 — @marcoww6
- [#35996](https://github.com/facebook/react/pull/35996) [flow] Migrate type param bounds to extends syntax — @marcoww6

**近 14 天已合并（13 个）：**
- [#36055](https://github.com/facebook/react/pull/36055) [Flight Reply] Early bailout if backing entry for Blob deserialization is not a Blob
- [#36026](https://github.com/facebook/react/pull/36026) Enable Fragment Ref flags across builds
- [#36024](https://github.com/facebook/react/pull/36024) [Flight] Clear chunk reason after successful module initialization
- [#36011](https://github.com/facebook/react/pull/36011) [DevTools] fix: don't show empty suspended by section
- [#36010](https://github.com/facebook/react/pull/36010) Fix focus set for delegated and already focused elements
- [#35999](https://github.com/facebook/react/pull/35999) [enableInfiniteRenderLoopDetection] Warn about potential infinite loop
- [#35994](https://github.com/facebook/react/pull/35994) [DevTools] Ignore new production renderers if we already use "worse" versions
- [#35985](https://github.com/facebook/react/pull/35985) [DevTools] Fix crash when rendering a new class Component with errored state
- [#35636](https://github.com/facebook/react/pull/35636) Update CSS shorthand property list
- 及 4 个 dependabot 安全更新

---

### 健康摘要

- 共 **1185** 个 open issue，约 **50** 个 open PR
- **1** 个 milestone 进行中（19.0.0，完成率 54.5%），**0** 个逾期（无截止日期）
- 近 14 天：合并 **13** 个 PR，关闭 **24** 个 issue
- **最需关注**：Milestone 19.0.0 中 5 个剩余 issue 均无 assignee，平均搁置超 4 年，建议团队重新 triage 或明确是否仍在 scope 内
