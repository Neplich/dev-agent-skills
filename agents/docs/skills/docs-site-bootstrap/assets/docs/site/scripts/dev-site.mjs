import { spawn } from 'node:child_process';
import { watch } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { relative } from 'node:path';
import { GENERATED_ROOT, SITE_ROOT, toPosix } from './lib/paths.mjs';
import { prepareSite } from './prepare-site.mjs';

const IGNORED = ['.generated/', '.vitepress/cache/', '.vitepress/dist/', 'node_modules/'];

export function attachChildLifecycle(child, watcher, clearPending, runtimeProcess = process) {
  let closed = false;
  const cleanup = () => {
    if (closed) return;
    closed = true;
    clearPending();
    watcher.close();
    runtimeProcess.removeListener('SIGINT', stop);
    runtimeProcess.removeListener('SIGTERM', stop);
  };
  const stop = () => {
    cleanup();
    child.kill('SIGTERM');
  };
  child.once('close', (code) => {
    cleanup();
    if (typeof code === 'number') runtimeProcess.exitCode = code;
  });
  runtimeProcess.once('SIGINT', stop);
  runtimeProcess.once('SIGTERM', stop);
}

export async function devSite(target, extraArgs = []) {
  if (!['public', 'internal'].includes(target)) throw new Error('Target must be public or internal');
  await prepareSite(target);
  const command = process.platform === 'win32' ? 'npx.cmd' : 'npx';
  const child = spawn(command, ['vitepress', 'dev', `${GENERATED_ROOT}/${target}`, ...extraArgs], {
    cwd: SITE_ROOT,
    stdio: 'inherit'
  });
  let timer;
  const watcher = watch(SITE_ROOT, { recursive: true }, (_event, filename) => {
    if (!filename) return;
    const path = toPosix(relative(SITE_ROOT, `${SITE_ROOT}/${filename}`));
    if (IGNORED.some((prefix) => path.startsWith(prefix))) return;
    if (!/\.(md|ya?ml)$/i.test(path)) return;
    clearTimeout(timer);
    timer = setTimeout(() => {
      prepareSite(target).catch((error) => console.error(`Prepare failed: ${error.message}`));
    }, 120);
  });
  attachChildLifecycle(child, watcher, () => clearTimeout(timer));
  return child;
}

if (fileURLToPath(import.meta.url) === process.argv[1]) {
  const [target, ...args] = process.argv.slice(2);
  devSite(target, args).catch((error) => {
    console.error(error instanceof Error ? error.message : error);
    process.exitCode = 1;
  });
}
