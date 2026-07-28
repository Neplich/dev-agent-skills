import { execFile } from 'node:child_process';
import { randomUUID } from 'node:crypto';
import {
  lstat, mkdir, readFile, realpath, rename, rm, rmdir, writeFile
} from 'node:fs/promises';
import { dirname, isAbsolute, relative, resolve, sep } from 'node:path';
import { promisify } from 'node:util';
import { fileURLToPath } from 'node:url';
import matter from 'gray-matter';
import YAML from 'yaml';
import { validatePage } from './lib/frontmatter.mjs';
import { REPO_ROOT, SITE_ROOT, toPosix } from './lib/paths.mjs';

const exec = promisify(execFile);
const START = '<!-- docs-scaffold:start -->';
const END = '<!-- docs-scaffold:end -->';
const RELEASE_HANDOFF = 'Release Notes are not supported by new:doc; use the independent Release Notes Skill from issue #116.';
const TYPES = {
  api: { directory: 'api', template: 'api-template.md' },
  database: { directory: 'database', template: 'database.md' },
  design: { directory: 'design', template: 'feature-design.md' },
  ops: { directory: 'ops', template: 'ops-runbook.md' },
  product: { directory: 'product', template: 'product-handbook.md' }
};
const VISIBILITIES = new Set(['public', 'internal', 'both']);
const STAGES = new Set(['draft', 'dev', 'ops', 'release']);

function values(argv, index, option) {
  const value = argv[index + 1];
  if (!value || value.startsWith('--')) throw new Error(`${option} requires a value`);
  return value;
}

export function parseArgs(argv) {
  const options = {
    owners: [], relatedCode: [], excludes: [], changeMapTargets: [],
    dryRun: false, overwrite: false
  };
  const flags = new Set();
  const scalar = new Map([
    ['--type', 'type'], ['--path', 'path'], ['--title', 'title'],
    ['--visibility', 'visibility'], ['--stage', 'stage'],
    ['--code-glob', 'codeGlob'], ['--trigger', 'trigger']
  ]);
  const repeated = new Map([
    ['--owner', 'owners'], ['--related-code', 'relatedCode'],
    ['--exclude', 'excludes'], ['--change-map-target', 'changeMapTargets']
  ]);
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === '--dry-run' || argument === '--overwrite') {
      if (flags.has(argument)) throw new Error(`${argument} may be provided only once`);
      flags.add(argument);
      options[argument === '--dry-run' ? 'dryRun' : 'overwrite'] = true;
    }
    else if (scalar.has(argument)) {
      const key = scalar.get(argument);
      if (options[key] !== undefined) throw new Error(`${argument} may be provided only once`);
      options[key] = values(argv, index, argument);
      index += 1;
    } else if (repeated.has(argument)) {
      options[repeated.get(argument)].push(values(argv, index, argument));
      index += 1;
    } else {
      throw new Error(`Unknown argument: ${argument}`);
    }
  }
  return options;
}

function required(value, option) {
  if (typeof value !== 'string' || value.trim() === '') throw new Error(`${option} is required`);
}

function normalizeRepoGlob(value, option) {
  required(value, option);
  const normalized = value.replaceAll('\\', '/');
  if (/[\0\r\n]/.test(normalized) || isAbsolute(value) || normalized.startsWith('/')
      || /^[A-Za-z]:\//.test(normalized)
      || normalized.split('/').includes('..')) {
    throw new Error(`${option} must be repository-root relative`);
  }
  return normalized;
}

