from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/public/images/lessons'; OUT.mkdir(parents=True,exist_ok=True)
REG='C:/Windows/Fonts/msyh.ttc'; BOLD='C:/Windows/Fonts/msyhbd.ttc'
INK='#303448'; MUTED='#70758b'; PURPLE='#8b76c9'; BLUE='#7199c3'; GREEN='#72a38d'; ORANGE='#cc9b69'; LINE='#e4e2ee'
def font(n,b=False): return ImageFont.truetype(BOLD if b else REG,n)
def rr(box,fill,outline=None,r=18,w=2): d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=w)
def txt(x,y,s,size=26,fill=INK,b=False): d.text((x,y),s,font=font(size,b),fill=fill)
def center(x,y,s,size=26,fill=INK,b=False): d.text((x,y),s,font=font(size,b),fill=fill,anchor='mm')
def lines(x,y,s,width=440,size=25,fill=MUTED,gap=9):
    row=''; yy=y
    for ch in s:
        if ch=='\n' or d.textlength(row+ch,font=font(size))>width:
            txt(x,yy,row,size,fill); yy+=size+gap; row='' if ch=='\n' else ch
        else: row+=ch
    if row: txt(x,yy,row,size,fill)
def arrow(x,y,x2,y2,color=PURPLE):
    d.line((x,y,x2,y2),fill=color,width=4); a=math.atan2(y2-y,x2-x)
    pts=[(x2,y2),(x2-13*math.cos(a-.5),y2-13*math.sin(a-.5)),(x2-13*math.cos(a+.5),y2-13*math.sin(a+.5))]; d.polygon(pts,fill=color)
def badge(x,y,s,color=PURPLE):
    w=int(d.textlength(s,font=font(21)))+28; rr((x,y,x+w,y+35),'#ffffff',LINE,10);txt(x+14,y+4,s,21,color)
def person(x,y,label='你',color=PURPLE,point=False):
    d.ellipse((x-39,y+118,x+58,y+134),fill='#e9e8f0')
    # seated rounded silhouette and hair, no industry uniform
    rr((x-28,y+57,x+43,y+121),color,r=24)
    d.ellipse((x-22,y-2,x+38,y+63),fill='#f4d8c3',outline='#e5c4ad',width=2)
    d.pieslice((x-25,y-7,x+40,y+46),180,360,fill='#454254')
    d.ellipse((x-22,y+1,x-7,y+38),fill='#454254')
    for ex in [x-2,x+17]: d.ellipse((ex,y+27,ex+4,y+32),fill='#484353')
    d.arc((x+1,y+34,x+18,y+45),10,165,fill='#b77e71',width=2)
    d.line((x-9,y+82,x-34,y+104),fill=color,width=15)
    if point: d.line((x+31,y+81,x+79,y+58),fill=color,width=15);d.ellipse((x+72,y+48,x+88,y+64),fill='#f4d8c3')
    else: d.line((x+32,y+83,x+57,y+107),fill=color,width=15)
    center(x+9,y+155,label,22,color,True)
def robot(x,y):
    rr((x-45,y,x+45,y+88),'#ece6f8','#c6b8e3',18);rr((x-33,y+13,x+33,y+54),'#77708c',r=12)
    for ex in [x-16,x+14]:d.ellipse((ex-4,y+27,ex+4,y+37),fill='#d9f0e9')
    d.arc((x-11,y+33,x+11,y+48),10,170,fill='#d9f0e9',width=2)
    d.line((x,y-1,x,y-16),fill='#b6a8ce',width=4);d.ellipse((x-5,y-23,x+5,y-13),fill='#cdb7e8')
    center(x,y+117,'AI',22,PURPLE,True)
def bubble(x,y,s,w=300):
    rr((x,y,x+w,y+69),'white',LINE,15);d.polygon([(x+24,y+68),(x+39,y+68),(x+23,y+82)],fill='white');lines(x+15,y+15,s,w-30,23,INK,5)
def window(x,y,title,rows,accent=PURPLE,w=360):
    rr((x+5,y+8,x+w+5,y+188),'#e9e7f1',r=14);rr((x,y,x+w,y+180),'white',LINE,14)
    rr((x+1,y+1,x+w-1,y+35),'#f5f4f9',r=13)
    for i in range(3): d.ellipse((x+15+i*12,y+13,x+21+i*12,y+19),fill=['#dfb6b6','#e8d2a9','#bfd9c7'][i])
    txt(x+63,y+6,title,17,MUTED)
    for i,row in enumerate(rows):
        yy=y+49+i*37;rr((x+16,yy,x+w-16,yy+29),'#f8f7fb',r=6);txt(x+25,yy+2,row,20,accent if i==len(rows)-1 else INK)
