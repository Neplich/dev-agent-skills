import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('confirmed classes exist and blocked class has no page', () => {
  assert.equal(existsSync('ops/deployment/development/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/image-sources.md'), true);
  assert.equal(existsSync('ops/deployment/kubernetes-helm'), false);
});

test('Docker index and change map include the image authority', () => {
  const docker = readFileSync('ops/deployment/docker/index.md', 'utf8');
  const map = readFileSync('standards/change-map.yaml', 'utf8');
  assert.match(docker, /\(image-sources\.md\)/);
  assert.match(map, /docs\/site\/ops\/deployment\/docker\/image-sources\.md/);
});

test('confirmed pages do not contain Helm placeholders', () => {
  for (const path of ['ops/deployment/development/index.md', 'ops/deployment/docker/index.md']) {
    assert.doesNotMatch(readFileSync(path, 'utf8'), /helm install|imagePullSecrets|<namespace>/i);
  }
});