function validateInputs(options, repoRoot) {
  required(options.type, '--type');
  if (options.type === 'release-notes' || options.type === 'release') {
    throw new Error(RELEASE_HANDOFF);
  }
  const type = TYPES[options.type];
  if (!type) throw new Error(`Unknown document type: ${options.type}`);
  for (const [value, option] of [
    [options.path, '--path'], [options.title, '--title'],
    [options.visibility, '--visibility'], [options.stage, '--stage']
  ]) required(value, option);
  if (/[\0\r\n]/.test(options.title)) throw new Error('--title must be a single line');
  if (/[\0\r\n]/.test(options.path)) {
    throw new Error('--path must not contain NUL, CR, or LF control characters');
  }
  if (!VISIBILITIES.has(options.visibility)) {
    throw new Error('--visibility must be public, internal, or both');
  }
  if (!STAGES.has(options.stage)) throw new Error('--stage must be draft, dev, ops, or release');
  if (!options.owners.length || options.owners.some((item) => !item.trim())) {
    throw new Error('at least one non-empty --owner is required');
  }
  if (!options.relatedCode.length || options.relatedCode.some((item) => !item.trim())) {
    throw new Error('at least one non-empty --related-code is required');
  }
  options.relatedCode = options.relatedCode.map((item) => normalizeRepoGlob(item, '--related-code'));
  if (isAbsolute(options.path)) throw new Error('--path must be repository-root relative');
  const normalized = toPosix(options.path);
  const expected = `docs/site/${type.directory}/`;
  if (normalized === 'docs/site/release-notes' || normalized.startsWith('docs/site/release-notes/')) {
    throw new Error(RELEASE_HANDOFF);
  }
  const target = resolve(repoRoot, normalized);
  const lexical = toPosix(relative(repoRoot, target));
  if (lexical.startsWith('../') || lexical === '..' || !lexical.startsWith('docs/site/')) {
    throw new Error('--path must stay inside docs/site/');
  }
  if (!lexical.startsWith(expected) || !lexical.endsWith('.md')) {
    throw new Error(`--type ${options.type} requires a Markdown path under ${expected}**`);
  }
  const pageSegments = lexical.slice(expected.length).split('/');
  if (pageSegments.some((segment) => segment.startsWith('.'))) {
    throw new Error('--path must not contain hidden path segments under the document type directory');
  }
  const mappingSupplied = [
    options.codeGlob, options.trigger, ...options.excludes, ...options.changeMapTargets
  ].some((value) => value !== undefined && value !== '');
  if (mappingSupplied) {
    required(options.codeGlob, '--code-glob');
    required(options.trigger, '--trigger');
    options.codeGlob = normalizeRepoGlob(options.codeGlob, '--code-glob');
    options.excludes = options.excludes.map((item) => normalizeRepoGlob(item, '--exclude'));
    if (!options.changeMapTargets.length
        || options.changeMapTargets.some((item) => !item.trim())) {
      throw new Error('explicit change-map input requires at least one --change-map-target');
    }
    options.changeMapTargets = options.changeMapTargets.map((mapTarget) => {
      if (/[\0\r\n]/.test(mapTarget)) {
        throw new Error('--change-map-target must be a single repository-relative path');
      }
      if (isAbsolute(mapTarget)) {
        throw new Error('--change-map-target must be repository-root relative under docs/site/');
      }
      const absolute = resolve(repoRoot, toPosix(mapTarget));
      const relativeTarget = toPosix(relative(repoRoot, absolute));
      if (relativeTarget === '..' || relativeTarget.startsWith('../')
          || !relativeTarget.startsWith('docs/site/')) {
        throw new Error('--change-map-target must be repository-root relative under docs/site/');
      }
      const pageSegments = relativeTarget.slice('docs/site/'.length).split('/');
      if (!relativeTarget.endsWith('.md') || pageSegments.some((segment) => segment.startsWith('.'))) {
        throw new Error('--change-map-target must be a Markdown page under docs/site/');
      }
      return relativeTarget;
    });
  }
  return { target, lexical, type, mappingSupplied };
}

function markerCount(source, marker) {
  return source.split(marker).length - 1;
}

export function extractScaffold(source) {
  if (markerCount(source, START) !== 1 || markerCount(source, END) !== 1) {
    throw new Error('template must contain exactly one docs-scaffold block');
  }
  const start = source.indexOf(START);
  const end = source.indexOf(END);
  if (start >= end) throw new Error('template scaffold markers are out of order');
  const block = source.slice(start + START.length, end).trim();
  const match = block.match(/^```md\r?\n([\s\S]*?)\r?\n```$/);
  if (!match) throw new Error('template scaffold block must contain exactly one md fence');
  return `${match[1]}\n`;
}

const yamlScalar = (value) => JSON.stringify(value);
const yamlList = (values) => values.map((value) => `  - ${yamlScalar(value)}`).join('\n');

function renderPage(scaffold, options) {
  const replacements = new Map([
    ['title: {{title}}', `title: ${yamlScalar(options.title)}`],
    ['{{title}}', options.title],
    ['{{visibility}}', options.visibility],
    ['{{doc_type}}', options.type],
    ['{{stage}}', options.stage],
    ['  - {{owner}}', yamlList(options.owners)],
    ['  - {{related_code}}', yamlList(options.relatedCode)]
  ]);
  let output = scaffold;
  for (const [placeholder, value] of replacements) output = output.replaceAll(placeholder, value);
  if (/{{[^}]+}}/.test(output)) throw new Error('template scaffold contains an unsupported placeholder');
  const page = matter(output);
  if (page.data.doc_type !== options.type) {
    throw new Error(`template doc_type must be fixed to ${options.type}`);
  }
  if (page.data.last_verified_version !== 'unverified') {
    throw new Error('template last_verified_version must be fixed to unverified');
  }
  const errors = validatePage({ data: page.data });
  if (errors.length) throw new Error(`generated frontmatter is invalid: ${errors.join('; ')}`);
  return output;
}

function uniqueSorted(values) {
  return [...new Set(values.map((value) => value.trim()).filter(Boolean))].sort();
}

