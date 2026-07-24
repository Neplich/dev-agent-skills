import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('aggregate path migrated', () => {
  assert.equal(existsSync('ops/deployment.md'), false);
  assert.equal(existsSync('ops/deployment/index.md'), true);
  assert.equal(existsSync('ops/deployment/environment-reference.md'), true);
  for (const kind of ['development', 'docker', 'kubernetes-helm']) {
    assert.equal(existsSync(`ops/deployment/${kind}/index.md`), true);
  }
});

test('legacy links and mappings are repaired without data loss', () => {
  const all = ['ops/index.md', 'product/runtime.md', 'standards/change-map.yaml'].map((p) => readFileSync(p, 'utf8')).join('\n');
  assert.doesNotMatch(all, /ops\/deployment\.md|\.\.\/ops\/deployment\.md|\.\/deployment\.md/);
  assert.match(all, /custom_owner_field: preserve-me/);
  assert.match(all, /scripts\/dev\/examples/);
  for (const kind of ['development', 'docker', 'kubernetes-helm']) assert.match(all, new RegExp(`deployment/${kind}`));
});
