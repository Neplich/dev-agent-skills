import { resolve } from 'node:path';
import fg from 'fast-glob';
import matter from 'gray-matter';
import { readText, SITE_ROOT, toPosix } from './paths.mjs';

export const VISIBILITIES = new Set(['public', 'internal', 'both']);
export const DOC_TYPES = new Set([
  'landing', 'release', 'design', 'api', 'database', 'ops', 'product', 'manual'
]);
export const STAGES = new Set(['draft', 'dev', 'ops', 'release']);
export const SECTION_ORDER = [
  'standards', 'product', 'manual', 'design', 'api', 'database', 'ops', 'release-notes'
];
export const IGNORE_GLOBS = [
  '**/.meta/**', '**/.generated/**', '**/.vitepress/cache/**',
  '**/.vitepress/dist/**', '**/node_modules/**'
];
export const HOME_NAVIGATION_MARKER = '<!-- docs-site-navigation -->';

export async function readNavigation(target, { siteRoot = SITE_ROOT } = {}) {
  if (!['public', 'internal'].includes(target)) {
    throw new Error('navigation target must be public or internal');
  }
  const source = await readText(resolve(siteRoot, `.vitepress/navigation.${target}.json`));
  const entries = JSON.parse(source);
  if (!Array.isArray(entries) || entries.length === 0) {
    throw new Error(`navigation.${target} must be a non-empty array`);
  }
  for (const [index, entry] of entries.entries()) {
    if (!entry || typeof entry.text !== 'string' || !entry.text.trim()
      || typeof entry.link !== 'string' || !/^\/[\w/-]*\/$/.test(entry.link)) {
      throw new Error(`navigation.${target}[${index}] must define text and a root-relative link`);
    }
  }
  return entries;
}

export function renderHomeNavigation(source, entries) {
  const markerCount = source.split(HOME_NAVIGATION_MARKER).length - 1;
  if (markerCount !== 1) {
    throw new Error(`home page must contain exactly one ${HOME_NAVIGATION_MARKER} marker`);
  }
  const list = entries.map(({ text, link }) => `- [${text}](${link})`).join('\n');
  return source.replace(HOME_NAVIGATION_MARKER, list);
}

export function routeFor(relativePath) {
  const value = toPosix(relativePath).replace(/\.md$/i, '');
  if (value.endsWith('/index')) return `/${value.slice(0, -6)}/`;
  return value === 'index' ? '/' : `/${value}`;
}

export function visibleFor(visibility, target) {
  if (target === 'public') return visibility === 'public' || visibility === 'both';
  if (target === 'internal') return VISIBILITIES.has(visibility);
  throw new Error(`Unsupported site target: ${target}`);
}

export async function collectMarkdown({ includeHomes = true, siteRoot = SITE_ROOT } = {}) {
  const patterns = includeHomes
    ? ['**/*.md']
    : SECTION_ORDER.map((section) => `${section}/**/*.md`);
  const entries = await fg(patterns, {
    cwd: siteRoot,
    onlyFiles: true,
    followSymbolicLinks: false,
    dot: true,
    ignore: IGNORE_GLOBS
  });
  const pages = [];
  for (const relativePath of entries.sort()) {
    const source = await readText(resolve(siteRoot, relativePath));
    const parsed = matter(source);
    pages.push({
      relativePath: toPosix(relativePath),
      absolutePath: resolve(siteRoot, relativePath),
      source,
      data: parsed.data ?? {},
      content: parsed.content,
      route: routeFor(relativePath)
    });
  }
  return pages;
}
