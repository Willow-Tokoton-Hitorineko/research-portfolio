# Willow · 金融研究与数据作品集

精选作品的静态导航网站：已有公开作品、独立方法演示与明确贡献边界。

在线入口：https://willow-tokoton-hitorineko.github.io/research-portfolio/

## 本地查看

```sh
python -m http.server 8790 --bind 127.0.0.1
```

打开 http://127.0.0.1:8790 。网站无需安装依赖、API Key 或登录。所有正文和项目链接无需 JavaScript 即可阅读；筛选是渐进增强。

## 文件与维护

- `index.html`、`portfolio.css`、`portfolio.js`：网站与筛选。
- `projects.json`：当前公开主张清单，更新时同步 HTML 与 PDF。
- `portfolio-summary.pdf`：与公开版口径一致的四页摘要。
- `PUBLICATION.md`：发布边界与本地核查记录。

网站只提供摘要和仓库链接，不复制各作品的完整源码、研究数据库或内部证据。没有访客追踪、远程字体、金融接口或模型调用。

## 版权

本仓库网站代码与新生成的公开摘要采用 MIT；指向其他仓库的代码、第三方数据和原研究材料遵循各自权利边界。未分发公司资料、个人联系方式、原始研究截图或商业数据。


## 更新与重建

`projects.json` 是项目描述的唯一数据源，网站和 PDF 共用它。需要 Python 3.11+：

```bash
pip install -r requirements-build.txt
python tools/build.py
python tools/build.py --check
```

PDF 使用确定性生成；`--check` 在临时目录重建并检查四个生成文件是否与提交版本一致。修改描述后请提交 JSON 及生成结果，避免网站和 PDF 口径漂移。工具无联网请求，无私人路径；字体使用 ReportLab 内置 CID 字体。


## 浏览体验

网站支持关键词搜索、已有作品/独立演示筛选及三条一键阅读路线。筛选条件保存到链接中，刷新仍可恢复；没有匹配时提供清除提示。每个作品的“定位此作品”链接可直达并展开贡献与边界。所有作品在无 JavaScript 时仍可阅读。

- [AI 产品与规则工程](https://willow-tokoton-hitorineko.github.io/research-portfolio/?route=product#projects)
- [金融研究与数据方法](https://willow-tokoton-hitorineko.github.io/research-portfolio/?route=research#projects)
- [工具交付与人工复核](https://willow-tokoton-hitorineko.github.io/research-portfolio/?route=tools#projects)

`tools/portfolio.js` 是交互脚本源文件，构建时同步到根目录。真实浏览器验证搜索空结果、路线切换、链接刷新恢复和项目直达；生成文件通过一致性检查。查询词在页面 URL 中，分享前请使用公开关键词；站点不存储访客筛选记录。
