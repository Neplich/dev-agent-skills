import assert from 'node:assert/strict';
import { EventEmitter } from 'node:events';
import {
  cp, lstat, mkdir, mkdtemp, readFile, readdir, rm, symlink, writeFile
} from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import YAML from 'yaml';
import { checkAffected } from '../check-affected.mjs';
import { attachChildLifecycle } from '../dev-site.mjs';
import { npmExecutable, scaffoldDocument } from '../scaffold-doc.mjs';

const TEST_DIR = dirname(fileURLToPath(import.meta.url));
const SITE_SOURCE = resolve(TEST_DIR, '../..');
const MAP_FIXTURE = resolve(TEST_DIR, 'fixtures/change-map.yaml');
const TYPE_CASES = [
  ['api', 'api'],
  ['database', 'database'],
  ['design', 'design'],
  ['ops', 'ops'],
  ['product', 'product']
];

async function createFixture() {
  const repoRoot = await mkdtemp(join(tmpdir(), 'docs-scaffold-'));
  const siteRoot = resolve(repoRoot, 'docs/site');
  await cp(resolve(SITE_SOURCE, 'standards/templates'), resolve(siteRoot, 'standards/templates'), {
    recursive: true
  });
  await cp(MAP_FIXTURE, resolve(siteRoot, 'standards/change-map.yaml'));
  return { repoRoot, siteRoot };
}

function options(type = 'api', directory = type) {
  return {
    type,
    path: `docs/site/${directory}/generated.md`,
    title: `${type} generated page`,
    visibility: 'internal',
    stage: 'draft',
    owners: ['docs'],
    relatedCode: [`src/${type}/**`],
    excludes: [],
    changeMapTargets: [],
    dryRun: false,
    overwrite: false
  };
}

const noChecks = async () => {};

async function treeSnapshot(root) {
  const result = new Map();
  async function walk(path, prefix = '') {
    for (const entry of await readdir(path, { withFileTypes: true })) {
      const absolute = resolve(path, entry.name);
      const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
      if (entry.isDirectory()) await walk(absolute, relative);
      else result.set(relative, await readFile(absolute, 'utf8'));
    }
  }
  await walk(root);
  return result;
}

for (const [type, directory] of TYPE_CASES) {
  test(`scaffoldDocument creates a valid ${type} page`, async () => {
    const fixture = await createFixture();
    let checks = 0;
    const input = options(type, directory);
    const summary = await scaffoldDocument(input, {
      ...fixture,
      runDocsChecks: async () => { checks += 1; }
    });
    const target = resolve(fixture.repoRoot, input.path);
    const source = await readFile(target, 'utf8');
    const page = matter(source);
    assert.equal(page.data.doc_type, type);
    assert.equal(page.data.last_verified_version, 'unverified');
    assert.deepEqual(page.data.owners, ['docs']);
    assert.deepEqual(page.data.related_code, [`src/${type}/**`]);
    assert.match(page.content, new RegExp(`^\\n?# ${type} generated page$`, 'm'));
    assert.equal(summary.changeMapDelta, null);
    assert.equal(checks, 1);
  });
}

test('scaffoldDocument rejects unknown document types', async () => {
  const fixture = await createFixture();
  await assert.rejects(
    scaffoldDocument(options('unknown'), { ...fixture, runDocsChecks: noChecks }),
    /Unknown document type/
  );
});

test('scaffoldDocument rejects paths outside docs/site', async () => {
  const fixture = await createFixture();
  const input = options();
  input.path = 'docs/generated.md';
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /inside docs\/site/
  );
});

test('scaffoldDocument rejects a change-map target that resolves outside docs/site', async () => {
  const fixture = await createFixture();
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = ['docs/site/../outside.md'];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /--change-map-target must be repository-root relative under docs\/site\//
  );
});

test('scaffoldDocument rejects non-relative change-map code globs', async (context) => {
  for (const codeGlob of ['/src/api/**', '../src/api/**', 'C:\\src\\api\\**']) {
    await context.test(codeGlob, async () => {
      const fixture = await createFixture();
      const input = options();
      input.codeGlob = codeGlob;
      input.trigger = 'API behavior changes';
      input.changeMapTargets = [input.path];
      await assert.rejects(
        scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
        /--code-glob must be repository-root relative/
      );
    });
  }
});

test('scaffoldDocument rejects non-page change-map targets', async (context) => {
  for (const mapTarget of ['docs/site/api', 'docs/site/api/generated.txt', 'docs/site/.meta/page.md']) {
    await context.test(mapTarget, async () => {
      const fixture = await createFixture();
      const input = options();
      input.codeGlob = 'src/api/**';
      input.trigger = 'API behavior changes';
      input.changeMapTargets = [mapTarget];
      await assert.rejects(
        scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
        /--change-map-target must be a Markdown page under docs\/site\//
      );
    });
  }
});

