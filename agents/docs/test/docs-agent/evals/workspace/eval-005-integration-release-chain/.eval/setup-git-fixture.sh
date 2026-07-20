#!/bin/sh
set -eu

fixture_root=$(pwd -P)
metadata_path="$fixture_root/eval_metadata.json"
runtime_evidence="$fixture_root/.eval/runtime-git-evidence.md"

if [ ! -f "$metadata_path" ] || ! grep -q 'eval-005-integration-release-chain' "$metadata_path"; then
  echo "run this script from the eval-005 runtime workspace root" >&2
  exit 1
fi

if [ -e "$fixture_root/.git" ]; then
  echo "runtime workspace already contains .git; apply execution_cleanup before rerunning" >&2
  exit 1
fi

fixture_tmp=$(mktemp -d "${TMPDIR:-/tmp}/docs-eval-005.XXXXXX")
pre_tag_transaction_ref=refs/heads/fixture-pre-tag-transaction
post_tag_transaction_ref=refs/heads/fixture-post-tag-transaction

cleanup() {
  status=$?
  trap - EXIT HUP INT TERM
  if git rev-parse --git-dir >/dev/null 2>&1; then
    git switch -q --detach "${target_commit:-HEAD}" 2>/dev/null || true
    git update-ref -d "$pre_tag_transaction_ref" 2>/dev/null || true
    git update-ref -d "$post_tag_transaction_ref" 2>/dev/null || true
  fi
  rm -rf "$fixture_tmp"
  exit "$status"
}
trap cleanup EXIT HUP INT TERM

require_committed_blob() {
  commit=$1
  path=$2
  expected_blob=$3
  mode=$(git ls-tree "$commit" -- "$path" | awk '{print $1}')
  type=$(git ls-tree "$commit" -- "$path" | awk '{print $2}')
  blob=$(git ls-tree "$commit" -- "$path" | awk '{print $3}')
  if [ "$mode" != 100644 ] || [ "$type" != blob ] || [ "$blob" != "$expected_blob" ]; then
    echo "invalid committed blob: $commit:$path" >&2
    exit 1
  fi
}

for path in \
  src/search/routes.ts \
  tests/search-api.test.ts \
  docs/site/api/ai-search.md \
  docs/site/standards/change-map.yaml \
  docs/site/release-notes/v1.4.0.md \
  docs/site/release-notes/index.md \
  docs/site/.meta/releases.json \
  package.json
do
  mkdir -p "$fixture_tmp/$(dirname "$path")"
  cp "$fixture_root/$path" "$fixture_tmp/$path"
done

rm -f \
  "$fixture_root/src/search/routes.ts" \
  "$fixture_root/tests/search-api.test.ts" \
  "$fixture_root/docs/site/api/ai-search.md" \
  "$fixture_root/docs/site/release-notes/v1.4.0.md"
cp "$fixture_root/.eval/git-base/docs/site/standards/change-map.yaml" "$fixture_root/docs/site/standards/change-map.yaml"
cp "$fixture_root/.eval/git-base/docs/site/release-notes/index.md" "$fixture_root/docs/site/release-notes/index.md"
cp "$fixture_root/.eval/git-base/docs/site/.meta/releases.json" "$fixture_root/docs/site/.meta/releases.json"
cp "$fixture_root/.eval/git-base/package.json" "$fixture_root/package.json"

git init -q -b fixture-build
git config user.name "Docs Eval Fixture"
git config user.email "docs-eval@example.invalid"
git add --all
GIT_AUTHOR_DATE='2026-07-20T01:00:00Z' GIT_COMMITTER_DATE='2026-07-20T01:00:00Z' \
  git commit -q -m 'fixture: v1.3.0 base'
base_commit=$(git rev-parse HEAD)
git branch fixture-base "$base_commit"

for path in \
  src/search/routes.ts \
  tests/search-api.test.ts \
  docs/site/api/ai-search.md \
  docs/site/standards/change-map.yaml \
  docs/site/release-notes/v1.4.0.md \
  docs/site/release-notes/index.md \
  docs/site/.meta/releases.json \
  package.json
do
  mkdir -p "$fixture_root/$(dirname "$path")"
  cp "$fixture_tmp/$path" "$fixture_root/$path"
