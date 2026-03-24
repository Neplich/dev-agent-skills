# golang/go 项目路线图

> 基于 GitHub 里程碑、Issue 和 PR 数据自动生成 | 数据获取日期: 2026-03-20
>
> 仓库: [golang/go](https://github.com/golang/go)

---

## 📊 总览

| 里程碑 | 状态 | 开放 | 已关闭 | 进度 |
|--------|------|------|--------|------|
| [Go1.26.2](https://github.com/golang/go/milestone/430) | 🔧 补丁发布 | 25 | 0 | ░░░░░░░░░░ 0% |
| [Go1.25.9](https://github.com/golang/go/milestone/431) | 🔧 补丁发布 | 5 | 3 | ██████░░░░ 38% |
| [Go1.27](https://github.com/golang/go/milestone/408) | 🚀 下一主版本 | 327 | 146 | ███░░░░░░░ 31% |
| [Go1.28](https://github.com/golang/go/milestone/423) | 📋 规划中 | 4 | 0 | ░░░░░░░░░░ 0% |
| [gopls/v0.22.0](https://github.com/golang/go/milestone/415) | 🔨 开发中 | 12 | 26 | ███████░░░ 68% |
| [gopls/v0.23.0](https://github.com/golang/go/milestone/432) | 📋 规划中 | 32 | 1 | ░░░░░░░░░░ 3% |
| [Proposal](https://github.com/golang/go/milestone/30) | 🔄 持续进行 | 990 | 3606 | ████████░░ 78% |
| [Backlog](https://github.com/golang/go/milestone/117) | 🔄 持续进行 | 2581 | 2755 | █████░░░░░ 52% |
| [Unplanned](https://github.com/golang/go/milestone/6) | 🔄 持续进行 | 1944 | 2901 | ██████░░░░ 60% |
| [Unreleased](https://github.com/golang/go/milestone/22) | 🔄 持续进行 | 1809 | 8782 | ████████░░ 83% |

---

## 🔧 第一阶段：当前补丁发布

### Go 1.26.2 — 补丁修复

> 里程碑: [Go1.26.2](https://github.com/golang/go/milestone/430) | 开放: 25 | 已关闭: 0

当前最新稳定版本的补丁发布，聚焦于回溯修复（backport）关键 bug。

#### 编译器与运行时

| Issue | 标题 | 状态 |
|-------|------|------|
| [#78198](https://github.com/golang/go/issues/78198) | cmd/compile: panic on invalid generic append with type parameter spread | CherryPickCandidate |
| [#78087](https://github.com/golang/go/issues/78087) | runtime: `go runtime.GC()` can cause segfault with `-race` builds | CherryPickCandidate |
| [#78041](https://github.com/golang/go/issues/78041) | runtime: Windows crash with Go 1.26.0, 1.26.1 | CherryPickApproved |
| [#77922](https://github.com/golang/go/issues/77922) | cmd/compile: internal compiler error len larger than cap for OSLICEHEADER | CherryPickApproved |
| [#77856](https://github.com/golang/go/issues/77856) | runtime: allocation in printfloat64 causes throw | CherryPickApproved |
| [#77838](https://github.com/golang/go/issues/77838) | cmd/compile: internal compiler error: panic: interface conversion | CherryPickApproved |
| [#77809](https://github.com/golang/go/issues/77809) | cmd/compile: internal compiler error: cannot represent parameters of type struct | CherryPickApproved |
| [#77799](https://github.com/golang/go/issues/77799) | runtime: segmentation violation when debug and using race detector | CherryPickApproved |
| [#77773](https://github.com/golang/go/issues/77773) | cmd/compile: internal compiler error: panic during rewrite tern with GOEXPERIMENT=simd | CherryPickApproved |
| [#77731](https://github.com/golang/go/issues/77731) | runtime: regression segfault on linux 3.4 on mipsle | CherryPickApproved |
| [#77935](https://github.com/golang/go/issues/77935) | runtime: on 32bits arches timespec (64) definition is wrong | CherryPickCandidate |
| [#77931](https://github.com/golang/go/issues/77931) | runtime: regression Synology's Linux fork causes syscall conflict | CherryPickCandidate |
| [#77880](https://github.com/golang/go/issues/77880) | runtime: regression seccomp on 32bits Androids <= 10 | CherryPickCandidate |

#### 标准库与工具链

| Issue | 标题 | 状态 |
|-------|------|------|
| [#78191](https://github.com/golang/go/issues/78191) | cmd/fix: panics with "package path has no import prefix" | CherryPickApproved |
| [#78155](https://github.com/golang/go/issues/78155) | testing: B.Loop loop allows body to be optimized away (1.26 regression) | CherryPickApproved |
| [#78111](https://github.com/golang/go/issues/78111) | net/url: url.Parse breaks mongodb connection string parsing | CherryPickCandidate |
| [#78058](https://github.com/golang/go/issues/78058) | cmd/go: DiskCache.Trim on macOS blocks go command for >20 minutes | CherryPickApproved |
| [#78019](https://github.com/golang/go/issues/78019) | net/http: race condition on Windows when using os.File as request body | CherryPickApproved |
| [#77885](https://github.com/golang/go/issues/77885) | net: ReadMsgUDP/WriteMsgUDP fails with WSAEFAULT on Windows | CherryPickApproved |
| [#77800](https://github.com/golang/go/issues/77800) | cmd/fix: fix can fail without actually applying any fixes | CherryPickApproved |

#### 文档

| Issue | 标题 | 状态 |
|-------|------|------|
| [#77950](https://github.com/golang/go/issues/77950) | net/http: package doc comment is missing | CherryPickApproved |
| [#77586](https://github.com/golang/go/issues/77586) | builtin: update new documentation for Go 1.26 expression syntax | CherryPickApproved |

---

### Go 1.25.9 — 补丁修复

> 里程碑: [Go1.25.9](https://github.com/golang/go/milestone/431) | 开放: 5 | 已关闭: 3

上一稳定版本的安全与关键 bug 修复。

| Issue | 标题 | 标签 |
|-------|------|------|
| [#78086](https://github.com/golang/go/issues/78086) | runtime: `go runtime.GC()` can cause segfault with `-race` builds | CherryPickCandidate |
| [#78057](https://github.com/golang/go/issues/78057) | cmd/go: DiskCache.Trim on macOS blocks go command for >20 minutes | CherryPickApproved |
| [#77968](https://github.com/golang/go/issues/77968) | crypto/x509: overly broad excluded constraints | CherryPickApproved |
| [#77921](https://github.com/golang/go/issues/77921) | cmd/compile: internal compiler error len larger than cap for OSLICEHEADER | CherryPickApproved |
| [#77298](https://github.com/golang/go/issues/77298) | cmd/compile: per-loop variable with line directive | CherryPickCandidate |

---

## 🚀 第二阶段：下一主版本 — Go 1.27

> 里程碑: [Go1.27](https://github.com/golang/go/milestone/408) | 开放: 327 | 已关闭: 146 | 进度: 31%

```
进度: ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 31% (146/473)
```

### Issue 分类统计

| 分类 | 数量 | 占比 |
|------|------|------|
| NeedsInvestigation | 64 | 19.6% |
| BugReport | 51 | 15.6% |
| compiler/runtime | 34 | 10.4% |
| GoCommand | 18 | 5.5% |
| NeedsFix / FixPending | 24 | 7.3% |
| Tools | 10 | 3.1% |
| Performance | 4 | 1.2% |
| Documentation | 5 | 1.5% |
| Proposal / Proposal-Accepted | 11 | 3.4% |
| release-blocker | 6 | 1.8% |
| OS-Windows | 4 | 1.2% |

### 发布阻塞项 (Release Blockers)

| Issue | 标题 |
|-------|------|
| [#78134](https://github.com/golang/go/issues/78134) | cmd/compile: internal compiler error: bad live variable at entry |
| [#78081](https://github.com/golang/go/issues/78081) | cmd/compile: unexplained compiler panic build flakes |
| [#76472](https://github.com/golang/go/issues/76472) | remove gotypesalias, asynctimerchan GODEBUG flag for 1.27 |
| [#75836](https://github.com/golang/go/issues/75836) | all: end support for macOS 12 in Go 1.27 |
| [#60792](https://github.com/golang/go/issues/60792) | all: announce end of support for old Linux versions |
| [#60234](https://github.com/golang/go/issues/60234) | cmd/compile: update compiler's PGO profile |
| [#52188](https://github.com/golang/go/issues/52188) | all: announce end of support for old Windows releases |
| [#40561](https://github.com/golang/go/issues/40561) | x/build: update release targets for upcoming major Go release |
| [#36905](https://github.com/golang/go/issues/36905) | all: update standard-library dependencies |
| [#22487](https://github.com/golang/go/issues/22487) | lib/time: update tzdata before release |
| [#23011](https://github.com/golang/go/issues/23011) | all: announce end of support for old macOS releases |

### 重点工作领域

#### 编译器与运行时改进

- 多项内部编译器错误修复 (ICE bugs)
- PGO (Profile-Guided Optimization) 改进: [#69046](https://github.com/golang/go/issues/69046), [#58298](https://github.com/golang/go/issues/58298), [#59612](https://github.com/golang/go/issues/59612)
- 迭代器性能优化: [#69015](https://github.com/golang/go/issues/69015)
- GC 改进: [#61426](https://github.com/golang/go/issues/61426), [#73835](https://github.com/golang/go/issues/73835)
- 逃逸分析改进: [#62653](https://github.com/golang/go/issues/62653), [#62501](https://github.com/golang/go/issues/62501)
- 废弃 SetFinalizer: [#70425](https://github.com/golang/go/issues/70425)
- FIPS 140-3 验证: [#69536](https://github.com/golang/go/issues/69536)
- HTTP/2 移入标准库: [#67810](https://github.com/golang/go/issues/67810)
- `go fix` 内联功能相关 bug 修复（多项）

#### 平台支持变更

- 结束 macOS 12 支持: [#75836](https://github.com/golang/go/issues/75836)
- 旧版 Linux 支持公告: [#60792](https://github.com/golang/go/issues/60792)
- 旧版 Windows 支持公告: [#52188](https://github.com/golang/go/issues/52188)
- 移除旧 GODEBUG 标志: [#76472](https://github.com/golang/go/issues/76472), [#75316](https://github.com/golang/go/issues/75316)

#### Go 命令与模块

- 构建缓存问题: [#69566](https://github.com/golang/go/issues/69566), [#73033](https://github.com/golang/go/issues/73033)
- `go work sync` 修复: [#65363](https://github.com/golang/go/issues/65363), [#63901](https://github.com/golang/go/issues/63901)
- `go mod verify -tag`: [#68669](https://github.com/golang/go/issues/68669)

---

## 📋 第三阶段：远期规划 — Go 1.28

> 里程碑: [Go1.28](https://github.com/golang/go/milestone/423) | 开放: 4 | 已关闭: 0

Go 1.28 目前处于早期规划阶段，仅有少量基础设施 issue。

| Issue | 标题 | 标签 |
|-------|------|------|
| [#77341](https://github.com/golang/go/issues/77341) | build: adopt Go 1.26 as bootstrap toolchain for Go 1.28 | release-blocker, early-in-cycle |
| [#73152](https://github.com/golang/go/issues/73152) | cmd/go: confusing situation with 'go run' and '//go:build ignore' | NeedsInvestigation |
| [#67799](https://github.com/golang/go/issues/67799) | cmd/go: duplicate libobjc library with 2+ cgo packages with Objective-C | NeedsInvestigation |
| [#40705](https://github.com/golang/go/issues/40705) | internal/goversion: increment Version at start of cycle | release-blocker, recurring |

---

## 🛠️ 工具生态系统

### gopls/v0.22.0

> 里程碑: [gopls/v0.22.0](https://github.com/golang/go/milestone/415) | 开放: 12 | 已关闭: 26 | 进度: 68%

```
进度: ██████████████████████████████████░░░░░░░░░░░░░░░░░░ 68% (26/38)
```

| Issue | 标题 | 类型 |
|-------|------|------|
| [#78142](https://github.com/golang/go/issues/78142) | OOB index in extractFunctionMethod | Bug |
| [#78110](https://github.com/golang/go/issues/78110) | go/ssa: next tuple and bound method closure omit explicit interface conversion | Bug |
| [#77814](https://github.com/golang/go/issues/77814) | mcp exhausts file descriptors | Bug |
| [#77802](https://github.com/golang/go/issues/77802) | implementations: not working on dynamic function calls | Bug |
| [#77396](https://github.com/golang/go/issues/77396) | proposal: pause gopls from command line | Proposal |
| [#77336](https://github.com/golang/go/issues/77336) | TestMCPCommandLogging/trace.log failures | Bug |
| [#76803](https://github.com/golang/go/issues/76803) | yield analysis: false positive with reified boolean | Bug |
| [#76331](https://github.com/golang/go/issues/76331) | experimental LSP dialog support | Feature |
| [#75469](https://github.com/golang/go/issues/75469) | Completion of generic argument resulting in invalid casting | Bug |
| [#74686](https://github.com/golang/go/issues/74686) | symbolic link to / causes ModuleResolver to scan entire file system | Bug |
| [#74292](https://github.com/golang/go/issues/74292) | add file watcher for headless mode | Feature |
| [#74258](https://github.com/golang/go/issues/74258) | TestMCPCommandStdio flake due to race condition | Bug |

### gopls/v0.23.0

> 里程碑: [gopls/v0.23.0](https://github.com/golang/go/milestone/432) | 开放: 32 | 已关闭: 1 | 进度: 3%

重点方向:
- MCP (Model Context Protocol) 服务器改进: [#77960](https://github.com/golang/go/issues/77960), [#78083](https://github.com/golang/go/issues/78083)
- 重构能力增强: 内联改进 ([#70759](https://github.com/golang/go/issues/70759), [#70085](https://github.com/golang/go/issues/70085), [#66370](https://github.com/golang/go/issues/66370)), 类型移动 ([#57016](https://github.com/golang/go/issues/57016)), 声明移动 ([#70583](https://github.com/golang/go/issues/70583))
- 代码现代化分析器: unsafe.Add 替换 ([#76648](https://github.com/golang/go/issues/76648)), errors.AsType ([#75692](https://github.com/golang/go/issues/75692))
- 遥测驱动的崩溃修复（多项 telemetry-wins 标签 issue）
- 漏洞检查 IDE 支持: [#75447](https://github.com/golang/go/issues/75447)

---

## 📝 提案 (Proposals)

> 里程碑: [Proposal](https://github.com/golang/go/milestone/30) | 开放: 990 | 已关闭: 3606

```
处理进度: ████████████████████████████████████████░░░░░░░░░░ 78% (3606/4596)
```

### 近期活跃提案

| Issue | 标题 | 类型 |
|-------|------|------|
| [#78205](https://github.com/golang/go/issues/78205) | cmd/cover: add -text flag for terminal coverage output | ToolProposal |
| [#78189](https://github.com/golang/go/issues/78189) | runtime/jit: user frame support for JIT compilers and VMs | LibraryProposal |
| [#78160](https://github.com/golang/go/issues/78160) | cmd/fix: add `//go:fix remove` directive for obsolete calls | ToolProposal |
| [#78141](https://github.com/golang/go/issues/78141) | crypto/hkdf: add ExpandBytes and KeyBytes for byte slice info | LibraryProposal |
| [#78090](https://github.com/golang/go/issues/78090) | cmd/go: delete bzr support | ToolProposal |
| [#78072](https://github.com/golang/go/issues/78072) | os: support deleting files with POSIX semantics for Windows 2019 and older | LibraryProposal |
| [#78064](https://github.com/golang/go/issues/78064) | x/net/http2: deprecate Transport and Server | LibraryProposal |
| [#78054](https://github.com/golang/go/issues/78054) | log/slog: add `Uint`, `SignedInt` | LibraryProposal |
| [#78008](https://github.com/golang/go/issues/78008) | reflect: add `Value.TypeAssert[T any]` | LibraryProposal |
| [#78007](https://github.com/golang/go/issues/78007) | reflect: add `Value.Unpack[T any]` for unpacking Values into Go types | LibraryProposal |

---

## 🔄 近期活跃 Pull Requests

| PR | 标题 | 作者 |
|----|------|------|
| [#78232](https://github.com/golang/go/pull/78232) | regexp/syntax: extract maxRepeat constant and document nested repetition limit | kunwar-vikrant |
| [#78206](https://github.com/golang/go/pull/78206) | cmd/go: report importer-specific positions in go list dependency errors | fenghaojiang |
| [#78194](https://github.com/golang/go/pull/78194) | cmd/link: propagate Mach-O section alignment to symbol in loadmacho | penglei |
| [#78151](https://github.com/golang/go/pull/78151) | debug/macho: return FormatError for truncated or empty files | zheliu2 |
| [#78150](https://github.com/golang/go/pull/78150) | os/user: return UnknownUserError for ERROR_NONE_MAPPED on Windows | zheliu2 |
| [#78125](https://github.com/golang/go/pull/78125) | os: fix Chtimes timestamp overflow for dates outside 1677-2262 | zheliu2 |
| [#78124](https://github.com/golang/go/pull/78124) | runtime: skip /proc reads when containermaxprocs=0 | zheliu2 |
| [#78080](https://github.com/golang/go/pull/78080) | slices: document backing array behavior in package doc | kovan |
| [#78024](https://github.com/golang/go/pull/78024) | cmd/go/internal/modfetch/codehost: set LC_ALL=C for VCS commands | JackDanger |
| [#77962](https://github.com/golang/go/pull/77962) | crypto/x509: avoid false wildcard matches for 2-label exclusions | willswire |

---

## 📦 积压与未规划

### Backlog（积压）

> 里程碑: [Backlog](https://github.com/golang/go/milestone/117) | 开放: 2,581 | 已关闭: 2,755

大量长期 issue，涵盖编译器优化、运行时改进、标准库增强等。近期新增:

| Issue | 标题 |
|-------|------|
| [#78220](https://github.com/golang/go/issues/78220) | crypto/tls: Seg Fault In TLS Handshake in RKE |
| [#78218](https://github.com/golang/go/issues/78218) | crypto/internal/fips140/bigmod: extendedGCD Implementation Mismatch |
| [#78203](https://github.com/golang/go/issues/78203) | cmd/compile: use table lookups for switch statements with dense integer const cases |
| [#78178](https://github.com/golang/go/issues/78178) | crypto/tls: X25519MLKEM768 always fails under GODEBUG=fips140=only |
| [#78172](https://github.com/golang/go/issues/78172) | net/http: server does not validate IP-literal Host headers per RFC 3986 |

### Unplanned（未规划）

> 里程碑: [Unplanned](https://github.com/golang/go/milestone/6) | 开放: 1,944 | 已关闭: 2,901

无特定发布计划的 issue。

### 其他积压里程碑

| 里程碑 | 开放 | 已关闭 | 链接 |
|--------|------|--------|------|
| gopls/backlog | 364 | 141 | [查看](https://github.com/golang/go/milestone/192) |
| gopls/unplanned | 112 | 108 | [查看](https://github.com/golang/go/milestone/180) |
| pkgsite/backlog | 73 | 71 | [查看](https://github.com/golang/go/milestone/263) |
| pkgsite/unplanned | 92 | 321 | [查看](https://github.com/golang/go/milestone/167) |
| website/backlog | 30 | 62 | [查看](https://github.com/golang/go/milestone/269) |
| website/unplanned | 20 | 26 | [查看](https://github.com/golang/go/milestone/249) |
| vuln/unplanned | 72 | 202 | [查看](https://github.com/golang/go/milestone/288) |
| Gccgo | 70 | 329 | [查看](https://github.com/golang/go/milestone/23) |
| gollvm | 38 | 41 | [查看](https://github.com/golang/go/milestone/100) |
| Unreleased | 1,809 | 8,782 | [查看](https://github.com/golang/go/milestone/22) |

---

## 🗺️ 路线图时间线总结

```
阶段一 [当前]     Go 1.26.2 补丁 + Go 1.25.9 补丁
                   ├── 25 个回溯修复待合并 (Go 1.26.2)
                   └── 5 个回溯修复待合并 (Go 1.25.9)

阶段二 [开发中]   Go 1.27 主版本
                   ├── 327 个开放 issue, 146 已关闭
                   ├── 13 个发布阻塞项
                   ├── 重点: 编译器稳定性, go fix, 平台支持变更
                   └── 重点: PGO 改进, HTTP/2 标准化, FIPS 验证

阶段三 [规划中]   Go 1.28
                   └── 4 个基础设施 issue (引导工具链升级等)

工具生态           gopls v0.22.0 (68% 完成) → v0.23.0 (规划中)
                   ├── MCP 服务器改进
                   ├── 重构能力增强
                   └── 遥测驱动的稳定性修复

持续进行           990 个活跃提案 | 2,581 积压 | 1,944 未规划
```

---

*本路线图基于 [golang/go](https://github.com/golang/go) GitHub 数据自动生成，反映数据获取时的项目状态。*
