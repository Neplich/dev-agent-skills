import { execFile } from 'node:child_process';
import { access } from 'node:fs/promises';
import { promisify } from 'node:util';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import picomatch from 'picomatch';
import YAML from 'yaml';
import { checkFrontmatter } from './check-frontmatter.mjs';
import { readText, REPO_ROOT, SITE_ROOT, toPosix } from './lib/paths.mjs';

const exec = promisify(execFile);
const MAP_PATH = resolve(SITE_ROOT, 'standards/change-map.yaml');

function parseArgs(argv) {
  const result = { strict: false, base: null };
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] === '--strict') result.strict = true;
    else if (argv[index] === '--base') result.base = argv[++index];
    else throw new Error(`Unknown argument: ${argv[index]}`);
  }
  if (result.base === undefined) throw new Error('--base requires a git ref');
  return result;
}

async function git(args) {
  const { stdout } = await exec('git', args, { cwd: REPO_ROOT });
  return stdout;
}

function parseNameOnly(output) {
  return output.split('\n').map((item) => toPosix(item.trim())).filter(Boolean);
}

async function changedFiles(base) {
  if (base) {
    const mergeBase = (await git(['merge-base', base, 'HEAD'])).trim();
    const committed = parseNameOnly(await git(['diff', '--name-only', `${mergeBase}...HEAD`]));
    const working = parseNameOnly(await git(['diff', '--name-only', 'HEAD']));
    const untracked = parseNameOnly(await git(['ls-files', '--others', '--exclude-standard']));
    return [...new Set([...committed, ...working, ...untracked])].sort();
  }
  const unstaged = parseNameOnly(await git(['diff', '--name-only']));
  const staged = parseNameOnly(await git(['diff', '--name-only', '--cached']));
  const untracked = parseNameOnly(await git(['ls-files', '--others', '--exclude-standard']));
  return [...new Set([...unstaged, ...staged, ...untracked])].sort();
}

function matches(path, glob, excludes = []) {
  return picomatch(glob, { dot: true })(path)
    && !excludes.some((pattern) => picomatch(pattern, { dot: true })(path));
}

async function requiredDocExists(path) {
  try {
    await access(resolve(REPO_ROOT, path));
    return true;
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
  const raw = YAML.parse(await readChangeMap()) ?? {};
  const map = raw.change_map ?? {};
  if (typeof map !== 'object' || Array.isArray(map)) {
    throw new Error('change_map must be a mapping');
  }
  const changed = await getChangedFiles(base);
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
