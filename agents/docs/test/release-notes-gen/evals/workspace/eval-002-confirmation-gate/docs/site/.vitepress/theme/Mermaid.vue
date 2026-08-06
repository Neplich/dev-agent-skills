<script lang="ts">
let sequence = 0;
</script>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import { useData } from 'vitepress';

const props = defineProps<{ code: string }>();
const { isDark } = useData();
const container = ref<HTMLDivElement>();

async function renderDiagram() {
  const target = container.value;
  if (!target) return;

  try {
    const { default: mermaid } = await import('mermaid');
    mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      theme: isDark.value ? 'dark' : 'default'
    });
    const id = `mermaid-${sequence++}`;
    const { svg } = await mermaid.render(id, props.code);
    target.classList.remove('mermaid-diagram--error');
    target.innerHTML = svg;
  } catch (error) {
    const message = document.createElement('p');
    const source = document.createElement('pre');
    const code = document.createElement('code');
    message.textContent = `Mermaid 渲染失败：${error instanceof Error ? error.message : String(error)}`;
    code.textContent = props.code;
    source.append(code);
    target.classList.add('mermaid-diagram--error');
    target.replaceChildren(message, source);
  }
}

onMounted(renderDiagram);
watch(isDark, renderDiagram);
</script>

<template><div ref="container" class="mermaid-diagram" /></template>
