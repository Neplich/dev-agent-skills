#!/bin/sh
set -eu

fixture_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$fixture_root"

if [ -e .git ]; then
  echo "fixture already initialized" >&2
  exit 1
fi

git init -q -b fixture-caller
git config user.name "Docs Eval Fixture"
git config user.email "docs-eval@example.invalid"

git commit -q --allow-empty -m "fixture: base release state"
base_commit=$(git rev-parse HEAD)
git branch fixture-base "$base_commit"
git tag v1.3.0 "$base_commit"

git add \
  package.json \
  release-chain-entry.md \
  release-notes-handoff.md \
  docs \
  src \
  tests \
  evidence
git commit -q -m "fixture: target release content"
target_commit=$(git rev-parse HEAD)
git branch fixture-target "$target_commit"
git branch fixture-build "$target_commit"

git update-ref refs/eval/tag-entry/v1.4.0 "$target_commit"
git update-ref refs/eval/release-evidence-expected/v1.4.0 "$target_commit"

drift_blob=$(printf '%s\n' "synthetic post-entry drift" | git hash-object -w --stdin)
target_tree=$(git rev-parse "$target_commit^{tree}")
git read-tree "$target_tree"
git update-index --add --cacheinfo 100644 "$drift_blob" .eval-drift-marker
combined_tree=$(git write-tree)
git read-tree "$target_tree"
drift_commit=$(printf '%s\n' "fixture: concurrent release evidence drift" | git commit-tree "$combined_tree" -p "$target_commit")

git update-ref refs/tags/v1.4.0 "$drift_commit"
git update-ref refs/heads/release-evidence/v1.4.0 "$drift_commit"
git reset -q --hard "$target_commit"

cat > .eval/runtime-git-evidence.md <<EOF
# Synthetic Git object index

- base_ref: \`refs/heads/fixture-base\`
- base_commit: \`$base_commit\`
- previous_tag_ref: \`refs/tags/v1.3.0\`
- previous_tag_object: \`$(git rev-parse refs/tags/v1.3.0)\`
- target_ref: \`refs/heads/fixture-target\`
- target_commit: \`$target_commit\`
- caller_ref: \`refs/heads/fixture-caller\`
- release_branch_ref: \`refs/heads/fixture-build\`
- tag_entry_snapshot_ref: \`refs/eval/tag-entry/v1.4.0\`
- tag_entry_snapshot_object: \`$(git rev-parse refs/eval/tag-entry/v1.4.0)\`
- actual_tag_ref: \`refs/tags/v1.4.0\`
- actual_tag_object: \`$(git rev-parse refs/tags/v1.4.0)\`
- release_evidence_expected_ref: \`refs/eval/release-evidence-expected/v1.4.0\`
- release_evidence_expected_object: \`$(git rev-parse refs/eval/release-evidence-expected/v1.4.0)\`
- release_evidence_branch_ref: \`refs/heads/release-evidence/v1.4.0\`
- release_evidence_branch_object: \`$(git rev-parse refs/heads/release-evidence/v1.4.0)\`
EOF

git status --porcelain=v2
