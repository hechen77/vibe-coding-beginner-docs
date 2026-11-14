from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
ns=runpy.run_path(str(root/'scripts/draw-lessons.py'))
lessons=ns['LESSONS']
anchors={
'01':['## 能运行，是一个开始','## 你、甲方和 AI，各自做什么？','## 三条线索，让项目始终能解释'],
'02':['## 保存文件，为什么还不够？','## 第三步：认识 Git、备份与数据库的区别','## 第四步：先练习一次恢复'],
'03':['## 先看一个你可能遇到的场景','### 第二步：先用自然语言说明任务，再请 AI 帮你组织提示词','### 第四步：整理成可以拿去沟通的问题清单'],
'04':['## 先看一个容易误会的回复','### 第四步：给规则配上验收条件','## 需求变了，怎样处理？'],
'05':['### 第四步：准备一份按任务讲述的演示脚本','### 第三步：补齐页面状态，别只画成功画面','## 反馈怎样回到项目资料？'],
'06':['## 技术名称很多，不代表方案可靠','## 风险高的部分，先做小试验','## 把方案拆成可验证的实施顺序'],
'07':['## 为什么新会话不能只说“继续开发”？','### 第一步：整理当前有效资料','## 数据库变更：先设计迁移，再考虑执行'],
'08':['## 页面都有了，为什么还是没法用？','## 第四步：运行一次真实链路，检查四类证据','## 第五步：保存稳定节点，再进入下一个闭环'],
'09':['## 第二步：不仅检查界面，也检查后端是否拒绝','## 第四步：要求审查结论附上证据','## 第六步：修复后回归，不只重试报错位置'],
'10':['## 先别连续发送“还是不行”','## 第三步：沿着数据流逐段观察','## 第七步：带着脱敏材料求助'],
'11':['## 交付不是发一个压缩包','## 第四步：备份之后，真的恢复一次','## 第五步：按清单发布，并设置停止条件'],
'12':['## 第三步：请 AI 纠错，而不是替你完成全部理解','## 第二步：沿着一条请求跟到保存结果','## 第五步：做一次受控的小改动'],
'prompt':['## 先说人话，再整理结构','## 一张表，把脑中的想法变成可讨论的要求','## 生成的提示词，怎样判断能不能用？']}
for key,title,panels in lessons:
    p=root/'docs/prompt-writing-practice.md' if key=='prompt' else next((root/'docs').glob(key+'-*.md'))
    text=p.read_text(encoding='utf-8')
    for i,((kind,heading,caption,detail),anchor) in enumerate(zip(panels,anchors[key]),1):
        marker=f'<!-- teaching-figure:{key}-{i} -->'
        if marker in text: continue
        if anchor not in text:raise ValueError(f'{p}: missing {anchor}')
        src=f'/images/lessons/{key}-scene-{i}.png'
        extra='\n> 图中提示词仅作为示例，不建议作为实际项目中的提示词使用。\n' if kind=='ai' else ''
        figure=f'\n\n{marker}\n{extra}\n![{heading}。{caption}]({src})\n\n*图解：{caption} [查看大图]({src})*\n'
        text=text.replace(anchor+'\n',anchor+figure,1)
    p.write_text(text,encoding='utf-8')
print('Embedded 39 teaching scenes in 12 chapters and prompt practice.')