done
git add --all
GIT_AUTHOR_DATE='2026-07-20T01:05:00Z' GIT_COMMITTER_DATE='2026-07-20T01:05:00Z' \
  git commit -q -m 'fixture: v1.4.0 release target'
target_commit=$(git rev-parse HEAD)
git branch fixture-target "$target_commit"
git switch -q -c fixture-pre-tag-transaction "$target_commit"

for path in \
  docs/site/api/ai-search.md \
  docs/site/release-notes/v1.4.0.md \
  docs/site/release-notes/index.md
do
  sed 's/last_verified_version: unverified/last_verified_version: v1.4.0/' "$path" > "$fixture_tmp/stamped.md"
  mv "$fixture_tmp/stamped.md" "$path"
done

route_blob=$(git rev-parse "$target_commit:src/search/routes.ts")
test_blob=$(git rev-parse "$target_commit:tests/search-api.test.ts")
api_target_blob=$(git rev-parse "$target_commit:docs/site/api/ai-search.md")
change_map_base_blob=$(git rev-parse "$base_commit:docs/site/standards/change-map.yaml")
change_map_target_blob=$(git rev-parse "$target_commit:docs/site/standards/change-map.yaml")
change_map_patch_sha=$(git diff --binary "$base_commit" "$target_commit" -- docs/site/standards/change-map.yaml | shasum -a 256 | awk '{print $1}')
base_target_raw=$(git diff --raw --no-abbrev --no-renames "$base_commit" "$target_commit" | tr '\n' ';')
base_target_name_status=$(git diff --name-status --no-renames "$base_commit" "$target_commit" | tr '\n' ';')
release_target_blob=$(git rev-parse "$target_commit:docs/site/release-notes/v1.4.0.md")
index_target_blob=$(git rev-parse "$target_commit:docs/site/release-notes/index.md")
metadata_target_blob=$(git rev-parse "$target_commit:docs/site/.meta/releases.json")
package_target_blob=$(git rev-parse "$target_commit:package.json")
release_target_sha=$(git show "$target_commit:docs/site/release-notes/v1.4.0.md" | shasum -a 256 | awk '{print $1}')
index_target_sha=$(git show "$target_commit:docs/site/release-notes/index.md" | shasum -a 256 | awk '{print $1}')
metadata_target_sha=$(git show "$target_commit:docs/site/.meta/releases.json" | shasum -a 256 | awk '{print $1}')
package_target_sha=$(git show "$target_commit:package.json" | shasum -a 256 | awk '{print $1}')
api_stamp_sha=$(shasum -a 256 docs/site/api/ai-search.md | awk '{print $1}')
release_stamp_sha=$(shasum -a 256 docs/site/release-notes/v1.4.0.md | awk '{print $1}')
index_stamp_sha=$(shasum -a 256 docs/site/release-notes/index.md | awk '{print $1}')
release_stamp_blob=$(git hash-object docs/site/release-notes/v1.4.0.md)
index_stamp_blob=$(git hash-object docs/site/release-notes/index.md)
api_stamp_blob=$(git hash-object docs/site/api/ai-search.md)
inventory_json='[{"extractor":"git-tag-name-v1","locator":"refs/tags/v1.4.0","locator_kind":"git-ref","required_raw_form":"vX.Y.Z","selector":"tag-name","source_id":"actual_tag"},{"extractor":"json-pointer-rfc6901-v1","locator":"package.json","locator_kind":"git-file","required_raw_form":"X.Y.Z","selector":"/version","source_id":"host_package"},{"extractor":"markdown-release-index-v1","locator":"docs/site/release-notes/index.md","locator_kind":"git-file","required_raw_form":"vX.Y.Z","selector":"entry[v1.4.0].version","source_id":"release_index"},{"extractor":"json-pointer-rfc6901-v1","locator":"docs/site/.meta/releases.json","locator_kind":"git-file","required_raw_form":"vX.Y.Z","selector":"/latest","source_id":"release_metadata"},{"extractor":"markdown-release-heading-v1","locator":"docs/site/release-notes/v1.4.0.md","locator_kind":"git-file","required_raw_form":"vX.Y.Z","selector":"heading[h1].release-version","source_id":"release_notes"},{"extractor":"handoff-field-v1","locator":"release-notes-handoff.md","locator_kind":"handoff","required_raw_form":"vX.Y.Z","selector":"target_release_version","source_id":"target_version"}]'
inventory_digest=$(printf '%s' "$inventory_json" | shasum -a 256 | awk '{print $1}')
require_committed_blob "$target_commit" src/search/routes.ts "$route_blob"
require_committed_blob "$target_commit" tests/search-api.test.ts "$test_blob"
require_committed_blob "$target_commit" docs/site/api/ai-search.md "$api_target_blob"
require_committed_blob "$target_commit" docs/site/standards/change-map.yaml "$change_map_target_blob"
require_committed_blob "$target_commit" docs/site/release-notes/v1.4.0.md "$release_target_blob"
require_committed_blob "$target_commit" docs/site/release-notes/index.md "$index_target_blob"
require_committed_blob "$target_commit" docs/site/.meta/releases.json "$metadata_target_blob"
require_committed_blob "$target_commit" package.json "$package_target_blob"
mkdir -p docs/site/.meta/audit/handoffs
sed \
  -e "s/{{BASE_COMMIT}}/$base_commit/g" \
  -e "s/{{TARGET_COMMIT}}/$target_commit/g" \
  -e "s/{{ROUTE_BLOB}}/$route_blob/g" \
  -e "s/{{TEST_BLOB}}/$test_blob/g" \
  -e "s/{{API_TARGET_BLOB}}/$api_target_blob/g" \
  -e "s/{{API_STAMP_BLOB}}/$api_stamp_blob/g" \
  -e "s/{{CHANGE_MAP_BASE_BLOB}}/$change_map_base_blob/g" \
  -e "s/{{CHANGE_MAP_TARGET_BLOB}}/$change_map_target_blob/g" \
  -e "s/{{CHANGE_MAP_PATCH_SHA256}}/$change_map_patch_sha/g" \
  -e "s|{{BASE_TARGET_RAW}}|$base_target_raw|g" \
  -e "s|{{BASE_TARGET_NAME_STATUS}}|$base_target_name_status|g" \
  -e "s/{{RELEASE_TARGET_BLOB}}/$release_target_blob/g" \
  -e "s/{{INDEX_TARGET_BLOB}}/$index_target_blob/g" \
  -e "s/{{RELEASE_STAMP_BLOB}}/$release_stamp_blob/g" \
  -e "s/{{INDEX_STAMP_BLOB}}/$index_stamp_blob/g" \
  -e "s/{{METADATA_TARGET_BLOB}}/$metadata_target_blob/g" \
  -e "s/{{PACKAGE_TARGET_BLOB}}/$package_target_blob/g" \
  -e "s/{{RELEASE_TARGET_SHA256}}/$release_target_sha/g" \
  -e "s/{{INDEX_TARGET_SHA256}}/$index_target_sha/g" \
  -e "s/{{METADATA_TARGET_SHA256}}/$metadata_target_sha/g" \
  -e "s/{{PACKAGE_TARGET_SHA256}}/$package_target_sha/g" \
  -e "s/{{API_STAMP_SHA256}}/$api_stamp_sha/g" \
  -e "s/{{RELEASE_STAMP_SHA256}}/$release_stamp_sha/g" \
  -e "s/{{INDEX_STAMP_SHA256}}/$index_stamp_sha/g" \
  -e "s|{{INVENTORY_JSON}}|$inventory_json|g" \
  -e "s/{{INVENTORY_DIGEST}}/$inventory_digest/g" \
  .eval/git-pretag/audit-v1.4.0.md.in > docs/site/.meta/audit/audit-v1.4.0.md
