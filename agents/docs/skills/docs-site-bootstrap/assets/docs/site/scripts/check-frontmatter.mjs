import { fileURLToPath } from 'node:url';
import { collectFrontmatterFailures } from './lib/frontmatter.mjs';

function parseArgs(argv) {
  const allowed = new Set(['--version-anchor-unavailable']);
  const unknown = argv.find((value) => !allowed.has(value));
  if (unknown) throw new Error(`Unknown argument: ${unknown}`);
  return {
    anchorUnavailable: argv.includes('--version-anchor-unavailable')
      || process.env.DOCS_VERSION_ANCHOR === 'unavailable'
  };
}

export async function checkFrontmatter() {
  return collectFrontmatterFailures();
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  const failures = await checkFrontmatter();
  if (options.anchorUnavailable) {
    console.log(
      'version_anchor: unavailable; keep the existing last_verified_version, '
      + 'or use unverified for a new page.'
    );
  }
  for (const failure of failures) {
    console.error(failure.path);
    for (const error of failure.errors) console.error(`  - ${error}`);
  }
  if (failures.length) {
    process.exitCode = 1;
  } else {
    console.log('Frontmatter check passed.');
  }
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
