import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

const required = [
  'ops/deployment/index.md',
  'ops/deployment/environment-reference.md',
  'ops/deployment/docker/index.md',
  'ops/deployment/docker/image-sources.md',
];

test('Docker deployment verification uses the current page tree', () => {
  assert.equal(existsSync('ops/ai-hub-upgrade.md'), false);
  for (const path of required) assert.equal(existsSync(path), true, path);
});

test('deployment authorities are linked and mapped atomically', () => {
  const ops = readFileSync('ops/index.md', 'utf8');
  const root = readFileSync('ops/deployment/index.md', 'utf8');
  const docker = readFileSync('ops/deployment/docker/index.md', 'utf8');
  const map = readFileSync('standards/change-map.yaml', 'utf8');

  assert.match(ops, /\.\/deployment\//);
  assert.match(root, /environment-reference\.md/);
  assert.match(root, /docker\//);
  assert.match(docker, /\.\.\/environment-reference\.md/);
  assert.match(docker, /image-sources\.md/);
  for (const path of required) assert.match(map, new RegExp(path.replaceAll('/', '\\/').replace('.', '\\.')));
  assert.match(map, /deploy\/examples\/\*\*/);
});
