import { spawn } from 'node:child_process';
import { watch } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { relative, resolve } from 'node:path';
import { GENERATED_ROOT, SITE_ROOT, toPosix } from './lib/paths.mjs';
import { prepareSite } from './prepare-site.mjs';

const IGNORED = ['.generated/', '.vitepress/cache/', '.vitepress/dist/', 'node_modules/'];

export function shouldPrepareForChange(path) {
  if (IGNORED.some((prefix) => path.startsWith(prefix))) return false;
  return path.startsWith('.vitepress/') || path.startsWith('public/')
    || /\.(md|ya?ml)$/i.test(path);
}

export function attachChildLifecycle(
  child, watcher, clearPending, runtimeProcess = process,
  reportError = (error) => console.error(error instanceof Error ? error.message : error)
) {
  let cleaned = false;
  let settled = false;
  let cleanupFailed = false;
  const cleanup = () => {
    if (cleaned) return;
    cleaned = true;
    for (const release of [clearPending, () => watcher.close()]) {
      try {
        release();
      } catch (error) {
        reportError(error);
        cleanupFailed = true;
      }
    }
    runtimeProcess.removeListener('SIGINT', stopInterrupt);
    runtimeProcess.removeListener('SIGTERM', stopTerminate);
    watcher.removeListener?.('error', watcherFailed);
  };
  const finish = (code, error = null) => {
    if (settled) return;
    settled = true;
    cleanup();
    if (error) reportError(error);
    runtimeProcess.exitCode = error || cleanupFailed
      ? 1 : (typeof code === 'number' ? code : 1);
  };
  const stop = (signal, exitCode) => {
    if (settled) return;
    settled = true;
    cleanup();
    runtimeProcess.exitCode = exitCode;
    try {
      child.kill(signal);
    } catch (error) {
      reportError(error);
      runtimeProcess.exitCode = 1;
    }
  };
  const stopInterrupt = () => stop('SIGINT', 130);
  const stopTerminate = () => stop('SIGTERM', 143);
  const watcherFailed = (error) => {
    finish(null, error);
    try {
      child.kill('SIGTERM');
    } catch (killError) {
      reportError(killError);
    }
  };
  child.once('error', (error) => finish(null, error));
  child.once('close', (code) => finish(code));
  watcher.once?.('error', watcherFailed);
  runtimeProcess.once('SIGINT', stopInterrupt);
  runtimeProcess.once('SIGTERM', stopTerminate);
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
  let watcher;
  try {
    watcher = watch(SITE_ROOT, { recursive: true }, (_event, filename) => {
      if (!filename) return;
      const path = toPosix(relative(SITE_ROOT, resolve(SITE_ROOT, filename)));
      if (!shouldPrepareForChange(path)) return;
      clearTimeout(timer);
      timer = setTimeout(() => {
        prepareSite(target).catch((error) => console.error(`Prepare failed: ${error.message}`));
      }, 120);
    });
  } catch (error) {
    child.kill('SIGTERM');
    throw error;
  }
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
