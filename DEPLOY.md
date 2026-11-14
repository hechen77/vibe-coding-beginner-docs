# 把站点发到网上

这份文档讲怎么把「把项目做明白」放到公网上，让别人拿到一个网址就能打开。

推荐用 Cloudflare Pages：免费、不需要绑银行卡、不需要备案、自带 HTTPS。

站点现在很小（构建后约 5 MB，132 个文件），任何免费额度都够用。**真正的风险不是流量，是读者所在网络能不能打开**，这一点只能发布后实测。

## 发布之前先确认三件事

在项目根目录执行：

```sh
pnpm install --frozen-lockfile
pnpm check
pnpm docs:build
```

`pnpm check` 会检查图片链接、术语用词和提示词说明标记；构建产物在 `docs/.vitepress/dist`。

## 方式一：接了 Git 自动构建（推荐）

好处是以后改完内容只要推一次代码，网站自己重新发布，不用手动上传。

### 第 1 步：把项目放进 GitHub

项目现在还没有版本管理。在项目根目录执行：

```sh
git init
git add .
git commit -m "初始版本：AI 辅助开发指南"
```

然后在 GitHub 上新建一个**私有或公开**的仓库，按页面提示把本地代码推上去。

推之前先看一眼 `git status`，确认没有把密钥、`.cache`、`node_modules` 提交进去——`.gitignore` 已经排除了这些，但第一次提交值得检查一遍。

### 第 2 步：在 Cloudflare 建一个 Pages 项目

1. 注册并登录 Cloudflare（免费，不需要填支付方式）。
2. 左侧找到 **Workers & Pages**，选 **Create** → **Pages** → **Connect to Git**。
3. 授权访问刚才那个仓库。
4. 构建配置按下面填：

| 项目 | 填什么 |
| --- | --- |
| Framework preset | VitePress（没有这个选项就选 None） |
| Build command | `pnpm docs:build` |
| Build output directory | `docs/.vitepress/dist` |
| 根目录 | 留空（项目就在仓库根） |

5. 环境变量里加一条 `NODE_VERSION`，值填 `22`。（项目里也有 `.nvmrc`，两处一致就不会因为 Node 版本闹脾气。）

### 第 3 步：等构建，拿网址

第一次构建通常一两分钟。成功后会给一个 `项目名.pages.dev` 的网址，直接就能打开。

之后每次推代码到默认分支，它都会自动重新构建。

## 方式二：直接传构建结果（不想碰 Git）

不想弄 GitHub 的话，这条路最短：本地构建好，把成品文件夹传上去。代价是每次改完都得自己重新传一遍。

1. 本地执行 `pnpm docs:build`。
2. Cloudflare 里选 **Create** → **Pages** → **Upload assets**。
3. 把 `docs/.vitepress/dist` 这个文件夹整个拖进去。
4. 发布，拿网址。

生成的文件夹可以直接拖，不用先压缩。以后更新重复第 1、3 步即可，注意别只传改动的单个文件。

## 方式三：退回 GitHub Pages

如果 Cloudflare 那边卡住了，GitHub Pages 也能用，而且同样免费、不绑卡。

1. 仓库 **Settings → Pages → Build and deployment → Source** 选 **GitHub Actions**。
2. 新建 `.github/workflows/deploy.yml`。注意两处和默认模板不一样：
   - 构建命令用 `pnpm docs:build`，并在前面加一步安装 pnpm；
   - **环境变量 `SITE_BASE` 必须设成 `/你的仓库名/`**。

第 2 点是最容易翻车的地方。GitHub Pages 的项目页地址是 `https://用户名.github.io/仓库名/`，属于子路径。不设 `SITE_BASE` 的话，图片和内部链接会全部 404——页面能打开，图全是破的。

这个项目已经支持用环境变量控制路径前缀（`docs/.vitepress/config.mts` 里的 `base` 读的是 `SITE_BASE`），所以工作流里加一行就行：

```yaml
      - name: Build with VitePress
        run: pnpm docs:build
        env:
          SITE_BASE: /你的仓库名/
```

## 发布后自己验一遍

别急着把链接发出去，先确认这几件事：

- [ ] 首页能打开，左上角图标正常显示。
- [ ] 侧边栏点得动，进任意一章都有内容。
- [ ] 章节里的三张教学图都显示出来了（图片最容易因为路径前缀出错）。
- [ ] 搜索框能搜到内容（比如搜「回退」）。
- [ ] 手机打开一遍，字不挤、图不溢出。
- [ ] 让别人用他自己的网络打开一次——国内访问境外服务，个体差异很大，只有实测才知道。

如果图片打不开、但文字正常，八成是路径前缀没配对，回去看上面「方式三」的第 2 点。

## 关于以后绑自己的域名

不着急做。等网址发出去、确实有稳定读者了再考虑。

需要注意：Cloudflare 买域名（Registrar）是要绑银行卡的，但**用自己的域名不必须用 Cloudflare 买**——在别处买的域名也能加进来，一样免费用它的 HTTPS。域名本身每年几十块钱，这是唯一的持续成本。

## 顺带说一句 PDF

对国内读者来说，发一个 PDF 文件往往比发网址更可靠：不用等加载，也不用担心打不开。

网站适合随时更新，PDF 适合传播和离线阅读。等正文定稿了再做一份，两套东西各管一头。
