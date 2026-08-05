import { execFile } from 'node:child_process';
import { lstat, realpath } from 'node:fs/promises';
import { promisify } from 'node:util';
import { isAbsolute, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import picomatch from 'picomatch';
import YAML from 'yaml';
import { checkFrontmatter } from './check-frontmatter.mjs';
import { readText, REPO_ROOT, SITE_ROOT, toPosix } from './lib/paths.mjs';

const exec = promisify(execFile);
const MAP_PATH = resolve(SITE_ROOT, 'standards/change-map.yaml');

export function parseArgs(argv) {
  const result = { strict: false, base: null };
  let strictSeen = false;
  let baseSeen = false;
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] === '--strict') {
      if (strictSeen) throw new Error('--strict may be provided only once');
      strictSeen = true;
      result.strict = true;
    } else if (argv[index] === '--base') {
      if (baseSeen) throw new Error('--base may be provided only once');
      baseSeen = true;
      const value = argv[index + 1];
      if (!value || value.startsWith('--')) throw new Error('--base requires a git ref');
      result.base = value;
      index += 1;
    }
    else throw new Error(`Unknown argument: ${argv[index]}`);
  }
  return result;
}

async function git(args) {
  const { stdout } = await exec('git', args, { cwd: REPO_ROOT });
  return stdout;
}

export function parseGitPaths(output) {
  return output.split('\0').map((item) => toPosix(item)).filter(Boolean);
}

async function refExists(ref, runGit) {
  try {
    await runGit(['rev-parse', '--verify', '--quiet', `${ref}^{commit}`]);
    return true;
  } catch {
    return false;
  }
}

export async function inferCommittedBase(
  { runGit = git, environment = process.env } = {}
) {
  const candidates = [
    environment.GITHUB_BASE_SHA,
    environment.CI_MERGE_REQUEST_DIFF_BASE_SHA,
    environment.GITHUB_BASE_REF && `origin/${environment.GITHUB_BASE_REF}`,
    environment.GITHUB_BASE_REF,
    environment.CI_MERGE_REQUEST_TARGET_BRANCH_NAME
      && `origin/${environment.CI_MERGE_REQUEST_TARGET_BRANCH_NAME}`,
    environment.CHANGE_TARGET && `origin/${environment.CHANGE_TARGET}`
  ].filter(Boolean);
  try {
    const remoteHead = (await runGit([
      'symbolic-ref', '--quiet', '--short', 'refs/remotes/origin/HEAD'
    ])).trim();
    if (remoteHead) candidates.push(remoteHead);
  } catch {
    // A local or shallow checkout may not have an origin/HEAD symbolic ref.
  }
  candidates.push('HEAD^1');
  for (const candidate of [...new Set(candidates)]) {
    if (await refExists(candidate, runGit)) return candidate;
  }
  return null;
}

export async function changedFiles(
  base, { strict = false, runGit = git, environment = process.env } = {}
) {
  const committedBase = base ?? (strict
    ? await inferCommittedBase({ runGit, environment })
    : null);
  if (strict && !committedBase) {
    throw new Error('strict affected check could not determine a committed base');
  }
  if (committedBase) {
    const mergeBase = (await runGit(['merge-base', committedBase, 'HEAD'])).trim();
    const committed = parseGitPaths(await runGit([
      'diff', '--name-only', '-z', `${mergeBase}...HEAD`
    ]));
    const working = parseGitPaths(await runGit(['diff', '--name-only', '-z', 'HEAD']));
    const untracked = parseGitPaths(await runGit([
      'ls-files', '--others', '--exclude-standard', '-z'
    ]));
    return [...new Set([...committed, ...working, ...untracked])].sort();
  }
  const unstaged = parseGitPaths(await runGit(['diff', '--name-only', '-z']));
  const staged = parseGitPaths(await runGit(['diff', '--name-only', '--cached', '-z']));
  const untracked = parseGitPaths(await runGit([
    'ls-files', '--others', '--exclude-standard', '-z'
  ]));
  return [...new Set([...unstaged, ...staged, ...untracked])].sort();
}

function matches(path, glob, excludes = []) {
  return picomatch(glob, { dot: true })(path)
    && !excludes.some((pattern) => picomatch(pattern, { dot: true })(path));
}

function repoRelativeGlob(value, label) {
  if (typeof value !== 'string' || value.trim() === '' || value !== value.trim()
      || value.includes('\\') || value.startsWith('/') || /^[A-Za-z]:\//.test(value)
      || value.split('/').includes('..')) {
    throw new Error(`${label} must be repository-root relative`);
  }
}