test('scaffoldDocument rejects a symlinked change-map parent outside docs/site', async () => {
  const fixture = await createFixture();
  const outside = resolve(fixture.repoRoot, 'outside-standards');
  await cp(resolve(fixture.siteRoot, 'standards'), outside, { recursive: true });
  await rm(resolve(fixture.siteRoot, 'standards'), { recursive: true });
  await symlink(outside, resolve(fixture.siteRoot, 'standards'), 'dir');
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /must not escape docs\/site through a symbolic link/
  );
});

test('scaffoldDocument rejects a target path that escapes through a symbolic link', async () => {
  const fixture = await createFixture();
  const outside = resolve(fixture.repoRoot, 'outside');
  await mkdir(outside);
  await symlink(outside, resolve(fixture.siteRoot, 'api'), 'dir');
  await assert.rejects(
    scaffoldDocument(options(), { ...fixture, runDocsChecks: noChecks }),
    /must not escape docs\/site through a symbolic link/
  );
});

test('scaffoldDocument rejects a type and directory mismatch', async () => {
  const fixture = await createFixture();
  await assert.rejects(
    scaffoldDocument(options('api', 'ops'), { ...fixture, runDocsChecks: noChecks }),
    /requires a Markdown path under docs\/site\/api\//
  );
});

test('scaffoldDocument rejects an existing page without overwrite authorization', async () => {
  const fixture = await createFixture();
  const input = options();
  await scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks });
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /target already exists/
  );
});

test('scaffoldDocument rejects a broken target symlink even with overwrite authorization', async () => {
  const fixture = await createFixture();
  await mkdir(resolve(fixture.siteRoot, 'api'));
  const target = resolve(fixture.siteRoot, 'api/generated.md');
  await symlink(resolve(fixture.repoRoot, 'missing.md'), target, 'file');
  const input = options();
  input.overwrite = true;
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /target page must not be a symbolic link/
  );
  assert.equal((await lstat(target)).isSymbolicLink(), true);
});

test('scaffoldDocument rejects missing #118 inputs and incomplete change-map input', async (context) => {
  await context.test('missing owner', async () => {
    const fixture = await createFixture();
    const input = options();
    input.owners = [];
    await assert.rejects(
      scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
      /at least one non-empty --owner/
    );
  });
  await context.test('incomplete mapping', async () => {
    const fixture = await createFixture();
    const input = options();
    input.codeGlob = 'src/api/**';
    await assert.rejects(
      scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
      /--trigger is required/
    );
  });
});

test('scaffoldDocument rejects missing or duplicate template scaffold blocks', async (context) => {
  for (const variant of ['missing', 'duplicate']) {
    await context.test(variant, async () => {
      const fixture = await createFixture();
      const template = resolve(fixture.siteRoot, 'standards/templates/api-template.md');
      const source = await readFile(template, 'utf8');
      const broken = variant === 'missing'
        ? source.replace('<!-- docs-scaffold:start -->', '<!-- removed -->')
        : `${source}\n<!-- docs-scaffold:start -->\n`;
      await writeFile(template, broken);
      await assert.rejects(
        scaffoldDocument(options(), { ...fixture, runDocsChecks: noChecks }),
        /exactly one docs-scaffold block/
      );
    });
  }
});

test('scaffoldDocument dry-run reports the delta and writes nothing', async () => {
  const fixture = await createFixture();
  const before = await treeSnapshot(fixture.repoRoot);
  const input = options();
  input.dryRun = true;
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path];
  const summary = await scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks });
  const after = await treeSnapshot(fixture.repoRoot);
  assert.deepEqual(after, before);
  assert.equal(summary.dryRun, true);
  assert.equal(summary.page, input.path);
  assert.equal(summary.changeMapDelta.codeGlob, 'src/api/**');
});

test('scaffoldDocument explicitly merges and stably sorts change-map fields', async () => {
  const fixture = await createFixture();
  const input = options('product');
  input.path = 'docs/site/product/manual-extra.md';
  input.codeGlob = 'manual/**';
  input.trigger = 'A replacement trigger that must not erase manual text';
  input.changeMapTargets = [input.path, 'docs/site/product/manual.md'];
  input.excludes = ['manual/generated/**', 'manual/archive/**', 'manual/generated/**'];
  await scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks });
  const data = YAML.parse(await readFile(resolve(fixture.siteRoot, 'standards/change-map.yaml'), 'utf8'));
  assert.deepEqual(data.change_map['manual/**'].required_docs, [
    'docs/site/product/manual-extra.md',
    'docs/site/product/manual.md'
  ]);
  assert.deepEqual(data.change_map['manual/**'].exclude, [
    'manual/archive/**', 'manual/generated/**'
  ]);
  assert.equal(data.change_map['manual/**'].trigger, 'Keep this manual entry');
  assert.equal(data.change_map['manual/**'].custom_rule_field, 'keep-me');
});