git add docs/site/api/ai-search.md docs/site/release-notes/v1.4.0.md docs/site/release-notes/index.md docs/site/.meta/audit/audit-v1.4.0.md
GIT_AUTHOR_DATE='2026-07-20T01:10:00Z' GIT_COMMITTER_DATE='2026-07-20T01:10:00Z' \
  git commit -q -m 'fixture: stamp and anchor v1.4.0 docs'
anchor_commit=$(git rev-parse HEAD)
anchor_tree=$(git rev-parse 'HEAD^{tree}')
candidate_blob=$(git rev-parse 'HEAD:docs/site/.meta/audit/audit-v1.4.0.md')
anchor_full_patch_sha=$(git diff --binary "$target_commit" "$anchor_commit" | shasum -a 256 | awk '{print $1}')
git branch fixture-pre-tag-anchor "$anchor_commit"
lineage_json=$(printf '[{"anchor_commit":"%s","anchor_tree":"%s","attempt":1,"previous_lineage_digest":"sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945","record_blob":"%s","record_path":"docs/site/.meta/audit/audit-v1.4.0.md"}]' "$anchor_commit" "$anchor_tree" "$candidate_blob")
lineage_digest=$(printf '%s' "$lineage_json" | shasum -a 256 | awk '{print $1}')

