# Export and Share Capture

## Runtime Preconditions

- Run this Playwright Test snippet only inside the isolated eval scratch workspace.
- Set `MANUAL_EVAL_ARTIFACT_DIR` to that scratch workspace's screenshot directory.
- Do not print, persist, or copy the generated share URL; its pako payload is eval-sensitive evidence.

## Playwright Test Snippet

```ts
import { expect, test } from '@playwright/test';
import path from 'node:path';

const artifactDir = process.env.MANUAL_EVAL_ARTIFACT_DIR!;

test.use({
  viewport: { width: 1920, height: 1080 },
  deviceScaleFactor: 1,
  colorScheme: 'light',
  acceptDownloads: true,
});

test('capture export and share evidence without exposing payload', async ({ page }) => {
  await page.goto('https://mermaid.live/', { waitUntil: 'networkidle' });

  const actualViewport = await page.evaluate(() => ({
    width: window.innerWidth,
    height: window.innerHeight,
  }));
  expect(actualViewport).toEqual({ width: 1920, height: 1080 });

  const temporaryOverlays = page.getByRole('dialog').filter({
    hasText: /promot|upgrade|newsletter|translate|welcome/i,
  });
  for (const overlay of await temporaryOverlays.all()) {
    const close = overlay.getByRole('button', { name: /close|dismiss|not now|×/i });
    if (await close.isVisible()) await close.click();
  }

  const exportControl = page.getByRole('button', { name: /export/i }).first();
  await expect(exportControl).toBeVisible();
  await exportControl.click();
  const exportSurface = page.getByRole('menu').or(page.getByRole('dialog')).filter({
    hasText: /png|svg|export/i,
  }).first();
  await expect(exportSurface).toBeVisible();
  await page.screenshot({
    path: path.join(artifactDir, 'step-1-open-export-options.png'),
    animations: 'disabled',
  });
  await page.keyboard.press('Escape');

  const shareControl = page.getByRole('button', { name: /share/i }).first();
  await expect(shareControl).toBeVisible();
  await shareControl.click();
  const shareSurface = page.getByRole('dialog').filter({ hasText: /share|link/i }).first();
  await expect(shareSurface).toBeVisible();
  await expect(shareSurface.locator('input, textarea, a[href]').first()).toBeVisible();

  await shareSurface.locator('input, textarea, a[href]').evaluateAll((nodes) => {
    for (const node of nodes) {
      const element = node as HTMLElement;
      element.style.filter = 'blur(12px)';
      element.setAttribute('data-eval-redacted', 'true');
    }
  });
  await page.screenshot({
    path: path.join(artifactDir, 'step-2-review-share-action.png'),
    animations: 'disabled',
  });
});
```

## Evidence Notes

- The snippet verifies that a share value exists without reading or logging its contents.
- Link-bearing elements are visually redacted before capture; durable manual text should describe the share action semantically.
- Screenshot files and generated share data are runtime artifacts and must not be copied back into this fixture.
