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
// 无可见 index 页的子树取子树内可见叶子的最小显式 `nav_order`，
// 使被扁平化的子树保持其内部显式顺序，而不是整体被当作无序。
function explicitOrder(page) {
  const value = page?.data?.nav_order;
  return Number.isInteger(value) && value >= 0 ? value : null;
}

function navOrder(item) {
  const page = item.page ?? item.child?.page;
  if (page) return explicitOrder(page);
  const child = item.child;
  if (child) {
    let minimum = null;
    for (const sub of [...child.children.values(), ...child.leaves.values()]) {
      // sub 为 node（含 children）时递归子树，为 page 时取其显式顺序
      const subOrder = sub.children ? navOrder({ child: sub }) : explicitOrder(sub);
      if (subOrder !== null && (minimum === null || subOrder < minimum)) {
        minimum = subOrder;
      }
    }
    return minimum;
  }
  return null;
}

function sidebarItems(current) {
  const childItems = [
    ...[...current.children.entries()].map(([key, child]) => ({ key, child })),
    ...[...current.leaves.entries()].map(([key, page]) => ({ key, page }))
  ]
    .sort((a, b) => {
      const left = navOrder(a);
      const right = navOrder(b);
      if (left !== null && right !== null) {
        return left !== right ? left - right : compareText(a.key, b.key);
      }
      if (left !== null) return -1;
      if (right !== null) return 1;
      return compareText(a.key, b.key);
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
