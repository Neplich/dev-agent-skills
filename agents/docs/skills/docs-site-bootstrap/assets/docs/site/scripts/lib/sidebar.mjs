import { SECTION_ORDER, visibleFor } from './pages.mjs';

const SECTION_LABELS = {
  standards: '文档规范',
  product: '产品',
  manual: '操作手册',
  design: '设计',
  api: 'API',
  database: '数据库',
  ops: '运维',
  'release-notes': '发布说明'
};

function node() {
  return { page: null, children: new Map(), leaves: new Map() };
}

function compareText(left, right) {
  return left < right ? -1 : left > right ? 1 : 0;
}

// Section 内排序：优先按 frontmatter `nav_order`（非负整数升序），
// 缺省、非整数或负值一律回退路径 slug 字典序。
function navOrder(item) {
  const page = item.page ?? item.child?.page;
  const value = page?.data?.nav_order;
  return Number.isInteger(value) && value >= 0 ? value : Number.MAX_SAFE_INTEGER;
}

function sidebarItems(current) {
  const childItems = [
    ...[...current.children.entries()].map(([key, child]) => ({ key, child })),
    ...[...current.leaves.entries()].map(([key, page]) => ({ key, page }))
  ]
    .sort((a, b) => {
      const order = navOrder(a) - navOrder(b);
      return order !== 0 ? order : compareText(a.key, b.key);
    })
    .flatMap(({ key, child, page }) => {
      const items = page
        ? [{ text: page.data.title, link: page.route }]
        : sidebarItems(child);
      return items.length ? items : [{ text: key, items: [] }];
    });
  const result = [];
  if (current.page) {
    result.push({
      text: current.page.data.title,
      link: current.page.route,
      ...(childItems.length ? { items: childItems } : {})
    });
    return result;
  }
  return childItems;
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
      current.leaves.set(leaf, page);
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
