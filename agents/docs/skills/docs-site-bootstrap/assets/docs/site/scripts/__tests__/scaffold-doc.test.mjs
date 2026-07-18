import assert from 'node:assert/strict';
import { EventEmitter } from 'node:events';
import {
  cp, lstat, mkdir, mkdtemp, readFile, readdir, rm, symlink, writeFile
} from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve, win32 } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import YAML from 'yaml';
import {
  checkAffected, parseArgs as parseAffectedArgs, parseGitPaths,
  requiredDocExists, validateChangeMap
} from '../check-affected.mjs';
import { parseArgs as parseFrontmatterArgs } from '../check-frontmatter.mjs';
import { explicitVersion, validateReleaseMetadata } from '../check-version.mjs';
import { attachChildLifecycle } from '../dev-site.mjs';
import { collectMarkdown } from '../lib/pages.mjs';
import { buildSidebar } from '../lib/sidebar.mjs';
import { replaceGeneratedDirectory, validateGeneratedRoot } from '../prepare-site.mjs';
import {
  missingParentDirectories, npmExecutable, parseArgs as parseScaffoldArgs, scaffoldDocument
} from '../scaffold-doc.mjs';

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

test('scaffoldDocument rejects hidden path segments under a document type directory', async () => {
  const fixture = await createFixture();
  const input = options();
  input.path = 'docs/site/api/.meta/generated.md';
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /--path must not contain hidden path segments/
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

test('scaffoldDocument rejects non-relative exclude and related-code globs', async (context) => {
  for (const [field, value, expected] of [
    ['excludes', '../generated/**', /--exclude must be repository-root relative/],
    ['relatedCode', 'C:\\outside\\**', /--related-code must be repository-root relative/]
  ]) {
    await context.test(field, async () => {
      const fixture = await createFixture();
      const input = options();
      input.codeGlob = 'src/api/**';
      input.trigger = 'API behavior changes';
      input.changeMapTargets = [input.path];
      input[field] = [value];
      await assert.rejects(
        scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
        expected
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

test('scaffoldDocument rejects an existing Markdown-shaped directory as a change-map target', async () => {
  const fixture = await createFixture();
  await mkdir(resolve(fixture.siteRoot, 'api/directory.md'), { recursive: true });
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path, 'docs/site/api/directory.md'];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /must resolve to a regular Markdown file/
  );
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

test('scaffoldDocument rejects a change-map file symlink even when it stays inside docs/site', async () => {
  const fixture = await createFixture();
  const mapPath = resolve(fixture.siteRoot, 'standards/change-map.yaml');
  const realMap = resolve(fixture.siteRoot, 'standards/change-map.real.yaml');
  await writeFile(realMap, await readFile(mapPath, 'utf8'), 'utf8');
  await rm(mapPath);
  await symlink(realMap, mapPath, 'file');
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /change-map file must not be a symbolic link/
  );
});

test('scaffoldDocument rejects an additional change-map target outside docs/site through a symlink', async () => {
  const fixture = await createFixture();
  const outside = resolve(fixture.repoRoot, 'outside-pages');
  await mkdir(outside);
  await symlink(outside, resolve(fixture.siteRoot, 'api-link'), 'dir');
  const input = options();
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path, 'docs/site/api-link/reference.md'];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /--change-map-target must not escape docs\/site through a symbolic link/
  );
});

test('scaffoldDocument dry-run rejects an existing symlinked change-map target', async () => {
  const fixture = await createFixture();
  await mkdir(resolve(fixture.siteRoot, 'api'));
  const actual = resolve(fixture.siteRoot, 'api/actual.md');
  await writeFile(actual, '# actual\n', 'utf8');
  await symlink(actual, resolve(fixture.siteRoot, 'api/alias.md'), 'file');
  const input = options();
  input.dryRun = true;
  input.codeGlob = 'src/api/**';
  input.trigger = 'API behavior changes';
  input.changeMapTargets = [input.path, 'docs/site/api/alias.md'];
  await assert.rejects(
    scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
    /must resolve to a regular Markdown file/
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
  await context.test('multi-line title', async () => {
    const fixture = await createFixture();
    const input = options();
    input.title = 'first line\nsecond line';
    await assert.rejects(
      scaffoldDocument(input, { ...fixture, runDocsChecks: noChecks }),
      /--title must be a single line/
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

test('scaffoldDocument reports rollback cleanup failures without hiding the write failure', async () => {
  const fixture = await createFixture();
  const input = options();
  input.path = 'docs/site/api/nested/generated.md';
  await assert.rejects(
    scaffoldDocument(input, {
      ...fixture,
      runDocsChecks: async () => {
        await writeFile(resolve(fixture.siteRoot, 'api/concurrent.md'), 'keep', 'utf8');
        throw new Error('simulated verification failure');
      }
    }),
    (error) => {
      assert.equal(error instanceof AggregateError, true);
      assert.match(error.message, /rollback encountered 1 error/);
      assert.match(error.cause.message, /simulated verification failure/);
      return true;
    }
  );
  assert.equal(await readFile(resolve(fixture.siteRoot, 'api/concurrent.md'), 'utf8'), 'keep');
});

test('missingParentDirectories uses Windows path semantics for rollback boundaries', async () => {
  const siteRoot = 'C:\\repo\\docs\\site';
  const target = 'C:\\repo\\docs\\site\\api\\nested\\generated.md';
  const missing = await missingParentDirectories(target, siteRoot, {
    pathApi: win32,
    pathExists: async () => false
  });
  assert.deepEqual(missing, [
    'C:\\repo\\docs\\site\\api\\nested',
    'C:\\repo\\docs\\site\\api'
  ]);
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

test('checkAffected rejects a change map without the top-level change_map key', async () => {
  await assert.rejects(
    checkAffected({}, {
      checkFrontmatter: async () => [],
      readChangeMap: async () => YAML.stringify({ version: 1 }),
      changedFiles: async () => []
    }),
    /change_map is required and must be a mapping/
  );
});

test('validateChangeMap rejects malformed rules instead of disabling checks', async (context) => {
  const cases = [
    [{ 'src/**': null }, /entry src\/\*\* must be a mapping/],
    [{ 'src/**': { trigger: 'change' } }, /required_docs must be a non-empty string array/],
    [{ 'src/**': { required_docs: ['../outside.md'], trigger: 'change' } }, /repository-root relative/],
    [{ 'src/**': { required_docs: ['docs/site/api/page.md'] } }, /trigger must be a non-empty string/],
    [{ 'src/**': { required_docs: ['docs/site/api/page.md'], trigger: 'change', exclude: '../all' } }, /exclude must be a string array/]
  ];
  for (const [changeMap, expected] of cases) {
    await context.test(expected.source, () => {
      assert.throws(() => validateChangeMap({ change_map: changeMap }), expected);
    });
  }
});

test('requiredDocExists rejects a required page reached through an external symlink', async () => {
  const fixture = await createFixture();
  const outside = resolve(fixture.repoRoot, 'outside-required');
  await mkdir(outside);
  await writeFile(resolve(outside, 'page.md'), '# outside\n', 'utf8');
  await symlink(outside, resolve(fixture.siteRoot, 'linked'), 'dir');
  assert.equal(await requiredDocExists('docs/site/linked/page.md', fixture), false);
});

test('parseGitPaths preserves whitespace and newlines in NUL-delimited git paths', () => {
  assert.deepEqual(parseGitPaths('src/空 格.mjs\0src/line\nbreak.mjs\0'), [
    'src/空 格.mjs', 'src/line\nbreak.mjs'
  ]);
});

test('CLI parsers reject duplicate flags and option-looking empty values', () => {
  assert.throws(() => parseAffectedArgs(['--strict', '--strict']), /only once/);
  assert.throws(() => parseAffectedArgs(['--base', '--strict']), /requires a git ref/);
  assert.throws(() => parseAffectedArgs(['--base', 'main', '--base', 'HEAD']), /only once/);
  assert.throws(
    () => parseFrontmatterArgs(['--version-anchor-unavailable', '--version-anchor-unavailable']),
    /only once/
  );
  assert.throws(() => explicitVersion(['--version', '--other'], {}), /requires a value/);
  assert.throws(() => explicitVersion([], { RELEASE_VERSION: ' ' }), /non-empty string/);
  assert.throws(() => parseScaffoldArgs(['--dry-run', '--dry-run']), /only once/);
  assert.throws(() => parseScaffoldArgs(['--overwrite', '--overwrite']), /only once/);
});

test('validateReleaseMetadata rejects malformed root objects and ambiguous versions', () => {
  assert.deepEqual(validateReleaseMetadata(null), ['release metadata must be an object']);
  const errors = validateReleaseMetadata({
    latest: '',
    released: ['v1.0.0', 'v1.0.0'],
    verifiedDocs: { '': 'v1.0.0' }
  });
  assert.ok(errors.includes('latest must not be an empty string'));
  assert.ok(errors.includes('released must not contain duplicates'));
  assert.ok(errors.includes('verifiedDocs keys must be non-empty paths'));
});

test('collectMarkdown does not follow symlinked directories outside the site root', async () => {
  const root = await mkdtemp(join(tmpdir(), 'docs-pages-'));
  const outside = await mkdtemp(join(tmpdir(), 'docs-pages-outside-'));
  await writeFile(resolve(outside, 'page.md'), '---\ntitle: outside\n---\n', 'utf8');
  await symlink(outside, resolve(root, 'linked'), 'dir');
  assert.deepEqual(await collectMarkdown({ siteRoot: root }), []);
});

test('validateGeneratedRoot rejects a generated directory symlinked outside docs/site', async () => {
  const fixture = await createFixture();
  const outside = resolve(fixture.repoRoot, 'outside-generated');
  await mkdir(outside);
  await symlink(outside, resolve(fixture.siteRoot, '.generated'), 'dir');
  await assert.rejects(
    validateGeneratedRoot(resolve(fixture.siteRoot, '.generated'), fixture.siteRoot),
    /must not escape docs\/site through a symbolic link/
  );
});

test('replaceGeneratedDirectory preserves the previous tree when preparation fails', async () => {
  const root = await mkdtemp(join(tmpdir(), 'docs-generated-'));
  const output = resolve(root, 'public');
  await mkdir(output);
  await writeFile(resolve(output, 'state.txt'), 'old', 'utf8');
  await assert.rejects(
    replaceGeneratedDirectory(output, async (staging) => {
      await writeFile(resolve(staging, 'state.txt'), 'partial', 'utf8');
      throw new Error('build failed');
    }),
    /build failed/
  );
  assert.equal(await readFile(resolve(output, 'state.txt'), 'utf8'), 'old');
  assert.deepEqual((await readdir(root)).sort(), ['public']);
});

test('buildSidebar uses code-point ordering independent of locale data', () => {
  const pages = ['ä.md', 'Z.md'].map((relativePath) => ({
    relativePath: `api/${relativePath}`,
    route: `/api/${relativePath.slice(0, -3)}`,
    data: { title: relativePath, visibility: 'both' }
  }));
  const items = buildSidebar(pages, 'public')['/api/'][0].items;
  assert.deepEqual(items.map((item) => item.text), ['Z.md', 'ä.md']);
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

test('attachChildLifecycle handles spawn errors and signal exit codes', async (context) => {
  await context.test('spawn error', () => {
    const child = new EventEmitter();
    child.kill = () => {};
    const watcher = new EventEmitter();
    watcher.close = () => {};
    const runtimeProcess = new EventEmitter();
    const errors = [];
    attachChildLifecycle(child, watcher, () => {}, runtimeProcess, (error) => errors.push(error));
    child.emit('error', new Error('spawn failed'));
    assert.equal(runtimeProcess.exitCode, 1);
    assert.match(errors[0].message, /spawn failed/);
    assert.equal(runtimeProcess.listenerCount('SIGINT'), 0);
  });
  await context.test('SIGINT', () => {
    const child = new EventEmitter();
    let signal;
    child.kill = (value) => { signal = value; };
    const watcher = new EventEmitter();
    watcher.close = () => {};
    const runtimeProcess = new EventEmitter();
    attachChildLifecycle(child, watcher, () => {}, runtimeProcess);
    runtimeProcess.emit('SIGINT');
    assert.equal(signal, 'SIGINT');
    assert.equal(runtimeProcess.exitCode, 130);
  });
  await context.test('cleanup failure', () => {
    const child = new EventEmitter();
    child.kill = () => {};
    const runtimeProcess = new EventEmitter();
    const errors = [];
    attachChildLifecycle(child, { close: () => { throw new Error('close failed'); } },
      () => {}, runtimeProcess, (error) => errors.push(error));
    child.emit('close', 0);
    assert.equal(runtimeProcess.exitCode, 1);
    assert.match(errors[0].message, /close failed/);
  });
});

test('test:docs runs the affected-document gate in strict mode', async () => {
  const packageData = JSON.parse(await readFile(resolve(SITE_SOURCE, 'package.json'), 'utf8'));
  assert.match(packageData.scripts['test:docs'], /check:affected -- --strict/);
});

test('npmExecutable uses the Windows npm command shim', () => {
  assert.equal(npmExecutable('win32'), 'npm.cmd');
  assert.equal(npmExecutable('darwin'), 'npm');
});
