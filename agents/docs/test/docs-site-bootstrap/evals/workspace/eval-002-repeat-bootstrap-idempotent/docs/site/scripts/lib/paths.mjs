import { dirname, isAbsolute, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { randomUUID } from 'node:crypto';
import { lstat, mkdir, readFile, realpath, rename, rm, writeFile } from 'node:fs/promises';

const LIB_DIR = dirname(fileURLToPath(import.meta.url));
export const SITE_ROOT = resolve(LIB_DIR, '../..');
export const REPO_ROOT = resolve(SITE_ROOT, '../..');
export const GENERATED_ROOT = resolve(SITE_ROOT, '.generated');
export const NAV_ROOT = resolve(GENERATED_ROOT, '.navigation');

export const toPosix = (value) => value.split(sep).join('/');
export const repoRelative = (value) => toPosix(relative(REPO_ROOT, value));

async function exists(path) {
  try {
    await lstat(path);
    return true;
  } catch (error) {
    if (error?.code === 'ENOENT') return false;
    throw error;
  }
}

export async function validatePathInside(target, root, label) {
  const realRoot = await realpath(root);
  let existing = target;
  while (!(await exists(existing))) {
    const parent = dirname(existing);
    if (parent === existing) throw new Error(`${label} has no existing parent`);
    existing = parent;
  }
  const realExisting = await realpath(existing);
  const relativeExisting = toPosix(relative(realRoot, realExisting));
  if (relativeExisting === '..' || relativeExisting.startsWith('../')
      || isAbsolute(relativeExisting)) {
    throw new Error(`${label} must not escape docs/site through a symbolic link`);
  }
}

export async function readText(path) {
  return readFile(path, 'utf8');
}

export async function writeText(path, content) {
  await mkdir(dirname(path), { recursive: true });
  const temporary = `${path}.docs-write-${randomUUID()}.tmp`;
  try {
    await writeFile(temporary, content, 'utf8');
    await rename(temporary, path);
  } catch (error) {
    try {
      await rm(temporary, { force: true });
    } catch (cleanupError) {
      throw new AggregateError([error, cleanupError], 'write failed and temporary cleanup failed', {
        cause: error
      });
    }
    throw error;
  }
}
