import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readText, REPO_ROOT, SITE_ROOT } from './lib/paths.mjs';

const exec = promisify(execFile);

export function explicitVersion(argv, environment = process.env) {
  let requested = null;
  for (let index = 0; index < argv.length; index += 1) {
    if (argv[index] !== '--version') throw new Error(`Unknown argument: ${argv[index]}`);
    if (requested !== null) throw new Error('--version may be provided only once');
    if (!argv[index + 1] || argv[index + 1].startsWith('--')) {
      throw new Error('--version requires a value');
    }
    requested = argv[index + 1];
    index += 1;
  }
  const environmentVersion = environment.RELEASE_VERSION;
  if (requested === null && environmentVersion !== undefined
      && (typeof environmentVersion !== 'string' || environmentVersion.trim() === '')) {
    throw new Error('RELEASE_VERSION must be a non-empty string when set');
  }
  return requested ?? environmentVersion ?? null;
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

export function validateReleaseMetadata(data) {
  const errors = [];
  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    return ['release metadata must be an object'];
  }
  if (!(data.latest === null || typeof data.latest === 'string')) {
    errors.push('latest must be null or a string');
  } else if (typeof data.latest === 'string' && data.latest.trim() === '') {
    errors.push('latest must not be an empty string');
  }
  if (!Array.isArray(data.released)
      || data.released.some((item) => typeof item !== 'string' || item.trim() === '')) {
    errors.push('released must be a non-empty string array when entries are present');
  }
  if (!data.verifiedDocs || typeof data.verifiedDocs !== 'object' || Array.isArray(data.verifiedDocs)) {
    errors.push('verifiedDocs must be an object');
  }
  const released = Array.isArray(data.released) ? data.released : [];
  if (new Set(released).size !== released.length) errors.push('released must not contain duplicates');
  if (data.latest === null && released.length) errors.push('latest cannot be null when released is non-empty');
  if (data.latest !== null && !released.includes(data.latest)) errors.push('latest must appear in released');
  if (data.latest !== null && released.at(-1) !== data.latest) errors.push('latest must be the final released entry');
  for (const [pathKey, version] of Object.entries(data.verifiedDocs ?? {})) {
    if (pathKey.trim() === '') errors.push('verifiedDocs keys must be non-empty paths');
    if (typeof version !== 'string' || version.trim() === '' || !released.includes(version)) {
      errors.push(`verifiedDocs entry ${pathKey} must reference a released version`);
    }
  }
  return errors;
}

export async function checkVersion({ requested = null } = {}, dependencies = {}) {
  const readReleaseMetadata = dependencies.readReleaseMetadata
    ?? (() => readText(resolve(SITE_ROOT, '.meta/releases.json')));
  const getVersionAnchor = dependencies.versionAnchor ?? versionAnchor;
  const data = JSON.parse(await readReleaseMetadata());
  const errors = validateReleaseMetadata(data);
  const anchor = await getVersionAnchor(requested);
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
