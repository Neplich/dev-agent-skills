import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readText, REPO_ROOT, SITE_ROOT } from './lib/paths.mjs';

const exec = promisify(execFile);

function explicitVersion(argv) {
  let requested = null;
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] !== '--version') throw new Error(`Unknown argument: ${argv[index]}`);
    if (requested !== null) throw new Error('--version may be provided only once');
    if (!argv[index + 1]) throw new Error('--version requires a value');
    requested = argv[index + 1];
    index += 1;
  }
  return requested ?? process.env.RELEASE_VERSION ?? null;
}

async function versionAnchor(requested) {
  if (requested) return { value: requested, source: 'explicit' };
  try {
    const { stdout } = await exec('git', ['describe', '--tags', '--exact-match', 'HEAD'], {
      cwd: REPO_ROOT
    });
    return { value: stdout.trim(), source: 'git-tag' };
  } catch {
    return { value: null, source: 'unavailable' };
  }
}

export async function checkVersion({ requested = null } = {}) {
  const path = resolve(SITE_ROOT, '.meta/releases.json');
  const data = JSON.parse(await readText(path));
  const errors = [];
  if (!(data.latest === null || typeof data.latest === 'string')) {
    errors.push('latest must be null or a string');
  }
  if (!Array.isArray(data.released) || data.released.some((item) => typeof item !== 'string')) {
    errors.push('released must be a string array');
  }
  if (!data.verifiedDocs || typeof data.verifiedDocs !== 'object' || Array.isArray(data.verifiedDocs)) {
    errors.push('verifiedDocs must be an object');
  }
  const released = Array.isArray(data.released) ? data.released : [];
  if (data.latest === null && released.length) errors.push('latest cannot be null when released is non-empty');
  if (data.latest !== null && !released.includes(data.latest)) errors.push('latest must appear in released');
  if (data.latest !== null && released.at(-1) !== data.latest) errors.push('latest must be the final released entry');
  for (const [pathKey, version] of Object.entries(data.verifiedDocs ?? {})) {
    if (typeof version !== 'string' || !released.includes(version)) {
      errors.push(`verifiedDocs entry ${pathKey} must reference a released version`);
    }
  }
  const anchor = await versionAnchor(requested);
  if (anchor.value && data.latest !== anchor.value) {
    errors.push(`latest ${String(data.latest)} does not match ${anchor.source} ${anchor.value}`);
  }
  return { errors, anchor };
}

async function main() {
  const requested = explicitVersion(process.argv.slice(2));
  const result = await checkVersion({ requested });
  if (!result.anchor.value) {
    console.log('Version anchor unavailable; checked release metadata consistency only.');
  }
  for (const error of result.errors) console.error(`- ${error}`);
  if (result.errors.length) process.exitCode = 1;
  else console.log('Version metadata check passed.');
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
