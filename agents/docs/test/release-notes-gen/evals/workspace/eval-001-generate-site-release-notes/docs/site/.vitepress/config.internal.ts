import { defineConfig, mergeConfig } from 'vitepress';
import sidebar from './generated/sidebar.internal.mjs';
import { shared } from './config.shared';

export default mergeConfig(shared, defineConfig({
  title: '内部正式文档',
  themeConfig: {
    nav: [
      { text: '规范', link: '/standards/' },
      { text: '产品', link: '/product/' },
      { text: '设计', link: '/design/' },
      { text: 'API', link: '/api/' },
      { text: '数据库', link: '/database/' },
      { text: '运维', link: '/ops/' },
      { text: '发布说明', link: '/release-notes/' }
    ],
    sidebar
  }
}));