test('scaffoldDocument rejects an invalid target change-map entry', async () => {
  const fixture = await createFixture();
  const mapPath = resolve(fixture.siteRoot, 'standards/change-map.yaml');
  const source = await readFile(mapPath, 'utf8');
  await writeFile(mapPath, source.replace(
    'required_docs:\n      - docs/site/product/manual.md',
    'required_docs: docs/site/product/manual.md'
  ));
  const input = options('product');
  input.path = 'docs/site/product/manual-extra.md';
  input.codeGlob = 'manual/**';
  input.trigger = 'Manual behavior changes';
  input.changeMapTargets = [input.path];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /required_docs must be a string array/
  );
});

test('scaffoldDocument preserves unknown change-map entries and top-level fields', async () => {
  const fixture = await createFixture();
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path];
  await scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks });
  const data = YAML.parse(await readFile(resolve(fixture.siteRoot, 'standards/change-map.yaml'), 'utf8'));
  assert.equal(data.custom_top_level, 'keep-me');
  assert.equal(data.change_map['manual/**'].custom_rule_field, 'keep-me');
  assert.deepEqual(data.change_map['src/api/**'].required_docs, [input.path]);
});

test('scaffoldDocument rolls back the page and change map when post-write checks fail', async () => {
  const fixture = await createFixture();
  const input = options();
  input.path = 'docs/site/api/nested/deep/generated.md';
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path];
  const mapPath = resolve(fixture.siteRoot, 'standards/change-map.yaml');
  const originalMap = await readFile(mapPath, 'utf8');
  await assert.rejects(
    scaffoldDocument(input, {
      ...fixture,
      runDocsChecks: async () => { throw new Error('simulated test:docs failure'); }
    }),
    /simulated test:docs failure/
  );
  await assert.rejects(readFile(resolve(fixture.repoRoot, input.path), 'utf8'), /ENOENT/);
  await assert.rejects(readdir(resolve(fixture.siteRoot, 'api')), /ENOENT/);
  assert.equal(await readFile(mapPath, 'utf8'), originalMap);
});

test('scaffoldDocument rejects release notes and hands off to issue #116', async () => {
  const fixture = await createFixture();
  const input = options('release-notes');
  input.path = 'docs/site/release-notes/v1.md';
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /Release Notes Skill from issue #116/
  );
  const pathInput = options('api');
  pathInput.path = 'docs/site/release-notes/v1.md';
  await assert.rejects(
    scaffoldDocument(pathInput, { ...fixture, runDocsChecks: noChecks }),
    /Release Notes Skill from issue #116/
  );
});

test('checkAffected treats a deleted required doc as missing even when it changed', async () => {
  const requiredDoc = 'docs/site/api/required.md';
  const result = await checkAffected({ strict: true }, {
    checkFrontmatter: async () => [],
    readChangeMap: async () => YAML.stringify({
      change_map: {
        'src/api/**': {
          required_docs: [requiredDoc],
          trigger: 'API behavior changes'
        }
      }
    }),
    changedFiles: async () => ['src/api/handler.mjs', requiredDoc],
    requiredDocExists: async () => false
  });
  assert.equal(result.blocked, true);
  assert.deepEqual(result.suspects[0].missingDocs, [requiredDoc]);
});

test('attachChildLifecycle closes the watcher and propagates the child exit code', () => {
  const child = new EventEmitter();
  child.kill = () => {};
  const runtimeProcess = new EventEmitter();
  runtimeProcess.exitCode = undefined;
  let watcherCloses = 0;
  let timerClears = 0;
  attachChildLifecycle(child, { close: () => { watcherCloses += 1; } }, () => {
    timerClears += 1;
  }, runtimeProcess);
  child.emit('close', 2);
  assert.equal(watcherCloses, 1);
  assert.equal(timerClears, 1);
  assert.equal(runtimeProcess.exitCode, 2);
  assert.equal(runtimeProcess.listenerCount('SIGINT'), 0);
  assert.equal(runtimeProcess.listenerCount('SIGTERM'), 0);
});

test('npmExecutable uses the Windows npm command shim', () => {
  assert.equal(npmExecutable('win32'), 'npm.cmd');
  assert.equal(npmExecutable('darwin'), 'npm');
});