def paper(x,y,title,rows,w=300):
    rr((x+6,y+7,x+w+6,y+166),'#eae6f2',r=12);rr((x,y,x+w,y+159),'#fff',LINE,12);txt(x+18,y+13,title,22,PURPLE,True)
    for i,row in enumerate(rows): txt(x+18,y+52+i*31,row,20,MUTED)
def database(x,y,label,color=BLUE):
    rr((x,y+18,x+100,y+105),'#edf3f9',color,6);d.ellipse((x,y,x+100,y+39),fill='#dce9f5',outline=color,width=3)
    d.arc((x,y+42,x+100,y+81),0,180,fill=color,width=2);d.arc((x,y+73,x+100,y+112),0,180,fill=color,width=2)
    center(x+50,y+141,label,21,color,True)
def mark(x,y,kind='check',color=GREEN):
    d.ellipse((x-21,y-21,x+21,y+21),fill='white',outline=color,width=3)
    if kind=='check':d.line((x-11,y,x-3,y+9,x+12,y-10),fill=color,width=4)
    elif kind=='cross':d.line((x-8,y-8,x+8,y+8),fill=color,width=3);d.line((x+8,y-8,x-8,y+8),fill=color,width=3)
    else:center(x,y-1,'?',28,color,True)
def flow(y,names,colors=None):
    colors=colors or [PURPLE]*len(names);step=780/len(names)
    for i,name in enumerate(names):
        x=110+i*step;rr((x,y,x+step-32,y+83),'white',colors[i],12);center(x+(step-32)/2,y+41,name,24,colors[i],True)
        if i<len(names)-1:arrow(x+step-23,y+41,x+step-7,y+41,colors[i])

def scene(kind,y,title,caption,detail):
    rr((40,y,960,y+400),'#ffffff',LINE,20);txt(65,y+18,title[2:] if title[:1] in '①②③' else title,28,INK,True)
    # distinct teaching scenes; canvas coordinates stay inside every panel
    if kind=='talk':
        person(145,y+125,'甲方',BLUE,True);person(840,y+125,'你',PURPLE)
        bubble(225,y+82,detail[0],520);paper(330,y+172,detail[1],detail[2:],350)
    elif kind=='ai':
        person(144,y+125);robot(838,y+155);bubble(220,y+83,detail[0],510);paper(310,y+174,detail[1],detail[2:],390)
    elif kind=='screen':
        person(137,y+125,'你',PURPLE,True);window(270,y+96,detail[0],detail[1:4],w=450)
        problem=any(word in title for word in ['失败','不能','刷新','不等于','连续','无法'])
        mark(820,y+166,'cross' if problem else 'check',ORANGE if problem else GREEN)
    elif kind=='data':
        window(100,y+105,detail[0],detail[1:3],w=330);arrow(465,y+180,586,y+180);database(643,y+116,detail[3]);mark(835,y+168,'check',GREEN)
    elif kind=='split':
        paper(106,y+100,detail[0],detail[1:3],325);paper(548,y+100,detail[3],detail[4:6],325);arrow(453,y+177,523,y+177,ORANGE)
    elif kind=='flow':
        flow(y+117,detail[:3],[PURPLE,BLUE,GREEN]);badge(155,y+230,detail[3],PURPLE);badge(520,y+230,detail[4],GREEN)
    elif kind=='backup':
        database(120,y+110,detail[0]);arrow(260,y+169,431,y+169);database(470,y+110,detail[1],GREEN);paper(653,y+108,'实际验证',detail[2:],215)
    elif kind=='limit':
        person(130,y+131,'你',PURPLE,True);paper(260,y+104,detail[0],detail[1:3],330);rr((657,y+106,855,y+240),'#fff8ed','#e7cba6',16);center(756,y+141,'先暂停',27,ORANGE,True);lines(676,y+181,detail[3],164,21,ORANGE)
    # caption sits in an independent strip so it never covers the art
    rr((61,y+351,939,y+387),'#f6f4fb',r=9);center(500,y+368,caption,22,'#77678f')

