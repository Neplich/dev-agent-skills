import { SECTION_ORDER, visibleFor } from './pages.mjs';

const SECTION_LABELS = {
  standards: '文档规范',
  product: '产品',
  design: '设计',
  api: 'API',
  database: '数据库',
  ops: '运维',
  'release-notes': '发布说明'
};

export function buildSidebar(pages, target) {
  const sidebar = {};
  for (const section of SECTION_ORDER) {
    const items = pages
      .filter((page) => page.relativePath.startsWith(`${section}/`))
      .filter((page) => visibleFor(page.data.visibility, target))
      .sort((left, right) => left.relativePath.localeCompare(right.relativePath, 'zh-CN'))
      .map((page) => ({ text: page.data.title, link: page.route }));
    if (items.length) {
      sidebar[`/${section}/`] = [{ text: SECTION_LABELS[section], items }];
    }
  }
  return sidebar;
}

export function renderSidebar(sidebar) {
  return `export default ${JSON.stringify(sidebar, null, 2)};\n`;
}
