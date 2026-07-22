import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('confirmed classes exist and blocked class has no page', () => {
  assert.equal(existsSync('ops/deployment/development/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/index.md'), true);
  assert.equal(existsSync('ops/deployment/kubernetes-helm'), false);
});

test('confirmed pages do not contain Helm placeholders', () => {
  for (const path of ['ops/deployment/development/index.md', 'ops/deployment/docker/index.md']) {
    assert.doesNotMatch(readFileSync(path, 'utf8'), /helm install|imagePullSecrets|<namespace>/i);
  }
});
