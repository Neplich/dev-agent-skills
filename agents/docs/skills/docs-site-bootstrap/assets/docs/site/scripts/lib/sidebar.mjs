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

// Section 内排序：显式声明 `nav_order`（非负整数）的页面按值升序、
// 始终排在无 `nav_order` 的页面之前；无序页面之间回退路径 slug 字典序。
// 存在性优先，因此任意合法 `nav_order` 取值都不会与「无序」混淆。
function explicitOrder(page) {
  const value = page?.data?.nav_order;
  return Number.isInteger(value) && value >= 0 ? value : null;
}

// 无可见 index 页的子树扁平化到当前层参与排序，使其叶子的显式顺序
// 与同层条目按同一 comparator 混合，而不是整体作为不可分的块。
function flattenIndexless(child) {
  const items = [];
  for (const [key, sub] of child.children.entries()) {
    if (sub.page) {
      items.push({ key, child: sub });
    } else {
      items.push(...flattenIndexless(sub));
    }
  }
  for (const [key, page] of child.leaves.entries()) {
    items.push({ key, page });
  }
  return items;
}

function sidebarItems(current) {
  const childItems = [];
  for (const [key, child] of current.children.entries()) {
    if (child.page) {
      childItems.push({ key, child });
    } else {
      childItems.push(...flattenIndexless(child));
    }
  }
  for (const [key, page] of current.leaves.entries()) {
    childItems.push({ key, page });
  }
  const items = childItems
    .sort((a, b) => {
      const left = explicitOrder(a.page ?? a.child?.page);
      const right = explicitOrder(b.page ?? b.child?.page);
      if (left !== null && right !== null) {
        return left !== right ? left - right : compareText(a.key, b.key);
      }
      if (left !== null) return -1;
      if (right !== null) return 1;
      return compareText(a.key, b.key);
    })
    .flatMap(({ key, child, page }) => {
      const childItems = page
        ? [{ text: page.data.title, link: page.route }]
        : sidebarItems(child);
      return childItems.length ? childItems : [{ text: key, items: [] }];
    });
  const result = [];
  if (current.page) {
    result.push({
      text: current.page.data.title,
      link: current.page.route,
      ...(items.length ? { items } : {})
    });
    return result;
  }
  return items;
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
