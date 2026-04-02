<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Skills_Collection-blueviolet?style=for-the-badge&logo=anthropic" alt="Claude Code Skills">
  <img src="https://img.shields.io/badge/Skills-100+-orange?style=for-the-badge" alt="100+ Skills">
  <img src="https://img.shields.io/badge/Updated-2026.04-brightgreen?style=for-the-badge" alt="Updated 2026.04">
</p>

<h1 align="center">🐙 Claude Code Skills 全景指南</h1>

<p align="center">
  <b>一站式搭建你的 AI 编程工作站 · 从入门到精通的 Skills 百科全书</b>
</p>

<p align="center">
  <a href="#-快速安装-claude-code">安装指南</a> •
  <a href="#-claude-项目目录结构">目录结构</a> •
  <a href="#-用户画像速查">用户画像</a> •
  <a href="#-skills-全景总表">Skills 总表</a> •
  <a href="#-分类详解">分类详解</a> •
  <a href="#-mcp-服务器生态">MCP 生态</a> •
  <a href="#-本仓库预装-skills">预装 Skills</a> •
  <a href="./gallery.html">可视化页面</a>
</p>

---

## 🚀 快速安装 Claude Code

> 三步搞定，开启你的 AI 编程之旅

```bash
# 1️⃣ 安装 Node.js (>= 18) — 推荐用 nvm
nvm install --lts

# 2️⃣ 全局安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 3️⃣ 启动！首次会引导你登录 Anthropic 账号
claude
```

**IDE 集成**：VS Code / JetBrains 搜索 "Claude Code" 扩展即可安装。

**安装 Skills 的方式**：
```bash
# 方式一：手动复制 —— 把 skill 的 .md 文件放到 ~/.claude/commands/ 目录
cp my-skill.md ~/.claude/commands/

# 方式二：一键安装器 —— 部分合集提供 CLI 安装
npx antigravity install <skill-name>

# 方式三：git clone —— 直接克隆仓库后按 README 指引配置
git clone https://github.com/<repo>.git
```

> 💡 **Tip**: Skills 就是放在 `~/.claude/commands/` 下的 Markdown 文件，用 `/skill-name` 即可调用。

---

## 📁 Claude 项目目录结构

> 理解 `.claude/` 目录是掌握 Claude Code 的第一步

### 项目级结构（提交到版本控制）

```
your-project/
├── CLAUDE.md                      # 📋 项目指令，每次会话自动加载
├── .mcp.json                      # 🔌 项目级 MCP 服务器配置（团队共享）
├── .claude/
│   ├── settings.json              # ⚙️ 团队共享设置：权限、Hooks、模型（提交到 git）
│   ├── settings.local.json        # 🔒 个人覆盖设置（已 gitignore）
│   ├── commands/                  # 📝 Slash 命令（.md 文件 → /command-name 调用）
│   │   └── fix-issue.md
│   ├── skills/                    # 🎯 Skills（比 commands 更强大，支持脚本和引用文件）
│   │   └── <skill-name>/
│   │       ├── SKILL.md           #    必需入口，含 YAML frontmatter
│   │       ├── scripts/           #    可选脚本
│   │       ├── references/        #    可选参考文档
│   │       └── templates/         #    可选模板
│   ├── agents/                    # 🤖 子 Agent 定义（.md 文件 + YAML frontmatter）
│   │   └── code-reviewer.md
│   ├── rules/                     # 📏 规则文件，按主题分类，可路径限定
│   │   ├── testing.md
│   │   └── frontend/
│   │       └── react.md
│   └── agent-memory/              # 🧠 子 Agent 持久化记忆
│       └── <agent-name>/
│           └── MEMORY.md
```

### 用户全局配置（`~/.claude/`）

```
~/.claude/
├── CLAUDE.md                      # 🌍 全局个人指令（所有项目生效）
├── settings.json                  # ⚙️ 默认设置
├── keybindings.json               # ⌨️ 自定义快捷键
├── commands/                      # 📝 全局 Slash 命令
├── skills/                        # 🎯 全局 Skills
├── agents/                        # 🤖 全局子 Agent
├── rules/                         # 📏 全局规则
├── projects/                      # 🧠 Auto Memory（每个项目的记忆）
│   └── <project-path>/memory/
│       └── MEMORY.md
└── sessions/                      # 📂 会话状态
```

### 关键文件说明

