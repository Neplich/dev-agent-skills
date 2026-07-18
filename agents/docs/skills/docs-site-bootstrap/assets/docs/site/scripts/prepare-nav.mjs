import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { collectMarkdown } from './lib/pages.mjs';
import { buildSidebar, renderSidebar } from './lib/sidebar.mjs';
import { NAV_ROOT, SITE_ROOT, validatePathInside, writeText } from './lib/paths.mjs';

export async function prepareNav() {
  await validatePathInside(NAV_ROOT, SITE_ROOT, '.generated navigation');
  const pages = await collectMarkdown({ includeHomes: false });
  for (const target of ['public', 'internal']) {
    const sidebar = buildSidebar(pages, target);
    await writeText(
      resolve(NAV_ROOT, `sidebar.${target}.mjs`),
      renderSidebar(sidebar)
    );
  }
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  prepareNav().then(() => console.log('Navigation prepared.')).catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
