"""把 Markdown 里的图片说明文字，同步成 draw-lessons.py 里最新的白话文案。

只改「图片行」和「图解行」，不碰正文，也不碰 teaching-figure 注释。重复执行结果一致。
"""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'

tree = ast.parse((ROOT / 'scripts/draw-lessons.py').read_text(encoding='utf-8'))
lessons = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == 'LESSONS' for t in node.targets
    ):
        lessons = ast.literal_eval(node.value)
        break
if lessons is None:
    raise SystemExit('draw-lessons.py 里没找到 LESSONS')

changed = 0
missing = []
for key, _title, panels in lessons:
    if key == 'prompt':
        path = DOCS / 'prompt-writing-practice.md'
    else:
        matches = sorted(DOCS.glob(f'{key}-*.md'))
        if not matches:
            missing.append(f'{key}: 找不到章节文件')
            continue
        path = matches[0]
    text = path.read_text(encoding='utf-8')
    for i, (_kind, heading, caption, _detail) in enumerate(panels, 1):
        marker = f'<!-- teaching-figure:{key}-{i} -->'
        src = f'/images/lessons/{key}-scene-{i}.png'
        idx = text.find(marker)
        if idx < 0:
            missing.append(f'{path.name}: 缺少 {marker}')
            continue
        head, tail = text[:idx], text[idx:]
        new_alt = f'![{heading}。{caption}]({src})'
        tail, n_alt = re.subn(r'!\[[^\]]*\]\(' + re.escape(src) + r'\)', new_alt, tail, count=1)
        new_cap = f'*图解：{caption} [查看大图]({src})*'
        tail, n_cap = re.subn(
            r'\*图解：.*?\[查看大图\]\(' + re.escape(src) + r'\)\*', new_cap, tail, count=1
        )
        if not (n_alt and n_cap):
            missing.append(f'{path.name}: {marker} 后面的图片行或图解行没找到')
        changed += n_alt + n_cap
        text = head + tail
    path.write_text(text, encoding='utf-8')

print(f'更新了 {changed} 行图片说明文字。')
if missing:
    print('需要人工看的地方：')
    for item in missing:
        print(' -', item)
