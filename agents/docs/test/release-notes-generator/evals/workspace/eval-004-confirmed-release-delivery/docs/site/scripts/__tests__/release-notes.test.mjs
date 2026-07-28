import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';

test('confirmed release page keeps all evidence categories', () => {
  const text = fs.readFileSync(new URL('../../release-notes/v1.0.0.md', import.meta.url), 'utf8');
  for (const heading of ['用户可见功能', '架构与关键实现', '数据库迁移', '部署与配置', '交付资产', '升级、兼容性与风险']) {
    assert.match(text, new RegExp('## ' + heading));
  }
});
