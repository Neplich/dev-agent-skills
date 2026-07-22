import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('confirmed classes exist and blocked class has no page', () => {
  assert.equal(existsSync('ops/deployment/index.md'), true);
  assert.equal(existsSync('ops/deployment/environment-reference.md'), true);
  assert.equal(existsSync('ops/deployment/development/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/image-sources.md'), true);
  assert.equal(existsSync('ops/deployment/kubernetes-helm'), false);
});

test('confirmed deployment pages link their authorities and appear in the change map', () => {
  const root = readFileSync('ops/deployment/index.md', 'utf8');
  const development = readFileSync('ops/deployment/development/index.md', 'utf8');
  const docker = readFileSync('ops/deployment/docker/index.md', 'utf8');
  const map = readFileSync('standards/change-map.yaml', 'utf8');

  assert.match(root, /\(environment-reference\.md\)/);
  assert.match(root, /\(development\/index\.md\)/);
  assert.match(root, /\(docker\/index\.md\)/);
  assert.match(development, /\(\.\.\/environment-reference\.md\)/);
  assert.match(docker, /\(\.\.\/environment-reference\.md\)/);
  assert.match(docker, /\(image-sources\.md\)/);
  for (const path of [
    'docs/site/ops/deployment/index.md',
    'docs/site/ops/deployment/environment-reference.md',
    'docs/site/ops/deployment/development/index.md',
    'docs/site/ops/deployment/docker/index.md',
    'docs/site/ops/deployment/docker/image-sources.md',
  ]) {
    assert.match(map, new RegExp(path.replaceAll('/', '\\/').replace('.', '\\.')));
  }
});

test('confirmed pages do not contain Helm placeholders', () => {
  for (const path of ['ops/deployment/development/index.md', 'ops/deployment/docker/index.md']) {
    assert.doesNotMatch(readFileSync(path, 'utf8'), /helm install|imagePullSecrets|<namespace>/i);
  }
});
