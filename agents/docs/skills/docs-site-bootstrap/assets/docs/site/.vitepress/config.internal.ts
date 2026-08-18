import { defineConfig, mergeConfig } from 'vitepress';
import sidebar from './generated/sidebar.internal.mjs';
import navigation from './navigation.internal.json';
import { shared } from './config.shared';

export default mergeConfig(shared, defineConfig({
  title: '内部正式文档',
  themeConfig: {
    nav: navigation,
    sidebar
  }
}));