sed \
  -e "s/{{BASE_COMMIT}}/$base_commit/g" \
  -e "s/{{TARGET_COMMIT}}/$target_commit/g" \
  -e "s/{{ANCHOR_COMMIT}}/$anchor_commit/g" \
  -e "s/{{ANCHOR_TREE}}/$anchor_tree/g" \
  -e "s/{{CANDIDATE_BLOB}}/$candidate_blob/g" \
  -e "s|{{LINEAGE_JSON}}|$lineage_json|g" \
  -e "s/{{INVENTORY_DIGEST}}/$inventory_digest/g" \
  -e "s/{{LINEAGE_DIGEST}}/$lineage_digest/g" \
  .eval/git-pretag/pre-tag-v1.4.0.md.in > docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md
git add docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md
GIT_AUTHOR_DATE='2026-07-20T01:15:00Z' GIT_COMMITTER_DATE='2026-07-20T01:15:00Z' \
  git commit -q -m 'fixture: add v1.4.0 discovery handoff'
handoff_commit=$(git rev-parse HEAD)
handoff_tree=$(git rev-parse 'HEAD^{tree}')
handoff_blob=$(git rev-parse 'HEAD:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md')
git branch fixture-pre-tag-handoff "$handoff_commit"

if [ "$(git rev-parse "$anchor_commit^")" != "$target_commit" ] || [ "$(git rev-parse "$handoff_commit^")" != "$anchor_commit" ]; then
  echo "pre-tag transaction parent chain is invalid" >&2
  exit 1
fi
if [ "$(git cat-file -t "$candidate_blob")" != blob ] || [ "$(git cat-file -t "$handoff_blob")" != blob ]; then
  echo "pre-tag record object type is invalid" >&2
  exit 1
fi
if ! git show "$anchor_commit:docs/site/.meta/audit/audit-v1.4.0.md" | grep -Fq -- '- Candidate conclusion: `candidate_verified`.' ||
   ! git show "$handoff_commit:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md" | grep -Fq -- '- phase_result: `ready_for_tag`' ||
   ! git show "$handoff_commit:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md" | grep -Fq -- "- anchor_commit: \`$anchor_commit\`" ||
   ! git show "$handoff_commit:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md" | grep -Fq -- "- candidate_record_blob: \`$candidate_blob\`"; then
  echo "pre-tag committed record readback is invalid" >&2
  exit 1
fi
if [ "$(git rev-parse refs/heads/fixture-build)" != "$target_commit" ]; then
  echo "fixture release branch moved before pre-tag integration" >&2
  exit 1
fi
git update-ref refs/heads/fixture-build "$handoff_commit" "$target_commit"
if [ "$(git rev-parse refs/heads/fixture-build)" != "$handoff_commit" ]; then
  git update-ref refs/heads/fixture-build "$target_commit" "$handoff_commit" || true
  echo "pre-tag integration readback failed" >&2
  exit 1
fi

git branch release-evidence/v1.4.0 "$handoff_commit"
git tag v1.4.0 "$handoff_commit"
tag_object=$(git rev-parse refs/tags/v1.4.0)
tag_commit=$(git rev-parse 'refs/tags/v1.4.0^{}')
tag_tree=$(git rev-parse 'refs/tags/v1.4.0^{tree}')
evidence_head=$(git rev-parse refs/heads/release-evidence/v1.4.0)

