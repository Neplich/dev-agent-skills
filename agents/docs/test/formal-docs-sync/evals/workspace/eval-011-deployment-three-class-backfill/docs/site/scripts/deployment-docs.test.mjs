import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import test from 'node:test';

const required = [
  'ops/deployment/index.md', 'ops/deployment/environment-reference.md',
  'ops/deployment/development/index.md', 'ops/deployment/development/image-build.md',
  'ops/deployment/docker/index.md', 'ops/deployment/docker/image-sources.md',
  'ops/deployment/kubernetes-helm/index.md', 'ops/deployment/kubernetes-helm/image-sources.md',
  'ops/deployment/kubernetes-helm/chart-package.md', 'ops/deployment/kubernetes-helm/values-reference.md',
];

test('three-class deployment page tree exists', () => {
  for (const path of required) assert.equal(existsSync(path), true, path);
});

test('navigation and change map include nested authorities', () => {
  const ops = readFileSync('ops/index.md', 'utf8');
  const map = readFileSync('standards/change-map.yaml', 'utf8');
  assert.match(ops, /deployment\//);
  for (const path of required) assert.match(map, new RegExp(path.replaceAll('/', '\\/').replace('.', '\\.')));
  assert.match(map, /custom_owner_field: preserve-me/);
});

test('all nested authorities are linked and internal links resolve', () => {
  const classIndexes = {
    'ops/deployment/development/index.md': ['image-build.md'],
    'ops/deployment/docker/index.md': ['image-sources.md'],
    'ops/deployment/kubernetes-helm/index.md': ['image-sources.md', 'chart-package.md', 'values-reference.md'],
  };
  for (const [index, children] of Object.entries(classIndexes)) {
    const body = readFileSync(index, 'utf8');
    for (const child of children) assert.match(body, new RegExp(`\\(${child.replace('.', '\\.')}\\)`), `${index} -> ${child}`);
  }
  for (const path of required) {
    const body = readFileSync(path, 'utf8');
    for (const match of body.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
      const target = match[1].split('#')[0];
      if (!target || target.includes('://')) continue;
      const resolved = resolve(dirname(path), target);
      assert.equal(existsSync(resolved) || existsSync(`${resolved}/index.md`), true, `${path} -> ${target}`);
    }
  }
});