function requiredDocPath(value, label) {
  repoRelativeGlob(value, label);
  const segments = value.split('/');
  if (!value.startsWith('docs/site/') || !value.endsWith('.md')
      || segments.some((segment) => segment === '' || segment.startsWith('.'))) {
    throw new Error(`${label} must be a Markdown page under docs/site/`);
  }
}

function stringArray(value, label, { nonEmpty = false } = {}) {
  if (!Array.isArray(value) || (nonEmpty && value.length === 0)
      || value.some((item) => typeof item !== 'string' || item.trim() === '')) {
    throw new Error(`${label} must be ${nonEmpty ? 'a non-empty' : 'a'} string array`);
  }
  if (new Set(value).size !== value.length) throw new Error(`${label} must not contain duplicates`);
}

export function validateChangeMap(raw) {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)
      || !Object.hasOwn(raw, 'change_map')) {
    throw new Error('change_map is required and must be a mapping');
  }
  const map = raw.change_map;
  if (!map || typeof map !== 'object' || Array.isArray(map)) {
    throw new Error('change_map must be a mapping');
  }
  for (const [codeGlob, rule] of Object.entries(map)) {
    repoRelativeGlob(codeGlob, `change_map key ${JSON.stringify(codeGlob)}`);
    if (!rule || typeof rule !== 'object' || Array.isArray(rule)) {
      throw new Error(`change_map entry ${codeGlob} must be a mapping`);
    }
    stringArray(rule.required_docs, `change_map entry ${codeGlob} required_docs`, { nonEmpty: true });
    for (const path of rule.required_docs) requiredDocPath(path, `change_map entry ${codeGlob} required_docs item`);
    if (typeof rule.trigger !== 'string' || rule.trigger.trim() === '') {
      throw new Error(`change_map entry ${codeGlob} trigger must be a non-empty string`);
    }
    if (rule.exclude !== undefined) {
      stringArray(rule.exclude, `change_map entry ${codeGlob} exclude`);
      for (const pattern of rule.exclude) repoRelativeGlob(pattern, `change_map entry ${codeGlob} exclude item`);
    }
  }
  return map;
}

export async function requiredDocExists(
  path, { repoRoot = REPO_ROOT, siteRoot = SITE_ROOT } = {}
) {
  try {
    const candidate = resolve(repoRoot, path);
    if (!(await lstat(candidate)).isFile()) return false;
    const realSiteRoot = await realpath(siteRoot);
    const source = await realpath(candidate);
    const realRelative = toPosix(relative(realSiteRoot, source));
    return realRelative !== '..' && !realRelative.startsWith('../')
      && !isAbsolute(realRelative) && realRelative !== '';
  } catch {
    return false;
  }
}

export async function checkAffected({ base = null, strict = false } = {}, dependencies = {}) {
  const runFrontmatterCheck = dependencies.checkFrontmatter ?? checkFrontmatter;
  const readChangeMap = dependencies.readChangeMap ?? (() => readText(MAP_PATH));
  const getChangedFiles = dependencies.changedFiles ?? changedFiles;
  const docExists = dependencies.requiredDocExists ?? requiredDocExists;
  const frontmatterFailures = await runFrontmatterCheck();
  if (frontmatterFailures.length) {
    return { blocked: true, frontmatterFailures, changed: [], suspects: [] };
  }
  const map = validateChangeMap(YAML.parse(await readChangeMap()));
  const changed = await getChangedFiles(base, { strict });
  const changedSet = new Set(changed);
  const suspects = [];
  for (const [codeGlob, rule] of Object.entries(map)) {
    const codeMatches = changed.filter((path) => matches(path, codeGlob, rule.exclude ?? []));
    if (!codeMatches.length) continue;
    const missingDocs = [];
    for (const path of rule.required_docs ?? []) {
      if (!changedSet.has(path) || !(await docExists(path))) missingDocs.push(path);
    }
    if (missingDocs.length) {
      suspects.push({ codeGlob, trigger: rule.trigger ?? '', codeMatches, missingDocs });
    }
  }
  return { blocked: strict && suspects.length > 0, frontmatterFailures: [], changed, suspects };
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const result = await checkAffected(options);
  for (const suspect of result.suspects) {
    console.warn(`suspect: ${suspect.codeGlob}`);
    console.warn(`  changed code: ${suspect.codeMatches.join(', ')}`);
    console.warn(`  required docs not changed: ${suspect.missingDocs.join(', ')}`);
    if (suspect.trigger) console.warn(`  trigger: ${suspect.trigger}`);
  }
  if (!result.suspects.length) console.log('No affected-document suspects found.');
  if (result.frontmatterFailures.length) console.error('Frontmatter is invalid; affected check blocked.');
  if (result.blocked) process.exitCode = 1;
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