git switch -q -c fixture-post-tag-transaction "$evidence_head"
sed \
  -e "s/{{TAG_OBJECT}}/$tag_object/g" \
  -e "s/{{TAG_COMMIT}}/$tag_commit/g" \
  -e "s/{{TAG_TREE}}/$tag_tree/g" \
  -e "s/{{HANDOFF_COMMIT}}/$handoff_commit/g" \
  -e "s/{{HANDOFF_TREE}}/$handoff_tree/g" \
  -e "s/{{HANDOFF_BLOB}}/$handoff_blob/g" \
  -e "s/{{CANDIDATE_BLOB}}/$candidate_blob/g" \
  -e "s/{{INVENTORY_DIGEST}}/$inventory_digest/g" \
  -e "s/{{LINEAGE_DIGEST}}/$lineage_digest/g" \
  -e "s/{{EVIDENCE_EXPECTED_HEAD}}/$evidence_head/g" \
  .eval/git-posttag/audit-v1.4.0-post-tag.md.in > docs/site/.meta/audit/audit-v1.4.0-post-tag.md
git add docs/site/.meta/audit/audit-v1.4.0-post-tag.md
GIT_AUTHOR_DATE='2026-07-20T01:20:00Z' GIT_COMMITTER_DATE='2026-07-20T01:20:00Z' \
  git commit -q -m 'fixture: persist v1.4.0 post-tag audit'
post_tag_commit=$(git rev-parse HEAD)
post_tag_tree=$(git rev-parse "$post_tag_commit^{tree}")
post_tag_blob=$(git rev-parse "$post_tag_commit:docs/site/.meta/audit/audit-v1.4.0-post-tag.md")
post_tag_parent=$(git rev-parse "$post_tag_commit^")

require_committed_blob "$tag_commit" docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md "$handoff_blob"
require_committed_blob "$tag_commit" docs/site/.meta/audit/audit-v1.4.0.md "$candidate_blob"
require_committed_blob "$tag_commit" docs/site/release-notes/v1.4.0.md "$release_stamp_blob"
require_committed_blob "$tag_commit" docs/site/release-notes/index.md "$index_stamp_blob"
require_committed_blob "$tag_commit" docs/site/.meta/releases.json "$metadata_target_blob"
require_committed_blob "$tag_commit" package.json "$package_target_blob"
if ! git show "$tag_commit:docs/site/release-notes/v1.4.0.md" | grep -Fq '# v1.4.0' ||
   ! git show "$tag_commit:docs/site/release-notes/index.md" | grep -Fq 'v1.4.0' ||
   ! git show "$tag_commit:docs/site/.meta/releases.json" | grep -Fq '"latest": "v1.4.0"' ||
   ! git show "$tag_commit:package.json" | grep -Fq '"version": "1.4.0"'; then
  echo "post-tag version source parsing failed" >&2
  exit 1
fi
if ! git diff --quiet "$handoff_commit" "$tag_commit" -- || [ "$tag_tree" != "$handoff_tree" ]; then
  echo "post-tag handoff and tag trees diverged" >&2
  exit 1
fi

pre_integration_tag_object=$(git rev-parse refs/tags/v1.4.0)
pre_integration_tag_commit=$(git rev-parse 'refs/tags/v1.4.0^{}')
pre_integration_tag_tree=$(git rev-parse 'refs/tags/v1.4.0^{tree}')
if [ "$pre_integration_tag_object" != "$tag_object" ] || [ "$pre_integration_tag_commit" != "$tag_commit" ] || [ "$pre_integration_tag_tree" != "$tag_tree" ]; then
  echo "synthetic tag tuple moved before post-tag integration" >&2
  exit 1
fi
if [ "$(git rev-parse refs/heads/release-evidence/v1.4.0)" != "$evidence_head" ]; then
  echo "release evidence branch moved before post-tag integration" >&2
  exit 1
