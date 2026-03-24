# Project Status Report: anthropics/anthropic-sdk-python

**Report Date:** 2026-03-20
**Data Fetched:** 2026-03-20 via GitHub CLI (`gh`)

---

## 1. Repository Overview

| Field | Value |
|---|---|
| Repository | [anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) |
| Primary Language | Python |
| Stars | 2,983 |
| Forks | 532 |
| Latest Release | v0.86.0 (2026-03-18) |
| Last Push | 2026-03-19 |
| Open Milestones | None configured |

---

## 2. Milestone Progress

No milestones are currently configured in this repository. The project uses a continuous release cadence rather than milestone-based planning.

**Release Velocity (last 10 releases):**

| Version | Release Date |
|---|---|
| v0.86.0 (Latest) | 2026-03-18 |
| v0.85.0 | 2026-03-16 |
| v0.84.0 | 2026-02-25 |
| v0.83.0 | 2026-02-19 |
| v0.82.0 | 2026-02-18 |
| v0.81.0 | 2026-02-18 |
| v0.80.0 | 2026-02-17 |
| v0.79.0 | 2026-02-07 |
| v0.78.0 | 2026-02-05 |
| v0.77.1 | 2026-02-03 |

Release pace has been very active: 6 releases in the month of February 2026 alone, with 2 releases in the first 3 weeks of March 2026. Average release cadence is roughly every 4-7 days.

---

## 3. Open Issues

**Total Open Issues: 75**

### Issues by Label

| Label | Count | Notes |
|---|---|---|
| `api` | ~17 | Issues with the Anthropic API itself (not SDK) |
| `sdk` | ~12 | SDK-specific bugs and feature requests |
| `enhancement` | ~8 | Feature requests and improvements |
| `bedrock` | ~7 | AWS Bedrock integration issues |
| `vertex` | ~3 | Google Vertex AI integration issues |
| `bug` | ~2 | Labeled bugs (many bug reports are unlabeled) |
| `documentation` | ~2 | Documentation gaps |
| `question` | ~1 | Usage questions |
| *(no label)* | ~23 | Unlabeled — mix of bugs, questions, and feature requests |

### Notable Open Issues by Theme

