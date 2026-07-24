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

function node() {
  return { page: null, children: new Map() };
}

function compareText(left, right) {
  return left < right ? -1 : left > right ? 1 : 0;
}

function sidebarItems(current) {
  const result = [];
  if (current.page) {
    result.push({
      text: current.page.data.title,
      link: current.page.route,
      ...(current.children.size ? {
        items: [...current.children.entries()]
          .sort(([left], [right]) => compareText(left, right))
          .flatMap(([, child]) => sidebarItems(child))
      } : {})
    });
    return result;
  }
  for (const [segment, child] of [...current.children.entries()]
    .sort(([left], [right]) => compareText(left, right))) {
    const items = sidebarItems(child);
    result.push(...(items.length ? items : [{ text: segment, items: [] }]));
  }
  return result;
}

function sectionTree(pages, section) {
  const root = node();
  for (const page of pages) {
    const relative = page.relativePath.slice(section.length + 1);
    const segments = relative.split('/');
    const file = segments.pop();
    let current = root;
    for (const segment of segments) {
      if (!current.children.has(segment)) current.children.set(segment, node());
      current = current.children.get(segment);
    }
    if (file === 'index.md') {
      current.page = page;
    } else {
      const leaf = file.replace(/\.md$/i, '');
      if (!current.children.has(leaf)) current.children.set(leaf, node());
      current.children.get(leaf).page = page;
    }
  }
  return root;
}

export function buildSidebar(pages, target) {
  const sidebar = {};
  for (const section of SECTION_ORDER) {
    const sectionPages = pages
      .filter((page) => page.relativePath.startsWith(`${section}/`))
      .filter((page) => visibleFor(page.data.visibility, target));
    const items = sidebarItems(sectionTree(sectionPages, section));
    if (items.length) {
      sidebar[`/${section}/`] = [{ text: SECTION_LABELS[section], items }];
    }
  }
  return sidebar;
}

export function renderSidebar(sidebar) {
  return `export default ${JSON.stringify(sidebar, null, 2)};\n`;
}
