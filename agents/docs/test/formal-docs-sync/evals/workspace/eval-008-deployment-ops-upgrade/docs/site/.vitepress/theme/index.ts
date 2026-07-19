import { h } from 'vue';
import DefaultTheme from 'vitepress/theme';
import MermaidRenderer from './MermaidRenderer.vue';
import './custom.css';

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'layout-bottom': () => h(MermaidRenderer)
  }),
  enhanceApp({ app }) {
    app.component('MermaidRenderer', MermaidRenderer);
  }
};
