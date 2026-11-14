<script setup>
import { withBase } from 'vitepress'
const chapters = [
  { num:'01', title:'先把问题问明白', en:'DISCOVER', desc:'从一句需求开始，分清事实、猜测与未知。', chapters:'第 01—03 章', link:'/01-workflow', type:'discover', color:'violet', output:'问题清单' },
  { num:'02', title:'让需求有据可依', en:'DEFINE', desc:'和甲方对齐业务规则、范围与验收条件。', chapters:'第 04 章', link:'/04-confirm-requirements', type:'define', color:'blue', output:'需求基准' },
  { num:'03', title:'把想法变成方案', en:'DESIGN', desc:'用原型讲清操作，用试验确认实现路线。', chapters:'第 05—06 章', link:'/05-prototype', type:'design', color:'cyan', output:'原型与方案' },
  { num:'04', title:'一步一步做出来', en:'BUILD', desc:'约定修改边界，每次实现一个可验证的小闭环。', chapters:'第 07—08 章', link:'/07-development-boundaries', type:'build', color:'orange', output:'可运行版本' },
  { num:'05', title:'让结果经得起检查', en:'VERIFY', desc:'测试、审查与定位，修复之后还要回归。', chapters:'第 09—10 章', link:'/09-testing-review', type:'verify', color:'green', output:'验证记录' },
  { num:'06', title:'交付，也真正掌握', en:'DELIVER', desc:'能部署、能恢复，也能解释关键逻辑。', chapters:'第 11—12 章', link:'/11-delivery', type:'deliver', color:'rose', output:'交付与复盘' }
]
const resources = [
 { title:'怎样把需求说给 AI 听？', desc:'提示词方法 · 四组表达练习', link:'/prompt-writing-practice', icon:'prompt', color:'violet' },
 { title:'开始下一步之前，查一遍', desc:'需求、交接、测试与发布清单', link:'/checklists', icon:'check', color:'blue' },
 { title:'越改越乱时，先停一下', desc:'常见误区 · 定位与止损', link:'/pitfalls', icon:'stop', color:'orange' }
]
</script>

