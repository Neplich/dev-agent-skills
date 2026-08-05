# Basic Editing and Preview Capture

## Runtime Preconditions

- Run this Playwright Test snippet only inside the isolated eval scratch workspace.
- Set `MANUAL_EVAL_ARTIFACT_DIR` to that scratch workspace's screenshot directory.
- The fixture requires anonymous access to `https://mermaid.live/`; it contains no credentials.

## Playwright Test Snippet

```ts
import { expect, test } from '@playwright/test';
import path from 'node:path';

const artifactDir = process.env.MANUAL_EVAL_ARTIFACT_DIR!;

test.use({
  viewport: { width: 1920, height: 1080 },
  deviceScaleFactor: 1,
  colorScheme: 'light',
});

test('capture anonymous editing and preview evidence', async ({ page }) => {
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

  const editor = page.locator('.cm-editor').first();
  await expect(editor).toBeVisible();
  await editor.click();
  await page.keyboard.press(process.platform === 'darwin' ? 'Meta+A' : 'Control+A');
  await page.keyboard.type('flowchart LR\n  Start --> Review\n  Review --> Done');

  const renderedDiagram = page.locator('svg').filter({ has: page.locator('g') }).last();
  await expect(renderedDiagram).toBeVisible();

  await page.screenshot({
    path: path.join(artifactDir, 'step-1-edit-diagram.png'),
    animations: 'disabled',
  });
  await page.screenshot({
    path: path.join(artifactDir, 'step-2-review-preview.png'),
    animations: 'disabled',
  });
});
```

## Evidence Notes

- The viewport readback is an actual `window.innerWidth` / `window.innerHeight` measurement, independent of `test.use`.
- The runner must stop before either screenshot when the readback assertion fails.
- Screenshot files are runtime artifacts and must not be copied back into this fixture.