**Streaming / Event Handling**
- [#1258](https://github.com/anthropics/anthropic-sdk-python/issues/1258) — Mid-stream SSE errors get `status_code=200` instead of the actual error code (2026-03-18)
- [#1192](https://github.com/anthropics/anthropic-sdk-python/issues/1192) — `IndexError` when streaming
- [#941](https://github.com/anthropics/anthropic-sdk-python/issues/941) — `content_block_delta` event not deserialized correctly during streaming

**Bedrock Integration**
- [#1210](https://github.com/anthropics/anthropic-sdk-python/issues/1210) — Bedrock `beta.messages` missing `.stream()` method
- [#892](https://github.com/anthropics/anthropic-sdk-python/issues/892) — Bedrock client failing to detect AWS region correctly
- [#1103](https://github.com/anthropics/anthropic-sdk-python/issues/1103) — Token counting not supported in Bedrock

**Tool Use / Server Tools**
- [#1170](https://github.com/anthropics/anthropic-sdk-python/issues/1170) — Tool runner exits early when response has only server tool blocks and `pause_turn`
- [#1237](https://github.com/anthropics/anthropic-sdk-python/issues/1237) — `web_search_20250209` dynamic filtering causes excessive `pause_turn`

**Structured Outputs**
- [#1204](https://github.com/anthropics/anthropic-sdk-python/issues/1204) — Two bugs in structured output + thinking + tool use multi-turn
- [#1185](https://github.com/anthropics/anthropic-sdk-python/issues/1185) — "compiled grammar is too large" error for complex schemas

**Performance**
- [#1195](https://github.com/anthropics/anthropic-sdk-python/issues/1195) — `_transform_recursive` blocking event loop on large message payloads
- [#1211](https://github.com/anthropics/anthropic-sdk-python/issues/1211) — Slow imports

**Mutation Bug (widely reported)**
- [#1202](https://github.com/anthropics/anthropic-sdk-python/issues/1202) — `deepcopy_minimal` in `files.beta.upload` mutates dict in place (multiple PRs addressing this)

**Oldest Open Issues**
- [#432](https://github.com/anthropics/anthropic-sdk-python/issues/432) — Bedrock frequently has server-side errors (opened 2024-04-02)
- [#538](https://github.com/anthropics/anthropic-sdk-python/issues/538) — Feature request: Pydantic round-trip support (opened 2024-06-14)
- [#558](https://github.com/anthropics/anthropic-sdk-python/issues/558) — Feature request: Pydantic validators (opened 2024-06-27)

---

## 4. Pull Request Queue

**Total Open PRs: 50**

### PR Status Breakdown

| Status | Count |
|---|---|
| Awaiting Review (REVIEW_REQUIRED) | 46 |
| Approved (not yet merged) | 2 |
| Draft | 4 |

### Recently Merged PRs

| PR | Title | Merged |
|---|---|---|
| [#1249](https://github.com/anthropics/anthropic-sdk-python/pull/1249) | release: 0.86.0 | 2026-03-18 |
| [#1244](https://github.com/anthropics/anthropic-sdk-python/pull/1244) | fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases | 2026-03-16 |
| [#1209](https://github.com/anthropics/anthropic-sdk-python/pull/1209) | release: 0.85.0 | 2026-03-16 |
| [#1193](https://github.com/anthropics/anthropic-sdk-python/pull/1193) | release: 0.84.0 | 2026-02-25 |

### Open PR Categories (by type)

| Category | Count | Examples |
|---|---|---|
| Bug fixes | ~30 | Streaming, Bedrock region, deepcopy mutation, tool runner |
| Feature additions | ~6 | Observability hooks, enum support, files-from-zip helper |
| Tests | ~4 | Unit tests for tool_runner hooks, tool use example tests |
| Documentation | ~4 | CLAUDE.md, batch custom_id limit, example docstrings |
| Performance | ~2 | Skip no-op transforms, async stream transform deferral |
| Other | ~4 | Misc fixes |

### Approved PRs Pending Merge

| PR | Title | Approved |
|---|---|---|
| [#1183](https://github.com/anthropics/anthropic-sdk-python/pull/1183) | fix(structured outputs): improve error message for invalid `output_format` types | Yes |
| [#1174](https://github.com/anthropics/anthropic-sdk-python/pull/1174) | fix(tool runner): don't exit early on `pause_turn` | Yes |

### Notable Active PR Clusters

**`deepcopy_minimal` mutation fix** — At least 5 separate PRs addressing the same dict mutation bug introduced in file uploads (#1245, #1228, #1226, #1218, #1213), indicating fragmented community effort on a high-impact issue.

**Bedrock region detection** — At least 3 PRs (#1243, #1236, #1207) attempting to fix how the Bedrock client infers the AWS region from `aws_profile`.

**Bedrock `beta.messages.stream()`** — Multiple PRs (#1246, #1230) adding the missing `.stream()` method to Bedrock's beta messages endpoint.

**Tool runner `pause_turn` fix** — Multiple PRs (#1235, #1229, #1174) addressing the early exit on `pause_turn` when server tool use blocks are present. PR #1174 is already approved.

---

## 5. Key Observations

1. **No active milestones.** The project ships continuously via the `stainless-app` bot, with releases triggered by merged changes rather than milestone cycles.

2. **High PR volume with limited throughput.** With 50 open PRs and only ~2 approved/pending merge, there is significant review backlog. Many PRs have been open for weeks without a maintainer review.

3. **Duplicate PR clusters.** Several high-impact bugs (deepcopy mutation, Bedrock region, tool runner pause_turn) have attracted 3-5 competing community PRs addressing the same issue. This suggests the maintainers have not yet acknowledged a preferred fix path in these threads.

4. **Bedrock integration is a pain point.** Issues and PRs related to `AnthropicBedrock` (region detection, missing methods, token counting, retry policy) represent the largest cluster of unresolved problems.

5. **Streaming reliability issues persist.** Multiple open issues and PRs touch streaming deserialization, error handling, and event loop blocking—suggesting this subsystem needs a systematic review.

6. **Active community engagement.** 75 open issues and 50 open PRs on a relatively focused SDK indicate a large and engaged user base, but also points to a need for more maintainer bandwidth or clearer contribution guidelines to reduce noise.

---

*Data sourced via `gh` CLI on 2026-03-20. Issue and PR counts reflect the state at time of query.*