<template>
<div class="studio-home">
  <section class="studio-intro" aria-labelledby="main-heading">
    <div class="intro-orbit"><img class="brand-guide-hero" :src="withBase('/images/brand-guide.svg')" alt="把项目做明白：手册与铅笔" width="180" height="180"></div>
    <div class="intro-label"><span></span> 一本可以边做边学的开发指南</div>
    <h1 id="main-heading">和 AI 一起，<span>把项目做明白。</span></h1>
    <p class="intro-subtitle">从理解需求到可靠交付，把每一次“做出来”变成真正的“学会了”。</p>
    <div class="intro-actions"><a :href="withBase('/01-workflow.html')" class="studio-button">开始这段实践 <span aria-hidden="true">→</span></a><a :href="withBase('/roadmap.html')" class="intro-secondary">先看看完整目录 <span aria-hidden="true">↗</span></a></div>
    <div class="intro-meta"><span>12 个章节</span><i></i><span>1 个完整案例</span><i></i><span>按自己的节奏学习</span></div>
  </section>

  <section class="studio-path" aria-labelledby="path-heading">
    <div class="path-heading"><div><span class="small-label">YOUR PROJECT JOURNEY</span><h2 id="path-heading">一个项目，六站走明白</h2></div><p>每一站，都带走一份能用的成果。</p></div>
    <div class="journey-grid">
      <a v-for="(c,index) in chapters" :key="c.num" :href="withBase(c.link+'.html')" :class="['journey-card',c.color]">
        <div class="journey-top"><span>{{ c.num }} <i>/</i> {{ c.en }}</span><span class="journey-index">{{ c.chapters }}</span></div>
        <div :class="['chapter-art',c.type]" aria-hidden="true">
          <template v-if="c.type==='discover'"><div class="art-sheet sheet-back"></div><div class="art-sheet question-sheet"><span class="mini-label">甲方的想法</span><span class="art-line wide"></span><span class="art-line"></span><span class="art-line short"></span><div class="question-pill">先问清楚 <b>?</b></div></div><span class="art-bubble bubble-one">?</span><span class="art-bubble bubble-two">!</span></template>
          <template v-else-if="c.type==='define'"><div class="art-sheet rules-sheet"><span class="mini-label">需求确认</span><div v-for="n in 3" :key="n" class="rule-row"><span>✓</span><i></i></div></div><div class="art-stamp">已确认<small>READY</small></div></template>
          <template v-else-if="c.type==='design'"><div class="wire-window"><div class="window-dots"><i></i><i></i><i></i></div><div class="wire-body"><div class="wire-sidebar"></div><div class="wire-main"><b></b><div><i></i><i></i></div><span></span></div></div></div><div class="palette-chip"><i></i><i></i><i></i></div><div class="art-cursor"></div></template>
          <template v-else-if="c.type==='build'"><div class="code-window"><div class="window-dots"><i></i><i></i><i></i><span>project / build</span></div><div class="code-lines"><div><b>01</b><i class="purple"></i><i></i></div><div><b>02</b><i class="indent"></i><i class="orange-line"></i></div><div><b>03</b><i class="indent"></i><i></i></div><div><b>04</b><i class="purple"></i></div></div></div><div class="build-chip"><span>✓</span> 一个闭环，已完成</div></template>
          <template v-else-if="c.type==='verify'"><div class="art-sheet test-sheet"><span class="mini-label">检查记录</span><div class="test-row"><span>✓</span><i></i><small>通过</small></div><div class="test-row"><span>✓</span><i></i><small>通过</small></div><div class="test-row pending"><span>!</span><i></i><small>待核实</small></div></div><div class="magnifier"><span>✓</span></div></template>
          <template v-else><div class="delivery-box"><div class="box-lid"></div><div class="box-tape"></div><span>&lt;/&gt;</span></div><div class="delivery-note"><span>✓</span><i></i><i></i></div><span class="delivery-star">✦</span></template>
        </div>
        <h3>{{ c.title }}</h3><p>{{ c.desc }}</p><div class="journey-bottom"><span><i></i>{{ c.output }}</span><span class="circle-arrow" aria-hidden="true">↗</span></div>
      </a>
    </div>
  </section>

  <section class="practice-panel">
    <div class="practice-preview" aria-hidden="true"><div class="ticket"><div class="ticket-top"><span class="ticket-icon">A</span><span>ACTIVITY<br><b>报名与审核</b></span><i>DEMO</i></div><div class="ticket-divider"></div><div class="ticket-flow"><span>提交</span><i>→</i><span>审核</span><i>→</i><span class="ticket-success">通过</span></div><div class="ticket-lines"><i></i><i></i></div></div><span class="ticket-tag">用同一个案例，串起全部步骤</span></div>
    <div class="practice-copy"><span class="small-label">贯穿全书的实践案例</span><h2>从一句“做个报名系统”，<br>开始你的第一个完整项目。</h2><p>需求怎么问，页面怎么讲，代码怎么检查？<br>跟着案例走一遍，看每一步如何成为下一步的依据。</p><a :href="withBase('/case-study.html')">认识这个案例 <span aria-hidden="true">→</span></a></div>
  </section>

  <section class="studio-tools" aria-labelledby="tools-heading"><div class="path-heading"><div><span class="small-label">KEEP THESE CLOSE</span><h2 id="tools-heading">遇到问题，来这里翻一翻</h2></div><span class="tools-note">不必记住所有内容，知道去哪里找就好。</span></div><div class="tool-grid"><a v-for="r in resources" :key="r.title" :class="['tool-item',r.color]" :href="withBase(r.link+'.html')"><div class="tool-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path v-if="r.icon==='prompt'" d="M5 5h14v10H9l-4 4V5Zm4 4h6m-6 3h4"/><path v-else-if="r.icon==='check'" d="M8 4h11v17H5V4h3Zm1-2h6v4H9V2Zm0 10 2 2 4-4m-6 8h6"/><path v-else d="m9 3-6 6v6l6 6h6l6-6V9l-6-6H9Zm3 4v6m0 4v.1"/></svg></div><div><h3>{{ r.title }}</h3><p>{{ r.desc }}</p></div><span class="tool-arrow" aria-hidden="true">↗</span></a></div></section>
  <div class="studio-footnote"><span class="footnote-mark">i</span><p>提示词均用于教学示例，不建议作为实际项目中的提示词使用。请根据真实条件组织、核实与修订。</p></div>
</div>
</template>
