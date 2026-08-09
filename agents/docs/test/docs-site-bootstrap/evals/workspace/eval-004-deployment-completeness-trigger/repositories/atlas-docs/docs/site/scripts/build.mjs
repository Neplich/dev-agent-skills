import { build } from 'vitepress'

const [, , variant, outDir] = process.argv
await build('.', { outDir, define: { DOCS_VARIANT: JSON.stringify(variant) } })