fi
if [ "$post_tag_parent" != "$evidence_head" ] || [ "$(git cat-file -t "$post_tag_blob")" != blob ] ||
   ! git show "$post_tag_commit:docs/site/.meta/audit/audit-v1.4.0-post-tag.md" | grep -Fq -- '- phase_result: `release_verified`' ||
   ! git show "$post_tag_commit:docs/site/.meta/audit/audit-v1.4.0-post-tag.md" | grep -Fq -- "- release_evidence_expected_head: \`$evidence_head\`" ||
   ! git show "$post_tag_commit:docs/site/.meta/audit/audit-v1.4.0-post-tag.md" | grep -Fq -- '- command_evidence:'; then
  echo "post-tag transaction record readback is invalid" >&2
  exit 1
fi
git update-ref refs/heads/release-evidence/v1.4.0 "$post_tag_commit" "$evidence_head"
final_evidence_head=$(git rev-parse refs/heads/release-evidence/v1.4.0)
final_evidence_blob=$(git rev-parse "$final_evidence_head:docs/site/.meta/audit/audit-v1.4.0-post-tag.md")
if [ "$final_evidence_head" != "$post_tag_commit" ] || [ "$final_evidence_blob" != "$post_tag_blob" ]; then
  git update-ref refs/heads/release-evidence/v1.4.0 "$evidence_head" "$post_tag_commit" || true
  echo "post-tag integration readback failed" >&2
  exit 1
fi

git switch -q --detach "$target_commit"

printf '%s\n' \
  '# Runtime Git evidence' \
  '' \
  "- base_ref: \`refs/heads/fixture-base\`" \
  "- base_commit: \`$base_commit\`" \
  "- target_ref: \`refs/heads/fixture-target\`" \
  "- target_commit: \`$target_commit\`" \
  "- target_tree: \`$(git rev-parse "$target_commit^{tree}")\`" \
  "- anchor_ref: \`refs/heads/fixture-pre-tag-anchor\`" \
  "- anchor_commit: \`$anchor_commit\`" \
  "- anchor_tree: \`$anchor_tree\`" \
  "- candidate_blob: \`$candidate_blob\`" \
  "- target_to_anchor_full_patch_sha256: \`$anchor_full_patch_sha\`" \
  "- handoff_ref: \`refs/heads/fixture-pre-tag-handoff\`" \
  "- handoff_commit: \`$handoff_commit\`" \
  "- handoff_tree: \`$handoff_tree\`" \
  "- handoff_blob: \`$handoff_blob\`" \
  "- actual_tag_ref: \`refs/tags/v1.4.0\`" \
  "- tag_ref_target_object_id: \`$tag_object\`" \
  "- peeled_tag_commit: \`$tag_commit\`" \
  "- peeled_tag_tree: \`$tag_tree\`" \
  "- pre_integration_tag_ref_target_object_id: \`$pre_integration_tag_object\`" \
  "- pre_integration_peeled_tag_commit: \`$pre_integration_tag_commit\`" \
  "- pre_integration_peeled_tag_tree: \`$pre_integration_tag_tree\`" \
  "- release_evidence_branch_ref: \`refs/heads/release-evidence/v1.4.0\`" \
  "- release_evidence_expected_head: \`$evidence_head\`" \
  "- post_tag_result_commit: \`$post_tag_commit\`" \
  "- post_tag_result_parent: \`$post_tag_parent\`" \
  "- post_tag_result_tree: \`$post_tag_tree\`" \
  "- post_tag_result_blob: \`$post_tag_blob\`" \
  "- release_evidence_final_head: \`$final_evidence_head\`" \
  "- post_tag_fast_forward_and_readback: \`passed\`" \
  '' \
  'Every value above must be independently resolved from Git before it is accepted.' \
  > "$runtime_evidence"

if git diff --quiet "$base_commit" "$target_commit" --; then
  echo "fixture base and target unexpectedly have no diff" >&2
  exit 1
fi
if [ "$tag_tree" != "$handoff_tree" ] || [ "$evidence_head" != "$handoff_commit" ] || [ "$post_tag_parent" != "$evidence_head" ] || [ "$final_evidence_head" != "$post_tag_commit" ] || [ "$final_evidence_blob" != "$post_tag_blob" ]; then
  echo "fixture ref/tree invariant failed" >&2
  exit 1
fi

echo "$runtime_evidence"
