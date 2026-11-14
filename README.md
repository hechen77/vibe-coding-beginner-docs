# 把项目做明白

通用 AI 辅助开发图文指南。内容源位于 `docs`，网站使用 VitePress。主线共12章，另有提示词练习、案例记录、检查模板与常见误区。

## 本地阅读与编辑

建议使用 Node.js 20 或更新的受支持版本，以及项目声明的 pnpm 版本。

```sh
pnpm install --frozen-lockfile
pnpm docs:dev
```

按终端显示的地址访问。修改 Markdown 后，开发服务器会更新页面。不要把 VitePress 开发服务器当作公网正式站点。

## 检查与构建

```sh
pnpm check
pnpm docs:build
pnpm docs:preview
```

构建产物在 `docs/.vitepress/dist`。可将该目录部署到静态托管平台，不需要专门运行后端。实际对外发布由你确认并操作，当前项目没有自动发布工作流。

若托管在域名根路径，默认配置即可；若托管在子路径，构建时设置 `SITE_BASE`，例如 `/guide/`，并检查所有页面与图片。

Windows PowerShell 示例：

```powershell
$env:SITE_BASE = '/guide/'
pnpm docs:build
```

## 内容维护约定

- 人类沟通角色使用甲方与“你”，业务账号用通用功能名称。
- 所有提示词、AI话术示例旁标明：仅作为示例，不建议作为实际项目中的提示词使用。
- 案例规则集中在案例记录页；变化要同步相关章节和验收。
- 新页面加入站点导航与路线页，再运行检查和构建。
- `public/images` 内图片以 `/images/文件名` 引用；图中关键信息应在正文有等价说明。
- `pnpm check` 只做静态一致性检查，不能代替内容审阅和浏览器检查。

## 图片与 PDF 状态

十二章及提示词专题各配有三幅分散嵌入的教学场景，共39幅，位于 `docs/public/images/lessons`。可用 `scripts/draw-lessons.py` 重绘，`scripts/embed-lessons.py` 按章节锚点嵌入（已有标记不重复添加）。图示为本地程序绘制，不是外部模型生图。每幅图提供放大链接；原来的两张SVG保留作补充。

导航、首页与浏览器图标统一引用 `docs/public/images/brand-guide.svg`。修改这一个文件即可同步三个位置。

已提供单页打印样式。整本 PDF 尚未导出与校对，不存在可下载合订版。内容审定、插图完成后再制作 PDF，以免维护两套正文。

## 写作口吻

全站按 `internal/writing-style.md` 的口吻写：先说人话，专业词第一次出现就当场解释并举例子，讲“为什么”要说清“不做会怎样”。改稿前先看那份约定，以及第 01 章。

`pnpm check` 会顺带扫一遍术语（闭环、基线、回归、R0x 等），写回“专业腔”会直接报错。

教案图的画布文字也属于正文，改动流程是：先改 `scripts/draw-lessons.py` 里的标题和说明，重跑它重画，再跑 `scripts/sync-figure-captions.py` 把 Markdown 里的图片说明同步过去。

## 本机环境说明

平铺依赖布局用于兼容当前 Windows 沙箱的目录链接解析。构建过程中 esbuild 需要启动子进程；受限环境若禁止进程通信，需要给该构建过程相应权限，不能靠反复重装解决。
