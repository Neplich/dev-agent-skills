<script setup lang="ts">
import { nextTick, onMounted, watch } from 'vue';
import { useRoute } from 'vitepress';
import mermaid from 'mermaid';

const route = useRoute();
let sequence = 0;
mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: 'default' });

async function renderMermaid() {
  await nextTick();
  const blocks = document.querySelectorAll('pre > code.language-mermaid');
  for (const code of blocks) {
    const pre = code.parentElement;
    if (!pre || pre.dataset.mermaidRendered === 'true') continue;
    const container = document.createElement('div');
    container.className = 'mermaid-diagram';
    try {
      const id = `mermaid-${sequence++}`;
      const { svg } = await mermaid.render(id, code.textContent ?? '');
      container.innerHTML = svg;
      pre.dataset.mermaidRendered = 'true';
      pre.replaceWith(container);
    } catch (error) {
      container.classList.add('mermaid-diagram--error');
      container.textContent = error instanceof Error ? error.message : String(error);
      pre.replaceWith(container);
    }
  }
}

onMounted(renderMermaid);
watch(() => route.path, renderMermaid);
</script>

<template><span class="mermaid-renderer" aria-hidden="true" /></template>
