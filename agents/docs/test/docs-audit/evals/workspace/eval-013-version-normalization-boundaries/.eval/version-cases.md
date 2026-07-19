# Required version-source boundary cases

Confirmed inventory (all fields enter the inventory digest):

- digest_algorithm: `canonical-json-rfc8259-sorted-v1`
- canonical rules: RFC 8259 UTF-8, keys sorted, entries sorted by source_id,
  compact JSON, no trailing newline, optional members omitted, SHA-256 lowercase
- inventory_digest: `sha256:e511aca5591ef721dbe1095876fe9b718e7434a83a48e14de1e0f845124cced6`
- pre-tag tag state: the `tag` locator contract is persisted as
  `pending_expected_absent`; post-tag reads the same locator and fills raw value

| source_id | locator_kind | immutable locator | exact selector | deterministic extractor | required raw form |
| --- | --- | --- | --- | --- | --- |
| target | handoff | issue-116-confirmation-42 | `target_release_version` | `handoff-field-v1` | `vX.Y.Z` |
| tag | git-tag | `refs/tags/v1.2.0-rc.1+Build.7` | `tag-name` | `git-tag-name-v1` | `vX.Y.Z` |
| notes | git-file | `docs/site/release-notes/v1.2.0-rc.1+Build.7.md` | `frontmatter.version` | `yaml-frontmatter-v1` | `vX.Y.Z` |
| index | git-file | `docs/site/release-notes/index.md` | `entry[v1.2.0-rc.1+Build.7].version` | `markdown-release-index-v1` | `vX.Y.Z` |
| releases | git-file | `docs/site/.meta/releases.json` | `/releases/v1.2.0-rc.1+Build.7/version` | `json-pointer-rfc6901-v1` | `vX.Y.Z` |
| marketplace | git-file | `.claude-plugin/marketplace.json` | `/metadata/version` | `json-pointer-rfc6901-v1` | `X.Y.Z` |
| package | git-file | `package.json` | `/version` | `json-pointer-rfc6901-v1` | `X.Y.Z` |

The index and releases.json contain several historical versions. Only the
declared unique selector is allowed. A missing selector, two matching index
entries, a JSON Pointer that returns multiple values, or an unknown extractor
identity is independently invalid; the audit must not scan and choose a
plausible version.

Valid identity case:

- prefixed sources: `v1.2.0-rc.1+Build.7`
- unprefixed sources: `1.2.0-rc.1+Build.7`
- expected normalized identity: `1.2.0-rc.1+Build.7`

Independent invalid cases (report every applicable blocker):

- target: `V1.2.0-rc.1+Build.7`
- tag: `vv1.2.0-rc.1+Build.7`
- Release Notes page: `1.2.0-rc.1+Build.7` (missing required `v`)
- Release Notes index entry: missing
- releases.json release value: empty
- marketplace metadata.version: missing
- package.json version: `1.2-rc1` (loose/non-SemVer)
- comparison candidate: `v1.2.0-RC.1+build.7` (case mismatch)
- comparison candidate: `v1.2.0-rc.1` (build component lost)
- index selector: ambiguous duplicate entries
- releases.json selector: absent JSON Pointer
- extractor: unknown `json-auto-latest`

Pre-tag must persist the exact complete inventory and its digest. Post-tag must
consume that inventory unchanged and read each file-backed value from the
peeled tag tree, never from current filesystem bytes.