| 文件 | 作用 | 是否共享 |
|:---|:---|:---:|
| `CLAUDE.md` | 持久化指令，每次会话自动读取。支持层级加载和 `@path` 导入 | ✅ |
| `settings.json` | 权限、Hooks、模型、环境变量。优先级：managed > CLI > local > project > user | ✅ |
| `settings.local.json` | 个人覆盖，自动 gitignore | ❌ |
| `commands/*.md` | Slash 命令文件。文件名 = 命令名 | ✅ |
| `skills/*/SKILL.md` | 新一代 Skills 入口。支持 `$ARGUMENTS`、`` !`command` `` 动态注入 | ✅ |
| `agents/*.md` | 子 Agent 定义。可配 model、tools、memory、hooks | ✅ |
| `rules/*.md` | 规则文件。可用 `paths:` frontmatter 限定生效范围 | ✅ |
| `.mcp.json` | MCP 服务器配置。支持 `${ENV_VAR}` 注入密钥 | ✅ |

> 💡 **Commands vs Skills**：两者现在是同一机制。`commands/*.md` 是单文件命令，`skills/*/SKILL.md` 是带附件的完整 Skill。推荐新建 Skill 使用后者。

---

## 🎭 用户画像速查

每个 Skill 都标注了适用人群，方便你快速找到属于自己的装备：

| 符号 | 画像 | 说明 |
|:---:|:---|:---|
| 🌟 | **装机必备** | 通用型，人人都该装 |
| 🧑‍💻 | **全栈开发者** | 前后端、DevOps、全能选手 |
| 🔐 | **安全专家** | 渗透测试、安全审计、漏洞挖掘 |
| 🔬 | **研究员 / 数据科学家** | 学术研究、ML、数据分析 |
| 🎨 | **设计师 / 创作者** | UI/UX、图表、视觉设计 |
| 📈 | **营销 / SEO** | 搜索优化、内容营销、增长黑客 |
| 🎮 | **游戏开发者** | Unity、Godot、游戏工作室 |
| ✍️ | **写作者 / 内容创作** | 文案、翻译、小说、视频 |
| 💼 | **产品 / 商务** | PM、创业者、项目管理 |
| 🍎 | **Apple 平台开发** | iOS、macOS、Swift |
| 🐍 | **Python 开发者** | Python 生态专属 |
| 🌐 | **中文用户** | 中文本地化 / 适配 |

---

## 📊 Skills 全景总表

> 按 Star 数排序 · 标注适用人群 · 含发布日期 & 日均增速 · 点击名称直达仓库
>
> 🔥 **日增 ⭐ 含义**：= 总 Stars ÷ 仓库存在天数。数值越高，热度越猛。新仓库可能偏高，需结合存在天数判断。

### 🏆 合集 & 资源库（先看这些！）

