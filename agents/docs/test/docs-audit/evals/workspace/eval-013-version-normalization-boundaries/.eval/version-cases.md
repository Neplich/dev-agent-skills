# Release version-source observations

- maintainer_confirmation: `v1.2.0-rc.1+Build.7`
- pre_tag_declared_source_ids: `target`, `notes`, `index`, `releases`,
  `marketplace`, `package`
- post_tag_observed_source_ids: `target`, `tag`, `notes`, `index`, `releases`,
  `marketplace`, `package`

| source_id | locator_kind | immutable locator | exact selector | deterministic extractor | required raw form |
| --- | --- | --- | --- | --- | --- |
| target | handoff | docs-agent:release-notes-gen | `target_release_version` | `handoff-field-v1` | `vX.Y.Z` |
| tag | git-tag | `refs/tags/v1.2.0-rc.1+Build.7` | `tag-name` | `git-tag-name-v1` | `vX.Y.Z` |
| notes | git-file | `docs/site/release-notes/v1.2.0-rc.1+Build.7.md` | `frontmatter.version` | `yaml-frontmatter-v1` | `vX.Y.Z` |
| index | git-file | `docs/site/release-notes/index.md` | `entry[v1.2.0-rc.1+Build.7].version` | `markdown-release-index-v1` | `vX.Y.Z` |
| releases | git-file | `docs/site/.meta/releases.json` | `/releases/v1.2.0-rc.1+Build.7/version` | `json-pointer-rfc6901-v1` | `vX.Y.Z` |
| marketplace | git-file | `.claude-plugin/marketplace.json` | `/metadata/version` | `json-pointer-rfc6901-v1` | `X.Y.Z` |
| package | git-file | `package.json` | `/version` | `json-pointer-rfc6901-v1` | `X.Y.Z` |

## Observation set A

- prefixed sources: `v1.2.0-rc.1+Build.7`
- unprefixed sources: `1.2.0-rc.1+Build.7`
## Observation set B

- target: `V1.2.0-rc.1+Build.7`
- tag: `vv1.2.0-rc.1+Build.7`
- Release Notes page: `1.2.0-rc.1+Build.7` (missing required `v`)
- Release Notes index entry: missing
- releases.json release value: empty
- marketplace metadata.version: missing
- package.json version: `1.2-rc1` (loose/non-SemVer)
- comparison candidate 1: `v1.2.0-RC.1+build.7`
- comparison candidate 2: `v1.2.0-rc.1`
- index entries matching `v1.2.0-rc.1+Build.7`: `2`
- releases.json selector resolution count: `0`
- observed extractor identity: `json-auto-latest`