function parseChangeMap(source) {
  const document = YAML.parseDocument(source);
  if (document.errors.length) {
    throw new Error(`change-map parse failed: ${document.errors[0].message}`);
  }
  const map = document.get('change_map', true);
  if (!YAML.isMap(map)) throw new Error('change_map must be a mapping');
  return document;
}

function mergeChangeMap(source, options) {
  const document = parseChangeMap(source);
  const existing = document.getIn(['change_map', options.codeGlob]);
  if (existing !== undefined && !YAML.isMap(existing)) {
    throw new Error(`change_map entry ${options.codeGlob} must be a mapping`);
  }
  const previous = existing?.toJSON() ?? {};
  const stringList = (value) => Array.isArray(value)
    && value.every((item) => typeof item === 'string' && item.trim() !== '');
  if (previous.required_docs !== undefined && !stringList(previous.required_docs)) {
    throw new Error(`change_map entry ${options.codeGlob} required_docs must be a string array`);
  }
  if (previous.trigger !== undefined
      && (typeof previous.trigger !== 'string' || previous.trigger.trim() === '')) {
    throw new Error(`change_map entry ${options.codeGlob} trigger must be a non-empty string`);
  }
  if (previous.exclude !== undefined && !stringList(previous.exclude)) {
    throw new Error(`change_map entry ${options.codeGlob} exclude must be a string array`);
  }
  const requiredDocs = uniqueSorted([
    ...(Array.isArray(previous.required_docs) ? previous.required_docs : []),
    ...options.changeMapTargets
  ]);
  const excludes = uniqueSorted([
    ...(Array.isArray(previous.exclude) ? previous.exclude : []),
    ...options.excludes
  ]);
  if (existing === undefined) {
    const entry = { required_docs: requiredDocs, trigger: options.trigger };
    if (excludes.length) entry.exclude = excludes;
    document.setIn(['change_map', options.codeGlob], entry);
  } else {
    document.setIn(['change_map', options.codeGlob, 'required_docs'], requiredDocs);
    if (!previous.trigger) document.setIn(['change_map', options.codeGlob, 'trigger'], options.trigger);
    if (excludes.length) document.setIn(['change_map', options.codeGlob, 'exclude'], excludes);
  }
  const output = document.toString();
  parseChangeMap(output);
  return {
    output,
    delta: { codeGlob: options.codeGlob, requiredDocs, trigger: previous.trigger ?? options.trigger, excludes }
  };
}

async function exists(path) {
  try {
    await lstat(path);
    return true;
  } catch {
    return false;
  }
}

async function validateTargetRealPath(target, siteRoot, option = '--path') {
  const realSiteRoot = await realpath(siteRoot);
  let existingPath = target;
  while (!(await exists(existingPath))) {
    const parent = dirname(existingPath);
    if (parent === existingPath) throw new Error(`${option} has no existing parent`);
    existingPath = parent;
  }
  const realExistingPath = await realpath(existingPath);
  const relativeExistingPath = toPosix(relative(realSiteRoot, realExistingPath));
  if (relativeExistingPath === '..' || relativeExistingPath.startsWith('../')
      || isAbsolute(relativeExistingPath)) {
    throw new Error(`${option} must not escape docs/site through a symbolic link`);
  }
}

export function npmExecutable(platform = process.platform) {
  return platform === 'win32' ? 'npm.cmd' : 'npm';
}

async function defaultRunDocsChecks(siteRoot) {
  await exec(npmExecutable(), ['run', 'test:docs'], { cwd: siteRoot });
}

export async function missingParentDirectories(targetPath, stopAt, dependencies = {}) {
  const pathApi = dependencies.pathApi ?? { dirname, isAbsolute, relative, sep };
  const pathExists = dependencies.pathExists ?? exists;
  const missing = [];
  let current = pathApi.dirname(targetPath);
  while (current !== stopAt) {
    const relativeCurrent = pathApi.relative(stopAt, current);
    if (relativeCurrent === '' || relativeCurrent === '..'
        || relativeCurrent.startsWith(`..${pathApi.sep}`)
        || pathApi.isAbsolute(relativeCurrent)) break;
    if (await pathExists(current)) break;
    missing.push(current);
    current = pathApi.dirname(current);
  }
  return missing;
}

