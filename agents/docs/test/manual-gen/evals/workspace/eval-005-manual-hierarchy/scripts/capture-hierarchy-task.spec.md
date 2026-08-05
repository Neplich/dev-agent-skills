# Hierarchy Task Capture

## Runtime Preconditions

- Run this Playwright Test snippet only inside the isolated eval scratch workspace.
- Set `MANUAL_EVAL_ARTIFACT_DIR` to that scratch workspace's screenshot directory.
- The script gathers operation-level evidence; platform and business hierarchy labels must be derived from host evidence rather than this filename.

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

test('capture a reproducible anonymous diagram task', async ({ page }) => {
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
  await page.screenshot({
    path: path.join(artifactDir, 'step-1-locate-editor.png'),
    animations: 'disabled',
  });

  await editor.click();
  await page.keyboard.press(process.platform === 'darwin' ? 'Meta+A' : 'Control+A');
  await page.keyboard.type('sequenceDiagram\n  User->>System: Create diagram\n  System-->>User: Render preview');

  const renderedDiagram = page.locator('svg').filter({ has: page.locator('g') }).last();
  await expect(renderedDiagram).toBeVisible();
  await page.screenshot({
    path: path.join(artifactDir, 'step-2-confirm-rendered-result.png'),
    animations: 'disabled',
  });
});
```

## Evidence Notes

- The two captures support a numbered operation and its visible expected result; they do not prescribe the host's business taxonomy.
- The viewport readback must pass before either screenshot is produced.
- Screenshot files are runtime artifacts and must not be copied back into this fixture.
