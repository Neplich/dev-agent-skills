import { defineConfig, mergeConfig } from 'vitepress';
import sidebar from './generated/sidebar.public.mjs';
import navigation from './navigation.public.json';
import { shared } from './config.shared';

export default mergeConfig(shared, defineConfig({
  title: '公开文档',
  themeConfig: {
    nav: navigation,
    sidebar
  }
}));
