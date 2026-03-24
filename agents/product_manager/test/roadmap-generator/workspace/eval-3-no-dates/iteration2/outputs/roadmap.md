# Go Project Roadmap — golang/go
> Generated: 2026-03-20 | Source: GitHub Milestones & Issues

---

## Milestone Classification Summary

| Category | Milestones |
|---|---|
| 🔧 当前补丁 (Patch Releases) | Go1.26.2, Go1.25.9 |
| 🚀 下一版本 (Next Release) | Go1.27, gopls/v0.22.0 |
| 🔵 远期规划 (Far Future) | Go1.28 |
| 🛠️ 工具生态 (Tool Ecosystem) | gopls/v0.23.0, gopls/v0.22.0, gorelease, vuln/v1.1.0, Gccgo, gollvm |
| 🌐 子项目 (Sub-Projects) | pkgsite/search, pkgsite/upcoming, pkgsite/backlog, website/*, proxy.golang.org/*, pkgsite/unplanned |
| ⚪ 未排期 (Unplanned/Backlog) | Backlog, Unplanned, Proposal, gopls/unplanned, gopls/backlog, vuln/unplanned, pkgsite/unplanned, website/unplanned |

---

## 🔧 当前补丁 — Patch Releases

### Go1.26.2
> Milestone #430 | 22 open issues, 4 closed | Semantic: Patch version → 🔧 当前补丁

**🚨 发布阻塞项 (Release Blockers)**

All issues in this milestone are backport candidates from Go1.26 regression fixes:

**Compiler/Runtime Fixes:**
- [#78239](https://github.com/golang/go/issues/78239) `cmd/link`: panic on darwin/arm64 in go1.26.0: nil pointer deref in `arm64.gensymlate` / `SetSymSect` — `[CherryPickCandidate, compiler/runtime]`
- [#78198](https://github.com/golang/go/issues/78198) `cmd/compile`: panic on invalid generic append with type parameter spread — `[CherryPickCandidate, compiler/runtime]`
- [#78087](https://github.com/golang/go/issues/78087) `runtime`: `go runtime.GC()` can cause segfault with `-race` builds — `[CherryPickCandidate, compiler/runtime]`
- [#78041](https://github.com/golang/go/issues/78041) `runtime`: Windows crash with Go 1.26.0, 1.26.1 — `[CherryPickApproved, compiler/runtime]`
- [#77935](https://github.com/golang/go/issues/77935) `runtime`: on 32-bit arches timespec (64) definition is wrong — `[CherryPickCandidate, compiler/runtime]`
- [#77931](https://github.com/golang/go/issues/77931) `runtime`: regression Synology's Linux fork causes syscall conflict on older kernel versions — `[CherryPickCandidate, compiler/runtime]`
- [#77922](https://github.com/golang/go/issues/77922) `cmd/compile`: ICE len larger than cap for `OSLICEHEADER` — `[CherryPickApproved, compiler/runtime]`
- [#77880](https://github.com/golang/go/issues/77880) `runtime`: `seccomp prevented call to disallowed arm system call 422` on 32-bit Androids ≤ 10 — `[WaitingForInfo, CherryPickCandidate, compiler/runtime]`
- [#77809](https://github.com/golang/go/issues/77809) `cmd/compile`: ICE: cannot represent parameters of type struct... — `[CherryPickApproved, compiler/runtime]`
- [#77799](https://github.com/golang/go/issues/77799) `runtime`: segmentation violation when using race detector with debug — `[CherryPickApproved, compiler/runtime]`
- [#77773](https://github.com/golang/go/issues/77773) `cmd/compile`: ICE panic during rewrite tern with `GOEXPERIMENT=simd` — `[CherryPickApproved, compiler/runtime]`
- [#77731](https://github.com/golang/go/issues/77731) `runtime`: regression segfault on linux 3.4 on mipsle — `[CherryPickApproved, compiler/runtime]`
- [#77836](https://github.com/golang/go/issues/77836) `test/convert5`: output does not match expected on mipsle — `[CherryPickApproved, arch-mips]`

**Go Command Fixes:**
- [#78058](https://github.com/golang/go/issues/78058) `cmd/go`: `DiskCache.Trim` on macOS often blocks go command for >20 minutes — `[GoCommand, CherryPickApproved]`
- [#77801](https://github.com/golang/go/issues/77801) `cmd/fix`: change `-diff` to exit 1 if diffs exist — `[GoCommand, CherryPickCandidate]`

**Standard Library / Networking:**
- [#78019](https://github.com/golang/go/issues/78019) `net/http`: race condition on Windows when using `os.File` as request body — `[CherryPickApproved]`
- [#78111](https://github.com/golang/go/issues/78111) `net/url`: `url.Parse` in 1.26 breaks MongoDB connection string parsing with multiple hosts — `[CherryPickCandidate]`

**Tooling/Docs:**
- [#78191](https://github.com/golang/go/issues/78191) `cmd/fix`: panics with "package path has no import prefix" — `[CherryPickApproved]`
- [#77800](https://github.com/golang/go/issues/77800) `cmd/fix`: fix can print "applied 8 of 10 fixes; 2 files updated" but fail to apply any — `[CherryPickApproved]`
- [#77586](https://github.com/golang/go/issues/77586) `builtin`: update `new` documentation for Go 1.26 expression syntax — `[Documentation, CherryPickApproved]`

**Still Under Review:**
- [#78155](https://github.com/golang/go/issues/78155) `testing`: within `B.Loop`, assigning function result to `_` allows body to be optimized away (1.26 regression) — `[CherryPickApproved]`
- [#77297](https://github.com/golang/go/issues/77297) `cmd/compile`: go1.22+ cmd with `go.mod` 1.21 generates per-loop variable when using line directive — `[WaitingForInfo, CherryPickCandidate]`

---

### Go1.25.9
> Milestone #431 | 5 open issues, 3 closed | Semantic: Patch version → 🔧 当前补丁

**Compiler/Runtime:**
- [#78086](https://github.com/golang/go/issues/78086) `runtime`: `go runtime.GC()` can cause segfault with `-race` builds — `[CherryPickCandidate, compiler/runtime]`
- [#77921](https://github.com/golang/go/issues/77921) `cmd/compile`: ICE len larger than cap for `OSLICEHEADER` — `[CherryPickApproved, compiler/runtime]`
- [#77298](https://github.com/golang/go/issues/77298) `cmd/compile`: go1.22+ cmd with go.mod 1.21 generates per-loop variable when using line directive — `[CherryPickCandidate, compiler/runtime]`

**Go Command:**
- [#78057](https://github.com/golang/go/issues/78057) `cmd/go`: `DiskCache.Trim` on macOS often blocks go command for >20 minutes — `[GoCommand, CherryPickApproved]`

**Security:**
- [#77968](https://github.com/golang/go/issues/77968) `crypto/x509`: overly broad excluded constraints — `[CherryPickApproved, Backlog]`

---

## 🚀 下一版本 — Next Release

### Go1.27
> Milestone #408 | 324 open issues, 154 closed | Semantic: Minor version → 🚀 下一版本

**🚨 发布阻塞项 (Release Blockers)** — 13 issues

**Compiler Stability:**
- [#78134](https://github.com/golang/go/issues/78134) `cmd/compile`: ICE: bad live variable at entry — `[NeedsFix, release-blocker, compiler/runtime]`
- [#78081](https://github.com/golang/go/issues/78081) `cmd/compile`: unexplained compiler panic build flakes — `[NeedsFix, release-blocker, compiler/runtime]`

**Release Process / Lifecycle:**
- [#36905](https://github.com/golang/go/issues/36905) all: update standard-library dependencies at start/end of cycle — `[NeedsFix, release-blocker, recurring]`
- [#22487](https://github.com/golang/go/issues/22487) `lib/time`: update tzdata before release — `[NeedsFix, release-blocker, recurring]`
- [#60234](https://github.com/golang/go/issues/60234) `cmd/compile`: update compiler's PGO profile — `[Builders, NeedsFix, release-blocker, recurring]`
- [#40561](https://github.com/golang/go/issues/40561) `x/build/internal/releasetargets`: update for each upcoming major Go release — `[NeedsInvestigation, release-blocker, recurring]`

**Platform Support Changes:**
- [#75836](https://github.com/golang/go/issues/75836) all: end support for macOS 12 in Go 1.27 — `[OS-Darwin, Proposal-Accepted, early-in-cycle, release-blocker]`
- [#60792](https://github.com/golang/go/issues/60792) all: announce end of support for old Linux versions — `[Documentation, NeedsFix, release-blocker, recurring]`
- [#52188](https://github.com/golang/go/issues/52188) all: announce end of support for old Windows releases — `[OS-Windows, NeedsFix, release-blocker, recurring]`
- [#23011](https://github.com/golang/go/issues/23011) all: announce end of support for old macOS releases — `[OS-Darwin, NeedsFix, release-blocker, recurring]`

**API / Compatibility:**
- [#76472](https://github.com/golang/go/issues/76472) remove `gotypesalias`, `asynctimerchan` GODEBUG flag for 1.27 — `[Proposal-Accepted, release-blocker]`
- [#75316](https://github.com/golang/go/issues/75316) `crypto`: remove in Go 1.27 GODEBUGs introduced in Go 1.23 and earlier — `[Proposal-Accepted, release-blocker]`

**Performance:**
- [#75532](https://github.com/golang/go/issues/75532) `compress/gzip`: performance improvements impacting Kubernetes — `[Performance, NeedsInvestigation, release-blocker]`

---

**Compiler & Runtime (sample — 34+ issues total)**

*Early-in-cycle compiler work:*
- [#64208](https://github.com/golang/go/issues/64208) `cmd/compile`, importers: implement support for Alias type nodes in export data format — `[NeedsFix, early-in-cycle]`
- [#67347](https://github.com/golang/go/issues/67347) `cmd/compile/internal/types2`: enable unsorted processing of package objects — `[NeedsInvestigation, early-in-cycle]`
- [#67627](https://github.com/golang/go/issues/67627) `cmd/compile`: "panic: unification reached recursion depth limit" with recursive type constraint — `[NeedsInvestigation, early-in-cycle]`
- [#51244](https://github.com/golang/go/issues/51244) `go/types`, `cmd/compile`: "invalid type loop" depending on declaration order — `[NeedsFix, early-in-cycle]`
- [#77439](https://github.com/golang/go/issues/77439) `spec`, `cmd/compile`: type inference for generic function assigned to single-type type set should work — `[compiler/runtime, LanguageProposal]`
- [#77245](https://github.com/golang/go/issues/77245) `spec`: function type inference should work in all assignment contexts — `[Proposal-Accepted, TypeInference]`

*Performance & correctness:*
- [#77361](https://github.com/golang/go/issues/77361) `runtime`: selecting mark workers during start-the-world causes RSS regression in gopher-lua on large machines — `[Performance, NeedsInvestigation]`
- [#77332](https://github.com/golang/go/issues/77332) `cmd/go`: builds appear slower on openbsd/amd64 with Go 1.26rc2 — `[Performance, OS-OpenBSD]`
- [#77249](https://github.com/golang/go/issues/77249) `cmd/compile`: fatal error: all goroutines are asleep — deadlock! — `[NeedsInvestigation, compiler/runtime]`

---

**Go Command (18+ issues)**
- [#77346](https://github.com/golang/go/issues/77346) `cmd/go`: `go tool` and `go get -tool` could be documented better — `[Documentation, GoCommand]`
- [#77284](https://github.com/golang/go/issues/77284) `cmd/go`: support for older versions of git broken again — `[Security, NeedsFix, GoCommand]`
- [#77192](https://github.com/golang/go/issues/77192) `cmd/go`: `go doc`'s `-short` flag has no effect when given a symbol selector — `[GoCommand, FixPending]`
- [#77191](https://github.com/golang/go/issues/77191) `cmd/go`: `go doc`'s `-all` and `-short` flags don't work together — `[GoCommand]`
- [#54489](https://github.com/golang/go/issues/54489) `cmd/gofmt`: trailing newline in comments is removed since 1.19 — `[NeedsDecision, early-in-cycle]`

---

**Security / Crypto:**
- [#77377](https://github.com/golang/go/issues/77377) `crypto/tls`: disable session resumption when `VerifyPeerCertificate` is in use — `[Security, NeedsDecision]`
- [#77294](https://github.com/golang/go/issues/77294) `crypto/tls`: cap lifetime of authentication in TLS 1.3 — `[NeedsFix]`
- [#77359](https://github.com/golang/go/issues/77359) `crypto/tls`: don't recheck peer certificate validity on resumption if `InsecureSkipVerify` is set — `[NeedsFix]`

---

**Tools & Analysis (10+ issues)**
- [#77562](https://github.com/golang/go/issues/77562) `x/tools/go/analysis/passes/recursiveiter`: publish Analyzer and include it in `cmd/vet` — `[NeedsInvestigation, Analysis]`
- [#77564](https://github.com/golang/go/issues/77564) `cmd/fix`: `x/tools/go/analysis/passes/modernize`: `slicescontains` hoists needle expression — `[NeedsInvestigation, Tools]`
- [#77563](https://github.com/golang/go/issues/77563) `x/tools/go/analysis/passes/modernize`: `stringscutprefix` changes semantics for empty prefix — `[NeedsInvestigation, Tools]`
- [#77559](https://github.com/golang/go/issues/77559) `x/tools/go/analysis/passes/modernize`: `waitgroup` changes panic/recover semantics — `[NeedsInvestigation, Tools]`

> **Full scope**: 324 open issues across compiler/runtime (34%), go command (18%), tools (10%), platform support (4%), performance, documentation and more.

---

### gopls/v0.22.0
> Milestone #415 | 12 open issues, 26 closed | Semantic: Minor sub-project version → 🛠️ 工具生态 (tool/sub-project pattern)

**🚨 发布阻塞项 / Active Bugs:**
- [#78142](https://github.com/golang/go/issues/78142) `gopls`: OOB index in `extractFunctionMethod` — `[NeedsInvestigation, gopls/telemetry-wins, BugReport]`
- [#77814](https://github.com/golang/go/issues/77814) `gopls`: MCP exhausts file descriptors — `[BugReport]`
- [#77336](https://github.com/golang/go/issues/77336) `gopls/internal/cmd`: `TestMCPCommandLogging/trace.log` failures — `[NeedsInvestigation]`
- [#74258](https://github.com/golang/go/issues/74258) `gopls/internal/cmd`: `TestMCPCommandStdio` flake due to race condition when shutting down — `[NeedsInvestigation]`
- [#78110](https://github.com/golang/go/issues/78110) `x/tools/go/ssa`: next tuple and bound method closure omit explicit interface conversion instructions — `[NeedsInvestigation, BugReport]`
- [#75525](https://github.com/golang/go/issues/75525) `gopls`: Implementation OOB index panic in unify — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#76803](https://github.com/golang/go/issues/76803) `gopls/analysis/yield`: another false positive with a reified boolean — `[BugReport]`

**Feature Requests:**
- [#77802](https://github.com/golang/go/issues/77802) `gopls`: implementations: not working on dynamic function calls — `[NeedsInvestigation, Analysis]`
- [#77396](https://github.com/golang/go/issues/77396) proposal: `gopls`: pause gopls from command line and enable it back — `[Proposal, FeatureRequest]`
- [#76331](https://github.com/golang/go/issues/76331) `gopls`: experimental LSP dialog support
- [#75469](https://github.com/golang/go/issues/75469) `gopls`: Completion of generic argument resulting in invalid casting to constraints — `[gopls/completion]`
- [#74686](https://github.com/golang/go/issues/74686) `gopls`: symbolic link to `/` causes `ModuleResolver` to scan entire file system, burning CPU
- [#74292](https://github.com/golang/go/issues/74292) `gopls`: add file watcher for headless mode — `[FeatureRequest]`

---

## 🔵 远期规划 — Far Future

### Go1.28
> Milestone #423 | 4 open issues, 0 closed | Semantic: Far-future major → 🔵 远期规划

**🚨 发布阻塞项 (Bootstrap / Cycle Start):**
- [#77341](https://github.com/golang/go/issues/77341) `build`: adopt Go 1.26 as bootstrap toolchain for Go 1.28 — `[NeedsFix, early-in-cycle, release-blocker]`
- [#40705](https://github.com/golang/go/issues/40705) `internal/goversion`: increment Version at start of cycle — `[NeedsFix, early-in-cycle, release-blocker, recurring]`

**Other Early-Cycle:**
- [#73152](https://github.com/golang/go/issues/73152) `cmd/go`: confusing situation with `go run` and `//go:build ignore` — `[NeedsInvestigation, GoCommand, DevExp]`
- [#67799](https://github.com/golang/go/issues/67799) `cmd/go/internal/work`, `cmd/cgo`: duplicate `libobjc` library with 2+ cgo packages with Objective-C — `[OS-Darwin, NeedsInvestigation]`

> Note: Go 1.28 cycle has just started (only 4 issues). Real scope will grow significantly as Go 1.27 is released.

---

## 🛠️ 工具生态 — Tool Ecosystem

### gopls/v0.23.0
> Milestone #432 | 32 open issues, 1 closed | Semantic: Tool sub-project version → 🛠️ 工具生态

**Crash / Panic Bugs (Telemetry-tracked):**
- [#75236](https://github.com/golang/go/issues/75236) `gopls`: crash due to missing type in `inline.escape` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#75192](https://github.com/golang/go/issues/75192) `gopls`: Completion "unexpected surrounding" bug in `collectCompletions` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#74814](https://github.com/golang/go/issues/74814) `gopls`: `ApplyFix`: `createUndeclared` calls `ZeroExpr(types.Tuple)`, crashes — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#74653](https://github.com/golang/go/issues/74653) `x/tools/internal/refactor/inline`: `substituteTypeParams` panics in `reflect.Value.Set` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#74652](https://github.com/golang/go/issues/74652) `gopls`: `DidCreateFiles`: panic in `Files[i].URI.Clean()` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#74564](https://github.com/golang/go/issues/74564) `gopls`: SEGV in `types.Type.Underlying` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#73854](https://github.com/golang/go/issues/73854) `gopls`: nil panic in `types.Package.Path` while writing export data — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#73588](https://github.com/golang/go/issues/73588) `gopls`: "failed to find object for objectPath" bug in gcimporter — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#70553](https://github.com/golang/go/issues/70553) `gopls`: "slice bounds out of range" crash in `ExtractToNewFile` — `[NeedsInvestigation, gopls/telemetry-wins]`
- [#78083](https://github.com/golang/go/issues/78083) `gopls`: `packages.Load`: real error erased when "go list failed to return CompiledGoFiles" — `[BugReport]`
- [#74594](https://github.com/golang/go/issues/74594) `gopls/internal/test/integration`: `WriteGoSum` causes mysterious failures — `[NeedsInvestigation, BugReport]`

**Refactoring:**
- [#76205](https://github.com/golang/go/issues/76205) `gopls/analysis/unusedparams`: "no such param" error when applying fix — `[Refactoring]`
- [#75604](https://github.com/golang/go/issues/75604) `x/tools/internal/typesinternal`: `FileQualifier` needs to add imports, and reject unnameable types — `[NeedsFix, Refactoring]`
- [#70759](https://github.com/golang/go/issues/70759) `x/tools/internal/refactor/inline`: reduce call if neither binding decl nor callee body would create name conflicts — `[Refactoring]`
- [#70085](https://github.com/golang/go/issues/70085) `gopls`: add `refactor.inline.variable-all` code action — `[FeatureRequest, Refactoring]`
- [#66370](https://github.com/golang/go/issues/66370) `gopls`: support "inline all" and "inline away" — `[FeatureRequest, Refactoring]`
- [#57016](https://github.com/golang/go/issues/57016) `gopls`: support type move refactorings — `[FeatureRequest, Refactoring]`

**Features:**
- [#77960](https://github.com/golang/go/issues/77960) `gopls`: add a way to provide gopls settings for the built-in MCP server — `[FeatureRequest]`
- [#75447](https://github.com/golang/go/issues/75447) `gopls`: add conditional vulncheck IDE support
- [#74644](https://github.com/golang/go/issues/74644) `gopls`: Misguided missing method code action — `[ToolProposal]`
- [#74524](https://github.com/golang/go/issues/74524) `gopls`: `CodeAction(source.doc)`: mark up `DocLinks` to built-in types and methods
- [#74130](https://github.com/golang/go/issues/74130) `gopls`: Diagnostics: suppress diagnostics from dependencies (incl. std) — `[FeatureRequest]`
- [#70583](https://github.com/golang/go/issues/70583) `gopls`: feature: "move declaration" refactoring — `[FeatureRequest, Refactoring]`
- [#61677](https://github.com/golang/go/issues/61677) `gopls`: hover: doc link markup ignores import mapping of current file — `[FeatureRequest]`
- [#56572](https://github.com/golang/go/issues/56572) `gopls`: support global "go to implementation" queries on function types — `[FeatureRequest]`

**Analysis:**
- [#76648](https://github.com/golang/go/issues/76648) `x/tools/go/analysis/passes/modernize`: replace unsafe pointer arithmetic with `unsafe.Add(ptr, n)` — `[FeatureRequest]`
- [#75692](https://github.com/golang/go/issues/75692) `x/tools/go/analysis/passes/modernize`: `errorsastype`: modernize `errors.As` → `errors.AsType` — `[FeatureRequest, Analysis]`
- [#41436](https://github.com/golang/go/issues/41436) `x/tools/go/analysis`: a `Diagnostic` should indicate when it is a lint-style warning to be ignored in generated code — `[Thinking]`

**Documentation:**
- [#76343](https://github.com/golang/go/issues/76343) `gopls`: document Change Signature refactoring (rename on `func` token) — `[Documentation, Refactoring]`

**Test Infrastructure:**
- [#74595](https://github.com/golang/go/issues/74595) `gopls/internal/test/integration`: obviate `CleanModCache` by making `Snapshot.RunGoCommand` honor `GOMODCACHE` — `[FeatureRequest]`
- [#73933](https://github.com/golang/go/issues/73933) `gopls`: Extension is having trouble with one package in a big project — `[NeedsInvestigation]`

---

### vuln/v1.1.0
> Milestone #321 | 1 open issue, 1 closed | Semantic: Tool version → 🛠️ 工具生态

- [#59927](https://github.com/golang/go/issues/59927) `x/vuln`: update JSON output to show all locations of a vulnerable symbol — `[NeedsInvestigation, vulncheck or vulndb]`

---

### gorelease
> Milestone #178 | 8 open issues, 10 closed | Semantic: Tool project → 🛠️ 工具生态

**Feature Roadmap for `x/exp/cmd/gorelease`:**
- [#46371](https://github.com/golang/go/issues/46371) split release, diff functionality and prepare to merge into GOROOT — `[NeedsDecision, modules]`
- [#44945](https://github.com/golang/go/issues/44945) expose `analysis.Analyzer` — `[NeedsInvestigation, FeatureRequest]`
- [#39192](https://github.com/golang/go/issues/39192) fetch base version from directory with `-basedir` flag — `[NeedsInvestigation, FeatureRequest]`
- [#39191](https://github.com/golang/go/issues/39191) set allowed changes with `-compatibility` flag — `[NeedsInvestigation, FeatureRequest]`
- [#37566](https://github.com/golang/go/issues/37566) positional arguments should specify packages to compare — `[NeedsFix, FeatureRequest]`
- [#37561](https://github.com/golang/go/issues/37561) support `-json` and `-f` flags — `[NeedsFix, FeatureRequest]`
- [#37559](https://github.com/golang/go/issues/37559) report when packages can't be loaded without replace, exclude — `[NeedsFix, FeatureRequest]`
- [#37414](https://github.com/golang/go/issues/37414) add glossary-defined code next to each (in)compatible change — `[NeedsInvestigation, FeatureRequest]`

---

## 🌐 子项目 — Sub-Projects

### pkgsite/upcoming
> Milestone #429 | 3 open issues, 6 closed

- [#77393](https://github.com/golang/go/issues/77393) `x/playground`: examples in Gonum timeout downloading the module — `[NeedsFix, FeatureRequest]`
- [#76718](https://github.com/golang/go/issues/76718) `x/pkgsite`: implement HTTP/MCP API for pkg.go.dev
- [#74027](https://github.com/golang/go/issues/74027) `x/pkgsite`: support postgres task queues — `[NeedsInvestigation, FeatureRequest]`

### pkgsite/search
> Milestone #164 | 16 open issues, 24 closed | Search quality improvements backlog

Key themes:
- **Relevance**: Standard library package ranking ([#51107](https://github.com/golang/go/issues/51107)), v2 module prioritization ([#68711](https://github.com/golang/go/issues/68711))
- **Discoverability**: Support for `cmd/go` tools ([#36940](https://github.com/golang/go/issues/36940)), internal packages, partial match improvements
- **UX**: Sorting options ([#36952](https://github.com/golang/go/issues/36952)), more results per page ([#41245](https://github.com/golang/go/issues/41245)), accessibility ([#52248](https://github.com/golang/go/issues/52248))
- **Algorithm**: Better stopword handling ([#38766](https://github.com/golang/go/issues/38766)), similar name matching ([#37783](https://github.com/golang/go/issues/37783)), module rename scoring ([#37252](https://github.com/golang/go/issues/37252))

---

## ⚪ 未排期 — Unplanned / Backlog

> These milestones are large holding areas. Issue counts only.

| Milestone | Open Issues | Notes |
|---|---|---|
| Backlog | 2,578 | General Go backlog — all unscheduled work |
| Unplanned | 1,943 | Due 2099 (permanent unplanned) |
| Unreleased | 1,813 | Due 2099 (merged but not released) |
| Proposal | 991 | Open proposals under review |
| gopls/backlog | 364 | gopls unscheduled improvements |
| gopls/unplanned | 112 | gopls confirmed-unplanned items |
| pkgsite/unplanned | 92 | pkgsite non-prioritized work |
| vuln/unplanned | 72 | Vulnerability toolchain backlog |
| Gccgo | 70 | GCC frontend issues |
| pkgsite/backlog | 73 | pkgsite backlog |
| website/backlog | 30 | golang.org website work |
| gollvm | 38 | LLVM-based Go frontend |
| website/unplanned | 20 | Website non-prioritized |
| proxy.golang.org/backlog | 5 | Module proxy backlog |
| proxy.golang.org/unplanned | 3 | Module proxy unplanned |

---

## 📋 Issues Without Milestone (Recent, No Triage)

> 20 most recent open issues not yet assigned to a milestone (as of 2026-03-20)

- [#78241](https://github.com/golang/go/issues/78241) `cmd/link/internal/ld`: `TestRuntimeTypeAttrExternal` failures — `[NeedsInvestigation]`
- [#78238](https://github.com/golang/go/issues/78238) `cmd/link`: `peCreateExportFile` generates invalid `.def` file when output name has trailing dot — `[compiler/runtime, BugReport]`
- [#78236](https://github.com/golang/go/issues/78236) `syscall`: wrong constant used in `WaitStatus.Stopped()` & `WaitStatus.Continued()` comparisons — `[compiler/runtime, BugReport]`
- [#78222](https://github.com/golang/go/issues/78222) `regexp`: repeat count limit is lower than documented — `[Documentation, NeedsInvestigation, BugReport]`
- [#78217](https://github.com/golang/go/issues/78217) `debug/elf`: `NewFile` fails to parse ELF files with program header count overflow (`PN_XNUM`) — `[compiler/runtime, BugReport]`
- [#78213](https://github.com/golang/go/issues/78213) `net/http/internal/http2`: `TestTransportBlockingRequestWrite/headers` failures — `[NeedsInvestigation]`
- [#78209](https://github.com/golang/go/issues/78209) `net/http/internal/http2`: `TestTransportBlockingRequestWrite/body` failures — `[NeedsInvestigation]`
- [#78204](https://github.com/golang/go/issues/78204) `cmd/go`: `go test -cover` fails with "go tool covdata: fork/exec ... text file busy" — `[GoCommand, BugReport]`
- [#78202](https://github.com/golang/go/issues/78202) `net/http/internal/http2`: `TestTransportRetryHasLimit` failures — `[NeedsInvestigation]`
- [#78199](https://github.com/golang/go/issues/78199) `net/http`: `TestServerContentType/h1` failures — `[NeedsInvestigation]`
- [#78188](https://github.com/golang/go/issues/78188) `cmd/go`: `TestScript/vendor_complex` failures — `[NeedsInvestigation]`
- [#78187](https://github.com/golang/go/issues/78187) `net/http/internal/http2`: `TestTransportRetryAfterRefusedStream` failures — `[NeedsInvestigation]`
- [#78186](https://github.com/golang/go/issues/78186) `cmd/go`: `TestScript/test_match_no_tests_with_subtests` failures — `[NeedsInvestigation]`
- [#78180](https://github.com/golang/go/issues/78180) `cmd/link`: `TestExtLinkCmdlineDeterminism` failures — `[NeedsInvestigation, release-blocker, compiler/runtime]`
- [#78173](https://github.com/golang/go/issues/78173) `cmd/link`: invalid relocation in `SRODATAFIPS` — `[NeedsInvestigation, compiler/runtime]`
- [#78171](https://github.com/golang/go/issues/78171) `cmd/link`: `-buildmode=pie` binaries fail to run on s390x — `[arch-s390x, compiler/runtime, BugReport]`
- [#78161](https://github.com/golang/go/issues/78161) `testing`: memory corruption leading to panic — `[arch-riscv, BugReport]`
- [#78136](https://github.com/golang/go/issues/78136) `cmd/internal/testdir`: `Test/fixedbugs/issue75764.go` failures — `[NeedsInvestigation]`
- [#78130](https://github.com/golang/go/issues/78130) `net/http`: `TestDisableContentLength/h1` failures — `[NeedsInvestigation]`
- [#78129](https://github.com/golang/go/issues/78129) `crypto/rsa`: `TestEverything/350` failures — `[NeedsInvestigation]`

> Note: Issue [#78180](https://github.com/golang/go/issues/78180) (`cmd/link: TestExtLinkCmdlineDeterminism`) is labeled `release-blocker` despite having no milestone — should be triaged into Go1.27.

---

## Recently Closed Milestones

| Milestone | Closed | Issues (open/closed) |
|---|---|---|
| gopls/v0.21.1 | 2026-03-12 | 0/2 |
| vuln/2022 | 2023-04-07 | 0/35 |
| gopls/v0.9.3 | 2022-08-11 | 0/2 |
| gopls/v0.9.2 | 2022-08-11 | 0/39 |
| gopls/v0.9.1 | 2022-07-14 | 0/2 |

---

## Summary

| Milestone | Category | Status | Open Issues |
|---|---|---|---|
| Go1.25.9 | 🔧 当前补丁 | Active backport | 5 |
| Go1.26.2 | 🔧 当前补丁 | Active backport | 22 |
| Go1.27 | 🚀 下一版本 | In development | 324 |
| gopls/v0.22.0 | 🛠️ 工具生态 | Near release | 12 |
| gopls/v0.23.0 | 🛠️ 工具生态 | Future | 32 |
| Go1.28 | 🔵 远期规划 | Just started | 4 |
| vuln/v1.1.0 | 🛠️ 工具生态 | Stalled | 1 |
| gorelease | 🛠️ 工具生态 | Ongoing | 8 |
| pkgsite/upcoming | 🌐 子项目 | Active | 3 |
| pkgsite/search | 🌐 子项目 | Backlog | 16 |
| Backlog + Unplanned + Unreleased | ⚪ 未排期 | — | ~6,300+ |
| Proposal | ⚪ 未排期 | Under review | 991 |

**Total release-blockers tracked**: 13 in Go1.27, 2 in Go1.28 (cycle-start), ~22 open backport candidates in Go1.26.2