async function atomicWrite(changes, verify, rollbackRoots = []) {
  const originals = new Map();
  const temporary = [];
  try {
    for (const change of changes) {
      const hadOriginal = await exists(change.path);
      originals.set(change.path, hadOriginal ? await readFile(change.path) : null);
      await mkdir(dirname(change.path), { recursive: true });
      const temp = `${change.path}.docs-scaffold-${randomUUID()}.tmp`;
      await writeFile(temp, change.content, 'utf8');
      temporary.push(temp);
    }
    for (let index = 0; index < changes.length; index += 1) {
      await rename(temporary[index], changes[index].path);
    }
    await verify();
  } catch (error) {
    const rollbackErrors = [];
    for (const temp of temporary) {
      try {
        await rm(temp, { force: true });
      } catch (rollbackError) {
        rollbackErrors.push(rollbackError);
      }
    }
    for (const [path, content] of originals) {
      try {
        if (content === null) await rm(path, { force: true });
        else {
          await mkdir(dirname(path), { recursive: true });
          await writeFile(path, content);
        }
      } catch (rollbackError) {
        rollbackErrors.push(rollbackError);
      }
    }
    for (const root of rollbackRoots) {
      try {
        await rmdir(root);
      } catch (rollbackError) {
        rollbackErrors.push(rollbackError);
      }
    }
    if (rollbackErrors.length) {
      throw new AggregateError(
        [error, ...rollbackErrors],
        `write failed and rollback encountered ${rollbackErrors.length} error(s)`,
        { cause: error }
      );
    }
    throw error;
  }
}

export async function scaffoldDocument(options, dependencies = {}) {
  const repoRoot = dependencies.repoRoot ?? REPO_ROOT;
  const siteRoot = dependencies.siteRoot ?? SITE_ROOT;
  const runDocsChecks = dependencies.runDocsChecks ?? defaultRunDocsChecks;
  const resolved = validateInputs(options, repoRoot);
  if (await exists(resolved.target) && (await lstat(resolved.target)).isSymbolicLink()) {
    throw new Error(`target page must not be a symbolic link: ${resolved.lexical}`);
  }
  await validateTargetRealPath(resolved.target, siteRoot);
  const mapPath = resolve(siteRoot, 'standards/change-map.yaml');
  if (resolved.mappingSupplied) {
    await validateTargetRealPath(mapPath, siteRoot, '--change-map-target');
    if ((await lstat(mapPath)).isSymbolicLink()) {
      throw new Error('change-map file must not be a symbolic link');
    }
    for (const mapTarget of options.changeMapTargets) {
      const absoluteTarget = resolve(repoRoot, mapTarget);
      await validateTargetRealPath(absoluteTarget, siteRoot, '--change-map-target');
      if (await exists(absoluteTarget)) {
        const stats = await lstat(absoluteTarget);
        if (!stats.isFile()) {
          throw new Error('--change-map-target must resolve to a regular Markdown file when it exists');
        }
      }
    }
  }
  if (await exists(resolved.target)) {
    if (!options.overwrite) {
      throw new Error(`target already exists; pass --overwrite only after explicit authorization: ${resolved.lexical}`);
    }
  }
  const templatePath = resolve(siteRoot, 'standards/templates', resolved.type.template);
  const scaffold = extractScaffold(await readFile(templatePath, 'utf8'));
  const pageContent = renderPage(scaffold, options);
  const mapSource = await readFile(mapPath, 'utf8');
  parseChangeMap(mapSource);
  const mapChange = resolved.mappingSupplied ? mergeChangeMap(mapSource, options) : null;
  const summary = {
    dryRun: options.dryRun,
    page: resolved.lexical,
    docType: options.type,
    title: options.title,
    lastVerifiedVersion: 'unverified',
    changeMapDelta: mapChange?.delta ?? null
  };
  if (options.dryRun) return summary;

  await validateTargetRealPath(resolved.target, siteRoot);
  if (resolved.mappingSupplied) {
    await validateTargetRealPath(mapPath, siteRoot, '--change-map-target');
    if ((await lstat(mapPath)).isSymbolicLink()) {
      throw new Error('change-map file must not be a symbolic link');
    }
    for (const mapTarget of options.changeMapTargets) {
      const absoluteTarget = resolve(repoRoot, mapTarget);
      await validateTargetRealPath(absoluteTarget, siteRoot, '--change-map-target');
      if (await exists(absoluteTarget)) {
        const stats = await lstat(absoluteTarget);
        if (!stats.isFile()) {
          throw new Error('--change-map-target must resolve to a regular Markdown file when it exists');
        }
      }
    }
  }
  const rollbackDirectories = await missingParentDirectories(resolved.target, siteRoot);
  const changes = [{ path: resolved.target, content: pageContent }];
  if (mapChange) changes.push({ path: mapPath, content: mapChange.output });
  await atomicWrite(changes, async () => {
    const writtenPage = matter(await readFile(resolved.target, 'utf8'));
    const errors = validatePage({ data: writtenPage.data });
    if (errors.length) throw new Error(`written page frontmatter is invalid: ${errors.join('; ')}`);
    parseChangeMap(await readFile(mapPath, 'utf8'));
    await runDocsChecks(siteRoot);
  }, rollbackDirectories);
  return summary;
}

async function main() {
  const summary = await scaffoldDocument(parseArgs(process.argv.slice(2)));
  console.log(JSON.stringify(summary, null, 2));
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
