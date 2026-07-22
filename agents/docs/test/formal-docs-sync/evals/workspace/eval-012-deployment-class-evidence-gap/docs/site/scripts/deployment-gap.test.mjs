import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import test from 'node:test';

function assertLinksTo(source, target) {
  const body = readFileSync(source, 'utf8');
  const expected = resolve(target);
  const linked = [...body.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)].some((match) => {
    const link = match[1].split('#')[0];
    const resolved = resolve(dirname(source), link);
    return resolved === expected || resolve(resolved, 'index.md') === expected;
  });
  assert.equal(linked, true, `${source} -> ${target}`);
}

test('confirmed classes exist and blocked class has no page', () => {
  assert.equal(existsSync('ops/deployment/index.md'), true);
  assert.equal(existsSync('ops/deployment/environment-reference.md'), true);
  assert.equal(existsSync('ops/deployment/development/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/index.md'), true);
  assert.equal(existsSync('ops/deployment/docker/image-sources.md'), true);
  assert.equal(existsSync('ops/deployment/kubernetes-helm'), false);
});

test('confirmed deployment pages link their authorities and appear in the change map', () => {
  const map = readFileSync('standards/change-map.yaml', 'utf8');

  assertLinksTo('ops/deployment/index.md', 'ops/deployment/environment-reference.md');
  assertLinksTo('ops/deployment/index.md', 'ops/deployment/development/index.md');
  assertLinksTo('ops/deployment/index.md', 'ops/deployment/docker/index.md');
  assertLinksTo('ops/deployment/development/index.md', 'ops/deployment/environment-reference.md');
  assertLinksTo('ops/deployment/docker/index.md', 'ops/deployment/environment-reference.md');
  assertLinksTo('ops/deployment/docker/index.md', 'ops/deployment/docker/image-sources.md');
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
