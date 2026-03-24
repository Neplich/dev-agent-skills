# 🗺️ Roadmap — golang/go

> The Go programming language
> Source: [github.com/golang/go](https://github.com/golang/go)
> Generated: 2026-03-20

---

## ⚪ 未排期 (Unscheduled)

All open milestones have no due dates assigned.

### Go1.27

`██████░░░░░░░░░░` 31% complete — 146 closed / 327 open

> Milestone has 473 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/408)

### Go1.28

`░░░░░░░░░░░░░░░░` 0% complete — 0 closed / 4 open

- [ ] [#77341 — build: adopt Go 1.26 as bootstrap toolchain for Go 1.28](https://github.com/golang/go/issues/77341)
- [ ] [#73152 — cmd/go: confusing situation with 'go run' and '//go:build ignore'](https://github.com/golang/go/issues/73152)
- [ ] [#67799 — cmd/go/internal/work, cmd/cgo: duplicate libobjc library with 2 or more cgo packages with Objective-C](https://github.com/golang/go/issues/67799)
- [ ] [#40705 — internal/goversion: increment Version at start of cycle](https://github.com/golang/go/issues/40705)

[View milestone →](https://github.com/golang/go/milestone/423)

### Go1.26.2

`░░░░░░░░░░░░░░░░` 0% complete — 0 closed / 25 open

- [ ] [#78198 — cmd/compile: panic on invalid generic append with type parameter spread [1.26 backport]](https://github.com/golang/go/issues/78198)
- [ ] [#78191 — cmd/fix: panics with "package path has no import prefix" [1.26 backport]](https://github.com/golang/go/issues/78191)
- [ ] [#78155 — testing: within a B.Loop loop, assigning function result to _ allows body to be optimized away (1.26 regression) [1.26 backport]](https://github.com/golang/go/issues/78155)
- [ ] [#78111 — net/url: url.Parse in 1.26 breaks mongodb connection string parsing with multiple hosts [1.26 backport]](https://github.com/golang/go/issues/78111)
- [ ] [#78087 — runtime: `go runtime.GC()` can cause segfault with `-race` builds [1.26 backport]](https://github.com/golang/go/issues/78087)
- [ ] [#78058 — cmd/go: DiskCache.Trim on macOS often blocks go command for >20 minutes [1.26 backport]](https://github.com/golang/go/issues/78058)
- [ ] [#78041 — runtime: Windows crash with Go 1.26.0, 1.26.1 [1.26 backport]](https://github.com/golang/go/issues/78041)
- [ ] [#78019 — net/http: race condition on windows when using os.File as request body [1.26 backport]](https://github.com/golang/go/issues/78019)
- [ ] [#77950 — net/http: package doc comment is missing [1.26 backport]](https://github.com/golang/go/issues/77950)
- [ ] [#77935 — runtime: on 32bits arches timespec (64) definition is wrong [1.26 backport]](https://github.com/golang/go/issues/77935)

[View milestone →](https://github.com/golang/go/milestone/430)

### Go1.25.9

`██████████░░░░░░░` 38% complete — 3 closed / 5 open

- [x] [#78154 — testing: within a B.Loop loop, assigning function result to _ allows body to be optimized away (1.26 regression) [1.25 backport]](https://github.com/golang/go/issues/78154)
- [x] [#78056 — cmd/internal/testdir: Test/fixedbugs/{issue42032,issue51733,issue40954}.go fail with "missing LC_UUID load command" on macOS 26 in Go 1.25 [1.25 backport]](https://github.com/golang/go/issues/78056)
- [x] [#77999 — cmd/cgo/internal/test: build error on macOS 26 in Go 1.25 [1.25 backport]](https://github.com/golang/go/issues/77999)
- [ ] [#78086 — runtime: `go runtime.GC()` can cause segfault with `-race` builds [1.25 backport]](https://github.com/golang/go/issues/78086)
- [ ] [#78057 — cmd/go: DiskCache.Trim on macOS often blocks go command for >20 minutes [1.25 backport]](https://github.com/golang/go/issues/78057)
- [ ] [#77968 — crypto/x509: overly broad excluded constraints [1.25 backport]](https://github.com/golang/go/issues/77968)
- [ ] [#77921 — cmd/compile: internal compiler error len larger than cap for OSLICEHEADER [1.25 backport]](https://github.com/golang/go/issues/77921)
- [ ] [#77298 — cmd/compile: go1.22+ cmd with go.mod 1.21 generates per-loop variable when using line directive [1.25 backport]](https://github.com/golang/go/issues/77298)

[View milestone →](https://github.com/golang/go/milestone/431)

### gopls/v0.23.0

`███░░░░░░░░░░░░░` 3% complete — 1 closed / 32 open

- [x] [#78158 — x/tools/gopls: staticcheck gopls checks complains about result of `new()` parameters, please tag a new release](https://github.com/golang/go/issues/78158)
- [ ] [#78142 — x/tools/gopls: OOB index in extractFunctionMethod](https://github.com/golang/go/issues/78142)
- [ ] [#78110 — x/tools/go/ssa: next tuple and bound method closure omit explicit interface conversion instructions](https://github.com/golang/go/issues/78110)
- [ ] [#77814 — x/tools/gopls: mcp exhausts file descriptors](https://github.com/golang/go/issues/77814)
- [ ] [#77802 — x/tools/gopls: implementations: not working on dynamic function calls](https://github.com/golang/go/issues/77802)
- [ ] [#77681 — x/tools/gopls/internal/analysis/yield: false positive switch statement due to SSA code](https://github.com/golang/go/issues/77681)
- [ ] [#77574 — x/tools/gopls: semantic token for package-level (global) variables](https://github.com/golang/go/issues/77574)
- [ ] [#77560 — x/tools/go/analysis/passes/modernize: 'waitgroup' analyzer conflicts with passes/waitgroup](https://github.com/golang/go/issues/77560)
- [ ] [#77396 — proposal: x/tools/gopls: pause gopls from command line and enable it back](https://github.com/golang/go/issues/77396)
- [ ] [#77381 — x/tools/gopls: Inline variable code action ignores operator precedence](https://github.com/golang/go/issues/77381)

[View milestone →](https://github.com/golang/go/milestone/432)

### gopls/v0.22.0

`████████████░░░░` 68% complete — 26 closed / 12 open

- [ ] [#78083 — x/tools/gopls: packages.Load: "go list failed to return CompiledGoFiles" error erases the real error](https://github.com/golang/go/issues/78083)
- [ ] [#77960 — x/tools/gopls: add a way to provide gopls settings for the built-in MCP server](https://github.com/golang/go/issues/77960)
- [ ] [#76648 — x/tools/go/analysis/passes/modernize: replace unsafe pointer arithmetic with unsafe.Add(ptr, n)](https://github.com/golang/go/issues/76648)
- [ ] [#76343 — x/tools/gopls: document Change Signature refactoring (rename on `func` token)](https://github.com/golang/go/issues/76343)
- [ ] [#76205 — x/tools/gopls/internal/analysis/unusedparams: "no such param" error when applying fix](https://github.com/golang/go/issues/76205)
- [ ] [#75692 — x/tools/go/analysis/passes/modernize: errorsastype: modernize errors.As -> errors.AsType](https://github.com/golang/go/issues/75692)
- [ ] [#75604 — x/tools/internal/typesinternal: FileQualifier needs to add imports, and reject unnameable types](https://github.com/golang/go/issues/75604)
- [ ] [#75525 — x/tools/gopls: Implementation: OOB index panic in unify](https://github.com/golang/go/issues/75525)
- [ ] [#75447 — x/tools/gopls: add conditional vulncheck IDE support](https://github.com/golang/go/issues/75447)
- [ ] [#75236 — x/tools/gopls: crash due to missing type in inline.escape](https://github.com/golang/go/issues/75236)

[View milestone →](https://github.com/golang/go/milestone/415)

### Gccgo

`████████████░░░░` 82% complete — 329 closed / 70 open

> Milestone has 399 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/23)

### gollvm

`████████░░░░░░░░` 52% complete — 41 closed / 38 open

- [ ] [#74866 — gollvm: build fails with llvm latest and release/16.x](https://github.com/golang/go/issues/74866)
- [ ] [#56484 — gollvm: invalid argument to -O flag: fast](https://github.com/golang/go/issues/56484)
- [ ] [#56483 — test/bench/go1: benchmark Mandelbrot200 is reduced to zero with gollvm](https://github.com/golang/go/issues/56483)
- [ ] [#56092 — gollvm: error: 'class llvm::PointerType' has no member named 'getElementType'](https://github.com/golang/go/issues/56092)
- [ ] [#54562 — gollvm: os_linux.go:360:14: error: reference to undefined name '_itimerspec'](https://github.com/golang/go/issues/54562)

[View milestone →](https://github.com/golang/go/milestone/100)

### Proposal

`████████████░░░░` 78% complete — 3606 closed / 990 open

> Milestone has 4596 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/30)

### Backlog

`███████░░░░░░░░░` 52% complete — 2755 closed / 2581 open

> Milestone has 5336 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/117)

### Unplanned

`██████░░░░░░░░░░` 60% complete — 2901 closed / 1944 open

> Milestone has 4845 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/6)

### Unreleased

`████████████████` 83% complete — 8782 closed / 1810 open

> Milestone has 10592 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/22)

### gopls/unplanned

`███████░░░░░░░░░` 49% complete — 108 closed / 112 open

> Milestone has 220 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/180)

### gopls/backlog

`███████░░░░░░░░░` 28% complete — 141 closed / 364 open

> Milestone has 505 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/192)

### pkgsite/unplanned

`████████████░░░░` 78% complete — 321 closed / 92 open

> Milestone has 413 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/167)

### pkgsite/backlog

`███████████░░░░░` 49% complete — 71 closed / 73 open

> Milestone has 144 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/263)

### pkgsite/search

`██████░░░░░░░░░░` 60% complete — 24 closed / 16 open

- [ ] [#68711 — x/pkgsite: searches for standard library packages should surface and prioritize v2 versions](https://github.com/golang/go/issues/68711)
- [ ] [#65781 — x/pkgsite: builtins with lowercase names not searchable](https://github.com/golang/go/issues/65781)
- [ ] [#52248 — x/pkgsite: No skip to content button on search page](https://github.com/golang/go/issues/52248)
- [ ] [#51775 — x/pkgsite: improve search ranking heuristics or add a way to search by package name](https://github.com/golang/go/issues/51775)
- [ ] [#51107 — x/pkgsite: show `cmd/go` as the top entry in search result for 'go'](https://github.com/golang/go/issues/51107)

[View milestone →](https://github.com/golang/go/milestone/164)

### pkgsite/upcoming

`██████████░░░░░░` 67% complete — 6 closed / 3 open

- [ ] [#77393 — x/playground: examples in Gonum timeout downloading the module](https://github.com/golang/go/issues/77393)
- [ ] [#76718 — x/pkgsite: implement HTTP/MCP API for pkg.go.dev](https://github.com/golang/go/issues/76718)
- [ ] [#74027 — x/pkgsite: support postgres task queues](https://github.com/golang/go/issues/74027)

[View milestone →](https://github.com/golang/go/milestone/429)

### vuln/unplanned

`████████████░░░░` 74% complete — 202 closed / 72 open

> Milestone has 274 issues total. Showing count summary only.

[View milestone →](https://github.com/golang/go/milestone/288)

### vuln/v1.1.0

`████████░░░░░░░░` 50% complete — 1 closed / 1 open

- [x] [#56956 — x/vuln: Test failures](https://github.com/golang/go/issues/56956)
- [ ] [#59927 — x/vuln: update JSON output to show all locations of a vulnerable symbol](https://github.com/golang/go/issues/59927)

[View milestone →](https://github.com/golang/go/milestone/321)

### gorelease

`██████████░░░░░░` 56% complete — 10 closed / 8 open

- [ ] [#46371 — x/exp/cmd/gorelease: split release, diff functionality and prepare to merge into GOROOT](https://github.com/golang/go/issues/46371)
- [ ] [#44945 — x/exp/cmd/gorelease: expose analysis.Analyzer](https://github.com/golang/go/issues/44945)
- [ ] [#39192 — x/exp/cmd/gorelease: fetch base version from directory with -basedir flag](https://github.com/golang/go/issues/39192)
- [ ] [#39191 — x/exp/cmd/gorelease: set allowed changes with -compatibility flag](https://github.com/golang/go/issues/39191)

[View milestone →](https://github.com/golang/go/milestone/178)

### website/unplanned

`█████████░░░░░░░` 57% complete — 26 closed / 20 open

[View milestone →](https://github.com/golang/go/milestone/249)

### website/backlog

`██████████░░░░░░` 67% complete — 62 closed / 30 open

[View milestone →](https://github.com/golang/go/milestone/269)

### proxy.golang.org/backlog

`███████████░░░░░` 58% complete — 7 closed / 5 open

[View milestone →](https://github.com/golang/go/milestone/264)

### proxy.golang.org/unplanned

`██████░░░░░░░░░░` 40% complete — 2 closed / 3 open

[View milestone →](https://github.com/golang/go/milestone/265)

### Go1.4-bootstrap

`████████████████` 100% complete — 7 closed / 0 open

[View milestone →](https://github.com/golang/go/milestone/28)

### pkgsite/license

`████████████████` 100% complete — 31 closed / 0 open

[View milestone →](https://github.com/golang/go/milestone/168)

---

## ✅ 已完成 (Completed) — Last 5

### gopls/v0.21.1

`████████████████` 100% complete — 2 closed / 0 open — Closed 2026-03-12

- [x] [#77520 — x/tools/gopls: release version v0.21.1](https://github.com/golang/go/issues/77520)
- [x] [#76872 — x/tools/gopls: find all References doesn't work if function name highlighted](https://github.com/golang/go/issues/76872)

[View milestone →](https://github.com/golang/go/milestone/427)

### Go1.26.1

`████████████████` 100% complete — 26 closed / 0 open — Closed 2026-03-06

- [x] [#77974 — security: fix CVE-2026-27138 [1.26 backport]](https://github.com/golang/go/issues/77974)
- [x] [#77973 — security: fix CVE-2026-27137 [1.26 backport]](https://github.com/golang/go/issues/77973)
- [x] [#77972 — security: fix CVE-2026-27142 [1.26 backport]](https://github.com/golang/go/issues/77972)
- [x] [#77970 — security: fix CVE-2026-25679 [1.26 backport]](https://github.com/golang/go/issues/77970)
- [x] [#77904 — x/tools/go/analysis/passes/modernize: stringsbuilder breaks code when GenDecl is a block declaration [1.26 backport]](https://github.com/golang/go/issues/77904)
- [x] [#77899 — cmd/fix, x/tools/go/analysis/passes/modernize: bad rangeint rewriting [1.26 backport]](https://github.com/golang/go/issues/77899)
- [x] [#77860 — cmd/go: change `go mod init` default go directive back to 1.N [1.26 backport]](https://github.com/golang/go/issues/77860)
- [x] [#77849 — cmd/fix,x/tools/go/analysis/passes/modernize: stringscut rewrite changes behavior [1.26 backport]](https://github.com/golang/go/issues/77849)
- [x] [#77834 — os: FileInfo can escape from a Root [1.26 backport]](https://github.com/golang/go/issues/77834)
- [x] [#77807 — cmd/fix,x/tools/go/analysis/passes/modernize: stringsbuilder ignores variables if they are used multiple times [1.26 backport]](https://github.com/golang/go/issues/77807)

[View milestone →](https://github.com/golang/go/milestone/424)

### Go1.25.8

`████████████████` 100% complete — 9 closed / 0 open — Closed 2026-03-06

- [x] [#77971 — security: fix CVE-2026-27142 [1.25 backport]](https://github.com/golang/go/issues/77971)
- [x] [#77969 — security: fix CVE-2026-25679 [1.25 backport]](https://github.com/golang/go/issues/77969)
- [x] [#77833 — os: FileInfo can escape from a Root [1.25 backport]](https://github.com/golang/go/issues/77833)
- [x] [#77535 — cmd/compile: internal compiler error: 'main.func1': not lowered: v15, Load STRUCT PTR SSA [1.25 backport]](https://github.com/golang/go/issues/77535)
- [x] [#77531 — net/smtp: expiry date of localhostCert for testing is too short [1.25 backport]](https://github.com/golang/go/issues/77531)
- [x] [#77438 — cmd/go: CGO compilation fails after upgrading from Go 1.25.5 to 1.25.6 due to --define-variable flag in pkg-config [1.25 backport]](https://github.com/golang/go/issues/77438)
- [x] [#77413 — runtime: netpollinit() incorrectly prints the error from `linux.Eventfd` [1.25 backport]](https://github.com/golang/go/issues/77413)
- [x] [#77406 — os: Go 1.25.x regression on RemoveAll for windows [1.25 backport]](https://github.com/golang/go/issues/77406)
- [x] [#77253 — cmd/compile: miscompile of global array initialization [1.25 backport]](https://github.com/golang/go/issues/77253)

[View milestone →](https://github.com/golang/go/milestone/426)

### Go1.24.14

`████████████████` 100% complete — 2 closed / 0 open — Closed 2026-02-11

- [x] [#77437 — cmd/go: CGO compilation fails after upgrading from Go 1.25.5 to 1.25.6 due to --define-variable flag in pkg-config [1.24 backport]](https://github.com/golang/go/issues/77437)
- [x] [#77412 — runtime: netpollinit() incorrectly prints the error from `linux.Eventfd` [1.24 backport]](https://github.com/golang/go/issues/77412)

[View milestone →](https://github.com/golang/go/milestone/425)

### Go1.25.7

`████████████████` 100% complete — 5 closed / 0 open — Closed 2026-02-04

- [x] [#77425 — crypto/tls: CL 737700 broke session resumption on macOS [1.25 backport]](https://github.com/golang/go/issues/77425)
- [x] [#77356 — crypto/tls: revert Config.Clone change and apply lightweight chain validation [1.25 backport]](https://github.com/golang/go/issues/77356)
- [x] [#77323 — crypto/x509: single-label excluded DNS name constraints incorrectly match all wildcard SANs [1.25 backport]](https://github.com/golang/go/issues/77323)
- [x] [#77129 — cmd/go: potential code smuggling using doc comments (CVE-2025-61732) [1.25 backport]](https://github.com/golang/go/issues/77129)
- [x] [#75844 — cmd/compile: OOM killed on linux/arm64 [1.25 backport]](https://github.com/golang/go/issues/75844)

[View milestone →](https://github.com/golang/go/milestone/422)

---

## 📋 Backlog (No Milestone)

| # | Title | Status |
|---|-------|--------|
| [#78222](https://github.com/golang/go/issues/78222) | regexp: repeat count limit is lower than documented | [ ] |
| [#78219](https://github.com/golang/go/issues/78219) | cmd/compile: test case "TestIssue77597" failed due to "unsupported VMA range" on loong64 | [ ] |
| [#78217](https://github.com/golang/go/issues/78217) | debug/elf: NewFile fails to parse ELF files with program header count overflow (PN_XNUM) | [ ] |
| [#78213](https://github.com/golang/go/issues/78213) | net/http/internal/http2: TestTransportBlockingRequestWrite/headers failures | [ ] |
| [#78209](https://github.com/golang/go/issues/78209) | net/http/internal/http2: TestTransportBlockingRequestWrite/body failures | [ ] |
| [#78204](https://github.com/golang/go/issues/78204) | cmd/go: go test -cover fails with "go tool covdata: fork/exec ... text file busy" | [ ] |
| [#78202](https://github.com/golang/go/issues/78202) | net/http/internal/http2: TestTransportRetryHasLimit failures | [ ] |
| [#78199](https://github.com/golang/go/issues/78199) | net/http: TestServerContentType/h1 failures | [ ] |
| [#78192](https://github.com/golang/go/issues/78192) | cmd/link: Mach-O object loader drops section alignment, breaks ADRP on ARM64 | [ ] |
| [#78188](https://github.com/golang/go/issues/78188) | cmd/go: TestScript/vendor_complex failures | [ ] |
| [#78187](https://github.com/golang/go/issues/78187) | net/http/internal/http2: TestTransportRetryAfterRefusedStream failures | [ ] |
| [#78186](https://github.com/golang/go/issues/78186) | cmd/go: TestScript/test_match_no_tests_with_subtests failures | [ ] |
| [#78180](https://github.com/golang/go/issues/78180) | cmd/link: TestExtLinkCmdlineDeterminism failures | [ ] |
| [#78173](https://github.com/golang/go/issues/78173) | cmd/link: invalid relocation in SRODATAFIPS | [ ] |
| [#78171](https://github.com/golang/go/issues/78171) | cmd/link: -buildmode=pie binaries fail to run on s390x | [ ] |
| [#78161](https://github.com/golang/go/issues/78161) | testing: memory corruption leading to panic | [ ] |
| [#78136](https://github.com/golang/go/issues/78136) | cmd/internal/testdir:5_10: Test/fixedbugs/issue75764.go failures | [ ] |
| [#78130](https://github.com/golang/go/issues/78130) | net/http: TestDisableContentLength/h1 failures | [ ] |
| [#78129](https://github.com/golang/go/issues/78129) | crypto/rsa: TestEverything/350 failures | [ ] |
| [#78123](https://github.com/golang/go/issues/78123) | cmd/cgo/internal/testsanitizers: TestMSAN/arena_fail failures | [ ] |

---

> **Note:** No Mermaid gantt chart is included because golang/go has zero milestones with due dates to visualize.
