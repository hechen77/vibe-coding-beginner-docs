import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve('docs')
const errors = []
const files = fs.readdirSync(root).filter(x => x.endsWith('.md'))
const forbidden = /学生|老师|校园|同学|学校/g
let chars = 0
let images = 0
const marker = '仅作为示例，不建议作为实际项目中的提示词使用'
const jargon = /\bR0[1-9]\b|闭环|基线|颗粒度|赋能|抓手|痛点|范式|冒烟测试|幂等|解耦|门禁|受控修复|链路|上下文|契约|增量迁移|回归|对齐/g
for (const name of files) {
  const text = fs.readFileSync(path.join(root, name), 'utf8')
  chars += text.length
  if (forbidden.test(text)) errors.push(`${name}: 存在特定场景角色词`)
  forbidden.lastIndex = 0
  for (const match of text.matchAll(/!?\[[^\]]*\]\(([^)]+)\)/g)) {
    const target = match[1].split('#')[0]
    if (!target || /^(https?:|mailto:)/.test(target)) continue
    const base = target.startsWith('/images/') ? path.join(root, 'public', target.slice(1)) : path.resolve(root, target.replace(/^\//, ''))
    if (!fs.existsSync(base) && !fs.existsSync(base + '.md')) errors.push(`${name}: 缺失引用 ${target}`)
    if (match[0].startsWith('!')) images++
  }
  const lines = text.split('\n')
  lines.forEach((line, i) => {
    if (line.startsWith('> ') && /^(> )?(请|我拿到|我准备|我想|我有|你将)/.test(line)) {
      const previous = lines.slice(Math.max(0, i - 12), i).join('\n')
      if (!previous.includes(marker)) errors.push(`${name}:${i+1}: AI话术缺少临近示例说明`)
    }
  })
  if (name !== 'index.md' && !text.startsWith('# ')) errors.push(`${name}: 缺少一级标题`)
}
for (const name of fs.readdirSync(path.join(root, 'public/images')).filter(name => name.endsWith('.svg'))) {
  const text = fs.readFileSync(path.join(root, 'public/images', name), 'utf8')
  if (name.endsWith('.svg') && forbidden.test(text)) errors.push(`${name}: 图中存在特定场景词`)
  forbidden.lastIndex = 0
}
const config = fs.readFileSync(path.join(root, '.vitepress/config.mts'), 'utf8')
for (const match of config.matchAll(/link: '\/([^']+)'/g)) {
  if (!fs.existsSync(path.join(root, match[1] + '.md'))) errors.push(`导航目标缺失: ${match[1]}`)
}
for (const hit of config.matchAll(jargon)) errors.push(`config.mts: 导航文案里有术语「${hit[0]}」`)
if (errors.length) { console.error(errors.join('\n')); process.exitCode = 1 }
else console.log(`通过：${files.length}篇内容，${chars}字符，${images}处图片引用；本地链接、导航、角色词与AI话术示例标记检查正常。`)
