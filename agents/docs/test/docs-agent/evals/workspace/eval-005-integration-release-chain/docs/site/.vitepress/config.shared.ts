import { defineConfig } from 'vitepress';

export const shared = defineConfig({
  lang: 'zh-CN',
  title: '正式文档',
  description: '面向当前稳定状态的正式文档站',
  cleanUrls: true,
  markdown: { lineNumbers: true },
  themeConfig: {
    search: { provider: 'local' },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一页', next: '下一页' },
    sidebarMenuLabel: '目录',
    returnToTopLabel: '返回顶部'
  }
});