| Skill | ⭐ Stars | 📅 发布 | 🔥 日增 | 简介 | 适用 |
|:---|---:|:---:|---:|:---|:---:|
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 133,116 | 2026-01 | 1774.9 | 最全面的 CC 框架：Skills、内存、安全、多 Agent 编排 | 🌟🧑‍💻 |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 84,095 | 2024-11 | 172.0 | 最大的 MCP 服务器合集 | 🌟 |
| [gstack](https://github.com/garrytan/gstack) | 61,842 | 2026-03 | 2688.8 | Garry Tan（YC CEO）的完整 CC 配置 | 🌟💼 |
| [awesome-claude-skills (Composio)](https://github.com/ComposioHQ/awesome-claude-skills) | 50,515 | 2025-10 | 300.7 | 精选 Claude Skills 合集，含教程和资源 | 🌟 |
| [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 35,776 | 2025-04 | 102.5 | Skills、Hooks、子 Agent、插件全收录 | 🌟🧑‍💻 |
| [agents (wshobson)](https://github.com/wshobson/agents) | 32,815 | 2025-07 | 129.7 | 多 Agent 智能编排系统 | 🧑‍💻 |
| [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | 30,008 | 2026-01 | 379.8 | 1340+ 可一键安装的 Skills，带 CLI 安装器 | 🌟 |
| [ruflo](https://github.com/ruvnet/ruflo) | 29,334 | 2025-06 | 96.2 | Agent 编排平台：多 Agent 集群、RAG 集成 | 🧑‍💻 |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | 18,381 | 2026-01 | 235.7 | 营销专用 Skills：CRO、文案、SEO、分析 | 📈 |
| [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 16,028 | 2025-07 | 64.9 | 100+ 专业子 Agent 合集 | 🧑‍💻 |
| [awesome-agent-skills (VoltAgent)](https://github.com/VoltAgent/awesome-agent-skills) | 13,811 | 2025-10 | 88.0 | 1000+ 跨平台 Agent Skills | 🌟 |
| [awesome-claude-skills (travisvn)](https://github.com/travisvn/awesome-claude-skills) | ~10k | 2025-10 | — | 精选 Skills 列表，更新频率高 | 🌟 |
| [claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) | ~9.4k | 2025-11 | — | 高级配置示例：自动激活、Hooks、Agent | 🧑‍💻 |
| [awesome-claude-skills (BehiSecc)](https://github.com/BehiSecc/awesome-claude-skills) | ~8.1k | 2025-12 | — | 又一个精选 Skills 列表 | 🌟 |

### ⚡ 高人气单项 Skills（1000+ ⭐）

| Skill | ⭐ Stars | 📅 发布 | 🔥 日增 | 简介 | 适用 |
|:---|---:|:---:|---:|:---|:---:|
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 17,892 | 2026-01 | 198.8 | Manus 风格持久化 Markdown 规划系统 | 🌟🧑‍💻 |
| [humanizer](https://github.com/blader/humanizer) | 12,073 | 2026-01 | 161.0 | 去除 AI 写作痕迹，让文本更自然 | ✍️🌟 |
| [claude-skills (alirezarezvani)](https://github.com/alirezarezvani/claude-skills) | 8,847 | 2025-10 | 53.3 | 220+ Skills 覆盖工程、营销、产品、合规 | 🌟💼 |
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 8,780 | 2026-01 | 102.1 | Google NotebookLM 非官方 Python API | 🔬🐍 |
| [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 7,932 | 2026-02 | 158.6 | 完整游戏工作室：48 AI Agent + 36 工作流 | 🎮 |
| [Understand-Anything](https://github.com/Lum1104/Understand-Anything) | 7,596 | 2026-03 | 399.8 | 将代码库转为交互式知识图谱 | 🧑‍💻🔬 |
| [claude-skills (Jeffallan)](https://github.com/Jeffallan/claude-skills) | 7,575 | 2025-10 | 45.9 | 66 个全栈开发 Skills | 🧑‍💻 |
| [refly](https://github.com/refly-ai/refly) | 7,165 | 2024-02 | 9.3 | 开源 Skill 构建器：vibe workflow 定义 Skills | 🧑‍💻 |
| [skills (slavingia)](https://github.com/slavingia/skills) | 6,089 | 2026-03 | 553.5 | 基于《极简创业》的创业 Skills | 💼 |
| [AI-Research-Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 6,012 | 2025-11 | 39.8 | AI 研究 Skills 库：变身全能研究 Agent | 🔬 |
| [claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 5,685 | 2026-01 | 65.3 | 完整配置示例：Hooks + Skills + GH Actions | 🧑‍💻 |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | 5,446 | 2026-01 | 73.6 | Humanizer 中文版 | ✍️🌐 |
| [notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | 5,423 | 2025-10 | 32.7 | CC 直连 NotebookLM，带引用支持 | 🔬 |
| [Auto-claude-code-research (ARIS)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 5,282 | 2026-03 | 220.1 | 自动化 ML 研究：跨模型审查、实验自动化 | 🔬 |
| [dev-browser](https://github.com/SawyerHood/dev-browser) | 5,281 | 2025-12 | 43.3 | 让 Agent 操作浏览器 | 🧑‍💻 |
| [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | 4,703 | 2026-02 | 106.9 | GEO 优先 SEO：AI 搜索优化 | 📈 |
| [prompt-master](https://github.com/nidhinjs/prompt-master) | 4,390 | 2026-03 | 190.9 | 为任何 AI 工具生成精准提示词 | 🌟 |
| [skills (Trail of Bits)](https://github.com/trailofbits/skills) | 4,231 | 2026-01 | 53.6 | 安全研究、漏洞检测、审计工作流 | 🔐 |
| [Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 3,983 | 2026-02 | 107.6 | 753+ 网安 Skills，MITRE ATT&CK 映射 | 🔐 |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | 3,795 | 2026-02 | 69.0 | 19 子 Skill + 12 子 Agent 全能 SEO | 📈 |
| [claude-code-guide](https://github.com/zebbern/claude-code-guide) | 3,793 | 2025-06 | 13.3 | 从入门到精通完整指南 | 🌟 |
| [Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 3,656 | 2025-12 | 36.2 | 上下文管理：Hooks + 账本 + 交接机制 | 🧑‍💻 |
| [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 3,462 | 2025-07 | 12.7 | Hooks 大师课：全面教程与示例 | 🧑‍💻 |
| [pinme](https://github.com/glitternetwork/pinme) | ~3.1k | 2026-01 | — | 一条命令部署前端 | 🧑‍💻 |
| [codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | ~2.9k | 2026-01 | — | 把代码库变成交互式 HTML 课程 | 🔬✍️ |
| [buildwithclaude](https://github.com/davepoon/buildwithclaude) | ~2.7k | 2026-02 | — | Skills + Agent + 插件一站式中心 | 🌟 |
| [godogen](https://github.com/htdt/godogen) | ~2.5k | 2026-02 | — | 从游戏描述生成完整 Godot 4 项目 | 🎮 |
| [playwright-skill](https://github.com/lackeyjb/playwright-skill) | ~2.3k | 2026-01 | — | Playwright 浏览器自动化 | 🧑‍💻 |
| [my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | ~2.1k | 2025-11 | — | 新手友好配置模板 + 记忆系统 | 🌟 |
| [claudekit-skills](https://github.com/mrgoonie/claudekit-skills) | ~1.9k | 2026-01 | — | ClaudeKit 全套强力 Skills | 🧑‍💻 |
| [mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | ~1.6k | 2025-12 | — | Excalidraw 绘图：创建、编辑、导出 | 🎨 |
| [android-reverse-engineering](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | ~1.4k | 2026-01 | — | Android 逆向工程 | 🔐 |
| [hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | ~1.3k | 2025-09 | — | 多 Agent 实时监控面板 | 🧑‍💻 |
| [videocut-skills](https://github.com/Ceeon/videocut-skills) | ~1.3k | 2026-01 | — | 视频剪辑 Agent（中文） | ✍️🌐 |
| [skill-prompt-generator](https://github.com/huangserva/skill-prompt-generator) | ~1.2k | 2026-02 | — | AI 肖像提示词生成系统 | 🎨 |
| [browserwing](https://github.com/browserwing/browserwing) | ~1.2k | 2026-01 | — | 浏览器操作转 MCP / Skill | 🧑‍💻 |
| [claude-code-mcp (steipete)](https://github.com/steipete/claude-code-mcp) | ~1.2k | 2025-10 | — | Claude Code 作为 MCP 服务器 | 🧑‍💻 |
| [awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | ~1k | 2025-12 | — | 135 Agent + 35 Skills + 42 命令 | 🌟 |

### 🌱 潜力新星（100 ~ 1000 ⭐）

| Skill | ⭐ Stars | 📅 发布 | 简介 | 适用 |
|:---|---:|:---:|:---|:---:|
| [chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill) | ~900 | 2026-02 | AI 驱动中文小说创作 | ✍️🌐 |
| [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | ~868 | 2025-12 | 抖音无水印视频提取 | 🌐✍️ |
| [seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | ~821 | 2026-01 | 20 个 SEO & GEO Skills | 📈 |
| [nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | ~798 | 2026-01 | Nothing 风格极简 UI 生成 | 🎨 |
| [context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | ~746 | 2026-01 | 提高 Agent 输出质量的上下文工程 | 🧑‍💻 |
| [learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) | ~736 | 2025-11 | AI 辅助编程中的刻意练习 | 🔬🧑‍💻 |
| [iothackbot](https://github.com/BrownFineSecurity/iothackbot) | ~717 | 2026-01 | IoT 混合渗透测试 | 🔐 |
| [dotnet-skills](https://github.com/Aaronontheweb/dotnet-skills) | ~714 | 2026-01 | .NET 专属 Skills & 子 Agent | 🧑‍💻 |
| [x-article-publisher](https://github.com/wshuyi/x-article-publisher-skill) | ~700 | 2026-02 | Markdown → X (Twitter) 发布 | ✍️📈 |
| [Axiom](https://github.com/CharlesWiltgen/Axiom) | ~698 | 2025-11 | iOS / watchOS / tvOS 战斗级 Skills | 🍎 |
| [claude-skills (jezweb)](https://github.com/jezweb/claude-skills) | ~679 | 2025-12 | Cloudflare + React + Tailwind 全栈 | 🧑‍💻 |
| [claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | ~660 | 2025-12 | 生产级 Skill 构建工具 | 🧑‍💻 |
| [anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm) | ~654 | 2026-01 | 微信/网页/YouTube → NotebookLM | 🔬🌐 |
| [claude-health](https://github.com/tw93/claude-health) | ~637 | 2026-02 | CC 配置健康检查工具 | 🧑‍💻 |
| [second-brain-skills](https://github.com/coleam00/second-brain-skills) | ~603 | 2026-01 | CC 变身第二大脑 | 🔬💼 |
| [claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | ~601 | 2026-01 | 股票投资：技术分析、策略回测 | 💼 |
| [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | ~589 | 2026-02 | AEO/GEO 优化 & 品牌可见度 | 📈 |
| [translate-book](https://github.com/deusyu/translate-book) | ~584 | 2026-01 | 并行子 Agent 翻译整本书 | ✍️🌐 |
| [tutor-skills](https://github.com/RoundTable02/tutor-skills) | ~555 | 2026-02 | PDF/代码库 → Obsidian 学习笔记 | 🔬 |
| [laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup) | ~281 | 2026-02 | Laravel 一键配置 | 🧑‍💻 |
| [awesome-claude-code (LangGPT)](https://github.com/LangGPT/awesome-claude-code) | ~210 | 2025-10 | 中文 CC 资源列表 | 🌐 |
| [awesome-claude-code-config](https://github.com/Mizoreww/awesome-claude-code-config) | ~201 | 2026-01 | 生产级配置 + 自改进循环 | 🧑‍💻 |
| [meridian](https://github.com/markmdev/meridian) | ~145 | 2026-02 | 零配置结构化工作流 | 🧑‍💻 |
| [cchooks](https://github.com/GowayLee/cchooks) | ~124 | 2026-01 | Python Hooks SDK | 🐍 |
| [secure-claude-code](https://github.com/efij/secure-claude-code) | ~100 | 2026-01 | YARA 风格安全防护 | 🔐 |

---

## 📂 分类详解

### 🌟 装机必备 — 人人该装

> 这些是 Claude Code 生态的「基础设施」，无论你是什么角色都建议配置。

**[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** `133k ⭐` `🔥 1775/天`
目前最全面的 CC 性能优化框架。包含 Skills、记忆系统、安全策略、多 Agent 编排，是整个生态的「操作系统」级项目。支持 Claude Code、Codex、Cursor 等多平台。

**[gstack](https://github.com/garrytan/gstack)** `62k ⭐` `🔥 2689/天`
Y Combinator CEO Garry Tan 的个人 CC 配置，内含 23 个预定义 Agent 角色（CEO、设计师、工程经理、QA 等），是经过实战验证的开箱即用方案。发布仅 23 天即暴涨至 62k stars。

**[antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)** `30k ⭐` `🔥 380/天`
1340+ 可安装的 Skills，自带 CLI 安装器，`npx antigravity install` 一条命令搞定。最方便的批量安装方式。

**[planning-with-files](https://github.com/OthmanAdi/planning-with-files)** `18k ⭐` `🔥 199/天` `📦 本仓库已预装`
Manus 风格的持久化 Markdown 规划系统。用文件而非记忆来做项目规划，让 Agent 的思考过程可追溯、可编辑。

**[humanizer](https://github.com/blader/humanizer)** `12k ⭐` `🔥 161/天` `📦 本仓库已预装`
让 AI 生成的文本读起来更自然。任何需要输出文本的场景都用得上。

**[prompt-master](https://github.com/nidhinjs/prompt-master)** `4.4k ⭐` `🔥 191/天` `📦 本仓库已预装`
为任何 AI 工具编写精准提示词，带上下文和记忆保持。是提高 AI 交互效率的元技能。

**[claude-code-guide](https://github.com/zebbern/claude-code-guide)** `3.8k ⭐`
从入门到精通的完整指南，覆盖命令、工作流、Agent、Skills。新手的第一站。

---

### 🧑‍💻 开发者工具箱

> 全栈开发、DevOps、代码理解、自动化部署

**[Understand-Anything](https://github.com/Lum1104/Understand-Anything)** `7.6k ⭐` `🔥 400/天`
把任何代码库变成交互式知识图谱。接手新项目时的救星，帮你快速理解架构和依赖。

**[claude-skills (Jeffallan)](https://github.com/Jeffallan/claude-skills)** `7.6k ⭐` `🔥 46/天`
66 个精选全栈 Skills，覆盖前端、后端、数据库、测试等核心开发场景。

**[refly](https://github.com/refly-ai/refly)** `7.2k ⭐`
首个开源 Skill 构建器。用 vibe workflow 定义 Skills，在 CC、Cursor、Codex 上运行。想自己造轮子的开发者必看。

**[claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase)** `5.7k ⭐` `🔥 65/天`
完整的参考配置：Hooks + Skills + Agent + GitHub Actions CI/CD 集成。学习最佳实践的好材料。

**[dev-browser](https://github.com/SawyerHood/dev-browser)** `5.3k ⭐` `🔥 43/天`
让 Agent 自主使用浏览器。调试前端、爬取数据、端到端测试都能用。

**[Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3)** `3.7k ⭐` `🔥 36/天`
解决长会话的上下文丢失问题。通过 Hooks、账本、交接机制保持连续性。

**[playwright-skill](https://github.com/lackeyjb/playwright-skill)** `2.3k ⭐`
Playwright 浏览器自动化。Claude 自主编写并执行测试脚本。

**[pinme](https://github.com/glitternetwork/pinme)** `3.1k ⭐`
一条命令部署前端项目。简单粗暴，效率拉满。

**[dotnet-skills](https://github.com/Aaronontheweb/dotnet-skills)** `714 ⭐`
.NET 生态专属 Skills，C# / ASP.NET 开发者的福音。

**[Axiom](https://github.com/CharlesWiltgen/Axiom)** `698 ⭐` 🍎
久经战斗的 iOS / iPadOS / watchOS / tvOS 开发 Skills。Apple 平台开发者必备。

**[laravel-claude-code-setup](https://github.com/laraben/laravel-claude-code-setup)** `281 ⭐`
Laravel + Claude Code 一键配置，PHP 开发者的专属入口。

---

### 🔐 安全攻防

> 渗透测试、安全审计、漏洞挖掘、合规检查

**[skills (Trail of Bits)](https://github.com/trailofbits/skills)** `4.2k ⭐` `🔥 54/天`
由知名安全公司 Trail of Bits 出品。安全研究、漏洞检测、审计工作流，专业级品质。

**[Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** `4k ⭐` `🔥 108/天`
753+ 网络安全 Skills，完整映射 MITRE ATT&CK 框架。覆盖渗透测试、DFIR、威胁情报、云安全。

**[android-reverse-engineering](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)** `1.4k ⭐`
Android 应用逆向工程支持。移动安全研究者的利器。

**[iothackbot](https://github.com/BrownFineSecurity/iothackbot)** `717 ⭐`
IoT 设备混合渗透测试工具集。物联网安全的前沿。

**[secure-claude-code](https://github.com/efij/secure-claude-code)** `100 ⭐`
YARA 风格安全防护规则：防止密钥泄露、数据外泄、提示注入、MCP 滥用。

---

### 🔬 科研 & 知识管理

> 学术研究、ML 实验、知识图谱、笔记系统

**[notebooklm-py](https://github.com/teng-lin/notebooklm-py)** `8.8k ⭐` `🔥 102/天`
Google NotebookLM 非官方 Python API。研究者用 Python 直接操作 NotebookLM。

**[AI-Research-Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs)** `6k ⭐` `🔥 40/天`
开源 AI 研究 Skills 库。把 CC 变成全能研究 Agent，论文阅读、实验设计、结果分析一条龙。

**[notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill)** `5.4k ⭐` `🔥 33/天`
CC 直接与 NotebookLM 对话，所有回答带引用出处。知识工作者梦寐以求的功能。

**[Auto-claude-code-research (ARIS)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)** `5.3k ⭐` `🔥 220/天`
睡觉时让 AI 自动做研究！跨模型审查循环、idea 发现、实验自动化。ML 研究者的神器。

**[codebase-to-course](https://github.com/zarazhangrui/codebase-to-course)** `2.9k ⭐`
把任何代码库变成精美的交互式 HTML 课程。教育者和技术作者的好帮手。

**[second-brain-skills](https://github.com/coleam00/second-brain-skills)** `603 ⭐`
把 CC 变成你的第二大脑。知识管理爱好者（PKM）必看。

**[tutor-skills](https://github.com/RoundTable02/tutor-skills)** `555 ⭐`
PDF、文档、代码库自动转化为 Obsidian 学习笔记。学生和教育者的效率工具。

**[anything-to-notebooklm](https://github.com/joeseesun/anything-to-notebooklm)** `654 ⭐`
微信文章、网页、YouTube、PDF → NotebookLM。中文用户友好。

**[learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)** `736 ⭐`
在 AI 辅助编程中加入刻意练习。不只是让 AI 写代码，还要从中学习。

---

### 📈 营销 & SEO

> 搜索优化、内容营销、增长策略

**[marketingskills](https://github.com/coreyhaines31/marketingskills)** `18k ⭐` `🔥 236/天`
营销界的「everything-claude-code」。CRO、文案、SEO、数据分析、增长工程全覆盖。

**[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** `4.7k ⭐` `🔥 107/天`
GEO 优先的 SEO 策略：AI 搜索优化、可引用度评分、AI 爬虫分析、PDF 报告。面向 AI 时代的 SEO。

**[claude-seo](https://github.com/AgriciDaniel/claude-seo)** `3.8k ⭐` `🔥 69/天`
全能 SEO 系统：19 个子 Skill + 12 个子 Agent。技术 SEO、E-E-A-T、Schema、本地 SEO。

**[seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)** `821 ⭐`
20 个 SEO & GEO Skills：关键词研究、内容写作、技术审计、排名追踪。

**[gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)** `589 ⭐`
AEO/GEO 优化：品牌可见度、竞品对标、引用分析。

**[x-article-publisher](https://github.com/wshuyi/x-article-publisher-skill)** `700 ⭐`
Markdown 一键发布到 X (Twitter) Articles。内容创作者的分发利器。

---

### 🎮 游戏开发

> 全工作室流程、引擎集成

**[Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)** `7.9k ⭐` `🔥 159/天`
完整的 AI 游戏工作室：48 个 AI Agent 角色 + 36 个工作流 Skills。模拟真实游戏公司的层级结构，从策划到美术到 QA 全链路覆盖。

**[godogen](https://github.com/htdt/godogen)** `2.5k ⭐`
输入游戏描述，输出完整 Godot 4 项目。独立游戏开发的效率革命。

---

### ✍️ 写作 & 内容创作

> 文案、翻译、小说、视频

**[humanizer](https://github.com/blader/humanizer)** `12k ⭐` `🔥 161/天`
去除 AI 写作痕迹的标杆工具。

**[Humanizer-zh](https://github.com/op7418/Humanizer-zh)** `5.4k ⭐` `🔥 74/天`
Humanizer 中文版。中文写作者必备。

**[chinese-novelist-skill](https://github.com/PenglongHuang/chinese-novelist-skill)** `900 ⭐`
AI 驱动的中文小说创作，支持多章节、悬念节奏控制。

**[translate-book](https://github.com/deusyu/translate-book)** `584 ⭐`
用并行子 Agent 翻译整本书（PDF/DOCX/EPUB），效率极高。

**[videocut-skills](https://github.com/Ceeon/videocut-skills)** `1.3k ⭐`
视频剪辑 Agent，中文友好。

---

### 💼 产品 & 商务

> 创业、产品管理、金融

**[skills (slavingia)](https://github.com/slavingia/skills)** `6.1k ⭐` `🔥 554/天`
Gumroad 创始人 Sahil Lavingia 基于《极简创业》的 Skills。独立创业者的实战经验结晶。发布仅 11 天增速极猛。

**[claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)** `601 ⭐`
股票投资全套：市场分析、技术图表、经济日历、筛选器、策略回测。

**[pm-claude-code-setup](https://github.com/aakashg/pm-claude-code-setup)** `81 ⭐`
产品经理专用配置，即开即用。

---

### 🎨 设计 & 可视化

> UI 设计、图表、架构图

**[mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)** `1.6k ⭐`
Excalidraw 集成：AI 创建、编辑、导出手绘风格图表。

**[nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill)** `798 ⭐`
Nothing 品牌的极简设计语言：单色、排版优先、工业感。

**[skill-prompt-generator](https://github.com/huangserva/skill-prompt-generator)** `1.2k ⭐`
AI 肖像提示词生成系统，带自学习能力。

---

### 🔧 Hooks 生态

> 自定义 Claude Code 行为的利器

| 项目 | Stars | 说明 |
|:---|:---:|:---|
| [claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 3.5k | Hooks 大师课 |
| [hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | 1.3k | 多 Agent 监控 |
| [claude-code-hooks (karanb192)](https://github.com/karanb192/claude-code-hooks) | 315 | 拿来即用的 Hooks |
| [voice-hooks (shanraisshan)](https://github.com/shanraisshan/claude-code-hooks) | 233 | 语音交互 Hooks |
| [ccproxy](https://github.com/starbaser/ccproxy) | 193 | 请求拦截 / 模型路由 |
| [cchooks](https://github.com/GowayLee/cchooks) | 124 | Python Hooks SDK |
| [cc-hooks-ts](https://github.com/sushichan044/cc-hooks-ts) | 37 | TypeScript Hooks SDK |

---

## 🔌 MCP 服务器生态

> MCP (Model Context Protocol) 让 Claude Code 连接外部工具和数据源

| MCP 服务器 | ⭐ Stars | 📅 发布 | 🔥 日增 | 用途 | 适用 |
|:---|---:|:---:|---:|:---|:---:|
| [playwright-mcp (Microsoft)](https://github.com/microsoft/playwright-mcp) | 30,153 | 2025-03 | 79.8 | 浏览器自动化 | 🧑‍💻 |
| [github-mcp-server](https://github.com/github/github-mcp-server) | 28,489 | 2025-03 | 72.1 | GitHub 操作 | 🌟 |
| [fastmcp](https://github.com/PrefectHQ/fastmcp) | 24,227 | 2024-11 | 49.5 | 快速构建 MCP 服务器 | 🐍 |
| [serena](https://github.com/oraios/serena) | ~22k | 2025-06 | — | 代码语义检索 | 🧑‍💻 |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | 14,108 | 2025-02 | 34.1 | Figma 设计稿 → 代码 | 🎨🧑‍💻 |
| [genai-toolbox (Google)](https://github.com/googleapis/genai-toolbox) | ~14k | 2025-04 | — | 数据库 MCP | 🧑‍💻 |
| [pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server) | ~11k | 2025-08 | — | 多模型协作 | 🧑‍💻 |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | ~11k | 2025-05 | — | Chrome 浏览器控制 | 🧑‍💻 |
| [mcp (AWS)](https://github.com/awslabs/mcp) | ~8.7k | 2025-06 | — | AWS 服务集成 | 🧑‍💻 |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | ~8.1k | 2025-04 | — | Ghidra 逆向工程 | 🔐 |
| [git-mcp](https://github.com/idosal/git-mcp) | ~7.9k | 2025-05 | — | 消除代码幻觉 | 🌟 |
| [firecrawl-mcp](https://github.com/firecrawl/firecrawl-mcp-server) | ~5.9k | 2025-06 | — | 网页抓取 & 搜索 | 🔬 |
| [DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | ~5.8k | 2025-04 | — | 终端控制 & 文件系统 | 🧑‍💻 |
| [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | ~5.5k | 2025-05 | — | WhatsApp 消息 | 💼 |
| [XcodeBuildMCP (Sentry)](https://github.com/getsentry/XcodeBuildMCP) | ~5k | 2025-07 | — | Xcode 构建 | 🍎 |
| [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | ~5k | 2025-08 | — | Windows 桌面控制 | 🧑‍💻 |
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | ~4.8k | 2025-04 | — | Jira + Confluence | 💼 |
| [magic-mcp (21st-dev)](https://github.com/21st-dev/magic-mcp) | ~4.6k | 2025-06 | — | 前端组件生成 | 🎨🧑‍💻 |

---

## 📦 本仓库预装 Skills

> 克隆本仓库后，以下 Skills 开箱即用！

本仓库 `.claude/` 目录已预装 3 个装机必备 Skills：

```
.claude/
├── commands/
│   ├── humanizer.md              # ✍️ 去除 AI 写作痕迹（/humanizer）
│   ├── plan-with-files.md        # 📋 Manus 风格规划（/plan-with-files）
│   ├── plan-start.md             # ▶️ 开始规划（/plan-start）
│   └── plan-status.md            # 📊 查看规划状态（/plan-status）
└── skills/
    ├── planning-with-files/      # 📋 完整规划系统
    │   ├── SKILL.md
    │   ├── examples.md
    │   ├── reference.md
    │   ├── scripts/              # 初始化 & 检查脚本
    │   └── templates/            # 任务计划 & 进度模板
    └── prompt-master/            # 🎯 AI 提示词大师
        ├── SKILL.md
        └── references/           # 模式 & 模板参考
```

**使用方式**：
```bash
# 克隆仓库
git clone https://github.com/hauser-zhang/claude-skills-review.git
cd claude-skills-review

# 复制到你的全局配置（永久生效）
cp -r .claude/commands/* ~/.claude/commands/
cp -r .claude/skills/* ~/.claude/skills/

# 或者直接在此项目中使用
claude  # 启动后输入 /humanizer 等命令即可
```

---

## 🗺️ 新手路线图

```
第 1 步：安装 Claude Code
  ↓
第 2 步：选装一个合集（推荐 gstack 或 antigravity）
  ↓
第 3 步：按你的角色选 2~3 个专项 Skills
  ↓
第 4 步：配置 1~2 个常用 MCP 服务器（GitHub、Playwright）
  ↓
第 5 步：学习 Hooks，定制你的工作流
  ↓
🚀 你已经是 Claude Code 高手了！
```

---

## 📝 贡献

欢迎提交 Issue 或 PR 补充更多优质 Skills！

---

<p align="center">
  <sub>Made with ❤️ for the Claude Code community · 数据更新于 2026 年 4 月</sub>
</p>