LESSONS=[
('01','开发流程：把结果和依据连起来',[
 ('screen','① 页面出来了，不等于项目完成','成功画面只能证明你看到的那一次。',['活动报名系统','页面可以打开','提交后显示成功','权限、保存仍未验证']),
 ('talk','② 先把业务讲清楚','甲方确认业务，你记录事实与未知。',['通过审核后才占名额。','当前记录','已确认：审核占名额','待确认：取消与截止规则']),
 ('flow','③ 每个阶段留下可检查的产出','先照规则做，再照说好的标准去试。',['确认规则','分步实施','实际验证','保留决定与版本','用证据判断完成'])]),
('02','保存与恢复：代码和数据是两回事',[
 ('screen','① 连续修改之后，想回到原来','覆盖保存不是版本记录。',['修改记录','报名页面改了','审核接口也改了','哪一版还能正常运行？']),
 ('split','② 代码回退，不会恢复数据库','分别保护代码、配置、数据和上传文件。',['Git版本记录','保存代码差异','找到稳定提交','数据库备份','保存数据时间点','核对范围与权限']),
 ('backup','③ 备份之后，在隔离环境恢复一次','能恢复，才是可用的恢复方案。',['测试备份','独立恢复库','核对数量','核对关联','检查业务状态'])]),
('03','澄清需求：先看见彼此的理解差异',[
 ('talk','① 一句“满了就不能报”，有多种理解','同一句话，不能靠猜测填成规则。',['人数满了，就不能报。','含义仍待确认','提交就占名额？','审核通过才占名额？']),
 ('ai','② 请 AI 把差异变成具体问题','AI帮助提问，不代替甲方回答。',['先列未知，不要开始开发。','准备问甲方','30个名额，40人申请','您希望怎样处理？']),
 ('talk','③ 带着清楚的问题，向甲方核实','记录答复来源，再整理为当前规则。',['先收申请，审核通过才占。','需求记录','答复与问题编号对应','未回答的继续保留未知'])]),
('04','需求确认：从一句回复到验收证据',[
 ('talk','① “可以取消”，还不够具体','问清条件、动作和结果。',['报名可以取消。','还缺的边界','审核通过后还能取消吗？','截止后还能取消吗？']),
 ('split','② 把确认过的规则变成检查步骤','规则有条件，验收有预期。',['已确认的示例规则','截止前可取消已通过报名','取消后释放名额','对应验收','取消前：通过数30','取消后：通过数29']),
 ('limit','③ 新要求先评估，再同步资料','甲方确认业务，不等于授权操作线上数据。',['变更候选','取消后不释放名额？','影响展示、审核和测试','评估影响，确认后更新'])]),
('05','演示原型：让甲方提前走一遍项目',[
 ('flow','① 按真实任务演示，不只介绍按钮','把前置条件、操作结果和规则讲出来。',['提交申请','后台审核','查看结果','原型是假数据','模拟行为要标明']),
 ('screen','② 展示失败和冲突，不只展示成功','状态会影响下一步能做什么。',['原型状态演示','提交中：等待结果','请求失败：明确反馈','结果未知：先查询确认']),
 ('talk','③ 反馈分清是样式，还是规则变化','规则变化要同步需求、方案和验收。',['取消前要确认，并记录时间。','反馈记录','确认弹窗：交互调整','取消时间：数据与展示'])]),
('06','技术方案：选择要有理由，风险先试验',[
 ('ai','① 技术名词很多，不代表方案适合','每增加一项依赖，都要说明用途与代价。',['为什么需要缓存和队列？','逐项核对','对应哪个已确认需求','有没有更简单的选择']),
 ('screen','② 先试验影响后续的关键条件','先定义通过标准，再执行隔离试验。',['外部登录小试验','测试账号和权限到位','成功与失败分支可观察','记录限制，不伪造通过']),
 ('flow','③ 说清楚数据怎么走，再排先后顺序','身份、权限、必填检查，要跟着功能一起做。',['输入与请求','校验与保存','查询与反馈','写清外部条件','记录试验与限制'])]),
('07','会话交接：带上资料，也带上规矩',[
 ('ai','① 只说“继续开发”，新会话可能猜错','文件放在那儿，不代表 AI 读过。',['继续做，页面在这里。','缺少关键依据','当前是哪版需求？','哪些完成，哪些没完成？']),
 ('split','② 把现在有效的资料一起交给它','旧的版本收起来，别混进去。',['当前有效资料','需求、原型、开发方案','版本、进度、已知问题','这次的范围和规矩','这次只做一小段','动大东西先说明']),
 ('limit','③ 遇到删除数据，先核对再决定','连的哪个库、有没有备份、谁同意了，缺一样先别动手。',['数据库变更分析','连接的实际环境是什么','能不能只加字段不重建','没有明确同意，不碰真数据'])]),
('08','一段一段做：每次做一小段，做完就能试',[
 ('screen','① 提示成功，刷新却找不到记录','页面上说成功，不代表真的存进去了。',['报名端','点击后显示成功','刷新后记录消失','数据其实没存进去']),
 ('data','② 让输入、检查、保存、查询串起来','身份、截止、重复这些检查，要和功能一起做。',['提交与查询','保存真实测试记录','刷新后仍能查询','测试数据']),
 ('flow','③ 检查通过，存好一版再往下做','没做完的地方写清楚，别藏在“以后优化”里。',['一小段功能','验证结果','保存版本','这次做了什么说清楚','下一步能接上'])]),
('09','测试与审查：让结论有证据',[
 ('screen','① 隐藏按钮，不代表后端拒绝了访问','权限必须检查实际请求与数据结果。',['权限检查','无权限账号发起请求','后端应拒绝访问','不能泄露数据或改变状态']),
 ('ai','② 审查报告要有位置和触发条件','Skill提供方法，能力与覆盖范围仍需核实。',['这个风险怎样复现？','要求提供依据','入口、账号与操作条件','影响、证据、未覆盖范围']),
 ('flow','③ 先核实真假，改完再把老地方试一遍','说是误报也要给依据；没做的检查要写明。',['复现核实','想清楚再改','老地方再试一遍','没发现≠没问题','记录版本与环境'])]),
('10','定位故障：先缩小未知，再修改',[
 ('screen','① 连续盲改，会把问题越改越大','没有新增证据时，先停止扩大修改。',['取消后刷新又恢复','第一次改页面','第二次又改接口','第三次想重建数据表']),
 ('flow','② 沿数据流观察，一次验证一个假设','观察、推测与确认原因要分开。',['请求发出？','数据变化？','查询一致？','保留最短复现','用证据排除假设']),
 ('split','③ 改完把老地方再试一遍，卡住就带材料求助','把密钥和个人信息遮掉，该留的线索留着。',['修复验证','原步骤不再触发','以前好用的地方没坏','脱敏求助材料','版本、日志、复现步骤','已尝试方案和结果'])]),
('11','可靠交付：能运行，也能恢复',[
 ('screen','① 本机能用，换环境却启动失败','交付需要可复现的运行说明。',['目标环境检查','缺少配置说明','运行版本不一致','外部资源没有权限']),
 ('backup','② 发布前，验证备份和恢复','恢复旧备份可能丢失之后新增的数据。',['备份时间点','隔离恢复','核对耗时','核对数据','记录损失范围']),
 ('flow','③ 按计划发布，失败按条件停止','代码回退与数据恢复分别评估。',['核对版本配置','验收并观察','交接维护','保留停止与恢复路线','不顺手修改线上系统'])]),
('12','真正掌握：解释、定位，再验证变化',[
 ('ai','① 先自己解释，再请 AI 核对','复述 AI 的讲解，不等于理解实现。',['这是我理解的数据路径。','请核对当前代码','哪些正确，哪些缺依据','指出真实入口与调用']),
 ('flow','② 沿一次请求，找到真实实现','计划中的能力，不要写进当前架构。',['页面与请求','校验与保存','结果与查询','打开关键代码核对','观察日志和测试']),
 ('split','③ 先预测影响，再做一个小改动','用预测与实际的差异，确定下一步学习。',['修改前','预计涉及哪些部分','怎样检查关联功能','修改后','实际改了哪里','验证结果与遗漏'])]),
('prompt','表达需求：把含糊形容词变成条件',[
 ('ai','① 先说清任务，不急着生成结果','自然语言就可以，先说明目标和当前阶段。',['先帮我补充条件，再整理要求。','你提供的背景','已有资料与真实限制','未知、边界、期望输出']),
 ('split','② 不同任务，补充不同的关键条件','旅行、数据分析、文案、图片各有检查重点。',['先前的模糊描述','合理旅行、深入分析','高级文案、好看图片','更可讨论的条件','预算日期、指标口径','事实证据、用途与比例']),
 ('flow','③ 复述、试用、修订，比头衔更有用','图中话术仅为示例，不建议用于实际项目。',['补充与核实','整理要求','试用并检查','未知不编成事实','检查是否偏离原意'])])
]
for key,title,panels in LESSONS:
    im=Image.new('RGB',(1000,1440),'#f7f6fb');d=ImageDraw.Draw(im)
    rr((0,0,1000,1440),'#f7f6fb',r=0)
    txt(45,26,'把项目做明白 / '+('提示词专题' if key=='prompt' else '第 '+key+' 章'),20,PURPLE,True)
    txt(43,65,title,34,INK,True)
    for i,(kind,heading,caption,detail) in enumerate(panels):
        scene(kind,127+i*417,heading,caption,detail)
        im.crop((32,119+i*417,968,535+i*417)).save(OUT/(key+'-scene-'+str(i+1)+'.png'),optimize=True)
    txt(48,1399,'教学情境图 · 规则以本章说明为准 · 练习使用虚构数据',19,MUTED)
    im.save(OUT/(key+'-story.png'),optimize=True)
print('Created',len(LESSONS),'lesson illustrations in',OUT)
