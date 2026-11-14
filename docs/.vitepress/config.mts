import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: '把项目做明白',
  description: '从需求到交付，一步一步学会有依据的 AI 辅助开发。',
  base: process.env.SITE_BASE || '/',
  cleanUrls: false,
  lastUpdated: false,
  head: [['meta', { name: 'theme-color', content: '#f8f9fd' }], ['link', { rel: 'icon', type: 'image/svg+xml', href: `${process.env.SITE_BASE || '/'}images/brand-guide.svg` }]],
  themeConfig: {
    logo: { src: '/images/brand-guide.svg', alt: '把项目做明白：手册与铅笔' },
    siteTitle: '把项目做明白',
    nav: [
      { text: '开始学习', link: '/01-workflow' },
      { text: '路线与目录', link: '/roadmap' },
      { text: '提示词练习', link: '/prompt-writing-practice' },
      { text: '检查与模板', link: '/checklists' }
    ],
    sidebar: [
      { text: '从这里开始', items: [{ text: '使用说明与路线', link: '/roadmap' }, { text: '贯穿案例与规则记录', link: '/case-study' }] },
      { text: '一 · 准备与理解', items: [
        { text: '01 为什么需要开发流程', link: '/01-workflow' },
        { text: '02 工具、保存与回退', link: '/02-tools-and-recovery' },
        { text: '03 收到需求，先别写代码', link: '/03-understand-requirements' },
        { text: '04 沟通、规则与验收', link: '/04-confirm-requirements' }
      ] },
      { text: '二 · 方案与实现', items: [
        { text: '05 原型与甲方演示', link: '/05-prototype' },
        { text: '06 开发方案与风险验证', link: '/06-technical-plan' },
        { text: '07 资料、交接与操作边界', link: '/07-development-boundaries' },
        { text: '08 一次做一小段，做完就试', link: '/08-incremental-development' }
      ] },
      { text: '三 · 验证与交付', items: [
        { text: '09 测试与 AI 审查', link: '/09-testing-review' },
        { text: '10 定位、修复与求助', link: '/10-debugging' },
        { text: '11 发布、交付与维护', link: '/11-delivery' },
        { text: '12 理解代码与复盘', link: '/12-understanding-retrospective' }
      ] },
      { text: '需要时查阅', items: [
        { text: '提示词方法与四组练习', link: '/prompt-writing-practice' },
        { text: '检查清单与记录模板', link: '/checklists' },
        { text: '常见误区与止损', link: '/pitfalls' }
      ] }
    ],
    outline: { level: [2, 3], label: '本页内容' },
    docFooter: { prev: '上一节', next: '下一节' },
    sidebarMenuLabel: '学习目录',
    returnToTopLabel: '回到顶部',
    darkModeSwitchLabel: '切换外观',
    lightModeSwitchTitle: '切换浅色',
    darkModeSwitchTitle: '切换深色',
    search: { provider: 'local', options: { locales: { root: { translations: {
      button: { buttonText: '搜索内容', buttonAriaLabel: '搜索内容' },
      modal: { noResultsText: '没有找到相关内容', resetButtonTitle: '清空搜索', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } }
    } } } } },
    footer: { message: '先理解，再决定；分步实现，用证据验证。', copyright: '公开分享前请核对项目事实与最新工具能力。' }
  }
})
