import { cp, mkdir, realpath, rm, stat } from 'node:fs/promises';
import { dirname, isAbsolute, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import fg from 'fast-glob';
import { collectMarkdown, visibleFor } from './lib/pages.mjs';
import { GENERATED_ROOT, NAV_ROOT, SITE_ROOT, readText, writeText } from './lib/paths.mjs';
import { prepareNav } from './prepare-nav.mjs';

const TARGETS = new Set(['public', 'internal']);
const MARKDOWN_REFERENCE = /!?\[[^\]]*\]\(\s*(<[^>\n]+>|[^)\s]+)(?:\s+(?:"[^"]*"|'[^']*'|\([^)]*\)))?\s*\)/g;
const HTML_REFERENCE = /\b(?:src|href)\s*=\s*(["'])(.*?)\1/gi;
const EXCLUDED_SEGMENTS = new Set(['.meta', '.vitepress', 'node_modules', '.generated']);

function directReferences(source) {
  const references = new Set();
  for (const match of source.matchAll(MARKDOWN_REFERENCE)) {
    const reference = match[1];
    references.add(reference.startsWith('<') ? reference.slice(1, -1) : reference);
  }
  for (const match of source.matchAll(HTML_REFERENCE)) references.add(match[2]);
  return references;
}

function excludedAsset(relativePath) {
  const segments = relativePath.split('/');
  return relativePath === 'standards/change-map.yaml'
    || segments.some((segment) => EXCLUDED_SEGMENTS.has(segment));
}

function warnSkippedAsset(page, reference, reason) {
  console.warn(`Skipped asset reference "${reference}" from "${page}": ${reason}.`);
}

async function referencedAssets(pages) {
  const siteRoot = await realpath(SITE_ROOT);
  const assets = new Map();
  for (const page of pages) {
    for (const rawReference of directReferences(page.source)) {
      const reference = rawReference.trim();
      if (!reference || reference.startsWith('#') || reference.startsWith('/')
        || /^https?:\/\//i.test(reference) || /^mailto:/i.test(reference)) continue;
      const pathOnly = reference.split(/[?#]/, 1)[0];
      if (/\.md$/i.test(pathOnly)) continue;
      let decodedPath;
      try {
        decodedPath = decodeURIComponent(pathOnly);
      } catch {
        warnSkippedAsset(page.relativePath, reference, 'invalid URL encoding');
        continue;
      }
      const candidate = resolve(SITE_ROOT, dirname(page.relativePath), decodedPath);
      const lexicalRelative = relative(SITE_ROOT, candidate).replaceAll('\\', '/');
      if (!lexicalRelative || lexicalRelative === '..' || lexicalRelative.startsWith('../')
        || isAbsolute(lexicalRelative)) {
        warnSkippedAsset(page.relativePath, reference, 'path is outside docs/site');
        continue;
      }
      if (excludedAsset(lexicalRelative)) {
        warnSkippedAsset(page.relativePath, reference, 'path is in an excluded area');
        continue;
      }
      try {
        const source = await realpath(candidate);
        const realRelative = relative(siteRoot, source).replaceAll('\\', '/');
        if (!realRelative || realRelative === '..' || realRelative.startsWith('../')
          || isAbsolute(realRelative)) {
          warnSkippedAsset(page.relativePath, reference, 'resolved path is outside docs/site');
          continue;
        }
        if (excludedAsset(realRelative)) {
          warnSkippedAsset(page.relativePath, reference, 'resolved path is in an excluded area');
          continue;
        }
        if (!(await stat(source)).isFile()) {
          warnSkippedAsset(page.relativePath, reference, 'resolved path is not a file');
          continue;
        }
        assets.set(lexicalRelative, source);
      } catch {
        warnSkippedAsset(page.relativePath, reference, 'file does not exist');
      }
    }
  }
  return assets;
}

export async function prepareSite(target) {
  if (!TARGETS.has(target)) throw new Error('Target must be public or internal');
  await prepareNav();
  const output = resolve(GENERATED_ROOT, target);
  await rm(output, { recursive: true, force: true });
  await mkdir(output, { recursive: true });

  const includedPages = [];
  for (const page of await collectMarkdown()) {
    if (page.relativePath === 'index.public.md' || page.relativePath === 'index.internal.md') continue;
    if (!visibleFor(page.data.visibility, target)) continue;
    await writeText(resolve(output, page.relativePath), page.source);
    includedPages.push(page);
  }
  const home = resolve(SITE_ROOT, `index.${target}.md`);
  const homeSource = await readText(home);
  await writeText(resolve(output, 'index.md'), homeSource);
  includedPages.push({ relativePath: `index.${target}.md`, source: homeSource });

  const publicAssets = await fg(['public/**'], {
    cwd: SITE_ROOT,
    onlyFiles: true,
    dot: true,
    ignore: [
      '**/.meta/**', '**/.generated/**', '**/node_modules/**', '**/.vitepress/**'
    ]
  });
  const referenced = await referencedAssets(includedPages);
  const vitepressAssets = await fg([
    '.vitepress/config.shared.ts', `.vitepress/config.${target}.ts`,
    '.vitepress/theme/**'
  ], {
    cwd: SITE_ROOT,
    onlyFiles: true,
    dot: true,
    ignore: ['**/.meta/**', '**/.generated/**', '**/node_modules/**']
  });
  for (const asset of new Set([...publicAssets, ...referenced.keys(), ...vitepressAssets])) {
    const destination = resolve(output, asset);
    await mkdir(dirname(destination), { recursive: true });
    await cp(referenced.get(asset) ?? resolve(SITE_ROOT, asset), destination);
  }
  await mkdir(resolve(output, '.vitepress/generated'), { recursive: true });
  await cp(
    resolve(NAV_ROOT, `sidebar.${target}.mjs`),
    resolve(output, `.vitepress/generated/sidebar.${target}.mjs`)
  );
  await writeText(
    resolve(output, '.vitepress/config.mts'),
    `export { default } from './config.${target}';\n`
  );
  return output;
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  const target = process.argv[2];
  prepareSite(target).then((output) => {
    console.log(`Prepared ${target} site at ${output}.`);
  }).catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
