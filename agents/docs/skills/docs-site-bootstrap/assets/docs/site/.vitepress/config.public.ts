import { defineConfig, mergeConfig } from 'vitepress';
import sidebar from './generated/sidebar.public.mjs';
import { shared } from './config.shared';

export default mergeConfig(shared, defineConfig({
  title: '公开文档',
  themeConfig: {
    nav: [
      { text: '产品', link: '/product/' },
      { text: '操作手册', link: '/manual/' },
      { text: '发布说明', link: '/release-notes/' }
    ],
    sidebar
  }
}));
