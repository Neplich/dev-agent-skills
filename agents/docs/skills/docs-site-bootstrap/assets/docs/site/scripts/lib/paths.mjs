import { dirname, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { mkdir, readFile, writeFile } from 'node:fs/promises';

const LIB_DIR = dirname(fileURLToPath(import.meta.url));
export const SITE_ROOT = resolve(LIB_DIR, '../..');
export const REPO_ROOT = resolve(SITE_ROOT, '../..');
export const GENERATED_ROOT = resolve(SITE_ROOT, '.generated');
export const NAV_ROOT = resolve(GENERATED_ROOT, '.navigation');

export const toPosix = (value) => value.split(sep).join('/');
export const repoRelative = (value) => toPosix(relative(REPO_ROOT, value));

export async function readText(path) {
  return readFile(path, 'utf8');
}

export async function writeText(path, content) {
  await mkdir(dirname(path), { recursive: true });
  await writeFile(path, content, 'utf8');
}
