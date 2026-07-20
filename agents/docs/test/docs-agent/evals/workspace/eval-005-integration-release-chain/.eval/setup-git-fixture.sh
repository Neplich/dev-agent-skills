#!/bin/sh
set -eu

fixture_root=$(pwd -P)
metadata_path="$fixture_root/eval_metadata.json"
runtime_evidence="$fixture_root/.eval/runtime-git-evidence.md"
target_release_version=v1.4.0
target_release_semver=${target_release_version#v}
candidate_record_path=docs/site/.meta/audit/audit-v1.4.0.md
discovery_record_path=docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md
post_tag_record_path=docs/site/.meta/audit/audit-v1.4.0-post-tag.md
blocked_post_tag_template=.eval/git-posttag/audit-v1.4.0-post-tag-blocked.md.in

if [ ! -f "$metadata_path" ] || ! grep -q 'eval-005-integration-release-chain' "$metadata_path"; then
  echo "run this script from the eval-005 runtime workspace root" >&2
  exit 1
fi

if [ -e "$fixture_root/.git" ]; then
  echo "runtime workspace already contains .git; apply execution_cleanup before rerunning" >&2
  exit 1
fi

fixture_tmp=$(mktemp -d "${TMPDIR:-/tmp}/docs-eval-005.XXXXXX")
pre_tag_worktree="$fixture_tmp/pre-tag-worktree"
post_tag_worktree="$fixture_tmp/post-tag-worktree"
pre_tag_transaction_ref=refs/heads/fixture-pre-tag-transaction
post_tag_transaction_ref=refs/heads/fixture-post-tag-transaction
pre_tag_integrated=0
post_tag_integrated=0
anchor_ref_created=0
handoff_ref_created=0
evidence_ref_created=0
synthetic_tag_created=0
post_tag_decision_evidence_ready=0
tab_character=$(printf '\t')

cleanup() {
  status=$?
  trap - EXIT HUP INT TERM
  cd "$fixture_root" 2>/dev/null || true
  if git -C "$fixture_root" rev-parse --git-dir >/dev/null 2>&1; then
    git -C "$fixture_root" worktree remove --force "$pre_tag_worktree" 2>/dev/null || true
    git -C "$fixture_root" worktree remove --force "$post_tag_worktree" 2>/dev/null || true
    git -C "$fixture_root" worktree prune 2>/dev/null || true
    if [ "$status" -ne 0 ]; then
      if [ "$post_tag_integrated" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/heads/release-evidence/v1.4.0 2>/dev/null || true)" = "${post_tag_commit:-}" ]; then
        git -C "$fixture_root" update-ref refs/heads/release-evidence/v1.4.0 "$evidence_head" "$post_tag_commit" 2>/dev/null || true
      fi
      if [ "$synthetic_tag_created" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/tags/v1.4.0 2>/dev/null || true)" = "${tag_object:-}" ]; then
        git -C "$fixture_root" update-ref -d refs/tags/v1.4.0 "$tag_object" 2>/dev/null || true
      fi
      if [ "$evidence_ref_created" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/heads/release-evidence/v1.4.0 2>/dev/null || true)" = "${evidence_head:-}" ]; then
        git -C "$fixture_root" update-ref -d refs/heads/release-evidence/v1.4.0 "$evidence_head" 2>/dev/null || true
      fi
      if [ "$pre_tag_integrated" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/heads/fixture-build 2>/dev/null || true)" = "${handoff_commit:-}" ]; then
        git -C "$fixture_root" update-ref refs/heads/fixture-build "$target_commit" "$handoff_commit" 2>/dev/null || true
      fi
      if [ "$handoff_ref_created" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/heads/fixture-pre-tag-handoff 2>/dev/null || true)" = "${handoff_commit:-}" ]; then
        git -C "$fixture_root" update-ref -d refs/heads/fixture-pre-tag-handoff "$handoff_commit" 2>/dev/null || true
      fi
      if [ "$anchor_ref_created" -eq 1 ] &&
         [ "$(git -C "$fixture_root" rev-parse refs/heads/fixture-pre-tag-anchor 2>/dev/null || true)" = "${anchor_commit:-}" ]; then
        git -C "$fixture_root" update-ref -d refs/heads/fixture-pre-tag-anchor "$anchor_commit" 2>/dev/null || true
      fi
      if [ -n "${target_commit:-}" ] &&
         { [ "$(git -C "$fixture_root" rev-parse HEAD 2>/dev/null || true)" != "$target_commit" ] ||
           [ "$(git -C "$fixture_root" status --porcelain=v2 2>/dev/null || true)" != "${host_status_before:-}" ] ||
           git -C "$fixture_root" show-ref --verify --quiet refs/heads/fixture-pre-tag-anchor ||
           git -C "$fixture_root" show-ref --verify --quiet refs/heads/fixture-pre-tag-handoff ||
           git -C "$fixture_root" show-ref --verify --quiet refs/heads/release-evidence/v1.4.0 ||
           git -C "$fixture_root" show-ref --verify --quiet refs/tags/v1.4.0; }; then
        echo "transactional cleanup verification failed" >&2
      fi
    fi
    git -C "$fixture_root" update-ref -d "$pre_tag_transaction_ref" 2>/dev/null || true
    git -C "$fixture_root" update-ref -d "$post_tag_transaction_ref" 2>/dev/null || true
  fi
  rm -rf "$fixture_tmp"
  exit "$status"
}
trap cleanup EXIT
trap 'exit 129' HUP
trap 'exit 130' INT
trap 'exit 143' TERM

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

require_record_line() {
  record=$1
  expected=$2
  if ! grep -Fqx -- "$expected" "$record"; then
    echo "record schema is missing: $expected" >&2
    exit 1
  fi
}

require_record_contains() {
  record=$1
  expected=$2
  if ! grep -Fq -- "$expected" "$record"; then
    echo "record evidence is missing: $expected" >&2
    exit 1
  fi
}

reject_unexpanded_placeholders() {
  record=$1
  if grep -Fq '{{' "$record"; then
    echo "record contains an unexpanded placeholder: $record" >&2
    exit 1
  fi
}

require_section_order() {
  record=$1
  evidence_marker=$2
  conclusion_marker=$3
  evidence_line=$(grep -nF -- "$evidence_marker" "$record" | head -1 | cut -d: -f1)
  conclusion_line=$(grep -nF -- "$conclusion_marker" "$record" | head -1 | cut -d: -f1)
  if [ -z "$evidence_line" ] || [ -z "$conclusion_line" ] || [ "$evidence_line" -ge "$conclusion_line" ]; then
    echo "record conclusion precedes decision evidence: $record" >&2
    exit 1
  fi
}

validate_blocked_post_tag_template() {
  record=$1
  require_section_order "$record" '## Decision evidence' '## Conclusion'
  require_record_line "$record" '- second_tag_tuple_validation: `failed`'
  require_record_line "$record" '- expected_head_validation: `failed`'
  require_record_line "$record" '- phase_result: `blocked`'
  require_record_line "$record" '- release_verified_emitted: `false`'
  if grep -Fqx -- '- phase_result: `release_verified`' "$record"; then
    echo "blocked post-tag sample contains a success conclusion" >&2
    exit 1
  fi
}

validate_candidate_schema() {
  record=$1
  reject_unexpanded_placeholders "$record"
  require_record_line "$record" '- schema_version: `1.0`'
  require_record_line "$record" '- attempt: `1`'
  require_record_line "$record" '- phase: `pre-tag`'
  require_record_line "$record" "- base_ref_commit: \`$base_commit\`"
  require_record_line "$record" "- target_ref_commit: \`$target_commit\`"
  require_record_line "$record" '- target_release_version: `v1.4.0` (maintainer-confirmed)'
  require_record_line "$record" "- source_binding_target_release_version: \`$source_target_release_version\`"
  require_record_line "$record" "- source_binding_anchor_sha: \`$source_anchor_sha\`"
  require_record_line "$record" "- source_binding_digest: \`sha256:$source_digest\`"
  require_record_line "$record" "- Candidate version-source binding: \`(target_release_version=$source_target_release_version, anchor_sha=$source_anchor_sha, digest=sha256:$source_digest)\`; discovery and post-tag consumers must reproduce this tuple exactly."
  require_record_line "$record" "- discovery_record_path: \`$discovery_record_path\`"
  require_record_line "$record" "- post_tag_record_path: \`$post_tag_record_path\`"
  require_record_line "$record" '- diff_semantics: two-dot endpoint diff'
  require_record_line "$record" '- Unified stamp set: `docs/site/api/ai-search.md`, `docs/site/release-notes/v1.4.0.md`, `docs/site/release-notes/index.md`.'
  require_record_line "$record" "- Canonical inventory algorithm: \`canonical-json-rfc8259-sorted-v1\`; exact canonical JSON: \`$inventory_json\`."
  require_record_line "$record" "- Canonical inventory digest: \`sha256:$inventory_digest\`."
  require_record_line "$record" '- Initial staged inventory: `M 100644/blob/'"$api_target_blob"' -> 100644/blob/'"$api_stamp_blob"' docs/site/api/ai-search.md`; `M 100644/blob/'"$release_target_blob"' -> 100644/blob/'"$release_stamp_blob"' docs/site/release-notes/v1.4.0.md`; `M 100644/blob/'"$index_target_blob"' -> 100644/blob/'"$index_stamp_blob"' docs/site/release-notes/index.md`; `A absent -> 100644/blob/self docs/site/.meta/audit/audit-v1.4.0.md` (self object supplied by anchor readback, not embedded recursively). Name-status is exactly `M,M,M,A`; summary contains only the candidate create; full binary patch decision `passed`; rename/copy disabled; no delete/type/mode-only/symlink/gitlink/path-swap/extra-path delta.'
  require_record_line "$record" '- Final staged inventory after atomic candidate replacement: the same exact four paths, statuses, modes, types and stamp blob ids; candidate self blob is confirmed by the committed anchor/readback rather than self-referenced in its own bytes; raw, name-status, summary and full binary patch decision again `passed` with zero unauthorized delta. `.eval/runtime-git-evidence.md` supplies the post-commit `target..anchor` full-patch digest for independent readback, not as a self-referential candidate field.'
  require_record_line "$record" '- Stamp read-back: all three pages equal `v1.4.0`.'
  require_record_line "$record" '- Blocking items: none.'
  require_record_line "$record" '- Candidate conclusion: `candidate_verified`.'
  if grep -Eq 'phase_result:.*ready_for_tag|Candidate conclusion:.*ready_for_tag' "$record"; then
    echo "candidate record claims final pre-tag success" >&2
    exit 1
  fi
}

validate_handoff_schema() {
  record=$1
  reject_unexpanded_placeholders "$record"
  for line in \
    '- schema_version: `1.0`' \
    '- attempt: `1`' \
    '- phase: `pre-tag`' \
    '- target_release_version: `v1.4.0`' \
    '- phase_result: `ready_for_tag`' \
    '- post_commit_confirmation: `passed`' \
    '- discovery_path_preimage: `absent`' \
    '- lineage_digest_algorithm: `canonical-json-rfc8259-sorted-v1`' \
    '- immediately_superseded_attempt: none'
  do
    require_record_line "$record" "$line"
  done
  require_record_line "$record" "- base_ref_commit: \`$base_commit\`"
  require_record_line "$record" "- target_ref_commit: \`$target_commit\`"
  require_record_line "$record" "- version_source_inventory_digest: \`sha256:$inventory_digest\`"
  require_record_line "$record" "- anchor_commit: \`$anchor_commit\`"
  require_record_line "$record" "- anchor_tree: \`$anchor_tree\`"
  require_record_line "$record" "- candidate_record_blob: \`$candidate_blob\`"
  require_record_line "$record" "- lineage_canonical_json: \`$lineage_json\`"
  require_record_line "$record" "- lineage_digest: \`sha256:$lineage_digest\`"
  require_record_line "$record" "- source_binding_target_release_version: \`$source_target_release_version\`"
  require_record_line "$record" "- source_binding_anchor_sha: \`$source_anchor_sha\`"
  require_record_line "$record" "- source_binding_digest: \`sha256:$source_digest\`"
  require_record_line "$record" "- candidate_source_binding: \`(target_release_version=$source_target_release_version, anchor_sha=$source_anchor_sha, digest=sha256:$source_digest)\`"
  require_record_line "$record" "- current_entry: \`$discovery_current_entry\`"
  require_record_line "$record" "- post_tag_record_path: \`$post_tag_record_path\`"
}

validate_post_tag_schema() {
  record=$1
  reject_unexpanded_placeholders "$record"
  require_section_order "$record" '## Decision evidence' '## Conclusion'
  for line in \
    '- schema_version: `1.0`' \
    '- attempt: `1`' \
    '- phase: `post-tag`' \
    '- target_release_version: `v1.4.0`' \
    '- phase_result: `release_verified`' \
    '- second_tag_tuple_validation: `passed`' \
    '- expected_head_validation: `passed`' \
    '- locator_mode: `handoff`' \
    '- inventory_recomputed_from_tag_candidate: `passed`' \
    '- lineage_recomputed_from_tag_handoff: `passed`' \
    '- tag_tree_equals_handoff_tree: `true`' \
    '- candidate_schema_check: `passed`' \
    '- candidate_blob_readback: `passed`' \
    '- stamped_page_blob_and_sha256_checks: `passed`' \
    '- strict_source_selector_and_raw_form_checks: `passed`' \
    '- expected_head_check_before_commit: `passed`' \
    '- staged_convergence: raw/name-status/summary/full-binary single-path gate `passed`' \
    '- committed_convergence: expected-head-to-result raw/name-status/summary/full-binary single-path gate and result blob readback `passed`' \
    '- decision_checks_completed_before_record: `passed`' \
    '- blockers: `[]`' \
    '- tag_mutations: `0`' \
    '- remote_writes: `0`' \
    '- github_release_writes: `0`'
  do
    require_record_line "$record" "$line"
  done
  require_record_line "$record" "- tag_ref_target_object_id: \`$tag_object\`"
  require_record_line "$record" "- peeled_tag_commit: \`$tag_commit\`"
  require_record_line "$record" "- peeled_tag_tree: \`$tag_tree\`"
  require_record_line "$record" "- handoff_commit: \`$handoff_commit\`"
  require_record_line "$record" "- handoff_tree: \`$handoff_tree\`"
  require_record_line "$record" "- handoff_blob: \`$handoff_blob\`"
  require_record_line "$record" "- candidate_record_blob: \`$candidate_blob\`"
  require_record_line "$record" "- version_source_inventory_digest: \`sha256:$inventory_digest\`"
  require_record_line "$record" "- lineage_digest: \`sha256:$lineage_digest\`"
  require_record_line "$record" "- source_binding_target_release_version: \`$source_target_release_version\`"
  require_record_line "$record" "- source_binding_anchor_sha: \`$source_anchor_sha\`"
  require_record_line "$record" "- source_binding_digest: \`sha256:$source_digest\`"
  require_record_line "$record" "- pre_integration_tag_ref_target_object_id: \`$pre_integration_tag_object\`"
  require_record_line "$record" "- pre_integration_peeled_tag_commit: \`$pre_integration_tag_commit\`"
  require_record_line "$record" "- pre_integration_peeled_tag_tree: \`$pre_integration_tag_tree\`"
  require_record_line "$record" "- release_evidence_expected_head: \`$evidence_head\`"
  require_record_line "$record" "- release_evidence_observed_head_before_record: \`$evidence_observed_head_before_record\`"
  require_record_line "$record" "- candidate_anchor_commit: \`$anchor_commit\`"
  require_record_line "$record" "- discovery_anchor_commit: \`$handoff_commit\`"
  require_record_line "$record" "- isolated_commit_parent: \`$evidence_head\`"
  require_record_line "$record" '- command_evidence:'
}

collect_post_tag_decision_evidence() {
  pre_integration_tag_object=$(git rev-parse refs/tags/v1.4.0)
  pre_integration_tag_commit=$(git rev-parse 'refs/tags/v1.4.0^{}')
  pre_integration_tag_tree=$(git rev-parse 'refs/tags/v1.4.0^{tree}')
  evidence_observed_head_before_record=$(git rev-parse refs/heads/release-evidence/v1.4.0)

  if [ "$pre_integration_tag_object" != "$tag_object" ] ||
     [ "$pre_integration_tag_commit" != "$tag_commit" ] ||
     [ "$pre_integration_tag_tree" != "$tag_tree" ]; then
    echo "synthetic tag tuple moved before post-tag record rendering" >&2
    exit 1
  fi
  if [ "$evidence_observed_head_before_record" != "$evidence_head" ]; then
    echo "release evidence branch moved before post-tag record rendering" >&2
    exit 1
  fi
  post_tag_decision_evidence_ready=1
}

render_verified_post_tag_record() {
  output=$1
  if [ "$post_tag_decision_evidence_ready" -ne 1 ]; then
    echo "post-tag success record requested before decision evidence passed" >&2
    exit 1
  fi
  sed \
    -e "s/{{TARGET_RELEASE_VERSION}}/$source_target_release_version/g" \
    -e "s/{{SOURCE_ANCHOR_SHA}}/$source_anchor_sha/g" \
    -e "s/{{SOURCE_DIGEST}}/$source_digest/g" \
    -e "s/{{TAG_OBJECT}}/$tag_object/g" \
    -e "s/{{TAG_COMMIT}}/$tag_commit/g" \
    -e "s/{{TAG_TREE}}/$tag_tree/g" \
    -e "s/{{PRE_INTEGRATION_TAG_OBJECT}}/$pre_integration_tag_object/g" \
    -e "s/{{PRE_INTEGRATION_TAG_COMMIT}}/$pre_integration_tag_commit/g" \
    -e "s/{{PRE_INTEGRATION_TAG_TREE}}/$pre_integration_tag_tree/g" \
    -e "s/{{HANDOFF_COMMIT}}/$handoff_commit/g" \
    -e "s/{{HANDOFF_TREE}}/$handoff_tree/g" \
    -e "s/{{HANDOFF_BLOB}}/$handoff_blob/g" \
    -e "s/{{CANDIDATE_BLOB}}/$candidate_blob/g" \
    -e "s/{{ANCHOR_COMMIT}}/$anchor_commit/g" \
    -e "s/{{INVENTORY_DIGEST}}/$inventory_digest/g" \
    -e "s/{{LINEAGE_DIGEST}}/$lineage_digest/g" \
    -e "s/{{EVIDENCE_EXPECTED_HEAD}}/$evidence_head/g" \
    -e "s/{{EVIDENCE_OBSERVED_HEAD}}/$evidence_observed_head_before_record/g" \
    .eval/git-posttag/audit-v1.4.0-post-tag.md.in > "$output"
  validate_post_tag_schema "$output"
}

validate_blocked_post_tag_template "$blocked_post_tag_template"

validate_added_record_delta() {
  delta_kind=$1
  delta_base=$2
  delta_end=$3
  record_path=$4
  record_validator=$5
  record_name=$(basename "$record_path")
  raw_delta="$fixture_tmp/$record_name.raw"
  status_delta="$fixture_tmp/$record_name.status"
  summary_delta="$fixture_tmp/$record_name.summary"
  binary_delta="$fixture_tmp/$record_name.binary"
  record_copy="$fixture_tmp/$record_name.readback"

  if [ "$delta_kind" = staged ]; then
    git diff --cached --raw --no-abbrev --no-renames > "$raw_delta"
    git diff --cached --name-status --no-renames > "$status_delta"
    git diff --cached --summary --no-renames > "$summary_delta"
    git diff --cached --binary --no-renames > "$binary_delta"
    git show ":$record_path" > "$record_copy"
    record_mode=$(git ls-files -s "$record_path" | awk '{print $1}')
  else
    git diff --raw --no-abbrev --no-renames "$delta_base" "$delta_end" > "$raw_delta"
    git diff --name-status --no-renames "$delta_base" "$delta_end" > "$status_delta"
    git diff --summary --no-renames "$delta_base" "$delta_end" > "$summary_delta"
    git diff --binary --no-renames "$delta_base" "$delta_end" > "$binary_delta"
    git show "$delta_end:$record_path" > "$record_copy"
    record_mode=$(git ls-tree "$delta_end" -- "$record_path" | awk '{print $1}')
  fi

  if [ "$(cat "$status_delta")" != "A${tab_character}$record_path" ] ||
     ! grep -Eq "^:000000 100644 0{40} [0-9a-f]{40} A[[:space:]]+$record_path$" "$raw_delta" ||
     [ "$(wc -l < "$raw_delta" | tr -d ' ')" != 1 ] ||
     [ "$(sed -e 's/^[[:space:]]*//' "$summary_delta")" != "create mode 100644 $record_path" ] ||
     [ "$record_mode" != 100644 ] || [ ! -s "$binary_delta" ]; then
    echo "record delta is invalid: $record_path" >&2
    exit 1
  fi
  "$record_validator" "$record_copy"
}

validate_candidate_delta() {
  delta_kind=$1
  delta_end=${2:-}
  candidate_path=docs/site/.meta/audit/audit-v1.4.0.md
  expected_paths="$fixture_tmp/expected-candidate-paths"
  actual_paths="$fixture_tmp/actual-candidate-paths"
  expected_status="$fixture_tmp/expected-candidate-status"
  actual_status="$fixture_tmp/actual-candidate-status"
  raw_delta="$fixture_tmp/candidate-raw"
  summary_delta="$fixture_tmp/candidate-summary"
  binary_delta="$fixture_tmp/candidate-binary"

  printf '%s\n' \
    docs/site/.meta/audit/audit-v1.4.0.md \
    docs/site/api/ai-search.md \
    docs/site/release-notes/index.md \
    docs/site/release-notes/v1.4.0.md \
    | LC_ALL=C sort > "$expected_paths"
  printf '%s\n' \
    'A docs/site/.meta/audit/audit-v1.4.0.md' \
    'M docs/site/api/ai-search.md' \
    'M docs/site/release-notes/index.md' \
    'M docs/site/release-notes/v1.4.0.md' \
    | LC_ALL=C sort > "$expected_status"

  if [ "$delta_kind" = staged ]; then
    git diff --cached --name-only --no-renames | LC_ALL=C sort > "$actual_paths"
    git diff --cached --name-status --no-renames | awk '{print $1 " " $2}' | LC_ALL=C sort > "$actual_status"
    git diff --cached --raw --no-abbrev --no-renames > "$raw_delta"
    git diff --cached --summary --no-renames > "$summary_delta"
    git diff --cached --binary --no-renames > "$binary_delta"
    show_candidate=':'
  else
    git diff --name-only --no-renames "$target_commit" "$delta_end" | LC_ALL=C sort > "$actual_paths"
    git diff --name-status --no-renames "$target_commit" "$delta_end" | awk '{print $1 " " $2}' | LC_ALL=C sort > "$actual_status"
    git diff --raw --no-abbrev --no-renames "$target_commit" "$delta_end" > "$raw_delta"
    git diff --summary --no-renames "$target_commit" "$delta_end" > "$summary_delta"
    git diff --binary --no-renames "$target_commit" "$delta_end" > "$binary_delta"
    show_candidate="$delta_end:"
  fi

  if ! cmp -s "$expected_paths" "$actual_paths" || ! cmp -s "$expected_status" "$actual_status"; then
    echo "candidate delta contains unexpected paths or statuses" >&2
    exit 1
  fi
  if [ "$(wc -l < "$raw_delta" | tr -d ' ')" != 4 ] ||
     ! grep -Eq '^:000000 100644 0{40} [0-9a-f]{40} A[[:space:]]+docs/site/\.meta/audit/audit-v1\.4\.0\.md$' "$raw_delta" ||
     [ "$(grep -Ec '^:100644 100644 [0-9a-f]{40} [0-9a-f]{40} M[[:space:]]+docs/site/(api/ai-search\.md|release-notes/index\.md|release-notes/v1\.4\.0\.md)$' "$raw_delta")" != 3 ]; then
    echo "candidate raw metadata is invalid" >&2
    exit 1
  fi
  if [ "$(sed -e 's/^[[:space:]]*//' "$summary_delta")" != "create mode 100644 $candidate_path" ] || [ ! -s "$binary_delta" ]; then
    echo "candidate summary or binary patch is invalid" >&2
    exit 1
  fi

  for path in \
    docs/site/api/ai-search.md \
    docs/site/release-notes/v1.4.0.md \
    docs/site/release-notes/index.md
  do
    preimage="$fixture_tmp/preimage-$(basename "$path")"
    expected="$fixture_tmp/expected-$(basename "$path")"
    actual="$fixture_tmp/actual-$(basename "$path")"
    git show "$target_commit:$path" > "$preimage"
    if [ "$(grep -c '^last_verified_version: unverified$' "$preimage")" != 1 ]; then
      echo "candidate stamp preimage is invalid: $path" >&2
      exit 1
    fi
    sed 's/^last_verified_version: unverified$/last_verified_version: v1.4.0/' "$preimage" > "$expected"
    git show "$show_candidate$path" > "$actual"
    if [ "$(grep -c '^last_verified_version: v1.4.0$' "$actual")" != 1 ] || ! cmp -s "$expected" "$actual"; then
      echo "candidate stamp changed unauthorized content: $path" >&2
      exit 1
    fi
  done

  candidate_readback="$fixture_tmp/candidate-record-readback"
  git show "$show_candidate$candidate_path" > "$candidate_readback"
  if [ "$delta_kind" = staged ]; then
    candidate_mode=$(git ls-files -s "$candidate_path" | awk '{print $1}')
  else
    candidate_mode=$(git ls-tree "$delta_end" -- "$candidate_path" | awk '{print $1}')
  fi
  if [ "$candidate_mode" != 100644 ]; then
    echo "candidate record schema or mode is invalid" >&2
    exit 1
  fi
  validate_candidate_schema "$candidate_readback"
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

git init -q -b fixture-caller
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
git branch fixture-build "$target_commit"
host_head_before=$(git rev-parse HEAD)
host_status_before=$(git status --porcelain=v2)
git worktree add -q -b fixture-pre-tag-transaction "$pre_tag_worktree" "$target_commit"
cd "$pre_tag_worktree"

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
source_target_release_version=$target_release_version
source_anchor_sha=$target_commit
source_digest=$inventory_digest
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
  -e "s/{{TARGET_RELEASE_VERSION}}/$source_target_release_version/g" \
  -e "s/{{SOURCE_ANCHOR_SHA}}/$source_anchor_sha/g" \
  -e "s/{{SOURCE_DIGEST}}/$source_digest/g" \
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
  .eval/git-pretag/audit-v1.4.0.md.in > "$fixture_tmp/audit-v1.4.0.md"
mv "$fixture_tmp/audit-v1.4.0.md" docs/site/.meta/audit/audit-v1.4.0.md
git add docs/site/api/ai-search.md docs/site/release-notes/v1.4.0.md docs/site/release-notes/index.md docs/site/.meta/audit/audit-v1.4.0.md
validate_candidate_delta staged
cp docs/site/.meta/audit/audit-v1.4.0.md "$fixture_tmp/final-audit-v1.4.0.md"
mv "$fixture_tmp/final-audit-v1.4.0.md" docs/site/.meta/audit/audit-v1.4.0.md
git add docs/site/.meta/audit/audit-v1.4.0.md
validate_candidate_delta staged
GIT_AUTHOR_DATE='2026-07-20T01:10:00Z' GIT_COMMITTER_DATE='2026-07-20T01:10:00Z' \
  git commit -q -m 'fixture: stamp and anchor v1.4.0 docs'
anchor_commit=$(git rev-parse HEAD)
validate_candidate_delta committed "$anchor_commit"
anchor_tree=$(git rev-parse 'HEAD^{tree}')
candidate_blob=$(git rev-parse 'HEAD:docs/site/.meta/audit/audit-v1.4.0.md')
anchor_full_patch_sha=$(git diff --binary "$target_commit" "$anchor_commit" | shasum -a 256 | awk '{print $1}')
git branch fixture-pre-tag-anchor "$anchor_commit"
anchor_ref_created=1
lineage_json=$(printf '[{"anchor_commit":"%s","anchor_tree":"%s","attempt":1,"previous_lineage_digest":"sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945","record_blob":"%s","record_path":"%s","source_anchor_sha":"%s","source_digest":"sha256:%s","target_release_version":"%s"}]' "$anchor_commit" "$anchor_tree" "$candidate_blob" "$candidate_record_path" "$source_anchor_sha" "$source_digest" "$source_target_release_version")
lineage_digest=$(printf '%s' "$lineage_json" | shasum -a 256 | awk '{print $1}')
discovery_current_entry=$(printf '(attempt=1, target_release_version=%s, source_anchor_sha=%s, source_digest=sha256:%s, anchor_commit=%s, anchor_tree=%s, record_path=%s, record_blob=%s, previous_lineage_digest=sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945)' "$source_target_release_version" "$source_anchor_sha" "$source_digest" "$anchor_commit" "$anchor_tree" "$candidate_record_path" "$candidate_blob")

sed \
  -e "s/{{TARGET_RELEASE_VERSION}}/$source_target_release_version/g" \
  -e "s/{{SOURCE_ANCHOR_SHA}}/$source_anchor_sha/g" \
  -e "s/{{SOURCE_DIGEST}}/$source_digest/g" \
  -e "s/{{BASE_COMMIT}}/$base_commit/g" \
  -e "s/{{TARGET_COMMIT}}/$target_commit/g" \
  -e "s/{{ANCHOR_COMMIT}}/$anchor_commit/g" \
  -e "s/{{ANCHOR_TREE}}/$anchor_tree/g" \
  -e "s/{{CANDIDATE_BLOB}}/$candidate_blob/g" \
  -e "s|{{LINEAGE_JSON}}|$lineage_json|g" \
  -e "s|{{DISCOVERY_CURRENT_ENTRY}}|$discovery_current_entry|g" \
  -e "s/{{INVENTORY_DIGEST}}/$inventory_digest/g" \
  -e "s/{{LINEAGE_DIGEST}}/$lineage_digest/g" \
  .eval/git-pretag/pre-tag-v1.4.0.md.in > "$fixture_tmp/pre-tag-v1.4.0.md"
mv "$fixture_tmp/pre-tag-v1.4.0.md" docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md
git add docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md
validate_added_record_delta staged "$anchor_commit" '' docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md validate_handoff_schema
GIT_AUTHOR_DATE='2026-07-20T01:15:00Z' GIT_COMMITTER_DATE='2026-07-20T01:15:00Z' \
  git commit -q -m 'fixture: add v1.4.0 discovery handoff'
handoff_commit=$(git rev-parse HEAD)
validate_added_record_delta committed "$anchor_commit" "$handoff_commit" docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md validate_handoff_schema
handoff_tree=$(git rev-parse 'HEAD^{tree}')
handoff_blob=$(git rev-parse 'HEAD:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md')
git branch fixture-pre-tag-handoff "$handoff_commit"
handoff_ref_created=1

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
cd "$fixture_root"
git worktree remove "$pre_tag_worktree"
git worktree prune
if [ -e "$pre_tag_worktree" ] || git worktree list --porcelain | grep -Fq "worktree $pre_tag_worktree"; then
  echo "pre-tag isolated worktree cleanup failed" >&2
  exit 1
fi
git update-ref -d "$pre_tag_transaction_ref"
if [ "$(git rev-parse HEAD)" != "$host_head_before" ] || [ "$(git status --porcelain=v2)" != "$host_status_before" ]; then
  echo "fixture caller worktree or index changed before pre-tag integration" >&2
  exit 1
fi
if [ "$(git rev-parse refs/heads/fixture-build)" != "$target_commit" ]; then
  echo "fixture release branch moved before pre-tag integration" >&2
  exit 1
fi
if ! git update-ref refs/heads/fixture-build "$handoff_commit" "$target_commit"; then
  echo "pre-tag compare-and-swap fast-forward integration failed" >&2
  exit 1
fi
pre_tag_integrated=1
if [ "$(git rev-parse refs/heads/fixture-build)" != "$handoff_commit" ] ||
   [ "$(git rev-parse refs/heads/fixture-build^{tree})" != "$handoff_tree" ] ||
   [ "$(git rev-parse refs/heads/fixture-build:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md)" != "$handoff_blob" ]; then
  git update-ref refs/heads/fixture-build "$target_commit" "$handoff_commit" || true
  echo "pre-tag integration readback failed" >&2
  exit 1
fi

post_tag_host_head_before=$(git rev-parse HEAD)
post_tag_host_status_before=$(git status --porcelain=v2)
git branch release-evidence/v1.4.0 "$handoff_commit"
evidence_ref_created=1
evidence_head=$(git rev-parse refs/heads/release-evidence/v1.4.0)
git tag v1.4.0 "$handoff_commit"
synthetic_tag_created=1
tag_object=$(git rev-parse refs/tags/v1.4.0)
tag_commit=$(git rev-parse 'refs/tags/v1.4.0^{}')
tag_tree=$(git rev-parse 'refs/tags/v1.4.0^{tree}')

candidate_from_tag="$fixture_tmp/candidate-from-tag.md"
handoff_from_tag="$fixture_tmp/handoff-from-tag.md"
git show "$tag_commit:docs/site/.meta/audit/audit-v1.4.0.md" > "$candidate_from_tag"
git show "$tag_commit:docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md" > "$handoff_from_tag"
validate_candidate_schema "$candidate_from_tag"
validate_handoff_schema "$handoff_from_tag"

tag_inventory_json=$(sed -n 's/^- Canonical inventory algorithm: `canonical-json-rfc8259-sorted-v1`; exact canonical JSON: `\(.*\)`\.$/\1/p' "$candidate_from_tag")
tag_inventory_digest=$(printf '%s' "$tag_inventory_json" | shasum -a 256 | awk '{print $1}')
tag_lineage_json=$(sed -n 's/^- lineage_canonical_json: `\(.*\)`$/\1/p' "$handoff_from_tag")
tag_lineage_digest=$(printf '%s' "$tag_lineage_json" | shasum -a 256 | awk '{print $1}')
if [ "$tag_inventory_json" != "$inventory_json" ] || [ "$tag_inventory_digest" != "$inventory_digest" ] ||
   [ "$tag_lineage_json" != "$lineage_json" ] || [ "$tag_lineage_digest" != "$lineage_digest" ]; then
  echo "post-tag inventory or lineage digest recomputation failed" >&2
  exit 1
fi

require_committed_blob "$tag_commit" docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md "$handoff_blob"
require_committed_blob "$tag_commit" docs/site/.meta/audit/audit-v1.4.0.md "$candidate_blob"
require_committed_blob "$tag_commit" docs/site/api/ai-search.md "$api_stamp_blob"
require_committed_blob "$tag_commit" docs/site/release-notes/v1.4.0.md "$release_stamp_blob"
require_committed_blob "$tag_commit" docs/site/release-notes/index.md "$index_stamp_blob"
require_committed_blob "$tag_commit" docs/site/.meta/releases.json "$metadata_target_blob"
require_committed_blob "$tag_commit" package.json "$package_target_blob"

tag_api_sha=$(git show "$tag_commit:docs/site/api/ai-search.md" | shasum -a 256 | awk '{print $1}')
tag_release_sha=$(git show "$tag_commit:docs/site/release-notes/v1.4.0.md" | shasum -a 256 | awk '{print $1}')
tag_index_sha=$(git show "$tag_commit:docs/site/release-notes/index.md" | shasum -a 256 | awk '{print $1}')
tag_metadata_sha=$(git show "$tag_commit:docs/site/.meta/releases.json" | shasum -a 256 | awk '{print $1}')
tag_package_sha=$(git show "$tag_commit:package.json" | shasum -a 256 | awk '{print $1}')
if [ "$tag_api_sha" != "$api_stamp_sha" ] || [ "$tag_release_sha" != "$release_stamp_sha" ] ||
   [ "$tag_index_sha" != "$index_stamp_sha" ] || [ "$tag_metadata_sha" != "$metadata_target_sha" ] ||
   [ "$tag_package_sha" != "$package_target_sha" ]; then
  echo "post-tag file-backed source SHA-256 recomputation failed" >&2
  exit 1
fi
tag_raw_version=$(git for-each-ref --format='%(refname:short)' refs/tags/v1.4.0)
target_raw_version=$(git show "$tag_commit:release-notes-handoff.md" | sed -n 's/^target_release_version: "\(v[^"]*\)"$/\1/p')
release_raw_version=$(git show "$tag_commit:docs/site/release-notes/v1.4.0.md" | sed -n 's/^# \(v[^[:space:]]*\)$/\1/p')
index_raw_version=$(git show "$tag_commit:docs/site/release-notes/index.md" | sed -n 's/^- \[\(v[^]]*\)\](.*)$/\1/p')
metadata_raw_version=$(git show "$tag_commit:docs/site/.meta/releases.json" | node -e 'let source=""; process.stdin.on("data", chunk => source += chunk).on("end", () => process.stdout.write(JSON.parse(source).latest))')
package_raw_version=$(git show "$tag_commit:package.json" | node -e 'let source=""; process.stdin.on("data", chunk => source += chunk).on("end", () => process.stdout.write(JSON.parse(source).version))')
for raw_version in "$tag_raw_version" "$target_raw_version" "$release_raw_version" "$index_raw_version" "$metadata_raw_version"
do
  if ! printf '%s\n' "$raw_version" | grep -Eq '^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$' || [ "$raw_version" != v1.4.0 ]; then
    echo "post-tag vX.Y.Z source parsing failed: $raw_version" >&2
    exit 1
  fi
done
if ! printf '%s\n' "$package_raw_version" | grep -Eq '^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$' ||
   [ "$package_raw_version" != 1.4.0 ]; then
  echo "post-tag X.Y.Z package source parsing failed: $package_raw_version" >&2
  exit 1
fi
for normalized_version in "${tag_raw_version#v}" "${target_raw_version#v}" "${release_raw_version#v}" "${index_raw_version#v}" "${metadata_raw_version#v}" "$package_raw_version"
do
  if [ "$normalized_version" != 1.4.0 ]; then
    echo "post-tag normalized SemVer mismatch: $normalized_version" >&2
    exit 1
  fi
done
require_record_contains "$candidate_from_tag" "post-stamp SHA-256 \`$tag_api_sha\`"
require_record_contains "$candidate_from_tag" "post-stamp SHA-256 \`$tag_release_sha\`"
require_record_contains "$candidate_from_tag" "post-stamp SHA-256 \`$tag_index_sha\`"
require_record_contains "$candidate_from_tag" "SHA-256 \`$tag_metadata_sha\`"
require_record_contains "$candidate_from_tag" "SHA-256 \`$tag_package_sha\`"
if ! git diff --quiet "$handoff_commit" "$tag_commit" -- || [ "$tag_tree" != "$handoff_tree" ]; then
  echo "post-tag handoff and tag trees diverged" >&2
  exit 1
fi

collect_post_tag_decision_evidence
git worktree add -q -b fixture-post-tag-transaction "$post_tag_worktree" "$evidence_head"
cd "$post_tag_worktree"
render_verified_post_tag_record "$fixture_tmp/audit-v1.4.0-post-tag.md"
mv "$fixture_tmp/audit-v1.4.0-post-tag.md" docs/site/.meta/audit/audit-v1.4.0-post-tag.md
git add docs/site/.meta/audit/audit-v1.4.0-post-tag.md
validate_added_record_delta staged "$evidence_head" '' docs/site/.meta/audit/audit-v1.4.0-post-tag.md validate_post_tag_schema
GIT_AUTHOR_DATE='2026-07-20T01:20:00Z' GIT_COMMITTER_DATE='2026-07-20T01:20:00Z' \
  git commit -q -m 'fixture: persist v1.4.0 post-tag audit'
post_tag_commit=$(git rev-parse HEAD)
validate_added_record_delta committed "$evidence_head" "$post_tag_commit" docs/site/.meta/audit/audit-v1.4.0-post-tag.md validate_post_tag_schema
post_tag_tree=$(git rev-parse "$post_tag_commit^{tree}")
post_tag_blob=$(git rev-parse "$post_tag_commit:docs/site/.meta/audit/audit-v1.4.0-post-tag.md")
post_tag_parent=$(git rev-parse "$post_tag_commit^")

cd "$fixture_root"
git worktree remove "$post_tag_worktree"
git worktree prune
if [ -e "$post_tag_worktree" ] || git worktree list --porcelain | grep -Fq "worktree $post_tag_worktree"; then
  echo "post-tag isolated worktree cleanup failed" >&2
  exit 1
fi
git update-ref -d "$post_tag_transaction_ref"
if [ "$(git rev-parse HEAD)" != "$post_tag_host_head_before" ] ||
   [ "$(git status --porcelain=v2)" != "$post_tag_host_status_before" ]; then
  echo "fixture caller worktree or index changed during post-tag transaction" >&2
  exit 1
fi

integration_tag_object=$(git rev-parse refs/tags/v1.4.0)
integration_tag_commit=$(git rev-parse 'refs/tags/v1.4.0^{}')
integration_tag_tree=$(git rev-parse 'refs/tags/v1.4.0^{tree}')
if [ "$integration_tag_object" != "$pre_integration_tag_object" ] || [ "$integration_tag_commit" != "$pre_integration_tag_commit" ] || [ "$integration_tag_tree" != "$pre_integration_tag_tree" ]; then
  echo "synthetic tag tuple moved after post-tag evidence capture" >&2
  exit 1
fi
if [ "$(git rev-parse refs/heads/release-evidence/v1.4.0)" != "$evidence_observed_head_before_record" ]; then
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
post_tag_integrated=1
final_evidence_head=$(git rev-parse refs/heads/release-evidence/v1.4.0)
final_evidence_blob=$(git rev-parse "$final_evidence_head:docs/site/.meta/audit/audit-v1.4.0-post-tag.md")
if [ "$final_evidence_head" != "$post_tag_commit" ] || [ "$final_evidence_blob" != "$post_tag_blob" ]; then
  git update-ref refs/heads/release-evidence/v1.4.0 "$evidence_head" "$post_tag_commit" || true
  echo "post-tag integration readback failed" >&2
  exit 1
fi

printf '%s\n' \
  '# Runtime Git evidence' \
  '' \
  "- base_ref: \`refs/heads/fixture-base\`" \
  "- base_commit: \`$base_commit\`" \
  "- target_ref: \`refs/heads/fixture-target\`" \
  "- target_commit: \`$target_commit\`" \
  "- target_tree: \`$(git rev-parse "$target_commit^{tree}")\`" \
  '- caller_ref: `refs/heads/fixture-caller`' \
  "- caller_head: \`$(git rev-parse refs/heads/fixture-caller)\`" \
  '- release_branch_ref: `refs/heads/fixture-build`' \
  "- release_branch_final_head: \`$(git rev-parse refs/heads/fixture-build)\`" \
  "- anchor_ref: \`refs/heads/fixture-pre-tag-anchor\`" \
  "- anchor_commit: \`$anchor_commit\`" \
  "- anchor_tree: \`$anchor_tree\`" \
  "- candidate_blob: \`$candidate_blob\`" \
  "- target_to_anchor_full_patch_sha256: \`$anchor_full_patch_sha\`" \
  '- pre_tag_isolated_worktree_cleanup: `passed`' \
  '- pre_tag_initial_and_final_staged_delta_gates: `passed`' \
  '- pre_tag_committed_delta_gate: `passed`' \
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
  '- post_tag_isolated_worktree_cleanup: `passed`' \
  '- post_tag_staged_and_committed_delta_gates: `passed`' \
  '- post_tag_inventory_lineage_sha_and_raw_form_recomputation: `passed`' \
  '- post_tag_decision_checks_before_record: `passed`' \
  '- caller_worktree_and_index_preserved: `passed`' \
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

candidate_binding=$(git show "$anchor_commit:$candidate_record_path" | sed -n 's/^- Candidate version-source binding: `\(.*\)`; discovery.*$/\1/p')
discovery_binding=$(git show "$handoff_commit:$discovery_record_path" | sed -n 's/^- candidate_source_binding: `\(.*\)`$/\1/p')
post_tag_binding=$(git show "$post_tag_commit:$post_tag_record_path" | sed -n 's/^- source_binding_target_release_version: `\(.*\)`$/target_release_version=\1/p')
post_tag_anchor=$(git show "$post_tag_commit:$post_tag_record_path" | sed -n 's/^- source_binding_anchor_sha: `\(.*\)`$/anchor_sha=\1/p')
post_tag_digest=$(git show "$post_tag_commit:$post_tag_record_path" | sed -n 's/^- source_binding_digest: `sha256:\(.*\)`$/digest=sha256:\1/p')
committed_discovery_current_entry=$(git show "$handoff_commit:$discovery_record_path" | sed -n 's/^- current_entry: `\(.*\)`$/\1/p')
committed_lineage_json=$(git show "$handoff_commit:$discovery_record_path" | sed -n 's/^- lineage_canonical_json: `\(.*\)`$/\1/p')
committed_lineage_digest=$(printf '%s' "$committed_lineage_json" | shasum -a 256 | awk '{print $1}')
discovery_lineage_digest=$(git show "$handoff_commit:$discovery_record_path" | sed -n 's/^- lineage_digest: `sha256:\(.*\)`$/\1/p')
post_tag_lineage_digest=$(git show "$post_tag_commit:$post_tag_record_path" | sed -n 's/^- lineage_digest: `sha256:\(.*\)`$/\1/p')
expected_binding="target_release_version=$source_target_release_version, anchor_sha=$source_anchor_sha, digest=sha256:$source_digest"
if [ "$candidate_binding" != "($expected_binding)" ] || [ "$discovery_binding" != "($expected_binding)" ] ||
   [ "$post_tag_binding, $post_tag_anchor, $post_tag_digest" != "$expected_binding" ]; then
  echo "candidate/discovery/post-tag source bindings diverged" >&2
  exit 1
fi
if [ "$committed_discovery_current_entry" != "$discovery_current_entry" ] ||
   [ "$committed_lineage_json" != "$lineage_json" ] ||
   [ "$committed_lineage_digest" != "$lineage_digest" ] ||
   [ "$discovery_lineage_digest" != "$lineage_digest" ] ||
   [ "$post_tag_lineage_digest" != "$lineage_digest" ]; then
  echo "committed discovery current-entry or lineage digest self-check failed" >&2
  exit 1
fi
if ! git show "$anchor_commit:$candidate_record_path" | grep -Fqx -- "- discovery_record_path: \`$discovery_record_path\`" ||
   ! git show "$anchor_commit:$candidate_record_path" | grep -Fqx -- "- post_tag_record_path: \`$post_tag_record_path\`" ||
   ! git show "$handoff_commit:$discovery_record_path" | grep -Fqx -- "- candidate_record_path: \`$candidate_record_path\`" ||
   ! git show "$handoff_commit:$discovery_record_path" | grep -Fqx -- "- post_tag_record_path: \`$post_tag_record_path\`" ||
   ! git show "$post_tag_commit:$post_tag_record_path" | grep -Fqx -- "- candidate_record_path: \`$candidate_record_path\`" ||
   ! git show "$post_tag_commit:$post_tag_record_path" | grep -Fqx -- "- handoff_path: \`$discovery_record_path\`" ||
   ! git show "$handoff_commit:$discovery_record_path" | grep -Fqx -- "- lineage_digest: \`sha256:$lineage_digest\`" ||
   ! git show "$post_tag_commit:$post_tag_record_path" | grep -Fqx -- "- lineage_digest: \`sha256:$lineage_digest\`"; then
  echo "candidate/discovery/post-tag cross-reference self-check failed" >&2
  exit 1
fi

echo "$runtime_evidence"
